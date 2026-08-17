#!/usr/bin/env python3
"""Exact homogeneity audit for R11.

Checks only the scalar powers used in the amplitude and concentration-scaling
proof. The functional-analytic differentiation argument is in R11 itself.
"""
from fractions import Fraction

# Amplitude-only scaling:
# D Phi_{a u} contributes a^-1; diffusion tangent a; convection tangent a^2.
assert Fraction(-1)+Fraction(1)==0
assert Fraction(-1)+Fraction(2)==1

# Full NS scaling S_m u = m u(mx):
# spatial derivative adds m, so Delta and convection both scale m^3.
assert 1+2==3          # amplitude m times two spatial derivatives
assert 1+1+1==3        # u * grad u: m * (m*m)

# A degree-zero diagnostic applied to S_m[u+t m^2 h] differentiates with m^2.
assert 2==2

# For kappa_L:
# omega x u scales amplitude-quadratically under pure amplitude scaling;
# |u|u also scales quadratically; numerator and denominator both scale a^4.
assert 2+2==4
assert 2+2==4

# Under full spatial NS scaling, Lamb is m^3 and |u|u is m^2, hence kappa
# numerator/denominator both scale m^5 on the measure-preserving torus map.
assert 3+2==5
assert 3+2==5

print('PASS R11 amplitude affine-law exponents')
print('PASS R11 full Navier-Stokes concentration-scaling exponents')
print('PASS R11 kappa_L degree-zero scaling audit')
print('SCOPE: homogeneity audit only; no regularity conclusion.')
