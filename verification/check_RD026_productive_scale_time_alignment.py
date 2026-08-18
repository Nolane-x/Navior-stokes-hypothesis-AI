#!/usr/bin/env python3
"""Exact scalar countermodel for RD026; not an NSE trajectory."""
from __future__ import annotations
import math
checks=0

def ok(c,m):
    global checks
    checks+=1
    if not c: raise AssertionError(m)

theta=.5
for branch in ('fast','slow'):
    prev_tau=None
    for n in range(4,5001):
        R=float(n); L=R/2; q=R**-2; D=1.0; B=R
        Sigma=math.sqrt(2)*B*D
        ell=R**-4 if branch=='fast' else R**-1
        M=n**3; b=1/M
        tau=R*R*ell
        ok(math.sqrt(ell*q)+1e-18 >= b, 'R42 beta cap')
        ok(q/R+1e-18 >= b, 'R43 alpha/k cap')
        ok(Sigma>=L, 'Sigma parent floor')
        ok(Sigma/R>=1, 'unit tail capacity')
        ok(abs(R/B-1)<1e-15, 'productive/effective amplitude alignment')
        ok((B/2)/R >= .5-1e-15, 'nontrivial normalized center')
        ok(D<=1, 'uniform D3')
        ok(R*R*q >= theta/26, 'q capacity')
        ok(R**3*math.sqrt(ell*q) >= theta/27, 'cubic capacity')
        ok(R**4*ell >= theta/27, 'stress capacity')
        ok(ell<1 and q<1, 'shrinking raw costs')
        if prev_tau is not None:
            if branch=='fast': ok(tau<prev_tau, 'fast tau decreasing')
            else: ok(tau>prev_tau, 'slow tau increasing')
        prev_tau=tau
    n=10**6; R=float(n)
    ell=R**-4 if branch=='fast' else R**-1
    tau=R*R*ell
    if branch=='fast': ok(tau<1e-10, 'fast tau ->0')
    else: ok(tau>1e5, 'slow tau ->infinity')
print(f'RD026_PASS checks={checks}')
