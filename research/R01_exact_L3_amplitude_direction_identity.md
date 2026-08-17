# R01 — Exact critical `L^3` amplitude–direction identity

**Status:** `exact project lemma / not claimed novel`  
**Scope:** smooth periodic 3D incompressible Navier–Stokes while the solution is smooth  
**Clay status:** **not a global regularity proof**

We normalize to the unit torus `T^3=(R/Z)^3` and write

`∂_t u + (u·∇)u = νΔu - ∇p`, `div u=0`.

Let `ρ=|u|`. Testing the equation against `ρu` gives the exact identity

`(1/3) d/dt ∫ ρ^3 + ν D_3(u) = W_3(u,p)`,

where

`D_3(u) = ∫ [ ρ |∇u|^2 + ρ^{-1} Σ_j (u·∂_j u)^2 ]`,

with the second integrand defined as zero on `{ρ=0}` by its continuous bound

`ρ^{-1}(u·∂_j u)^2 ≤ ρ |∂_j u|^2`,

and

`W_3(u,p)=∫ p u·∇ρ`.

On the set `{ρ>0}`, writing `u=ρn`, `|n|=1`, the diffusion decomposes as

`D_3(u) = ∫ [ 2ρ|∇ρ|^2 + ρ^3|∇n|^2 ]`

`         = (8/9)∫|∇ρ^(3/2)|^2 + ∫ρ^3|∇n|^2`.

Incompressibility gives the exact amplitude–direction relation

`n·∇ρ = -ρ div n`,

hence

`u·∇ρ = -ρ^2 div n`

where `ρ>0`, so the pressure work can be viewed as

`W_3 = -∫ p ρ^2 div n`

whenever the direction form is justified (or after a standard nonvanishing/regularization argument).

## Proof

### Time and transport terms

Because `ρu = ∇_u (|u|^3/3)` in the velocity variable,

`∫ ∂_t u·ρu = (1/3)d/dt ∫ρ^3`.

For convection,

`(u·∇)u·ρu = (1/3)u·∇(ρ^3)`,

whose integral vanishes on the torus because `div u=0`.

### Diffusion

Integration by parts gives

`-∫ Δu·ρu = ∫ ∇u : ∇(ρu)`

`= ∫ [ρ|∇u|^2 + Σ_j (u·∂_j u) ∂_jρ]`.

For `ρ>0`, `∂_jρ=(u·∂_j u)/ρ`, yielding `D_3` above. The zero set is harmless because

`(u·∂_j u)^2/ρ ≤ ρ|∂_j u|^2`.

If `u=ρn`, then `u·∂_j u=ρ∂_jρ` and

`|∂_j u|^2 = |∂_jρ|^2 + ρ^2|∂_j n|^2`,

because `n·∂_j n=0`. Summing yields the amplitude–direction form.

### Pressure

`-∫∇p·ρu = ∫p div(ρu) = ∫p u·∇ρ`,

again using `div u=0`.

Finally, from `0=div(ρn)=n·∇ρ+ρ div n`, we obtain the direction identity.

## Why this matters

`L^3` is scale-critical for 3D Navier–Stokes. R01 isolates the obstruction to a direct critical entropy estimate:

- viscosity contributes a manifestly nonnegative amplitude-gradient plus direction-gradient dissipation;
- convection cancels exactly;
- all sign-indefiniteness is concentrated in the nonlocal pressure work `W_3`.

This is a useful reduction, not closure. A global proof through R01 would still need an a priori estimate on `W_3` that survives arbitrary amplitude/concentration and does not assume the desired critical bound.

## Relation to prior work

Alexis Vasseur explicitly used the incompressibility relation

`|u| div(u/|u|) = -(u/|u|)·∇|u|`

in a velocity-direction regularity criterion. R01 does **not** claim novelty for that relation; it packages the critical `L^3` testing identity and its exact diffusion split as this project's H1 proof interface.

Primary source: https://arxiv.org/abs/0705.2446
