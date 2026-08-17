#!/usr/bin/env python3
"""Structural algebra checks for R07.

Verifies the sharp two-vector coefficient p/(p-1), the p=3 value 3/2,
and random vector instances of the weighted quadratic inequality. It does not
verify any weighted Helmholtz-projector bound and does not prove regularity.
"""
from fractions import Fraction

import numpy as np

for p in range(3, 31):
    C = Fraction(p, p - 1)
    assert C == Fraction(1, p - 1) + 1

assert Fraction(3, 2) == Fraction(3, 3 - 1)

rng = np.random.default_rng(707)
for p in (3, 4, 5, 8, 16):
    C = p / (p - 1)
    for _ in range(1000):
        a = rng.normal(size=3)
        b = rng.normal(size=3)
        lhs = np.dot(a + b, a + b)
        rhs = C * ((p - 1) * np.dot(a, a) + np.dot(b, b))
        assert lhs <= rhs + 2e-12 * (1 + rhs)

# Near-equality direction for the abstract scalar/vector inequality:
# a is proportional to 1/(p-1), b proportional to 1, same direction.
for p in (3, 5, 11):
    e = np.array([1.0, 0.0, 0.0])
    a = e / (p - 1)
    b = e
    ratio = np.dot(a + b, a + b) / ((p - 1) * np.dot(a, a) + np.dot(b, b))
    assert abs(ratio - p / (p - 1)) < 1e-14

print("PASS R07 coefficient p/(p-1) for p=3..30")
print("PASS R07 random vector inequality stress")
print("PASS R07 abstract sharpness directions")
print("SCOPE: local structural algebra only; weighted Helmholtz transfer and global regularity remain open.")
