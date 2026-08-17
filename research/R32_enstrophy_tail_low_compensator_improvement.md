# R32 — Enstrophy-tail improvement for the low-frequency synchronization compensator

**Status:** `exact analytic improvement / stronger synchronization defect estimate`  
**Depends on:** R25, R29–R31  
**Clay status:** does not make the compensator uniform on parabolic scales; no global regularity conclusion

R29 identifies the exact cross-representation high-pass mismatch

`D_K=W_grad,>K-W_sol,>K`

as the negative low-frequency raw pairing

`D_K=-<Pi_{<=K}L,Pi_{<=K}G>`,

where

`L=omega×u`, `G=|u|u`.

The first R29 estimate used only `L^1` Fourier coefficient bounds on both factors and gave the finite-mode growth `N_K`.

R32 spends one available energy derivative more efficiently. It improves the compensator to `N_K^(2/3)` growth and makes the time dependence proportional to the **actual enstrophy tail**.

Work on the normalized unit torus in the canonical zero-mean frame.

## 1. Low Lamb factor from `L^1`

As before,

`||L||_1<=||omega||_2||u||_2`.

On the finite output set of size `N_K`, the Fourier coefficient bound gives

> `||Pi_{<=K}L||_2`
>
> `<=N_K^(1/2)||omega||_2||u||_2`.

No additional derivative is used on this factor.

## 2. Improve the nonlinear test factor through `L^(3/2)`

For

`G=|u|u`,

we have

`||G||_(3/2)=||u||_3^2`.

Interpolation gives

`||u||_3^2<=||u||_2||u||_6`.

For zero-mean periodic divergence-free velocity, Sobolev and the standard curl/gradient equivalence give

`||u||_6<=C_S||grad u||_2=C_S||omega||_2`.

Therefore

> `||G||_(3/2)`
>
> `<=C_S||u||_2||omega||_2`.

Hausdorff–Young sends `L^(3/2)` to Fourier `ell^3`. Restricting an `ell^3` sequence to `N_K` modes and embedding `ell^3 -> ell^2` on that finite set costs only `N_K^(1/6)`. Hence

> `||Pi_{<=K}G||_2`
>
> `<=C_HY N_K^(1/6)||G||_(3/2)`
>
> `<=C_1 N_K^(1/6)||u||_2||omega||_2`.

Here `C_1` depends only on the normalized Fourier/Sobolev conventions, not on `K` or the solution.

## 3. Improved pointwise compensator estimate

Cauchy–Schwarz now yields

> `|D_K|`
>
> `=|<Pi_{<=K}L,Pi_{<=K}G>|`
>
> `<=C_1 N_K^(2/3)`
>
> `  * ||u||_2^2 ||omega||_2^2`.

With `E0=||u_0||_2`, energy monotonicity gives the canonical form

> `|D_K(t)|`
>
> `<=C_1 N_K^(2/3) E0^2 ||omega(t)||_2^2`.

Since lattice counting has `N_K` of cubic order, the cutoff growth is of quadratic order rather than the cubic growth in the original R29 `L^1/L^1` bound.

## 4. Time-integrated enstrophy-tail estimate

For every interval `[a,b]` in the smooth lifespan,

> `int_a^b |D_K(t)| dt`
>
> `<=C_1 N_K^(2/3) E0^2`
>
> `  * int_a^b ||omega||_2^2 dt`.

The global energy inequality gives

`int_0^{T*}||omega||_2^2 dt<=E0^2/(2nu)`

through every smooth pre-endpoint interval, and the improper enstrophy integral has finite total mass.

Therefore, for every fixed `K`,

> `int_a^{T*}|D_K|dt -> 0`

as `a↑T*`.

This recovers the terminal synchronization of R29, but now the rate is controlled by the **remaining dissipation mass** rather than only by the geometric window length.

## 5. Stronger diagonal extraction

Let `K_n->infinity` and `epsilon_n->0` be arbitrary.

Because

`q(a)=int_a^{T*}||omega||_2^2 dt ->0`,

for each `n` one may choose `a_n<T*` so close to the endpoint that

> `q(a_n)`
>
> `<=epsilon_n /`
>
> `  [C_1 N_{K_n}^(2/3)E0^2]`.

Then

> `sup_{a_n<T<T*}`
>
> `|A_grad^{K_n}(a_n,T)-A_sol^{K_n}(a_n,T)|`
>
> `<=epsilon_n`.

R28/R30 still force the two productive works and balanced high-pass action to diverge on every such terminal interval. Thus R31's diagonal packet extraction can be based on the actual enstrophy tail rather than the cruder explicit `sqrt(delta)` estimate.

## 6. Combined best compensator estimate

R29 and R32 provide two independent controls:

> `int_a^b |D_K|dt`
>
> `<= min(`
>
> `  N_K E0^4 sqrt((b-a)/(2nu)),`
>
> `  C_1 N_K^(2/3) E0^2`
>
> `    * int_a^b ||omega||_2^2dt`
>
> `)`.

The first is explicit in interval length; the second has better cutoff growth and adapts to the actual dissipation history.

Neither dominates universally.

## 7. Why this is not yet parabolic-scale synchronization

On a parabolic time window of length comparable to `K^-2`, R32 alone does not provide an a-priori rate for the enstrophy tail as a function of `K`.

The energy inequality guarantees only absolute continuity of the enstrophy integral, not a universal modulus strong enough to cancel the `N_K^(2/3)` factor.

Therefore R32 does **not** prove that the two pressure-work representations synchronize uniformly on `K^-2` windows.

What it does prove is that the remaining nonuniformity has been reduced to a much more specific question:

> can Navier–Stokes dynamics provide a quantitative terminal enstrophy-tail modulus, or can additional structure reduce the compensator below the generic `K^2` counting scale?

## 8. Generic interpolation barrier

The R32 route uses only:

1. finite-mode counting / Hausdorff–Young;
2. energy `L^2` control;
3. one `H^1` derivative through enstrophy;
4. generic Sobolev interpolation.

Within this simple allocation, making the time factor no worse than `||omega||_2^2` naturally produces the combined cutoff exponent `1/2+1/6=2/3` in `N_K`, i.e. quadratic lattice-scale growth.

R32 does not claim a theorem that `K^2` is universally sharp. An improvement below this level must be tested for genuinely Navier–Stokes-specific cancellation rather than assumed from generic interpolation.

## 9. New frontier after R32

The most valuable next target is now quantitative and falsifiable:

> **improve the low-frequency orthogonality compensator using the exact structures `L=omega×u`, `G=|u|u`, incompressibility and/or the R24 transported-speed identity, beyond the generic `N_K^(2/3)` energy-enstrophy scale.**

A successful subquadratic compensator estimate, especially one compatible with parabolic windows, would materially strengthen the R31 compactness packet and could connect the common productive UV mechanism to a scale-invariant blow-up limit.

## 10. Verification

`verification/check_R32_enstrophy_tail_compensator.py` verifies the finite-set `ell^3 -> ell^2` factor `N^(1/6)`, the `L^3` interpolation inequality, the exponent bookkeeping producing `N_K^(2/3)`, and the diagonal absolute-continuity extraction logic.

The continuum proof uses standard Hausdorff–Young, Sobolev interpolation, Cauchy–Schwarz and the energy inequality.
