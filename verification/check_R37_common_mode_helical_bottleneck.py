#!/usr/bin/env python3
"""Structural verifier for R37 common-mode/helical channel bottleneck."""
import math
import random
import numpy as np

TOL = 3e-11


def norm(v):
    return float(np.linalg.norm(v))


def helical(k, s, n):
    k = np.array(k, dtype=float)
    a = norm(k)
    kh = k / a
    n = np.array(n, dtype=float)
    n = n / norm(n)
    e2 = np.cross(kh, n)
    h = (n + 1j * s * e2) / math.sqrt(2)
    assert norm(1j * np.cross(k, h) - s * a * h) < 1e-10
    return h


def pq_normal(p, q):
    cr = np.cross(p, q)
    if norm(cr) < 1e-12:
        raise ValueError("collinear")
    return cr / norm(cr)


def proj_q(k, v):
    k = np.array(k, dtype=float)
    return k * np.dot(k, v) / np.dot(k, k)


def proj_p(k, v):
    return v - proj_q(k, v)


def test_helical():
    rng = random.Random(37037)
    checks = 0
    for _ in range(6000):
        while True:
            p = np.array([rng.randint(-7, 7) for _ in range(3)], float)
            q = np.array([rng.randint(-7, 7) for _ in range(3)], float)
            k = p + q
            if norm(p) > 0 and norm(q) > 0 and norm(k) > 0 and norm(np.cross(p, q)) > 1e-8:
                break
        n = pq_normal(p, q)
        a, b, c = norm(p), norm(q), norm(k)
        mu = float(np.dot(p, q) / (a * b))
        sint = norm(np.cross(p, q)) / (a * b)
        ph, qh, kh = p / a, q / b, k / c
        for s in (-1, 1):
            for t in (-1, 1):
                hp, hq = helical(p, s, n), helical(q, t, n)
                x = np.cross(hp, hq)
                x_formula = 0.5j * (t * qh - s * ph) - 0.5 * s * t * sint * n
                assert norm(x - x_formula) < TOL
                direct = np.cross(s * a * hp, hq) + np.cross(t * b * hq, hp)
                f = (s * a - t * b) * x
                assert norm(direct - f) < TOL
                qscalar = (t * (b + a * mu) - s * (a + b * mu)) / c
                qx_formula = 0.5j * qscalar * kh
                assert norm(proj_q(k, x) - qx_formula) < TOL
                if s == t:
                    qf_formula = -0.5j * ((a - b) ** 2) * (1 - mu) / c * kh
                    assert norm(proj_q(k, f) - qf_formula) < 1e-9
                checks += 5

    candidates = []
    vectors = []
    for x in range(-5, 6):
        for y in range(-5, 6):
            for z in range(-5, 6):
                if (x, y, z) != (0, 0, 0):
                    vectors.append(np.array((x, y, z), float))
    by_radius = {}
    for v in vectors:
        by_radius.setdefault(round(float(np.dot(v, v))), []).append(v)
    for r2, vs in by_radius.items():
        if r2 < 2:
            continue
        for i in range(min(len(vs), 30)):
            for j in range(i + 1, min(len(vs), 30)):
                p, q = vs[i], vs[j]
                k = p + q
                if norm(k) > 1e-9 and norm(np.cross(p, q)) > 1e-9:
                    candidates.append((p, q))
                    if len(candidates) >= 300:
                        break
            if len(candidates) >= 300:
                break
        if len(candidates) >= 300:
            break
    assert candidates

    for p, q in candidates:
        n = pq_normal(p, q)
        a, b = norm(p), norm(q)
        assert abs(a - b) < 1e-12
        k = p + q
        c = norm(k)
        mu = float(np.dot(p, q) / (a * b))
        theta = math.acos(max(-1, min(1, mu)))
        for s in (-1, 1):
            t = -s
            hp, hq = helical(p, s, n), helical(q, t, n)
            f = (s * a - t * b) * np.cross(hp, hq)
            assert abs(norm(proj_q(k, f)) - c) < 2e-10
            assert abs(norm(proj_p(k, f)) - c * math.sin(theta / 2)) < 2e-10
            checks += 2

    for p, q in candidates[:100]:
        n = pq_normal(p, q)
        a, b = norm(p), norm(q)
        for s in (-1, 1):
            hp, hq = helical(p, s, n), helical(q, s, n)
            f = (s * a - s * b) * np.cross(hp, hq)
            assert norm(f) < 1e-12
            checks += 1
    return checks


def fft_k(n):
    return np.fft.fftfreq(n) * n


def inner_vec(a, b):
    return float(np.mean(np.sum(a * b, axis=-1)).real)


def inner_tensor(a, b):
    return float(np.mean(np.sum(a * b, axis=(-2, -1))).real)


