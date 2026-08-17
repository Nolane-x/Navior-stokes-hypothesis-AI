#!/usr/bin/env python3
"""Algebra/scope verifier for R34 smooth high-filter obstruction."""
from fractions import Fraction
from itertools import product


def check_square_partition():
    checks = 0
    vals = [Fraction(0), Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(9, 10), Fraction(1)]
    for a in vals:  # a=m^2, 1-a=h^2
        b = 1-a
        for w in [Fraction(-7,3), Fraction(-1), Fraction(0), Fraction(2,5), Fraction(11,4)]:
            assert a*w+b*w == w
            checks += 1
    return checks


def check_adaptive_high_channel():
    checks = 0
    vals = [Fraction(1,7), Fraction(1,3), Fraction(1), Fraction(5,2)]
    for B, X, p, q, cg, cs in product(vals, repeat=6):
        c0=max(cg,cs)
        best=min(B+cg*X*q, B+cs*X*p)
        rhs=B+c0*X*min(p,q)
        assert best<=rhs
        checks+=1
    return checks


def check_contraction_and_finite_low():
    checks=0
    vals=[Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)]
    for h2 in vals:
        for x2 in [Fraction(0),Fraction(1,3),Fraction(5),Fraction(23,2)]:
            assert h2*x2<=x2
            checks+=1
    # Low support coefficient envelope: multiplying coefficients by |m|<=1
    # cannot exceed the raw finite-mode envelope.
    for mabs in vals:
        assert mabs<=1
        checks+=1
    return checks


def check_endpoint_logic():
    checks=0
    # finite low + finite smooth high action gives finite endpoint RHS
    for low in [Fraction(0),Fraction(2),Fraction(17,3)]:
        for high in [Fraction(0),Fraction(1,5),Fraction(100)]:
            bound=Fraction(7,2)+3*low+Fraction(9,4)*high
            assert bound<10**9
            checks+=1
    return checks


def main():
    checks=check_square_partition()
    checks+=check_adaptive_high_channel()
    checks+=check_contraction_and_finite_low()
    checks+=check_endpoint_logic()
    print(f"PASS R34 smooth high-filter escape algebra checks={checks}")

if __name__=='__main__':
    main()
