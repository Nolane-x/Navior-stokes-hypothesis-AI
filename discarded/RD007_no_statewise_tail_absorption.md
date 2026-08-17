# RD007 — The R08 high-amplitude tail cannot be absorbed statewise by `D_3` with a universal constant

**Status:** `exact structural no-go`  
**Depends on:** R03, R08, RD001  
**Kills:** any attempted closure of R08 by a universal instantaneous estimate

`||u||_(3/2) ||Q(1_{|u|>M_*}(omega×u))||_2^2 <= C D_3`

with a fixed amplitude-independent constant `C` for all smooth divergence-free states  
**Does not kill:** time-integrated, Reynolds-dependent, history-dependent, concentration-scale, or solution-trajectory estimates

R08 reduces the critical obstruction to the statewise density

`T(u)=U ||Q(1_{rho>M_*(u)} L)||_2^2`,

where

`rho=|u|`, `L=omega×u`, `U=||u||_(3/2)`,

and

`M_*(u)=nu^2/[12 C_H^2 U]`.

It is tempting to try to finish R08 by proving

`T(u) <= C D_3(u)`

for all smooth divergence-free states. This is impossible.

## 1. Pure-amplitude scaling

Fix a smooth divergence-free state `u` with `Q L != 0`, and let

`u_a=a u`, `a>0`.

Then

`U(u_a)=a U(u)`,

`D_3(u_a)=a^3 D_3(u)`,

`L(u_a)=a^2 L(u)`,

and the intrinsic threshold becomes

`M_*(u_a)=M_*(u)/a`.

The high-amplitude condition is therefore

`|u_a|>M_*(u_a)`

iff

`rho > M_*(u)/a^2`.

Consequently

`T(u_a)`

`= a^5 U(u)`

`  * ||Q(1_{rho>M_*(u)/a^2} L(u))||_2^2`.

Because `L=omega×u=0` wherever `u=0`, the truncated Lamb field converges in `L^2` to the full Lamb field as `a->infinity`. The boundedness of `Q` then gives

`Q(1_{rho>M_*/a^2}L) -> QL` in `L^2`.

Thus, if `QL != 0`,

> `T(u_a)/D_3(u_a)`

> `~ a^2 [ U(u)||QL||_2^2 / D_3(u) ] -> infinity`.

No finite universal constant `C` can absorb the R08 tail density into `D_3` statewise.

## 2. Existence of a valid base state with `QL != 0`

RD001 gives an explicit smooth periodic mean-zero divergence-free family with

`W_3>0`

for sufficiently small nonzero perturbation parameter. R03 gives

`W_3=<QL,Q(|u|u)>`.

Therefore any such RD001 state necessarily has

`QL != 0`.

Hence the amplitude-scaling no-go above is not vacuous.

## 3. Why this does not contradict R08 critical scaling

The scaling used here changes amplitude while holding spatial frequency fixed. It is a Reynolds/amplitude sweep over admissible initial data, not the full local Navier–Stokes parabolic scaling.

R08's spacetime action is scale invariant under the full Euclidean Navier–Stokes scaling because the corresponding time scale changes as well. RD007 instead proves that **instantaneous** tail absorption cannot hold uniformly over arbitrary amplitudes at a fixed spatial shape.

This is precisely why any successful R08 closure must exploit evolution/history.

## 4. Research consequence

The following shortcut is permanently discarded:

`R08 tail density <= universal constant * D_3`

at each time.

A viable theorem must include at least one genuinely dynamical ingredient, for example:

1. integration over a viscosity/nonlinear time scale;
2. a relation between high-amplitude support lifetime and tail size;
3. frequency-dependent compensation under true parabolic scaling;
4. depletion that appears only after conditioning on actual Navier–Stokes trajectories;
5. a minimal-blow-up compactness/recurrence contradiction.

RD007 therefore reinforces the epoch-8 representation shift: the live object is a **critical spacetime action**, not another instantaneous coercive inequality.
