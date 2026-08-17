#!/usr/bin/env python3
"""Stdlib-only verification for R15 and R16.

Checks the canonical frequency minimizer, spectral-variance identity,
monochromatic helicity/spin relation, and the critical scaling bookkeeping of
R16. It does not prove finiteness of the critical actions or global regularity.
"""
import math
import random
from fractions import Fraction

rng=random.Random(1516)

# R15: test the convex quadratic minimizer on random positive spectral atoms.
for _ in range(5000):
    n=rng.randint(2,20)
    freqs=[10**rng.uniform(-1,2) for _ in range(n)]
    weights=[10**rng.uniform(-2,1) for _ in range(n)]
    E=sum(weights)
    mean=sum(f*w for f,w in zip(freqs,weights))/E
    second=sum(f*f*w for f,w in zip(freqs,weights))
    variance=second-mean*mean*E
    assert variance >= -1e-10*(1+second)

    def q(lam):
        return sum((f-lam)**2*w for f,w in zip(freqs,weights))

    # Convex minimum at the weighted mean.
    eps=max(1e-7,1e-5*mean)
    qm=q(mean)
    assert q(mean-eps) >= qm-1e-10*(1+qm)
    assert q(mean+eps) >= qm-1e-10*(1+qm)

# Monochromatic shell spin/helicity identity.
for _ in range(5000):
    Ep=10**rng.uniform(-3,3)
    Em=10**rng.uniform(-3,3)
    E=Ep+Em
    h=(Ep-Em)/E
    m=2*math.sqrt(Ep*Em)/E
    assert abs(m*m + h*h - 1.0) < 2e-12

# R16 algebra: |a+b|^2 <= 2|a|^2+2|b|^2 in R^3.
for _ in range(10000):
    a=[rng.gauss(0,1) for _ in range(3)]
    b=[rng.gauss(0,1) for _ in range(3)]
    lhs=sum((x+y)**2 for x,y in zip(a,b))
    rhs=2*sum(x*x for x in a)+2*sum(y*y for y in b)
    assert lhs <= rhs + 1e-12*(1+rhs)

# R16 critical scaling exponents.
# spin: U -1, lambda_*^2 +2, cross-L2^2 +1, dt -2.
assert Fraction(-1)+Fraction(2)+Fraction(1)+Fraction(-2)==0
# bandwidth: U -1, ||r*x u||_2^2 +3, dt -2.
assert Fraction(-1)+Fraction(3)+Fraction(-2)==0

print('PASS R15 canonical weighted frequency minimizer')
print('PASS R15 spectral variance and shell helicity/spin identity')
print('PASS R16 two-mechanism norm split')
print('PASS R16 critical action scaling')
print('SCOPE: structural algebra only; action finiteness and global regularity remain OPEN.')
