# Developer quickstart

This project is an upstream-derived hardware research repository. Build instructions below are inherited from upstream and **not yet validated by the FuSa-SoC maintainers**.

## Prerequisites

- Bender-compatible dependency tooling
- Compatible PULP RISC-V compiler toolchain
- QuestaSim for the documented upstream RTL simulation path
- Tool versions and environment variables matching the upstream scripts

## Checkout

```sh
git clone https://github.com/TomcoGame/FuSa-SoC.git
cd FuSa-SoC
make pulp-runtime
make pulp-freertos
source env/env.sh
make checkout
make build SIM_TOP=tb_safety_island_preloaded
```

For JTAG testbench use `make build SIM_TOP=tb_safety_island_jtag`.

## First verification targets

- Reproduce dependency checkout from `Bender.lock`.
- Compile the upstream RTL with a documented toolchain.
- Reproduce `sw/tests/runtime_ecc`, `runtime_bus_err` and `runtime_clic_basic`.
- Capture logs, tool versions, test configuration and results.
- Separate upstream baseline results from newly developed safety evidence.

## Licensing

Review `LICENSE.md`, individual source headers and dependency licenses. Do not assume that the top-level license covers every dependency.
