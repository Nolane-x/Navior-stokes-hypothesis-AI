# NS00 — Frozen Problem Certificate and Rival Map

**Status:** `verified-scope / research bootstrap`  
**World:** `world4_05c73a9403ba4574`  
**Depth:** `W5`  
**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`

## Frozen theorem target

Prove Clay statement (B): for every smooth periodic divergence-free initial velocity `u_0` on `T^3 = R^3/Z^3`, viscosity `nu>0`, and zero forcing, the 3D incompressible Navier–Stokes equations possess a smooth periodic solution for all `t>=0`.

The official Fefferman statement explicitly permits any one of four alternatives (A)–(D). This program freezes (B) as the first target; a switch requires a recorded representation shift.

## Scaling

After normalizing viscosity, the Euclidean local scaling is

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`.

For `||u||_{L^q}`, the scaling exponent is `1-3/q`; hence `L^3` is critical. For spacetime Serrin norms `L^p_t L^q_x`, the critical relation is `2/p+3/q=1`.

## Known baseline constraints

1. Smooth arbitrary data have a local smooth solution; the unresolved step is excluding finite maximal time.
2. Global weak solutions exist, but known weak theory does not close global smoothness/uniqueness.
3. Partial regularity allows a small singular set; that is much weaker than proving the singular set empty.
4. Endpoint/critical regularity criteria show that control of certain critical quantities would prevent blow-up, but the missing step is deriving such control a priori from arbitrary smooth data.
5. Tao's averaged Navier–Stokes blow-up construction preserves the energy cancellation while blowing up, so a successful positive proof must exploit finer structure of the true nonlinearity rather than energy plus generic harmonic-analysis estimates alone.
6. Velocity-direction criteria show that incompressibility links streamline amplitude growth to `div(u/|u|)`, exposing a geometric variable that can be tested without assuming vorticity alignment.

## Critical unknown

The live bottleneck is:

> Find a scale-critical or concentration-defeating coercive mechanism that is dynamically enforced by the **true** incompressible Navier–Stokes nonlinearity for arbitrary smooth data.

A regularity criterion is not enough. The project must prove the criterion's hypothesis from the equations.

## Rival route map

### H1 — Critical velocity-amplitude / direction-pressure route

Start from the exact `L^3` entropy identity obtained by testing with `u|u|`. Decompose `u=rho n`, `rho=|u|`, `|n|=1`. Incompressibility gives

`n·grad rho = -rho div n`.

The pressure work in the `L^3` identity becomes a coupling between pressure, amplitude and direction divergence. Goal: find a true-NS coercive inequality that absorbs this term without a smallness assumption on `||u||_3`.

**Fast falsifier:** construct smooth divergence-free Fourier fields for which any proposed universal pressure-direction sign/coercivity inequality fails.

### H2 — Vorticity-strain depletion route

Use

`(1/2)d/dt ||omega||_2^2 + nu ||grad omega||_2^2 = integral omega·S omega`.

Goal: prove a dynamically forced depletion of vortex stretching at precisely the concentration scales needed to beat the supercritical enstrophy inequality.

**Fast falsifier:** finite Fourier fields maximizing stretching efficiency under incompressibility and fixed energy/enstrophy.

### H3 — True-triad anti-cascade barrier

Use helical/Fourier triads and the exact Leray-projected interaction coefficients. Tao's averaged model shows that generic energy cancellation is insufficient; therefore seek an algebraic constraint of genuine triads that forbids a self-similar energy cascade compatible with finite-time blow-up.

**Fast falsifier:** exhibit exact true-NS triad chains realizing the proposed cascade geometry.

### H4 — Minimal blow-up / ancient-solution Liouville route

Assume a first singularity, rescale around concentration, extract a minimal ancient solution, then prove a Liouville theorem using a new rigidity invariant.

**Fast falsifier:** identify a compactness step that only converges weakly where the nonlinearity requires strong convergence, or produce nontrivial ancient solutions satisfying the proposed invariant.

## Priority decision

Run H1 and H3 first.

- H1 directly attacks a critical norm and has an exact amplitude-direction identity already tied to a published regularity criterion.
- H3 is the necessary adversarial companion: it checks whether candidate estimates actually use true Navier–Stokes structure or only properties shared by Tao's averaged blow-up operator.
- H2 remains a secondary route because the standard enstrophy inequality is strongly supercritical.
- H4 is deferred until a genuinely new rigidity quantity exists; otherwise concentration compactness only repackages the same missing estimate.

## Primary sources

- C. Fefferman, official Clay problem description: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- A. Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*: https://arxiv.org/abs/0705.2446
- T. Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*: https://arxiv.org/abs/1402.0290

## Exit rule

NS00 certifies only the problem scope and research frontier. It proves no new regularity theorem and does not advance the Clay claim by itself.
