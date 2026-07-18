#!/usr/bin/env python3
"""Valida o CSV canônico e gera o JSON consumido pelo site."""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "data_resources.csv"
JSON_PATH = ROOT / "data" / "data_resources.json"
REQUIRED_COLUMNS = [
    "resource_id", "resource_name", "acronym", "official_identity", "description",
    "homepage_url", "data_access_url", "thematic_domains", "data_product_types",
    "data_formats", "geographic_coverage", "spatial_resolution", "temporal_coverage",
    "temporal_resolution", "data_sources", "free_download", "access_conditions",
    "api_available", "api_documentation_url", "license", "institutional_status",
    "owner_or_manager", "academic_uses", "limitations", "verification_url",
    "last_verified",
]
REQUIRED_VALUES = [
    "resource_id", "resource_name", "official_identity", "description", "homepage_url",
    "thematic_domains", "geographic_coverage", "free_download", "access_conditions",
    "api_available", "license", "owner_or_manager", "academic_uses", "limitations",
    "verification_url", "last_verified",
]
DOWNLOAD_VALUES = {"sim", "parcial", "não", "desconhecido", "não se aplica"}
API_VALUES = {"sim", "não", "desconhecido"}
DATE_RE = re.compile(r"^20\d{2}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^DR\d{4}$")

def is_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)

def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")

with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    if reader.fieldnames != REQUIRED_COLUMNS:
        fail("cabeçalho diferente do esquema documentado")
    rows = list(reader)

if not rows:
    fail("CSV sem registros")

seen_ids: set[str] = set()
seen_names: set[str] = set()
for line, row in enumerate(rows, start=2):
    missing = [field for field in REQUIRED_VALUES if not row[field].strip()]
    if missing:
        fail(f"linha {line}: campos obrigatórios vazios: {', '.join(missing)}")
    resource_id = row["resource_id"].strip()
    if not ID_RE.fullmatch(resource_id):
        fail(f"linha {line}: resource_id inválido: {resource_id}")
    if resource_id in seen_ids:
        fail(f"linha {line}: resource_id duplicado: {resource_id}")
    seen_ids.add(resource_id)
    name_key = row["resource_name"].strip().casefold()
    if name_key in seen_names:
        fail(f"linha {line}: nome duplicado: {row['resource_name']}")
    seen_names.add(name_key)
    for field in ("homepage_url", "verification_url"):
        if not is_https(row[field].strip()):
            fail(f"linha {line}: {field} deve ser URL HTTPS")
    for field in ("data_access_url", "api_documentation_url"):
        value = row[field].strip()
        if value and value != "não se aplica" and not is_https(value):
            fail(f"linha {line}: {field} deve ser URL HTTPS, vazio ou 'não se aplica'")
    if row["free_download"] not in DOWNLOAD_VALUES:
        fail(f"linha {line}: free_download inválido")
    if row["api_available"] not in API_VALUES:
        fail(f"linha {line}: api_available inválido")
    if not DATE_RE.fullmatch(row["last_verified"]):
        fail(f"linha {line}: last_verified deve usar AAAA-MM-DD")

expected_ids = [f"DR{i:04d}" for i in range(1, len(rows) + 1)]
if sorted(seen_ids) != expected_ids:
    fail("IDs devem ser contínuos de DR0001 até o último registro")

JSON_PATH.write_text(
    json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"OK: {len(rows)} fontes validadas; JSON gerado em {JSON_PATH.relative_to(ROOT)}")
