# Verification baseline and reproducibility
## Current evidence
The repository contains upstream simulation and software tests. The new GitHub Actions **FuSa baseline checks** workflow checks file presence, documentation integrity, SVG parsing, and records key file hashes. **It does not run RTL simulation**.

## Existing upstream infrastructure
- `.github/workflows/lint.yml` runs lint and generated-source cleanliness checks; status must be verified on this fork.
- `.github/workflows/internal.yml` contains an upstream-specific GitLab mirror action guarded to the upstream repository.
- `sim/Makefile` and `safed.mk` use QuestaSim and Bender.
- `sw/tests/runtime_ecc`, `runtime_bus_err`, `runtime_clic_basic` and other tests are available; passing status on this fork is not established.

## Reproduction procedure (not yet executed)
1. Capture git SHA and OS/toolchain versions.
2. Resolve `Bender.lock` dependencies using `make checkout`.
3. Build with `make build SIM_TOP=tb_safety_island_preloaded`.
4. Run existing ECC and bus-error tests following their Makefiles.
5. Preserve logs, test outputs, environment manifest, source hashes and known deviations.
6. Add targeted fault injection after baseline tests pass.

## Evidence levels
| Level | Meaning |
|---|---|
| 0 | Documentation or static repository check |
| 1 | Source compiles / elaborates |
| 2 | Existing test executes and passes |
| 3 | Directed fault-injection result with detection latency |
| 4 | Reviewed coverage analysis tied to explicit fault model |
| 5 | Independently assessed application-specific safety evidence |

Current new workflow reaches **Level 0 only**. Do not conflate CI green status with IEC 61508 or ISO 26262 compliance.
