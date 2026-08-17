#!/usr/bin/env python3
"""Exact rational exponent verifier for RD016."""
from fractions import Fraction


def theta(p):
    return Fraction(3,2) * (p-Fraction(1)) / p


def alpha(p):
    return Fraction(3,1)/p - Fraction(1,2)


def main():
    checks=0
    candidates=[]
    # Dense rational grid on [1,3].
    for den in range(1,121):
        for num in range(den,3*den+1):
            p=Fraction(num,den)
            th=theta(p)
            al=alpha(p)
            # interpolation identity 1/(2p)=1/2-theta/3
            assert Fraction(1,2)/p == Fraction(1,2)-th/Fraction(3)
            checks+=1
            if 4*th<=2:
                assert p<=Fraction(3,2)
                candidates.append((2*al,p))
                checks+=1
            if p<=Fraction(3,2):
                assert 4*th<=2
                checks+=1
    best=min(candidates)
    assert best[0]==3
    assert best[1]==Fraction(3,2)
    checks+=2
    # Formula for post-Young cutoff exponent.
    for p in [Fraction(1),Fraction(6,5),Fraction(4,3),Fraction(3,2)]:
        assert 2*alpha(p)==Fraction(6,1)/p-1
        assert 2*alpha(p)>=3
        checks+=2
    print(f"PASS RD016 stress Holder-Bernstein barrier checks={checks}")

if __name__=='__main__':
    main()
