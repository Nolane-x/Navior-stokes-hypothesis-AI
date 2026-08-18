#!/usr/bin/env python3
import random


def lower_bound(N,eta,zeta,E,nu,q):
    return 3.0*(N-0.5*eta-zeta)/(E*E+6.0*nu*q)


def main():
    rng=random.Random(44044)
    checks=0
    for _ in range(5000):
        N=rng.randint(3,100000)
        eta=rng.random()*0.2
        zeta=rng.random()*0.1
        E=10**rng.uniform(-1,1)
        nu=10**rng.uniform(-3,0.5)
        q=10**rng.uniform(-12,1)
        eps=0.5*eta+zeta
        W=N-eps+rng.random()*2.0
        Amin=3*W/(E*E+6*nu*q)
        claimed=lower_bound(N,eta,zeta,E,nu,q)
        assert Amin+1e-13 >= claimed
        A=Amin*(1+rng.random()*2)
        capacity=A*(E*E+6*nu*q)
        assert capacity >= 3*W-1e-10
        checks+=2

    E=2.3; nu=0.017
    prev=0
    for n in [10,30,100,300,1000,3000,10000]:
        q=n**-2; eta=n**-2; zeta=n**-2
        A=lower_bound(n,eta,zeta,E,nu,q)
        assert A>prev
        assert A/(n/E**2)>2.99
        prev=A
        checks+=2

    print(f'PASS R44 unit-work amplitude-center algebra checks={checks}')
    print('CERTIFIED: A_I >= 3(N-eta/2-zeta)/(E0^2+6 nu q_I) from R01/R40/R41 budgets')
    print('SCOPE: extraction/algebra certificate only; spatial peak is not compactness or an energy atom')

if __name__=='__main__': main()
