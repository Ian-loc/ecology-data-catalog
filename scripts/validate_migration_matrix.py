#!/usr/bin/env python3
"""Valida a matriz DATA1-B contra o CSV canônico e o contrato 0.8.0."""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "data_resources.csv"
MATRIX_PATH = ROOT / "migration" / "data1b_migration_matrix.csv"
SCHEMA_PATH = ROOT / "schema" / "v0.8.0-draft.json"

MATRIX_COLUMNS = [
    "resource_id",
    "resource_type_proposed",
    "geographic_scope_proposed",
    "data_formats_proposed",
    "access_protocols_proposed",
    "access_tools_proposed",
    "institutional_status_proposed",
    "citation_guidance_url_proposed",
    "confidence",
    "migration_status",
    "rationale",
    "exceptions",
]
CONFIDENCE = {"alta", "média", "baixa"}
EXCEPTION_CODES = {
    "other_documented_requires_manual_confirmation",
    "global_non_geographic_resource",
}
PLACEHOLDERS = {"unknown", "not_applicable", "varies_by_dataset"}


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split("|") if item.strip()]


def is_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
source_columns, source_rows = read_csv(CSV_PATH)
matrix_columns, matrix_rows = read_csv(MATRIX_PATH)

if len(source_columns) != 34:
    fail(f"CSV canônico deve permanecer com 34 campos no DATA1-B; encontrados {len(source_columns)}")
if len(source_rows) != 51:
    fail(f"CSV canônico deve permanecer com 51 fontes; encontradas {len(source_rows)}")
if matrix_columns != MATRIX_COLUMNS:
    fail("cabeçalho da matriz diferente do contrato DATA1-B")
if len(matrix_rows) != 51:
    fail(f"matriz deve conter 51 decisões; encontradas {len(matrix_rows)}")

source_by_id = {row["resource_id"]: row for row in source_rows}
source_ids = [row["resource_id"] for row in source_rows]
matrix_ids = [row["resource_id"] for row in matrix_rows]
if len(source_by_id) != 51:
    fail("CSV canônico contém resource_id duplicado")
if matrix_ids != source_ids:
    fail("matriz deve preservar exatamente a ordem e os 51 resource_id do CSV")
if len(set(matrix_ids)) != 51:
    fail("matriz contém resource_id duplicado")

allowed_types = set(schema["new_fields"]["resource_type"]["values"])
allowed_scopes = set(schema["new_fields"]["geographic_scope"]["values"])
allowed_formats = set(schema["controlled_values"]["data_formats"])
allowed_protocols = set(schema["controlled_values"]["access_protocols"])
allowed_status = set(schema["controlled_values"]["institutional_status"])
tool_prefixes = tuple(schema["new_fields"]["access_tools"]["value_prefixes"])

for line, proposal in enumerate(matrix_rows, start=2):
    rid = proposal["resource_id"]
    source = source_by_id[rid]

    if proposal["resource_type_proposed"] not in allowed_types:
        fail(f"linha {line}: resource_type inválido")
    if proposal["geographic_scope_proposed"] not in allowed_scopes:
        fail(f"linha {line}: geographic_scope inválido")

    formats = split_values(proposal["data_formats_proposed"])
    protocols = split_values(proposal["access_protocols_proposed"])
    tools = split_values(proposal["access_tools_proposed"])
    statuses = split_values(proposal["institutional_status_proposed"])
    exceptions = split_values(proposal["exceptions"])

    if not formats or not set(formats).issubset(allowed_formats):
        fail(f"linha {line}: data_formats_proposed inválido")
    if not protocols or not set(protocols).issubset(allowed_protocols):
        fail(f"linha {line}: access_protocols_proposed inválido")
    if not statuses or not set(statuses).issubset(allowed_status):
        fail(f"linha {line}: institutional_status_proposed inválido")
    if any(not tool.startswith(tool_prefixes) for tool in tools):
        fail(f"linha {line}: access_tools_proposed contém prefixo inválido")
    if any(code not in EXCEPTION_CODES for code in exceptions):
        fail(f"linha {line}: código de exceção desconhecido")

    for field_name, values in (("formatos", formats), ("protocolos", protocols)):
        if PLACEHOLDERS.intersection(values) and len(values) > 1:
            fail(f"linha {line}: placeholder combinado com valor positivo em {field_name}")

    confidence = proposal["confidence"]
    if confidence not in CONFIDENCE:
        fail(f"linha {line}: confiança inválida")
    expected_status = "revisão_manual" if confidence != "alta" or exceptions else "pronto_para_migração"
    if proposal["migration_status"] != expected_status:
        fail(f"linha {line}: migration_status incompatível com confiança e exceções")
    if not proposal["rationale"].strip():
        fail(f"linha {line}: justificativa vazia")

    citation_url = proposal["citation_guidance_url_proposed"].strip()
    if citation_url and not is_https(citation_url):
        fail(f"linha {line}: citation_guidance_url_proposed deve ser HTTPS ou vazio")

    if proposal["resource_type_proposed"] == "publishing_software":
        if proposal["geographic_scope_proposed"] != "not_applicable":
            fail(f"linha {line}: publishing_software exige geographic_scope not_applicable")
        if source["covers_brazil"] != "não se aplica":
            fail(f"linha {line}: publishing_software exige covers_brazil não se aplica")

    if proposal["geographic_scope_proposed"] == "not_applicable" and source["covers_brazil"] != "não se aplica":
        fail(f"linha {line}: geographic_scope not_applicable contradiz covers_brazil")

    if proposal["geographic_scope_proposed"] == "global" and source["covers_brazil"] not in {"sim", "parcial"}:
        if "global_non_geographic_resource" not in exceptions:
            fail(f"linha {line}: escopo global sem cobertura do Brasil exige exceção documentada")

    positive_access = [value for value in protocols if value not in {"unknown", "not_applicable"}] or tools
    if source["programmatic_access"] == "sim" and not positive_access:
        fail(f"linha {line}: acesso programático sim exige protocolo ou ferramenta")
    if source["programmatic_access"] == "não" and [value for value in protocols if value not in {"unknown", "not_applicable"}]:
        fail(f"linha {line}: acesso programático não contradiz protocolo positivo")

    has_other_documented = (
        "other_documented" in formats
        or "other_documented" in protocols
        or any(tool.startswith("other_documented") for tool in tools)
    )
    if has_other_documented:
        if "other_documented_requires_manual_confirmation" not in exceptions:
            fail(f"linha {line}: other_documented exige exceção e revisão manual")
        if proposal["migration_status"] != "revisão_manual":
            fail(f"linha {line}: other_documented não pode ser migrado automaticamente")

confidence_counts = Counter(row["confidence"] for row in matrix_rows)
status_counts = Counter(row["migration_status"] for row in matrix_rows)
type_counts = Counter(row["resource_type_proposed"] for row in matrix_rows)
scope_counts = Counter(row["geographic_scope_proposed"] for row in matrix_rows)

if confidence_counts["baixa"]:
    fail("matriz contém decisão de baixa confiança; resolver antes da integração")
if status_counts["pronto_para_migração"] == 0 or status_counts["revisão_manual"] == 0:
    fail("matriz deve distinguir decisões prontas e decisões para revisão manual")

print(
    "OK: matriz DATA1-B validada — "
    f"51 fontes; {confidence_counts['alta']} alta confiança; "
    f"{confidence_counts['média']} confiança média; "
    f"{status_counts['pronto_para_migração']} prontas; "
    f"{status_counts['revisão_manual']} para revisão manual; "
    f"{len(type_counts)} tipos; {len(scope_counts)} escalas; CSV 0.7.0 preservado"
)
