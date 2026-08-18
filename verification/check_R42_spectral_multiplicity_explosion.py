#!/usr/bin/env python3
"""Verifier for R42 unit-burst spectral multiplicity explosion.

Audits coefficient/concentration-number inequalities and severe signed
cancellation examples. Not a continuum global-regularity certificate.
"""
import math
import random
import numpy as np

rng=np.random.default_rng(42042)
prng=random.Random(42042)
checks=0

# Core concentration-number statement on adversarial signed integrated mode work.
# Each |b_k|<=beta and total signed sum is normalized to 1. Any finite positive
# subset carrying theta needs at least theta/beta modes.
for _ in range(12000):
    beta=10**prng.uniform(-5,-0.2)
    theta=prng.uniform(0.05,0.95)
    # Build enough positive atoms at <= beta, plus a large negative cloud and
    # additional positives so total signed mass is exactly one.
    minpos=math.ceil((1.0+prng.uniform(0,20))/beta)
    pos=np.full(minpos,beta)
    target_pos=float(np.sum(pos))
    neg_total=target_pos-1.0
    if neg_total<0:
        # add positives until positive mass exceeds 1
        extra=math.ceil((1.0-target_pos)/beta)+1
        pos=np.concatenate([pos,np.full(extra,beta)])
        target_pos=float(np.sum(pos)); neg_total=target_pos-1.0
    # Split negative mass into atoms of size <= beta.
    nneg=max(1,math.ceil(neg_total/beta)) if neg_total>0 else 0
    neg=[]
    rem=neg_total
    for _j in range(nneg):
        x=min(beta,rem); neg.append(-x); rem-=x
    b=np.concatenate([pos,np.array(neg,dtype=float)]) if neg else pos.copy()
    assert np.max(np.abs(b))<=beta*(1+1e-12)
    assert abs(float(np.sum(b))-1.0)<1e-8
    positive=np.sort(np.maximum(b,0))[::-1]
    cs=np.cumsum(positive)
    m=int(np.searchsorted(cs,theta,side='left'))+1
    assert m+1e-9>=theta/beta
    checks+=3

# Random continuous-time envelopes collapsed to b_k. If |c_k(t)|<=B omega(t),
# then |b_k|<=B sqrt(|J|q_J).
for _ in range(5000):
    nt=prng.randint(5,80); m=prng.randint(5,500)
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
for n in range(1,1000):
    N=n*n+10
    ell=1/(n+2)**2
    q=1/(n+2)**3
    E=2.7; V=1.0; theta=0.5
    J=4*ell/N; qJ=4*q/N
    beta=(E**3/V)*math.sqrt(J*qJ)
    lower=theta/beta
    formula=theta*V*N/(4*E**3*math.sqrt(ell*q))
    assert abs(lower/formula-1.0)<1e-12
    if n>10:
        # crude monotonicity of this explicit diagonal test family
        prevN=(n-1)**2+10; prevell=1/(n+1)**2; prevq=1/(n+1)**3
        prev=theta*V*prevN/(4*E**3*math.sqrt(prevell*prevq))
        assert lower>prev
    checks+=2

# Sparse escape is impossible once beta is small: one/finitely many atoms cannot
# carry half the positive net work.
for mcap in [1,2,4,8,16,32,64,128]:
    beta=1/(10*mcap)
    assert mcap*beta<0.5
    assert 0.5/beta>mcap
    checks+=2

print(f"PASS R42 spectral multiplicity explosion checks={checks}")
print("SCOPE: conditional mode-concentration algebra only; NOT global regularity")
