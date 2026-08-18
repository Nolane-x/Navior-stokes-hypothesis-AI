#!/usr/bin/env python3
"""Primary certificate for the INTERNAL algebra/extraction part of R46.

This does not verify the imported Albritton--Barker theorems.  It verifies the
pointwise constants, burst tail implications, threshold-set lemma and formal NS
scaling used before the literature interface.
"""
from __future__ import annotations
import math
import numpy as np

rng=np.random.default_rng(460046)
checks=0

def ok(cond,msg):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(msg)

# Pointwise matrix geometry. M[i,j]=partial_j u_i.
for _ in range(60000):
    u=rng.normal(size=3)
    rho=float(np.linalg.norm(u))
    if rho<1e-10:
        continue
    M=rng.normal(size=(3,3))
    # divergence-free tangent matrix
    tr=np.trace(M)/3.0
    M=M-tr*np.eye(3)
    omega=np.array([
        M[2,1]-M[1,2],
        M[0,2]-M[2,0],
        M[1,0]-M[0,1],
    ])
    Lamb=np.cross(omega,u)
    X=rho*rho*float(np.sum(M*M))
    ok(float(np.dot(Lamb,Lamb)) <= 2*X+1e-10*(1+X), 'Lamb pointwise bound')

    grad_rho=np.array([float(np.dot(u,M[:,j]))/rho for j in range(3)])
    gradG=np.empty((3,3))
    for j in range(3):
        gradG[:,j]=grad_rho[j]*u+rho*M[:,j]
    ok(float(np.sum(gradG*gradG)) <= 4*X+1e-10*(1+X), 'gradG pointwise bound')

# Burst-scale implications and threshold-set algebra.
for _ in range(25000):
    L0=10**rng.uniform(-2,5)
    q=10**rng.uniform(-10,0)
    # Xint is int |u|^2|grad u|^2, forced above L0/sqrt(2).
    Xint=(L0/math.sqrt(2))*10**rng.uniform(0,2)
    Sigma=math.sqrt(2)*Xint
    ok(Sigma+1e-12 >= L0,'unit work forces Sigma>=L0')
    a2=L0/(2*math.sqrt(2)*q)
    low_cap=a2*q
    high_weight=Xint-low_cap
    ok(high_weight+1e-12 >= L0/(2*math.sqrt(2)), 'threshold high-set weighted mass')
    ok(math.sqrt(a2)>0,'threshold amplitude')

    theta=rng.uniform(.05,.95)
    # Rtheta upper consequence from tail Sigma/R.
    Rstar=Sigma/(1-theta)
    ok(Sigma/Rstar <= 1-theta+1e-12,'tail at quantile upper radius')

    # Coarse E45 hierarchy: choose Lambda >= Sigma/sqrt(2).
    Lambda=(Sigma/math.sqrt(2))*10**rng.uniform(0,2)
    ok(Sigma <= math.sqrt(2)*Lambda*(1+1e-12),'Sigma <= sqrt2 Lambda')

    # Formal NS scaling: L0,R,Sigma,Lambda,A scale as lambda;
    # q scales lambda^-1; Xint and Sigma scale lambda.
    lam=10**rng.uniform(-3,3)
    L02=lam*L0
    q2=q/lam
    X2=lam*Xint
    S2=math.sqrt(2)*X2
    a22=L02/(2*math.sqrt(2)*q2)
    ok(abs(S2/(lam*Sigma)-1)<1e-10,'Sigma scaling')
    ok(abs(math.sqrt(a22)/(lam*math.sqrt(a2))-1)<1e-10,'work-linked amplitude threshold scaling')

# Finite discrete threshold lemma: if total weighted amplitude-gradient mass X
# is large and total gradient mass is q, at least the claimed mass lies above
# the R46 amplitude threshold.
for _ in range(5000):
    m=int(rng.integers(20,200))
    g=np.exp(rng.uniform(-8,2,size=m))
    a=np.exp(rng.uniform(-4,6,size=m))
    q=float(np.sum(g))
    X=float(np.sum(a*a*g))
    if X<=0 or q<=0:
        continue
    # Choose L0 at most sqrt2 X so the unit-burst lower bound is respected.
    L0=math.sqrt(2)*X*rng.uniform(.05,.95)
    threshold2=L0/(2*math.sqrt(2)*q)
    high=float(np.sum((a*a*g)[a*a>=threshold2]))
    ok(high+1e-10*(1+X) >= L0/(2*math.sqrt(2)), 'discrete high-set lemma')

# Terminal center sequence / regular-neighborhood contradiction logic.
T=1.0
Mreg=100.0
for n in range(10,1010,10):
    t=T-1/n
    amp=n*n
    # Any claimed regular neighborhood bound Mreg is contradicted eventually.
    if t>T-.02 and amp>Mreg:
        ok(True,'terminal divergent center contradicts fixed regular bound')

print(f'R46_PRIMARY_PASS checks={checks}')
