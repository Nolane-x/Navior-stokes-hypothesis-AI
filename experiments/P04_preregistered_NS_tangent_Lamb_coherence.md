# P04 — Preregistered Navier–Stokes tangent test of dangerous Lamb coherence

**Status:** `preregistered trajectory challenger`  
**Depends on:** R03, P03, RD002  
**Clay status:** finite-dimensional numerical trajectory diagnostic only

P03 proved that a static divergence-free Fourier state can have projected Lamb-defect coherence

`kappa_L > 1/2`.

The surviving hypothesis after RD002 is not a universal statewise angle gap, but a **trajectory-dependent depletion**: perhaps the true Navier–Stokes vector field repels states from dangerous positive Lamb/amplitude-defect alignment.

P04 attacks the simplest local version of that claim.

## Frozen initial shape

Use exactly the committed P03 52-coefficient winner from

`verification/P03_expanded_Lamb_coherence_result.json`.

Let `v` denote that normalized divergence-free trigonometric field and form

`u_a = a v`

for amplitudes

`a in {0.5, 1, 2, 4, 8}`.

Fix viscosity `nu=1` on the unit torus.

## Frozen true-NS tangent

At each `u_a`, compute

`F_NS(u_a) = Delta u_a - P[(u_a·grad)u_a]`

using spectral derivatives and the exact Fourier Leray projector on an `N=48` grid.

The diagnostic is the directional derivative

`d_NS kappa_L(u_a) = d/dt kappa_L(u_a + t F_NS(u_a)) |_{t=0}`.

This is a tangent test, not a long-time Galerkin trajectory.

## Frozen numerical derivative

Let

`h0 = 2e-5 * ||u_a||_2 / ||F_NS(u_a)||_2`.

Use the symmetric derivative

`D(h)=[kappa_L(u_a+h F_NS)-kappa_L(u_a-h F_NS)]/(2h)`

at

`h in {h0/2, h0, 2h0}`.

Accept the sign only if all three derivatives have the same strict sign and the relative spread

`(max D - min D)/max(1,|mean D|)`

is `<5e-3`.

Independently replay the accepted sign on `N=64` with the same dimensionless step rule.

## Frozen hypotheses

- **H-repel:** every amplitude in `{0.5,1,2,4,8}` has a robust strictly negative `d_NS kappa_L` at both N=48 and N=64.
- **H-nonrepel:** at least one amplitude has a robust nonnegative derivative (strictly positive under the sign gate, or zero within numerical resolution).
- **INCONCLUSIVE:** derivative signs fail the frozen step/resolution stability gate.

Interpretation is one-way:

- `H-nonrepel` falsifies the simple local claim that true Navier–Stokes dynamics universally decreases `kappa_L` near this dangerous static state across Reynolds/amplitude scaling;
- `H-repel` does **not** prove trajectory depletion globally, because it concerns one initial shape and five amplitudes.

## Required outputs

For every amplitude and both resolutions record:

- initial `kappa_L`;
- `||u||_2`, `||F_NS||_2`, and `h0`;
- the three symmetric derivatives;
- mean derivative and spread;
- sign-stability verdict.

Also record the implementation SHA-256 and the final verdict.

No amplitude set, viscosity, initial shape, derivative stencil, threshold, resolution, or verdict rule may change after the first primary measurement begins without a new experiment ID.
