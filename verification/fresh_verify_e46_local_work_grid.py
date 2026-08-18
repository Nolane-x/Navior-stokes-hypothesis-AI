#!/usr/bin/env python3
"""Fresh physical/Fourier reconstruction for the internal R46 tail bound.

Independent of the primary checker.  Constructs smooth nonvanishing periodic
zero-mean divergence-free fields, computes common-work Fourier coefficients and
checks

  sum_{|k|>R}|c_k| <= sqrt(2)/R * int |u|^2 |grad u|^2.

This is a statewise reconstruction only; it does not verify the external
singularity-to-ancient-solution theorem.
"""
from __future__ import annotations
import math
import numpy as np

rng=np.random.default_rng(460046)
V=(2*math.pi)**3
checks=0
max_tail_ratio=0.0
max_lamb_ratio=0.0
max_gradg_ratio=0.0


def ok(c,msg):
    global checks
    checks+=1
    if not c: raise AssertionError(msg)


def physical(C):
    N=C.shape[0]
    return np.fft.ifftn(C*(N**3),axes=(0,1,2)).real


def put_pair(C,k,a):
    N=C.shape[0]
    p=tuple(int(x)%N for x in k)
    m=tuple(int(-x)%N for x in k)
    C[p]=a
    C[m]=np.conjugate(a)

for world in range(20):
    N=32
    U=np.zeros((N,N,N,3),complex)
    # Smooth nonvanishing Beltrami base.
    put_pair(U,(0,0,1),np.array([-0.5j,0.5,0],complex))
    modes=[]
    for i in range(-3,4):
        for j in range(-3,4):
            for k in range(-3,4):
                if (i,j,k)==(0,0,0): continue
                if (i,j,k)<(-i,-j,-k): continue
                r=math.sqrt(i*i+j*j+k*k)
                if 1.2<=r<=3.5: modes.append((i,j,k))
    rng.shuffle(modes)
    for k in modes[:12]:
        kv=np.asarray(k,float)
        z=rng.normal(size=3)+1j*rng.normal(size=3)
        z=z-kv*np.dot(kv,z)/np.dot(kv,kv)
        nz=np.linalg.norm(z)
        if nz>1e-10: put_pair(U,k,0.02*z/nz)

    freq=np.fft.fftfreq(N)*N
    KX,KY,KZ=np.meshgrid(freq,freq,freq,indexing='ij')
    K=np.stack([KX,KY,KZ],axis=-1)
    kmag=np.linalg.norm(K,axis=-1)
    W=1j*np.cross(K,U)
    u=physical(U); omega=physical(W)
    rho=np.linalg.norm(u,axis=-1)
    ok(float(rho.min())>.45,'nonvanishing margin')
    G=rho[...,None]*u
    Lamb=np.cross(omega,u)
    Gh=np.fft.fftn(G,axes=(0,1,2))/(N**3)
    Lh=np.fft.fftn(Lamb,axes=(0,1,2))/(N**3)

    # Exact spectral gradient of u.
    grad=np.empty((N,N,N,3,3))
    for a in range(3):
        for j in range(3):
            grad[...,a,j]=physical((1j*K[...,j]*U[...,a])[...,None])[...,0]
    grad2=np.sum(grad*grad,axis=(-2,-1))
    dxV=V/(N**3)
    X=dxV*float(np.sum(rho*rho*grad2))

    # Direct pointwise integral ratios supporting the two geometry constants.
    L2=dxV*float(np.sum(Lamb*Lamb))
    max_lamb_ratio=max(max_lamb_ratio,L2/(2*X))
    ok(L2 <= 2*X*(1+2e-10),'integrated Lamb <=2X')

    # Spectral grad G norm (grid reconstruction).
    gradG2=V*float(np.sum((kmag[...,None]**2)*np.abs(Gh)**2))
    max_gradg_ratio=max(max_gradg_ratio,gradG2/(4*X))
    ok(gradG2 <= 4*X*1.02,'gradG <=4X')

    c=np.zeros((N,N,N),float)
    for ix in np.ndindex(N,N,N):
        r=kmag[ix]
        if r<1e-12: continue
        kv=K[ix]
        g=Gh[ix]
        qg=kv*np.dot(kv,g)/(r*r)
        jg=2*qg-g
        c[ix]=(V/2)*np.real(np.dot(Lh[ix],np.conjugate(jg)))

    for R in [.75,1.25,1.75,2.5,3.5,5,7,9]:
        tail=float(np.sum(np.abs(c[kmag>R+1e-12])))
        rhs=math.sqrt(2)*X/R
        ratio=tail/rhs if rhs else 0
        max_tail_ratio=max(max_tail_ratio,ratio)
        ok(ratio<1.002,f'R46 tail ratio {ratio} at R={R}')

print('R46_FRESH_GRID_PASS',
      f'checks={checks}',
      f'max_tail_ratio={max_tail_ratio:.6g}',
      f'max_lamb_ratio={max_lamb_ratio:.6g}',
      f'max_gradG_ratio={max_gradg_ratio:.6g}')
