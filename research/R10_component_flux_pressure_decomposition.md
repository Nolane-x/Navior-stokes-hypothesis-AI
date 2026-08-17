# R10 — Component-flux decomposition of iso-speed pressure work

**Status:** `exact structural decomposition; frontier corrected by R21/C001`  
**Depends on:** R03, R09, RD005  
**Corrected by:** R21, C001  
**Clay status:** partial reduction only; no global bound is proved

> **Canonical correction.** The decomposition below is algebraically exact, but R21 proves that in the regularity-equivalent canonical **zero-mean Galilean frame**, every connected regular iso-speed component has `J_a(s)=0` separately. Therefore the inter-component term introduced here vanishes identically in the canonical proof frame. Sections describing it as a surviving obstruction are retained only to show the historical derivation; the live frontier is the intra-component pressure oscillation plus bad level geometry/critical levels.

R09 shows that the critical pressure work depends only on pressure variation modulo functions of the speed `rho=|u|`. RD005 warns that a regular speed level may be disconnected and that controlling geometry uniformly is impossible from incompressibility alone.

Let `s` be a regular value of `rho` at a smooth time slice and write

`Sigma_s = {x : rho(x)=s} = disjoint_union_a Sigma_{s,a}`

for its connected components. Let

`n_rho = grad rho / |grad rho|`

be the oriented level normal, and define the component flux

`J_a(s) = integral_{Sigma_{s,a}} u·n_rho dS`.

R09 gives the weaker total cancellation

> `sum_a J_a(s)=0`

for almost every regular `s`. R21 subsequently strengthens this to `J_a(s)=0` for every component in the canonical zero-mean frame.

## 1. Exact component decomposition

The level contribution to `W_3` is

`I(s) = integral_{Sigma_s} p u·n_rho dS`.

Choose on each component any scalar `pbar_a(s)`; in particular one may use the surface mean of `p`. Then exactly

> `I(s) = sum_a pbar_a(s) J_a(s)`
>
> `       + sum_a integral_{Sigma_{s,a}} [p-pbar_a(s)] u·n_rho dS`.

Historically this exposed two algebraic mechanisms:

1. **inter-component pressure/flux covariance**
   `C_inter(s)=sum_a pbar_a J_a`;
2. **within-component pressure oscillation**
   `C_intra(s)=sum_a integral (p-pbar_a) u·n_rho`.

R21 now gives, in the fixed zero-mean frame,

> `J_a(s)=0` for every `a`, hence `C_inter(s)=0`.

Therefore the canonical identity simplifies to

> `I(s)=C_intra(s)`.

This correction is frame-sensitive. The exact travelling shear retained in R21 has nonzero component flux before Galilean normalization, so one may not switch frames after defining speed-level quantities.

## 2. Tangential pressure gradient is a projected-Lamb quantity

R03 gives the Bernoulli/Lamb identity

`Q(omega x u) = -grad B`,

`B = p + rho^2/2`.

On `Sigma_s`, the kinetic term `rho^2/2=s^2/2` is constant. Therefore its tangential gradient vanishes and

> `grad_{Sigma_s} p = grad_{Sigma_s} B`
>
> `                     = -Proj_{T Sigma_s} Q(omega x u)`.

Consequently, whenever a component admits a surface Poincare inequality with constant `C_P(Sigma_{s,a})`, its intra-component pressure fluctuation obeys

`||p-pbar_a||_{L2(Sigma_{s,a})}`

`<= C_P(Sigma_{s,a}) ||Proj_T Q(omega x u)||_{L2(Sigma_{s,a})}`.

This identifies the correct local forcing for the surviving term. RD005 prevents treating the surface Poincare constants as uniformly bounded without further dynamical information.

## 3. Historical inter-component warning and its resolution

Before R21, tangential gradients determined pressure only up to one additive constant per connected component, so an estimate using only `grad_Sigma p` appeared unable to see `C_inter`.

R21 supplies the missing topological/Helmholtz fact: after Galilean reduction to zero mean, the periodic divergence-free velocity is a global periodic curl `u=curl A`. Each regular level component is a closed oriented surface, hence surface Stokes gives its flux exactly zero. Thus component pressure offsets cannot contribute through `C_inter` in the canonical frame.

The remaining issue is not pressure offsets between components but the size of the within-component fluctuation when the component geometry has poor Poincare constants.

## 4. Flux interpretation after R21

Since

`q=u·grad rho=|grad rho| u·n_rho`,

the component flux `J_a` measures net velocity crossing a connected iso-speed sheet. R21 proves that this net crossing is zero componentwise in the normalized periodic setting.

Pointwise crossing need not vanish: positive and negative normal velocity may cancel on the same component. Therefore the pressure work can still be nonzero because pressure correlates with that signed crossing **within** the component.

This gives the corrected live mechanism:

> control the covariance of **within-component pressure fluctuation** with the zero-mean signed crossing density on dynamically dangerous high-speed levels.

## 5. Compatibility with the high-amplitude reduction

R08 says only levels above the intrinsic threshold

`M_*(t)=nu^2/[12 C_H^2 ||u||_(3/2)]`

need support the surviving projected-Lamb tail obstruction.

After R21 it is unnecessary to control component pressure means or inter-component flux covariance. A positive theorem may target only regular values `s>M_*(t)` and prove that, for example,

1. a geometry-weighted surface Poincare factor is integrable in coarea/time;
2. tangential projected-Lamb energy makes the intra-component term absorbable;
3. the set of geometrically degenerate levels has insufficient coarea weight to make the critical action diverge;
4. a quotient/Dirichlet-form estimate bypasses explicit surface constants altogether.

## 6. Remaining obstruction

R10 + R21 still do **not** bound surface Poincare constants, tangential projected-Lamb energy on high-speed components, or critical-value contributions.

The corrected load-bearing quantity is now one mechanism rather than two:

> **intra-component projected-Lamb pressure oscillation on potentially bad iso-speed geometry.**

Any future proof must control this quantity at critical scaling and justify the coarea/critical-level limit operations. R10/R21 do not solve global regularity.
