#!/usr/bin/env python3
"""Valida o contrato e a matriz de trabalho DATA1-BX sem autorizar migração."""
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "migration" / "data1bx_contract.json"

EXPECTED_SOURCE_FIELDS = [
    "data_product_types",
    "visualization_types",
    "data_sources",
    "temporal_resolution",
    "access_conditions",
]
EXPECTED_RULES = {
    "field_level_confidence_required_when_value_present",
    "blank_value_requires_unresolved_field",
    "carried_forward_is_not_external_verification",
    "official_confirmation_requires_https_evidence_date_and_reviewer",
    "confirmed_record_requires_no_unresolved_fields",
    "resource_ids_must_match_canonical_order",
    "automatic_migration_forbidden",
}


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def split_values(value: str, separator: str) -> list[str]:
    return [item.strip() for item in value.split(separator) if item.strip()]


def is_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def is_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return len(value) == 10


contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

if contract.get("phase") != "DATA1-BX":
    fail("fase do contrato deve ser DATA1-BX")
if contract.get("status") != "population_pending":
    fail("contrato inicial deve permanecer em population_pending")
if contract.get("expected_records") != 51:
    fail("contrato deve exigir 51 registros")
if contract.get("preserve_resource_ids") is not True:
    fail("contrato deve preservar resource_id")
if contract.get("automatic_migration_allowed") is not False:
    fail("DATA1-BX não pode autorizar migração automática")
if set(contract.get("rules", [])) != EXPECTED_RULES:
    fail("regras do contrato DATA1-BX estão incompletas ou divergentes")

dimensions = contract.get("dimensions", [])
source_fields = [item.get("source_field") for item in dimensions]
if source_fields != EXPECTED_SOURCE_FIELDS:
    fail("as cinco dimensões DATA1-BX devem aparecer na ordem contratada")
if len({item.get("proposal_column") for item in dimensions}) != len(dimensions):
    fail("proposal_column duplicada no contrato")
if len({item.get("confidence_column") for item in dimensions}) != len(dimensions):
    fail("confidence_column duplicada no contrato")

context_columns = contract.get("required_context_columns", [])
expected_context = [
    "bx_review_status",
    "bx_evidence_basis",
    "bx_evidence_url",
    "bx_last_verified",
    "bx_reviewer",
    "bx_unresolved_fields",
    "bx_notes",
]
if context_columns != expected_context:
    fail("colunas de contexto DATA1-BX divergentes")

canonical_path = ROOT / contract["canonical_csv"]
base_matrix_path = ROOT / contract["base_matrix"]
target_matrix_path = ROOT / contract["target_matrix"]

source_columns, source_rows = read_csv(canonical_path)
_, base_rows = read_csv(base_matrix_path)
target_columns, target_rows = read_csv(target_matrix_path)

if len(source_columns) != 34:
    fail(f"CSV canônico deve permanecer com 34 campos; encontrados {len(source_columns)}")
if len(source_rows) != 51:
    fail(f"CSV canônico deve permanecer com 51 fontes; encontradas {len(source_rows)}")
if len(base_rows) != 51:
    fail(f"matriz DATA1-B deve permanecer com 51 fontes; encontradas {len(base_rows)}")
if not all(field in source_columns for field in source_fields):
    fail("CSV canônico não contém todas as cinco dimensões DATA1-BX")

expected_header = ["resource_id"]
for item in dimensions:
    expected_header.extend([item["proposal_column"], item["confidence_column"]])
expected_header.extend(context_columns)
if target_columns != expected_header:
    fail("cabeçalho da matriz DATA1-BX diverge do contrato")
if len(target_rows) != 51:
    fail(f"matriz DATA1-BX deve conter 51 linhas; encontradas {len(target_rows)}")

source_ids = [row["resource_id"] for row in source_rows]
base_ids = [row["resource_id"] for row in base_rows]
target_ids = [row["resource_id"] for row in target_rows]
if source_ids != base_ids or source_ids != target_ids:
    fail("DATA1-BX deve preservar exatamente a ordem e os IDs do CSV canônico")
if len(set(target_ids)) != 51:
    fail("matriz DATA1-BX contém resource_id duplicado")

allowed_confidence = set(contract["confidence_values"])
allowed_status = set(contract["review_status_values"])
allowed_basis = set(contract["evidence_basis_values"])
separator = contract["unresolved_separator"]
field_set = set(source_fields)
status_counts: Counter[str] = Counter()

