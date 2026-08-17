# R10 — Component-flux decomposition of iso-speed pressure work

**Status:** `exact structural reduction / not claimed novel`  
**Depends on:** R03, R09, RD005  
**Clay status:** partial reduction only; no global bound is proved

R09 shows that the critical pressure work depends only on pressure variation modulo functions of the speed `rho=|u|`. RD005 warns that a regular speed level may be disconnected and that controlling pressure oscillation inside each component is not enough.

R10 makes that missing term explicit.

Let `s` be a regular value of `rho` at a smooth time slice and write

`Sigma_s = {x : rho(x)=s} = disjoint_union_a Sigma_{s,a}`

for its connected components. Let

`n_rho = grad rho / |grad rho|`

be the oriented level normal, and define the component flux

`J_a(s) = integral_{Sigma_{s,a}} u·n_rho dS`.

By the coarea form of the R09 cancellation,

> `sum_a J_a(s)=0`

for almost every regular `s`.

## 1. Exact component decomposition

The level contribution to `W_3` is

`I(s) = integral_{Sigma_s} p u·n_rho dS`.

Choose on each component any scalar `pbar_a(s)`; in particular one may use the surface mean of `p`. Then exactly

> `I(s) = sum_a pbar_a(s) J_a(s)`

> `       + sum_a integral_{Sigma_{s,a}} [p-pbar_a(s)] u·n_rho dS`.

Thus pressure work has two distinct mechanisms:

1. **inter-component pressure/flux covariance**
   `C_inter(s)=sum_a pbar_a J_a`;
2. **within-component pressure oscillation**
   `C_intra(s)=sum_a integral (p-pbar_a) u·n_rho`.

Because `sum_a J_a=0`, the inter-component term is invariant under adding the same scalar to every `pbar_a`, as it must be under the R09 quotient symmetry `p -> p+F(rho)`.

For two components this simplifies to

`C_inter = [pbar_1-pbar_2] J_1`

because `J_2=-J_1`. Hence even if pressure is perfectly constant on each component, a difference of component means can still drive `L^3` pressure work.

## 2. Tangential pressure gradient is a projected-Lamb quantity

R03 gives the Bernoulli/Lamb identity

`Q(omega x u) = -grad B`,

`B = p + rho^2/2`.

On `Sigma_s`, the kinetic term `rho^2/2=s^2/2` is constant. Therefore its tangential gradient vanishes and

> `grad_{Sigma_s} p = grad_{Sigma_s} B`

> `                     = -Proj_{T Sigma_s} Q(omega x u)`.

Consequently, whenever a component admits a surface Poincare inequality with constant `C_P(Sigma_{s,a})`, its intra-component pressure fluctuation obeys a schematic exact-input bound

`||p-pbar_a||_{L2(Sigma_{s,a})}`

`<= C_P(Sigma_{s,a}) ||Proj_T Q(omega x u)||_{L2(Sigma_{s,a})}`.

This identifies the correct local forcing for the intra-component term. RD005 prevents treating the surface Poincare constants as uniformly bounded without further dynamical information.

## 3. Inter-component term cannot be recovered from tangential gradients alone

Tangential gradients determine pressure only up to one additive constant on each connected component. Therefore `C_inter` is invisible to any estimate based solely on `grad_{Sigma}p` inside individual components.

A complete R09 proof must supply an independent mechanism controlling at least one of:

- differences of component pressure means;
- component fluxes `J_a`;
- their covariance `sum_a pbar_a J_a`;
- a global quotient norm that controls both intra- and inter-component effects simultaneously.

This is an exact proof obligation, not a technical afterthought.

## 4. Flux interpretation

Since

`q=u·grad rho=|grad rho| u·n_rho`,

the component flux `J_a` measures how much incompressible velocity crosses a given connected iso-speed sheet. The total crossing cancels at each speed, but individual components may exchange equal and opposite flux.

Thus a dangerous pressure configuration must correlate pressure offsets with these compensating component fluxes.

This offers a route that is more specific than generic level-set geometry:

> control the **pressure-offset × compensating-flux** mechanism on the R08 high-amplitude levels.

## 5. Compatibility with the high-amplitude reduction

R08 says only levels above the intrinsic threshold

`M_*(t)=nu^2/[12 C_H^2 ||u||_(3/2)]`

need support the surviving projected-Lamb tail obstruction.

R10 therefore narrows the geometric program further. It is unnecessary to control all speed levels uniformly. A positive theorem may target only regular values `s>M_*(t)` and prove that either

1. the component flux vector `J(s)` is small;
2. pressure means across components nearly agree;
3. tangential projected-Lamb energy makes the intra-component term absorbable;
4. the set of exceptional levels has insufficient coarea weight to make the critical action diverge.

## 6. Remaining obstruction

R10 does not bound component fluxes, component pressure offsets, or surface Poincare constants. It removes a hidden gap from the R09 strategy and turns it into two explicit load-bearing quantities:

> **intra-component projected-Lamb oscillation** and **inter-component pressure/flux covariance**.

Any future iso-speed proof that omits the second term is incomplete whenever level sets are disconnected.
