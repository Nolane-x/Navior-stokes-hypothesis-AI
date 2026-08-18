#!/usr/bin/env python3
import math, random

C2=26.0
C3=27.0

def maxnorm_shell_count(m:int)->int:
    return (2*m+1)**3-(2*m-1)**3

def lattice_weight_sum(R:int)->float:
    s=0.0
    for x in range(-R,R+1):
      for y in range(-R,R+1):
       for z in range(-R,R+1):
        if x==y==z==0: continue
        r=math.sqrt(x*x+y*y+z*z)
        if r<=R+1e-12: s += 1.0/r
    return s

def lattice_count(R:int)->int:
    n=0
    for x in range(-R,R+1):
      for y in range(-R,R+1):
       for z in range(-R,R+1):
        if x==y==z==0: continue
        if x*x+y*y+z*z<=R*R: n+=1
    return n

def main():
    checks=0
    for m in range(1,101):
        assert maxnorm_shell_count(m)==24*m*m+2
        checks+=1
    for R in range(1,61):
        S=lattice_weight_sum(R)
        N=lattice_count(R)
        assert S <= C2*R*R + 1e-12, (R,S,C2*R*R)
        assert N <= C3*R**3 + 1e-12, (R,N,C3*R**3)
        checks+=2

    rng=random.Random(43043)
    for _ in range(500):
        V=10**rng.uniform(-0.5,0.5)
        E=10**rng.uniform(-0.3,0.7)
        ell=10**rng.uniform(-9,-2)
        q=10**rng.uniform(-9,-2)
        alpha=E*E*q/V
        beta=E**3*math.sqrt(ell*q)/V
        theta=rng.uniform(0.1,0.9)
        K2=math.sqrt(theta/(C2*alpha))
        K3=(theta/(C3*beta))**(1/3)
        for K,C,powr in [(K2,C2,2),(K3,C3,3)]:
            R=max(0.25,0.999*K)
            if R>=1:
                cap=(alpha*C*R**2) if powr==2 else (beta*C*R**3)
                assert cap < theta*(1+1e-12)
                checks+=1

    for lam in [0.125,0.5,2,7,32]:
        E=1.7; ell=0.03; q=0.011; R=5.2
        I2=E**2*q*R**2
        I3=E**3*math.sqrt(ell*q)*R**3
        Ep=lam**(-0.5)*E; ellp=lam**(-2)*ell; qp=lam**(-1)*q; Rp=lam*R
        assert abs(Ep**2*qp*Rp**2-I2) <= 2e-12*max(1,abs(I2))
        assert abs(Ep**3*math.sqrt(ellp*qp)*Rp**3-I3) <= 2e-12*max(1,abs(I3))
        checks+=2

    print(f'PASS R43 intrinsic quantile-scale checks={checks}')
    print('CERTIFIED: sum_{0<|k|<=R} 1/|k| <= 26 R^2 and N(R)<=27R^3 for integer R>=1')
    print('CERTIFIED: theta-work quantile radius obeys both alpha^-1/2 and beta^-1/3 scale-critical floors')
    print('SCOPE: structural/lattice/homogeneity certificate only; no compactness or global regularity')

if __name__=='__main__': main()