for line, row in enumerate(target_rows, start=2):
    status = row["bx_review_status"].strip()
    basis = row["bx_evidence_basis"].strip()
    evidence_url = row["bx_evidence_url"].strip()
    verified = row["bx_last_verified"].strip()
    reviewer = row["bx_reviewer"].strip()
    unresolved = split_values(row["bx_unresolved_fields"], separator)

    if status not in allowed_status:
        fail(f"linha {line}: bx_review_status inválido")
    if basis not in allowed_basis:
        fail(f"linha {line}: bx_evidence_basis inválido")
    if len(unresolved) != len(set(unresolved)):
        fail(f"linha {line}: bx_unresolved_fields contém duplicatas")
    if any(field not in field_set for field in unresolved):
        fail(f"linha {line}: bx_unresolved_fields contém campo desconhecido")

    proposals: dict[str, str] = {}
    confidences: dict[str, str] = {}
    for item in dimensions:
        field = item["source_field"]
        proposal = row[item["proposal_column"]].strip()
        confidence = row[item["confidence_column"]].strip()
        proposals[field] = proposal
        confidences[field] = confidence

        if confidence and confidence not in allowed_confidence:
            fail(f"linha {line}: confiança inválida em {field}")
        if proposal and not confidence:
            fail(f"linha {line}: proposta em {field} exige confiança por campo")
        if confidence and not proposal:
            fail(f"linha {line}: confiança em {field} exige proposta")
        if not proposal and field not in unresolved:
            fail(f"linha {line}: campo vazio {field} deve permanecer em bx_unresolved_fields")

    if evidence_url and not is_https(evidence_url):
        fail(f"linha {line}: bx_evidence_url deve ser HTTPS")
    if verified and not is_iso_date(verified):
        fail(f"linha {line}: bx_last_verified deve usar YYYY-MM-DD")

    if basis == "none" and any([evidence_url, verified, reviewer]):
        fail(f"linha {line}: evidence basis none não aceita metadados de evidência")
    if basis == "official_documentation" and not all([evidence_url, verified, reviewer]):
        fail(f"linha {line}: documentação oficial exige URL, data e revisor")

    if status == "não_iniciado":
        if any(proposals.values()) or any(confidences.values()):
            fail(f"linha {line}: não_iniciado não pode conter propostas")
        if set(unresolved) != field_set:
            fail(f"linha {line}: não_iniciado deve manter as cinco dimensões pendentes")
        if basis != "none":
            fail(f"linha {line}: não_iniciado exige evidence basis none")

    elif status == "carregado_do_csv":
        if not all(proposals.values()):
            fail(f"linha {line}: carregado_do_csv exige cinco valores copiados")
        if set(confidences.values()) != {"desconhecida"}:
            fail(f"linha {line}: carregado_do_csv deve usar confiança desconhecida")
        if set(unresolved) != field_set:
            fail(f"linha {line}: valores carregados continuam pendentes de verificação")
        if basis != "canonical_csv":
            fail(f"linha {line}: carregado_do_csv exige evidence basis canonical_csv")
        if any([evidence_url, verified, reviewer]):
            fail(f"linha {line}: carregar do CSV não equivale a evidência externa")

    elif status == "revisão_manual":
        if not unresolved:
            fail(f"linha {line}: revisão_manual exige ao menos uma dimensão pendente")
        if basis == "none" and any(proposals.values()):
            fail(f"linha {line}: propostas em revisão exigem base de evidência explícita")

    elif status == "confirmado_documentação_oficial":
        if not all(proposals.values()) or not all(confidences.values()):
            fail(f"linha {line}: confirmação oficial exige cinco propostas e confianças")
        if unresolved:
            fail(f"linha {line}: confirmação oficial não aceita campos pendentes")
        if basis != "official_documentation":
            fail(f"linha {line}: confirmação oficial exige evidence basis official_documentation")
        if not all([evidence_url, verified, reviewer]):
            fail(f"linha {line}: confirmação oficial exige URL, data e revisor")

    status_counts[status] += 1

print(
    "OK: contrato e matriz DATA1-BX validados — "
    f"51 fontes; {status_counts['não_iniciado']} não iniciadas; "
    f"{status_counts['carregado_do_csv']} carregadas do CSV; "
    f"{status_counts['revisão_manual']} em revisão; "
    f"{status_counts['confirmado_documentação_oficial']} confirmadas; "
    "CSV 0.7.0 e matriz DATA1-B preservados; migração automática bloqueada"
)