def test_common_mode():
    rng = np.random.default_rng(37038)
    checks = 0
    for n, cutoff in ((20, 2.7), (24, 3.4), (28, 4.1)):
        ks = fft_k(n)
        kx, ky, kz = np.meshgrid(ks, ks, ks, indexing="ij")
        kv = np.stack([kx, ky, kz], axis=-1)
        k2 = np.sum(kv * kv, axis=-1)
        uhat = np.zeros((n, n, n, 3), dtype=complex)
        raw = rng.normal(size=(n, n, n, 3))
        fh = np.fft.fftn(raw, axes=(0, 1, 2))
        band = (k2 > 0) & (k2 <= 9)
        dot = np.sum(kv * fh, axis=-1)
        qpart = np.zeros_like(fh)
        qpart[band] = kv[band] * (dot[band][:, None] / k2[band][:, None])
        uhat[band] = fh[band] - qpart[band]
        u = np.fft.ifftn(uhat, axes=(0, 1, 2)).real
        omega_hat = 1j * np.cross(kv, uhat)
        omega = np.fft.ifftn(omega_hat, axes=(0, 1, 2)).real
        lamb = np.cross(omega, u)
        rho = np.linalg.norm(u, axis=-1)
        g = rho[..., None] * u
        lh = np.fft.fftn(lamb, axes=(0, 1, 2))
        gh = np.fft.fftn(g, axes=(0, 1, 2))

        def qhat(field):
            d = np.sum(kv * field, axis=-1)
            out = np.zeros_like(field)
            mask = k2 > 0
            out[mask] = kv[mask] * (d[mask][:, None] / k2[mask][:, None])
            return out

        qlh, qgh = qhat(lh), qhat(gh)
        plh, pgh = lh - qlh, gh - qgh
        rad = np.sqrt(k2)
        a_sym = np.exp(-(rad / cutoff) ** 4)
        a_sym[0, 0, 0] = 1.0
        h = np.sqrt(np.maximum(0, 1 - a_sym))

        def filt(field, symbol):
            return np.fft.ifftn(field * symbol[..., None], axes=(0, 1, 2)).real

        hql, hqg = filt(qlh, h), filt(qgh, h)
        hpl, hpg = filt(plh, h), filt(pgh, h)
        hl, hg = filt(lh, h), filt(gh, h)
        w_grad = inner_vec(hql, hqg)
        w_sol = -inner_vec(hpl, hpg)
        jhg = hqg - hpg
        common = 0.5 * (w_grad + w_sol)
        assert abs(common - 0.5 * inner_vec(hl, jhg)) < 2e-10

        am_l = filt(lh, a_sym)
        defect = inner_vec(am_l, g)
        eye = np.eye(3)
        stress = u[..., :, None] * u[..., None, :] - 0.5 * rho[..., None, None] ** 2 * eye
        th = np.fft.fftn(stress, axes=(0, 1, 2))
        ht = np.fft.ifftn(th * h[..., None, None], axes=(0, 1, 2)).real
        grad_gh = np.empty((n, n, n, 3, 3), dtype=complex)
        for j, kk in enumerate((kx, ky, kz)):
            grad_gh[..., :, j] = 1j * kk[..., None] * gh
        hgradg = np.fft.ifftn(grad_gh * h[..., None, None], axes=(0, 1, 2)).real
        assert abs(defect - inner_tensor(ht, hgradg)) < 3e-9
        assert abs((w_grad - w_sol) + defect) < 3e-9
        assert abs(inner_vec(lamb, g)) < 2e-10
        checks += 4

        for _ in range(500):
            uv = rng.normal(size=3)
            rr = norm(uv)
            grad_u = rng.normal(size=(3, 3))
            grad_u -= np.eye(3) * np.trace(grad_u) / 3
            grad_rho = grad_u.T @ uv / rr
            grad_g = rr * grad_u + np.outer(uv, grad_rho)
            stress_jet = np.outer(uv, uv) - 0.5 * rr * rr * np.eye(3)
            q_amp = float(np.dot(uv, grad_rho))
            lhs = float(np.sum(stress_jet * grad_g))
            rhs = 1.5 * rr * rr * q_amp
            assert abs(lhs - rhs) < 2e-10 * (1 + abs(rhs))
            checks += 1
    return checks


def main():
    helical_checks = test_helical()
    common_checks = test_common_mode()
    print(
        "PASS R37 common-mode/helical bottleneck "
        f"checks={helical_checks + common_checks} "
        f"helical={helical_checks} common={common_checks}"
    )
    print("SCOPE: exact structural/finite-grid verification only; NOT global regularity")


if __name__ == "__main__":
    main()
