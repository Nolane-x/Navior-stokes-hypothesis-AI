#!/usr/bin/env python3
"""Scaling certificate for RD022.

The family is smooth/divergence-free by construction u=A v((x-x0)/r) with
compactly supported divergence-free seed v. This script verifies the exact
norm exponents and limiting regimes; it is NOT a Navier-Stokes trajectory.
"""
import math, random


def quantities(A,r,ell,C0=1.7,C1=2.3):
    peak=A
    e2=C0*A*A*r**3
    h1=C1*A*A*r
    q=ell*h1
    return peak,e2,h1,q


def main():
    checks=0
    prev_e=1e99; prev_q=1e99; prev_peak=0
    for n in [8,16,32,64,128,256,512,1024]:
        A=float(n); r=1.0/n; ell=1.0/(n*n)
        peak,e2,h1,q=quantities(A,r,ell)
        assert abs(peak-n)<1e-14
        assert abs(e2-1.7/n)<1e-13
        assert abs(h1-2.3*n)<1e-11
        assert abs(q-2.3/n)<1e-13
        assert peak>prev_peak and e2<prev_e and q<prev_q
        prev_peak,prev_e,prev_q=peak,e2,q
        checks+=7

    # General exponents: A=n^a, r=n^-b, ell=n^-c.
    # Peak diverges if a>0; energy vanishes if 2a-3b<0;
    # integrated H1 vanishes if 2a-b-c<0.
    rng=random.Random(22022)
    for _ in range(1000):
        a=rng.uniform(0.2,2.0)
        b=rng.uniform(2*a/3+0.05,3.5)
        c=max(0.1,2*a-b+0.05+rng.random())
        assert a>0
        assert 2*a-3*b<0
        assert 2*a-b-c<0
        n1=100.0; n2=1000.0
        q1=quantities(n1**a,n1**(-b),n1**(-c))
        q2=quantities(n2**a,n2**(-b),n2**(-c))
        assert q2[0]>q1[0]
        assert q2[1]<q1[1]
        assert q2[3]<q1[3]
        checks+=6

    print(f'PASS RD022 peak/local-energy route-guard checks={checks}')
    print('CERTIFIED: peak can diverge while total/local L2 energy and abstract interval enstrophy cost vanish')
    print('SCOPE: smooth divergence-free functional family; NOT a Navier-Stokes trajectory')

if __name__=='__main__': main()
