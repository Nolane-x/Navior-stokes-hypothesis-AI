#!/usr/bin/env python3
"""Verifier for R42 unit-burst spectral multiplicity explosion.

Audits coefficient/concentration-number inequalities, arbitrarily large signed
cancellation clouds without allocating them explicitly, and R41 good-burst
substitution. Not a continuum global-regularity certificate.
"""
import math
import random
import numpy as np

rng=np.random.default_rng(42042)
prng=random.Random(42042)
checks=0

# Analytic large-multiplicity certificate.  If every positive atom is <=beta,
# at least ceil(theta/beta) atoms are necessary to carry theta positive mass.
# We separately allow the total positive and negative masses to be huge while
# keeping signed total equal to one; cancellation does not alter the count.
for _ in range(50000):
    beta=10**prng.uniform(-12,-0.2)
    theta=prng.uniform(0.01,0.99)
    excess=10**prng.uniform(-4,8)  # positive mass = 1+excess; negative=excess
    positive_total=1.0+excess
    negative_total=excess
    npos=math.ceil(positive_total/beta)
    nneg=math.ceil(negative_total/beta) if negative_total else 0
    need=math.ceil(theta/beta-1e-14)
    assert npos>=need
    assert need*beta+1e-12*max(1.0,theta)>=theta
    if need>1:
        assert (need-1)*beta<theta*(1+1e-12)
    # The clouds can cancel back to net one while every atom respects beta.
    assert abs(positive_total-negative_total-1.0)<1e-8*max(1.0,positive_total)
    assert nneg>=0
    checks+=5

# Moderate explicit signed clouds independently replay the same inequality.
for _ in range(8000):
    beta=prng.uniform(0.01,0.2)
    theta=prng.uniform(0.05,0.95)
    positive_total=prng.uniform(1.0,4.0)
    npos=math.ceil(positive_total/beta)
    pos=np.full(npos,beta)
    pos[-1]=positive_total-beta*(npos-1)
    negative_total=positive_total-1.0
    nneg=math.ceil(negative_total/beta) if negative_total>0 else 0
    neg=np.empty(nneg)
    if nneg:
        neg.fill(-beta)
        neg[-1]=-(negative_total-beta*(nneg-1))
        b=np.concatenate([pos,neg])
    else:
        b=pos
    assert np.max(np.abs(b))<=beta*(1+1e-12)
    assert abs(float(np.sum(b))-1.0)<1e-10
    positive=np.sort(np.maximum(b,0))[::-1]
    cs=np.cumsum(positive)
    m=int(np.searchsorted(cs,theta,side='left'))+1
    assert m+1e-9>=theta/beta
    checks+=3

# Random continuous-time envelopes collapsed to b_k. If |c_k(t)|<=B omega(t),
# then |b_k|<=B sqrt(|J|q_J).
for _ in range(7000):
    nt=prng.randint(5,80); m=prng.randint(5,300)
    dt=10**prng.uniform(-9,-2); B=10**prng.uniform(-2,2)
    omega=np.abs(rng.normal(size=nt))*10**prng.uniform(-2,2)
    coeff=rng.uniform(-1,1,size=(nt,m))
    c=B*omega[:,None]*coeff
    b=np.sum(c,axis=0)*dt
    q=float(np.sum(omega*omega)*dt); length=nt*dt
    beta=B*math.sqrt(length*q)
    assert float(np.max(np.abs(b)))<=beta*(1+1e-12)
    checks+=1

# R41 good-burst quantitative lower bound and diagonal divergence.
previous=None
for n in range(1,2000):
    N=n*n+10
    ell=1/(n+2)**2
    q=1/(n+2)**3
    E=2.7; V=1.0; theta=0.5
    J=4*ell/N; qJ=4*q/N
    beta=(E**3/V)*math.sqrt(J*qJ)
    lower=theta/beta
    formula=theta*V*N/(4*E**3*math.sqrt(ell*q))
    assert abs(lower/formula-1.0)<1e-12
    if previous is not None:
        assert lower>previous
    previous=lower
    checks+=2

# Sparse escape is impossible once beta is small: bounded mode counts cannot
# carry a fixed positive fraction of the normalized net work.
for mcap in [1,2,4,8,16,32,64,128,1024,10**6,10**12]:
    beta=1/(10*mcap)
    assert mcap*beta<0.5
    assert 0.5/beta>mcap
    checks+=2

print(f"PASS R42 spectral multiplicity explosion checks={checks}")
print("SCOPE: conditional mode-concentration algebra only; NOT global regularity")
