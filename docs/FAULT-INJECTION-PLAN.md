# Fault-injection verification plan (draft)

**Status:** Planning only. No tests in this document have been executed.

## Baseline requirements
- Identify a target safety function, failure response and fault-tolerant time interval before declaring diagnostic adequacy.
- Preserve the SentryCore source revision, Bender lock, simulator version, toolchain version and test configuration.
- Establish nominal execution, boot and memory operation before injecting faults.
- Distinguish source presence, compiled test, passing test, fault-detection result and reviewed coverage.

## Campaign matrix

| ID | Injection target | Method to develop | Expected observable | Required evidence |
|---|---|---|---|---|
| FI-ECC-01 | Single-bit SRAM corruption | Existing `runtime_ecc/fault_injection.tcl` baseline | ECC correction/reporting according to configuration | Waveforms, registers, latency, pass criteria |
| FI-ECC-02 | Multi-bit SRAM corruption | Directed simulation fault | Uncorrectable error reporting and specified response | Error propagation and system reaction |
| FI-TCLS-01 | One TCLS core diverges | Directed register/logic perturbation | Mismatch detection, escalation | Detection latency and reset/fault containment |
| FI-TCLS-02 | Common-cause perturbation | Multi-core fault model | Identify uncovered common-mode faults | Explicit limitation and mitigation |
| FI-BUS-01 | Instruction/data bus error | Existing `runtime_bus_err` baseline | Fault status/handler path | Register capture and interrupt/exception timing |
| FI-RESET-01 | Reset/power-domain disturbance | Future system integration test | Defined safety reaction | Independence and fault propagation |
| FI-SEC-01 | Security island unavailable | Future integrated/external prototype | Safety response remains available | Timing, boundary behavior, no blocking |

## Exit criteria for first real simulation milestone
1. Reproducible dependency checkout and simulator build.
2. At least one ECC and one bus-error test with saved logs and clear pass/fail criteria.
3. Explicit source and toolchain hashes.
4. Documented deviations, unsupported tools and failed tests.
5. Review that simulation does not itself establish SIL/ASIL metrics.

## Immediate CI coverage
`tools/verify_rtl_inventory.py` is **static source inventory only**. It detects removal/renaming of expected RTL and test hooks; it does not elaborate RTL or exercise any fault.
