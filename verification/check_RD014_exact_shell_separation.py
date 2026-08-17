#!/usr/bin/env python3
from fractions import Fraction as F
from collections import defaultdict

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
    return (csub(cmul(a[1],b[2]),cmul(a[2],b[1])),
            csub(cmul(a[2],b[0]),cmul(a[0],b[2])),
            csub(cmul(a[0],b[1]),cmul(a[1],b[0])))
def norm2(v): return sum(z[0]*z[0]+z[1]*z[1] for z in v)
def neg(k): return tuple(-x for x in k)
def divergence(k,u):
    out=C()
    for ki,ui in zip(k,u): out=cadd(out,cscale(ui,F(ki)))
    return out
def omega(k,u):
    kc=tuple(C(x,0) for x in k)
    return vcscale(cross(kc,u),C(0,1))
def projP(k,v):
    if k==(0,0,0): return v
    k2=F(sum(x*x for x in k))
    kv=C()
    for ki,vi in zip(k,v): kv=cadd(kv,cscale(vi,F(ki)))
    return tuple(csub(vi,cscale(kv,F(ki)/k2)) for vi,ki in zip(v,k))

modes=[
 ((1,3,-3),(C(-6,-15),C(9,11),C(7,6))),
 ((1,-2,2),(C(-2,-2),C(1,0),C(2,1))),
 ((1,0,2),(C(-6,-2),C(-9,1),C(3,1))),
]
uh={}
for k,u in modes:
    assert divergence(k,u)==C()
    uh[k]=u
    uh[neg(k)]=tuple(cconj(z) for z in u)
wh={k:omega(k,u) for k,u in uh.items()}
L={}
for p,w in wh.items():
    for r,u in uh.items():
        q=tuple(p[i]+r[i] for i in range(3))
        L[q]=vadd(L.get(q,(C(),C(),C())),cross(w,u))

shells=defaultdict(lambda:[F(0),F(0)])
for q,v in L.items():
    if q==(0,0,0):
        assert norm2(v)==0
        continue
    pv=projP(q,v); qv=vsub(v,pv)
    s=sum(x*x for x in q)
    shells[s][0]+=norm2(pv)
    shells[s][1]+=norm2(qv)

expected={
 4:(F(7392),F(8992)),
 6:(F(260000,3),F(27460,3)),
 14:(F(12894680,7),F(184904,7)),
 20:(F(0),F(145440)),
 24:(F(35840,3),F(71968,3)),
 34:(F(1813224),F(8584)),
 36:(F(0),F(2880)),
 50:(F(18600),F(745300)),
 76:(F(0),F(9883800)),
}
assert {k:tuple(v) for k,v in shells.items()}==expected
Ep=sum(v[0] for v in shells.values())
Eq=sum(v[1] for v in shells.values())
overlap=sum(min(v[0],v[1]) for v in shells.values())
assert Ep==F(79378456,21)
assert Eq==F(227945624,21)
assert Ep/(Ep+Eq)==F(9922307,38415510)
assert overlap/min(Ep,Eq)==F(430977,19844614)
assert overlap/min(Ep,Eq)<F(11,500)
assert F(1,4)<Ep/(Ep+Eq)<F(27,100)
print('PASS RD014 exact global-balance/shell-separation counterexample')
print('P fraction =',float(Ep/(Ep+Eq)))
print('shell overlap / minority =',float(overlap/min(Ep,Eq)))
