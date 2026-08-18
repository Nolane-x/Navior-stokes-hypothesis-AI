# R45 — Absolute common-work tail, intrinsic UV cap, and per-burst center extraction

**Status:** `exact conditional spectral-tail theorem / compactness ingredient / not closure`  
**Depends on:** R20, R39–R44  
**Clay status:** **NOT SOLVED**

E44 attaches a diverging amplitude center and an intrinsic productive radius to a singularity-compatible unit common-work burst, but it gives only **lower** floors for the productive radius.  R45 adds the missing opposite estimate: the *entire signed common-work tail* has a `1/R` total-variation bound controlled by the burst amplitude and enstrophy cost.

This produces a scale-covariant upper active frequency

> `Gamma_J := A_J^2 q_J`,

where

> `A_J = sup_(t in J)||u(t)||_infinity`,  
> `q_J = int_J ||omega(t)||_2^2 dt`.

For every R41 unit burst, `Gamma_J` dominates the parent cutoff, bounds the R43 positive-work quantile radius from above, forces a quantitative amplitude/enstrophy law, and makes the normalized signed common-work measure uniformly tight at high normalized frequencies.

R45 is therefore a genuine spectral compactness ingredient.  RD023 shows that it does **not** by itself prevent collapse toward zero normalized frequency; the remaining dimensionless obstruction is spectral spread between the lower productive radius and `Gamma_J`.

## 1. Setup

Work on the periodic torus `Omega=T^3` of volume `V`, with the same Fourier convention as R43,

`fhat(k)=V^-1 int_Omega f(x) exp(-ik·x) dx`.

Let

`rho=|u|`, `G=rho u`, `L=omega×u`,

and for nonzero output mode `k`,

> `c_k(t)=(V/2) Re[Lhat(k,t)·conj(J_k Ghat(k,t))]`,

where `J_k=Q_k-P_k` is the Helmholtz reflection and hence an isometry.

For a preterminal interval `J`, define

> `b_k(J)=int_J c_k(t)dt`.

On an R41 unit common-work burst at parent cutoff `L0`,

> `sum_(|k|>L0) b_k(J)=1`.

Write `ell_J=|J|`, `A_J=sup_J||u||_infinity`, and `q_J=int_J||omega||_2^2dt`.

## 2. Instantaneous absolute high-frequency tail

Parseval and Cauchy–Schwarz give, for every `R>0`,

`sum_(|k|>R)|c_k(t)|`

`<= (V/2) [sum_(|k|>R)|Lhat(k)|^2]^(1/2)`

`          [sum_(|k|>R)|Ghat(k)|^2]^(1/2)`.

The first factor is at most `V^-1/2||L||_2`.  For the second,

`sum_(|k|>R)|Ghat(k)|^2`

`<= R^-2 sum_k |k|^2|Ghat(k)|^2`

`= R^-2 V^-1||grad G||_2^2`.

Pointwise,

`|L|<=|u||omega|`,

and the R43 weak chain-rule estimate strengthens in `L^2` to

> `|grad G|<=2|u||grad u|` a.e.

Therefore

`||L||_2<=||u||_infinity||omega||_2`,

`||grad G||_2<=2||u||_infinity||grad u||_2`

`              =2||u||_infinity||omega||_2`.

The factor `2` cancels the `1/2` in the definition of `c_k`, giving the exact project bound

> `sum_(|k|>R)|c_k(t)|`
>
> `<= R^-1 ||u(t)||_infinity^2 ||omega(t)||_2^2`.

This is stronger than a modewise envelope: it controls the full signed-output tail in `ell^1_k` total variation.

## 3. Burstwise total-variation tail

Tonelli and the previous estimate give

> `T_J(R):=sum_(|k|>R)|b_k(J)|`
>
> `<= R^-1 int_J ||u(t)||_infinity^2||omega(t)||_2^2 dt`
>
> `<= A_J^2 q_J/R`.

Define the **intrinsic UV cap**

> `Gamma_J:=A_J^2 q_J`.

Then

> `T_J(R)<=Gamma_J/R`.

In particular, after frequency normalization `xi=k/Gamma_J`, the signed common-work measure

> `mu_J=sum_(|k|>L0) b_k(J) delta_(k/Gamma_J)`

satisfies, for every `r>0`,

> `|mu_J|({|xi|>r})<=1/r`.

Thus the high-frequency total variation is uniformly tight in the `Gamma_J` scale.

## 4. Every unit burst has its own amplitude center

At the parent cutoff `R=L0`, unit normalization gives

`1=|sum_(|k|>L0)b_k|`

` <=sum_(|k|>L0)|b_k|`

` <= L0^-1 int_J ||u||_infinity^2||omega||_2^2dt`.

Hence the stronger trajectory-level action statement

> `int_J ||u(t)||_infinity^2||omega(t)||_2^2dt >= L0`.

Consequently

> `Gamma_J=A_J^2 q_J>=L0`,

and

> `A_J>=sqrt(L0/q_J)`.

Since a preterminal burst is compact in time and the trajectory is smooth there, an actual maximizing time and point `(x_J,t_J)` exist.  Therefore **each** R41 unit burst, not merely one selected from a large R44 parent packet, carries its own amplitude center.  Along the diagonal singular extraction `L0->infinity` and `q_J->0`, so this center amplitude diverges.

