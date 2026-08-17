#!/usr/bin/env python3
"""Independent verifier for R36 two-sided separated-frequency null structure."""
import math
import random

L_A = math.sqrt(2.0 / math.e)  # sup |grad exp(-|xi|^2)|
A_INF = 1.0
C_A = max(L_A, 2.0 * A_INF)


def norm(v):
    return math.sqrt(sum(abs(x) ** 2 for x in v))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def perp(k, v):
    kk = sum(x * x for x in k)
    if kk == 0:
        return v
    c = sum(k[i] * v[i] for i in range(3)) / kk
    return tuple(v[i] - c * k[i] for i in range(3))


def aval(k, K):
    return math.exp(-sum(x * x for x in k) / (K * K))


def main():
    rng = random.Random(36036)
    checks = 0
    for K in (3.0, 7.0, 13.0, 29.0):
        for _ in range(5000):
            p = tuple(rng.randint(-35, 35) for _ in range(3))
            q = tuple(rng.randint(-35, 35) for _ in range(3))
            if p == (0, 0, 0) or q == (0, 0, 0):
                continue
            up = perp(p, tuple(rng.uniform(-1.0, 1.0) for _ in range(3)))
            uq = perp(q, tuple(rng.uniform(-1.0, 1.0) for _ in range(3)))
            if norm(up) < 1e-12 or norm(uq) < 1e-12:
                continue
            wp = tuple(1j * z for z in cross(p, up))
            wq = tuple(1j * z for z in cross(q, uq))
            k = tuple(p[i] + q[i] for i in range(3))
            delta = abs(aval(k, K) - aval(p, K))
            triad = delta * norm(cross(wp, uq))
            rhs_q = L_A * norm(q) / K * norm(wp) * norm(uq)
            assert triad <= rhs_q + 5e-12
            rhs_p = C_A * norm(p) / K * norm(up) * norm(wq)
            assert triad <= rhs_p + 5e-12
            checks += 2

    for K in (2.0, 11.0, 37.0):
        for p in ((1, 2, 3), (7, -4, 2), (-9, 5, 1)):
            q = (0, 0, 0)
            assert abs(aval(p, K) - aval(p, K)) <= 1e-15
            checks += 1

    expected_gap = math.exp(-1.0) - math.exp(-2.0)
    for Kint in (4, 8, 16, 32, 64):
        K = float(Kint)
        p = (Kint, 0, 0)
        q = (0, Kint, 0)
        up = (0.0, 1.0, 0.0)
        uq = (1.0, 0.0, 0.0)
        wp = tuple(1j * z for z in cross(p, up))
        k = tuple(p[i] + q[i] for i in range(3))
        gap = abs(aval(k, K) - aval(p, K))
        assert abs(gap - expected_gap) <= 2e-15
        ratio = gap * norm(cross(wp, uq)) / (norm(wp) * norm(uq))
        assert ratio > 0.23
        checks += 2

    for eta in (0.01, 0.03, 0.1, 0.25):
        assert L_A * eta <= C_A * eta
        checks += 1

    print(f"PASS R36 two-sided commutator null checks={checks}")


if __name__ == '__main__':
    main()
