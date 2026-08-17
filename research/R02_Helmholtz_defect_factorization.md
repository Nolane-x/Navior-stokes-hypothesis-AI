# R02 — Helmholtz-defect factorization of critical `L^3` pressure work

**Status:** `exact structural reduction / not claimed novel`  
**Depends on:** R01  
**Clay status:** not a global proof

R01 isolates the critical `L^3` obstruction

`W_3(u,p)=∫ p u·∇|u|`.

R02 rewrites this term without treating pressure as an opaque scalar.

Let `P` be the `L^2` Leray projector onto periodic divergence-free vector fields and `Q=I-P` the gradient Helmholtz projector. Define

`N(u)=(u·∇)u`,

`G(u)=|u|u`.

For a smooth divergence-free field, pressure satisfies

`Q N(u) = -∇p`.

Because `Q` is an orthogonal self-adjoint projector,

`W_3(u,p) = -<∇p,G(u)>`

`           = <Q N(u), G(u)>`

`           = <Q N(u), Q G(u)>`.

Thus

> `W_3 = < Q[(u·∇)u], Q[|u|u] >_{L^2}`.

The entire sign-indefinite pressure contribution is the correlation of two **longitudinal defects**:

1. the longitudinal part removed from the quadratic transport by incompressibility;
2. the longitudinal part of the nonlinear `L^3` test field `|u|u`.

## Potential form

Since `div u=0`,

`div G(u) = div(|u|u) = u·∇|u|`.

On zero-mean scalar fields, write

`Qv = ∇Δ^{-1} div v`.

Then

`Q N = -∇p`,

`Q G = ∇Δ^{-1}(u·∇|u|)`.

Therefore `W_3` is equivalently an `H^{-1}`-type correlation of the pressure source and the streamline-amplitude source.

## Defect coherence

When both defects are nonzero, define

`κ(u) = W_3 / ( ||Q N||_2 ||Q G||_2 )`.

Then exactly

`|κ(u)| <= 1`

by Cauchy-Schwarz, and R01 becomes

`(1/3)d/dt ||u||_3^3 + νD_3`

`= κ ||Q[(u·∇)u]||_2 ||Q[|u|u]||_2`.

This separates H1 into three possible mechanisms:

- **angle depletion:** `κ` becomes small/negative near concentration;
- **transport-defect depletion:** the longitudinal part of true nonlinear transport is smaller than generic bilinear estimates predict;
- **test-defect depletion:** the amplitude-direction geometry makes `Q(|u|u)` small compared with the R01 diffusion.

RD001 proves that no argument may replace all three by one universal constant times `D_3`: amplitude scaling defeats that shortcut.

## Why this representation is useful

Tao's averaged-equation blow-up result warns that energy cancellation and generic bilinear estimates are insufficient. R02 exposes quantities tied directly to the exact Leray/pressure structure of the true equation. A viable next theorem must show a concentration-scale restriction on at least one of the three factors above **along actual Navier–Stokes trajectories**, not for arbitrary states.

## Verification

The factorization uses only:

- pressure Poisson / Leray decomposition;
- self-adjoint orthogonal projection `Q`;
- the R01 integration-by-parts identity.

A future numerical experiment may estimate `κ` for finite Fourier fields, but such measurements cannot certify a continuum bound.
