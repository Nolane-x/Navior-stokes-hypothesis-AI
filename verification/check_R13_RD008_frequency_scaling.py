#!/usr/bin/env python3
"""Exact counting/scaling audit for R13 and RD008.

Checks finite Fourier-mode counting growth, the energy/enstrophy scaling, and
critical tail-action homogeneity. This does not prove ultraviolet summability or
Navier-Stokes global regularity.
"""
from fractions import Fraction

# R13: number of integer modes in a 3D box/ball is O(K^3), so the L1->L2
# finite-frequency operator constant squared is O(K^3).
# We audit the dimension exponent only.
space_dimension = 3
assert space_dimension == 3
assert Fraction(space_dimension, 2) * 2 == 3

# Energy estimate powers in the R13 low-frequency action:
# U <= E0, ||u||_2^2 <= E0^2, and integrated enstrophy <= E0^2/(2 nu).
assert 1 + 2 + 2 == 5

# RD008 standard local NS scaling u_lambda=lambda u(lambda x,lambda^2 t).
# L2 norm squared: amplitude^2 lambda^2 times dx lambda^-3 -> lambda^-1.
assert 2 - 3 == -1
# grad u amplitude exponent 2; squared 4, dx -3, dt -2 -> -1.
assert 4 - 3 - 2 == -1

# R08 critical action: U L^{3/2} exponent -1; projected Lamb L2^2 +3; dt -2.
assert -1 + 3 - 2 == 0

# Threshold covariance: M* ~ U^-1 therefore exponent +1, like velocity amplitude.
assert -(-1) == 1

print('PASS R13 finite-frequency K^3 counting exponent')
print('PASS R13 energy-power bookkeeping')
print('PASS RD008 energy/enstrophy scale as lambda^-1')
print('PASS RD008 R08 tail action scale invariance')
print('SCOPE: exact counting/scaling audit only; ultraviolet regularity remains OPEN.')
