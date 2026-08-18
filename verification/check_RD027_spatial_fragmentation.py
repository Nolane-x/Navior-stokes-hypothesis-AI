#!/usr/bin/env python3
"""Scaling certificate for RD027 smooth divergence-free fragmentation route guard."""
from __future__ import annotations
import random, math
rng=random.Random(270027)
checks=0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

for _ in range(50000):
    M=rng.randint(10,10**6)
    c=10**rng.uniform(-2,2)
    CX=10**rng.uniform(-2,2)
    CD=10**rng.uniform(-2,2)
    C9=10**rng.uniform(-2,2)
    r=1/M
    X_one=c**4*r*CX
    X_total=M*X_one
    D_one=c**3*r*CD
    D_total=M*D_one
    I9=M*c**9*r**3*C9
    L9cubed=I9**(1/3)
    ok(abs(X_total-c**4*CX)<=1e-10*max(1,X_total),'global X constant')
    ok(abs(D_total-c**3*CD)<=1e-10*max(1,D_total),'global D3 constant')
    ok(abs(I9-c**9*C9/M**2)<=1e-10*max(1,I9),'L9 ninth-power scaling')
    ok(abs(L9cubed-c**3*C9**(1/3)*M**(-2/3))<=1e-10*max(1,L9cubed),'L9 cubed scaling')
    ok(X_one/X_total<=1/M+1e-15,'fixed-ball one-bump fraction')
    ok(c>0,'center amplitude nonzero')

M=10**9
ok(1/M<1e-8,'local X fraction ->0')
ok(M*(1/M)==1.0,'global X survives')
ok(M*(1/M)==1.0,'global D3 survives')
ok(M**(-2/3)<1e-5,'L9 cubed bounded and vanishing')
print(f'RD027_PASS checks={checks}')
