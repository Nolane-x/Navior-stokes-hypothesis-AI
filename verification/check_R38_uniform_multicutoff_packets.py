#!/usr/bin/env python3
"""Verifier for R38 uniform multi-cutoff/shell terminal-packet extraction logic."""
import math
import random


def lattice_radii(L):
    R = math.ceil(L)
    vals = []
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            for z in range(-R, R + 1):
                r2 = x*x + y*y + z*z
                if r2 and r2 <= L*L + 1e-12:
                    vals.append(r2)
    return sorted(set(vals))


def count_modes(K):
    R = math.ceil(K)
    n = 0
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            for z in range(-R, R + 1):
                r2 = x*x + y*y + z*z
                if r2 and r2 <= K*K + 1e-12:
                    n += 1
    return n


def main():
    rng = random.Random(38038)
    checks = 0

    # Below a finite ceiling only finitely many periodic sharp projectors occur,
    # and N_K is monotone in K.
    for L in [1, 1.5, 2, 3.7, 5.2, 8.1, 12.0]:
        radii = lattice_radii(L)
        assert len(radii) < (2*math.ceil(L)+1)**3
        samples = [0.0] + [math.sqrt(r) for r in radii] + [L]
        prev = -1
        NL = count_modes(L)
        for K in sorted(samples):
            NK = count_modes(K)
            assert NK >= prev and NK <= NL
            prev = NK
            checks += 2
        edges = [0.0] + [math.sqrt(r) for r in radii] + [L]
        for a, b in zip(edges, edges[1:]):
            if b-a > 1e-10:
                mid = (a+b)/2
                x = a + (b-a)/3
                y = a + 2*(b-a)/3
                assert count_modes(x) == count_modes(y) == count_modes(mid)
                checks += 1

    # R32 uniform tolerance domination for every K <= L.
    for _ in range(500):
        L = rng.uniform(1.1, 14.0)
        eps = 10**rng.uniform(-8, -1)
        C = 10**rng.uniform(-1, 1)
        E = 10**rng.uniform(-1, 1)
        NL = max(1, count_modes(L))
        qtail = 0.7*eps/(C*(NL**(2/3))*E*E)
        for _ in range(20):
            K = rng.uniform(0, L)
            NK = count_modes(K)
            bound = C*(NK**(2/3) if NK else 0.0)*E*E*qtail
            assert bound <= eps*(1+1e-12)
            checks += 1

    # Synthetic finite-family extraction sanity: if each cumulative tail tends
    # to +infinity, finitely many cutoff classes admit one common b<T*.
    for m in [1, 2, 5, 20, 100]:
        M = 100.0 + m
        eps = 1e-5
        T = 1.0
        offsets = [1.0 + 0.17*j for j in range(m)]
        deltas = [eps*(j+1)/(2*m) for j in range(m)]
        thresholds = []
        for off, d in zip(offsets, deltas):
            thresholds += [
                1-1/(M+off),
                1-1/(M+off+d),
                1-1/(M+2*off),
            ]
        b = max(thresholds) + (T-max(thresholds))/2
        assert b < T
        for off, d in zip(offsets, deltas):
            ag = 1/(1-b)-off
            ass = ag-d
            ab = 1/(1-b)-2*off
            assert ag >= M and ass >= M and ab >= M
            assert abs(ag-ass) <= eps
            checks += 4

    # Uniform cumulative mismatch <= eps implies every shell mismatch <= 2 eps.
    # This is the exact algebra Delta(K1)-Delta(K2), independent of signs.
    for _ in range(1000):
        eps = 10**rng.uniform(-10, -2)
        m = rng.randint(3, 80)
        # Synthetic cumulative tails with arbitrary large common baseline and
        # mismatch values independently filling [-eps, eps].
        common = [10**rng.uniform(2, 5) for _ in range(m)]
        delta = [rng.uniform(-eps, eps) for _ in range(m)]
        agrad = [c + d/2 for c, d in zip(common, delta)]
        asol = [c - d/2 for c, d in zip(common, delta)]
        for _ in range(12):
            i = rng.randrange(0, m-1)
            j = rng.randrange(i+1, m)
            sgrad = agrad[i]-agrad[j]
            ssol = asol[i]-asol[j]
            assert abs(sgrad-ssol) <= 2*eps*(1+1e-9)
            checks += 1

    # Arbitrary prescribed terminal scale: choosing a with T*-a <= delta
    # automatically bounds every extracted I=[a,b] by delta because b<T*.
    for _ in range(500):
        T = rng.uniform(0.5, 3.0)
        delta = 10**rng.uniform(-10, -1)
        a = T - 0.8*delta
        b = a + rng.random()*(T-a)
        assert 0 <= b-a <= delta*(1+1e-12)
        checks += 1

    print(f"PASS R38 uniform multi-cutoff/shell packet checks={checks}")
    print("SCOPE: lattice/extraction/shell algebra certificate only; continuum inputs are R28/R30/R32")


if __name__ == "__main__":
    main()
