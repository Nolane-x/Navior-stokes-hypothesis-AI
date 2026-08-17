#!/usr/bin/env python3
"""Fresh structural checks for R05 and RD003.

These finite-dimensional stress checks validate the abstract Helmholtz algebra,
scaling bookkeeping, velocity-reversal oddness, and amplitude homogeneity used
by the written proofs. They do not certify Navier-Stokes global regularity.
"""
from fractions import Fraction

import numpy as np

# R05 scaling audit: 3/2 + (p-5/2) = p-1.
for p in range(2, 21):
    assert Fraction(3, 2) + (Fraction(p, 1) - Fraction(5, 2)) == p - 1

rng = np.random.default_rng(503)

# R05 abstract complementarity for orthogonal pairs and orthogonal projectors.
for n in (3, 5, 11):
    for _ in range(250):
        x = rng.normal(size=n)
        x /= np.linalg.norm(x)
        y = rng.normal(size=n)
        y -= x * np.dot(x, y)
        yn = np.linalg.norm(y)
        if yn < 1e-12:
            continue
        y /= yn

        M = rng.normal(size=(n, n))
        U, _, _ = np.linalg.svd(M, full_matrices=False)
        rank = int(rng.integers(1, n))
        Q = U[:, :rank] @ U[:, :rank].T
        P = np.eye(n) - Q

        q_pair = float(np.dot(Q @ x, Q @ y))
        p_pair = float(np.dot(P @ x, P @ y))
        assert abs(q_pair + p_pair) < 2e-12
        assert abs(q_pair) <= 0.5 + 2e-12

# R05 protected p=2 endpoint: if the test vector is solenoidal/range(P), Qy=0.
for n in (4, 8):
    M = rng.normal(size=(n, n))
    U, _, _ = np.linalg.svd(M, full_matrices=False)
    rank = n // 2
    P = U[:, :rank] @ U[:, :rank].T
    Q = np.eye(n) - P
    y = P @ rng.normal(size=n)
    assert np.linalg.norm(Q @ y) < 2e-12

# RD003: a quadratic functional paired with a quadratic convection has an odd
# nonlinear derivative under u -> -u and scales cubically under u -> a u.
for n in (3, 6):
    M = rng.normal(size=(n, n))
    A = (M + M.T) / 2
    T = rng.normal(size=(n, n, n))
    T = (T + T.swapaxes(1, 2)) / 2

    def B(u):
        return np.einsum("ijk,j,k->i", T, u, u)

    def nonlinear_derivative(u):
        return -float((A @ u) @ B(u))

    for _ in range(100):
        u = rng.normal(size=n)
        value = nonlinear_derivative(u)
        assert abs(nonlinear_derivative(-u) + value) < 1e-9 * (1 + abs(value))
        a = 3.75
        assert abs(nonlinear_derivative(a * u) - a**3 * value) < 1e-8 * (1 + abs(a**3 * value))

print("PASS R05 Helmholtz complementarity/half-bound stress")
print("PASS R05 scaling and protected p=2 endpoint")
print("PASS RD003 velocity-reversal oddness and cubic amplitude scaling")
print("SCOPE: structural algebra only; NOT Navier-Stokes global regularity.")
