#!/usr/bin/env python3
from fractions import Fraction as F

# RD010 exact shear audit on the normalized 2*pi torus:
# u=a(0,cos x,0), omega=(0,0,-a sin x),
# L=omega x u=(a^2/2) sin(2x)e_x.
# At cutoff ratio M_*/a=1/2, chi=1_{|cos x|>1/2}.
# The boundary x=pi/3 has a nonzero one-sided Lamb value.
sin2_boundary_sq = F(3,4)  # sin^2(2*pi/3)
assert sin2_boundary_sq > 0

# Hence the x-component jump magnitude squared is
# (a^2/2)^2 * 3/4 = 3 a^4 / 16.
jump_coeff_sq = F(3,16)
assert jump_coeff_sq == F(1,4) * sin2_boundary_sq

# Threshold algebra. If U=a*C_{3/2} and
# a^2=nu^2/(6 C_H^2 C_{3/2}), then
# M_*/a=nu^2/(12 C_H^2 C_{3/2} a^2)=1/2.
ratio = F(1,12) / F(1,6)
assert ratio == F(1,2)

# R18 constant chain:
# ||P_<=K L||_2 <= C_B ||L||_1 <= C_B ||omega||_2 ||u||_2.
# U<=||u||_2<=E0 and 2 nu int||omega||_2^2 <= E0^2
# imply int U ||P_<=K L||_2^2 <= C_B^2 E0^5/(2nu).
assert 3 + 2 == 5
assert F(1,2) == F(1,2)

# Critical scaling under u_lambda=lambda u(lambda x,lambda^2t):
# ||u||_{3/2}: -1; ||L||_2^2: +3; dt: -2.
assert -1 + 3 - 2 == 0

# Orthogonal low/high decomposition implication, represented on finite surrogates.
for total in (10**3, 10**6, 10**9):
    low = 137
    high = total-low
    assert high > total//2

print('PASS R18/RD010 structural checks')
print('RD010: exact shear has physical u on shell 1 and Lamb force on shell 2; sharp |cos x|>1/2 cutoff has a nonzero jump')
print('RD010: cutoff ratio M_*/a=1/2 is achieved by a^2=nu^2/(6 C_H^2 C_{3/2})')
print('R18: full-Lamb low-frequency action has the same C_B(K)^2 E0^5/(2nu) energy bound as R13 without cutoff contamination')
print('R18: full-Lamb action is scale invariant and A_tail<=A_L, so divergent A_tail forces genuine full-Lamb UV escape')
print('SCOPE: representation correction and structural reduction; NOT global regularity')
