#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt
import random

# Exact rational-complex helpers. A complex number is (re, im), each Fraction.
def cadd(a,b): return (a[0]+b[0], a[1]+b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cscale(a,s): return (a[0]*s,a[1]*s)
def cconj(a): return (a[0],-a[1])
def czero(): return (F(0),F(0))
def vadd(a,b): return tuple(cadd(x,y) for x,y in zip(a,b))
def vscale(a,s):
    if isinstance(s, tuple): return tuple(cmul(x,s) for x in a)
    return tuple(cscale(x,s) for x in a)
def vdot_real(a,b):
    out=czero()
    for x,y in zip(a,b): out=cadd(out,cmul(cconj(x),y))
    assert out[1] == 0
    return out[0]
def vdot_k(a,k):
    out=czero()
    for x,ki in zip(a,k): out=cadd(out,cscale(x,F(ki)))
    return out

def qadd(a,b): return tuple(x+y for x,y in zip(a,b))
def qneg(a): return tuple(-x for x in a)
def qnorm2(k): return sum(x*x for x in k)
def qnorm(k):
    n=qnorm2(k); r=isqrt(n); assert r*r==n; return F(r)

def project(q,v):
    if q == (0,0,0): return v
    n=F(qnorm2(q)); qdot=vdot_k(v,q)
    return tuple(cadd(vj,cscale(qdot,-F(qj)/n)) for vj,qj in zip(v,q))

R=lambda x:(F(x),F(0))

# R17: exact centered spectral moment identities.
rng=random.Random(170009)
for _ in range(100):
    radii=[F(rng.randint(1,9)) for _ in range(5)]
    weights=[F(rng.randint(1,9)) for _ in range(5)]
    E=sum(weights)
    M=sum(r*w for r,w in zip(radii,weights))
    Z=sum(r*r*w for r,w in zip(radii,weights))
    Y=sum(r*r*r*w for r,w in zip(radii,weights))
    lam=M/E
    sigma=Z-lam*lam*E
    centered=sum((r-lam)*(r-lam)*(r+lam)*w for r,w in zip(radii,weights))
    assert Y-lam*Z == centered
    assert centered >= lam*sigma
    assert sigma == sum((r-lam)*(r-lam)*w for r,w in zip(radii,weights))

# RD009: exact 3-4-5 triad
# v=(cos 4y, cos 3x,0)+(1/5)(4,-3,0) sin(3x+4y).
k=(3,0,0); l=(0,4,0); q=(3,4,0)
A=(R(0),R(1),R(0))
B=(R(1),R(0),R(0))
C=(R(F(4,5)),R(F(-3,5)),R(0))
uh={}
for kk,V in [(k,A),(l,B)]:
    uh[kk]=vscale(V,F(1,2)); uh[qneg(kk)]=vscale(V,F(1,2))
# sin(q.x)=(e^{iq.x}-e^{-iq.x})/(2i)
uh[q]=vscale(C,(F(0),F(-1,2)))
uh[qneg(q)]=vscale(C,(F(0),F(1,2)))

# Fourier convective coefficient: i sum_{p+r=q} (u_p.r) u_r.
Nh={}
for p,up in uh.items():
    for r,ur in uh.items():
        qq=qadd(p,r)
        upr=vdot_k(up,r)
        coeff=vscale(ur,cmul((F(0),F(1)),upr))
        Nh[qq]=vadd(Nh.get(qq,(czero(),czero(),czero())),coeff)
PN={qq:project(qq,V) for qq,V in Nh.items()}

E=sum(vdot_real(U,U) for U in uh.values())
M=sum(qnorm(kk)*vdot_real(U,U) for kk,U in uh.items())
Z=sum(qnorm(kk)**2*vdot_real(U,U) for kk,U in uh.items())
lam=M/E
sigma=Z-lam*lam*E
Ds2=sum(qnorm(kk)**2*(qnorm(kk)-lam)**2*vdot_real(U,U) for kk,U in uh.items())
prod=F(0); T=F(0)
for kk,U in uh.items():
    V=PN.get(kk,(czero(),czero(),czero()))
    prod += (qnorm(kk)-lam)**2 * vdot_real(U,V)
    T += qnorm(kk) * vdot_real(U,V)

assert E == F(3,2), E
assert M == F(6), M
assert Z == F(25), Z
assert lam == F(4), lam
assert sigma == F(1), sigma
assert Ds2 == F(17), Ds2
assert prod == F(-4,5), prod
assert T == F(1,10), T

print('PASS R17/RD009 exact checks')
print('R17: centered spectral moment identities verified on 100 exact random spectra')
print('RD009: E=3/2 M=6 Z=25 lambda*=4 sigma^2=1 ||Ds||^2=17 production=-4/5')
print("RD009: sigma^2'(0)=(8/5)A^3-34 nu A^2 >0 for A>(85/4)nu")
print('SCOPE: exact structural identities and explicit smooth periodic state; NOT global regularity')
