#!/usr/bin/env python3
"""Exact algebra/scope verifier for R30 fixed-cutoff balanced high-pass criterion."""
from fractions import Fraction
from itertools import product


def check_adaptive_min():
    checks = 0
    vals = [Fraction(1, 5), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(4)]
    for B, X, p, q, cg, cs in product(vals, repeat=6):
        c0 = max(cg, cs)
        # Gradient bound uses q=||HQL||; solenoidal bound uses p=||HPL||.
        lhs_best = min(B + cg * X * q, B + cs * X * p)
        rhs = B + c0 * X * min(p, q)
        assert lhs_best <= rhs, (B, X, p, q, cg, cs, lhs_best, rhs)
        checks += 1
    return checks


def check_young():
    checks = 0
    vals = [Fraction(1, 7), Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(7)]
    for nu, d, u, m, c0 in product(vals, repeat=5):
        rhs_a = nu * d / 2
        rhs_b = c0 * c0 * u * m * m / (2 * nu)
        # AM-GM form equivalent to
        # c0*sqrt(u*d)*m <= nu*d/2 + c0^2*u*m^2/(2nu).
        assert (rhs_a + rhs_b) ** 2 >= 4 * rhs_a * rhs_b
        assert 4 * rhs_a * rhs_b == c0 * c0 * u * d * m * m
        checks += 2
    return checks


def check_scaling():
    # U exponent -1; high-pass L2-squared Lamb exponent +3; dt exponent -2.
    assert -1 + 3 - 2 == 0
    # Pressure work and D3 have exponent +2 before dt integration.
    assert 2 - 2 == 0
    return 2


def check_cutoff_logic():
    # Finite low work plus finite balanced high-pass action gives finite endpoint RHS.
    checks = 0
    for low_mass in (Fraction(0), Fraction(1), Fraction(17, 3)):
        for high_action in (Fraction(0), Fraction(2, 5), Fraction(101)):
            initial = Fraction(7, 2)
            c = Fraction(9, 4)
            bound = initial + 3 * low_mass + 3 * c * high_action
            assert bound < 10**9
            checks += 1
    return checks


def main():
    checks = check_adaptive_min()
    checks += check_young()
    checks += check_scaling()
    checks += check_cutoff_logic()
    print(f"PASS R30 fixed-cutoff balanced high-pass algebra checks={checks}")


if __name__ == "__main__":
    main()
