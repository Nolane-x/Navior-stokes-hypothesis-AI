from fractions import Fraction

checks=0

# Sobolev exponent W^{1,6/5} -> L^2 in dimension 3.
assert Fraction(1,2) == Fraction(5,6) - Fraction(1,3)
checks += 1

# Weighted Holder used for F=grad G:
# int |F|^(6/5) = int (|F|^2/rho)^(3/5) rho^(3/5)
# with Holder exponents 5/3 and 5/2; after raising to 5/6,
# A exponent is 1/2 and int rho^(3/2) exponent is 1/3 = U^(1/2).
assert Fraction(3,5)*Fraction(5,3) == 1
assert Fraction(3,5)*Fraction(5,2) == Fraction(3,2)
assert Fraction(3,5)*Fraction(5,6) == Fraction(1,2)
assert Fraction(2,5)*Fraction(5,6) == Fraction(1,3)
checks += 4

# G=rho u=rho^2 e:
# |grad G|^2=4 rho^2 |grad rho|^2 + rho^4 |grad e|^2.
# Dividing by rho is bounded by 2 times D3 density
# 2 rho|grad rho|^2 + rho^3|grad e|^2.
for a in [Fraction(0),Fraction(1,7),Fraction(3),Fraction(13,4)]:
    for b in [Fraction(0),Fraction(2,9),Fraction(5),Fraction(7,3)]:
        lhs=4*a+b
        rhs=2*(2*a+b)
        assert lhs <= rhs
        checks += 1

# Mean Lamb force vanishes because integral (u.grad)u and integral grad(|u|^2/2) vanish.
# Algebraic bookkeeping of the channel-min consequence:
# if X<=Cs*a and X<=Cg*b, then X<=max(Cs,Cg)*min(a,b).
for Cs,Cg in [(Fraction(1),Fraction(2)),(Fraction(7,3),Fraction(5,4)),(Fraction(9),Fraction(1,7))]:
    Cmax=max(Cs,Cg)
    for a,b in [(Fraction(1,5),Fraction(3)),(Fraction(4),Fraction(2,3)),(Fraction(5,2),Fraction(7,4))]:
        x=min(Cs*a,Cg*b)
        assert x <= Cmax*min(a,b)
        checks += 1

# min(a,b) is the full-action balance factor.
for a,b in [(Fraction(1),Fraction(3)),(Fraction(5),Fraction(2)),(Fraction(7,4),Fraction(7,4))]:
    assert min(a,b) == (a+b-abs(a-b))/2
    checks += 1

print(f'PASS R27 balanced-channel min-action algebra: {checks} checks')
