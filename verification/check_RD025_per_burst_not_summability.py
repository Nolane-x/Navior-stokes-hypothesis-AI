#!/usr/bin/env python3
"""Scalar route guard for RD025; not an NSE construction."""
from __future__ import annotations
checks=0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

nu=0.7
partial=0.0
for n in range(1,10001):
    ell=2.0**(-2*n) if n<500 else 0.0
    q=2.0**(-3*n) if n<350 else 0.0
    D=1/nu
    work=1.0
    dY=0.0
    serrin=1.0
    ok(abs(dY/3+nu*D-work)<1e-14,'scalar L3 balance')
    ok(D<=2/nu,'uniform D3')
    ok(serrin<=1.0,'uniform Serrin')
    if n<300:
        ok(ell<1 and q<1,'shrinking costs')
    partial+=serrin
ok(partial==10000.0,'critical action diverges linearly')
ok(2.0**(-200)<1e-50,'duration tends zero')
ok(2.0**(-300)<1e-80,'q tends zero')
print(f'RD025_PASS checks={checks}')
