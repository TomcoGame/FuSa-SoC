# FuSa-SoC assurance framework v0.1

**Maturity:** scaffold / planning. This repository does not establish SIL, ASIL, hardware metrics, diagnostic coverage, certification, or independent assessment.

## Purpose
Create an auditable, configuration-specific chain from item boundary and hazards through requirements, architecture, analyses, verification, evidence and safety argument. The initial baseline is the PULP SentryCore safety island. The OpenTitan security island remains a proposed extension.

## Lifecycle and folders

| Directory | Purpose | Primary output |
| --- | --- | --- |
| `00-governance/` | Scope, roles, change control, baseline policy | Governance plan |
| `01-item-definition/` | Use case, boundaries, interfaces, operating modes | Item definition |
| `02-risk/` | HARA, hazard log, TARA, safety-security interactions | Risk register |
| `03-requirements/` | Safety and cybersecurity requirements, allocations | Requirements CSV |
| `04-architecture/` | Fault containment, safety mechanisms, interface contracts | Architecture baseline |
| `05-analyses/` | FMEA, FMEDA, FTA, DFA and assumptions | Analysis register |
| `06-verification/` | Test plans, test cases, fault-injection campaigns | Verification register |
| `07-evidence/` | Immutable evidence references, hashes, tool metadata | Evidence index |
| `08-safety-case/` | Structured claims, arguments, evidence links | Claim register |
| `09-assessment/` | Review findings, deviations, independent assessment | Findings register |
| `10-cybersecurity/` | TARA, secure boot, root-of-trust and co-engineering | Security work products |
| `schemas/` | JSON schemas for controlled records | Validation contract |
| `tools/` | Local assurance validation | Validator |

## Traceability model

`Item → Hazard/Threat → Goal → Requirement → Architecture Element → Analysis → Test → Evidence → Claim`

Records use stable IDs and explicit status. **Placeholder rows are examples, not accepted engineering requirements or verified test results.** A safety claim is not substantiated merely because an evidence path exists.

## Validate

```bash
python3 assurance/tools/validate.py
```

Validation checks required columns, unique IDs, allowed statuses and reference integrity across the starter CSV registers. It **does not** assess technical adequacy, SIL/ASIL metrics, or completeness against any standard.

## Change-control rules

1. All requirement, hazard and claim changes are reviewed through a pull request.
2. Evidence records must identify source revision, configuration, method, tool version, result and artifact hash before they can be marked verified.
3. Failed tests and unresolved findings must remain visible.
4. Never change a source file or baseline evidence in place to hide a failure.
5. The upstream RTL is untouched by this scaffold.

## First reference function

[SF-001 — Detect and report memory integrity faults](01-item-definition/REFERENCE-SF-001.md) is the first **candidate** component-level safety function. Its [FMEDA plan](05-analyses/FMEDA-PLAN.md), [failure-mode template](05-analyses/fmeda-memory-template.csv), [test plan](06-verification/SF-001-TEST-PLAN.md), and [fault campaign](06-verification/fault-campaign.csv) are drafts. No diagnostic coverage or safety integrity is claimed.
