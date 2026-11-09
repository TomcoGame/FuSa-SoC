# Preliminary FMEDA work plan — SF-001

**Status:** Template and methodology, no numerical metrics or diagnostic-coverage claims.

## Scope
Analyze the memory integrity path from SRAM storage and ECC generation/checking through fault status and the external observer. Confirm actual fault semantics from RTL and tests before assigning any failure-rate classification.

## Analysis steps
1. Identify block hierarchy and ECC encoding/decoding implementation.
2. Define component boundaries, mission profile, operating conditions and failure modes.
3. Record each failure mode, effect, diagnostic mechanism, diagnostic test interval and assumptions.
4. Classify single-point, residual, latent, detected and safe faults only under an approved safety concept.
5. Support any failure-rate inputs with technology/process evidence and a documented source.
6. Evaluate common-cause faults in ECC logic, clocks, resets, buses and reporting path.
7. Cross-reference test IDs, source revisions and observed evidence.
8. Review assumptions and unresolved fault classes before calculating metrics.

**Do not calculate SPFM, LFM, PMHF or SIL PFH/PFDavg until the target architecture, failure rates, operating profile and applicable method are established.**
