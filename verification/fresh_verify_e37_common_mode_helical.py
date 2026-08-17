#!/usr/bin/env python3
"""Independent E37 reconstruction: eigensolver helical basis + abstract common mode."""
import math
import random
import numpy as np


def norm(v):
    return float(np.linalg.norm(v))


def cross_matrix(k):
    x, y, z = k
    return np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]], dtype=complex)


def helical_eigenvector(k, s):
    k = np.asarray(k, float)
    a = norm(k)
    vals, vecs = np.linalg.eig(1j * cross_matrix(k))
    j = int(np.argmin(np.abs(vals - s * a)))
    v = vecs[:, j]
    v = v / norm(v)
    v = v - k * np.dot(k, v) / np.dot(k, k)
    v = v / norm(v)
    assert norm(1j * np.cross(k, v) - s * a * v) < 2e-10
    return v


def qproj(k, v):
    k = np.asarray(k, float)
    return k * np.dot(k, v) / np.dot(k, k)


def pproj(k, v):
    return v - qproj(k, v)


def main():
    rng = random.Random(937037)
    checks = 0
    maxerr = 0.0
    for _ in range(5000):
        while True:
            p = np.array([rng.randint(-10, 10) for _ in range(3)], float)
            q = np.array([rng.randint(-10, 10) for _ in range(3)], float)
            k = p + q
            if norm(p) > 0 and norm(q) > 0 and norm(k) > 0 and norm(np.cross(p, q)) > 1e-8:
                break
        a, b, c = norm(p), norm(q), norm(k)
        mu = float(np.dot(p, q) / (a * b))
        sint = norm(np.cross(p, q)) / (a * b)
        for s in (-1, 1):
            for t in (-1, 1):
                hp = helical_eigenvector(p, s)
                hq = helical_eigenvector(q, t)
                direct = np.cross(s * a * hp, hq) + np.cross(t * b * hq, hp)
                f = (s * a - t * b) * np.cross(hp, hq)
                assert norm(direct - f) < 3e-10
                if s == t:
                    q_expected = (a - b) ** 2 * (1 - mu) / (2 * c)
                    p_expected = abs(a - b) * sint * 0.5 * math.sqrt(1 + (a + b) ** 2 / c**2)
                else:
                    q_expected = (a + b) ** 2 * (1 + mu) / (2 * c)
                    p_expected = (a + b) * sint * 0.5 * math.sqrt(1 + (a - b) ** 2 / c**2)
                err = max(
                    abs(norm(qproj(k, f)) - q_expected),
                    abs(norm(pproj(k, f)) - p_expected),
                )
                maxerr = max(maxerr, err)
                assert err < 5e-9
                checks += 3

    # Independently verify the Helmholtz-reflection common-mode algebra.
    rng2 = np.random.default_rng(937038)
    for _ in range(10000):
        k = rng2.normal(size=3)
        k = k / norm(k)
        qmat = np.outer(k, k)
        pmat = np.eye(3) - qmat
        jmat = qmat - pmat
        lamb = rng2.normal(size=3) + 1j * rng2.normal(size=3)
        g = rng2.normal(size=3) + 1j * rng2.normal(size=3)
        h = float(rng2.random())
        inner = lambda x, y: np.vdot(x, y).real
        w_grad = h * h * inner(qmat @ lamb, qmat @ g)
        w_sol = -h * h * inner(pmat @ lamb, pmat @ g)
        common = 0.5 * (w_grad + w_sol)
        assert abs(2 * common - h * h * inner(lamb, jmat @ g)) < 2e-12
        checks += 1

    print(
        f"PASS fresh E37 common-mode/helical reconstruction checks={checks} "
        f"maxerr={maxerr:.3e}"
    )
    print("VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY")


if __name__ == "__main__":
    main()
