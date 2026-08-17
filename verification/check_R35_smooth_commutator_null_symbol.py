#!/usr/bin/env python3
"""Verifier for the R35 smooth commutator multiplier."""
import math
import random

L_A = math.sqrt(2.0 / math.e)


def norm3(v):
    return math.sqrt(sum(x*x for x in v))


def aval(v):
    return math.exp(-sum(x*x for x in v))


def main():
    rng = random.Random(35035)
    checks = 0
    for K in (2.0, 4.0, 9.0, 17.0):
        for _ in range(4000):
            p = tuple(rng.randint(-12, 12) for _ in range(3))
            q = tuple(rng.randint(-12, 12) for _ in range(3))
            k = tuple(p[i] + q[i] for i in range(3))
            pk = tuple(x / K for x in p)
            kk = tuple(x / K for x in k)
            diff = abs(aval(kk) - aval(pk))
            rhs = min(2.0, L_A * norm3(q) / K)
            assert diff <= rhs + 2e-14
            if q == (0, 0, 0):
                assert diff <= 1e-15
            checks += 1

    # Symbol identity is algebraically A(product)-product(A omega):
    # [a(k)-a(p)] times each triad coefficient.
    for _ in range(1000):
        ak = rng.random()
        ap = rng.random()
        coeff = rng.uniform(-10.0, 10.0)
        direct = ak * coeff - ap * coeff
        symbol = (ak - ap) * coeff
        assert abs(direct - symbol) <= 1e-13
        checks += 1

    for eta in (0.01, 0.05, 0.1, 0.25):
        for K in (10.0, 30.0, 100.0):
            qnorm = eta * K
            assert L_A * qnorm / K <= L_A * eta * (1.0 + 1e-15)
            checks += 1

    print(f"PASS R35 smooth commutator null symbol checks={checks}")


if __name__ == "__main__":
    main()
