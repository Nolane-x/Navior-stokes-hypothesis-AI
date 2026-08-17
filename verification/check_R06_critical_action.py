#!/usr/bin/env python3
"""Algebra/scaling verification for R06.

This checker verifies the exact constants and local scaling exponents in the
critical Bernoulli/Lamb action reduction. The periodic dual Sobolev inequality
itself is a standard functional-analytic input and is not numerically estimated
here.
"""
from fractions import Fraction

# (2/3)*sqrt(9/8) = 1/sqrt(2), checked after squaring.
assert Fraction(2, 3) ** 2 * Fraction(9, 8) == Fraction(1, 2)

# Young coefficient: a=(C_H/sqrt(2))*X and ab <= (nu/2)b^2+a^2/(2nu)
# gives C_H^2/(4nu) X^2.
assert Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)

# Local Euclidean scaling exponents in 3D.
# ||u||_{3/2}: -1
# ||Q(omega x u)||_2^2: +3
# dt: -2
assert Fraction(-1) + Fraction(3) + Fraction(-2) == 0

# R01/R03 pressure work scaling: QL has 3/2; QG has 1/2.
assert Fraction(3, 2) + Fraction(1, 2) == 2

# D3 also scales with exponent 2.
# rho |grad u|^2 contributes 1 + 4 - 3 = 2.
assert Fraction(1) + Fraction(4) - Fraction(3) == 2

print("PASS R06 defect constant 1/sqrt(2)")
print("PASS R06 Young coefficient C_H^2/(4 nu)")
print("PASS R06 critical action scaling")
print("PASS R06 W3/D3 scaling consistency")
print("SCOPE: algebra/scaling audit only; NOT finiteness of the critical action and NOT global regularity.")
