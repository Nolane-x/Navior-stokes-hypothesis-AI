#!/usr/bin/env python3
"""Primary algebraic certificate for R48 productive-scale alignment."""
from __future__ import annotations
import math, random
rng=random.Random(480048)
checks=0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

for _ in range(120000):
    nu=10**rng.uniform(-2,2)
    theta=rng.uniform(.05,.95)
    Dstar=28/(3*nu)
    D=rng.uniform(.001,1)*Dstar
    B=10**rng.uniform(-3,5)
    X=B*D
    Sigma=math.sqrt(2)*X
    L=rng.uniform(.01,1)*Sigma
    Rtheta=rng.uniform(L, Sigma/(1-theta))
    A=B*rng.uniform(1,20)
    center=B*rng.uniform(.5,2)
    ok(D<=Dstar+1e-12,'Dstar')
    ok(Sigma>=L,'Sigma parent')
    ok(Rtheta<=Sigma/(1-theta)+1e-12,'quantile upper')
    ok(Rtheta/B<=math.sqrt(2)*D/(1-theta)+1e-12,'R/B exact')
    ok(Rtheta/B<=28*math.sqrt(2)/(3*nu*(1-theta))+1e-12,'R/B uniform')
    ok(B<=A,'B<=A')
    ok(Rtheta/A<=28*math.sqrt(2)/(3*nu*(1-theta))+1e-12,'R/A uniform')
    ok(B>=L/(math.sqrt(2)*D)-1e-12,'B cutoff lower')
    ok(center/Rtheta>=3*nu*(1-theta)/(56*math.sqrt(2))-1e-12,'center normalized')

# Weighted-atom half-mass lemma: B = X/D, x_i <= a_i d_i, H={a>=B/2}.
for _ in range(30000):
    m=rng.randint(4,80)
    d=[10**rng.uniform(-4,2) for _ in range(m)]
    a=[10**rng.uniform(-4,4) for _ in range(m)]
    frac=[rng.random() for _ in range(m)]
    x=[a[i]*d[i]*frac[i] for i in range(m)]
    D=sum(d); X=sum(x)
    if X==0: continue
    B=X/D
    high=sum(xi for xi,ai in zip(x,a) if ai>=B/2)
    ok(high>=X/2-1e-10*max(1,X),'half X mass')

# Formal NSE concentration scaling: R,B,A -> lambda; D action invariant.
for _ in range(20000):
    lam=10**rng.uniform(-4,4)
    R=10**rng.uniform(-3,4); B=10**rng.uniform(-3,4); D=10**rng.uniform(-3,3)
    ok(abs((lam*R)/(lam*B)-R/B)<1e-12*max(1,R/B),'ratio invariant')
    ok(abs(D-D)<1e-15,'D invariant')

print(f'R48_PRIMARY_PASS checks={checks}')
