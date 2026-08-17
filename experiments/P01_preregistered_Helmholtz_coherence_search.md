# P01 — Preregistered search for high Helmholtz-defect coherence

**Status:** `preregistered experiment`  
**Depends on:** R02  
**Registration time:** before the frozen primary measurement below  
**Clay status:** computational evidence only; cannot prove or disprove global regularity

## Motivation

R02 factorizes the critical pressure work as

`W_3 = <Q[(u·∇)u], Q[|u|u]>`

and defines the normalized defect coherence

`κ(u) = W_3 / (||Q[(u·∇)u]||_2 ||Q[|u|u]||_2)`.

A tempting H1 subroute would require a statewise universal angle gap `κ <= κ_* < 1`, preferably with a strong margin. Before building on such a claim, P01 searches adversarially for highly aligned smooth divergence-free Fourier states.

## Pilot disclosure

Before this preregistration, an exploratory low-mode pseudospectral search was performed to debug the representation. It found:

- random Gaussian fields with small positive/negative coherence;
- a sparse low-mode field with `κ ≈ 0.236`;
- an unfrozen stochastic hill-climb candidate with `κ ≈ 0.8207468` on a coarse `12^3` grid.

These pilot values are **not** confirmatory evidence and will not be rewritten as preregistered predictions.

## Frozen basis

Use the seven wavevectors

```text
(1,0,0), (0,1,0), (0,0,1),
(1,1,0), (1,0,1), (0,1,1),
(1,1,1)
```

and, for each wavevector `k`, two fixed real polarization vectors spanning `k^⊥`. For every polarization use both cosine and sine phases. This gives 28 real coefficients.

Fields are mean-zero, real, smooth, periodic, and exactly divergence-free at the analytic Fourier level.

## Frozen optimizer

Deterministic seed: `20260817`.

1. Draw `5000` coefficient vectors from independent standard normals and normalize each to Euclidean coefficient norm one.
2. Keep the largest measured `κ`.
3. Run `12000` hill-climb proposals from that candidate. At proposal `j`, add isotropic Gaussian coefficient noise with standard deviation
   `σ_j = 0.20 * (0.02/0.20)^(j/11999)`,
   renormalize, and accept iff measured `κ` increases.
4. No restarts, adaptive schedules, basis changes, or manual coefficient edits after measurement begins.

The optimizer is allowed to optimize only `κ`; it may not optimize a surrogate and then report `κ` post hoc.

## Frozen discretization and confirmation

Optimization grid: `N=24` points per dimension.

For the winning coefficient vector, recompute `κ` independently at

`N = 24, 32, 48, 64`.

Use spectral derivatives and the Fourier Helmholtz projector. Products are evaluated pseudospectrally. Because `|u|u` is not band-limited, the result is accepted as numerically converged only if the last two values differ by less than `2e-4`.

## Frozen hypotheses

The pilot already rules out preregistering a threshold below `0.8207468`.

The new confirmatory question is deliberately harder:

- **H-high:** the frozen search produces a converged state with `κ >= 0.90`.
- **H-gap:** the frozen search fails to reach `0.90`.

This experiment does **not** interpret H-gap as proof of a universal bound; it only means this fixed challenger failed.

If H-high occurs, every proposed universal statewise gap `κ <= 0.90` is falsified immediately.

## Outputs frozen in advance

The result artifact must report:

- best `κ` after the random stage;
- best `κ` after the frozen hill climb;
- convergence table for `N=24,32,48,64`;
- coefficient vector of the winner;
- norms `||QN||_2`, `||QG||_2`, and `W_3` at confirmation resolutions;
- exact seed and implementation hash/checksum;
- verdict `H-high`, `H-gap`, or `INCONCLUSIVE_DISCRETIZATION`.

No threshold, optimizer budget, basis, or convergence tolerance may be changed after the primary measurement without creating a new experiment ID.
