#!/usr/bin/env python3
"""Exact scalar-envelope countermodel for RD023."""
from __future__ import annotations
import math

checks=0

def ok(c,msg):
    global checks
    checks+=1
    if not c: raise AssertionError(msg)

p=2.0
for n in range(4,101):
    M=n**3
    q=4*math.sqrt(3)/n**2
    ell=1/n**4
    Gamma=n**p
    A2=Gamma/q
    L=n/2
    b=1/M
    # Box radii are between sqrt(3)n and 2sqrt(3)n.
    rmin=math.sqrt(3)*n
    rmax=2*math.sqrt(3)*n
    # R43 1/k cap (worst at largest radius).
    ok(q/rmax >= b-1e-15, 'R43 alpha/|k| cap')
    # R42 beta cap.
    beta=math.sqrt(ell*q)
    ok(beta >= b-1e-15, 'R42 beta cap')
    # R45 low stress cap (worst at smallest radius).
    ok(ell*rmin >= b-1e-15, 'stress low-mode cap')
    # Intrinsic UV cap and parent relation.
    ok(abs(A2*q-Gamma) <=1e-12*Gamma, 'Gamma=A^2 q')
    ok(Gamma>=L, 'Gamma>=L')
    # Tail TV model: for R below support TV=1, and Gamma/R >=1 because
    # Gamma >> rmax; above support TV=0.
    ok(Gamma/rmax >=1, 'high-tail bound through support')
    # Multiplicity, small costs, and collapse.
    ok(M>=n**3, 'multiplicity')
    ok(q<2, 'q finite/small sequence')
    ok(ell<1, 'ell finite/small sequence')
    ok(rmax/Gamma <= 2*math.sqrt(3)/n**(p-1)+1e-15, 'normalized support')

# Asymptotic checks at large n.
n=10**6
q=4*math.sqrt(3)/n**2
ell=n**-4
Gamma=n**p
rmax=2*math.sqrt(3)*n
ok(q<1e-10,'q->0')
ok(ell<1e-20,'ell->0')
ok(n**3>10**12,'multiplicity->infinity')
ok(rmax/Gamma<1e-5,'normalized productive cloud ->0')
print(f'RD023_PASS checks={checks}')
