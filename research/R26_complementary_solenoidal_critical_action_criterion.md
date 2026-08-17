# R26 — Complementary solenoidal critical-action criterion and two-channel co-divergence

**Status:** `exact conditional reduction / trajectory coupling theorem`  
**Depends on:** R01, R05–R07, R19, R24–R25  
**Clay status:** neither critical channel is proved finite for arbitrary data

R06 proves that the critical `L^3` barrier closes if the **gradient/Bernoulli** action

`A_grad(T)=int_0^T U ||Q L||_2^2 dt`,

is finite, where

`U=||u||_(3/2)`, `L=omega×u`.

R19 later split the full Lamb action into

`A_L=A_sol+A_grad`,

with

`A_sol(T)=int_0^T U ||P L||_2^2 dt`.

R19 could only conclude that a tail-driven singularity makes at least one channel diverge. R26 proves the complementary continuation estimate: **finite `A_sol` also controls the critical `L^3` norm.** Hence a singular trajectory compatible with the R01/R06 endpoint mechanism must make **both** channels diverge.

Work on the normalized unit periodic torus in the canonical zero-mean Galilean frame.

## 1. Complementary pressure-work representation

R05 gives

> `W_3 = - <P L, P(|u|u)>`.

Since `P L` is divergence-free,

`<P L,P(|u|u)>=<P L,|u|u>`.

Therefore

> `|W_3| <= ||P L||_2 || |u|u ||_2`.

The problem is now to estimate the nonlinear test field by the same `L^3` diffusion geometry used in R01.

## 2. The correct transformed field

Let

`rho=|u|`,

and define

> `V=rho^(1/2)u=rho^(3/2)e`

on `{rho>0}`, with the natural continuous value `V=0` on the zero set.

Then

`|V|=rho^(3/2)`

and

> `|| |u|u ||_2^2 = int rho^4 = ||V||_(8/3)^(8/3)`.

Also

`||V||_1 = int rho^(3/2) = U^(3/2)`.

## 3. Exact gradient comparison with `D_3`

On `{rho>0}`,

`V=rho^(3/2)e`.

Because `e·partial_j e=0`, the amplitude/direction cross term vanishes exactly and

> `|grad V|^2`
>
> `= (9/4) rho |grad rho|^2 + rho^3 |grad e|^2`.

R07 gives the exact `p=3` diffusion geometry

`D_3=int [2 rho|grad rho|^2 + rho^3|grad e|^2]`.

Consequently

> `||grad V||_2^2 <= (9/8) D_3`.

The zero set is handled by approximation/chain-rule arguments for the locally Lipschitz map `u -> |u|^(1/2)u`; equivalently one may first use `rho_eps=(rho^2+eps^2)^(1/2)` and pass to the limit.

## 4. Periodic Gagliardo–Nirenberg estimate

Interpolation between `L^1` and `L^6` gives

`||V||_(8/3) <= ||V||_1^(1/4) ||V||_6^(3/4)`.

Raise to `8/3`:

> `||V||_(8/3)^(8/3) <= ||V||_1^(2/3) ||V||_6^2`.

On the unit torus, write `V=(V-mean V)+mean V`. Periodic Sobolev/Poincare and `|mean V|<=||V||_1` give, for a torus constant `C_S`,

`||V||_6 <= C_S ||grad V||_2 + ||V||_1`.

Therefore

`||V||_6^2 <= 2 C_S^2 ||grad V||_2^2 + 2 ||V||_1^2`.

Using Sections 2–3,

> `|| |u|u ||_2^2`
>
> `<= (9/4) C_S^2 U D_3 + 2 U^4`.

Equivalently,

> `|| |u|u ||_2`
>
> `<= (3/2) C_S U^(1/2) D_3^(1/2) + sqrt(2) U^2`.

The `U^4` term is a fixed-domain/zero-mode lower-order term. It is not the critical ultraviolet term.

## 5. Critical solenoidal pressure estimate

Insert the previous bound into the complementary pressure representation:

`|W_3|`

`<= (3/2) C_S U^(1/2)||P L||_2 D_3^(1/2)`

`   + sqrt(2) U^2 ||P L||_2`.

Young's inequality gives

> `|W_3|`
>
> `<= (nu/2) D_3`
>
> ` + [9 C_S^2/(8nu) + 1/2] U ||P L||_2^2`
>
> ` + U^3`.

Define

`C_sol(nu)=9 C_S^2/(8nu)+1/2`.

R01 then yields

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`
>
> `<= C_sol(nu) U ||P(omega×u)||_2^2 + U^3`.

Integrating on `[0,T]`,

> `||u(T)||_3^3 + (3nu/2)int_0^T D_3 dt`
>
> `<= ||u(0)||_3^3 + 3 C_sol(nu) A_sol(T) + 3 int_0^T U^3 dt`.

On the unit torus, energy gives

`U<=||u||_2<=E0=||u_0||_2`,

so

`int_0^T U^3 dt <= T E0^3`.

Hence:

> **finite `A_sol(T)` implies an a-priori finite `L^infinity_t L^3_x` bound and finite integrated `D_3` on `[0,T]`.**

As in R06, converting this endpoint bound into continuation uses the corresponding periodic/local endpoint regularity theorem; R26 does not silently replace that obligation.

## 6. Two-channel co-divergence theorem

R06 already gives the complementary statement:

> finite `A_grad(T)` controls the same `L^3` barrier.

Therefore, within the R01/R06 continuation framework, a finite-time singularity at `T*` must satisfy simultaneously

> `A_sol(T*)=infinity`
>
> **and**
>
> `A_grad(T*)=infinity`.

This strictly sharpens R19's earlier necessary statement

`A_sol=infinity or A_grad=infinity (or both)`.

The canonical singularity requirement after R26 is **co-divergence of both orthogonal physical Lamb channels**.

## 7. Ultraviolet consequence with R19/R25

R19 proves that any divergent channel action escapes every fixed Fourier cutoff. R25 independently removes fixed low-output pressure work.

Thus a singular trajectory in this proof program must sustain, at arbitrarily high output frequencies:

1. non-summable solenoidal physical Lamb action `U||P L||_2^2`;
2. non-summable Bernoulli-gradient physical Lamb action `U||Q L||_2^2`;
3. high-output critical pressure coupling rather than a bounded-output artifact.

This is substantially more rigid than the E23 two-branch dichotomy: neither physical channel may remain regular while the other alone carries the singularity.

R26 does **not** prove that the two divergences occur on the same dyadic scale-time boxes. Establishing synchronization/coupling across scales is the next major target.

## 8. Scaling audit

`A_sol` is scale invariant by R19. The leading term

`U ||P L||_2^2 dt`

has total scaling exponent zero.

The torus remainder `int U^3 dt` is lower order under ultraviolet Euclidean blow-up rescaling and is finite on every finite interval by energy. It is not the critical obstruction.

## 9. Verification

`verification/check_R26_solenoidal_action_criterion.py` checks the exact interpolation exponents, the `9/8` gradient comparison, the transformation of `||V||_1` into powers of `U`, and the Young-splitting algebra.

The functional inequalities used are standard periodic interpolation and Sobolev/Poincare estimates; no finite computation is promoted into the continuum theorem.
