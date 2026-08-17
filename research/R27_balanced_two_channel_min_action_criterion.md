# R27 — Balanced two-channel minimum-action criterion

**Status:** `exact conditional reduction / integrated channel-synchronization theorem`  
**Depends on:** R01, R03, R05–R07, R19, R24–R26  
**Clay status:** the balanced critical action is not proved finite for arbitrary data

R26 proves that finiteness of the solenoidal critical action

`A_sol(T)=int_0^T U ||P L||_2^2 dt`,

with `U=||u||_(3/2)` and `L=omega×u`, is sufficient to control the critical `L^3` barrier. R06 gives the analogous criterion for the gradient/Bernoulli action

`A_grad(T)=int_0^T U ||Q L||_2^2 dt`.

R27 sharpens both statements simultaneously. It removes the lower-order torus remainder from the R26 solenoidal estimate and proves that the **pointwise weaker Helmholtz channel** is itself a critical continuation quantity.

Work on the unit periodic torus in the canonical zero-mean Galilean frame.

## 1. Mean Lamb force vanishes

Use the exact identity

`(u·grad)u = omega×u + grad(|u|^2/2)`.

Periodicity and `div u=0` give

`int (u·grad)u dx = int div(u tensor u) dx = 0`,

and

`int grad(|u|^2/2) dx = 0`.

Therefore

> `int L dx = 0`.

Since `P` preserves the zero Fourier mode, this also gives

> `mean(P L)=0`.

## 2. Remove the nonlinear test-field mean exactly

Let

`rho=|u|`, `G=rho u`.

R05 gives the complementary pressure-work identity

> `W_3 = - <P L, P G>`.

Because `P L` is divergence-free,

`<P L,P G>=<P L,G>`.

Because `mean(P L)=0`,

> `W_3 = - <P L, G-mean(G)>`.

Thus the constant mode of `G` is completely invisible to the solenoidal pressure pairing. This allows a homogeneous Sobolev–Poincare estimate and removes the lower-order `U^3` remainder that appeared in R26.

## 3. Exact weighted derivative bound for `G=|u|u`

On `{rho>0}`, write

`u=rho e`, `|e|=1`.

Then

`G=rho^2 e`.

Since `e·partial_j e=0`, amplitude and direction derivatives are orthogonal and

> `|grad G|^2`
>
> `=4 rho^2 |grad rho|^2 + rho^4 |grad e|^2`.

Divide by `rho`:

`|grad G|^2/rho`

`=4 rho |grad rho|^2 + rho^3 |grad e|^2`.

R07 writes the `p=3` diffusion density as

`2 rho |grad rho|^2 + rho^3 |grad e|^2`.

Hence pointwise almost everywhere,

> `|grad G|^2/rho`
>
> `<= 2 [2 rho |grad rho|^2 + rho^3 |grad e|^2]`,

and therefore

> `int |grad G|^2/rho dx <= 2 D_3`.

At `rho=0` the quotient is interpreted by its natural limiting/weak value. The map `u -> |u|u` is `C^1`, and the estimate can equivalently be justified by regularization.

## 4. Weighted Holder transfers this to `W^{1,6/5}`

For a vector or matrix field `F`, write

`|F|^(6/5) = (|F|^2/rho)^(3/5) rho^(3/5)`.

Holder with exponents `5/3` and `5/2` gives

`int |F|^(6/5)`

`<= [int |F|^2/rho]^(3/5) [int rho^(3/2)]^(2/5)`.

Raising to the power `5/6`,

> `||F||_(6/5)`
>
> `<= [int |F|^2/rho]^(1/2) [int rho^(3/2)]^(1/3)`.

Since

`U=||u||_(3/2)`

and

`int rho^(3/2)=U^(3/2)`,

the second factor is `U^(1/2)`. Taking `F=grad G` and using Section 3,

> `||grad G||_(6/5) <= sqrt(2 U D_3)`.

## 5. Homogeneous periodic Sobolev–Poincare estimate

In three dimensions,

`W^(1,6/5) -> L^2`.

Let `C_SP` be a periodic mean-zero Sobolev–Poincare constant such that

`||F-mean(F)||_2 <= C_SP ||grad F||_(6/5)`.

Then

> `||G-mean(G)||_2`
>
> `<= C_SP sqrt(2 U D_3)`.

Substituting into Section 2,

> `|W_3|`
>
> `<= C_SP sqrt(2 U) ||P L||_2 D_3^(1/2)`.

