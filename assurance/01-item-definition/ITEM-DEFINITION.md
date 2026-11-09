# Reference item definition — template

**Status:** NOT STARTED

| Field | Definition |
| --- | --- |
| Reference application | TBD: select one concrete automotive or industrial use case |
| System boundary | Safety island RTL, firmware and specified integration interfaces |
| External components | Host SoC, memory, clocks, reset, power, safety supervisor — TBD |
| Safety function | TBD |
| Operating modes | Boot, normal, degraded, diagnostic, update, shutdown — to define |
| Safe state | Application-specific; cannot be inferred from RTL alone |
| Fault-tolerant time interval | TBD by hazard analysis |
| Assumptions of use | TBD |
| Out of scope | Proposed OpenTitan integration until separately baselined |

## Interface inventory
Document AXI, JTAG, interrupt, clock/reset, memory and fault reporting interfaces with directions, timing and ownership.

## Exit criteria
Item boundary, operating modes, interfaces, safety function, hazards, external dependencies and assumptions reviewed and approved.
