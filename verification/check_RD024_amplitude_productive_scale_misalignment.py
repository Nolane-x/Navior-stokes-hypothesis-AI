#!/usr/bin/env python3
"""Exact asymptotic scalar countermodels for RD024.

The checker verifies that both Chi=R_theta/A ->0 and Chi->infinity are
compatible with the scalar R43--R46 lower/upper scale constraints.  It does not
construct Navier--Stokes trajectories.
"""
from __future__ import annotations
import math

checks=0

def ok(c,msg):
    global checks
    checks+=1
    if not c: raise AssertionError(msg)

theta=.5
V=E0=1.0
Cq=4*math.sqrt(3)

for n in range(20,2001,20):
    q=Cq/n**2
    ell=n**-4
    L=n/4

    r2=math.sqrt(theta*V/(26*E0**2*q))
    r3=(theta*V/(27*E0**3*math.sqrt(ell*q)))**(1/3)
    r4=(theta*V/(27*E0**4*ell))**.25
    floor=max(r2,r3,r4,L)

    # Branch A: Chi -> 0.
    A=n**1.5
    R=4*n
    Sigma=4*n
    Gamma=A*A*q
    ok(R>=floor,'branch A lower floors')
    ok(A*A*q>=L,'branch A amplitude condition')
    ok(Sigma>=L,'branch A Sigma>=L')
    ok(Sigma<=math.sqrt(2)*Gamma,'branch A Sigma hierarchy')
    ok(R<=Sigma/(1-theta),'branch A quantile upper')
    chiA=R/A
    ok(chiA<=4/math.sqrt(n)+1e-14,'branch A chi formula')

    # Branch B: Chi -> infinity.
    A=n**3
    R=n**3.5
    Sigma=n**3.5
    Gamma=A*A*q
    ok(R>=floor,'branch B lower floors')
    ok(A*A*q>=L,'branch B amplitude condition')
    ok(Sigma>=L,'branch B Sigma>=L')
    ok(Sigma<=math.sqrt(2)*Gamma,'branch B Sigma hierarchy')
    ok(R<=Sigma/(1-theta),'branch B quantile upper')
    chiB=R/A
    ok(abs(chiB-math.sqrt(n))<1e-8*math.sqrt(n),'branch B chi formula')

    # Per-mode cap feasibility by multiplicity choices.
    # A: M=n^3 modes at |k| <= 2sqrt(3)n, b=1/M.
    bA=n**-3
    kA=2*math.sqrt(3)*n
    beta=math.sqrt(ell*q)
    ok(q/kA >= bA-1e-15,'branch A R43 per-mode cap')
    ok(beta >= bA-1e-15,'branch A R42 cap')
    ok(ell*(math.sqrt(3)*n) >= bA-1e-15,'branch A stress cap')

    # B: M=n^6 modes near |k|~n^(7/2), b=n^-6.
    bB=n**-6
    kB=2*n**3.5
    ok(q/kB >= bB-1e-15,'branch B R43 per-mode cap')
    ok(beta >= bB-1e-15,'branch B R42 cap')
    ok(ell*(.5*n**3.5) >= bB-1e-15,'branch B stress cap')

# Explicit asymptotic witnesses.
n=10**8
chiA=4/math.sqrt(n)
chiB=math.sqrt(n)
ok(chiA<1e-3,'Chi A ->0')
ok(chiB>1e3,'Chi B ->infinity')
print(f'RD024_PASS checks={checks}')
