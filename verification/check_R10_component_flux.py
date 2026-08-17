#!/usr/bin/env python3
"""Stdlib-only algebra check for R10 component-flux decomposition.

This validates the exact bookkeeping identity and gauge invariance of the
inter-component term. It does not control real Navier-Stokes level-set geometry
or prove global regularity.
"""
import random

rng = random.Random(1010)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

for components in range(2, 13):
    for _ in range(500):
        # Model component fluxes with exact total cancellation.
        J = [rng.gauss(0.0, 1.0) for _ in range(components)]
        J[-1] = -sum(J[:-1])
        pbar = [rng.gauss(0.0, 1.0) for _ in range(components)]
        intra = [rng.gauss(0.0, 1.0) for _ in range(components)]

        # Exact decomposition: modeled total level work = inter + intra.
        inter = dot(pbar, J)
        total = inter + sum(intra)
        reconstructed = sum(p*j + r for p, j, r in zip(pbar, J, intra))
        assert abs(total - reconstructed) < 1e-10

        # R09 quotient symmetry: common pressure offset drops out because sum J=0.
        c = rng.gauss(0.0, 1.0)
        shifted = dot([p + c for p in pbar], J)
        assert abs(shifted - inter) < 1e-10

# Two-component simplification.
for _ in range(1000):
    j = rng.gauss(0.0, 1.0)
    p1 = rng.gauss(0.0, 1.0)
    p2 = rng.gauss(0.0, 1.0)
    lhs = p1 * j + p2 * (-j)
    rhs = (p1 - p2) * j
    assert abs(lhs - rhs) < 1e-12

print("PASS R10 component decomposition bookkeeping")
print("PASS R10 common-pressure gauge invariance")
print("PASS R10 two-component pressure-offset x flux identity")
print("SCOPE: algebra only; component flux/pressure control and global regularity remain OPEN.")
