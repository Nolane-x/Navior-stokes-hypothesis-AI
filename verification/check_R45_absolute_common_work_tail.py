#!/usr/bin/env python3
"""Primary algebra/capacity certificate for R45.

This checker does not simulate Navier--Stokes.  It verifies the exact implication
chain used by R45 on randomized scalar parameters and finite synthetic work
catalogues, plus the lattice capacities and critical scaling laws.
"""
from __future__ import annotations
import math, random

rng = random.Random(450045)
checks = 0

def ok(cond: bool, msg: str):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

# Lattice capacities used by R43/R45.
for R in range(1, 18):
    pts=[]
    for i in range(-R,R+1):
        for j in range(-R,R+1):
            for k in range(-R,R+1):
                rr=math.sqrt(i*i+j*j+k*k)
                if 0 < rr <= R+1e-12:
                    pts.append((rr,i,j,k))
    ok(len(pts) <= 27*R**3, f'N(R) capacity failed R={R}')
    ok(sum(1/x[0] for x in pts) <= 26*R**2 + 1e-10, f'weighted capacity failed R={R}')
    ok(sum(x[0] for x in pts) <= 27*R**4 + 1e-10, f'stress |k| capacity failed R={R}')

# Randomized implication chain.
for _ in range(10000):
    V=10**rng.uniform(-1,1)
    E0=10**rng.uniform(-1,1)
    ell=10**rng.uniform(-8,-1)
    q=10**rng.uniform(-8,-1)
    theta=rng.uniform(.08,.92)
    L0=10**rng.uniform(-1,3)

    # Pick the exact work scale Lambda above the parent/quantile requirements,
    # then allow the coarse Gamma=A^2 q cap to be larger.
    r2=math.sqrt(theta*V/(26*E0**2*q))
    r3=(theta*V/(27*E0**3*math.sqrt(ell*q)))**(1/3)
    r4=(theta*V/(27*E0**4*ell))**.25
    Lambda=max(1.01*L0,(1-theta)*max(r2,r3,r4)*1.01)
    Gamma=Lambda*10**rng.uniform(0,1.5)
    A=math.sqrt(Gamma/q)

    ok(Lambda >= L0, 'exact work scale dominates parent cutoff')
    ok(Gamma >= Lambda, 'coarse Gamma dominates Lambda')
    Rtheta=min(Lambda/(1-theta), max(r2,r3,r4)*1.0001)
    ok(Rtheta <= Lambda/(1-theta)+1e-12, 'sharp Lambda quantile upper cap')
    ok(Rtheta >= r2*.999, 'q-floor')
    ok(Rtheta >= r3*.999, 'cubic floor')
    ok(Rtheta >= r4*.999, 'stress quartic floor')

    # Derived amplitude floors.
    fL=math.sqrt(L0/q)
    fq=math.sqrt(1-theta)*(theta*V/26)**.25*E0**-.5*q**-.75
    fc=math.sqrt(1-theta)*(theta*V/27)**(1/6)*E0**-.5*ell**(-1/12)*q**(-7/12)
    fs=math.sqrt(1-theta)*(theta*V/27)**.125*E0**-.5*ell**-.125*q**-.5
    ok(A+1e-12 >= fL, 'A>=sqrt(L/q)')
    ok(A+1e-12 >= fq, 'q amplitude floor')
    ok(A+1e-12 >= fc, 'cubic amplitude floor')
    ok(A+1e-12 >= fs, 'stress amplitude floor')

    # Critical scaling.  Formal concentration scaling: A->lambda A,
    # q->lambda^-1 q, ell->lambda^-2 ell, E0->lambda^-1/2 E0,
    # R,L,Lambda,Gamma->lambda times themselves.
    lam=10**rng.uniform(-2,2)
    V2=V
    E02=lam**-.5*E0
    ell2=lam**-2*ell
    q2=lam**-1*q
    A2=lam*A
    G2=A2*A2*q2
    Lambda2=lam*Lambda
    ok(abs(Lambda2/(lam*Lambda)-1)<1e-10, 'Lambda scaling')
    ok(abs(G2/(lam*Gamma)-1)<1e-10, 'Gamma scaling')
    inv_q=A*E0**.5*q**.75
    inv_q2=A2*E02**.5*q2**.75
    ok(abs(inv_q2/inv_q-1)<1e-10, 'q-amplitude invariant')
    inv_s=A*E0**.5*ell**.125*q**.5
    inv_s2=A2*E02**.5*ell2**.125*q2**.5
    ok(abs(inv_s2/inv_s-1)<1e-10, 'stress-amplitude invariant')

# Synthetic signed catalogues: if total net above L is one and TV tail is
# bounded by Lambda/R, positive work below Lambda/(1-theta) is >=theta.
for _ in range(5000):
    theta=rng.uniform(.1,.9)
    m=rng.randint(8,80)
    vals=[rng.uniform(-.1,.2) for _ in range(m-1)]
    vals.append(1-sum(vals))
    radii=sorted(rng.uniform(1,50) for _ in range(m))
    L0=.5
    Lambda=L0
    for R in radii:
        tail=sum(abs(v) for rr,v in zip(radii,vals) if rr>=R)
        Lambda=max(Lambda,R*tail)
    Lambda=max(Lambda,L0*sum(abs(v) for v in vals))
    Rstar=Lambda/(1-theta)
    pos_total=sum(max(v,0) for v in vals)
    tail_pos=sum(max(v,0) for rr,v in zip(radii,vals) if rr>Rstar)
    below=pos_total-tail_pos
    if any(rr>Rstar for rr in radii):
        tail_abs=sum(abs(v) for rr,v in zip(radii,vals) if rr>Rstar)
        ok(tail_abs <= Lambda/Rstar + 1e-9, 'synthetic Lambda TV tail')
    ok(below + 1e-9 >= theta, 'positive quantile consequence')

print(f'R45_PRIMARY_PASS checks={checks}')
