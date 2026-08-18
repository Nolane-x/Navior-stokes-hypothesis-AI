#!/usr/bin/env python3
"""Fresh E47 verifier using independent trace geometry and finite-difference Z derivative.

Does not import the primary R47 checker.
"""
from __future__ import annotations
import math, random
import numpy as np

rng=random.Random(470147)
checks=0
max_fd_rel=0.0
max_ratio=0.0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

for trial in range(1000):
    N=rng.randint(3,30)
    pieces=[]
    t=0.0; f=0.0
    first_hit={0:0.0}
    last_exit={}
    for j in range(1,N+1):
        base=float(j-1)
        for _ in range(rng.randint(2,5)):
            low=base-rng.uniform(.1,3.0)
            dt=rng.uniform(.01,.1)
            pieces.append((t,t+dt,f,low)); t+=dt; f=low
            dt=rng.uniform(.01,.1)
            pieces.append((t,t+dt,f,base)); t+=dt; f=base
        last_exit[j]=t
        for target in (base+.2,base+.55,base+.82,float(j)):
            dt=rng.uniform(.01,.1)
            pieces.append((t,t+dt,f,target)); t+=dt; f=target
        first_hit[j]=t
    for j in range(1,N+1):
        s=last_exit[j]; e=first_hit[j]
        ok(e>s,'positive burst length')
        vals=[]
        for t0,t1,f0,f1 in pieces:
            if t1 < s-1e-15 or t0 > e+1e-15: continue
            lo=max(t0,s); hi=min(t1,e)
            if hi < lo: continue
            for a in np.linspace(0,1,9):
                tt=lo+a*(hi-lo)
                frac=(tt-t0)/(t1-t0) if t1>t0 else 0
                vals.append(f0+frac*(f1-f0))
        ok(min(vals)>=j-1-1e-12,'fresh no drawdown')
        ok(max(vals)<=j+1e-12,'fresh no overshoot')
        ok(abs(vals[0]-(j-1))<1e-10,'fresh starts at level')
        ok(abs(vals[-1]-j)<1e-10,'fresh ends at next level')

for _ in range(50000):
    u=np.array([rng.gauss(0,1) for _ in range(3)],dtype=float)
    if np.linalg.norm(u)<.15:
        u[0]+=1.0
    J=np.array([[rng.gauss(0,1) for _ in range(3)] for __ in range(3)],dtype=float)
    J[2,2]=-(J[0,0]+J[1,1])
    rho=np.linalg.norm(u)
    D3=rho*np.sum(J*J) + sum(float(np.dot(u,J[:,j]))**2/rho for j in range(3))
    eps=1e-6/max(1.0,np.linalg.norm(J))
    def Z(v):
        return math.sqrt(np.linalg.norm(v))*v
    gradZ=np.zeros((3,3))
    for j in range(3):
        gradZ[:,j]=(Z(u+eps*J[:,j])-Z(u-eps*J[:,j]))/(2*eps)
    g=float(np.sum(gradZ*gradZ))
    ratio=g/D3
    max_ratio=max(max_ratio,ratio)
    ok(ratio>=1-2e-7,'fresh D3 lower ratio')
    ok(ratio<=9/8+2e-7,'fresh D3 upper ratio')
    analytic=np.zeros((3,3))
    for j in range(3):
        v=J[:,j]
        analytic[:,j]=math.sqrt(rho)*v + 0.5*(np.dot(u,v)/(rho**1.5))*u
    rel=np.linalg.norm(gradZ-analytic)/max(1e-12,np.linalg.norm(analytic))
    max_fd_rel=max(max_fd_rel,rel)
    ok(rel<2e-7,'finite difference derivative consistency')

print(f'R47_FRESH_PASS checks={checks} max_fd_rel={max_fd_rel:.3e} max_gradZ_D3_ratio={max_ratio:.12f}')
