# RD001 — No universal amplitude-independent absorption of critical `L^3` pressure work

**Status:** `exact structural no-go / not claimed novel`  
**Kills:** the naive H1 subroute `W_3 <= C D_3` with a universal amplitude-independent constant  
**Does not kill:** geometry-dependent, scale-dependent, frequency-dependent, or critical-norm-dependent pressure control

R01 gives

`(1/3)d/dt ∫|u|^3 + ν D_3(u) = W_3(u,p)`,

where

`W_3(u,p)=∫ p u·∇|u|`.

A tempting closure would be to prove a universal bound

`W_3(u,p) <= C D_3(u)`

for every smooth divergence-free periodic field, ideally with `C<ν`. This route is impossible.

## Explicit mean-zero nonvanishing family

Work on the unit torus `T^3=(R/Z)^3`. Set

`Z = 2πz`, `A = 2π(x+y+z)`, `B = 2π(x+y)`

and define

`u_base = (sin Z, cos Z, 0)`,

`w = (-sin A, sin A, cos B)`.

Both fields are smooth, periodic, mean-zero and divergence-free. Also `|u_base|=1`. Let

`u_ε = u_base + ε w`.

Since `|w|<=sqrt(3)`, for `|ε|<1/(2sqrt(3))` we have `|u_ε|>=1/2`, so all amplitude/direction expressions are smooth.

Let `p_ε` be the zero-mean pressure determined by

`-Δp_ε = Σ_{i,j} ∂_i u_{ε,j} ∂_j u_{ε,i}`.

Then

`W_3(ε) := ∫ p_ε u_ε·∇|u_ε|`

has the expansion

`W_3(ε) = (π/6) ε^2 + O(ε^3)`.

In particular, `W_3(ε)>0` for all sufficiently small nonzero `ε`.

## Exact second-order calculation

Write

`p_ε = ε p_1 + O(ε^2)`,

because the base field has zero pressure source. The first pressure coefficient is

`p_1 = (1/3)[ cos 2π(x+y-z) - cos 2π(x+y+z)`

`               - sin 2π(x+y+z) - sin 2π(x+y-z) ]`.

This follows by direct substitution into the pressure Poisson equation.

Because `|u_base|=1`, the first amplitude variation is

`ρ_1 = u_base·w = (cos Z - sin Z) sin A`.

Thus the first streamline-amplitude term is

`q_1 := u_base·∇ρ_1`

`    = 2π cos(4πz) cos 2π(x+y+z)`

`    = π[ cos 2π(x+y+3z) + cos 2π(x+y-z) ]`.

Therefore

`W_3(ε) = ε^2 ∫p_1 q_1 + O(ε^3)`.

All Fourier modes are orthogonal except the common mode `cos 2π(x+y-z)`. Since its coefficients are `1/3` in `p_1` and `π` in `q_1`, and its squared torus average is `1/2`,

`∫p_1 q_1 = (1/3) π (1/2) = π/6 > 0`.

## Amplitude-scaling obstruction

Fix one sufficiently small `ε` with `W_3(u_ε,p_ε)>0` and set

`u^{(a)} = a u_ε`, `a>0`.

The pressure scales quadratically:

`p^{(a)} = a^2 p_ε`.

Hence

`W_3(u^{(a)},p^{(a)}) = a^4 W_3(u_ε,p_ε)`,

while the R01 diffusion functional scales cubically:

`D_3(u^{(a)}) = a^3 D_3(u_ε)`.

Consequently

`W_3(u^{(a)},p^{(a)}) / D_3(u^{(a)})`

`= a [W_3(u_ε,p_ε)/D_3(u_ε)] -> infinity` as `a->infinity`.

Therefore:

> For every finite constant `C`, there exists a smooth periodic mean-zero divergence-free field with `W_3 > C D_3`.

Taking `C=ν` and using local smooth existence shows that there are smooth periodic initial data for which

`d/dt ||u(t)||_3^3 |_{t=0} > 0`.

Thus `||u||_3` has no universal monotonicity principle of this direct pressure-absorption form.

## Research consequence

H1 survives only in a sharper form. Any successful critical `L^3` route must exploit a quantity that changes under the amplitude scaling above, for example:

- dynamically generated direction geometry;
- frequency/concentration information;
- a critical norm coupled to pressure work;
- a nonlocal cancellation special to the true solution trajectory rather than an arbitrary instantaneous divergence-free field.

A statewise universal inequality `W_3 <= C D_3` is permanently discarded.
