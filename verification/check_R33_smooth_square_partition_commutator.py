#!/usr/bin/env python3
"""Independent verifier for R33 smooth square-partition identities.

Uses two lineages:
1. exact rational finite-mode weighted Helmholtz algebra with m^2+h^2=1;
2. physical/Fourier grid reconstruction of the commutator pairing.
"""
from fractions import Fraction
import random
import numpy as np

TOL = 2e-9


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def qproj(k, v):
    kk = dot(k, k)
    kv = dot(k, v)
    return tuple(ki * kv / kk for ki in k)


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def exact_mode_algebra():
    rng = random.Random(33033)
    checks = 0
    for _ in range(1000):
        k = tuple(Fraction(rng.randint(-4, 4)) for _ in range(3))
        if dot(k, k) == 0:
            continue
        L = tuple(Fraction(rng.randint(-7, 7), rng.randint(1, 5)) for _ in range(3))
        G = tuple(Fraction(rng.randint(-7, 7), rng.randint(1, 5)) for _ in range(3))
        a = Fraction(rng.randint(0, 20), 20)  # m^2
        b = 1-a                              # h^2

        QL, QG = qproj(k, L), qproj(k, G)
        PL, PG = sub(L, QL), sub(G, QG)

        wgrad = dot(QL, QG)
        wsol = -dot(PL, PG)
        low_grad = a * wgrad
        high_grad = b * wgrad
        low_sol = a * wsol
        high_sol = b * wsol

        assert low_grad + high_grad == wgrad
        assert low_sol + high_sol == wsol
        assert (high_grad-high_sol) == b * dot(L, G)
        assert (low_grad-low_sol) == a * dot(L, G)
        checks += 4
    return checks


def project_q(Fh, kvec, k2):
    out = np.zeros_like(Fh)
    mask = k2 > 0
    d = np.sum(kvec * Fh, axis=-1)
    out[mask] = kvec[mask] * (d[mask] / k2[mask])[..., None]
    return out


def grid_commutator():
    checks = 0
    n = 18
    rng = np.random.default_rng(330033)
    ks = np.fft.fftfreq(n) * n
    kx, ky, kz = np.meshgrid(ks, ks, ks, indexing='ij')
    kvec = np.stack([kx, ky, kz], axis=-1)
    k2 = kx*kx + ky*ky + kz*kz
    nz = k2 > 0

    raw = rng.normal(size=(n,n,n,3))
    uh = np.fft.fftn(raw, axes=(0,1,2), norm='ortho')
    d = np.sum(kvec*uh, axis=-1)
    uh[nz] -= kvec[nz]*(d[nz]/k2[nz])[...,None]
    uh[~nz] = 0
    uh *= (k2 <= 16)[...,None]
    u = np.fft.ifftn(uh, axes=(0,1,2), norm='ortho').real
    uh = np.fft.fftn(u, axes=(0,1,2), norm='ortho')

    wh = 1j*np.cross(kvec, uh)
    omega = np.fft.ifftn(wh, axes=(0,1,2), norm='ortho').real
    rho = np.linalg.norm(u, axis=-1)
    G = rho[...,None]*u
    L = np.cross(omega,u)
    Gh = np.fft.fftn(G, axes=(0,1,2), norm='ortho')
    Lh = np.fft.fftn(L, axes=(0,1,2), norm='ortho')

    # Smooth square partition: theta goes smoothly from 0 to pi/2 over radii.
    r = np.sqrt(k2)
    K = 3.0
    s = np.clip((r/K - 0.6)/1.2, 0.0, 1.0)
    smoothstep = s*s*(3-2*s)
    theta = 0.5*np.pi*smoothstep
    m = np.cos(theta)
    h = np.sin(theta)
    assert np.max(np.abs(m*m+h*h-1.0)) < 1e-14

    QL,QG = project_q(Lh,kvec,k2), project_q(Gh,kvec,k2)
    PL,PG = Lh-QL, Gh-QG
    vol = n**3
    inn = lambda A,B: float(np.vdot(A,B).real/vol)

    W = inn(QL,QG)
    Wm = inn(m[...,None]*QL,m[...,None]*QG)
    Wh = inn(h[...,None]*QL,h[...,None]*QG)
    assert abs(W-(Wm+Wh)) <= TOL*max(1.0,abs(W))
    checks += 1

    Ws = -inn(PL,PG)
    Wsm = -inn(m[...,None]*PL,m[...,None]*PG)
    Wsh = -inn(h[...,None]*PL,h[...,None]*PG)
    assert abs(Ws-(Wsm+Wsh)) <= TOL*max(1.0,abs(Ws))
    checks += 1

    high_mismatch = Wh-Wsh
    low_raw = inn(m[...,None]*Lh,m[...,None]*Gh)
    assert abs(high_mismatch+low_raw) <= TOL*max(1.0,abs(high_mismatch),abs(low_raw))
    checks += 1

    # Commute M^2 through the cross-product multiplication operator.
    m2 = m*m
    M2L = np.fft.ifftn(m2[...,None]*Lh, axes=(0,1,2), norm='ortho').real
    M2omega = np.fft.ifftn(m2[...,None]*wh, axes=(0,1,2), norm='ortho').real
    comm = M2L - np.cross(M2omega,u)
    lhs = float(np.mean(np.sum(M2L*G,axis=-1)))
    rhs = float(np.mean(np.sum(comm*G,axis=-1)))
    assert abs(lhs-rhs) <= TOL*max(1.0,abs(lhs),abs(rhs))
    checks += 1

    pointzero = np.max(np.abs(np.sum(np.cross(M2omega,u)*G,axis=-1)))
    assert pointzero <= TOL*max(1.0,np.max(np.linalg.norm(M2omega,axis=-1)*np.linalg.norm(u,axis=-1)*np.linalg.norm(G,axis=-1)))
    checks += 1
    return checks


def main():
    checks = exact_mode_algebra() + grid_commutator()
    print(f'PASS R33 smooth square-partition commutator checks={checks}')


if __name__ == '__main__':
    main()
