# P02 — Preregistered adversarial search for near-alignment of the true Lamb defects

**Status:** `preregistered experiment`  
**Depends on:** R03  
**Clay status:** finite-dimensional challenger only

R03 sharpens the critical pressure obstruction to

`W_3 = < Q(ω×u), Q(|u|u) >`.

Define

`κ_L = W_3 / (||Q(ω×u)||_2 ||Q(|u|u)||_2)`.

A useful statewise angle-depletion theorem would require a quantitative gap below `+1`. P02 tries to destroy that possibility before any proof effort is invested in it.

## Frozen field family

Use the same 28-real-parameter, seven-wavevector divergence-free trigonometric family as P01:

```text
(1,0,0), (0,1,0), (0,0,1),
(1,1,0), (1,0,1), (0,1,1),
(1,1,1).
```

For each wavevector, use two deterministic orthonormal transverse polarizations and both sine/cosine phases. Normalize the 28-vector of coefficients to Euclidean norm one.

## Frozen optimizer

Seed: `20260818`.

- `5000` independent normalized Gaussian coefficient draws;
- keep the largest `κ_L`;
- `12000` sequential hill proposals;
- proposal noise standard deviation
  `σ_j = 0.20*(0.02/0.20)^(j/11999)`;
- renormalize after every proposal;
- accept iff `κ_L` increases;
- no restarts, basis changes, adaptive schedules, or manual edits.

Optimization resolution: `N=24`.

## Independent-resolution gate

For the winning coefficient vector recompute `κ_L`, `W_3`, `||Q(ω×u)||_2`, and `||Q(|u|u)||_2` at

`N=24,32,48,64`.

Accept numerical convergence only if the N=48 and N=64 values of `κ_L` differ by `<2e-4`.

## Frozen hypotheses

No `κ_L` pilot search was run before this preregistration.

- **H-near:** the frozen search produces a converged state with `κ_L >= 0.95`.
- **H-gap:** it fails to reach `0.95`.

Interpretation is deliberately asymmetric:

- `H-near` immediately falsifies every proposed universal statewise bound `κ_L<=0.95`;
- `H-gap` does **not** prove any universal gap and only records challenger failure.

## Required output

- random-stage maximum;
- final hill maximum;
- confirmation table at N=24,32,48,64;
- winning 28-vector;
- exact seed;
- implementation SHA-256;
- verdict `H-near`, `H-gap`, or `INCONCLUSIVE_DISCRETIZATION`.
