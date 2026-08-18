#!/usr/bin/env python3
"""Fresh physical/Fourier reconstruction for R45.

Independent from the primary scalar checker.  It constructs smooth nonvanishing
zero-mean divergence-free trigonometric velocity fields on [0,2pi]^3, computes
u, omega, G=|u|u and L=omega x u on a dealiased-enough grid, reconstructs the
Fourier common-work coefficients, and checks the R45 Parseval tail and stress
low-mode envelopes numerically.
"""
from __future__ import annotations
import math
import numpy as np

rng=np.random.default_rng(450045)
V=(2*math.pi)**3
checks=0
max_tail_ratio=0.0
max_stress_ratio=0.0
max_grad_ratio=0.0


def ok(cond,msg):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(msg)


def idx(k,N): return k % N

def set_pair(U,k,a):
    N=U.shape[0]
    kp=tuple(idx(x,N) for x in k)
    km=tuple(idx(-x,N) for x in k)
    U[kp]=a
    U[km]=np.conjugate(a)


def physical(coeff):
    N=coeff.shape[0]
    return np.fft.ifftn(coeff*(N**3),axes=(0,1,2)).real

for world in range(24):
    N=32
    U=np.zeros((N,N,N,3),dtype=np.complex128)
    # Base nonvanishing divergence-free field u=(sin z, cos z, 0).
    set_pair(U,(0,0,1),np.array([-0.5j,0.5,0.0],complex))
    # Small independent divergence-free perturbations.
    candidates=[]
    for i in range(-3,4):
        for j in range(-3,4):
            for k in range(-3,4):
                if (i,j,k)==(0,0,0): continue
                # canonical representative to avoid double insertion
                if (i,j,k) < tuple(-x for x in (i,j,k)): continue
                r=math.sqrt(i*i+j*j+k*k)
                if 1.2 <= r <= 3.5:
                    candidates.append((i,j,k))
    rng.shuffle(candidates)
    for k in candidates[:10]:
        kv=np.array(k,float)
        z=rng.normal(size=3)+1j*rng.normal(size=3)
        z=z-kv*np.dot(kv,z)/np.dot(kv,kv)
        nz=np.linalg.norm(z)
        if nz<1e-12: continue
        z=0.018*z/nz
        set_pair(U,k,z)

    # Wave-number grids.
    freq=np.fft.fftfreq(N)*N
    KX,KY,KZ=np.meshgrid(freq,freq,freq,indexing='ij')
    K=np.stack([KX,KY,KZ],axis=-1)
    kmag=np.linalg.norm(K,axis=-1)

    # Exact spectral vorticity.
    W=1j*np.cross(K,U)
    u=physical(U); omega=physical(W)
    rho=np.linalg.norm(u,axis=-1)
    ok(float(rho.min())>0.55,f'world {world}: base nonvanishing margin lost')
    G=rho[...,None]*u
    Lamb=np.cross(omega,u)
    Ghat=np.fft.fftn(G,axes=(0,1,2))/(N**3)
    Lhat=np.fft.fftn(Lamb,axes=(0,1,2))/(N**3)

    A=float(rho.max())
    E02=V*float(np.sum(np.abs(U)**2))
    Z2=V*float(np.sum(np.abs(W)**2))
    # Physical and Fourier Parseval cross-checks.
    dxV=V/(N**3)
    E02_phys=dxV*float(np.sum(u*u))
    Z2_phys=dxV*float(np.sum(omega*omega))
    ok(abs(E02/E02_phys-1)<2e-12,'energy Parseval')
    ok(abs(Z2/Z2_phys-1)<2e-12,'enstrophy Parseval')

    # Spectral derivative norm of G; field is nonvanishing and smooth.
    gradG2=V*float(np.sum((kmag[...,None]**2)*np.abs(Ghat)**2))
    ratio_grad=math.sqrt(gradG2)/(2*A*math.sqrt(Z2))
    max_grad_ratio=max(max_grad_ratio,ratio_grad)
    ok(ratio_grad < 1.015,f'grad G envelope ratio={ratio_grad}')

    # Build c_k exactly from the Fourier coefficients and Helmholtz reflection.
    c=np.zeros((N,N,N),float)
    stress_ratio=0.0
    for ii in range(N):
        for jj in range(N):
            for kk in range(N):
                r=kmag[ii,jj,kk]
                if r<1e-12: continue
                kv=K[ii,jj,kk]
                g=Ghat[ii,jj,kk]
                qg=kv*(np.dot(kv,g)/(r*r))
                jg=2*qg-g
                val=(V/2.0)*np.real(np.dot(Lhat[ii,jj,kk],np.conjugate(jg)))
                c[ii,jj,kk]=val
                # R45 stress-output envelope |c_k| <= E0^4 |k|/V.
                denom=(E02**2)*r/V
                if denom>0:
                    stress_ratio=max(stress_ratio,abs(val)/denom)
    max_stress_ratio=max(max_stress_ratio,stress_ratio)
    ok(stress_ratio < 1.0015,f'stress envelope ratio={stress_ratio}')

    # Full ell1 high tail check for several cutoffs.
    for R in [0.75,1.25,1.75,2.5,3.5,5.0,7.0,9.0]:
        tail=float(np.sum(np.abs(c[kmag>R+1e-12])))
        rhs=A*A*Z2/R
        ratio=tail/rhs if rhs else 0.0
        max_tail_ratio=max(max_tail_ratio,ratio)
        ok(ratio < 1.0015,f'tail ratio={ratio} R={R} world={world}')

print('R45_FRESH_GRID_PASS',
      f'checks={checks}',
      f'max_tail_ratio={max_tail_ratio:.6g}',
      f'max_stress_ratio={max_stress_ratio:.6g}',
      f'max_grad_ratio={max_grad_ratio:.6g}')
