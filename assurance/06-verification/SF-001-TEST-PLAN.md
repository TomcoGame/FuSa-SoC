# SF-001 ECC fault-injection verification plan

**Status:** Test design only. No simulator execution or passing result claimed.

## Preconditions
- Freeze source commit, Bender.lock, target configuration and testbench.
- Record simulator version, compiler/toolchain, host and test commands.
- Confirm nominal boot and memory access.
- Establish ECC error signal/register mapping from RTL and generated registers.
- Define reset and timeout behavior and an external observation point.

| Case | Injection | Observation | Pass criterion (pending design review) |
|---|---|---|---|
| SF001-T01 | Single-bit SRAM corruption | Corrected data and fault report | Matches specified ECC correction/reporting behavior |
| SF001-T02 | Multi-bit SRAM corruption | Uncorrectable error path | Defined indication and response observed |
| SF001-T03 | Fault during reset | Fault reporting/recovery | Behavior matches documented reset contract |
| SF001-T04 | Reporting path interruption | Missing or delayed fault report | Failure detected or explicitly recorded as coverage gap |
| SF001-T05 | Nominal memory operation | No injected faults | No unexpected fault reports |

## Measurement
For each run record injected fault location and time, activation conditions, first observed indication time, delta cycles/time, final software-visible status, output waveform, test verdict and unexplained behavior.

## Evidence format
Store raw simulation logs and waveforms in a versioned evidence location or durable artifact store. Register their cryptographic hashes in `../07-evidence/evidence.csv`; never label a test `verified` without associated evidence.

## Existing starting points
- `sw/tests/runtime_ecc/` including `fault_injection.tcl`
- `sw/tests/runtime_bus_err/`
- `rtl/safety_island_top.sv` ECC wrappers and reporting paths

The existing scripts have not been demonstrated to meet these acceptance criteria in this fork.
