# RD003 — No generic quadratic Lyapunov can make 3D convection statewise dissipative for all amplitudes

**Status:** `exact structural no-go / elementary symmetry argument; not claimed novel`  
**Kills:** attempts to solve arbitrary-data regularity by adding a fixed quadratic correction whose convection contribution is strictly dissipative for every state  
**Does not kill:** nonquadratic, history-dependent, sign-restricted, solution-dependent, or exactly convection-invariant functionals

Let `H` be a real divergence-free phase space on the torus, let

`B(u,u)=P[(u·grad)u]`

be the Euler/Navier–Stokes quadratic convection, and consider a fixed quadratic functional

`Phi_A(u) = (1/2)<Au,u>`,

where `A` is linear and self-adjoint on the smooth states under consideration.

The nonlinear contribution to its derivative is

`N_A(u) = -<Au,B(u,u)>`.

## Oddness under velocity reversal

Because convection is quadratic,

`B(-u,-u)=B(u,u)`,

while linearity gives

`A(-u)=-Au`.

Therefore

> `N_A(-u) = -N_A(u)`.

Hence a statewise sign law

`N_A(u) <= 0 for every smooth divergence-free u`

immediately implies `N_A(u)=0` for every such `u`: applying the same law to `-u` gives `-N_A(u)<=0`, so `N_A(u)>=0`.

Thus:

> A fixed quadratic functional cannot receive a strictly dissipative sign from the convection term on all states. Its convective contribution must either change sign somewhere or vanish identically.

## Arbitrary-amplitude Navier–Stokes corollary

Suppose one tries to prove global regularity by showing `Phi_A` is nonincreasing for every smooth initial state under

`partial_t u + B(u,u) = nu Delta u`.

At a state `a u`, `a>0`, the nonlinear contribution scales cubically,

`N_A(a u) = a^3 N_A(u)`,

while the viscous quadratic contribution

`V_A(a u)=nu< A(a u), Delta(a u)>`

scales as `a^2 V_A(u)`.

If `N_A` is not identically zero, velocity reversal provides a state with `N_A(u)>0`. For sufficiently large `a`, the positive cubic term dominates any fixed quadratic viscous contribution. Therefore a universal arbitrary-amplitude monotonicity theorem for a fixed quadratic `Phi_A` is impossible unless

`N_A(u) ≡ 0`.

This conclusion does not require `A` to commute with `Delta`; only the homogeneities matter.

## Examples of the surviving exceptional class

Kinetic energy corresponds to `A=I`. Its convective contribution vanishes exactly:

`<u,B(u,u)>=0`.

Other quadratic quantities may also have exact Euler cancellations in special settings, but RD003 says that **strict statewise convective damping cannot be manufactured merely by choosing a fixed quadratic metric**.

## Research consequence

The H3 search space should not spend effort on a generic fixed quadratic energy correction of the form

`||u||_2^2 + <Ku,u>`

whose hoped-for mechanism is a universally negative convection term. Either the modified quadratic is another exact convection invariant/cancellation, or its nonlinear derivative changes sign and arbitrary amplitude defeats monotonicity.

Potentially viable alternatives must be structurally different:

1. a nonquadratic critical functional;
2. a time/history-dependent metric;
3. a scale-local multilevel quantity whose coefficients react to the evolving spectrum;
4. a functional that is not monotone statewise but obeys an integrated barrier along genuine Navier–Stokes trajectories;
5. a conditional quadratic form whose admissible state set is itself proved dynamically invariant.

RD003 therefore reinforces the representation shift already forced by RD001/RD002: the missing mechanism is unlikely to be a simple instantaneous Lyapunov sign valid on the full divergence-free state space.
