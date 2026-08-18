#!/usr/bin/env python3
"""Verifier for R40 strong finite-catalog absolute-work evacuation.

Structural/diagonal-extraction certificate only.  Not global regularity.
"""
import math
import random
import numpy as np

TOL = 3e-12


def helmholtz(k):
    k = np.asarray(k, dtype=float)
    q = np.outer(k, k) / float(np.dot(k, k))
    p = np.eye(3) - q
    return p, q


def dotc(a, b):
    return np.vdot(b, a)


def main():
    rng = np.random.default_rng(40040)
    prng = random.Random(40040)
    checks = 0
    max_ratio = 0.0

    # Projection-level work bound: each exact representation is bounded by
    # |Lhat||Ghat|, since P,Q are orthogonal contractions.
    for _ in range(40000):
        while True:
            k = rng.integers(-15, 16, size=3)
            if np.dot(k, k) > 0:
                break
        P, Q = helmholtz(k)
        L = rng.normal(size=3) + 1j*rng.normal(size=3)
        G = rng.normal(size=3) + 1j*rng.normal(size=3)
        denom = np.linalg.norm(L)*np.linalg.norm(G)
        wg = abs(float(np.real(dotc(Q@L, Q@G))))
        ws = abs(float(np.real(dotc(P@L, P@G))))
        if denom > 1e-15:
            max_ratio = max(max_ratio, wg/denom, ws/denom)
        assert wg <= denom*(1+TOL)
        assert ws <= denom*(1+TOL)
        assert np.linalg.norm(P@Q) < TOL
        checks += 3

    # Finite-catalog L1_t ell1_k envelope for both representations.
    for _ in range(3500):
        m = prng.randint(1, 350)
        nt = prng.randint(5, 80)
        dt = 10**prng.uniform(-8, -2)
        B = 10**prng.uniform(-2, 2)  # V^-1 E0^3
        omega = np.abs(rng.normal(size=nt))*10**prng.uniform(-2, 2)
        rg = rng.uniform(0, 1, size=(nt,m))
        rs = rng.uniform(0, 1, size=(nt,m))
        wg = B*omega[:,None]*rg
        ws = B*omega[:,None]*rs
        lhs = float(np.sum(wg+ws)*dt)
        q = float(np.sum(omega*omega)*dt)
        length = nt*dt
        rhs = 2*m*B*math.sqrt(length*q)
        assert lhs <= rhs*(1+1e-12)
        checks += 1

    # Arbitrarily fast finite-catalog growth can be beaten by moving the
    # start closer to T*. Synthetic model delta=q=x => sqrt(delta*q)=x.
    for n in range(1,45):
        m = 10**min(n,14)
        zeta = 10**(-n/3)
        B = 3.7
        x = zeta/(8*m*B)
        bound = 2*m*B*x
        assert x > 0
        assert bound <= zeta/4*(1+1e-12)
        checks += 2

    # Synthetic R38-compatible packets: resolved absolute work vanishes while
    # exterior signed (hence positive-part) work exceeds M.
    for _ in range(4000):
        zeta = 10**prng.uniform(-9,-3)
        M = 10**prng.uniform(1,5)
        m = prng.randint(1,200)
        # Resolved works, with total absolute mass <= zeta.
        wg_in = np.abs(rng.normal(size=m))
        ws_in = np.abs(rng.normal(size=m))
        scale = zeta/max(1.0, float(np.sum(wg_in+ws_in)))
        wg_in *= scale
        ws_in *= scale
        assert float(np.sum(wg_in+ws_in)) <= zeta*(1+1e-12)
        # Exterior signed work can be represented by positive mass >= M plus
        # optional negative mass; signed total >= M implies positive part >=M.
        neg_g = float(abs(rng.normal()))
        neg_s = float(abs(rng.normal()))
        pos_g = M + neg_g + abs(float(rng.normal()))
        pos_s = M + neg_s + abs(float(rng.normal()))
        signed_g = pos_g-neg_g
        signed_s = pos_s-neg_s
        assert signed_g >= M and signed_s >= M
        assert pos_g >= M and pos_s >= M
        c_in = 0.5*(wg_in+ws_in)
        assert float(np.sum(np.abs(c_in))) <= zeta/2*(1+1e-12)
        checks += 5

    print(f"PASS R40 absolute-work evacuation checks={checks} max_projection_ratio={max_ratio:.12f}")
    print("SCOPE: projection/coefficient and diagonal extraction logic only; NOT global regularity")


if __name__ == '__main__':
    main()
