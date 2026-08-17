#!/usr/bin/env python3
"""Fresh replay and provenance gate for P03/RD002.

This checker verifies that the committed experiment script is byte-identical to
what the frozen result claims, re-evaluates the committed winner at independent
resolutions, and confirms the preregistered >1/2 falsification margin.

It certifies only a finite-dimensional computational challenger. It is NOT a
Navier-Stokes regularity or singularity proof.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "experiments" / "run_P03_expanded_lamb_coherence.py"
RESULT = ROOT / "verification" / "P03_expanded_Lamb_coherence_result.json"
ROBUST = ROOT / "verification" / "P03_high_resolution_robustness.json"


def load_module(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location("p03_replay", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load P03 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


result = json.loads(RESULT.read_text())
robust = json.loads(ROBUST.read_text())
actual_hash = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
assert actual_hash == result["script_sha256"], (actual_hash, result["script_sha256"])
assert result["seed"] == 20260819
assert result["random_trials"] == 3000
assert result["hill_trials"] == 8000
assert result["verdict"] == "H-break-half"
assert result["converged_last_two"] is True
assert abs(result["confirmation"][-1]["kappa"] - result["confirmation"][-2]["kappa"]) < result["convergence_tolerance"]
assert result["confirmation"][-1]["kappa"] > 0.5

p03 = load_module(SCRIPT)
c = np.array(result["winner_coefficients"], dtype=np.float64)
assert c.shape == (52,)

# Fresh independent-resolution replay at N=64 and N=96.
for N in (64, 96):
    kappa, details = p03.eval_kappa(c, N, None, True)
    if N == 64:
        target = result["confirmation"][-1]
    else:
        target = next(item for item in robust["values"] if item["N"] == 96)
    assert abs(kappa - target["kappa"]) < 2e-10
    assert abs(details["W3"] - target["W3"]) < 2e-10
    assert abs(details["QLamb_L2"] - target["QLamb_L2"]) < 2e-10
    assert abs(details["QG_L2"] - target["QG_L2"]) < 2e-10
    assert kappa > 0.5

# The post-confirmation N=128 value also retains a wide numerical margin.
n128 = next(item for item in robust["values"] if item["N"] == 128)
assert n128["kappa"] > 0.519

print("PASS P03 byte-level provenance hash")
print("PASS P03 frozen protocol metadata")
print("PASS P03 winner replay at N=64 and N=96")
print("PASS preregistered kappa_L > 1/2 falsification margin")
print("SCOPE: P03/RD002 finite-dimensional challenger only; NOT global regularity.")

# This explicit end marker also makes creation of the workflow precede its trigger commit.
