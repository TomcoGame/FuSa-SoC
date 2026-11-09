#!/usr/bin/env python3
"""Static source-inventory checks. NOT RTL simulation or fault-injection verification."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    "TCLS configuration": ("rtl/safety_island_pkg.sv", r"UseTCLS"),
    "TCLS generation": ("rtl/safety_core_wrap.sv", r"if\s*\(SafetyIslandCfg\.UseTCLS\)"),
    "TCLS error outputs": ("rtl/safety_core_wrap.sv", r"\.tmr_error_o"),
    "ECC memory wrapper": ("rtl/safety_island_top.sv", r"ecc_sram_wrap"),
    "ECC manager interface": ("rtl/safety_island_top.sv", r"ecc_mgr"),
    "AXI input interface": ("rtl/safety_island_top.sv", r"axi_input_req_i"),
    "AXI output interface": ("rtl/safety_island_top.sv", r"axi_output_req_o"),
    "ECC test source": ("sw/tests/runtime_ecc/Makefile", r"fault_injection\.tcl"),
    "Bus error test": ("sw/tests/runtime_bus_err/Makefile", r"runtime_bus_err"),
}
results = []
for label, (path, pattern) in CHECKS.items():
    file = ROOT / path
    data = file.read_bytes() if file.is_file() else b""
    present = bool(re.search(pattern, data.decode("utf-8", errors="replace")))
    results.append({"check": label, "file": path, "source_present": present,
                    "sha256": hashlib.sha256(data).hexdigest() if data else None,
                    "verification_level": "static-source-inventory-only"})
report = {"schema_version": 1, "warning": "No RTL simulation, diagnostic coverage or safety integrity verified",
          "checks": results, "passed": all(r["source_present"] for r in results)}
print(json.dumps(report, indent=2))
raise SystemExit(0 if report["passed"] else 1)
