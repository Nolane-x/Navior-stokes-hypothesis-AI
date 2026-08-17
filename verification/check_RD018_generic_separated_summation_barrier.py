#!/usr/bin/env python3
"""Exact exponent verifier for RD018 generic separated-frequency summation barrier."""
from fractions import Fraction


def main():
    checks = 0
    for n in range(0, 101):
        r = Fraction(3, 2) + Fraction(n, 100) * Fraction(1, 2)
        invr = 1 / r
        invs = invr - Fraction(1, 2)
        if invs > 0:
            s = 1 / invs
            beta = 3 * (Fraction(1, 2) - 1 / s)
        else:
            beta = Fraction(3, 2)  # s=infinity endpoint
        alpha = beta - 1
        omega_exp = 2 + 3 / r
        energy_exp = 2 - 3 / r
        assert alpha == 2 - 3 / r
        assert energy_exp == alpha
        assert Fraction(0) <= alpha <= Fraction(1, 2)
        assert Fraction(7, 2) <= omega_exp <= 4
        assert omega_exp > 2
        checks += 6

    endpoints = [
        (Fraction(3, 2), Fraction(0), Fraction(0), Fraction(4)),
        (Fraction(2), Fraction(1, 2), Fraction(1, 2), Fraction(7, 2)),
    ]
    for r, alpha, energy_exp, omega_exp in endpoints:
        assert 2 - 3 / r == alpha
        assert 2 - 3 / r == energy_exp
        assert 2 + 3 / r == omega_exp
        checks += 3

    print(f"PASS RD018 separated summation barrier checks={checks}")


if __name__ == '__main__':
    main()
