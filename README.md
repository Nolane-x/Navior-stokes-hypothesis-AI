# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World 0.5.0 at depth W5.

## Status

**NOT SOLVED.** The repository contains verified structural reductions, exact counterexamples/no-gos, independent challengers and reproducible checkers. None is a Clay solution.

Primary target: Clay statement **(B)** — global existence and smoothness on the periodic domain `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current checkpoint

Latest canonical semantic checkpoint: `checkpoints/W5-E28-SEMANTIC-LEDGER.md`.

Historical E23 provenance remains frozen under the original research world `world4_05c73a9403ba4574`, whose final E23 governance gate was `FAILED / NONCONVERGED` with internal score `0.8333333333333334` and one material mathematical unknown still open.

The live E24–E28 work was reconstructed in a **fresh** W5 continuation world `world_e3fcf95bd269` because the old runtime database was not present in the execution filesystem. Its gate score is intentionally **not compared numerically** with E23. The continuation gate remains failed and retains `critical_unknowns=1`.

The repository-wide E28 Python verification gate passed at GitHub Actions run `32031960379`. The current E28 verification directory contains 32 Python certificates/fresh verifiers, all covered by that aggregate workflow.

Internal World/gate scores are research-governance diagnostics, **not percentages of the Millennium problem solved**.

## Canonical frame

Clay statement (B) permits periodic data with nonzero mean. For zero forcing the spatial mean `m` is conserved, and the exact Galilean transform

```text
v(x,t) = u(x + m t,t) - m
```

reduces the regularity problem to a zero-mean periodic field. Because speed-based diagnostics are not Galilean invariant, all amplitude/iso-speed quantities in the current proof spine are frozen in this canonical zero-mean frame. R21/C001 record the theorem and the frame-sensitive falsifier.

## Strongest verified proof spine

### 1. Critical `L^3` / physical Lamb reduction

R01–R08 derive the critical `L^3` balance and identify a scale-invariant pressure/Lamb obstruction. R18 removes the sharp-cutoff representation hazard: divergence of the R08 tail action forces divergence of the **untruncated physical Lamb action**

```text
A_L(T) = ∫ ||u||_(3/2) ||ω×u||_2^2 dt
```

and forces it through arbitrarily high physical Fourier outputs. R20 proves that physical Lamb output above `K` cannot be produced when both velocity/vorticity inputs are confined below `K/2`.

### 2. Helmholtz physical channels

With `L=ω×u`, R19 splits

```text
L = P L + Q L,
A_sol  = ∫ U ||P L||_2^2 dt,
A_grad = ∫ U ||Q L||_2^2 dt,
U = ||u||_(3/2).
```

`P L` is the divergence-free dynamical channel; `Q L=-∇(p+|u|^2/2)` is the Bernoulli-gradient channel. R14–R17 expose helical conflict, spectral bandwidth and exact bandwidth-variance evolution. RD009 proves viscosity does not make that variance statewise monotone; RD011 proves neither physical channel universally dominates the other.

### 3. Branch-G representation was sharpened

R22–R23 give

```text
Q(|u|u) = Q[(curl^{-1}u)×∇|u|] = [Q,|u|]u.
```

R24 identifies the scalar actually seen by this projector. With `rho=|u|`, `e=u/rho` on `{rho>0}`, and `S=sym ∇u`,

```text
q_amp = div(rho u)
      = u·∇rho
      = u^T S u / rho
      = rho e^T S e
      = -rho^2 div e,
Q(rho u) = ∇Δ^{-1} q_amp.
```

Thus the pressure-test defect sees **transported speed / longitudinal strain**, not raw Fourier complexity of `|u|`.

RD013 makes the distinction exact: the smooth low-frequency field

```text
u=(2 cos z, sin z, 0)
```

has infinitely many Fourier harmonics in `|u|`, yet `Q(|u|u)=0`. Raw amplitude UV is therefore not physical Branch-G UV.

### 4. Fixed output is harmless

R25 proves that for every fixed Fourier cutoff `K`, with `N_K=#{0<|k|<=K}`,

```text
||P_<=K Q(|u|u)||_2 <= sqrt(N_K)||u||_2^2,
||P_<=K Q(ω×u)||_2 <= sqrt(N_K)||ω||_2||u||_2,
```

so the corresponding low-output pressure work is absolutely time-integrable on every finite smooth interval by the energy inequality.

Therefore any nonintegrable Branch-G pressure mechanism must escape every fixed output cutoff.

### 5. R26–R27 couple the two physical channels

R26 proves a complementary solenoidal critical-action criterion: finiteness of

```text
A_sol = ∫ U ||P(ω×u)||_2^2 dt
```

controls the same endpoint `L^3` barrier that R06 controls through `A_grad`.

R27 sharpens this by removing the irrelevant test-field mean and proving a homogeneous estimate. Define the **balanced minimum action**

