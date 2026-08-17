# RD006 — Simple local Navier–Stokes repulsion of dangerous Lamb coherence is falsified

**Status:** `preregistered finite-dimensional trajectory falsification`  
**Depends on:** P03, P04  
**Kills:** the simple hypothesis that the true Navier–Stokes vector field must locally decrease projected Lamb coherence near every dangerous high-coherence state  
**Does not kill:** delayed, integrated, concentration-specific, tail-action, or other trajectory-dependent depletion mechanisms

After RD002 killed a universal statewise bound on

`kappa_L = <Q(omega×u),Q(|u|u)> / (||Q(omega×u)||_2 ||Q(|u|u)||_2)`,

a natural fallback was:

> perhaps arbitrary states can have large positive `kappa_L`, but the true Navier–Stokes dynamics immediately pushes such states toward lower coherence.

P04 preregistered a direct tangent test of this idea using the P03 winner.

## Frozen test

Let `v` be the committed P03 52-coefficient divergence-free field and set

`u_a=a v`, `a in {0.5,1,2,4,8}`, `nu=1`.

For each amplitude P04 computed the exact spectral Navier–Stokes tangent on the finite grid,

`F_NS(u)=Delta u-P[(u·grad)u]`,

and the symmetric directional derivative

`d_NS kappa_L = d/dt kappa_L(u+tF_NS(u))|_{t=0}`.

The derivative sign had to agree at three frozen step sizes and at both `N=48` and `N=64`.

## Result

The verdict was

> `H-nonrepel`.

Every tested amplitude had a robust **positive** tangent derivative.

At `N=64` the mean derivatives were approximately

```text
a=0.5 : +3.7344154154
a=1   : +3.5066161710
a=2   : +3.0510176814
a=4   : +2.1398207017
a=8   : +0.3174267395
```

The three-step relative spreads were all below `1.5e-7`, far inside the preregistered `5e-3` stability threshold. `N=48` gave the same positive signs with closely matching values.

Thus, on this dangerous static state, the true Navier–Stokes tangent initially **increases** rather than decreases projected Lamb coherence over the entire frozen amplitude set.

## Interpretation

This falsifies the simple local mechanism

`high kappa_L => d_NS kappa_L/dt < 0`

as a universal law.

It does **not** imply blow-up. `kappa_L` is only one normalized alignment variable, and a trajectory may later turn, dissipate, move its amplitude support, or reduce the R08 tail action through defect sizes even while coherence initially increases.

The result therefore redirects the positive program away from a one-variable local angle Lyapunov law.

## Surviving trajectory mechanisms

A viable route must use richer information, such as:

1. the full R08 high-amplitude tail action rather than `kappa_L` alone;
2. delayed/integrated depletion over a concentration time scale;
3. joint evolution of defect sizes and coherence;
4. amplitude-level transport and R09/R10 quotient-pressure/flux geometry;
5. exact triad/helical restrictions on sustained multiscale production rather than instantaneous tangent sign.

## Scope

P04 is a spectral finite-grid diagnostic with frozen preregistration and resolution/step stability. It is not an interval certificate or continuum theorem. RD006 therefore falsifies the **simple local hypothesis within the tested finite-dimensional representation** and strongly warns against promoting it, but it does not establish a universal continuum counterexample theorem.
