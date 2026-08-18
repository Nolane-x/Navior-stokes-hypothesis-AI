#!/usr/bin/env python3
import numpy as np, math, random

TWOPI=2*math.pi; V=TWOPI**3

def add(u,grad,X,Y,Z,k,a,b,amp,phase):
    k=np.array(k,float); a=np.array(a,float); b=np.array(b,float)
    a-=k*np.dot(k,a)/np.dot(k,k); b-=k*np.dot(k,b)/np.dot(k,k)
    th=k[0]*X+k[1]*Y+k[2]*Z+phase
    c=np.cos(th); s=np.sin(th)
    u += amp*(c[...,None]*a+s[...,None]*b)
    for j in range(3): grad[...,j,:] += amp*k[j]*(-s[...,None]*a+c[...,None]*b)

def one(N,seed):
    rng=random.Random(seed); x=np.arange(N)*TWOPI/N
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    u=np.zeros((N,N,N,3)); grad=np.zeros((N,N,N,3,3))
    modes=[(1,0,0),(0,1,1),(1,-1,2),(2,1,0),(2,-1,1),(1,2,-1)]
    for j,k in enumerate(modes):
        a=[rng.uniform(-1,1) for _ in range(3)]
        b=[rng.uniform(-1,1) for _ in range(3)]
        add(u,grad,X,Y,Z,k,a,b,0.2+0.03*j,rng.uniform(0,TWOPI))
    rho=np.linalg.norm(u,axis=-1)
    A=float(rho.max())
    g2=np.sum(grad*grad,axis=(-2,-1))
    dots=np.sum(u[...,None,:]*grad,axis=-1)
    second=np.zeros_like(rho)
    mask=rho>1e-12
    second[mask]=np.sum(dots[mask]**2,axis=-1)/rho[mask]
    d3dens=rho*g2+second
    assert np.max(d3dens-2*A*g2) < 1e-9
    Y=V*np.mean(rho**3)
    E2=V*np.mean(rho**2)
    assert Y <= A*E2*(1+2e-13)
    curl=np.empty_like(u)
    curl[...,0]=grad[...,1,2]-grad[...,2,1]
    curl[...,1]=grad[...,2,0]-grad[...,0,2]
    curl[...,2]=grad[...,0,1]-grad[...,1,0]
    grad2=V*np.mean(g2); om2=V*np.mean(np.sum(curl*curl,axis=-1))
    assert abs(grad2-om2) < 2e-10*max(1,grad2)
    D3=V*np.mean(d3dens)
    assert D3 <= 2*A*om2*(1+2e-12)

def main():
    checks=0
    for N in (18,22,26):
        for seed in range(441,451):
            one(N,seed); checks+=4
    print(f'PASS fresh E44 amplitude/D3 physical-grid checks={checks}')
    print('VERDICT: PASS_PARTIALS_ONLY_CENTER_SELECTION_NOT_SPATIAL_COMPACTNESS')

if __name__=='__main__': main()
