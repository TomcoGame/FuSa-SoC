# OpenTitan integration trade study — FuSa-SoC
**Status:** Preliminary architecture study; no implementation or qualification claim.

## Decision
Preserve the PULP SentryCore safety island and evaluate OpenTitan as a **separate security domain**, initially through a defined command/status interface. Do not replace the existing TCLS core or import all OpenTitan RTL before reproducing baseline simulation.

## Alternatives
| Option | Advantages | Principal concerns | Recommendation |
|---|---|---|---|
| A. External security controller / discrete root of trust | Independent integration boundary; faster prototype; fewer RTL dependencies | Board cost, physical interfaces, reset/power coupling, latency | **First demonstrator** |
| B. Integrated OpenTitan-derived security island | Common SoC integration, configurable secure services, reusable RTL | Clock/reset/power isolation, bus arbitration, security-to-safety interference, verification scope | **Research target** |
| C. Merge security features into TCLS safety CPU | Potentially fewer blocks | Weak separation, shared failure modes, complex safety/security argument | Do not pursue initially |
| D. Safety-only SentryCore | Minimum baseline complexity | No integrated hardware root of trust | Maintain as reference baseline |

## Proposed integration contract
- Security domain may authorize images and updates; safety domain independently evaluates runtime safety conditions.
- Security failure, boot delay, or update interruption must not prevent a time-bounded safety response.
- Cross-domain requests are bounded, authenticated where needed, rate-limited, and explicitly versioned.
- Reset, clock, power, memory, DMA, debug and bus dependencies require dependent-failure analysis.
- Fault reporting and safe-state actuation must be specified at system level; the existing RTL does not provide a certified safe-state path.

## Engineering gates
1. Reproduce SentryCore RTL build/simulation with recorded tools and hashes.
2. Define a concrete automotive/industrial reference use case and safety function.
3. Create system block diagram, trust boundaries and fault-containment regions.
4. Map safety goals, security goals and shared assets; perform preliminary HARA/TARA.
5. Assess OpenTitan hardware IP dependencies and licenses at file/revision level.
6. Prototype an external security-controller interface with failure-injection tests.
7. Compare measured timing, fault behavior, resource costs and verification effort against an integrated approach.
8. Decide whether to import OpenTitan-derived RTL after review.

## Open questions
- Which OpenTitan top-level variant and IP subset best meets the requirements?
- How is firmware authenticity checked without creating unsafe startup dependencies?
- Can the safety domain reach its safe state during security-domain reset or loss of clock?
- What is the hardware fault model, diagnostic test interval, and required fault-tolerant time interval?
- Which security-to-safety attack paths require dedicated mitigations?

## Links
- [OpenTitan](https://github.com/lowRISC/opentitan)
- [PULP Safety Island](https://github.com/pulp-platform/safety_island)
- [FuSa-SoC architecture](ARCHITECTURE.md)

**No safety or security certification is implied by the architecture choices.**
