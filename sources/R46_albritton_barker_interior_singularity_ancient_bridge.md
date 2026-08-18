# R46 source note — Albritton–Barker interior singularity bridge

**Source type:** primary research paper / theorem import  
**Use in this repository:** literature-backed bridge only; not claimed as an internally reproved theorem

## Primary source

Dallas Albritton and Tobias Barker, *Localised necessary conditions for singularity formation in the Navier-Stokes equations with curved boundary*, arXiv:1811.00507v2 (2019).

- arXiv: https://arxiv.org/abs/1811.00507
- Theorem 1.1: local `L^3` norm diverges in every fixed neighborhood of an interior singular point for the stated suitable-solution class.
- Theorem 1.2: an interior singularity generates a non-trivial mild bounded ancient solution in `R^3` as a blow-up limit.

The paper explicitly states that the interior case of Theorem 1.2 was already known and treats the boundary/localisation setting in greater generality.

## Scope mapping to the periodic project

The project studies a smooth periodic zero-forcing solution on `T^3` up to a hypothetical finite maximal smooth time `T*`.

For any point `x*` in the torus, choose a Euclidean chart/ball strictly smaller than the injectivity radius. The preterminal smooth solution restricted to that chart is an interior suitable weak solution: it satisfies the equations distributionally and the local energy equality, hence the local energy inequality. The periodic problem has no physical boundary at `x*`.

A constant viscosity `nu>0` may be normalized to viscosity one by the standard change `u=nu v`, `tau=nu t`, `p=nu^2 q`; singular/regular status and the local blow-up structure are unchanged up to this deterministic rescaling.

Therefore, once R46 internally proves that a subsequential R45 work-linked center `(x_n,t_n)` converges to an actual singular point `(x*,T*)`, the **interior** parts of Albritton–Barker Theorems 1.1 and 1.2 apply locally.

## What is imported

Under the finite-time singularity hypothesis and after identifying an interior singular point `x*`, R46 may use the following consequences as literature-backed facts:

1. for every sufficiently small fixed chart radius `r>0`,

   `||u(t)||_{L^3(B_r(x*))} -> infinity` as `t -> T*_-`;

2. a non-trivial mild bounded ancient Navier–Stokes solution on `R^3` exists as a blow-up limit at that singularity.

## What is NOT imported

The source does not identify its blow-up normalization with any project-specific productive-work scale such as

- `R_theta` from R43;
- `Lambda_J` from R45/C003;
- the spatially local weighted-work scale introduced in R46;
- the R37 helical common-mode decomposition.

It therefore does **not** transfer the R37–R45 productive-work structure into the ancient solution automatically. That scale/alignment problem remains a new proof obligation and is guarded explicitly by RD024.

## Provenance discipline

This source note is a theorem-interface record, not a substitute for the paper. The repository does not claim originality for the imported singularity-to-ancient-solution result and does not count it as a proof of global regularity.
