# SF-001 — Detect and report safety-island memory integrity faults

**Status:** Candidate reference safety function — not approved or validated.
**Baseline:** FuSa-SoC SentryCore-derived safety island. This is a *component-level demonstrator*, not an automotive item definition or assigned SIL/ASIL safety function.

## Intended behavior
For a defined class of SRAM integrity faults affecting safety-related execution or data, the safety island shall detect an error and make a fault indication observable at a specified interface within a defined reaction interval. An external system supervisor is responsible for deciding and achieving the application-specific safe state.

## Boundary
**Inside candidate scope:** ECC SRAM wrappers, error indications, error management/status registers, clock/reset dependencies and the processor-visible error path.

**Outside candidate scope:** complete vehicle or machine safe-state control, external supervisor, power integrity, security root of trust and fault-free operation of all upstream dependencies.

## Operating modes and assumptions
| Mode | Candidate behavior / question |
|---|---|
| Boot | When are ECC checking and reporting active? Must be established |
| Normal operation | Detect/report faults according to configured ECC mechanisms |
| Diagnostic test | Fault injection must not silently corrupt normal evidence |
| Reset | Determine whether fault status is latched, cleared or lost |
| Degraded operation | Determine allowed behavior after an uncorrectable fault |

## Fault model (to validate)
- Single-bit memory corruption in an ECC-protected SRAM word
- Multi-bit corruption beyond correction capability
- Faults in ECC logic, fault signaling, clock/reset, and common-cause dependencies
- Faults outside the ECC protection boundary are explicitly not covered without further mechanisms

## Timing
No fault-tolerant time interval or detection-time limit is claimed. The system-level hazard analysis must define the required interval. Tests shall measure the elapsed time from injected fault to observable indication and compare it with an approved limit **once one exists**.

## Acceptance gates
1. Verify exact ECC configuration and fault outputs in the target RTL revision.
2. Define error-indication register/interrupt pin and observer.
3. Define deterministic fault-injection procedure and expected response for each fault type.
4. Capture logs/waveforms with source, tool, configuration and injection time.
5. Analyze uncovered faults, reset/clock dependencies and external supervisor assumptions.
6. Obtain independent review before making diagnostic coverage or integrity claims.

## Related starter IDs
HZ-002, REQ-002, ARCH-002, AN-002, TEST-002, CLAIM-002. These existing records are draft and do not yet constitute a validated trace chain.
