# R06 — Critical Bernoulli/Lamb action controls the `L^3` barrier

**Status:** `verified-partial conditional reduction / not claimed novel`  
**Depends on:** R01, R03  
**Clay status:** does not prove the critical action is finite; therefore not global regularity

R01 gives the exact critical balance

`(1/3)d/dt ||u||_3^3 + nu D_3 = W_3`,

and R03 gives

`W_3 = <Q(omega x u), Q(|u|u)>`.

R06 controls the second Helmholtz defect by the **amplitude part of the same R01 dissipation**, producing a scale-critical spacetime obstruction that every successful proof through this route must defeat.

Work on the unit three-torus and let `C_H` denote any constant for the mean-zero periodic dual Sobolev estimate

`|| grad(-Delta)^(-1) f ||_2 <= C_H ||f||_(6/5)`.

Let

`rho=|u|`, `G=rho u`, `L=omega x u`.

## 1. Test-field Helmholtz defect estimate

Because `div u=0`,

`div G = u·grad rho`.

For `rho>0`, writing `n=u/rho`,

`u·grad rho`

`= rho n·grad rho`

`= (2/3) rho^(1/2) n·grad(rho^(3/2))`.

Therefore, almost everywhere (with the zero set handled by the continuous/weak interpretation),

`|div G| <= (2/3) rho^(1/2) |grad(rho^(3/2))|`.

Holder with exponents `3` and `2` gives

`||div G||_(6/5)`

`<= (2/3) ||rho^(1/2)||_3 ||grad(rho^(3/2))||_2`

`= (2/3) ||u||_(3/2)^(1/2) ||grad(rho^(3/2))||_2`.

Since

`QG = grad Delta^(-1) div G`

up to the harmless sign convention for `Delta`, and R01 contains

`D_3 >= (8/9)||grad(rho^(3/2))||_2^2`,

we obtain the exact-constant reduction

> `||Q(|u|u)||_2 <= (C_H/sqrt(2)) ||u||_(3/2)^(1/2) D_3^(1/2)`.

## 2. Critical pressure-work estimate

Using R03,

`|W_3| <= ||QL||_2 ||QG||_2`

so

> `|W_3| <= (C_H/sqrt(2)) ||u||_(3/2)^(1/2) ||Q(omega x u)||_2 D_3^(1/2)`.

Young's inequality gives

`|W_3| <= (nu/2)D_3`

`          + (C_H^2/(4nu)) ||u||_(3/2) ||Q(omega x u)||_2^2`.

Substitution into R01 yields

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`

> `<= (C_H^2/(4nu)) ||u||_(3/2) ||Q(omega x u)||_2^2`.

Hence for every smooth interval `[0,T]`,

> `||u(T)||_3^3 + (3nu/2) int_0^T D_3 dt`

> `<= ||u(0)||_3^3 + (3 C_H^2/(4nu)) A_L(T)`,

where the **critical Lamb/Bernoulli action** is

> `A_L(T) = int_0^T ||u||_(3/2) ||Q(omega x u)||_2^2 dt`.

Because R03 gives

`Q(omega x u) = -grad B`, `B=p+|u|^2/2`,

this can equivalently be written

`A_B(T)=int_0^T ||u||_(3/2) ||grad(p+|u|^2/2)||_2^2 dt`.

## 3. Scale audit

Under the local Euclidean Navier–Stokes scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

- `||u||_(3/2)` scales as `lambda^(-1)`;
- `||Q(omega x u)||_2^2` scales as `lambda^3`;
- `dt` scales as `lambda^(-2)`.

Thus

> `A_L` is scale invariant.

This is the main structural gain over replacing `||u||_(3/2)` by a fixed torus energy bound: the weighted action has exactly the scaling of a plausible critical continuation obstruction.

## 4. Consequence for a hypothetical singularity

R06 proves directly, without any endpoint regularity theorem, that

> finite `A_L(T)` implies a finite a priori bound on `sup_{t<=T} ||u(t)||_3` and on the integrated R01 dissipation.

Consequently, in any framework where bounded `L^infinity_t L^3_x` is an endpoint continuation/regularity criterion, a finite-time singularity must force

> `A_L(T*) = infinity`.

The classical endpoint `L^infinity_t L^3_x` regularity theorem of Escauriaza–Seregin–Sverak establishes the corresponding critical regularity mechanism for the Cauchy problem; periodic use should be invoked only through an appropriate periodic/localized version rather than by silently treating the torus as finite-energy `R^3` data.

Primary reference for the endpoint mechanism:
L. Escauriaza, G. Seregin, V. Sverak, *L_{3,infinity}-solutions of the Navier-Stokes equations and backward uniqueness*, Russian Math. Surveys 58 (2003), 211–250, DOI 10.1070/RM2003v058n02ABEH000609.

## 5. Unit-torus energy corollary

Because the unit torus has volume one,

`||u||_(3/2) <= ||u||_2 <= ||u_0||_2`

along a smooth unforced solution by the energy inequality. Therefore the stronger sufficient condition

`int_0^T ||Q(omega x u)||_2^2 dt < infinity`

also bounds `||u||_3` on `[0,T]`.

This corollary is convenient but loses the local scale-critical form; the weighted action `A_L` is the canonical object.

## 6. What remains open

R06 does **not** show `A_L` is finite for arbitrary smooth data. That is now the sharpened H1/H3 frontier:

> Can the true Navier–Stokes dynamics prevent the scale-critical Bernoulli/Lamb action from diverging at a finite time?

A successful theorem must exploit evolution/history, because RD001 and RD002 show that arbitrary instantaneous states admit strong pressure growth and substantial projected Lamb coherence.

Candidate next mechanisms include:

1. a frequency-local flux inequality for `Q(omega x u)` that uses exact Leray triad geometry;
2. an integrated cancellation between `PL` and `QL` along the actual trajectory;
3. a concentration-compactness theorem showing any minimal blow-up with infinite `A_L` violates the four-way Helmholtz geometry exposed by R04;
4. a monotonicity or reverse-transfer law for a **nonquadratic**, scale-local functional (RD003 excludes the naive fixed-quadratic option).