```text
A_bal(T)
  = ∫ U(t)
      min(||P(ω×u)||_2^2, ||Q(ω×u)||_2^2) dt.
```

Then, for a torus constant `C_*`,

```text
||u(T)||_3^3 + (3ν/2)∫_0^T D_3 dt
  <= ||u(0)||_3^3 + 3 C_* A_bal(T).
```

Hence finite `A_bal` controls the endpoint `L^3` barrier. Within the corresponding periodic/localized endpoint continuation framework, a finite-time singularity must force

```text
A_bal(T*) = infinity.
```

This is stronger than saying merely that both individual channel actions diverge: even the **weaker channel at each time** must accumulate non-summable critical action.

C002 records that R19's original `S or G` dichotomy remains mathematically true but is no longer the sharp canonical frontier.

### 6. Global channel balance is not shell balance

RD014 gives an exact real divergence-free three-mode finite-Fourier field for which the global solenoidal fraction is about `25.83%`, while the natural shell-overlap functional is only about `2.17%` of the weaker global channel energy.

Therefore R27 cannot be promoted into a same-shell P/Q synchronization theorem. Scale synchronization requires genuinely new dynamics.

### 7. R28 switches to productive pressure-work UV

R28 uses both exact pressure-work representations

```text
W_3 = <Q L,Q(|u|u)>
    = -<P L,P(|u|u)>.
```

For every fixed output cutoff, the low-frequency piece of **both** representations is absolutely time-integrable. If the endpoint `L^3` quantity diverges, R01 forces cumulative signed pressure work to tend to `+infinity`. Therefore for every fixed `K`, both exact representations must satisfy

```text
∫ W_grad,>K dt -> +infinity,
∫ W_sol,>K  dt -> +infinity.
```

Equivalently, each representation must contain an ultraviolet sequence of **productive positive pressure-work shells**. RD014 still allows the two productive sequences to live at different scales/times.

## Current missing theorem

The frontier is no longer simply “control S” and “control G” independently.

A positive proof through this program must now rule out, or a priori bound, an arbitrary-data trajectory that simultaneously has:

1. divergent scale-critical balanced action `A_bal`;
2. productive high-output pressure work above every fixed cutoff in both exact Helmholtz representations;
3. possible spectral separation between the two representations, as permitted by RD014.

The sharp research question is therefore:

> **Can actual Navier–Stokes dynamics sustain a non-summable balanced/productive ultraviolet cascade while keeping the two Helmholtz representations separated in scale/time, or does triad geometry, helical structure, commutator structure, dissipation, or concentration rigidity force a contradiction / known continuation criterion?**

No arbitrary-data a-priori estimate answering this question is currently proved. This is why the project remains `NONCONVERGED_PARTIALS_ONLY` and **NOT SOLVED**.

## Independent verification and adversarial evidence

Recent verified gates include:

- R24/RD013: run `32029607416`;
- R25: run `32029668632`;
- R26: run `32030235082`;
- R27 exact criterion: run `32030583668`;
- R27 fresh physical-grid reconstruction: run `32030790881`;
- RD014 exact shell-separation no-go: run `32031474432`;
- R28 dual productive-UV theorem: run `32031706755`;
- full E28 Python-certificate gate: run `32031960379`.

The fresh R27 verifier reconstructs the load-bearing identities independently in physical/Fourier grid form rather than importing the exact rational checker.

## Research integrity

The repository follows `docs/research_protocol.md`. In particular:

- finite Fourier computation never implies the continuum PDE theorem;
- a regularity criterion is not a proof until its hypothesis is derived a priori;
- energy/enstrophy alone is not promoted into critical control;
- negative results and corrections remain first-class artifacts;
- speed-based arguments may not switch Galilean frames silently;
- every load-bearing claim declares its verification scope;
- internal World scores are never presented as percentages of the Millennium problem solved.

## Primary-source interfaces

- Clay/Fefferman official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- T. Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*: https://arxiv.org/abs/1402.0290
- A. Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*: https://arxiv.org/abs/0705.2446
- J. Lerner, N. Vigneron, *On some properties of the curl operator and their consequences for the Navier-Stokes system*: https://arxiv.org/abs/2203.07950
- Z. Grujic, Z. Bradshaw, *Frequency localized regularity criteria for the 3D Navier-Stokes equations*: https://arxiv.org/abs/1501.01043
- A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*: https://arxiv.org/abs/1507.06611

## Repository layout

```text
docs/          protocols, problem certificates, dependency maps
research/      verified partial theorems, challengers and structural reductions
corrections/   explicit scope/frontier corrections
discarded/     falsified routes and exact obstructions
experiments/   preregistered or frozen computational experiments
verification/  exact/symbolic/independent reproduction checkers
world/         public-safe Nolane World summaries and gates
checkpoints/   milestone semantic ledgers
```

The project advances only when a result survives its declared verification scope.
