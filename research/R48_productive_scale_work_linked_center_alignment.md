# R48 — Productive-scale / work-linked-center alignment on R47 bursts

**Status:** `exact scale-alignment theorem / closes one RD024 branch / not closure`  
**Depends on:** R43, R46, R47  
**Clay status:** **NOT SOLVED**

E46/RD024 left open both extreme branches of the amplitude/productive-frequency ratio `Chi_theta=R_theta/A`: the productive scale could, at the scalar-envelope level, run arbitrarily faster or arbitrarily slower than an amplitude scale.  R47 adds a uniform critical `D_3` action on a positive-density subfamily of the actual unit common-work bursts.  R48 feeds that new PDE budget back into the R46 spatially local tail estimate.

The result is a genuine one-sided alignment theorem:

> on the R47 subfamily, the productive quantile frequency cannot outrun a work-linked amplitude scale by an arbitrary factor.

More strongly, rescaling directly by `R_theta` leaves a uniformly non-zero velocity amplitude at a center selected from the same weighted-gradient density that controls the common-work tail.

## 1. R47-good burst and local tail density

Let `J` be one of the R47-good unit common-work bursts at parent cutoff `L0`.  Set

> `D_J=int_J D_3(t)dt <= D_*:=28/(3nu)`.

Let

> `X_J=int_J int_(T^3)|u|^2|grad u|^2 dxdt`,
>
> `Sigma_J=sqrt(2) X_J`.

R46 gives

> `T_J(R)=sum_(|k|>R)|b_k(J)| <= Sigma_J/R`,

and unit normalization at `L0` gives

> `Sigma_J>=L0>0`.

Hence `D_J>0` as well.

## 2. Effective amplitude selected by the work-controlling density

Define

> `B_J:=X_J/D_J = Sigma_J/(sqrt(2)D_J)`.

Pointwise in spacetime,

`|u|^2|grad u|^2`

`=|u| [ |u||grad u|^2 ]`

`<= |u| d_3`,

where `d_3` is the R01 `D_3` density.  Therefore

> `B_J<=A_J:=sup_(T^3 x J)|u|`.

This amplitude scale is not an arbitrary supremum: it is the average amplitude seen by the first, load-bearing component of the critical `D_3` measure.

## 3. A work-linked high-amplitude set carries half the `X` mass

Define

> `H_J={ (x,t): |u(x,t)|>=B_J/2 }`.

On the complement,

> `|u|^2|grad u|^2 <= (B_J/2)d_3`.

Hence

`int_((T^3 x J)\H_J)|u|^2|grad u|^2`

`<= (B_J/2)D_J=X_J/2`.

Therefore

> `int_(H_J)|u|^2|grad u|^2 >= X_J/2`.

In particular `H_J` is nonempty.  Choose a point `(x_J,t_J)` in it. Then

> `|u(x_J,t_J)|>=B_J/2`.

Thus the selected center is tied to a set carrying a fixed fraction of the exact spacetime density used in the R46 common-work tail theorem.

## 4. Upper productive radius from the R46 absolute tail

Fix `0<theta<1`, and let `R_theta=R_theta(J,L0)` be the R43 positive common-work quantile radius.

The net common work above `L0` equals one, so its total positive mass is at least one.  For every `R>L0`, the positive tail is bounded by total variation:

> `sum_(|k|>R)(b_k)_+ <= T_J(R)<=Sigma_J/R`.

Thus positive work accumulated between `L0` and `R` is at least

> `1-Sigma_J/R`.

Since `Sigma_J>=L0`, choosing

> `R=Sigma_J/(1-theta)`

is admissible and gives

> `R_theta <= Sigma_J/(1-theta)`.

Using `Sigma_J=sqrt(2)B_JD_J` and the R47 bound,

> `R_theta/B_J`
>
> `<= sqrt(2)D_J/(1-theta)`
>
> `<= 28sqrt(2)/[3nu(1-theta)]`.

Equivalently,

> `B_J >= [3nu(1-theta)/(28sqrt(2))] R_theta`.

Because `B_J<=A_J`, R48 also obtains the direct one-sided amplitude alignment

> `R_theta/A_J <= 28sqrt(2)/[3nu(1-theta)]`.

This **eliminates the `Chi_theta=R_theta/A_J -> infinity` branch of RD024 on the R47-good subfamily.**

## 5. Parent cutoff is also aligned from below

From `Sigma_J>=L0` and `Sigma_J=sqrt(2)B_JD_J`,

> `B_J >= L0/(sqrt(2)D_J)`
>
> `>= [3nu/(28sqrt(2))]L0`.

Hence the work-linked effective amplitude itself grows at least linearly with the prescribed escaping parent cutoff.

## 6. Productive-scale rescaling is nontrivial at the work-linked center

At the point selected in Section 3,

`|u(x_J,t_J)|>=B_J/2`.

Combining with Section 4 gives

> `|u(x_J,t_J)|/R_theta`
>
> `>= 3nu(1-theta)/(56sqrt(2))`.

Now perform the Navier–Stokes rescaling at the **productive scale**

> `r_J=1/R_theta`,
>
> `v_J(y,s)=r_J u(x_J+r_J y,t_J+r_J^2 s)`.

Then

> `|v_J(0,0)|>=3nu(1-theta)/(56sqrt(2))`.

So the productive-scale rescaling cannot converge to zero merely because its amplitude normalization was too weak.  The rescaled sequence is quantitatively nontrivial at the selected center before any compactness passage.

At the same time:

- the common pressure-work integral is scale invariant;
- `int D_3 dt` is scale invariant and remains bounded by `D_*` on the rescaled burst;
- the R47 `L^3_tL^9_x` action is scale invariant and uniformly bounded;
- by the definition of `R_theta`, at least `theta` units of positive integrated common work have accumulated by normalized output radius `1`.

These facts give a substantially more rigid candidate for the E46 ancient/compactness transfer program.

## 7. What R48 closes and what remains open

R48 closes one precise E46/RD024 escape branch:

> productive frequency cannot escape to `+infinity` relative to the amplitude scale on the R47-good bursts.

It does **not** give the opposite inequality.  The branch

> `R_theta/A_J ->0`

may still occur if a much larger amplitude/spatial structure coexists with work carried at lower relative frequency.

Nor does R48 prove

- `R_theta^2|J|` is bounded below or above;
- a positive amount of work lies in a fixed annulus `c<|k|/R_theta<1` rather than cascading toward normalized frequency zero while a vanishing amount triggers the quantile endpoint;
- local energy bounds on fixed productive-scale cylinders;
- strong PDE compactness of `v_J`;
- passage of the global Fourier common-work measure to an ancient limit;
- a Liouville contradiction;
- global regularity.

The primary remaining bridge is now narrower:

> **establish parabolic time/spatial compactness for the nontrivial productive-scale R48 rescaling, or exploit the residual `R_theta/A ->0` branch / quantile IR cascade to obtain a contradiction.**

## 8. Verification

`verification/check_R48_productive_scale_alignment.py` checks the exact `X<=|u|d_3` implication, the effective-amplitude half-mass lemma, the tail-to-quantile bound, constants, and Navier–Stokes scaling.

A fresh verifier independently generates spacetime weighted samples and signed Fourier catalogues to test the half-mass and quantile consequences without importing the primary checker.

**R48 is a verified-partial candidate until its independent and repository-wide gates pass. It is not a proof of global regularity.**
