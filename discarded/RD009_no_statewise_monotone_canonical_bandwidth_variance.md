# RD009 — Canonical radial variance is not statewise monotone under Navier–Stokes

**Status:** `exact smooth periodic counterexample to a proposed closure mechanism`  
**Depends on:** R17  
**Does not imply:** finite-time blow-up, failure of global regularity, or divergence of `A_bw`

R17 gives

`(sigma_D^2)' = -2 <(D-lambda_*)^2u,P(omega×u)>`

`                  -2 nu ||D(D-lambda_*)u||_2^2`.

For the Stokes equation the first term vanishes and `sigma_D^2` decreases. A natural but false strengthening is that the full Navier–Stokes nonlinearity might preserve this monotonicity, or at least be statewise absorbable by the viscous term with an amplitude-independent constant.

RD009 gives an exact counterexample.

## 1. Explicit 3–4–5 triad

Work on the normalized `2 pi`-periodic torus and use normalized spatial-average inner products. Define

`v(x,y,z)`

`= (cos(4y), cos(3x), 0)`

`  + (1/5)(4,-3,0) sin(3x+4y)`.

The field is smooth, mean-zero and divergence-free. Its three active radial shells have frequencies `3`, `4`, `5`, with equal `L^2` energy.

Exact Fourier calculation gives

`E(v)=||v||_2^2 = 3/2`,

`M(v)=<Dv,v> = 6`,

`Z(v)=||Dv||_2^2 = 25`,

so

> `lambda_*(v)=4`,

and

> `sigma_D^2(v)=Z-lambda_*^2 E = 1`.

For

`s=(D-4)v`,

one also has

> `||D s||_2^2 = 17`.

## 2. Exact nonlinear production

Let

`N=P((v·grad)v)=P(omega×v)`.

The closed `3–4–5` Fourier triad calculation gives

> `<(D-4)^2 v,N> = -4/5`.

Hence the nonlinear contribution in the R17 variance law is positive:

> `-2 <(D-4)^2v,N> = 8/5`.

Now scale only the velocity amplitude:

`u_A=A v`, `A>0`.

The canonical center remains `lambda_*=4`, while

`sigma_D^2(u_A)=A^2`,

`||D(D-4)u_A||_2^2=17 A^2`,

and the nonlinear production scales cubically. Therefore the exact initial derivative along the smooth Navier–Stokes solution issued from `u_A` is

> `(sigma_D^2)'(0) = (8/5) A^3 - 34 nu A^2`.

Thus

> `(sigma_D^2)'(0)>0` whenever `A>(85/4)nu`.

For every fixed viscosity `nu>0`, smooth divergence-free periodic data can therefore make the canonical radial variance initially increase.

## 3. What is falsified

RD009 falsifies all of the following unrestricted strategies:

1. `sigma_D^2(t)` is universally nonincreasing for Navier–Stokes;
2. the R17 nonlinear variance production is always nonpositive;
3. the nonlinear variance production can be absorbed by the R17 viscous term with an amplitude-independent statewise constant for arbitrary smooth states;
4. R16's bandwidth mechanism can be closed merely by invoking the Stokes tendency to narrow the spectrum.

The counterexample is statewise and local in time. It says nothing about whether such production can remain coherent over a scale-critical sequence of time intervals.

## 4. Surviving positive route

A viable theorem must use additional information, for example:

- time-integrated cancellation of the centered determinant;
- helical triad signs or flux constraints unavailable to arbitrary instantaneous states;
- frequency-local dissipation versus production over parabolic scale-time boxes;
- a minimal-blow-up compactness/rigidity argument;
- a quantitative relation between `A_spin` and variance production that prevents both mechanisms from staying large.

This is exactly the type of trajectory-level information that the R16 frontier already demands.

## 5. Verification scope

`verification/check_R17_RD009_spectral_variance.py` reconstructs the triad with exact rational complex Fourier arithmetic, including the Leray projection, and certifies

`E=3/2`, `M=6`, `Z=25`, `lambda_*=4`, `sigma_D^2=1`,

`||D(D-lambda_*)v||_2^2=17`,

and

`<(D-lambda_*)^2v,P((v·grad)v)>=-4/5`.

The coordinate convention only fixes the common unit of Fourier frequency. On `R^3/Z^3` the corresponding physical frequencies acquire the common `2 pi` factor; the amplitude-scaling no-go is unchanged.
