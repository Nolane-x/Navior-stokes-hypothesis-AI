#!/usr/bin/env python3
from __future__ import annotations
import math, random
r=random.Random(490049); n=0; s2=math.sqrt(2)
def ck(x,m):
 global n; n+=1
 if not x: raise AssertionError(m)
for _ in range(60000):
 nu=10**r.uniform(-2,2); Ds=28/(3*nu); D=Ds*r.uniform(1e-5,1); X=10**r.uniform(-5,8)
 S=s2*X; K=2*S; L=S*r.uniform(1e-6,1); e=r.uniform(0,.5); B=X/D
 ck(abs(K-2*s2*X)<=1e-12*max(1,K),'K'); ck(L<=K/2+1e-12,'L')
 ck(abs(S/K-.5)<1e-14,'tail'); ck(abs(X/K-1/(2*s2))<1e-14,'X/K')
 ck(abs(B/K-1/(2*s2*D))<1e-12*max(1,B/K),'B/K')
 ck(B/K>=3*nu/(56*s2)-1e-12,'B lower'); ck(B/(2*K)>=3*nu/(112*s2)-1e-12,'center')
 ck((X/2)/K>=1/(4*s2)-1e-14,'H mass')
 m=1-e; A4n=K*(2*m*m/X); ck(A4n>=4*s2*m*m-1e-12,'L4 exact'); ck(A4n>=s2-1e-12,'L4 uniform')
 E=10**r.uniform(-2,3); V=10**r.uniform(-1,2); dt=10**r.uniform(-12,-1)
 mean=E**4*dt/(K*V**(5/3)); ck(mean>=0 and math.isfinite(mean),'mean')
for _ in range(100000):
 neg=10**r.uniform(-8,3); pos=1+neg; ta=r.uniform(0,.5); tp=r.uniform(0,ta); band=pos-tp
 ck(pos>=1,'P'); ck(tp<=.5+1e-15,'tail P'); ck(band>=.5-1e-12,'band')
for _ in range(30000):
 z=r.randint(4,80); d=[10**r.uniform(-8,5) for i in range(z)]; a=[10**r.uniform(-8,8) for i in range(z)]; f=[r.random() for i in range(z)]
 x=[a[i]*d[i]*f[i] for i in range(z)]; D=sum(d); X=sum(x)
 if X<=0: continue
 B=X/D; H=sum(xi for xi,ai in zip(x,a) if ai>=B/2); ck(H>=X/2-1e-10*max(1,X),'half')
for _ in range(50000):
 C6=10**r.uniform(-1,2); C0=10**r.uniform(-1,2); E=10**r.uniform(-2,3); V=10**r.uniform(-1,2); X=10**r.uniform(-3,8); K=2*s2*X; dt=10**r.uniform(-12,-2)
 g=4*X/K; mean=E**4*dt/(K*V**(5/3)); M=C6*g+C0*mean
 ck(abs(g-s2)<1e-13,'grad'); ck(M<=C6*s2+C0*mean+1e-12,'L4L12'); ck(mean>=0 and math.isfinite(M),'finite')
for _ in range(50000):
 R=10**r.uniform(-8,-.1); M=10**r.uniform(-3,3); C=10**r.uniform(-1,1); q=C*M**.75*R**.75; h=C*M**.75*(R/2)**.75
 ck(h<q,'local'); ck(abs(h/q-2**(-.75))<1e-12,'3/4')
for _ in range(40000):
 l=10**r.uniform(-5,5); X=10**r.uniform(-4,6); K=2*s2*X; A=10**r.uniform(-5,7)
 ck(abs((l*X)/(l*K)-X/K)<1e-12,'scale X'); ck(abs((l*A)/(l*K)-A/K)<1e-12*max(1,A/K),'scale L4')
print(f'R49_PRIMARY_PASS checks={n}')
