#!/usr/bin/env python3
"""Valida seleção, rastreabilidade e bloqueios do lote DATA1-BR/BR1."""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "migration" / "br1_contract.json"
SEPARATOR = " | "

EXPECTED_HEADER = [
    "resource_id",
    "resource_name",
    "selection_rank",
    "impact_level",
    "scientific_risk_level",
    "risk_flags",
    "selection_rationale",
    "internal_consistency_status",
    "internal_findings",
    "existing_verification_url",
    "existing_access_documentation_url",
    "review_dimensions",
    "external_review_status",
    "evidence_url_used",
    "reviewer",
    "reviewed_at",
    "decision",
    "notes",
]

EXPECTED_RULES = {
    "exactly_seven_records_in_fixed_order",
    "all_records_must_exist_in_canonical_csv",
    "all_records_must_be_manual_review_in_data1b",
    "all_records_must_preserve_unknown_field_confidence_in_data1bx_until_external_review",
    "existing_evidence_urls_must_match_canonical_csv",
    "blocked_external_review_forbids_evidence_reviewer_and_date",
    "blocked_external_review_requires_hold_current_csv",
    "no_canonical_csv_changes_without_current_official_evidence",
    "selection_does_not_equal_validation",
}


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(SEPARATOR) if item.strip()]


