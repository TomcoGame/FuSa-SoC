# Assurance governance plan — draft

## Scope
Reference component: SentryCore-derived FuSa-SoC safety island. Target item, operating environment, safety function and integrity targets are **TBD**. No automotive item-level HARA has been performed.

## Roles to assign
- Project owner: approves baselines and scope
- Safety manager: maintains safety plan and independence criteria
- RTL owner: reviews hardware changes and dependent effects
- Verification lead: controls tests, faults and evidence
- Cybersecurity lead: maintains TARA and security/safety interactions
- Independent reviewer/assessor: role and independence to be established

## Required gates
G0 scope/item definition → G1 hazard/threat analysis → G2 requirements → G3 architecture → G4 analysis → G5 verification → G6 safety case → G7 independent review.

A gate requires documented approvals and open-issue disposition; directory existence alone does not constitute completion.

## Baselines
Record Git SHA, dependency lock hash, RTL configuration, toolchain, test environment and safety manual assumptions for each reviewed release.

## Applicability
IEC 61508 / ISO 26262 / ISO/SAE 21434 are **candidate frameworks**. Applicability, tailoring, independence and required work products must be justified for the actual target item.
