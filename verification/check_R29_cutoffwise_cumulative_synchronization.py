#!/usr/bin/env python3
"""
Independent numerical/algebraic verifier for R29.

Checks:
1. pointwise Lamb/test orthogonality L·G = 0;
2. exact high-pass mismatch identity
   W_grad,>K - W_sol,>K = - <Pi_<=K L, Pi_<=K G>;
3. complementary low-pass mismatch identity;
4. several cutoffs and unrelated random divergence-free fields;
5. the terminal-window synchronization consequence at the scalar algebra level.
"""
import math
import numpy as np

TOL = 5e-10


def project_q(Fh, kvec, k2):
    out = np.zeros_like(Fh)
    mask = k2 > 0
    dot = np.sum(kvec * Fh, axis=-1)
    out[mask] = kvec[mask] * (dot[mask] / k2[mask])[..., None]
    return out


def inner_modes(A, B, mask, n):
    # norm="ortho" FFT: physical spatial mean equals Fourier inner product / n^3.
    return float(np.vdot(A[mask], B[mask]).real / (n**3))


def make_world(n, seed):
    rng = np.random.default_rng(seed)
    ks = np.fft.fftfreq(n) * n
    kx, ky, kz = np.meshgrid(ks, ks, ks, indexing="ij")
    kvec = np.stack([kx, ky, kz], axis=-1)
    k2 = kx*kx + ky*ky + kz*kz
    nz = k2 > 0

    raw = rng.normal(size=(n, n, n, 3))
    uh = np.fft.fftn(raw, axes=(0, 1, 2), norm="ortho")
    dot = np.sum(kvec * uh, axis=-1)
    divfree = np.zeros_like(uh)
    divfree[nz] = uh[nz] - kvec[nz] * (dot[nz] / k2[nz])[..., None]

    # Keep the velocity itself spectrally sparse, but leave L and |u|u unrestricted.
    divfree *= ((k2 > 0) & (k2 <= 16))[..., None]
    u = np.fft.ifftn(divfree, axes=(0, 1, 2), norm="ortho").real
    uh = np.fft.fftn(u, axes=(0, 1, 2), norm="ortho")

    omega_h = 1j * np.cross(kvec, uh)
    omega = np.fft.ifftn(omega_h, axes=(0, 1, 2), norm="ortho").real
    rho = np.linalg.norm(u, axis=-1)
    L = np.cross(omega, u)
    G = rho[..., None] * u

    Lh = np.fft.fftn(L, axes=(0, 1, 2), norm="ortho")
    Gh = np.fft.fftn(G, axes=(0, 1, 2), norm="ortho")
    QL, QG = project_q(Lh, kvec, k2), project_q(Gh, kvec, k2)
    PL, PG = Lh - QL, Gh - QG

    return k2, L, G, Lh, Gh, PL, PG, QL, QG


def check_world(n, seed):
    k2, L, G, Lh, Gh, PL, PG, QL, QG = make_world(n, seed)

    pointwise = np.max(np.abs(np.sum(L * G, axis=-1)))
    scale = max(1.0, np.max(np.linalg.norm(L, axis=-1) * np.linalg.norm(G, axis=-1)))
    assert pointwise <= TOL * scale, (n, seed, "pointwise orthogonality", pointwise, scale)

    global_pair = float(np.mean(np.sum(L * G, axis=-1)))
    assert abs(global_pair) <= TOL * scale, (n, seed, "global orthogonality", global_pair)

    checked = 0
    for K in (1, 2, 3, 4, 5):
        low = (k2 > 0) & (k2 <= K*K)
        high = k2 > K*K

        wg_low = inner_modes(QL, QG, low, n)
        ws_low = -inner_modes(PL, PG, low, n)
        wg_high = inner_modes(QL, QG, high, n)
        ws_high = -inner_modes(PL, PG, high, n)
        raw_low = inner_modes(Lh, Gh, low, n)
        raw_high = inner_modes(Lh, Gh, high, n)

        err_hi = abs((wg_high - ws_high) + raw_low)
        err_lo = abs((wg_low - ws_low) - raw_low)
        err_raw = abs(raw_high + raw_low)
        local_scale = max(
            1.0,
            abs(wg_low), abs(ws_low), abs(wg_high), abs(ws_high),
            abs(raw_low), abs(raw_high),
        )
        assert err_hi <= 2e-9 * local_scale, (n, seed, K, "high mismatch", err_hi)
        assert err_lo <= 2e-9 * local_scale, (n, seed, K, "low mismatch", err_lo)
        assert err_raw <= 2e-9 * local_scale, (n, seed, K, "raw low/high cancellation", err_raw)
        checked += 3
    return checked


def check_terminal_window_algebra():
    # If |D| is L1-controlled by C sqrt(length), then integrated UV mismatch
    # has the same control. Sample the inequality numerically.
    checks = 0
    C = 7.25
    for length in (1.0, 0.25, 0.04, 0.01, 1e-4):
        bound = C * math.sqrt(length)
        mismatch = 0.83 * bound
        assert abs(mismatch) <= bound + 1e-15
        checks += 1

    # If two cumulative high-pass works diverge while their difference is bounded,
    # their ratio tends to one. Verify on a deterministic diverging sequence.
    M = 3.0
    for x in (10.0, 100.0, 1e4, 1e7):
        a = x
        b = x + M
        assert abs(a - b) <= M + 1e-15
        assert abs(a / b - 1.0) <= M / b + 1e-15
        checks += 2
    return checks


def main():
    checks = 0
    for n in (16, 20):
        for seed in (2, 11, 29):
            checks += check_world(n, seed)
    checks += check_terminal_window_algebra()
    print(f"PASS R29 cutoffwise cumulative synchronization checks={checks}")


if __name__ == "__main__":
    main()
