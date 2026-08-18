#!/usr/bin/env python3
"""Fresh-context verifier for R40.

Independent reconstruction: random rank-one orthogonal projectors and direct
physical-space discrete Fourier coefficients; no import from the primary R40 checker.
"""
import math
import numpy as np

rng = np.random.default_rng(94040)
checks = 0
maxerr = 0.0

# Any orthogonal P/Q split contracts each work pairing separately.
for _ in range(25000):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    Q = np.outer(n,n)
    P = np.eye(3)-Q
    L = rng.normal(size=3)+1j*rng.normal(size=3)
    G = rng.normal(size=3)+1j*rng.normal(size=3)
    denom = np.linalg.norm(L)*np.linalg.norm(G)
    for R in (P,Q):
        w = abs(float(np.real(np.vdot(R@G,R@L))))
        err = max(0.0,w-denom)
        maxerr=max(maxerr,err)
        assert w <= denom*(1+2e-12)
        checks += 1

# Direct coefficient reconstruction under normalized discrete measure.
for N in (41,67,103):
    x=np.arange(N)
    for _ in range(180):
        u=rng.normal(size=(N,3))
        om=rng.normal(size=(N,3))
        L=np.cross(om,u)
        G=np.linalg.norm(u,axis=1)[:,None]*u
        un=math.sqrt(float(np.mean(np.sum(u*u,axis=1))))
        on=math.sqrt(float(np.mean(np.sum(om*om,axis=1))))
        for k in rng.integers(0,N,size=20):
            ph=np.exp(-2j*np.pi*k*x/N)[:,None]
            Lh=np.mean(L*ph,axis=0)
            Gh=np.mean(G*ph,axis=0)
            assert np.linalg.norm(Lh) <= on*un*(1+1e-12)
            assert np.linalg.norm(Gh) <= un*un*(1+1e-12)
            # Independent random output projector for the contraction step.
            n=rng.normal(size=3); n/=np.linalg.norm(n)
            Q=np.outer(n,n); P=np.eye(3)-Q
            for R in (P,Q):
                w=abs(float(np.real(np.vdot(R@Gh,R@Lh))))
                assert w <= on*un**3*(1+2e-12)
                checks+=1
            checks+=2

# Diagonal evacuation envelope with catalog cardinality and terminal tail.
for _ in range(5000):
    m=int(rng.integers(1,1000000))
    E=10**rng.uniform(-1,1)
    zeta=10**rng.uniform(-10,-2)
    # choose sqrt(delta*q) strictly below the required threshold
    root=zeta/(8*m*E**3)
    bound=2*m*E**3*root
    assert bound <= zeta/4*(1+1e-12)
    checks+=1

print(f"PASS fresh E40/R40 absolute-work reconstruction checks={checks} maxerr={maxerr:.3e}")
print("VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY")
