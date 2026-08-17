# R35 — Smooth commutator null symbol and low-velocity-frequency gain

**Status:** `exact Fourier-symbol theorem / one-sided scale gain`  
**Depends on:** R23, R33–R34  
**Clay status:** does not sum the remaining high-velocity/high-high interactions; no global regularity conclusion

R33 identifies the smooth cross-representation synchronization defect as

`D_K=<[A_K,C_u]omega,G>`,

where

`A_K=M_K^2`, `C_u omega=omega×u`, `G=|u|u`.

R35 computes the exact Fourier symbol of this commutator and shows that **low-frequency velocity modulation cannot generate a full-strength defect**.

Let the real even smooth symbol of `A_K` be

`a_K(xi)=a(xi/K)`,

where `a` is a fixed bounded `C^1` profile. Write

`A_inf=||a||_infinity`,

`L_a=||grad a||_infinity`.

## 1. Exact commutator triad symbol

Using Fourier convention `exp(i k·x)`, the product

`omega×u`

at output `k` is

`sum_{p+q=k} omegahat(p)×uhat(q)`.

Applying `A_K` after multiplication contributes the factor `a_K(k)`, while applying it first to `omega` contributes `a_K(p)`. Therefore

> `widehat{[A_K,C_u]omega}(k)`
>
> `=sum_{p+q=k}`
>
> ` [a_K(k)-a_K(p)]`
>
> ` [omegahat(p)×uhat(q)]`.

Since `k=p+q`, the commutator multiplier is exactly

> `a((p+q)/K)-a(p/K)`.

A spatially constant velocity multiplier has `q=0` and therefore contributes **exactly zero**.

## 2. Mean-value low/high ratio gain

The mean-value theorem gives

`|a_K(p+q)-a_K(p)|`

`<=L_a |q|/K`.

The trivial bounded-symbol estimate gives

`|a_K(p+q)-a_K(p)|<=2A_inf`.

Hence every triad satisfies

> `|a_K(p+q)-a_K(p)|`
>
> `<=min(2A_inf, L_a |q|/K)`.

This is the R35 null structure.

If

`|q|<=eta K`,

then

> `|a_K(p+q)-a_K(p)|<=L_a eta`.

Thus the portion of the synchronization defect in which the **multiplying velocity** lies well below the filter scale carries a genuine small factor.

## 3. What frequency is forced to be high

The frequency `p` belongs to vorticity and the frequency `q` belongs to the velocity that multiplies it inside the Lamb force.

R35 says that a commutator defect of order one cannot be produced by a velocity modulation with `|q|/K ->0` unless another norm or multiplicity compensates for the symbol gain.

In particular, any candidate sequence that saturates the smooth commutator at increasing `K` must place substantial effective weight in interactions with

> `|q| comparable to or larger than K`,

or in a sufficiently large accumulation of lower-frequency interactions to overcome their individual `|q|/K` suppression.

This is an **input-scale bridge** for the R33/R34 common-mode defect.

## 4. Relation to R23

R23 studies

`Q(|u|u)=[Q,|u|]u`

and finds a gain when velocity frequency is high but amplitude frequency is low.

R35 studies the different commutator

`[A_K,C_u]omega`

and finds a gain when the **multiplying velocity frequency is low relative to the filter scale**.

The two null structures act on different sides of the pressure-work mechanism:

- R23 constrains the nonlinear test defect `G`;
- R35 constrains the smooth P/Q synchronization defect of the Lamb factor `L`.

A closing paraproduct theorem may need to use both simultaneously rather than estimating either factor generically.

## 5. Velocity-only form

Since

`omegahat(p)=i p×uhat(p)`,

the commutator can be written entirely in velocity modes:

`widehat{[A_K,C_u]omega}(k)`

`=i sum_{p+q=k}`

` [a_K(k)-a_K(p)]`

` [(p×uhat(p))×uhat(q)]`.

Thus every dangerous smooth-defect interaction is a genuine velocity triad with the additional symbol difference imposed by the filter commutator.

Incompressibility `p·uhat(p)=0` remains available for further helical/triad analysis.

## 6. Dyadic frontier after R35

Relative to a filter scale `K`, split the multiplying velocity input into

1. **very low `q`:** `|q|<<K`; commutator-small by `|q|/K`;
2. **transition `q`:** `|q|~K`; no small symbol factor, but the interaction is localized to the active scale;
3. **high `q`:** `|q|>>K`; no gain from R35 alone and must be coupled to dissipation, R20 high-input support, or a published frequency-local criterion.

R35 therefore removes the possibility that the smooth representation defect is a purely low-frequency modulation phenomenon.

## 7. Limitation

The symbol gain is not by itself a norm estimate. Large numbers of triads, high vorticity amplitude, or the nonlinear test factor `G` can offset a small individual multiplier.

R35 does **not** prove

`|D_K|<=o(1)`

uniformly along arbitrary trajectories, nor does it improve R32's integrated compensator bound by itself.

The next useful result must convert the symbol gain into a summable paraproduct/frequency-window estimate without assuming the conclusion of a known regularity criterion.

## 8. Verification

`verification/check_R35_smooth_commutator_null_symbol.py` reconstructs the commutator Fourier convolution from independent finite-mode data and checks the exact multiplier difference. It also stress-tests the mean-value gain on many integer triads using a smooth Gaussian profile with a known global gradient bound.

The theorem itself is the elementary Fourier product rule plus the mean-value theorem; no sharp-cutoff multiplier claim is involved.
