# RD002 — A universal statewise Lamb-defect coherence bound `κ_L <= 1/2` is falsified numerically

**Status:** `preregistered computational falsification with high-resolution robustness`  
**Depends on:** R03, P02, P03  
**Does not affect:** the exact R04 full-norm half-bound  
**Clay status:** not a regularity result

R03 defines

`κ_L = <Q(ω×u),Q(|u|u)> / (||Q(ω×u)||_2 ||Q(|u|u)||_2)`.

P02's seven-wavevector family reached only `κ_L≈0.3381`. That made a statewise projected-angle bound near `1/2` look superficially plausible, but no such claim was adopted. P03 was preregistered specifically to challenge it in an expanded mixed-sign Fourier family.

## Frozen P03 outcome

P03 used 13 wavevectors, 52 real divergence-free Fourier coefficients, seed `20260819`, 3000 random states and 8000 frozen hill proposals.

The winning state gave

`κ_L(N=24) = 0.5197517411371275`,

and independent-resolution confirmation gave

`κ_L(N=48) = 0.519728783424544`,

`κ_L(N=64) = 0.5197256482415721`.

The N=48/N=64 difference is about `3.14e-6`, far below the preregistered `2e-4` convergence tolerance. The frozen verdict is therefore

`H-break-half`.

A post-confirmation robustness replay retained the strict margin:

`κ_L(N=80)  = 0.5197248335505487`,

`κ_L(N=96)  = 0.5197249394119691`,

`κ_L(N=128) = 0.519725873321033`.

## Consequence

The research program permanently discards the subroute

> prove global regularity by establishing a universal **statewise** projected-angle inequality `κ_L<=1/2` for every smooth divergence-free field.

The P03 field is a strong converged numerical counterexample to that threshold.

## Important distinction from R04

RD002 does **not** contradict R04.

R04 proves

`|W_3| <= (1/2)||ω×u||_2 ||u||_4^2`,

where the denominator uses the **full unprojected norms** of two pointwise orthogonal fields.

`κ_L` instead normalizes by the two **gradient-projected norms**. A projected coherence greater than `1/2` is entirely compatible with the abstract half-bound.

## What survives

Three sharper possibilities remain live:

1. a different universal statewise bound `κ_L<c<1` with `c>0.5198`;
2. a **trajectory-dependent** depletion law that is false on arbitrary divergence-free states but enforced by Navier–Stokes evolution near concentration;
3. closure through defect sizes or four-way Helmholtz balance rather than angle alone.

Because increasing basis richness raised the observed maximum from about `0.338` to `0.520`, the project assigns lower priority to proving a statewise angle gap and higher priority to trajectory/history-dependent mechanisms.

## Evidence scope

P03 is not an interval-arithmetic proof of the counterexample. It is a preregistered finite-dimensional numerical falsification with a stable margin through N=128. Any future theorem using the exact threshold `1/2` must first supply a rigorous reason why the P03 field is outside its hypotheses.
