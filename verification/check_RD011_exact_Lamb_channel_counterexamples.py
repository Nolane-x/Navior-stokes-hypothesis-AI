#!/usr/bin/env python3
from fractions import Fraction as F

# Exact rational-complex arithmetic, z=(re,im).
def C(re=0,im=0): return (F(re),F(im))
def cadd(a,b): return (a[0]+b[0],a[1]+b[1])
def csub(a,b): return (a[0]-b[0],a[1]-b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cscale(a,s): return (a[0]*s,a[1]*s)
def cconj(a): return (a[0],-a[1])
def vadd(a,b): return tuple(cadd(x,y) for x,y in zip(a,b))
def vsub(a,b): return tuple(csub(x,y) for x,y in zip(a,b))
def vcscale(a,s): return tuple(cmul(x,s) for x in a)
def cross(a,b):
    return (
        csub(cmul(a[1],b[2]),cmul(a[2],b[1])),
        csub(cmul(a[2],b[0]),cmul(a[0],b[2])),
        csub(cmul(a[0],b[1]),cmul(a[1],b[0])),
    )
def norm2(v): return sum(z[0]*z[0]+z[1]*z[1] for z in v)
def neg(k): return tuple(-x for x in k)
def projP(k,v):
    if k==(0,0,0): return v
    k2=F(sum(x*x for x in k))
    kv=C()
    for ki,vi in zip(k,v): kv=cadd(kv,cscale(vi,F(ki)))
    return tuple(csub(vi,cscale(kv,F(ki)/k2)) for vi,ki in zip(v,k))
def omega(k,u):
    kc=tuple(C(x,0) for x in k)
    return vcscale(cross(kc,u),C(0,1))
def divergence(k,u):
    out=C()
    for ki,ui in zip(k,u): out=cadd(out,cscale(ui,F(ki)))
    return out

def analyze(modes):
    uh={}
    for k,u in modes:
        assert divergence(k,u)==C(), (k,u,divergence(k,u))
        uh[k]=u
        uh[neg(k)]=tuple(cconj(z) for z in u)
    wh={k:omega(k,u) for k,u in uh.items()}
    L={}
    for p,w in wh.items():
        for r,u in uh.items():
            q=tuple(p[i]+r[i] for i in range(3))
            L[q]=vadd(L.get(q,(C(),C(),C())),cross(w,u))
    Ep=Eq=F(0)
    for q,v in L.items():
        if q==(0,0,0):
            # Periodicity/incompressibility makes this zero for these fields.
            assert norm2(v)==0
            continue
        pv=projP(q,v); qv=vsub(v,pv)
        Ep += norm2(pv); Eq += norm2(qv)
    return Ep,Eq,Ep/(Ep+Eq)

sol_heavy=[
 ((1,1,0),(C(F(3,2),1),C(F(-3,2),-1),C(2,-2))),
 ((1,-1,1),(C(F(-5,3),2),C(F(-7,3),-1),C(F(-2,3),-3))),
 ((0,1,0),(C(1,-3),C(0,0),C(-2,-3))),
]
grad_heavy=[
 ((1,1,0),(C(F(5,2),1),C(F(-5,2),-1),C(1,-1))),
 ((0,0,1),(C(0,3),C(0,-3),C(0,0))),
 ((1,1,-1),(C(1,3),C(1,-3),C(2,0))),
]

Ep,Eq,r=analyze(sol_heavy)
assert Ep==F(63275,27), Ep
assert Eq==F(50770,27), Eq
assert r==F(12655,22809), r
assert r>F(1,2)

Ep2,Eq2,r2=analyze(grad_heavy)
assert Ep2==F(4328,9), Ep2
assert Eq2==F(125641,9), Eq2
assert r2==F(4328,129969), r2
assert r2<F(1,2)

print('PASS RD011 exact Lamb-channel counterexamples')
print('solenoidal-heavier: P=',Ep,'Q=',Eq,'P/L=',r,float(r))
print('gradient-heavier:   P=',Ep2,'Q=',Eq2,'P/L=',r2,float(r2))
print('FALSIFIED: universal coefficient-one statewise dominance in either direction')
print('SCOPE: exact smooth finite-Fourier states; NOT a blow-up construction')