## 5. Upper bound for the R43 positive-work quantile radius

Let `0<theta<1` and let `R_theta(J,L0)` be the R43 radius containing `theta` units of positive integrated common work.  Since

`sum_(|k|>L0)b_k=1`,

the total positive mass above `L0` is at least one.  For every `R>L0`,

`sum_(|k|>R)(b_k)_+ <= T_J(R)<=Gamma_J/R`.

Therefore

`sum_(L0<|k|<=R)(b_k)_+ >=1-Gamma_J/R`.

Choosing `R=Gamma_J/(1-theta)` is legitimate because `Gamma_J>=L0`, and gives

> `R_theta(J,L0) <= Gamma_J/(1-theta)`.

This is the first upper active-radius estimate in the unit-burst spine.

## 6. A third low-frequency capacity from the stress output factor

R43 gives two lower floors for `R_theta`.  There is also an independent low-frequency envelope using the exact stress form

> `L=div T`,  `T=u tensor u-(rho^2/2)I`.

Pointwise `|T|_F<=2|u|^2`, so

`|Lhat(k)|<=2V^-1 |k| E0^2`,

while

`|Ghat(k)|<=V^-1 E0^2`.

Thus

> `|c_k(t)|<=V^-1 E0^4 |k|`,

and on a burst of length `ell_J`,

> `|b_k(J)|<=V^-1 E0^4 ell_J |k|`.

Using `N(R)<=27R^3` and `|k|<=R`,

> `sum_(0<|k|<=R)|b_k(J)|`
>
> `<=27 V^-1 E0^4 ell_J R^4`.

Hence the positive quantile radius obeys the additional critical-homogeneous floor

> `R_theta(J,L0) >= [theta V/(27E0^4 ell_J)]^(1/4)`.

This estimate is independent of `q_J` and comes from the physical output derivative in `L=div T`.

## 7. Quantitative amplitude–dissipation laws

Combining the R45 upper radius with the three lower floors (the two from R43 plus the new stress floor) yields

> `A_J >= sqrt(L0/q_J)`,

> `A_J >= sqrt(1-theta) (theta V/26)^(1/4)`
> `       * E0^(-1/2) q_J^(-3/4)`,

> `A_J >= sqrt(1-theta) (theta V/27)^(1/6)`
> `       * E0^(-1/2) ell_J^(-1/12) q_J^(-7/12)`,

and

> `A_J >= sqrt(1-theta) (theta V/27)^(1/8)`
> `       * E0^(-1/2) ell_J^(-1/8) q_J^(-1/2)`.

All four are homogeneous under the Navier–Stokes concentration scaling.

The `q_J^(-3/4)` law is especially notable: a unit productive burst whose unweighted enstrophy cost tends to zero must pay a super-`q^-1/2` amplitude price.

## 8. What is now compact and what is still not

R43 provided a lower productive radius.  R45 provides a scale-covariant upper cap and, after normalization by `Gamma_J`, uniform high-frequency total-variation tightness.

Define the dimensionless spectral-spread ratio

> `Delta_theta(J):=Gamma_J/R_theta(J,L0)`.

R45 gives only

> `Delta_theta(J)>=1-theta`.

If `Delta_theta` remains bounded on a singular sequence, then the R43 productive radius and the R45 total-variation cap are comparable, giving a genuine bounded-frequency window for a fixed fraction of normalized productive work.

If instead `Delta_theta->infinity`, the work-carrying positive quantile scale collapses toward zero after `Gamma_J` normalization.  RD023 shows that all scalar envelopes proved through R45 permit this abstractly.  Therefore the next load-bearing theorem must either

1. bound `Delta_theta` using genuine PDE/helical input-output geometry; or
2. exploit the `Delta_theta->infinity` branch to obtain a contradiction from R36/R37 separated/output depletion or another dynamical rigidity principle.

## 9. What R45 does not prove

R45 does not prove

- a lower-frequency tightness bound after `Gamma_J` rescaling;
- bounded `Delta_theta`;
- spatial local-energy tightness at `Gamma_J^-1` or `R_theta^-1`;
- parabolic comparability of burst duration with either spectral scale;
- compactness of the rescaled velocity fields;
- a nontrivial ancient solution or Liouville contradiction;
- global regularity.

The new result is a two-sided spectral **architecture** for the normalized work, not the final rigidity theorem.

## 10. Verification scope

`verification/check_R45_absolute_common_work_tail.py` verifies the exact algebraic consequences, critical homogeneity, lattice/stress capacity, randomized signed-work tail/quantile inequalities, and the per-burst center bound.

`verification/fresh_verify_e45_common_work_tail_grid.py` independently reconstructs smooth divergence-free finite-Fourier fields in physical space and checks the instantaneous Parseval tail bound and stress-output low-mode envelope without importing the primary checker.

`verification/check_RD023_gamma_rescaling_low_frequency_collapse.py` verifies an abstract high-multiplicity family that satisfies the R42/R43/R45 scalar envelopes but collapses to zero normalized frequency after `Gamma_J` rescaling.

**R45 is a verified-partial candidate until its independent and repository-wide gates pass.  It is not a proof of Navier–Stokes global regularity.**
