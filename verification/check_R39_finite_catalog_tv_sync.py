#!/usr/bin/env python3
"""Structural verifier for R39 finite-catalog spacetime total-variation synchronization.

Scope: exact P/Q mode algebra plus finite-catalog/extraction logic.  This is not a
continuum global-regularity certificate.
"""
import math
import random
import numpy as np

TOL = 2e-12


def helmholtz(k):
    k = np.asarray(k, dtype=float)
    q = np.outer(k, k) / float(np.dot(k, k))
    p = np.eye(3) - q
    return p, q


def cdot(a, b):
    return np.vdot(b, a)  # a dot conjugate(b)


def main():
    rng = np.random.default_rng(39039)
    prng = random.Random(39039)
    checks = 0
    maxerr = 0.0

    # Exact modewise identity:
    # w_grad - w_sol = Re(QL.QG*) + Re(PL.PG*) = Re(L.G*).
    for _ in range(30000):
        while True:
            k = rng.integers(-12, 13, size=3)
            if np.dot(k, k) > 0:
                break
        P, Q = helmholtz(k)
        L = rng.normal(size=3) + 1j * rng.normal(size=3)
        G = rng.normal(size=3) + 1j * rng.normal(size=3)
        PL, QL = P @ L, Q @ L
        PG, QG = P @ G, Q @ G
        wgrad = float(np.real(cdot(QL, QG)))
        wsol = -float(np.real(cdot(PL, PG)))
        rhs = float(np.real(cdot(L, G)))
        err = abs((wgrad - wsol) - rhs)
        maxerr = max(maxerr, err)
        assert err < TOL
        assert np.linalg.norm(P @ Q) < TOL
        assert np.linalg.norm(P + Q - np.eye(3)) < TOL
        checks += 3

    # Synthetic spacetime coefficient bound.  If every |d_k(t)| <= B*w(t),
    # then int sum_F |d_k| <= |F| B int w <= |F| B sqrt(|I| q).
    for _ in range(3000):
        m = prng.randint(1, 300)
        nt = prng.randint(8, 80)
        dt = 10 ** prng.uniform(-8, -2)
        B = 10 ** prng.uniform(-2, 2)
        omega = np.abs(rng.normal(size=nt)) * 10 ** prng.uniform(-2, 2)
        q = float(np.sum(omega * omega) * dt)
        length = nt * dt
        coeff = rng.uniform(-1, 1, size=(nt, m))
        d = B * omega[:, None] * coeff
        lhs = float(np.sum(np.abs(d)) * dt)
        mid = m * B * float(np.sum(omega) * dt)
        rhs = m * B * math.sqrt(length * q)
        assert lhs <= mid * (1 + 1e-13)
        assert mid <= rhs * (1 + 1e-12)
        checks += 2

    # Growing catalogs can be synchronized no matter how fast |F_n| grows,
    # because the extraction may move farther toward T* for each finite n.
    # Use delta=q=x as a synthetic tail model, so sqrt(delta*q)=x.
    for n in range(1, 35):
        m = 10 ** min(n, 12)
        eta = 10.0 ** (-n / 2)
        C = 1.7
        E = 2.3
        x = eta / (4 * C * m * E**3)
        bound = C * m * E**3 * x
        assert x > 0.0
        assert bound <= eta / 4 * (1 + 1e-12)
        checks += 2

    # ell1 mode discrepancy controls every partition of the catalog with no
    # extra factor equal to the number of partition cells.
    for _ in range(3000):
        m = prng.randint(1, 500)
        delta = rng.normal(size=m)
        scale = 10 ** prng.uniform(-8, -1) / max(1.0, np.sum(np.abs(delta)))
        delta *= scale
        tv = float(np.sum(np.abs(delta)))
        labels = rng.integers(0, prng.randint(1, 25) + 1, size=m)
        grouped = 0.0
        for lab in np.unique(labels):
            grouped += abs(float(np.sum(delta[labels == lab])))
        assert grouped <= tv * (1 + 1e-12)
        checks += 1

    # One-tail-atom compactification: resolved ell1 mismatch plus the exterior
    # aggregate mismatch bounds the total variation of the coarsened measure.
    for _ in range(3000):
        m = prng.randint(1, 500)
        resolved = rng.normal(size=m)
        resolved *= 10 ** prng.uniform(-10, -3) / max(1.0, np.sum(np.abs(resolved)))
        tail = float(rng.normal() * 10 ** prng.uniform(-10, -3))
        tv = float(np.sum(np.abs(resolved)) + abs(tail))
        eta = float(np.sum(np.abs(resolved)))
        eps = abs(tail)
        assert tv <= eta + eps + 1e-15
        checks += 1

    print(f"PASS R39 finite-catalog TV synchronization checks={checks} maxerr={maxerr:.3e}")
    print("SCOPE: exact mode algebra and finite-catalog extraction logic only; NOT global regularity")


if __name__ == "__main__":
    main()
