# R30 — Fixed-cutoff balanced high-pass action escape

**Status:** `exact conditional reduction / scale-local balanced-action theorem`  
**Depends on:** R01, R06, R25, R27–R29  
**Clay status:** does not bound the surviving high-pass balanced action; no global regularity conclusion

R27 proves that a singular endpoint in the critical `L^3` framework must make the global balanced action

`A_bal=int U min(||PL||_2^2,||QL||_2^2) dt`

diverge, where

`U=||u||_(3/2)`, `L=omega×u`.

R29 then synchronizes the cumulative productive pressure work in the two representations modulo an energy-controlled low-frequency compensator.

R30 strengthens the action side itself: **for every fixed Fourier cutoff, the balanced minority action above that cutoff must diverge.** Thus the R27 minority channel cannot remain large only because of bounded-frequency mass.

Let

`G=|u|u`,

and let `Pi_{<=K}`, `Pi_{>K}` be the orthogonal Fourier projectors used in R25/R28.

Define

`p_K(t)=||Pi_{>K} P L||_2`,

`q_K(t)=||Pi_{>K} Q L||_2`.

## 1. Low-output pressure work is harmless in either representation

R25 gives, for the gradient representation,

`|W_grad,<=K|<=B_K(t)`,

while R28 gives the same estimate for the solenoidal representation,

`|W_sol,<=K|<=B_K(t)`,

where

> `B_K(t)=N_K ||omega||_2 ||u||_2^3`,

and

`N_K=#{k in Z^3:0<|k|<=K}`.

For every finite smooth interval `[0,T]`, energy/enstrophy imply

> `int_0^T B_K(t) dt`
>
> `<=N_K E0^4 sqrt(T/(2nu))<infinity`,

with `E0=||u_0||_2`.

Therefore either exact pressure representation may be used at each time; the corresponding low-output remainder is always absolutely integrable.

## 2. High-pass test fields inherit the global diffusion bounds

R06 proves

`||QG||_2 <= C_g sqrt(U D_3)`,

with

`C_g=C_H/sqrt(2)`.

Because `Pi_{>K}` and `Q` commute and are contractions,

> `||Pi_{>K}QG||_2 <= C_g sqrt(U D_3)`.

On the solenoidal side, R27 proves

`||G-mean(G)||_2 <= C_s sqrt(U D_3)`,

where

`C_s=sqrt(2) C_SP`.

The high-pass projector kills the constant mode and commutes with `P`, so

> `||Pi_{>K}PG||_2`
>
> `<=||G-mean(G)||_2`
>
> `<=C_s sqrt(U D_3)`.

Thus the nonlinear test field is diffusion-controlled in either high-pass representation with constants independent of `K`.

## 3. Adaptive use of the weaker high-pass Lamb channel

The two exact decompositions are

`W_3=W_grad,<=K+W_grad,>K`,

and

`W_3=W_sol,<=K+W_sol,>K`.

Hence

`|W_3|`

`<=B_K + C_g sqrt(U D_3) q_K`,

and independently

`|W_3|`

`<=B_K + C_s sqrt(U D_3) p_K`.

Let

`C_0=max(C_g,C_s)`.

Taking the better of the two valid bounds at each time gives

> `|W_3|`
>
> `<=B_K + C_0 sqrt(U D_3) min(p_K,q_K)`.

This step is legitimate even though the two high-pass pressure works are not pointwise equal: whichever representation is chosen, its own low-frequency remainder is bounded by the same `B_K` envelope.

Young's inequality yields

> `|W_3|`
>
> `<=B_K +(nu/2)D_3`
>
> ` +(C_0^2/(2nu)) U min(p_K^2,q_K^2)`.

## 4. Fixed-cutoff balanced high-pass continuation criterion

R01 gives

`(1/3)d/dt ||u||_3^3 + nu D_3 = W_3`.

Combining with Section 3,

> `(1/3)d/dt ||u||_3^3 +(nu/2)D_3`
>
> `<=B_K +(C_0^2/(2nu))`
>
> `  * U min(p_K^2,q_K^2)`.