def valid_https_or_blank(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def valid_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return len(value) == 10


contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

if contract.get("phase") != "DATA1-BR" or contract.get("batch") != "BR1":
    fail("contrato deve identificar DATA1-BR/BR1")
if contract.get("status") != "internal_audit_complete_external_review_blocked":
    fail("estado BR1 deve registrar auditoria interna concluída e revisão externa bloqueada")
if contract.get("expected_records") != 7:
    fail("BR1 deve conter exatamente sete fontes")
if contract.get("automatic_csv_changes_allowed") is not False:
    fail("BR1 não pode autorizar alteração automática do CSV")
if set(contract.get("rules", [])) != EXPECTED_RULES:
    fail("regras do contrato BR1 estão incompletas ou divergentes")

expected_ids = contract.get("expected_resource_ids", [])
if len(expected_ids) != 7 or len(set(expected_ids)) != 7:
    fail("expected_resource_ids deve conter sete IDs únicos")

canonical_header, canonical_rows = read_csv(ROOT / contract["canonical_csv"])
_, data1b_rows = read_csv(ROOT / contract["data1b_matrix"])
_, data1bx_rows = read_csv(ROOT / contract["data1bx_matrix"])
review_header, review_rows = read_csv(ROOT / contract["review_matrix"])

if len(canonical_header) != 34 or len(canonical_rows) != 51:
    fail("CSV canônico deve permanecer em 51 fontes × 34 campos")
if review_header != EXPECTED_HEADER:
    fail("cabeçalho da matriz BR1 diverge do contrato")
if len(review_rows) != 7:
    fail("matriz BR1 deve conter sete linhas")
if [row["resource_id"] for row in review_rows] != expected_ids:
    fail("matriz BR1 deve preservar IDs e ordem definidos no contrato")

canonical = {row["resource_id"]: row for row in canonical_rows}
data1b = {row["resource_id"]: row for row in data1b_rows}
data1bx = {row["resource_id"]: row for row in data1bx_rows}

allowed_flags = set(contract["risk_flags"])
allowed_dimensions = set(contract["review_dimensions"])
allowed_impact = set(contract["impact_levels"])
allowed_risk = set(contract["scientific_risk_levels"])
allowed_internal = set(contract["internal_consistency_values"])
allowed_external = set(contract["external_review_status_values"])
allowed_decisions = set(contract["decision_values"])

for expected_rank, row in enumerate(review_rows, start=1):
    line = expected_rank + 1
    resource_id = row["resource_id"].strip()

    if resource_id not in canonical or resource_id not in data1b or resource_id not in data1bx:
        fail(f"linha {line}: {resource_id} ausente em uma matriz de origem")
    if row["resource_name"].strip() != canonical[resource_id]["resource_name"].strip():
        fail(f"linha {line}: nome não corresponde ao CSV canônico")
    if row["selection_rank"].strip() != str(expected_rank):
        fail(f"linha {line}: selection_rank deve seguir a ordem do contrato")

    if row["impact_level"] not in allowed_impact:
        fail(f"linha {line}: impact_level inválido")
    if row["scientific_risk_level"] not in allowed_risk:
        fail(f"linha {line}: scientific_risk_level inválido")
    if row["internal_consistency_status"] not in allowed_internal:
        fail(f"linha {line}: internal_consistency_status inválido")
    if row["external_review_status"] not in allowed_external:
        fail(f"linha {line}: external_review_status inválido")
    if row["decision"] not in allowed_decisions:
        fail(f"linha {line}: decision inválida")

    flags = split_values(row["risk_flags"])
    dimensions = split_values(row["review_dimensions"])
    if len(flags) < 2 or len(flags) != len(set(flags)) or not set(flags).issubset(allowed_flags):
        fail(f"linha {line}: risk_flags inválidos ou insuficientes")
    if len(dimensions) < 5 or len(dimensions) != len(set(dimensions)) or not set(dimensions).issubset(allowed_dimensions):
        fail(f"linha {line}: review_dimensions inválidas ou insuficientes")

    for field in ("selection_rationale", "internal_findings", "notes"):
        if not row[field].strip():
            fail(f"linha {line}: {field} não pode ficar vazio")

    verification_url = row["existing_verification_url"].strip()
    access_url = row["existing_access_documentation_url"].strip()
    if not valid_https_or_blank(verification_url) or not valid_https_or_blank(access_url):
        fail(f"linha {line}: URLs existentes devem ser HTTPS ou vazias")
    if verification_url != canonical[resource_id]["verification_url"].strip():
        fail(f"linha {line}: existing_verification_url diverge do CSV")
    if access_url != canonical[resource_id]["access_documentation_url"].strip():
        fail(f"linha {line}: existing_access_documentation_url diverge do CSV")

    if data1b[resource_id]["migration_status"] != "revisão_manual":
        fail(f"linha {line}: fonte BR1 deve estar em revisão_manual na DATA1-B")
    if data1bx[resource_id]["bx_review_status"] != "carregado_do_csv":
        fail(f"linha {line}: fonte BR1 deve permanecer carregada do CSV na DATA1-BX")
    if data1bx[resource_id]["bx_evidence_basis"] != "canonical_csv":
        fail(f"linha {line}: DATA1-BX deve manter base canonical_csv")

    confidence_fields = [field for field in data1bx[resource_id] if field.endswith("_confidence")]
    if not confidence_fields or any(data1bx[resource_id][field] != "desconhecida" for field in confidence_fields):
        fail(f"linha {line}: DATA1-BX deve preservar confiança desconhecida")

    if row["external_review_status"] == "bloqueada_sem_web":
        if any(row[field].strip() for field in ("evidence_url_used", "reviewer", "reviewed_at")):
            fail(f"linha {line}: revisão bloqueada não aceita evidência, revisor ou data")
        if row["decision"] != "manter_csv_atual":
            fail(f"linha {line}: revisão bloqueada deve manter o CSV atual")
    else:
        if row["evidence_url_used"] and not valid_https_or_blank(row["evidence_url_used"].strip()):
            fail(f"linha {line}: evidence_url_used deve ser HTTPS")
        if row["reviewed_at"] and not valid_iso_date(row["reviewed_at"].strip()):
            fail(f"linha {line}: reviewed_at deve usar YYYY-MM-DD")

print(
    "OK: BR1 validado — 7 fontes selecionadas; auditoria interna registrada; "
    "revisão externa bloqueada; CSV 51 × 34 e confiança DATA1-BX preservados"
)
