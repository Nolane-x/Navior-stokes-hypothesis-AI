# R04 — Orthogonal Helmholtz half-bound for critical pressure work

**Status:** `exact structural theorem / elementary Hilbert-space mechanism; not claimed novel`  
**Depends on:** R03  
**Clay status:** verified partial structure only; not global regularity

R03 gives

`W_3 = <Q(ω×u), Q(|u|u)>`.

The two **unprojected** vectors in this identity are pointwise orthogonal:

`(ω×u)·(|u|u)=0`.

This simple fact combines with a sharp projector inequality to give a universal factor `1/2` that ordinary Cauchy–Schwarz misses.

## Abstract projector lemma

Let `H` be a real or complex Hilbert space, `Q` an orthogonal projector, `P=I-Q`, and let `x,y∈H` satisfy

`<x,y>=0`.

Then

`|<Qx,Qy>| = |<Px,Py>|`

and

> `|<Qx,Qy>| <= (1/2)||x|| ||y||`.

The constant `1/2` is sharp for general orthogonal pairs and projectors.

### Proof

Set

`a=||Qx||/||x||`, `b=||Qy||/||y||`,

with the zero-norm cases trivial. Orthogonality gives

`<Px,Py> = -<Qx,Qy>`.

Thus Cauchy–Schwarz in both complementary subspaces yields

`|<Qx,Qy>|/(||x||||y||)`

`<= min( ab, sqrt((1-a^2)(1-b^2)) )`.

If `ab<=1/2`, the claim is immediate. If `ab>1/2`, then with `A=a^2`, `B=b^2`, we have `AB>1/4` and

`A+B >= 2sqrt(AB)`.

Hence

`(1-A)(1-B) = 1-(A+B)+AB`

`<= (1-sqrt(AB))^2 < 1/4`,

so the complementary Cauchy bound is `<1/2`. Therefore the minimum is always at most `1/2`.

Sharpness is attained already in `R^2`: take orthonormal

`x=(1,1)/sqrt(2)`, `y=(1,-1)/sqrt(2)`

and let `Q` project onto the first coordinate. Then `|<Qx,Qy>|=1/2`.

## Navier–Stokes corollary

Take

`x = L = ω×u`,

`y = G = |u|u`.

Since `L·G=0` pointwise, they are `L^2`-orthogonal. R03 and the lemma give

> `|W_3| <= (1/2) ||ω×u||_2 || |u|u ||_2`

or equivalently

> `|W_3| <= (1/2) ||ω×u||_2 ||u||_4^2`.

This holds for every smooth periodic divergence-free field for which the quantities are finite.

A sharper two-sided projector form is

`|W_3| <= min(`

`  ||Q(ω×u)||_2 ||Q(|u|u)||_2,`

`  ||P(ω×u)||_2 ||P(|u|u)||_2`

`)`.

## Scale audit

Under `u_λ(x,t)=λu(λx,λ^2t)` in three dimensions,

- `||ω×u||_2` scales as `λ^(3/2)`;
- `||u||_4^2` scales as `λ^(1/2)`;
- their product scales as `λ^2`.

This matches `W_3` and the R01 dissipation `D_3`. Thus R04 is genuinely scale-compatible rather than a supercritical dimensional artifact.

## Equality pressure and a new barrier variable

Define the full orthogonal-splitting efficiency

`χ(u) = 2 W_3 / ( ||ω×u||_2 ||u||_4^2 )`

when the denominator is nonzero. Then exactly

`|χ(u)|<=1`.

Near `|χ|=1`, the abstract proof forces both orthogonal fields to have approximately half of their squared `L^2` mass in the gradient Helmholtz sector and half in the divergence-free sector, together with near-saturation of both complementary Cauchy inequalities. Therefore a hypothetical pressure-driven concentration that nearly saturates R04 must satisfy a rigid **four-way Helmholtz balance**.

This creates a concrete adversarial target: test whether true Navier–Stokes Fourier geometry can approach that equality configuration across increasing mode families.

## Limitation

R04 still contains `||ω×u||_2`, which is not controlled by energy at critical scaling. The theorem is therefore a structural reduction, not closure. Its value is that it replaces a generic pressure estimate by a sharp constraint forced by two properties specific to the true vector calculus structure:

1. the Lamb factorization of R03;
2. pointwise perpendicularity of `ω×u` and `u`.
