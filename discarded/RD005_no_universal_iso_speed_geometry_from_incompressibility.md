# RD005 — Incompressibility does not provide universal nice geometry of iso-speed surfaces

**Status:** `exact structural no-go; component-flux warning narrowed by R21/C001`  
**Depends on:** R09  
**Kills:** any R09 continuation that assumes a universal bound on iso-speed component count, curvature, connectivity, neck quality, or Poincare constants solely from smoothness + incompressibility  
**Does not kill:** estimates coupling level geometry to the actual pressure/Lamb field or to dynamically selected high-amplitude regions

> **Correction note.** RD005's main geometric no-go remains valid. Its original warning that disconnected components might carry nonzero compensating component fluxes is **not** a surviving obstruction in the canonical zero-mean Galilean frame: R21 proves `J_a(s)=0` for every regular component separately. What remains dangerous is bad component geometry together with within-component pressure oscillation.

R09 shows that critical pressure work depends only on pressure variation relative to velocity-amplitude classes. A natural next temptation is to control that variation by applying uniform Poincare/Sobolev inequalities on iso-speed level surfaces.

There is no universal geometric basis for such a step.

## Arbitrary smooth shear amplitudes

Let `f(y,z)` be **any** smooth periodic scalar on `T^2`, and define the three-dimensional shear field

`u(x,y,z) = ( f(y,z), 0, 0 )`.

Then

`div u = partial_x f = 0`,

and

`(u·grad)u = f partial_x u = 0`.

Thus with constant pressure, Navier–Stokes reduces exactly to

`partial_t f = nu (partial_yy + partial_zz) f`.

For every smooth initial `f`, this shear evolves by the two-dimensional heat equation and is globally smooth.

At the initial time its speed is simply

`rho(y,z)=|f(y,z)|`.

Therefore the iso-speed geometry of a perfectly smooth divergence-free Navier–Stokes state can inherit essentially arbitrary smooth scalar level-set complexity available in two variables.

## Consequences

By choosing `f` appropriately one can produce, with no loss of smoothness or incompressibility:

- arbitrarily many connected components of a regular speed level;
- arbitrarily high spatial frequency and curvature;
- pairs of large level-set regions connected by arbitrarily thin necks, causing surface Poincare constants to become arbitrarily poor;
- complicated topology changing across nearby amplitude levels;
- high-order nodal degeneracies at selected amplitudes.

No universal constant depending only on `nu`, total energy, or the fact `div u=0` can encode all of this instantaneous level-set geometry.

## Important pressure distinction

For these exact shears the nonlinear term vanishes and pressure may be chosen spatially constant. Consequently

`W_3=0`

regardless of how pathological the speed-level geometry is.

This is crucial: **bad iso-speed geometry alone is not the dangerous mechanism.** Any successful R09 theorem must control a joint quantity measuring how pressure/Lamb structure correlates with signed velocity crossing inside the amplitude levels.

## Component-flux warning — resolved in the canonical frame

The original RD005 version observed only the R09 total cancellation

`sum_a J_a(s)=0`

and warned that disconnected components might have nonzero `J_a` whose pressure-weighted covariance survives.

R21 closes exactly the escape clause already identified by that warning. After the regularity-equivalent Galilean reduction to zero spatial mean, the periodic divergence-free velocity has a global periodic vector potential `u=curl A`. For every closed regular component `Sigma_{s,a}`, surface Stokes gives

> `J_a(s)=integral_{Sigma_{s,a}}u·n_rho dS=0`.

Thus disconnectedness does **not** create an independent inter-component pressure-mean × flux obstruction in the canonical frame.

The frame qualification is essential: R21 retains an exact nonzero-mean travelling shear whose regular iso-speed tori do have nonzero individual flux. Speed-based diagnostics must therefore be defined after the Galilean normalization and kept in that frame.

## What RD005 still kills

The naive continuation

`R09 -> uniformly nice iso-speed surfaces -> uniform surface Poincare -> pressure bound`

remains discarded.

R21 removes the graph-of-component-means/fluxes branch, but the following obstructions survive fully:

1. surface Poincare constants may be arbitrarily poor;
2. connected components may be numerous and topologically complicated;
3. curvature and thin-neck degeneration may occur at high frequency;
4. critical speed values can invalidate naive regular-level formulas;
5. no geometry-only argument explains why tangential pressure/Lamb variation should be small on the dynamically dangerous high-amplitude levels.

## Research consequence after R21

Surviving R09 strategies should now focus on the **within-component** problem, for example:

1. use conditional expectation directly, avoiding explicit topology;
2. estimate pressure oscillation with a measure/Dirichlet form meaningful under degenerating fibers;
3. restrict to the R08 high-amplitude tail and prove joint geometric/pressure structure there from the actual nonlinearity;
4. derive a weighted surface Poincare estimate whose bad geometric factor is compensated by coarea weight or dissipation;
5. derive a nonlocal quotient-space estimate for `p modulo functions(|u|)` that bypasses surface Poincare constants entirely.

RD005 continues to prevent a hidden regularity assumption from entering the iso-speed route, while R21 removes one sub-obstruction that RD005 itself had left open.
