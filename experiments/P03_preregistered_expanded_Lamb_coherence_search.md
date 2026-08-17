# P03 — Preregistered expanded-family challenger for Lamb-defect coherence

**Status:** `preregistered experiment`  
**Depends on:** R03, R04, P02  
**Clay status:** finite-dimensional adversarial search only

P02's frozen seven-wavevector family reached only `κ_L≈0.33810`. That is not a theorem and may be a basis artifact. P03 deliberately expands the Fourier geometry before any statewise angle-gap conjecture is promoted.

## Pilot disclosure

The only prior information used to set this experiment is the committed P02 result. No search in the expanded family below was run before this registration.

## Frozen expanded wavevector family

Use one representative from each nonzero sign pair in `{-1,0,1}^3`, chosen by requiring the first nonzero component to be positive:

```text
(0,0,1),
(0,1,-1), (0,1,0), (0,1,1),
(1,-1,-1), (1,-1,0), (1,-1,1),
(1,0,-1), (1,0,0), (1,0,1),
(1,1,-1), (1,1,0), (1,1,1)
```

For each of the 13 wavevectors use two deterministic orthonormal transverse polarizations and both cosine/sine phases, giving **52 real coefficients**. Normalize the coefficient vector to Euclidean norm one.

This family strictly contains the directional content of P02 and adds mixed-sign triad geometry.

## Frozen objective

Maximize

`κ_L = <Q(ω×u),Q(|u|u)> / (||Q(ω×u)||_2 ||Q(|u|u)||_2)`.

## Frozen optimizer

Seed: `20260819`.

1. `3000` normalized Gaussian coefficient draws.
2. Keep the maximum `κ_L`.
3. `8000` sequential hill proposals.
4. Noise schedule
   `σ_j = 0.20*(0.015/0.20)^(j/7999)`.
5. Renormalize each proposal and accept iff `κ_L` increases.
6. No restarts, adaptive basis changes, post-hoc coefficient editing, or threshold changes.

Optimization grid: `N=24`.

## Frozen independent-resolution gate

Recompute the winner at `N=24,32,48,64`. Require

`|κ_L(N=64)-κ_L(N=48)| < 2e-4`.

## Frozen hypotheses

P02 makes a `0.95` threshold uninformative for the expanded challenger. P03 therefore tests a substantially stronger falsifier:

- **H-break-half:** the expanded frozen search finds a converged state with `κ_L >= 0.50`.
- **H-below-half:** the frozen challenger fails to reach `0.50`.

Interpretation remains one-way:

- H-break-half kills any future universal claim `κ_L<=0.5` immediately;
- H-below-half does **not** prove such a bound.

## Required outputs

- random-stage and final maxima;
- 52 winning coefficients;
- confirmation table at all four resolutions;
- `W_3`, `||Q(ω×u)||_2`, `||Q(|u|u)||_2`;
- exact seed and implementation SHA-256;
- verdict `H-break-half`, `H-below-half`, or `INCONCLUSIVE_DISCRETIZATION`.
