#!/usr/bin/env python3
"""Exact/synthetic route guard for RD021.

The constructions are abstract positive lattice work measures satisfying both
R43 coefficient envelopes. They are NOT Navier-Stokes trajectories.
"""
import math


def sub_case(n:int):
    assert n >= 8
    q=n**-2
    ell=n**-8
    alpha=q
    beta=math.sqrt(ell*q)
    side=n*n
    count=side**3
    need=2*n**5
    assert count >= need
    rmin=math.sqrt(3)*n**3
    rmax=math.sqrt(3)*(n**3+n**2-1)
    coeff=1/(2*n**5)
    assert coeff <= beta*(1+1e-15)
    assert coeff <= alpha/rmax*(1+1e-15), (n,coeff,alpha/rmax)
    assert abs(need*coeff-1.0)<1e-15
    return rmax*rmax*ell, rmin, rmax, count, need


def super_case(n:int):
    assert n >= 3
    q=n**-8
    ell=n**-2
    alpha=q
    beta=math.sqrt(ell*q)
    side=2*n**4
    count=side**3
    need=6*n**12
    assert count >= need
    rmin=math.sqrt(3)*n**4
    rmax=math.sqrt(3)*(3*n**4-1)
    coeff=1/(6*n**12)
    assert coeff <= beta*(1+1e-15)
    assert coeff <= alpha/rmax*(1+1e-15), (n,coeff,alpha/rmax)
    assert abs(need*coeff-1.0)<2e-15
    return rmin*rmin*ell, rmin, rmax, count, need


def main():
    checks=0
    prev_sub=None
    prev_super=None
    for n in [8,12,20,32,50,80,128]:
        p,lo,hi,count,need=sub_case(n)
        assert p < 7/n**2
        if prev_sub is not None: assert p < prev_sub
        prev_sub=p
        checks += 7
    for n in [3,4,6,8,12,20,32]:
        p,lo,hi,count,need=super_case(n)
        assert abs(p-3*n**6) <= 1e-12*max(1,p)
        if prev_super is not None: assert p > prev_super
        prev_super=p
        checks += 7
    assert prev_sub < 1e-3
    assert prev_super > 1e8
    checks += 2
    print(f'PASS RD021 parabolic countermodel checks={checks}')
    print(f'sub_parabolic_final={prev_sub:.6e}')
    print(f'super_parabolic_final={prev_super:.6e}')
    print('SCOPE: abstract coefficient measures satisfying both R43 caps; NOT Navier-Stokes trajectories')

if __name__=='__main__': main()
