# C001 — R10 inter-component flux obstruction is absent in the canonical zero-mean periodic frame

**Status:** `scope correction / R10 algebra retained, frontier narrowed by R21`  
**Affected:** R09, R10, RD005  
**Superseding theorem:** R21

R10 correctly decomposed the regular-level pressure work into

`I(s)=C_inter(s)+C_intra(s)`,

with

`C_inter(s)=sum_a pbar_a(s) J_a(s)`

and

`C_intra(s)=sum_a integral_{Sigma_{s,a}} (p-pbar_a)u·n_rho dS`.

However, R10 treated `C_inter` as a potentially load-bearing obstruction because it used only the total cancellation `sum_a J_a=0`.

R21 proves that after the explicit Galilean reduction to the zero-mean periodic frame, the velocity has a smooth periodic vector potential `u=curl A`. Surface Stokes then gives

`J_a(s)=0`

for every connected component of every regular positive iso-speed level. Therefore

> `C_inter(s)=0`

identically in the canonical frame.

## What is corrected

The following R10 interpretation is no longer canonical for this project:

> disconnected regular iso-speed components may sustain critical pressure work solely through different component pressure means multiplied by compensating nonzero component fluxes.

That mechanism is possible in a nonzero-mean frame but disappears after the regularity-equivalent Galilean zero-mean normalization.

R10's algebraic decomposition itself remains correct and useful as an audit identity.

## What is not corrected

RD005's principal no-go remains valid: arbitrary smooth divergence-free shears can have extremely complicated iso-speed geometry, including poor surface Poincare constants and many components. R21 does not give uniform geometric control.

The surviving pressure obstruction is the intra-component term and the treatment of critical speed values. In particular, a future proof must still justify any surface/quotient Poincare estimate with constants compatible with critical scaling and coarea/time integration.

## Frame discipline

Clay statement (B) permits nonzero mean periodic data. The reduction to zero mean is made by the exact Galilean transform

`v(x,t)=u(x+m t,t)-m`, `m=mean(u_0)`.

Regularity is invariant under this transform, but the speed `|u|` is not. Consequently all speed-based R01–R10 diagnostics used after C001 must be evaluated consistently in the normalized field `v`.

No argument may compute an iso-speed quantity in one Galilean frame and then invoke R21 in another.

## Nonzero-mean falsifier retained

The exact smooth solution

`u=(exp(-nu t)sin(y-a t),a,0)`

has nonzero component flux across its regular iso-speed coordinate tori. This witness is retained in R21/checker to make the scope boundary machine-auditable.

**C001 does not solve the gradient branch or the Navier–Stokes Millennium problem.** It removes one incorrectly retained sub-obstruction and makes the remaining proof obligation sharper.
