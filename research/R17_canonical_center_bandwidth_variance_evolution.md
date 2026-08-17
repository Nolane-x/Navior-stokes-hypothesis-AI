# R17 — Canonical center-frequency and bandwidth-variance evolution

**Status:** `exact structural theorem / centered reformulation; novelty not claimed`  
**Depends on:** R14–R16  
**Clay status:** no a-priori closure is proved

R15 introduced the canonical radial center

`lambda_* = <D u,u>/||u||_2^2`, `D=sqrt(-Delta)`,

and the spectral variance

`sigma_D^2 = ||D u||_2^2 - lambda_*^2 ||u||_2^2`.

R17 derives their exact dynamics along every smooth mean-zero periodic Navier–Stokes solution. The point is to turn the static `A_bw` language of R16 into a production/dissipation budget.

Let `P` be the divergence-free Leray projector (`Q=I-P` in R03), let

`L = omega × u`,

and write the projected velocity equation as

`u_t + P L = -nu D^2 u`.

Set

`E = ||u||_2^2`,

`M = <D u,u>`,

`Z = ||D u||_2^2`,

`lambda = M/E`,

and

`s = (D-lambda)u`.

Then

> `sigma_D^2 = ||s||_2^2 = Z-lambda^2 E`.

The helical bandwidth defect from R15 is

`r_*=(D-lambda)u_+-(D-lambda)u_-`.

Because the two spin sectors are orthogonal and `D` preserves them,

> `||r_*||_2 = ||s||_2 = sigma_D`.

Thus the static bandwidth size in R15/R16 is exactly the radial spectral variance around the moving energy-weighted center.

## 1. Exact center-frequency law

Energy gives

`E' = -2 nu Z`.

Also

`M' = -2 <D u,P L> - 2 nu <D u,D^2 u>`.

Since `<u,P L>=<u,L>=0` pointwise after integration,

`<D u,P L> = <(D-lambda)u,P L> = <s,P L>`.

Define

`Y=<D u,D^2 u>`.

Differentiating `lambda=M/E` yields

> `lambda' = -(2/E)<s,P L> -(2 nu/E)(Y-lambda Z)`.

The viscous spectral-drift term has the exact positive representation

> `Y-lambda Z`
>
> `= sum_k (|k|-lambda)^2 (|k|+lambda) |u_hat(k)|^2`
>
> `>= lambda sigma_D^2`.

Therefore viscosity alone always drags the energy-weighted center toward lower radial frequencies, while an upward nonlinear drift requires the true projected Lamb force to correlate with the centered bandwidth defect `s`.

By Cauchy–Schwarz and the previous lower bound,

> `lambda' <= (2 sigma_D/E)||P L||_2 - (2 nu lambda/E)sigma_D^2`
>
> `<= ||P L||_2^2 / (2 nu lambda E)`.

This is only a one-sided conditional estimate; the right-hand side is not known to be integrable at a hypothetical singularity.

## 2. Exact moving-variance law

The centered defect satisfies `<s,u>=0`. Hence differentiating

`sigma_D^2=||s||_2^2`

does **not** produce a `lambda'` term:

`(sigma_D^2)' = 2 <s,(D-lambda)u_t>`.

Substituting Navier–Stokes gives the exact identity

> `(sigma_D^2)'`
>
> `= -2 <(D-lambda)^2 u,P L>`
>
> `  -2 nu ||D(D-lambda)u||_2^2`.

Equivalently, define the centered projected-Lamb forcing

`G_lambda = D^(-1)(D-lambda)P L`

(on the mean-zero subspace). Then

> `(sigma_D^2)' + 2 nu ||D s||_2^2 = -2 <D s,G_lambda>`.

Young's inequality yields the rigorous budget

> `(sigma_D^2)' + nu ||D s||_2^2 <= nu^(-1) ||G_lambda||_2^2`.

For the linear Stokes equation (`P L=0`), this becomes

> `(sigma_D^2)' = -2 nu ||D s||_2^2 <= 0`.

So nonlinear projected Lamb forcing is the **only** source that can replenish the unnormalized canonical radial variance.

## 3. Relation to R16

R16 uses

`A_bw = int ||u||_(3/2) ||r_* × u||_2^2 dt`.

R17 identifies the amplitude of `r_*` exactly with the moving variance `sigma_D`, but it also shows why a static variance estimate is insufficient: the quantity can be dynamically replenished by the centered Lamb determinant

`<(D-lambda)^2u, P(omega×u)>`.

The live bandwidth question is therefore sharpened from

> "is the spectrum narrow?"

to

> "can the true Navier–Stokes triad dynamics sustain non-summable centered-Lamb production of radial variance quickly enough to support the R16 ultraviolet bandwidth action?"

## 4. Literature interface

Lerner–Vigneron study the curl/spin decomposition and the nonlocal determinants

`int det(curl u,u,(-Delta)^theta u)`,

which include the type of fractional-energy nonlinear terms appearing in `M'`. R17 does not claim those underlying fractional energy identities as new; its contribution in this ledger is the canonical moving-center/variance recombination tied directly to R15/R16.

Primary source: Nicolas Lerner and François Vigneron, *On some properties of the curl operator and their consequences for the Navier-Stokes system*, arXiv:2203.07950.

## 5. Immediate falsification target

A tempting closure would be to hope that viscosity forces `sigma_D^2` to decrease statewise. R17 does **not** assert this. RD009 gives an exact smooth 3–4–5 Fourier triad for which the nonlinear production term overwhelms viscosity at sufficiently large amplitude and makes `(sigma_D^2)'(0)>0`.

Therefore any successful bandwidth theorem must use trajectory-integrated, scale-critical, localization, triad-sign, or compactness information beyond statewise monotonicity of `sigma_D^2`.
