# Architecture and safety mechanisms

## Existing baseline
- `rtl/safety_core_wrap.sv`: TCLS core wrapper and error registers.
- `rtl/safety_island_top.sv`: integration, ECC SRAM, AXI, peripheral interfaces.
- `rtl/safety_island_pkg.sv`: configuration and address map.
- Upstream source: [PULP safety_island](https://github.com/pulp-platform/safety_island).

## Architecture elements (provisional IDs)
| ID | Element | Implementation maturity |
| --- | --- | --- |
| ARCH-001 | TCLS processor / mismatch detection | Upstream RTL exists; behavior unverified in this fork |
| ARCH-002 | ECC memory and error reporting | Upstream RTL exists; behavior unverified in this fork |
| ARCH-003 | External safety supervisor / safe-state control | Not implemented |
| ARCH-004 | Security root of trust | Proposed only |

The existing hardware diagram in `../../doc/` remains an upstream reference. The conceptual FuSa-SoC diagram is `../../docs/assets/fusa-soc-architecture.svg`.

## Next work
Define fault containment regions, clock/reset dependencies, common-cause analysis, fault reaction paths and safety/security interface contracts.
