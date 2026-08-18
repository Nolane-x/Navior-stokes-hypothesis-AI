# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World at depth W5.

## Status

**NOT SOLVED.** This repository contains verified partial structural theorems, explicit route guards/no-gos, independent reconstructions, challengers and reproducible certificates. None is a Clay solution.

Primary target: Clay statement **(B)** — global existence and smoothness on `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current checkpoint — W5-E44

Canonical semantic ledger:

> `checkpoints/W5-E44-SEMANTIC-LEDGER.md`

Final E44 aggregate verification:

```text
workflow run: 32088968521
verified_head: 700928a4cd70492708d551d2f95cf98dcf62b0fe
verification_scripts=61
W5_E44_FULL_SUITE=PASS
scope=PARTIAL_CERTIFICATES_ONLY_NOT_GLOBAL_REGULARITY
```

Self-report:

> `verification/W5_E44_full_suite_result.txt`

E44 research runtime:

> Nolane World `0.6.0`, world `world4_07282ed4e1fb4049`, depth `W5`.

Its convergence gate **FAILED intentionally** with `critical_unknowns=1`. The public-safe gate is

> `verification/W5_E44_world_gate_result.json`.

World scores are research-governance diagnostics, **not percentages of the Millennium Problem solved**.

## Canonical frame

For zero forcing the spatial mean is conserved. The Galilean transform

```text
v(x,t)=u(x+mt,t)-m
```

reduces the periodic regularity problem to the canonical zero-mean frame. Speed-based diagnostics in the proof spine are frozen in this frame; R21/C001 record the theorem and frame-sensitive falsifier.

## Proof spine — condensed

Set

```text
L=omega×u,
G=|u|u,
U=||u||_(3/2).
```

The exact critical pressure-work identities are

```text
W_3=<QL,QG>=-<PL,PG>.
```

### R01–R25 — endpoint obstruction and physical UV

R01–R08 isolate the scale-critical `L^3` pressure/Lamb obstruction. R18 removes cutoff-generated UV contamination and proves that the surviving mechanism must escape through the physical untruncated Lamb force. R20 proves high Lamb output cannot come from two inputs both confined below half the output scale.

R21–R25 clean the pressure representation and identify transported speed / longitudinal strain:

```text
Q(|u|u)=[Q,|u|]u,
q_amp=div(|u|u)=u·grad|u|=u^T S u/|u|.
```

Every fixed finite output range contributes only integrable pressure work, so any surviving singular mechanism must be genuinely ultraviolet.

### R26–R38 — balanced common mode and helical geometry

R27 introduces the balanced action

```text
A_bal=∫ U min(||PL||_2^2,||QL||_2^2)dt.
```

A hypothetical singular endpoint must make even the weaker Helmholtz channel non-summable.

R28–R34 synchronize the two exact productive pressure-work representations and extract shrinking terminal packets.

R37 corrects an important strategic issue: small P/Q mismatch does not control their common productive mode. With `J=Q-P`,

```text
2C_H=<HL,JHG>.
```

R37 then derives exact helical pair factors and closed P/Q channel geometry. Same-spin equal-shell pairs vanish; near-equal same-spin interactions are radially depleted; narrow-shell opposite-spin near-collinear interactions are depleted in the solenoidal channel. Pairwise depletion still does not automatically sum through a many-body nonlinear minimum.

R38 synchronizes productive work across an expanding cutoff hierarchy and across every signed sharp shell in that hierarchy.

### R39–R42 — normalized high-dimensional unit bursts

R39 upgrades finite-catalog synchronization to spacetime total variation. R40 proves resolved **absolute** work evacuates every prescribed growing finite catalog.

R41 extracts consecutive first-hitting intervals `J_j` satisfying exactly

```text
∫_(J_j) C_L dt=1,
```

while good bursts have vanishing duration and vanishing unweighted enstrophy cost.

R42 proves a per-output-mode cap

```text
|b_k(J)|<=beta_J,
beta_J=V^-1 E0^3 sqrt(|J|q_J),
```

and therefore any fixed positive fraction of the unit productive work requires an exploding number of output modes. The hypothetical terminal mechanism is both frequency escaping and spectrally high-dimensional.

## E44 advance — intrinsic scale + spatial center

### R43 — intrinsic positive-work quantile scale

R43 uses one derivative of the exact test field `G=|u|u`:

```text
|grad G|<=2|u||grad u|,
||grad G||_1<=2E0||omega||_2.
```

Hence, for each nonzero mode,

```text
|Ghat(k)|<=2V^-1 E0||omega||_2/|k|,
|c_k(t)|<=V^-1 E0^2||omega||_2^2/|k|.
```

For a unit burst `J`,

```text
|b_k(J)|<=alpha_J/|k|,
alpha_J=V^-1 E0^2 q_J.
```

Define `R_theta(J,L)` as the smallest radius above the parent cutoff carrying at least `theta` units of positive common work. Lattice capacity gives two critical-homogeneous floors:

```text
R_theta >= [theta V/(27E0^3 sqrt(|J|q_J))]^(1/3),
R_theta >= [theta V/(26E0^2 q_J)]^(1/2).
```

Thus each good unit burst selects an **intrinsic productive spectral scale** tending to infinity.

### RD021 — scale floor is not parabolic compactness

RD021 constructs abstract coefficient distributions satisfying both R42/R43 caps with unit positive work but with

```text
R_theta^2 |J| -> 0
```

or

```text
R_theta^2 |J| -> infinity.
```

They are not Navier–Stokes trajectories. They reject the shortcut from mode envelopes to parabolic compactness.

### R44 — the same burst gets an amplitude center

Take a parent packet containing `N` consecutive R41 unit bursts. If `eta` bounds resolved mismatch total variation, `zeta` bounds resolved absolute work and

```text
q_I=∫_I||omega||_2^2dt,
A_K=sup_(x,t in T^3×K)|u(x,t)|,
```

then the exact `L^3` balance plus

```text
||u||_3^3<=A_K E0^2,
D_3<=2||u||_infinity||omega||_2^2
```

implies

```text
A_K >= 3(N-eta/2-zeta)/(E0^2+6nu q_I).
```

Along the terminal diagonal, `N->infinity` while `eta,zeta,q_I->0`, so `A_K->infinity`. Choose a maximizing point `(x_n,t_n)` and then the unit burst `J_n*` containing `t_n`.

That **same actual-trajectory unit burst** now carries simultaneously:

- exactly one normalized common productive-work unit;
- negligible resolved work;
- vanishing duration;
- vanishing enstrophy cost;
- a diverging velocity peak at a chosen spatial center;
- a diverging intrinsic R43 productive spectral scale.

This is the canonical E44 center-scale object.

### RD022 — peak center is not yet a local-energy atom

A smooth compactly supported divergence-free concentration family

```text
u_n(x)=A_n v((x-x_0)/r_n)
```

has

```text
||u_n||_infinity=A_n,
||u_n||_2^2=C0 A_n^2 r_n^3,
||grad u_n||_2^2=C1 A_n^2 r_n.
```

With `A_n=n`, `r_n=n^-1`, the peak diverges while the total/local kinetic energy is `O(n^-1)->0`. Assigning an abstract interval `ell_n=n^-2` also makes the integrated `H^1` cost `O(n^-1)->0`.

This is not a Navier–Stokes trajectory. It proves only that

> `large peak + short duration + small integrated enstrophy`

is insufficient, by itself, to produce a local-energy atom.

## Canonical E44 obstruction

A hypothetical singular trajectory compatible with the verified proof spine must now support normalized terminal bursts that are simultaneously

1. frequency escaping;
2. spectrally high-dimensional;
3. balanced across the Helmholtz channels;
4. compatible with R37 spin/radial/angular depletion;
5. of unit common productive work;
6. of vanishing duration and unweighted enstrophy cost;
7. equipped with a diverging intrinsic productive radius `R_theta`;
8. equipped with a diverging spatial amplitude peak `(x_n,t_n)`;
9. yet potentially lacking any local-energy atom or parabolic tightness.

The next load-bearing theorem must therefore be one of:

> **local-energy/parabolic tightness for the R44 center-scale bursts**, sufficient to extract a nontrivial critical/ancient Navier–Stokes object;

or

> **many-body geometric depletion**, using R37 helical geometry plus R42 multiplicity to rule out coherent unit productive bursts directly.

Another finite-catalog estimate, another mismatch estimate, or another generic Hölder/Bernstein bound is not enough.

## Independent interfaces

The repository keeps spatial/critical-element approaches as challengers rather than silently importing them. In particular, profile-decomposition/minimal-element methods become relevant only after the needed critical compactness hypotheses are actually obtained. The E44 route guards prevent treating `center + scale` as if compactness had already been proved.

## Verification and research integrity

Final E44 aggregate:

```text
workflow run: 32088968521
61/61 Python certificates PASS
verified theorem/checker head: 700928a4cd70492708d551d2f95cf98dcf62b0fe
```

World gate: `verification/W5_E44_world_gate_result.json` — **FAILED / NONCONVERGED_PARTIALS_ONLY**.

The repository follows `docs/research_protocol.md`. In particular:

- finite computation never implies the continuum PDE theorem;
- a regularity criterion is not a proof until its hypothesis is derived a priori;
- negative results and route guards remain first-class artifacts;
- pairwise helical cancellation is not promoted silently into a many-body bound;
- an intrinsic frequency scale is not confused with parabolic compactness;
- a velocity peak is not confused with an energy atom;
- internal World metrics are never presented as percentages of the Millennium Problem solved.

## Repository layout

```text
docs/          protocols, problem certificates, dependency maps
research/      verified partial theorems, challengers and structural reductions
corrections/   explicit scope/frontier corrections
discarded/     falsified routes and exact obstructions
experiments/   preregistered or frozen computational experiments
verification/  exact/symbolic/fresh-context reproduction certificates
checkpoints/   milestone semantic ledgers
```

The project advances only when a result survives its declared verification scope.
