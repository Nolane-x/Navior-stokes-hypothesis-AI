# Navier–Stokes Hypothesis AI

A falsification-first, machine-auditable research program for the 3D incompressible Navier–Stokes Millennium Prize Problem, orchestrated with Nolane World 0.5.0 at depth W5.

## Status

**NOT SOLVED.** This repository must never promote a partial estimate, finite computation, heuristic cascade model, regularity criterion, or special-symmetry theorem into a Clay-solution claim.

Primary target: Clay statement **(B)** — global existence and smoothness on the periodic domain `R^3/Z^3` for every smooth divergence-free periodic initial velocity and zero forcing. Proving any one of Clay statements (A)–(D) is sufficient under the official problem description, but this project freezes (B) as the first target because periodic Fourier analysis and rigorous computation are cleaner.

Official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Current W5 research world

- Runtime: Nolane World `0.5.0` (Verified Distributed Cognition)
- Depth: `W5`
- World id: `world4_05c73a9403ba4574`
- Domain pack: `scientific-research`
- Initial colonies: first-principles, empirical, systems, adversary, challenger
- Closure rule: no `SOLVED` status without a complete proof chain, fresh independent verification, adversarial review, and a passing convergence gate.

## Core equation

On the 3-torus, with viscosity `nu>0` and zero forcing,

```text
∂_t u + (u·∇)u = nu Δu - ∇p,
∇·u = 0,
u(0)=u_0.
```

The proof target is global smoothness for arbitrary smooth periodic divergence-free `u_0`.

## Research strategy

The program separates four layers that are often incorrectly collapsed:

1. **Necessary blow-up geometry:** derive what any minimal singularity would have to look like under scaling, energy, pressure and vorticity transport.
2. **Critical obstruction:** identify the exact scale-critical quantity whose a priori control would rule out blow-up without assuming the desired conclusion.
3. **Mechanism-specific inequality:** exploit structure of the true Leray-projected nonlinearity, not merely the energy identity or generic bilinear estimates.
4. **Closure:** prove the critical quantity cannot diverge, then bootstrap to global smoothness with every compactness/limit step explicit.

Negative results are first-class artifacts. A route killed by a counterexample is retained under `discarded/` rather than silently removed.

## Research integrity

The repository follows `docs/research_protocol.md`. In particular:

- finite Fourier truncations never imply the PDE theorem by themselves;
- numerical non-blow-up never implies global regularity;
- energy conservation/dissipation alone is insufficient;
- any estimate that is supercritical at the Navier–Stokes scaling is presumed incapable of closing the Millennium problem unless paired with a new mechanism;
- a conditional regularity criterion is not a proof until its hypothesis is derived a priori for arbitrary smooth data;
- all claimed new lemmas require either an exact proof or a reproducible rigorous certificate.

## External baselines

The official Clay problem description records local smooth existence, global weak solutions, and partial regularity while leaving the 3D global smoothness question open. Terence Tao's averaged-equation blow-up construction shows that energy cancellation plus generic harmonic-analysis control is not enough; a positive proof must use finer structure of the actual Navier–Stokes nonlinearity.

Primary sources:

- Clay/Fefferman official problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- T. Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*: https://arxiv.org/abs/1402.0290

## Repository layout

```text
docs/          protocols, problem certificates, dependency maps
research/      verified partial theorems and structural reductions
discarded/     falsified routes and exact obstructions
experiments/   preregistered computational experiments
verification/  exact/symbolic/interval/reproduction checkers
world/         public-safe Nolane World state summaries and gates
checkpoints/   milestone ledgers
```

The project advances only when a result survives its declared verification scope.
