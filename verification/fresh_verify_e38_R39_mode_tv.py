#!/usr/bin/env python3
"""Fresh-context verifier for R39.

Independent lineage: random orthogonal projectors rather than the theorem's
wave-vector Helmholtz constructor, plus direct discrete physical-space Fourier
coefficient estimates.
"""
import math
import numpy as np

rng = np.random.default_rng(9039)
checks = 0
maxerr = 0.0

# Independent complementary-projector identity.
for _ in range(20000):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    Q = np.outer(n, n)
    P = np.eye(3) - Q
    L = rng.normal(size=3) + 1j * rng.normal(size=3)
    G = rng.normal(size=3) + 1j * rng.normal(size=3)
    wg = np.real(np.vdot(Q @ G, Q @ L))
    ws = -np.real(np.vdot(P @ G, P @ L))
    rhs = np.real(np.vdot(G, L))
    err = abs((wg - ws) - rhs)
    maxerr = max(maxerr, err)
    assert err < 2e-12
    checks += 1

# Direct physical-space coefficient bounds under normalized discrete measure.
# The argument is the finite-dimensional Cauchy-Schwarz analogue of the torus
# coefficient estimate and does not import the primary checker.
for N in (37, 61, 101):
    x = np.arange(N)
    for _ in range(200):
        u = rng.normal(size=(N, 3))
        om = rng.normal(size=(N, 3))
        L = np.cross(om, u)
        G = np.linalg.norm(u, axis=1)[:, None] * u
        un = math.sqrt(float(np.mean(np.sum(u * u, axis=1))))
        on = math.sqrt(float(np.mean(np.sum(om * om, axis=1))))
        for k in rng.integers(0, N, size=20):
            phase = np.exp(-2j * np.pi * k * x / N)[:, None]
            Lh = np.mean(L * phase, axis=0)
            Gh = np.mean(G * phase, axis=0)
            assert np.linalg.norm(Lh) <= on * un * (1 + 1e-12)
            assert np.linalg.norm(Gh) <= un * un * (1 + 1e-12)
            checks += 2

# Independent randomized replay of the spacetime total-variation envelope.
for _ in range(3000):
    nt = int(rng.integers(4, 70))
    m = int(rng.integers(1, 400))
    dt = 10 ** rng.uniform(-7, -2)
    E = 10 ** rng.uniform(-1, 1)
    om = np.abs(rng.normal(size=nt))
    envelope = E**3 * om
    ratios = rng.uniform(0, 1, size=(nt, m))
    d = envelope[:, None] * ratios
    lhs = float(np.sum(d) * dt)
    q = float(np.sum(om * om) * dt)
    length = nt * dt
    rhs = m * E**3 * math.sqrt(length * q)
    assert lhs <= rhs * (1 + 1e-12)
    checks += 1

print(f"PASS fresh E38/R39 mode-TV reconstruction checks={checks} maxerr={maxerr:.3e}")
print("VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY")
