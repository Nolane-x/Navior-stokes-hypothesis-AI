from fractions import Fraction

checks=0

# L^(8/3) interpolation between L^1 and L^6.
assert Fraction(3,8) == Fraction(1,4) + Fraction(3,4)*Fraction(1,6)
checks += 1
assert Fraction(1,4)*Fraction(8,3) == Fraction(2,3)
assert Fraction(3,4)*Fraction(8,3) == Fraction(2,1)
checks += 2

# Exact gradient comparison for V=rho^(1/2)u=rho^(3/2)e:
# |grad V|^2=(9/4)a+b, D3 density=2a+b, a,b>=0.
for a in [Fraction(0),Fraction(1,7),Fraction(2),Fraction(11,3)]:
    for b in [Fraction(0),Fraction(3,5),Fraction(4),Fraction(9,2)]:
        lhs=Fraction(9,4)*a+b
        rhs=Fraction(9,8)*(2*a+b)
        assert lhs <= rhs
        checks += 1

# ||V||_1=U^(3/2), hence the interpolation prefactors become U and U^4.
assert Fraction(3,2)*Fraction(2,3) == 1
assert Fraction(3,2)*Fraction(8,3) == 4
checks += 2

# Young split for sqrt(2) U^2 |PL| written as
# (sqrt(U)|PL|)(sqrt(2)U^(3/2)).
for s in [Fraction(1,3),Fraction(1),Fraction(5,2)]:
    U=s*s
    for a in [Fraction(0),Fraction(2,5),Fraction(3)]:
        x2=U*a*a
        y2=2*U**3
        assert 2*x2*y2 <= (x2+y2)**2
        checks += 1

print(f'PASS R26 solenoidal critical-action criterion algebra: {checks} checks')
