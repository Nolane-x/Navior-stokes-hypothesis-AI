#!/usr/bin/env python3
"""Finite-dimensional algebra check for R10 component-flux decomposition.

This validates the exact bookkeeping identity and gauge invariance of the
inter-component term. It does not control real Navier-Stokes level-set geometry
or prove global regularity.
"""
import numpy as np

rng = np.random.default_rng(1010)
for components in range(2, 13):
    for _ in range(500):
        # Model component fluxes with exact total cancellation.
        J = rng.normal(size=components)
        J[-1] = -float(np.sum(J[:-1]))
        pbar = rng.normal(size=components)
        intra = rng.normal(size=components)

        # Exact decomposition: modeled total level work = inter + intra.
        inter = float(np.dot(pbar, J))
        total = inter + float(np.sum(intra))
        reconstructed = float(np.sum(pbar * J + intra))
        assert abs(total - reconstructed) < 1e-11

        # R09 quotient symmetry: common pressure offset drops out because sum J=0.
        c = float(rng.normal())
        shifted = float(np.dot(pbar + c, J))
        assert abs(shifted - inter) < 1e-11

# Two-component simplification.
for _ in range(1000):
    j = float(rng.normal())
    p1, p2 = map(float, rng.normal(size=2))
    lhs = p1 * j + p2 * (-j)
    rhs = (p1 - p2) * j
    assert abs(lhs - rhs) < 1e-12

print("PASS R10 component decomposition bookkeeping")
print("PASS R10 common-pressure gauge invariance")
print("PASS R10 two-component pressure-offset x flux identity")
print("SCOPE: algebra only; component flux/pressure control and global regularity remain OPEN.")
