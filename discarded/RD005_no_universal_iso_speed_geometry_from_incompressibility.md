# RD005 — Incompressibility does not provide universal nice geometry of iso-speed surfaces

**Status:** `exact structural no-go`  
**Depends on:** R09  
**Kills:** any R09 continuation that assumes a universal bound on iso-speed component count, curvature, connectivity, or Poincare constants solely from smoothness + incompressibility  
**Does not kill:** estimates coupling level geometry to the actual pressure/Lamb field or to dynamically selected high-amplitude regions

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

This is crucial: **bad iso-speed geometry alone is not the dangerous mechanism.** Any successful R09 theorem must control a joint quantity measuring how pressure/Lamb structure correlates with the amplitude-level flux.

## Component-flux warning

At a regular speed `s`, R09 gives only the total level-flux cancellation

`sum_a J_a(s)=0`,

where the sum ranges over connected components and

`J_a(s)=∫_{Sigma_{s,a}} u·n_rho dS`.

If the level is disconnected, pressure may have different component means. A proof that controls only tangential pressure oscillation **within** each component can still miss an inter-component term

`sum_a pbar_a(s) J_a(s)`.

Therefore a fiberwise Poincare argument must either prove the relevant component fluxes vanish separately, or control the inter-component pressure offsets and flux covariance. This obligation cannot be omitted.

## Research consequence

The naive continuation

`R09 -> uniformly nice iso-speed surfaces -> uniform surface Poincare -> pressure bound`

is discarded.

Surviving R09 strategies must be pressure-aware, for example:

1. use conditional expectation directly, avoiding explicit topology;
2. estimate pressure oscillation with a measure/Dirichlet form that remains meaningful under disconnected fibers;
3. build a graph of level components with pressure offsets and fluxes and control the graph term;
4. restrict to the R08 high-amplitude tail and prove **joint** geometric/pressure structure there from the actual nonlinearity;
5. derive a nonlocal quotient-space estimate for `p modulo functions(|u|)` that bypasses surface Poincare constants entirely.

RD005 prevents a hidden regularity assumption from entering the iso-speed route.
