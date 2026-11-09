# Cybersecurity assurance (proposed security island)

**Status:** Planning; no OpenTitan RTL integrated.

## Planned work products
1. Cybersecurity item definition, assets and trust boundaries.
2. TARA and cybersecurity goals under ISO/SAE 21434 where applicable.
3. Secure boot, keys, lifecycle, debug authorization and firmware update architecture.
4. Safety-security interaction analysis: startup, reset, denial of service, update and clock/power interference.
5. Security verification evidence and residual risk decisions.

**Design constraint:** loss or compromise of the security domain must not obstruct a required safety response within the application-specific fault-tolerant time interval.

See `../../docs/OPENTITAN-TRADE-STUDY.md`.
