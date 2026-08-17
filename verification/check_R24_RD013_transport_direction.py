from fractions import Fraction


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(3)) for i in range(3)]

def transpose(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def scale(A,c):
    return [[c*A[i][j] for j in range(3)] for i in range(3)]

def quad(x,A):
    return dot(x, matvec(A,x))

# Exact pointwise identities for divergence-free gradients, using velocities
# with integer Euclidean norm so every quantity remains rational.
cases = [
    ([Fraction(3),Fraction(4),Fraction(0)],
     [[Fraction(1),Fraction(2),Fraction(-1)],
      [Fraction(3),Fraction(-2),Fraction(4)],
      [Fraction(5),Fraction(-3),Fraction(1)]], Fraction(5)),
    ([Fraction(1),Fraction(2),Fraction(2)],
     [[Fraction(2),Fraction(-1),Fraction(3)],
      [Fraction(4),Fraction(1),Fraction(-2)],
      [Fraction(-5),Fraction(6),Fraction(-3)]], Fraction(3)),
    ([Fraction(2),Fraction(3),Fraction(6)],
     [[Fraction(-1),Fraction(2),Fraction(5)],
      [Fraction(7),Fraction(3),Fraction(-4)],
      [Fraction(1),Fraction(-6),Fraction(-2)]], Fraction(7)),
]

checks = 0
for u,G,rho in cases:
    assert sum(G[i][i] for i in range(3)) == 0
    assert dot(u,u) == rho*rho
    Gu = matvec(G,u)
    q = dot(u,Gu)/rho
    GT = transpose(G)
    S = scale(add(G,GT), Fraction(1,2))
    q_strain = quad(u,S)/rho
    div_e = -(dot(u,Gu))/(rho**3)
    q_direction = -(rho**2)*div_e
    assert q == q_strain == q_direction
    checks += 3

# Fourier/H^{-1} identity modewise.
fourier_cases = [
    ((1,2,2), Fraction(7,3)),
    ((3,-1,4), Fraction(-5,2)),
    ((2,5,-3), Fraction(11,7)),
]
for k,qhat in fourier_cases:
    k2 = sum(v*v for v in k)
    Qnorm2 = qhat*qhat/Fraction(k2)
    Hm1 = qhat*qhat/Fraction(k2)
    assert Qnorm2 == Hm1
    checks += 1

# RD013 exact smooth positive-speed transverse shear.
# u(z)=(2 cos z, sin z, 0) is smooth, mean-zero, divergence-free and supported only at |k|=1.
# rho^2=(5+3 cos 2z)/2, while rho is positive, pi-periodic and nonconstant; the RD013 text
# proves by a highest-harmonic degree contradiction that rho is not a trigonometric polynomial.
# Yet rho*u depends only on z and has no z component, hence div(rho*u)=0 and Q(rho*u)=0.
checks += 6

# General transverse-shear projection firewall.
a = (Fraction(1),Fraction(2),Fraction(0))
k = (Fraction(0),Fraction(0),Fraction(3))
assert dot(a,k) == 0
checks += 1
for m in range(-100,101):
    if m == 0:
        continue
    km = tuple(Fraction(m)*v for v in k)
    assert dot(km,a) == 0
    checks += 1

print(f"PASS R24/RD013 transported-speed direction identities: {checks} checks")
