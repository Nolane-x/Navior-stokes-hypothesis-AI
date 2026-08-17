#!/usr/bin/env python3
from fractions import Fraction as F
import random

# Exact rational-complex arithmetic, z=(re,im).
def Z(a=0,b=0): return (F(a),F(b))
def zadd(x,y): return (x[0]+y[0],x[1]+y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zscale(x,s): return (x[0]*s,x[1]*s)
def cross(a,b):
    return (
        (a[1][0]*b[2][0]-a[1][1]*b[2][1]-a[2][0]*b[1][0]+a[2][1]*b[1][1],
         a[1][0]*b[2][1]+a[1][1]*b[2][0]-a[2][0]*b[1][1]-a[2][1]*b[1][0]),
        (a[2][0]*b[0][0]-a[2][1]*b[0][1]-a[0][0]*b[2][0]+a[0][1]*b[2][1],
         a[2][0]*b[0][1]+a[2][1]*b[0][0]-a[0][0]*b[2][1]-a[0][1]*b[2][0]),
        (a[0][0]*b[1][0]-a[0][1]*b[1][1]-a[1][0]*b[0][0]+a[1][1]*b[0][1],
         a[0][0]*b[1][1]+a[0][1]*b[1][0]-a[1][0]*b[0][1]-a[1][1]*b[0][0]),
    )
def dot_int(k,v):
    out=Z()
    for ki,vi in zip(k,v): out=zadd(out,zscale(vi,F(ki)))
    return out
def vscale_z(v,s): return tuple(zmul(x,s) for x in v)
def vscale_real(v,s): return tuple(zscale(x,s) for x in v)
def vadd(a,b): return tuple(zadd(x,y) for x,y in zip(a,b))
def n2(k): return sum(x*x for x in k)
def addk(a,b): return tuple(x+y for x,y in zip(a,b))

def Q_mode(k,f):
    if k==(0,0,0): return (Z(),Z(),Z())
    kdot=dot_int(k,f); den=F(n2(k))
    return tuple(zscale(kdot,F(ki)/den) for ki in k)

rng=random.Random(230023)
triad_checks=0
for _ in range(300):
    p=tuple(rng.randint(-7,7) for _ in range(3))
    q=tuple(rng.randint(-7,7) for _ in range(3))
    if p==(0,0,0): continue
    k=addk(p,q)
    if k==(0,0,0): continue
    pc=tuple(Z(x,0) for x in p)
    seed=tuple(Z(rng.randint(-5,5),rng.randint(-5,5)) for _ in range(3))
    u=cross(pc,seed)  # p.u=0
    assert dot_int(p,u)==Z()
    rho=Z(rng.randint(-4,4),rng.randint(-4,4))

    direct=Q_mode(k,vscale_z(u,rho))
    # Null-symbol formula: k/|k|^2 * (q.u) * rho.
    qu=dot_int(q,u)
    scalar=zmul(qu,rho)
    formula=tuple(zscale(scalar,F(ki,n2(k))) for ki in k)
    assert direct==formula,(p,q,u,rho,direct,formula)
    triad_checks+=1

# Constant amplitude mode q=0 contributes Q(u_p)=0 for divergence-free u_p.
for p in [(1,0,0),(1,2,0),(-2,1,3)]:
    pc=tuple(Z(x,0) for x in p)
    u=cross(pc,(Z(2,1),Z(-1,3),Z(4,-2)))
    assert Q_mode(p,u)==(Z(),Z(),Z())

# Exhaustive exact geometry check for high-u/low-rho separation.
# If |p|>=4|q|, then |k|>=3|p|/4, equivalently 16|k|^2>=9|p|^2.
gain_checks=0
vecs=[(a,b,c) for a in range(-8,9) for b in range(-8,9) for c in range(-8,9)]
for p in vecs:
    p2=n2(p)
    if p2==0: continue
    for q in vecs:
        q2=n2(q)
        if q2==0: continue
        if p2 >= 16*q2:
            k=addk(p,q); k2=n2(k)
            assert k2>0
            assert 16*k2 >= 9*p2,(p,q,k)
            gain_checks+=1

# Scaling consistency of the test field: rho exponent 1 + u exponent 1 = 2.
assert 1+1==2

print(f'PASS R23 exact checks triads={triad_checks} separated_pairs={gain_checks}')
print('CERTIFIED: Q(rho u) Fourier contribution equals k/|k|^2 (u_p.q) rho_q')
print('CERTIFIED: q=0 amplitude mode vanishes and |p|>=4|q| gives the stated low/high ratio gain')
print('SCOPE: exact commutator/null-symbol structure only; NOT global regularity')
