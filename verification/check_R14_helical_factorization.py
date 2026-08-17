#!/usr/bin/env python3
"""Stdlib-only algebra stress check for R14.

The helical projector identities curl u_+=D u_+, curl u_-=-D u_- are standard
Fourier definitions. This checker validates the load-bearing pointwise
reference-frequency Lamb factorization and its triangle/Hölder-style algebra.
It does not prove global regularity.
"""
import math
import random

rng=random.Random(1414)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(sum(x*x for x in a))

for _ in range(10000):
    up=tuple(rng.gauss(0,1) for _ in range(3))
    um=tuple(rng.gauss(0,1) for _ in range(3))
    Dup=tuple(rng.gauss(0,1) for _ in range(3))
    Dum=tuple(rng.gauss(0,1) for _ in range(3))
    lam=10**rng.uniform(-2,2)

    u=add(up,um)
    omega=sub(Dup,Dum)
    r=sub(sub(Dup,scale(lam,up)),sub(Dum,scale(lam,um)))

    lhs=cross(omega,u)
    rhs=add(scale(2*lam,cross(up,um)),cross(r,u))
    err=norm(sub(lhs,rhs))
    assert err < 2e-11*(1+norm(lhs)+norm(rhs))

    # Pointwise triangle version behind the norm inequalities.
    assert norm(lhs) <= 2*lam*norm(up)*norm(um)+norm(r)*norm(u)+2e-11*(1+norm(lhs))

# Beltrami endpoint: one spin sector and exact D=lambda.
for _ in range(1000):
    up=tuple(rng.gauss(0,1) for _ in range(3))
    lam=10**rng.uniform(-2,2)
    um=(0.0,0.0,0.0)
    Dup=scale(lam,up); Dum=(0.0,0.0,0.0)
    u=up; omega=Dup
    assert norm(cross(omega,u)) < 1e-12*(1+norm(u)**2)

print('PASS R14 exact helical conflict + bandwidth factorization stress')
print('PASS R14 pointwise norm bound')
print('PASS R14 single-spin monochromatic Beltrami endpoint')
print('SCOPE: structural algebra only; ultraviolet tail summability remains OPEN.')