Define the **balanced high-pass action**

> `A_bal,>K(T)`
>
> `:=int_0^T U(t)`
>
> `  min(`
>
> `    ||Pi_{>K}P(omega×u)||_2^2,`
>
> `    ||Pi_{>K}Q(omega×u)||_2^2`
>
> `  ) dt`.

Integration gives

> `||u(T)||_3^3 +(3nu/2)int_0^T D_3 dt`
>
> `<=||u(0)||_3^3`
>
> ` +3 N_K E0^4 sqrt(T/(2nu))`
>
> ` +(3C_0^2/(2nu)) A_bal,>K(T)`.

Therefore, for **any one fixed finite cutoff `K`**, finiteness of `A_bal,>K(T)` controls the critical endpoint barrier.

## 5. Singularities force balanced action through every fixed cutoff

Within the same periodic/localized endpoint continuation framework used in R06/R27, a finite-time singularity at `T*` must therefore satisfy

> `A_bal,>K(T*)=infinity`

for **every fixed finite `K`**.

This is strictly sharper than R27's global

`A_bal(T*)=infinity`.

It rules out a mechanism in which the pointwise weaker Helmholtz channel accumulates its divergent action only through a bounded set of Fourier outputs while the other channel alone escapes to the ultraviolet.

A singular trajectory compatible with this proof spine must maintain enough simultaneous P/Q tail activity that even

`min(||Pi_{>K}PL||_2^2,||Pi_{>K}QL||_2^2)`

has non-summable critical action for every fixed cutoff.

## 6. Interaction with RD014

RD014 constructs smooth states with severe shell-by-shell separation between `PL` and `QL`. R30 does not contradict that no-go.

R30 requires neither:

- common-shell support;
- comparable energy on each shell;
- instantaneous shell overlap.

The two channel tails may occupy different high shells. What R30 forces near a singular endpoint is only that **both tails are simultaneously non-negligible above every fixed cutoff often enough for their pointwise minimum action to diverge**.

Thus the remaining scale separation is much narrower than arbitrary statewise shell separation.

## 7. Relation to R29

R29 synchronizes the **signed cumulative productive work** above each cutoff:

`W_grad,>K-W_sol,>K`

is an energy-controlled low-frequency compensator.

R30 independently synchronizes the **critical tail strength** by forcing divergence of the pointwise weaker high-pass Lamb action.

Together they imply that a putative singular mechanism must carry, above every fixed cutoff:

1. divergent common-mode positive pressure work;
2. divergent balanced minority Lamb action.

This is a substantially more rigid object than the two independent E23 channel obstructions.

## 8. Scaling audit

For a cutoff family rescaled together with the Navier–Stokes transformation,

`K -> lambda K`,

the integrand

`U min(||Pi_{>K}PL||_2^2,||Pi_{>K}QL||_2^2) dt`

has exponent

`-1 +3 -2 =0`.

Thus the family is scale-covariant at the critical level. A numerically fixed torus cutoff by itself is not called scale-invariant; the cutoff must transform with the spatial scale.

## 9. Sharpened frontier after R30

The live obstruction is now a **common productive, balanced-tail ultraviolet cascade**.

A closing theorem may target one of the following stronger statements:

1. a uniform-in-`K` estimate for `A_bal,>K`;
2. decay of the minority tail fraction as `K->infinity` strong enough to contradict R30;
3. a flux identity coupling R29 common productive work to R30 balanced tail action and viscous dissipation;
4. a published frequency-local criterion whose hypothesis follows from the simultaneous high-pass balance forced here.

R30 proves none of these final bounds.

## 10. Verification

`verification/check_R30_fixed_cutoff_balanced_highpass.py` exhaustively verifies the adaptive-minimum algebra, Young inequality structure, critical scaling exponents and finite-low-plus-finite-high-action continuation logic using exact rational arithmetic.

The continuum proof itself uses only the already verified R06/R27 test-field bounds, R25/R28 finite-output estimates, contraction/commutation of Fourier and Helmholtz projectors, Young's inequality, and the R01 critical balance.
