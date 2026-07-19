#!/usr/bin/env python3
"""Valida o workflow de correções críticas sem alterar o catálogo canônico."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / "QUALITY_CORRECTION_WORKFLOW.md"
IMPLEMENTATION_PATH = ROOT / "IMPLEMENTATION_WORKFLOW.md"
STATUS_PATH = ROOT / "WORKFLOW_STATUS.md"
SELECTION_PATH = ROOT / "SELECTION_AND_COVERAGE_POLICY.md"
SCHEMA_PATH = ROOT / "schema" / "v0.8.0-draft.json"
CSV_PATH = ROOT / "data" / "data_resources.csv"
CITATION_PATH = ROOT / "CITATION.cff"
READINESS_PATH = ROOT / "release" / "doi_readiness.json"

EXPECTED_RULES = {
    "publishing_software_requires_not_applicable_geography",
    "global_scope_normally_covers_brazil",
    "not_applicable_scope_requires_not_applicable_brazil",
    "programmatic_yes_requires_protocol_or_tool",
    "programmatic_no_forbids_positive_protocol_without_exception",
    "authentication_yes_requires_access_condition",
    "free_download_yes_requires_data_access_url",
    "formats_must_not_contain_protocols_or_visualizations",
    "visualizations_must_not_contain_formats_or_protocols",
    "protocols_must_not_contain_client_tools",
    "citation_guidance_url_must_be_https",
    "multivalued_items_must_be_unique_and_trimmed",
    "academic_evidence_doi_is_not_source_identifier",
    "placeholders_must_not_coexist_with_positive_values",
}
REQUIRED_CYCLES = [
    "QC0", "SELECT1", "DATA1-BX", "DATA1-BR", "DATA1-C", "DATA1-D",
    "DATA2", "UX5", "RELEASE2", "DOI", "RES1", "EDU1",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def require_cycle_order(text: str, filename: str) -> None:
    positions: list[int] = []
    for cycle in REQUIRED_CYCLES:
        marker = f"| {cycle} |"
        position = text.find(marker)
        if position < 0:
            fail(f"{filename} não contém ciclo obrigatório: {cycle}")
        positions.append(position)
    if positions != sorted(positions):
        fail(f"ordem operacional dos ciclos está divergente em {filename}")


for path in (
    WORKFLOW_PATH, IMPLEMENTATION_PATH, STATUS_PATH, SELECTION_PATH,
    SCHEMA_PATH, CSV_PATH, CITATION_PATH, READINESS_PATH,
):
    if not path.exists():
        fail(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")

schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
rules = schema.get("cross_validation_rules", [])
if len(rules) != 14 or len(set(rules)) != 14 or set(rules) != EXPECTED_RULES:
    fail("contrato 0.8.0 não contém exatamente as 14 regras aprovadas")

workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
implementation = IMPLEMENTATION_PATH.read_text(encoding="utf-8")
status = STATUS_PATH.read_text(encoding="utf-8")
require_cycle_order(workflow, "QUALITY_CORRECTION_WORKFLOW.md")
require_cycle_order(implementation, "IMPLEMENTATION_WORKFLOW.md")

for token in (
    "não bloqueante para v1.0.0 e DOI",
    "data/product_resolution_examples.csv",
    "não é cientificamente seguro inferir resolução",
    "página didática",
    "Checkpoints de reordenação",
    "nenhuma nova fonte entra diretamente no catálogo",
):
    if token not in workflow:
        fail(f"workflow sem requisito: {token}")

for token in (
    "DATA1-BX antes de BR1",
    "Novas fontes permanecem fora do CSV",
    "RES1 e EDU1",
):
    if token not in status:
        fail(f"WORKFLOW_STATUS.md sem estado crítico: {token}")

selection = SELECTION_PATH.read_text(encoding="utf-8")
for section in (
    "Critérios mínimos de inclusão",
    "Critérios de exclusão",
    "Duplicidade e relação entre recursos",
    "Candidatos",
    "Matriz de lacunas",
    "Critérios de prioridade para expansão",
):
    if section not in selection:
        fail(f"política de seleção sem seção: {section}")

with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
    reader = csv.reader(handle)
    header = next(reader)
    rows = list(reader)
if len(header) != 34 or len(rows) != 51:
    fail("workflow crítico não pode alterar o CSV 0.7.0 de 51 × 34")

citation = CITATION_PATH.read_text(encoding="utf-8")
match = re.search(r'^version:\s*["\']?([^"\'\s]+)', citation, re.MULTILINE)
if not match or match.group(1) != "0.7.0":
    fail("versão formal deve permanecer 0.7.0")

readiness = json.loads(READINESS_PATH.read_text(encoding="utf-8"))
if readiness.get("doi_allowed") is not False:
    fail("DOI deve permanecer bloqueado")

print(
    "OK: correções de qualidade validadas — 14 regras alinhadas; "
    "seleção documentada; SELECT1 e DATA1-BX precedem BR1; "
    "RES1 e EDU1 não bloqueantes; CSV 51 × 34 e versão 0.7.0 preservados"
)
