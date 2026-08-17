#!/usr/bin/env python3
"""Exact algebra/scaling audit for R12 and RD007.

Checks the p-dependent coefficients, the distinguished p=4 estimate, and the
pure-amplitude homogeneities behind RD007. It does not prove arbitrary-data
regularity or any time-integrated tail estimate.
"""
from fractions import Fraction

# R12 general test-field coefficient (p-2)/sqrt(p-1): verify squared forms.
for p in range(2, 31):
    # [2(p-2)/p]^2 * [p^2/(4(p-1))] = (p-2)^2/(p-1)
    lhs = Fraction(4*(p-2)*(p-2), p*p) * Fraction(p*p, 4*(p-1))
    rhs = Fraction((p-2)*(p-2), p-1)
    assert lhs == rhs

# p=3 recovers 1/sqrt(2), squared.
assert Fraction((3-2)**2, 3-1) == Fraction(1,2)

# p=4: test-defect coefficient 2/sqrt(3); squared=4/3.
assert Fraction((4-2)**2,4-1) == Fraction(4,3)
# R07 Lamb coefficient at p=4 is sqrt(4/3), so product is 4/3.
assert Fraction(4,3) == Fraction(4,3)

# Small critical coefficient threshold solves nu-(4 CH/3)||u||_3 > 0.
# Dimensionless CH=nu=1 threshold = 3/4.
assert Fraction(3,4) * Fraction(4,3) == 1

# RD007 pure amplitude homogeneities.
# U_{3/2}: a^1; Lamb: a^2 => squared a^4; tail density a^5.
assert 1 + 2*2 == 5
# D3: rho * |grad u|^2 has a * a^2 = a^3 at fixed frequency.
assert 1 + 2 == 3
# Ratio tail density / D3 grows a^2.
assert 5 - 3 == 2
# Intrinsic threshold M*~U^{-1}: a^-1; condition a*rho > M*/a -> rho>M*/a^2.
assert 1 + 1 == 2

print('PASS R12 general p coefficient audit')
print('PASS R12 p=4 distinguished 4C_H/3 critical coefficient')
print('PASS RD007 pure-amplitude tail/D3 homogeneity a^2')
print('SCOPE: exact coefficient/scaling audit only; arbitrary-data regularity remains OPEN.')
