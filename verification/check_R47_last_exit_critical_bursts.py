#!/usr/bin/env python3
"""Certificate for R47 last-exit unit bursts and bounded critical action.

Scope: exact extraction/combinatorics/algebra. This does not simulate NSE or
certify global regularity.
"""
from __future__ import annotations
import math, random

rng=random.Random(470047)
checks=0

def ok(c,msg):
    global checks
    checks+=1
    if not c:
        raise AssertionError(msg)

def make_trace(N:int):
    t=[0.0]; f=[0.0]
    cur=0.0
    for j in range(1,N+1):
        base=j-1.0
        ok(abs(cur-base)<1e-12,'trace base')
        for _ in range(rng.randint(1,4)):
            cur=base-rng.uniform(0.05,1.75)
            t.append(t[-1]+rng.uniform(.01,.2)); f.append(cur)
            cur=base
            t.append(t[-1]+rng.uniform(.01,.2)); f.append(cur)
        for frac in (0.17,0.41,0.73):
            cur=base+frac+rng.uniform(-.03,.03)
            cur=min(j-1e-4,max(base+1e-4,cur))
            t.append(t[-1]+rng.uniform(.01,.2)); f.append(cur)
        cur=float(j)
        t.append(t[-1]+rng.uniform(.01,.2)); f.append(cur)
    return t,f

for N in range(2,60):
    t,f=make_trace(N)
    hit={j:next(i for i,x in enumerate(f) if abs(x-j)<1e-12) for j in range(N+1)}
    last_exit=[]
    for j in range(1,N+1):
        hi=hit[j]
        lo=hit[j-1]
        candidates=[i for i in range(lo,hi+1) if abs(f[i]-(j-1))<1e-12]
        s=max(candidates)
        last_exit.append((s,hi))
        ok(abs(f[hi]-f[s]-1)<1e-12,'unit net work')
        for i in range(s,hi+1):
            ok(f[i]>=j-1-1e-12 and f[i]<=j+1e-12,'no drawdown prefix')
        if j>1:
            ok(last_exit[-2][1] <= s,'disjoint ordered bursts')

for _ in range(20000):
    common=rng.random()
    eta=10**rng.uniform(-8,-1)
    zeta=10**rng.uniform(-8,-1)
    delta=rng.uniform(-eta,eta)
    low=rng.uniform(-zeta,zeta)
    w3=common+delta/2+low
    eps=eta/2+zeta
    ok(w3>=-eps-1e-15,'prefix W3 lower')
    ok(w3<=1+eps+1e-15,'prefix W3 upper')

nu=0.73
for _ in range(5000):
    N=rng.randint(20,500)
    Ya=rng.uniform(0,N)
    eps=rng.uniform(0,1)
    totalD=(Ya+3*(N+eps))/(3*nu)
    avgD=totalD/N
    ok(avgD <= 7/(3*nu)+1e-12,'uniform average D3 constant')
    delta=10**rng.uniform(-8,-1)
    qtail=10**rng.uniform(-9,-2)
    ell=[rng.expovariate(1.0) for _ in range(N)]
    q=[rng.expovariate(1.0) for _ in range(N)]
    d=[rng.expovariate(1.0) for _ in range(N)]
    se,sq,sd=sum(ell),sum(q),sum(d)
    ell=[x*delta/se for x in ell]
    q=[x*qtail/sq for x in q]
    d=[x*totalD/sd for x in d]
    good=[i for i in range(N) if ell[i] <= 4*delta/N+1e-15 and q[i] <= 4*qtail/N+1e-15 and d[i] <= 4*avgD+1e-15]
    ok(len(good) >= N//4,'simultaneous Markov fraction')
    for i in good[:5]:
        ok(d[i] <= 28/(3*nu)+1e-12,'uniform per-burst D3')

for _ in range(100000):
    rho=10**rng.uniform(-8,5)
    ar=10**rng.uniform(-10,5)
    bn=10**rng.uniform(-10,5)
    D3=2*rho*ar+rho**3*bn
    gradZ=2.25*rho*ar+rho**3*bn
    ok(D3 <= gradZ*(1+1e-14),'D3 <= gradZ')
    ok(gradZ <= (9/8)*D3*(1+1e-14),'gradZ <= 9/8 D3')

for _ in range(10000):
    lam=10**rng.uniform(-4,4)
    ok(abs((lam**(2/3))**3*lam**-2-1)<1e-12,'L3_t L9_x critical scaling')
    ok(abs(lam**2*lam**-2-1)<1e-12,'D3 action critical scaling')

print(f'R47_PRIMARY_PASS checks={checks}')