Young's inequality yields the clean solenoidal estimate

> `|W_3|`
>
> `<= (nu/2) D_3`
>
> ` + (C_SP^2/nu) U ||P L||_2^2`.

Thus R01 gives

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`
>
> `<= C_sol U ||P L||_2^2`,

where

`C_sol=C_SP^2/nu`.

This is the scale-critical solenoidal criterion with no lower-order torus remainder.

## 6. Combine with the R06 gradient criterion

R06 independently proves, for the same left-hand side,

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`
>
> `<= C_grad U ||Q L||_2^2`,

with

`C_grad=C_H^2/(4nu)`.

Define

`a(t)=||P L(t)||_2^2`,

`b(t)=||Q L(t)||_2^2`,

and

`C_*=max(C_sol,C_grad)`.

Because the same quantity is bounded by both right-hand sides,

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`
>
> `<= U min(C_sol a, C_grad b)`
>
> `<= C_* U min(a,b)`.

This motivates the **balanced minimum action**

> `A_bal(T)`
>
> `:= int_0^T U(t)`
>
> `   min( ||P(omega×u)||_2^2, ||Q(omega×u)||_2^2 ) dt`.

Therefore

> `||u(T)||_3^3 + (3nu/2)int_0^T D_3 dt`
>
> `<= ||u(0)||_3^3 + 3 C_* A_bal(T)`.

Hence finite `A_bal(T)` gives an a-priori `L^infinity_t L^3_x` bound and integrated `D_3` bound on every smooth interval `[0,T]`.

As in R06, promotion from this endpoint bound to continuation uses the appropriate periodic/localized `L^infinity_t L^3_x` regularity theorem and is not silently assumed here.

## 7. Singularities require divergence of the weaker channel

Within the R01/R06 endpoint continuation framework, a finite-time singularity at `T*` must therefore satisfy

> `A_bal(T*) = infinity`.

This is strictly stronger than the R26 statement

`A_sol=infinity` and `A_grad=infinity`.

Indeed, both individual integrals can diverge while the two channels alternate so strongly in time that their pointwise minimum remains integrable. R27 rules out such a purely separated-channel singular mechanism: the **weaker channel itself must accumulate non-summable critical action**.

R27 does not prove exact dyadic synchronization on every scale-time box. It proves an integrated synchronization requirement. Alternation remains possible only if the minority channel still contributes enough cumulative critical mass for `A_bal` to diverge.

## 8. Balance-fraction interpretation

Orthogonality gives

`a+b=||L||_2^2`.

Also

> `min(a,b)=(a+b-|a-b|)/2`.

When `L` is nonzero, define the solenoidal fraction

`r=a/(a+b)`.

Then

> `min(a,b)=||L||_2^2 min(r,1-r)`.

Thus

`A_bal`

`=int U ||L||_2^2 min(r,1-r) dt`.

A singularity compatible with this proof spine must therefore carry non-summable full Lamb action **while maintaining enough two-channel Helmholtz balance that the minority fraction is not integrably negligible**.

This couples the S and G branches at the level of the actual singularity obstruction.

## 9. Scaling audit

Under Navier–Stokes scaling,

- `U=||u||_(3/2)` has exponent `-1`;
- `||P L||_2^2` and `||Q L||_2^2` have exponent `+3`;
- `dt` has exponent `-2`.

Therefore

> `A_bal` is exactly scale invariant.

No subcritical finite-volume norm is used in the canonical criterion.

## 10. Updated frontier

R27 changes the central question from

> can either physical Lamb channel diverge?

to the sharper question

> can an arbitrary smooth Navier–Stokes trajectory sustain a non-summable **balanced ultraviolet Lamb cascade** in which even the weaker Helmholtz channel carries critical action?

Together with R25, fixed low outputs are already harmless. The next decisive theorem should therefore be scale-local: show that simultaneous high-output S/G balance is incompatible with dissipation, helical structure, pressure/strain geometry, or a known continuation criterion.

R27 does not prove that theorem.

## 11. Verification

`verification/check_R27_balanced_channel_min_action.py` verifies the Sobolev exponent, weighted-Holder exponents, the exact derivative-density comparison, and the minimum-channel algebra with exact rational arithmetic.

The continuum proof relies on periodic integration by parts, the standard three-dimensional Sobolev–Poincare embedding `W^(1,6/5)->L^2`, Holder, and Young inequalities; no finite computation is promoted into the PDE theorem.
