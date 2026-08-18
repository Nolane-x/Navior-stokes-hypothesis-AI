# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World at depth W5.

## Status

**NOT SOLVED.** This repository contains verified partial structural theorems, route guards/no-gos, primary-source theorem interfaces, independent reconstructions and reproducible certificates. None is a Clay solution.

Primary target: Clay statement **(B)** — global existence and smoothness on `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current checkpoint — W5-E46

Canonical ledger:

> `checkpoints/W5-E46-SEMANTIC-LEDGER.md`

Canonical aggregate verification:

```text
workflow run: 32094820170
verified_head: 961be1b878eacd69b81e72f495ea29c21dbc9fc7
verification_scripts=67
shards=8
W5_E46_FULL_SUITE=PASS
scope=PARTIAL_CERTIFICATES_ONLY_NOT_GLOBAL_REGULARITY
```

Specific R46 gate:

```text
workflow run: 32094667211
R46_PRIMARY_PASS checks=300095
R46_FRESH_GRID_PASS checks=220
RD024_PASS checks=1802
external_bridge=PRIMARY_SOURCE_SCOPE_PINNED_NOT_REPROVED_BY_SCRIPT
```

Fresh Nolane World 0.6 W5:

> `world5_20d12077702c0290f6e2`

The World gate **FAILED intentionally** with `critical_unknowns=1`; public-safe result:

> `verification/W5_E46_world_gate_result.json`.

World scores are research-governance diagnostics, not mathematical completion percentages.

## Proof spine — compressed

The project works in the canonical zero-mean Galilean frame. Let

```text
L=omega×u,
G=|u|u,
W_3=<QL,QG>=-<PL,PG>.
```

### R01–R25: isolate the physical endpoint obstruction

The early spine derives the exact critical `L^3` balance, removes several false coercivity routes, identifies the Lamb/pressure obstruction, and proves that any surviving endpoint mechanism must escape every fixed output Fourier cutoff. R20 proves that genuine high Lamb output requires actual high-frequency velocity input. R21–R25 clean pressure-level-set and transported-speed geometry and remove fixed-output pressure work as a blow-up mechanism.

### R26–R38: couple the Helmholtz channels and expose the common mode

R27 introduces balanced P/Q action; R28–R34 force productive work into shrinking ultraviolet terminal packets. R37 corrects the strategy from “make P/Q mismatch small” to “control the common productive mode” and derives exact helical pair geometry. Same-spin equal-shell interactions vanish and several near-degenerate pair sectors are depleted, but pairwise cancellation does not automatically sum in a many-body field. R38 synchronizes productive work across expanding cutoff hierarchies and signed shells.

### R39–R42: normalized spectrally high-dimensional bursts

R39 upgrades resolved P/Q synchronization to spacetime total variation. R40 proves resolved **absolute** work evacuates every prescribed growing finite catalog. R41 extracts actual-trajectory unit common-work bursts with shrinking duration and vanishing unweighted enstrophy cost. R42 proves that a fixed fraction of a unit productive burst requires an exploding number of output modes.

### R43–R45: productive frequency is squeezed from below and above

R43 gives intrinsic positive-work quantile radii `R_theta` with critical-homogeneous lower floors. R44 attaches a diverging velocity center to parent burst packets.

R45/C003 then proves the full signed common-work tail has an exact `1/R` upper scale. For a unit burst `J`, with integrated output coefficients `b_k(J)`, define

```text
Lambda_J=∫_J ||u(t)||_infinity^2 ||omega(t)||_2^2 dt.
```

Then

```text
T_J(R):=sum_(|k|>R)|b_k(J)| <= Lambda_J/R,
L0 <= Lambda_J,
R_theta <= Lambda_J/(1-theta).
```

Each unit burst therefore has its own diverging amplitude center. RD023 shows high-frequency tightness at this scale still does not imply non-collapse toward zero normalized frequency.

## R46 — spatially local work scale

E46 replaces the supremum-based tail control by a spatially local density.

For

```text
X(t)=∫_(T^3)|u|^2|grad u|^2 dx,
```

Parseval and the pointwise estimates

```text
|omega|^2 <= 2|grad u|^2,
|grad(|u|u)| <= 2|u||grad u|
```

give

```text
sum_(|k|>R)|c_k(t)| <= sqrt(2) X(t)/R.
```

Define

```text
Sigma_J=sqrt(2)∫_J∫_(T^3)|u|^2|grad u|^2 dxdt.
```

Then

```text
T_J(R)<=Sigma_J/R,
Sigma_J>=L0
```

on every unit common-work burst.

This forces a genuinely work-linked high-amplitude/gradient set. If

```text
a_J^2=L0/(2sqrt(2)q_J),
q_J=∫_J||omega||_2^2dt,
```

then the set `H_J={|u|>=a_J}` carries at least

```text
L0/(2sqrt(2))
```

of `∫|u|^2|grad u|^2`. Hence every terminal unit burst contains a work-linked point `(x_J,t_J)` with

```text
|u(x_J,t_J)| >= sqrt[L0/(2sqrt(2)q_J)] -> infinity.
```

Compactness of the torus gives a subsequence `x_J->x*`. A regular parabolic neighborhood of `(x*,T*)` would bound `u`, contradicting the selected points. Therefore `(x*,T*)` is an actual interior singular point under the finite-time singularity hypothesis.

## R46 primary-source bridge — the ancient object already exists if a singularity exists

The source interface is pinned in

> `sources/R46_albritton_barker_interior_singularity_ancient_bridge.md`.

Albritton–Barker, arXiv:1811.00507v2, proves for the relevant interior suitable-solution setting that:

- the local `L^3` norm diverges in every fixed neighborhood of an interior singular point (Theorem 1.1);
- an interior singularity generates a non-trivial mild bounded ancient Navier–Stokes solution on `R^3` as a blow-up limit (Theorem 1.2).

The periodic smooth preterminal solution restricted to a small Euclidean chart around `x*` fits the interior suitable-solution interface; positive constant viscosity is normalized deterministically.

**This repository does not claim to reprove those theorems.** The external result changes the internal frontier: existence of *some* non-trivial ancient blow-up object is no longer treated as the missing theorem once the R46 singular point is identified.

## RD024 — the decisive gap is transfer/alignment

Existence of an ancient object does not imply that the project-specific productive modes survive its normalization.

Define the dimensionless ratio

```text
Chi_theta=R_theta/A_J.
```

RD024 constructs two abstract scalar families compatible with the current R43–R46 envelopes, one with

```text
Chi_theta -> 0
```

and one with

```text
Chi_theta -> infinity.
```

These are not Navier–Stokes trajectories. They are route guards showing that a genuine PDE theorem is needed to align productive Fourier scales with an amplitude/ancient blow-up scale.

## Exact live frontier after E46

A hypothetical finite-time singularity must now support two lineages simultaneously.

**Productive-work lineage:**

- unit common high-pass work;
- synchronized Helmholtz representations;
- resolved absolute-work evacuation;
- exploding productive output multiplicity;
- R37 helical pair restrictions;
- R43 lower productive radius;
- R45 signed-work upper frequency;
- R46 spatially local amplitude-weighted gradient mass.

**Singularity lineage:**

- a work-linked center subsequence reaches a genuine singular point;
- local `L^3` diverges around that point by the imported theorem;
- a non-trivial mild bounded ancient blow-up solution exists by the imported theorem.

The remaining load-bearing theorem must **connect these lineages**. The highest-value routes are:

1. prove `R_theta`, `Sigma_J`/`Lambda_J` and an amplitude/ancient blow-up scale remain comparable on a subsequence;
2. prove a fixed positive fraction of unit common work and R37 helical structure survives an appropriate PDE-compact rescaling;
3. derive a Liouville/backward-uniqueness/Oseen contradiction for the transferred structured ancient solution;
4. bypass the limit with a many-body depletion theorem.

Another finite-catalog synchronization estimate or energy-only scaling argument would not materially change the project.

## Verification and governance

Canonical records:

```text
verification/R46_gate_result.txt
verification/W5_E46_full_suite_result.txt
verification/W5_E46_world_gate_result.json
checkpoints/W5-E46-SEMANTIC-LEDGER.md
```

The protocol is:

```text
candidate
→ exact domain/scope
→ adversarial falsifier
→ independent reconstruction
→ source-interface audit when importing literature
→ repository-wide replay
→ Nolane World nonconvergence/convergence gate
→ public-safe package
```

No certificate, World score, finite computation, imported partial theorem, or ancient-solution existence theorem is interpreted as a proof of global regularity.

## Current conclusion

**W5-E46 is a verified partial checkpoint, not a solution.** The program has moved from a vague ultraviolet pressure obstruction to a work-linked spatial singular point plus an established ancient blow-up object. The remaining problem is no longer “find an object to compactify”; it is to **transfer the productive common-work/helical architecture into a PDE-compact ancient limit and rule that structured limit out**, or prove the bursts impossible before taking a limit.
