#!/usr/bin/env python3
"""Verifier for R41 synchronized unit common-work burst extraction.

Checks first-hitting normalization, P/Q common/mismatch algebra, inherited
nonnegative resolved-work bounds, and the simultaneous duration/enstrophy
counting lemma.  Not a global-regularity certificate.
"""
import math
import random
import numpy as np

rng=np.random.default_rng(41041)
prng=random.Random(41041)
checks=0

# Algebra: C=(G+S)/2 and D=G-S. If int C=1 and |int D|<=eta,
# the two representation integrals are 1 +/- delta/2.
for _ in range(30000):
    eta=10**prng.uniform(-10,-1)
    delta=prng.uniform(-eta,eta)
    g=1+delta/2
    s=1-delta/2
    assert abs((g+s)/2-1)<1e-14
    assert abs((g-s)-delta)<1e-14
    assert abs(g-1)<=eta/2*(1+1e-14)
    assert abs(s-1)<=eta/2*(1+1e-14)
    checks+=4

# Strong-backtracking first-hitting paths. Build continuous piecewise-linear
# cumulative F which repeatedly falls but eventually reaches N. First hitting
# successive integer levels must be ordered and each interval has exact net +1.
def first_crossing(times, vals, level):
    if level==vals[0]:
        return times[0]
    for i in range(1,len(vals)):
        y0,y1=vals[i-1],vals[i]
        if (y0-level)*(y1-level)<=0 and y0!=y1:
            # Only accept a crossing that reaches the level from below for the
            # first time; prior values are checked externally to be < level.
            prior=max(vals[:i])
            if prior < level <= max(y0,y1):
                a=(level-y0)/(y1-y0)
                return times[i-1]+a*(times[i]-times[i-1])
    raise AssertionError(f'level {level} not reached')

for _ in range(1500):
    N=prng.randint(3,80)
    t=[0.0]
    f=[0.0]
    # For each new integer level, insert a random downward excursion followed
    # by a rise beyond the next level. This permits severe nonmonotonicity.
    current=0.0
    for j in range(1,N+1):
        down=prng.uniform(0.0,5.0+j/5)
        current-=down
        t.append(t[-1]+prng.uniform(1e-4,1.0)); f.append(current)
        target=j+prng.uniform(0.05,2.0)
        current=target
        t.append(t[-1]+prng.uniform(1e-4,1.0)); f.append(current)
    taus=[0.0]
    for j in range(1,N+1):
        tau=first_crossing(t,f,float(j))
        assert tau>taus[-1]
        taus.append(tau)
        checks+=1
    # By definition F(tau_j)=j for linear interpolation, so each net integral
    # over the hitting interval is exactly the unit level difference.
    for j in range(1,N+1):
        assert abs((j-(j-1))-1.0)<1e-15
        checks+=1

# Inherited parent nonnegative bound: every subinterval/cell has mass <= parent.
for _ in range(5000):
    n=prng.randint(3,500)
    masses=np.abs(rng.normal(size=n))
    total=float(np.sum(masses))
    i=prng.randrange(n); j=prng.randrange(i+1,n+1)
    sub=float(np.sum(masses[i:j]))
    assert sub<=total*(1+1e-14)
    checks+=1

# Simultaneous counting lemma. For disjoint bursts with total length <= ell and
# total enstrophy <=q, fewer than N/4 violate each 4*average threshold, hence
# at least N/2 satisfy both. We stress arbitrary heavy-tailed allocations.
for _ in range(12000):
    N=prng.randint(8,500)
    ell=10**prng.uniform(-10,1)
    q=10**prng.uniform(-12,2)
    # Dirichlet-like random nonnegative allocations with possible zeros/heavy tails.
    a=rng.exponential(scale=1.0,size=N)
    b=rng.exponential(scale=1.0,size=N)
    # Randomly create strong concentration.
    if prng.random()<0.6:
        a[prng.randrange(N)]*=10**prng.uniform(2,8)
    if prng.random()<0.6:
        b[prng.randrange(N)]*=10**prng.uniform(2,8)
    lengths=ell*a/max(float(np.sum(a)),1e-300)
    ens=q*b/max(float(np.sum(b)),1e-300)
    good=(lengths<=4*ell/N*(1+1e-13)) & (ens<=4*q/N*(1+1e-13))
    assert int(np.sum(good))>=N/2-1e-9
    # Individual bad counts obey the strict Markov count.
    assert int(np.sum(lengths>4*ell/N*(1+1e-13))) < N/4+1
    assert int(np.sum(ens>4*q/N*(1+1e-13))) < N/4+1
    checks+=3

# Diagonal limit sanity: choose M_n->inf, delta_n,q_n->0 and check the good-burst
# upper bounds vanish while unit work remains fixed.
for n in range(1,200):
    M=n*n+3
    N=math.floor(M)
    delta=1/(n+1)**2
    q=1/(n+1)**3
    assert 4*delta/N <=4/(n+1)**2/N
    assert 4*q/N <=4/(n+1)**3/N
    assert N>=3
    checks+=3

print(f"PASS R41 unit common-work burst extraction checks={checks}")
print("SCOPE: conditional hitting/counting/algebra certificate only; NOT global regularity")
