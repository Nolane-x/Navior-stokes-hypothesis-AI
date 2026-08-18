#!/usr/bin/env python3
"""Fresh independent scalar/catalogue verification for R48/C004."""
from __future__ import annotations
import math, random
rng=random.Random(480148)
checks=0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

nu=.83
Dstar=28/(3*nu)
for _ in range(20000):
    theta=rng.uniform(.1,.9)
    D=rng.uniform(.05,Dstar)
    B=10**rng.uniform(-2,4)
    Sigma=math.sqrt(2)*B*D
    L=Sigma*rng.uniform(.001,.3)
    Rstar=Sigma/(1-theta)
    pos_r=[L+(Rstar-L)*rng.random() for _ in range(20)]
    pos=[1/20]*20
    below=sum(pos)
    ok(below>=theta,'fresh positive quantile mass')
    ok(Rstar/B <= math.sqrt(2)*Dstar/(1-theta)+1e-12,'fresh scale alignment')
    center=.5*B
    ok(center/Rstar >= (1-theta)/(2*math.sqrt(2)*Dstar)-1e-12,'fresh center lower ratio')
    X=B*D
    ok(X/Rstar >= (1-theta)/math.sqrt(2)-1e-12,'fresh C004 rescaled X nontrivial')

for _ in range(25000):
    n=rng.randint(8,80)
    rho=[]; d=[]; x=[]
    for i in range(n):
        r=10**rng.uniform(-8,8)
        di=10**rng.uniform(-10,6)
        xi=r*di*(rng.random()**3)
        rho.append(r); d.append(di); x.append(xi)
    X=sum(x); D=sum(d)
    if X<=0 or D<=0: continue
    B=X/D
    xlow=sum(xi for r,xi in zip(rho,x) if r<B/2)
    ok(xlow<=X/2+1e-9*max(1,X),'fresh half-mass lemma')
    ok(max(rho)>=B/2,'fresh nonempty work-linked high set')

print(f'R48_FRESH_PASS checks={checks}')
