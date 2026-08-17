# R03 — Bernoulli/Lamb-defect factorization of the critical `L^3` obstruction

**Status:** `exact structural reduction / classical identities recombined; not claimed novel`  
**Depends on:** R01, R02  
**Clay status:** not a global proof

R02 writes the critical pressure work as

`W_3 = < Q[(u·∇)u], Q[|u|u] >`.

R03 removes a large gradient component exactly and shows that only the longitudinal part of the **Lamb/vortex force** can drive this obstruction.

Let

`ρ=|u|`, `ω=curl u`, `K=ρ^2/2`, `G=ρu`,

and let `Q=I-P` be the periodic gradient Helmholtz projector.

The Lamb identity is

`(u·∇)u = ω×u + ∇K`.

The pressure equation/Leray decomposition gives

`Q[(u·∇)u] = -∇p`.

Therefore, for the Bernoulli function

`B = p + K`,

we have the exact identity

`Q(ω×u) = -∇B`.

## Exact orthogonality

The kinetic-energy gradient is globally orthogonal to the nonlinear `L^3` test defect:

`<∇K, QG> = <∇K, G>`

because `∇K` is a gradient and `Q` is the orthogonal gradient projector. But

`<∇K,G>`

`= ∫ (ρ∇ρ)·(ρu)`

`= ∫ ρ^2 u·∇ρ`

`= (1/3)∫ u·∇(ρ^3)`

`= 0`

on the torus since `div u=0`.

Hence the R02 factorization sharpens to

> `W_3 = < Q(ω×u), Q(|u|u) >`.

Equivalently,

> `W_3 = -<∇B,Q(|u|u)> = ∫ B u·∇|u|`.

The replacement of `p` by `B=p+|u|^2/2` in the last integral is exact because the local kinetic term integrates to zero.

## Consequences

### 1. The true obstruction is a longitudinal Lamb defect

Define

`L(u)=Q(ω×u)` and `A(u)=Q(|u|u)`.

Then

`W_3=<L,A>`.

A critical `L^3` route can therefore focus on the size and alignment of these two **true-Navier–Stokes structural defects**, rather than on an opaque pressure scalar.

### 2. Beltrami / velocity-vorticity alignment kills the pressure obstruction

If `ω×u=0` pointwise, then `L=0`, so

`W_3=0`.

R01 then gives monotone `L^3` dissipation while the smooth solution remains in that exact aligned class. This is only a special structural case, not a general theorem.

### 3. A new normalized coherence variable

Whenever both defects are nonzero, define

`κ_L = W_3 / ( ||Q(ω×u)||_2 ||Q(|u|u)||_2 )`.

Then `|κ_L|<=1` exactly.

Unlike R02's normalization with `Q[(u·∇)u]`, `κ_L` removes the kinetic gradient component that is provably invisible to `W_3`. Therefore `κ_L` is the sharper adversarial quantity for testing an angle-depletion hypothesis.

### 4. Scale audit

Under the Euclidean Navier–Stokes scaling

`u_λ(x,t)=λu(λx,λ^2t)`,

`||Q(ω×u)||_2` scales as `λ^(3/2)`, while `||Q(|u|u)||_2` scales as `λ^(1/2)`. Their product scales as `λ^2`, exactly the same as `W_3` and `D_3` in R01. Thus the factorization does not lose the critical scaling.

## Research fork created by R03

A positive theorem must obtain at least one of the following along actual Navier–Stokes trajectories near a hypothetical concentration event:

1. **Lamb-size depletion:** `||Q(ω×u)||_2` is smaller than generic critical scaling predicts;
2. **amplitude-defect depletion:** `||Q(|u|u)||_2` is controlled by the R01 dissipation with a concentration-defeating gain;
3. **Lamb/amplitude angle depletion:** `κ_L` becomes quantitatively separated from `+1` strongly enough to close R01;
4. a coupled inequality combining all three.

The next adversarial experiment must target `κ_L`, not the less intrinsic R02 coherence.

## Scope warning

All identities above are exact, but none supplies an a priori global estimate. In particular, `|κ_L|<=1` is only Cauchy–Schwarz; a useful strict gap or dynamical depletion remains unproved.
