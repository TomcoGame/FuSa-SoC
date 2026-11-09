#!/usr/bin/env python3
"""Validate starter assurance registers. Structural checks only, not standards compliance."""
import csv
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REGISTERS = {
    "02-risk/hazards.csv": ("id", "title", "status"),
    "03-requirements/requirements.csv": ("id", "title", "source", "status", "allocated_to"),
    "05-analyses/analyses.csv": ("id", "type", "status", "related_requirement"),
    "06-verification/tests.csv": ("id", "title", "requirement_id", "status"),
    "07-evidence/evidence.csv": ("id", "title", "source_revision", "configuration", "tool_version", "result", "artifact_path", "sha256", "status"),
    "08-safety-case/claims.csv": ("id", "claim", "requirement_id", "evidence_id", "status"),
    "09-assessment/findings.csv": ("id", "title", "status"),
}
ALLOWED = {"draft", "planned", "in_progress", "verified", "rejected", "closed"}
errors, records, all_ids = [], {}, set()
for path, required in REGISTERS.items():
    with (BASE / path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        for col in required:
            if col not in headers:
                errors.append(f"{path}: missing column {col}")
        rows = list(reader)
    records[path] = rows
    for n, row in enumerate(rows, 2):
        rid = (row.get("id") or "").strip()
        if not rid or rid in all_ids:
            errors.append(f"{path}:{n}: blank or duplicate id {rid!r}")
        all_ids.add(rid)
        if (row.get("status") or "") not in ALLOWED:
            errors.append(f"{path}:{n}: invalid status")
        for col in required:
            if col in ("id", "status"):
                continue
            if col not in ("source_revision", "configuration", "tool_version", "result", "artifact_path", "sha256", "evidence_id", "allocated_to") and not (row.get(col) or "").strip():
                errors.append(f"{path}:{n}: missing {col}")

hazards = {r["id"] for r in records["02-risk/hazards.csv"]}
reqs = {r["id"] for r in records["03-requirements/requirements.csv"]}
evidence = {r["id"] for r in records["07-evidence/evidence.csv"]}
for r in records["03-requirements/requirements.csv"]:
    if r["source"] not in hazards:
        errors.append(f"{r['id']}: unknown hazard {r['source']}")
for file, col in (("05-analyses/analyses.csv", "related_requirement"),
                  ("06-verification/tests.csv", "requirement_id"),
                  ("08-safety-case/claims.csv", "requirement_id")):
    for r in records[file]:
        if r[col] not in reqs:
            errors.append(f"{r['id']}: unknown requirement {r[col]}")
for file in ("05-analyses/analyses.csv", "06-verification/tests.csv", "08-safety-case/claims.csv"):
    for r in records[file]:
        eid = (r.get("evidence_id") or "").strip()
        if eid and eid not in evidence:
            errors.append(f"{r['id']}: unknown evidence {eid}")
        if r["status"] == "verified" and not eid:
            errors.append(f"{r['id']}: verified without evidence")
for r in records["07-evidence/evidence.csv"]:
    if r["status"] == "verified":
        for field in ("source_revision", "configuration", "tool_version", "result", "artifact_path", "sha256"):
            if not (r.get(field) or "").strip():
                errors.append(f"{r['id']}: verified evidence missing {field}")
print(f"Assurance register structure: {sum(map(len,records.values()))} records, {len(errors)} errors")
for e in errors:
    print("ERROR:", e, file=sys.stderr)
sys.exit(1 if errors else 0)
