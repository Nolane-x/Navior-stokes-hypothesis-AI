# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the periodic 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World at depth W5.

## Status

**NOT SOLVED.** This repository contains verified partial structural theorems, explicit route guards/no-gos, primary-source theorem interfaces, independent reconstructions and reproducible certificates. None is a Clay solution.

Primary target: Clay statement **(B)** — global existence and smoothness on `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current checkpoint — W5-E48

Canonical semantic ledger:

> `checkpoints/W5-E48-SEMANTIC-LEDGER.md`

Final repository-wide verification:

```text
workflow run: 32100503157
verified_head: be7ed7c80a78ac270558445580ed6d7bee9c3dae
verification_scripts=74
shards=8
shard_counts=10,10,9,9,9,9,9,9
W5_E48_FULL_SUITE=PASS
scope=PARTIAL_CERTIFICATES_ONLY_NOT_GLOBAL_REGULARITY
```

Dedicated gates:

```text
R47 run: 32099072580
R47_PRIMARY_PASS checks=309094
R47_FRESH_PASS checks=231340
RD025_PASS checks=30302

R48/C004 run: 32100395344
R48_PRIMARY_PASS checks=1390000
R48_FRESH_PASS checks=130000
RD026_PASS checks=119928
```

RD027 adds an independent smooth divergence-free spatial-fragmentation route guard and is included in the final 74-certificate aggregate.

Fresh Nolane World 0.6 W5:

> `world4_cabfca04208f494d`

Its final public-safe gate is

> `verification/W5_E48_world_gate_result.json`.

The gate **FAILED** with `critical_unknowns=1`; no unknown, active-residency field or value-of-thought field was manipulated to force convergence. World scores are research-governance diagnostics, not percentages of the Millennium Problem solved.

## Proof spine — compressed

Work in the canonical zero-mean Galilean frame and set

```text
L=omega×u,
G=|u|u,
W_3=<QL,QG>=-<PL,PG>.
```

### R01–R25 — isolate the physical endpoint obstruction

The early spine derives the exact critical `L^3` balance, falsifies several coercive shortcuts, identifies the Lamb/pressure obstruction and proves that any surviving endpoint mechanism must escape every fixed output Fourier cutoff. R20 forces genuine high-frequency velocity input behind physical Lamb UV. R21–R25 clean the pressure/transported-speed representation and eliminate fixed-output pressure work as the terminal mechanism.

### R26–R38 — balanced Helmholtz common mode and helical geometry

R27 couples the solenoidal and Bernoulli channels through a balanced action. R28–R34 force productive work into shrinking ultraviolet terminal packets. R37 identifies the common productive mode and derives exact helical P/Q pair geometry; same-spin equal-shell interactions vanish and several near-degenerate sectors are depleted. R38 synchronizes cumulative and signed-shell pressure work across an expanding cutoff hierarchy. Pairwise depletion still does not automatically sum through a many-body nonlinear field.

### R39–R46 — unit bursts, intrinsic scales and a singular-point/ancient bridge

R39 upgrades resolved synchronization to spacetime total variation. R40 proves resolved absolute work evacuates every prescribed growing finite catalog. R41 extracts actual-trajectory unit common-work bursts; R42 forces productive-mode multiplicity to diverge. R43 supplies intrinsic positive-work quantile radii; R45/C003 gives an absolute `1/R` common-work tail. R46 replaces a supremum-only bound by the spatially local density

```text
X(t)=∫|u|^2|grad u|^2 dx,
Sigma_J=sqrt(2)∫_J X(t)dt,
T_J(R)<=Sigma_J/R.
```

R46 selects work-linked high-amplitude points converging to a genuine singular spatial point. A pinned primary-literature interface then supplies the standard interior-singularity / ancient-solution blow-up framework. The external theorem is cited, not reproved by project scripts.

## E48 advance

### R47 — last-exit unit bursts with a uniform critical PDE budget

R41 first-hit bursts can hide deep signed-work backtracking. R47 replaces them by last-exit / first-hit intervals. For every prefix of an R47 burst,

```text
0 <= ∫ C_L <= 1,
-eps <= ∫ W_3 <= 1+eps.
```

After fixing a terminal start time, terminal productive-work divergence permits the number of units `N` to be chosen larger than `||u(a)||_3^3`. The exact `L^3` balance and simultaneous Markov selection then produce a positive-density subfamily satisfying

```text
|J| -> 0,
q_J=∫_J||omega||_2^2dt -> 0,
∫_J D_3 dt <= 28/(3nu).
```

For

```text
Z=|u|^(1/2)u,
```

direct differentiation gives

```text
D_3 <= ||grad Z||_2^2 <= (9/8)D_3,
||Z||_6^2=||u||_9^3.
```

Hence these actual productive bursts have a uniform scale-critical `L^3_t L^9_x` bound. RD025 records the indispensable guard: a common `O(1)` critical bound per disjoint burst is not terminal summability or smallness.

### R48 — productive frequency cannot outrun a work-linked amplitude scale

On an R47-good burst define

```text
D_J=∫_J D_3dt,
X_J=∫_J∫|u|^2|grad u|^2dxdt,
Sigma_J=sqrt(2)X_J,
B_J=X_J/D_J.
```

Since `|u|^2|grad u|^2 <= |u| d_3`, `B_J<=sup|u|`. The set

```text
H_J={|u|>=B_J/2}
```

carries at least half of `X_J`.

For the R43 positive-work quantile radius `R_theta`, the R46 total-variation tail and R47 diffusion budget imply

```text
R_theta <= Sigma_J/(1-theta),
R_theta/B_J <= 28sqrt(2)/[3nu(1-theta)],
R_theta/sup|u| <= 28sqrt(2)/[3nu(1-theta)].
```

Thus the E46/RD024 branch `R_theta/sup|u| -> infinity` is eliminated on the R47-good subfamily.

At a work-linked center, rescaling directly at `r=1/R_theta` gives

```text
|v(0,0)| >= 3nu(1-theta)/(56sqrt(2)).
```

### C004 — nontriviality is measure-valued

R48 in fact yields

```text
X_J/R_theta >= (1-theta)/sqrt(2).
```

Therefore the productive-scale rescaling carries a fixed positive amount of the scale-invariant weighted-gradient measure

```text
∫|v|^2|grad v|^2 dyds,
```

and at least half of that lower bound lies on a set where the normalized velocity is bounded away from zero.

This is stronger than a single nonzero point, but it is still a **global** statement on an expanding rescaled torus.

### RD026 / RD027 — the two compactness gaps that remain

RD026 shows that all scalar constraints through R48/C004 permit both

```text
R_theta^2 |J| -> 0
```

and

```text
R_theta^2 |J| -> infinity.
```

So parabolic time alignment must come from genuine orbit dynamics.

RD027 constructs smooth divergence-free fragmented fields on expanding domains with fixed global weighted-gradient action, bounded `D_3` and a nonzero center, while every fixed ball captures vanishing weighted mass. Thus C004 global nontriviality is not local spatial tightness.

Neither RD026 nor RD027 is a Navier–Stokes blow-up construction. They are route guards against invalid compactness shortcuts.

## Canonical post-E48 frontier

The hypothetical singular mechanism has now been reduced to actual normalized bursts carrying simultaneously:

- exact unit productive common work with bounded prefix drawdown;
- vanishing duration and unweighted enstrophy cost;
- uniformly bounded critical `D_3` action;
- uniformly bounded critical `L^3_tL^9_x` action;
- one-sided productive-frequency/amplitude alignment;
- nonzero velocity at the productive scale;
- nonzero scale-invariant weighted-gradient mass on a nonzero-amplitude set;
- the earlier dual-channel synchronization and helical geometry.

The remaining load-bearing theorem is:

> **Use actual Navier–Stokes dynamics to prevent both RD026 temporal mismatch and RD027 spatial fragmentation / normalized-IR escape, obtaining local parabolic compactness that preserves a nonzero piece of productive common-work/helical structure, or derive a contradiction before taking a limit.**

Leading interfaces are Duhamel/heat propagation at the productive/work scale, local-energy propagation tied to the work density, concentration-compactness/rigidity, or a true many-body depletion theorem. Another scalar envelope alone is not enough.

## Scope

Every theorem and checker in this repository keeps an explicit scope statement. Finite-mode, symbolic, randomized and numerical certificates verify their declared identities, inequalities, countermodels or reconstructions only. **W5-E48 is a verified partial research checkpoint, not a proof of global regularity.**
