#!/usr/bin/env python3
from __future__ import annotations
import math,random,numpy as np
r=random.Random(490149); n=0; me=ml=mg=mw=0.0
def ck(x,m):
 global n; n+=1
 if not x: raise AssertionError(m)
def perp(k,z):
 k=np.array(k,float); z=np.array(z,float); z-=k*np.dot(z,k)/np.dot(k,k); q=np.linalg.norm(z)
 if q<1e-10: z=np.cross(k,[1.,0.,0.] if abs(k[0])<.9*np.linalg.norm(k) else [0.,1.,0.]); q=np.linalg.norm(z)
 return z/q
N=18; xs=np.linspace(0,2*np.pi,N,endpoint=False); Xg,Yg,Zg=np.meshgrid(xs,xs,xs,indexing='ij')
f=(np.fft.fftfreq(N)*N).astype(int); KX,KY,KZ=np.meshgrid(f,f,f,indexing='ij'); KV=np.stack([KX,KY,KZ],-1).astype(float); K2=np.sum(KV*KV,-1); mask=K2>0
for w in range(64):
 u=np.zeros((3,N,N,N)); g=np.zeros((3,3,N,N,N)); used=set()
 for _ in range(r.randint(3,8)):
  while True:
   k=tuple(r.randint(-4,4) for j in range(3))
   if k!=(0,0,0) and k not in used and tuple(-x for x in k) not in used: used.add(k); break
  kv=np.array(k,float); a=perp(kv,[r.uniform(-1,1) for j in range(3)])*r.uniform(.1,1.2); b=perp(kv,[r.uniform(-1,1) for j in range(3)])*r.uniform(.1,1.2)
  ph=kv[0]*Xg+kv[1]*Yg+kv[2]*Zg+r.uniform(-math.pi,math.pi); c=np.cos(ph); s=np.sin(ph)
  for i in range(3):
   u[i]+=a[i]*c+b[i]*s
   for j in range(3): g[i,j]+=kv[j]*(-a[i]*s+b[i]*c)
 ck(np.max(np.abs(sum(g[i,i] for i in range(3))))<2e-12,'div')
 rho=np.sqrt(np.sum(u*u,0)); gn=np.sum(g*g,axis=(0,1)); X=float(np.mean(rho*rho*gn)); ck(X>1e-12,'X')
 om=np.empty_like(u); om[0]=g[2,1]-g[1,2]; om[1]=g[0,2]-g[2,0]; om[2]=g[1,0]-g[0,1]
 L=np.moveaxis(np.cross(np.moveaxis(om,0,-1),np.moveaxis(u,0,-1)),-1,0); L2=float(np.mean(np.sum(L*L,0))); z=L2/(2*X); ml=max(ml,z); ck(z<=1+2e-12,'L')
 gr=np.zeros((3,N,N,N))
 for j in range(3): gr[j]=2*sum(u[i]*g[i,j] for i in range(3))
 z=float(np.mean(np.sum(gr*gr,0)))/(4*X); mg=max(mg,z); ck(z<=1+2e-12,'gr')
 G=rho[None]*u
 def Q(F):
  H=np.stack([np.fft.fftn(F[i]) for i in range(3)],-1); d=np.sum(KV*H,-1); Qh=np.zeros_like(H); Qh[mask]=KV[mask]*(d[mask]/K2[mask])[...,None]
  return np.stack([np.fft.ifftn(Qh[...,i]).real for i in range(3)])
 ql,qg=Q(L),Q(G); pl,pg=L-ql,G-qg; inn=lambda A,B:float(np.mean(np.sum(A*B,0))); wq=inn(ql,qg); wp=-inn(pl,pg); wj=.5*inn(L,qg-pg); sc=max(1,abs(wq),abs(wp),abs(wj)); z=max(abs(wq-wp),abs(wq-wj))/sc; me=max(me,z); ck(z<3e-11,'PQ')
 u4=math.sqrt(float(np.mean(rho**4))); rhs=math.sqrt(X)*u4/math.sqrt(2); z=abs(wq)/max(rhs,1e-30); mw=max(mw,z); ck(z<=1+2e-11,'work')
 lam=10**r.uniform(-3,3); ck(abs((lam*X)/(lam*2*math.sqrt(2)*X)-1/(2*math.sqrt(2)))<1e-13,'scale')
print(f'R49_FRESH_PHYSICAL_PASS checks={n} max_channel_err={me:.3e} max_lamb_ratio={ml:.12f} max_grad_rho2_ratio={mg:.12f} max_work_ratio={mw:.12f}')
