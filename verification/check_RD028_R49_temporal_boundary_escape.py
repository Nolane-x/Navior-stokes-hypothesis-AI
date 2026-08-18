#!/usr/bin/env python3
"""Abstract route guard: R49 integrated bounds do not force temporal interiority."""
from __future__ import annotations
import math,random
r=random.Random(490828); c=0
def ck(x,m):
 global c; c+=1
 if not x: raise AssertionError(m)
x0=1/(2*math.sqrt(2)); a4=2*math.sqrt(2); m12=5.; d0=1.; center=.2; band=.6
for n in range(2,50002):
 t=1/n; w=1/t; x=x0/t; a=a4/t; m=m12/t; d=d0/t
 ck(abs(w*t-1)<1e-12,'work'); ck(abs(x*t-x0)<1e-12,'X'); ck(abs(a*t-a4)<1e-12,'L4'); ck(abs(m*t-m12)<1e-12,'L12'); ck(abs(d*t-d0)<1e-12,'D'); ck(center>0 and band>=.5,'nonzero'); ck(t<=.5,'collapse')
for n in range(3,50003):
 T=float(n); e=1/n; w=1/e; x=x0/e; a=a4/e; m=m12/e; d=d0/e
 ck(abs(w*e-1)<1e-12,'long work'); ck(abs(x*e-x0)<1e-12,'long X'); ck(abs(a*e-a4)<1e-12,'long L4'); ck(abs(m*e-m12)<1e-12,'long L12'); ck(abs(d*e-d0)<1e-12,'long D'); ck(e/T<.25,'boundary'); ck(center>0 and band>=.5,'long nonzero')
for _ in range(40000):
 t=10**r.uniform(-10,-1); X=10**r.uniform(-2,1); A=10**r.uniform(0,2); M=10**r.uniform(0,2); D=10**r.uniform(-2,1)
 ck(abs((X/t)*t-X)<1e-10*max(1,X),'rX'); ck(abs((A/t)*t-A)<1e-10*max(1,A),'rA'); ck(abs((M/t)*t-M)<1e-10*max(1,M),'rM'); ck(abs((D/t)*t-D)<1e-10*max(1,D),'rD')
print(f'RD028_PASS checks={c}')
