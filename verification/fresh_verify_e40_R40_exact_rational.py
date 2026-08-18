#!/usr/bin/env python3
"""Exact-rational independent verifier for the R39/R40 projection algebra.

Uses fractions.Fraction only.  It verifies complementary Helmholtz projections,
modewise pairing decomposition, and exact Cauchy bounds for rational test data.
It does not verify the continuum Navier-Stokes theorem.
"""
from fractions import Fraction as F
import random

rng=random.Random(404040)
checks=0

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def norm2(a): return dot(a,a)

def Q(k,v):
    kk=dot(k,k)
    return mul(dot(k,v)/kk,k)

def P(k,v): return sub(v,Q(k,v))

def randvec():
    return tuple(F(rng.randint(-9,9),rng.randint(1,9)) for _ in range(3))

for _ in range(20000):
    while True:
        k=tuple(F(rng.randint(-8,8)) for _ in range(3))
        if norm2(k)!=0: break
    L=randvec(); G=randvec()
    qL=Q(k,L); pL=P(k,L); qG=Q(k,G); pG=P(k,G)
    # exact complementary splitting and orthogonality
    assert add(qL,pL)==L
    assert add(qG,pG)==G
    assert dot(qL,pL)==0
    assert dot(qG,pG)==0
    # exact pairing decomposition underlying R39
    assert dot(qL,qG)+dot(pL,pG)==dot(L,G)
    # exact squared Cauchy bounds underlying R40
    assert dot(qL,qG)**2 <= norm2(L)*norm2(G)
    assert dot(pL,pG)**2 <= norm2(L)*norm2(G)
    # projection contractions
    assert norm2(qL)<=norm2(L) and norm2(pL)<=norm2(L)
    assert norm2(qG)<=norm2(G) and norm2(pG)<=norm2(G)
    checks+=11

# Exact finite-catalog envelope arithmetic: if |w_g,k|,|w_s,k| <= B*omega_j,
# the sum over m modes and n time cells is <=2mB sum omega_j dt.
for _ in range(3000):
    m=rng.randint(1,80); nt=rng.randint(1,30)
    B=F(rng.randint(1,20),rng.randint(1,10)); dt=F(1,rng.randint(10,1000))
    om=[F(rng.randint(0,30),rng.randint(1,10)) for _ in range(nt)]
    total=F(0)
    for w in om:
        for _k in range(m):
            rg=F(rng.randint(0,100),100); rs=F(rng.randint(0,100),100)
            total += B*w*(rg+rs)*dt
    envelope=2*m*B*sum(om,F(0))*dt
    assert total<=envelope
    checks+=1

print(f"PASS fresh exact-rational R39/R40 checks={checks}")
print("VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY")
