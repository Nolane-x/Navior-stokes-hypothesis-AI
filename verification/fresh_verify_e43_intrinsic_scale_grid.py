#!/usr/bin/env python3
import numpy as np, math, random

TWOPI=2*math.pi; V=TWOPI**3

def add_mode(u,grad,omega,X,Y,Z,k,a,b,amp,phase):
    k=np.array(k,dtype=float); a=np.array(a,dtype=float); b=np.array(b,dtype=float)
    a=a-k*np.dot(k,a)/np.dot(k,k); b=b-k*np.dot(k,b)/np.dot(k,k)
    th=k[0]*X+k[1]*Y+k[2]*Z+phase
    cs=np.cos(th); sn=np.sin(th)
    for c in range(3): u[...,c]+=amp*(a[c]*cs+b[c]*sn)
    for j in range(3):
      for c in range(3): grad[...,j,c]+=amp*k[j]*(-a[c]*sn+b[c]*cs)
    ka=np.cross(k,a); kb=np.cross(k,b)
    for c in range(3): omega[...,c]+=amp*(-ka[c]*sn+kb[c]*cs)

def world(N,seed):
    rng=random.Random(seed)
    x=np.arange(N)*TWOPI/N
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    u=np.zeros((N,N,N,3)); grad=np.zeros((N,N,N,3,3)); om=np.zeros_like(u)
    add_mode(u,grad,om,X,Y,Z,(0,0,1),(1,0,0),(0,1,0),1.0,0.0)
    modes=[(1,1,0),(1,0,1),(0,1,2),(2,1,1),(1,-2,1)]
    for idx,k in enumerate(modes):
        a=[rng.uniform(-1,1) for _ in range(3)]; b=[rng.uniform(-1,1) for _ in range(3)]
        add_mode(u,grad,om,X,Y,Z,k,a,b,0.035+0.01*idx,rng.uniform(0,TWOPI))
    rho=np.linalg.norm(u,axis=-1)
    assert rho.min()>0.45, rho.min()
    G=rho[...,None]*u
    L=np.cross(om,u)
    gradG=np.zeros_like(grad)
    for j in range(3):
        du=grad[...,j,:]
        dr=np.sum(u*du,axis=-1)/rho
        gradG[...,j,:]=dr[...,None]*u+rho[...,None]*du
    gn=np.sqrt(np.sum(gradG**2,axis=(-2,-1)))
    un=np.linalg.norm(u,axis=-1); dUn=np.sqrt(np.sum(grad**2,axis=(-2,-1)))
    assert np.max(gn-2*un*dUn)<2e-11
    E=math.sqrt(V*np.mean(np.sum(u*u,axis=-1)))
    O=math.sqrt(V*np.mean(np.sum(om*om,axis=-1)))
    DG1=V*np.mean(gn)
    Ghat=np.fft.fftn(G,axes=(0,1,2))/(N**3)
    Lhat=np.fft.fftn(L,axes=(0,1,2))/(N**3)
    freqs=np.fft.fftfreq(N,d=1/N)
    max_g_ratio=0.; max_l_ratio=0.; max_c_ratio=0.; checks=0
    cutoff=N//5
    for i,kx in enumerate(freqs):
      for j,ky in enumerate(freqs):
       for h,kz in enumerate(freqs):
        k=np.array([kx,ky,kz],float); r=float(np.linalg.norm(k))
        if r<0.5 or r>cutoff: continue
        gh=Ghat[i,j,h]; lh=Lhat[i,j,h]
        g_ratio=r*np.linalg.norm(gh)/(DG1/V)
        l_ratio=np.linalg.norm(lh)/(E*O/V)
        assert g_ratio<1.01, (seed,k,g_ratio)
        assert l_ratio<1.00001, (seed,k,l_ratio)
        qhat=k*np.dot(k,gh)/(r*r); jg=2*qhat-gh
        c=0.5*V*float(np.real(np.dot(lh,np.conj(jg))))
        bound=E*E*O*O/(V*r)
        cr=abs(c)/bound if bound else 0
        assert cr<1.02, (seed,k,cr)
        max_g_ratio=max(max_g_ratio,g_ratio); max_l_ratio=max(max_l_ratio,l_ratio); max_c_ratio=max(max_c_ratio,cr)
        checks+=3
    return dict(seed=seed,N=N,minrho=float(rho.min()),g=max_g_ratio,l=max_l_ratio,c=max_c_ratio,checks=checks)

def main():
    total=0
    for N in (28,32):
      for seed in (431,432,433,434):
        r=world(N,seed); total+=r['checks']; print(r)
    print(f'PASS fresh E43 physical-grid coefficient reconstruction checks={total}')
    print('VERDICT: PASS_PARTIALS_ONLY_NOT_COMPACTNESS_NOT_GLOBAL_REGULARITY')
if __name__=='__main__': main()
