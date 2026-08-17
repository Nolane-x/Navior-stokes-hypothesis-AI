# RD004 — The natural amplitude `A_2` weight route fails even on a global smooth Navier–Stokes shear

**Status:** `exact structural no-go`  
**Depends on:** R07  
**Kills:** any proof step that requires a uniform Muckenhoupt `A_2` bound for the exact amplitude weights `|u|` and `1/|u|` along all smooth Navier–Stokes trajectories  
**Does not kill:** regularized, localized, time-integrated, non-power, or solution-adapted weighted singular-integral estimates

R07 controls the critical Lamb force in the natural weight

`∫ |omega x u|^2 / |u| <= (3/2) D_3`.

A tempting next step is to transfer this estimate through the Helmholtz/Riesz projector using weighted `L^2` theory. The standard route would require the amplitude weight `rho=|u|` (equivalently its reciprocal) to belong quantitatively to the Muckenhoupt class `A_2`.

That requirement is false even for an explicit global smooth Navier–Stokes solution.

## Exact smooth shear solution

On the unit torus, let

`u(x,y,z,t) = ( a(t) sin(2 pi z), 0, 0 )`,

with

`a(t)=exp(-4 pi^2 nu t)`.

Then

- `div u=0`;
- `(u·grad)u=0`, because `u` points in the `x` direction and depends only on `z`;
- `Delta u = -(2 pi)^2 u`;
- with constant pressure, `partial_t u = nu Delta u`.

Thus this is an exact smooth periodic Navier–Stokes solution for every `t>=0`.

Its amplitude is

`rho(z,t)=a(t)|sin(2 pi z)|`.

Near any zero plane, for example `z=0`,

`rho(z,t) ~ 2 pi a(t)|z|`.

Therefore

`rho(z,t)^(-1) ~ [2 pi a(t)]^(-1)|z|^(-1)`.

But in any three-dimensional box crossing the zero plane,

`∫ rho^(-1) dx dy dz`

contains the divergent one-dimensional factor

`∫_{-epsilon}^{epsilon} dz/|z| = infinity`.

Hence `rho^(-1)` is not even locally integrable. In particular,

> `rho(·,t) notin A_2`

for every finite `t>=0`.

Multiplication by the positive scalar `a(t)` does not change the `A_2` obstruction.

## Stronger power-weight obstruction at initial time

For any fixed exponent `alpha>0`, choose an odd integer `m` with `m alpha >= 1` and smooth mean-zero divergence-free shear data

`u_m(x,y,z,0)=(sin(2 pi z)^m,0,0)`.

Then

`rho_m^alpha ~ |z|^(m alpha)`

near `z=0`, so its reciprocal behaves as `|z|^(-m alpha)` and is not locally integrable. Thus no nonzero fixed positive power of velocity amplitude has a universal `A_2` guarantee over all smooth divergence-free initial data.

The exact R07 critical weight corresponds to the boundary case `alpha=1`, which already fails persistently on the simple heat-shear solution above.

## Consequence

The following route is permanently discarded:

> R07 weighted Lamb control + a universal statewise/trajectory-wide `A_2` bound for `|u|` + standard weighted Riesz-transform boundedness => global pressure control.

The obstacle is not a hypothetical singular flow. The weight degeneracy occurs in a completely regular solution with zero convection.

## What remains viable

A weighted-projection strategy must avoid demanding global `A_2(|u|)` control. Possible surviving variants are structurally different:

1. regularized weights with constants tracked quantitatively as the regularization vanishes;
2. localization away from nodal surfaces plus a separate treatment of low-amplitude regions;
3. weights built from a nonlocal/maximal envelope of amplitude rather than `|u|` itself;
4. time-integrated commutator estimates that exploit the PDE without requiring pointwise-in-time weighted Calderon–Zygmund boundedness;
5. a decomposition in amplitude levels where projection leakage across levels is estimated directly.

RD004 therefore sharpens the R07 frontier: **the missing mechanism cannot simply be imported from standard `A_2` theory using the raw velocity amplitude.**
