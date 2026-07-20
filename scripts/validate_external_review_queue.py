#!/usr/bin/env python3
"""Valida a fila consolidada DATA1-BR-CLOSE contra os cinco lotes versionados."""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "migration" / "external_review_queue_contract.json"
SEPARATOR = " | "
EXPECTED_HEADER = [
    "priority_rank", "priority_tier", "priority_score", "resource_id",
    "resource_name", "source_batch", "batch_rank", "impact_level",
    "scientific_risk_level", "link_role_status", "access_documentation_status",
    "risk_flag_count", "review_dimension_count", "review_focus", "queue_status",
    "evidence_url_used", "reviewer", "reviewed_at", "decision", "decision_notes",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        fail(f"arquivo ausente: {path.relative_to(ROOT)}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(SEPARATOR) if item.strip()]


def priority_tier(score: int) -> str:
    if score >= 90:
        return "P0"
    if score >= 82:
        return "P1"
    if score >= 74:
        return "P2"
    return "P3"


def main() -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if contract.get("phase") != "DATA1-BR-CLOSE":
        fail("contrato deve identificar DATA1-BR-CLOSE")
    if contract.get("expected_records") != 35:
        fail("fila deve conter 35 fontes")

    registry_path = ROOT / contract["batch_registry"]
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    active = registry.get("active_batches", [])
    active_names = [entry.get("batch") for entry in active]
    expected_batches = contract["expected_source_batches"]
    if active_names != expected_batches:
        fail("fila somente fecha com BR1–BR5 ativos na ordem planejada")

    source_rows: dict[str, dict[str, str]] = {}
    for entry in active:
        header, rows = read_csv(ROOT / entry["review_matrix"])
        if "resource_id" not in header or len(rows) != 7:
            fail(f"{entry['batch']}: matriz inválida")
        for row in rows:
            resource_id = row["resource_id"]
            if resource_id in source_rows:
                fail(f"ID repetido entre lotes: {resource_id}")
            row = dict(row)
            row["source_batch"] = entry["batch"]
            source_rows[resource_id] = row
    if len(source_rows) != 35:
        fail("BR1–BR5 devem fornecer 35 IDs únicos")

    _, data1b_rows = read_csv(ROOT / registry["data1b_matrix"])
    manual_ids = {
        row["resource_id"] for row in data1b_rows
        if row["migration_status"] == "revisão_manual"
    }
    if set(source_rows) != manual_ids or len(manual_ids) != 35:
        fail("fila deve corresponder exatamente aos 35 casos revisão_manual")

    audit = json.loads((ROOT / contract["link_role_audit"]).read_text(encoding="utf-8"))
    same_pending_ids = {
        item["resource_id"] for item in audit.get("records_requiring_review", [])
        if item.get("status") == "same_destination_pending_review"
    }
    role_flags = set(contract["role_review_flags"])
    scope_ids = set(contract["scope_decision_required_ids"])
    weights = contract["priority_weights"]

    expected: list[dict[str, object]] = []
    for resource_id, source in source_rows.items():
        flags = split_values(source["risk_flags"])
        dimensions = split_values(source["review_dimensions"])
        if resource_id in same_pending_ids:
            link_status = "same_destination_pending_review"
        elif role_flags.intersection(flags):
            link_status = "role_review_required"
        else:
            link_status = "separate_destinations"
        access_status = "documentada" if source["existing_access_documentation_url"].strip() else "ausente"
        score = (
            weights["impact_level"][source["impact_level"]]
            + weights["scientific_risk_level"][source["scientific_risk_level"]]
            + min(len(flags), weights["risk_flag_count"]["maximum"])
            + min(len(dimensions), weights["review_dimension_count"]["maximum"])
            + weights["link_role_status"][link_status]
            + (weights["missing_access_documentation"] if access_status == "ausente" else 0)
            + (weights["scope_decision_required"] if resource_id in scope_ids else 0)
        )
        expected.append({
            "resource_id": resource_id,
            "resource_name": source["resource_name"],
            "source_batch": source["source_batch"],
            "batch_rank": source["selection_rank"],
            "impact_level": source["impact_level"],
            "scientific_risk_level": source["scientific_risk_level"],
            "link_role_status": link_status,
            "access_documentation_status": access_status,
            "risk_flag_count": str(len(flags)),
            "review_dimension_count": str(len(dimensions)),
            "priority_score": score,
            "priority_tier": priority_tier(score),
        })

    expected.sort(key=lambda item: (
        -int(item["priority_score"]),
        str(item["source_batch"]),
        int(str(item["batch_rank"])),
        str(item["resource_id"]),
    ))

    queue_header, queue_rows = read_csv(ROOT / contract["queue"])
    if queue_header != EXPECTED_HEADER:
        fail("cabeçalho da fila diverge do contrato")
    if len(queue_rows) != 35 or len({row["resource_id"] for row in queue_rows}) != 35:
        fail("fila deve conter 35 IDs únicos")

    comparison_fields = [
        "resource_id", "resource_name", "source_batch", "batch_rank",
        "impact_level", "scientific_risk_level", "link_role_status",
        "access_documentation_status", "risk_flag_count",
        "review_dimension_count", "priority_tier",
    ]
    for rank, (row, expected_row) in enumerate(zip(queue_rows, expected), start=1):
        if row["priority_rank"] != str(rank):
            fail(f"linha {rank + 1}: priority_rank incorreto")
        if row["priority_score"] != str(expected_row["priority_score"]):
            fail(f"linha {rank + 1}: priority_score incorreto")
        for field in comparison_fields:
            if row[field] != str(expected_row[field]):
                fail(f"linha {rank + 1}: {field} diverge da fonte versionada")
        if len([item for item in row["review_focus"].split(";") if item.strip()]) < 4:
            fail(f"linha {rank + 1}: review_focus insuficiente")
        if row["queue_status"] != "aguardando_evidência_oficial":
            fail(f"linha {rank + 1}: status inicial inválido")
        if any(row[field].strip() for field in ("evidence_url_used", "reviewer", "reviewed_at")):
            fail(f"linha {rank + 1}: fila inicial não aceita evidência, revisor ou data")
        if row["decision"] != "manter_csv_atual":
            fail(f"linha {rank + 1}: decisão inicial deve preservar o CSV")
        if not row["decision_notes"].strip():
            fail(f"linha {rank + 1}: decision_notes obrigatório")
        if row["resource_id"] in scope_ids and "escopo" not in row["decision_notes"].casefold():
            fail(f"linha {rank + 1}: decisão de escopo não registrada")

    tier_counts = Counter(row["priority_tier"] for row in queue_rows)
    if dict(tier_counts) != contract["expected_tier_counts"]:
        fail(f"contagem por prioridade divergente: {dict(tier_counts)}")

    canonical_header, canonical_rows = read_csv(ROOT / contract["canonical_csv"])
    if len(canonical_header) != 34 or len(canonical_rows) != 51:
        fail("DATA1-BR-CLOSE não pode alterar o CSV canônico 51 × 34")

    print(
        "OK: DATA1-BR-CLOSE validado — 35 fontes priorizadas; "
        "P0=7, P1=10, P2=11, P3=7; ordem reproduzível; "
        "evidência externa pendente; CSV 51 × 34 preservado"
    )


if __name__ == "__main__":
    main()
