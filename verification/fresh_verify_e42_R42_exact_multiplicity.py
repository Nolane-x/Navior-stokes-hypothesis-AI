#!/usr/bin/env python3
"""Fresh exact-rational verifier for R42 spectral multiplicity explosion."""
from fractions import Fraction as F
import random

rng=random.Random(94242)
checks=0

# Exact atom-count lower bound: if 0<=a_i<=beta and sum over selected atoms >=theta,
# then count*beta>=theta.
for _ in range(50000):
    den=rng.randint(2,10000)
    beta=F(1,den)
    theta=F(rng.randint(1,9),10)
    m=(theta.numerator*beta.denominator + theta.denominator*beta.numerator-1)//(theta.denominator*beta.numerator)
    # m is ceil(theta/beta)
    assert F(m)*beta>=theta
    if m>0:
        assert F(m-1)*beta<theta
    checks+=2

# Severe cancellation: positive and negative clouds can be arbitrarily large,
# but a theta-sized positive portion still needs at least theta/beta atoms.
for _ in range(5000):
    beta=F(1,rng.randint(20,500))
    theta=F(1,2)
    extra=rng.randint(0,100)
    npos=(F(1)+F(extra))*beta.denominator  # enough beta-atoms for huge positive mass
    # We need not build the cloud explicitly; exact positive-atom cap is beta.
    need=(theta.numerator*beta.denominator + theta.denominator*beta.numerator-1)//(theta.denominator*beta.numerator)
    assert F(need)*beta>=theta
    assert need>=1
    checks+=2

# Good-burst substitution: beta <= 4 C sqrt(ell q)/N, hence m_theta >= theta N/(4 C sqrt(ell q)).
for n in range(1,2000):
    N=F(n*n+7)
    ell=F(1,(n+1)**2)
    q=F(1,(n+1)**4)
    # Use an exact rational surrogate r with r^2=ell*q: here sqrt is exact.
    root=F(1,(n+1)**3)
    assert root*root==ell*q
    C=F(5,2); theta=F(1,2)
    beta=4*C*root/N
    lower=theta/beta
    formula=theta*N/(4*C*root)
    assert lower==formula
    if n>1:
        N0=F((n-1)*(n-1)+7); root0=F(1,n**3)
        prev=theta*N0/(4*C*root0)
        assert lower>prev
    checks+=3

print(f"PASS fresh E42/R42 exact multiplicity checks={checks}")
print("VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY")
