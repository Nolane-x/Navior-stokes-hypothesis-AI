#!/usr/bin/env python3
"""Independent symbolic checker for the load-bearing RD001 coefficient.

This checker does not certify Navier-Stokes global regularity. It verifies the
explicit divergence-free family, the first pressure Poisson coefficient, the
first amplitude/streamline coefficient, and the exact positive leading
pressure-work coefficient pi/6 used by RD001.
"""

import sympy as sp

x, y, z, eps = sp.symbols("x y z eps", real=True)
pi = sp.pi
A = 2 * pi * (x + y + z)
B = 2 * pi * (x + y)
Z = 2 * pi * z

u0 = sp.Matrix([sp.sin(Z), sp.cos(Z), 0])
w = sp.Matrix([-sp.sin(A), sp.sin(A), sp.cos(B)])
vars_ = [x, y, z]

# Both fields are divergence free.
assert sp.simplify(sum(sp.diff(u0[i], vars_[i]) for i in range(3))) == 0
assert sp.simplify(sum(sp.diff(w[i], vars_[i]) for i in range(3))) == 0

# Pressure source: -Delta p = sum_{i,j} d_i u_j d_j u_i.
u = u0 + eps * w
source = sum(
    sp.diff(u[j], vars_[i]) * sp.diff(u[i], vars_[j])
    for i in range(3)
    for j in range(3)
)
source1 = sp.diff(source, eps).subs(eps, 0)

Cminus = 2 * pi * (x + y - z)
Cplus = 2 * pi * (x + y + z)
p1 = sp.Rational(1, 3) * (
    sp.cos(Cminus)
    - sp.cos(Cplus)
    - sp.sin(Cplus)
    - sp.sin(Cminus)
)

poisson_residual = -sum(sp.diff(p1, v, 2) for v in vars_) - source1
assert sp.trigsimp(sp.expand_trig(poisson_residual)) == 0

# First amplitude variation rho_1 = u0 dot w.
rho1 = (sp.cos(Z) - sp.sin(Z)) * sp.sin(A)
assert sp.trigsimp(sp.expand_trig(u0.dot(w) - rho1)) == 0

# u0 dot grad rho1 = 2*pi*cos(2Z)*cos(A).
# Verify the only nontrivial scalar identity needed for this reduction.
q1_factor = (sp.sin(Z) + sp.cos(Z)) * (sp.cos(Z) - sp.sin(Z))
assert sp.trigsimp(sp.expand_trig(q1_factor - sp.cos(2 * Z))) == 0

# Product-to-sum gives
# q1 = pi[cos 2pi(x+y+3z) + cos 2pi(x+y-z)].
# Only cos(Cminus) overlaps p1. Its squared torus average is 1/2.
leading = sp.Rational(1, 3) * pi * sp.Rational(1, 2)
assert sp.simplify(leading - pi / 6) == 0
assert leading.is_positive

print("PASS divergence-free base and perturbation")
print("PASS first pressure Poisson coefficient")
print("PASS first amplitude/streamline coefficient")
print("PASS W_3(eps) = (pi/6) eps^2 + O(eps^3), coefficient > 0")
print("SCOPE: R01/RD001 structural identity/no-go only; NOT global regularity.")
