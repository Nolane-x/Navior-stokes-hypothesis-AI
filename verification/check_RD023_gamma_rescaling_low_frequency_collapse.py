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
    Lambda=n**p
    Gamma=Lambda
    A2=Gamma/q
    L=n/2
    b=1/M
    rmin=math.sqrt(3)*n
    rmax=2*math.sqrt(3)*n
    ok(q/rmax >= b-1e-15, 'R43 alpha/|k| cap')
    beta=math.sqrt(ell*q)
    ok(beta >= b-1e-15, 'R42 beta cap')
    ok(ell*rmin >= b-1e-15, 'stress low-mode cap')
    ok(abs(A2*q-Gamma) <=1e-12*Gamma, 'Lambda=Gamma=A^2 q')
    ok(Lambda>=L, 'Lambda>=L')
    ok(Lambda/rmax >=1, 'sharp Lambda high-tail bound through support')
    ok(M>=n**3, 'multiplicity')
    ok(q<2, 'q finite/small sequence')
    ok(ell<1, 'ell finite/small sequence')
    ok(rmax/Lambda <= 2*math.sqrt(3)/n**(p-1)+1e-15, 'Lambda-normalized support')

n=10**6
q=4*math.sqrt(3)/n**2
ell=n**-4
Lambda=n**p
Gamma=Lambda
rmax=2*math.sqrt(3)*n
ok(q<1e-10,'q->0')
ok(ell<1e-20,'ell->0')
ok(n**3>10**12,'multiplicity->infinity')
ok(rmax/Lambda<1e-5,'Lambda-normalized productive cloud ->0')
print(f'RD023_PASS checks={checks}')
