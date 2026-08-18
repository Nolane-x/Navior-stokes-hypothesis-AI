# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World at depth W5.

## Status

**NOT SOLVED.** This repository contains verified partial structural theorems, explicit route guards/no-gos, independent reconstructions, challengers and reproducible certificates. None is a Clay solution.

Primary target: Clay statement **(B)** — global existence and smoothness on `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current checkpoint — W5-E45

Canonical semantic ledger:

> `checkpoints/W5-E45-SEMANTIC-LEDGER.md`

Canonical E45 aggregate verification:

```text
workflow run: 32093839544
verified_head: 9e7cdc361030dc686be2575f31c02d72a128aa0d
verification_scripts=64
shards=8
scripts_per_shard=8
W5_E45_FULL_SUITE=PASS
scope=PARTIAL_CERTIFICATES_ONLY_NOT_GLOBAL_REGULARITY
```

Specific R45 gate:

```text
workflow run: 32093191615
R45_PRIMARY_PASS checks=145492
R45_FRESH_GRID_PASS checks=312
RD023_PASS checks=974
```

E45 research runtime:

> Nolane World `0.6.0`, world `world5_712c95ada64ec9f250d5`, depth `W5`.

Its convergence gate **FAILED intentionally** with `critical_unknowns=1`. The public-safe gate is

> `verification/W5_E45_world_gate_result.json`.

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

R37 derives exact helical pair factors and closed P/Q channel geometry. Same-spin equal-shell pairs vanish; near-equal same-spin interactions are radially depleted; narrow-shell opposite-spin near-collinear interactions are depleted in the solenoidal channel. Pairwise depletion still does not automatically sum through a many-body nonlinear minimum.

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

## E44 — lower productive scale + center

### R43 — intrinsic positive-work quantile radius

R43 uses one derivative of the exact test field `G=|u|u`:

```text
|grad G|<=2|u||grad u|,
||grad G||_1<=2E0||omega||_2.
```

For a unit burst `J`, the integrated common-work coefficients satisfy a `1/|k|` envelope. If `R_theta(J,L)` is the smallest radius above the parent cutoff carrying at least `theta` units of positive common work, R43 obtains critical-homogeneous lower floors including

```text
R_theta >= [theta V/(27E0^3 sqrt(|J|q_J))]^(1/3),
R_theta >= [theta V/(26E0^2 q_J)]^(1/2).
```

Thus every good unit burst selects a productive spectral scale tending to infinity.

RD021 proves these lower floors do not by themselves force parabolic scale-time comparability.

### R44 — parent-packet amplitude center

Using the exact `L^3` balance, R44 proves that parent packets containing many consecutive unit common-work bursts force a diverging velocity maximum. RD022 prevents the invalid shortcut from a large peak plus short time/small integrated enstrophy to a local kinetic-energy atom.

## E45 — exact signed-work upper scale

### R45/C003 — the full signed tail has an intrinsic `1/R` cap

For an R41 unit common-work burst `J`, define

```text
c_k(t)=(V/2) Re[Lhat(k)·conj((Q_k-P_k)Ghat(k))],
b_k(J)=∫_J c_k(t)dt,
sum_(|k|>L0)b_k(J)=1.
```

Parseval, Cauchy–Schwarz,

```text
|L|<=|u||omega|,
|grad G|<=2|u||grad u|,
||grad u||_2=||omega||_2
```

give the instantaneous total-variation tail

```text
sum_(|k|>R)|c_k(t)|
<= R^-1 ||u(t)||_infinity^2 ||omega(t)||_2^2.
```

C003 records the sharp integrated work scale

```text
Lambda_J=∫_J ||u(t)||_infinity^2 ||omega(t)||_2^2 dt,
Gamma_J=A_J^2 q_J,
```

with

```text
T_J(R):=sum_(|k|>R)|b_k(J)|
<= Lambda_J/R
<= Gamma_J/R.
```

Unit normalization immediately gives

```text
L0 <= Lambda_J <= Gamma_J,
A_J >= sqrt(L0/q_J).
```

So **every individual unit burst** carries its own diverging amplitude center; no many-burst parent is needed for this weaker but more local conclusion.

After frequency normalization by `Lambda_J`, the signed common-work measure satisfies

```text
|mu_J|({|xi|>r})<=1/r.
```

This is uniform high-frequency total-variation tightness of the **work measure**.

### R45 — first upper positive-work radius

For fixed `0<theta<1`,

```text
R_theta(J,L0) <= Lambda_J/(1-theta)
               <= Gamma_J/(1-theta).
```

R45 also uses the exact stress form

```text
L=div(u tensor u-(|u|^2/2)I)
```

to obtain a third lower floor

```text
R_theta >= [theta V/(27E0^4|J|)]^(1/4).
```

Combining the upper and lower scales yields quantitative amplitude/enstrophy constraints, including

```text
A_J >= sqrt(1-theta)(theta V/26)^(1/4)
       E0^(-1/2) q_J^(-3/4).
```

Thus a normalized productive burst with vanishing unweighted enstrophy cost pays a super-`q^-1/2` amplitude price.

### RD023 — high-tail tightness is not spectral non-collapse

RD023 constructs an abstract `n^3`-mode positive work cloud satisfying the R42/R43/R45 scalar envelopes and even the **sharp** tail inequality with

```text
Lambda_n=Gamma_n=n^p, p>1,
```

while all productive modes obey

```text
|k|/Lambda_n -> 0.
```

It is not a Navier–Stokes trajectory. It proves only that scalar work-measure envelopes cannot be promoted to annular spectral compactness without genuine PDE/orbit structure.

## Exact live frontier after E45

E45 separates three compactness problems that must not be conflated:

1. **spectral non-collapse** — control or exploit

   ```text
   Delta_theta^work=Lambda_J/R_theta;
   ```

2. **parabolic scale-time control** — relate burst duration to `R_theta` or `Lambda_J`;
3. **spatial/local-energy tightness** — align a spatial concentration object with the same productive burst/scale.

An alternative is to bypass compactness entirely by proving a **many-body depletion theorem** that upgrades R37 pairwise helical cancellation plus R42 multiplicity into a summable bound for the common productive mode.

The next theorem should attack one of those load-bearing bridges. Another finite-catalog synchronization estimate, generic Hölder estimate, or energy-only scaling argument would not materially change the project.

## Verification discipline

Canonical E45 full-suite result:

> `verification/W5_E45_full_suite_result.txt`

Specific R45 result:

> `verification/R45_gate_result.txt`

World nonconvergence record:

> `verification/W5_E45_world_gate_result.json`

No certificate, numerical experiment, World score, finite verification, or structural reduction is interpreted as a proof of global regularity.

## Research protocol

The repository uses a theorem ledger and falsification-first progression:

```text
candidate theorem
→ exact scope/domain
→ adversarial route guards
→ independent/fresh verifier where useful
→ repository-wide replay
→ Nolane World nonconvergence/convergence gate
→ public-safe checkpoint/package
```

Failures and counterexamples are retained rather than hidden, because a false shortcut removed is valuable only if future work cannot silently reintroduce it.

## Current conclusion

**W5-E45 is a verified partial checkpoint, not a solution.** The singularity-compatible object is now far more constrained than at the beginning of the program: an actual-trajectory, unit common-work, high-dimensional ultraviolet burst with vanishing duration/enstrophy cost, a diverging amplitude center, a lower productive radius, and an exact signed-work upper scale. The remaining gap is to turn that architecture into genuine PDE compactness/rigidity or many-body depletion.
