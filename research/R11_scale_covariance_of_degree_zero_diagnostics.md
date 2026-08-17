# R11 — Scale covariance of degree-zero Navier–Stokes diagnostics

**Status:** `exact structural theorem`  
**Depends on:** only Navier–Stokes homogeneity; applied here to R03 `kappa_L`  
**Clay status:** no regularity conclusion

P04 varies the amplitude of one fixed spatial shape. A hypothetical singularity, however, is probed by the full Navier–Stokes scaling that changes amplitude and spatial frequency together. R11 separates these two operations exactly for any differentiable degree-zero diagnostic.

Let

`F_nu(u)=nu Delta u-B(u,u)`,

where

`B(u,u)=P[(u·grad)u]`.

Let `Phi` be a differentiable scalar diagnostic satisfying positive amplitude invariance

`Phi(a u)=Phi(u)` for every `a>0`.

The projected Lamb coherence `kappa_L` of R03 has this property because both `Q(omega×u)` and `Q(|u|u)` are quadratic in amplitude.

## 1. Amplitude-only law

Amplitude invariance implies for every tangent `h`

`D Phi_{a u}[h] = (1/a) D Phi_u[h]`.

Since

`F_nu(a u)=a nu Delta u-a^2 B(u,u)`,

we obtain

> `D Phi_{a u}[F_nu(a u)]`

> `= nu D Phi_u[Delta u] - a D Phi_u[B(u,u)]`.

Thus the instantaneous Navier–Stokes derivative of **any degree-zero diagnostic is affine in the amplitude `a`** when spatial shape/frequency are held fixed.

The two coefficients have a clean meaning:

- intercept: viscous contribution;
- slope: convective/Leray contribution.

A sign crossover under amplitude-only scaling is therefore not mysterious and must not be confused with a change under true Navier–Stokes scaling.

## 2. Integer concentration scaling on the torus

For an integer `m>=1`, define

`S_m u(x)=m u(m x)`

on the unit torus. The map `x -> m x (mod 1)` preserves torus integrals. The degree-zero Fourier Helmholtz projector commutes with this dilation, so for `Phi=kappa_L`,

> `Phi(S_m u)=Phi(u)`.

The Navier–Stokes vector field is exactly covariant:

`Delta(S_m u)=m^3 (Delta u)(m x)`,

`B(S_m u,S_m u)=m^3 B(u,u)(m x)`,

hence

> `F_nu(S_m u)=m^3 [F_nu(u)](m x)`.

Now

`S_m u + t m^3 h(m x) = S_m[u+t m^2 h]`.

Differentiating the scale-invariant diagnostic gives

> `D Phi_{S_m u}[F_nu(S_m u)]`

> `= m^2 D Phi_u[F_nu(u)]`.

Therefore the **sign** of the instantaneous derivative is invariant under every integer Navier–Stokes concentration scaling, while its magnitude scales as inverse time, `m^2`.

## 3. Application to projected Lamb coherence

For

`Phi(u)=kappa_L(u)`

whenever the two projected defects have nonzero norms:

1. amplitude-only sweeps must lie on an affine tangent law;
2. a positive/negative tangent sign at one smooth periodic field is inherited by all integer concentration-scaled copies `m u(mx)`;
3. a proposed universal local sign law near concentration cannot be rescued merely by saying that the original counterexample was 'too low frequency'.

A rigorous continuum counterexample to such a local sign law would still require a rigorously certified sign at the base field. P04 currently supplies high-margin numerical evidence, not an interval proof.

## 4. Interpretation of P04

P04's fixed-shape derivatives decrease as amplitude increases. R11 explains why: they must be affine in amplitude up to numerical error. This means the fixed-frequency amplitude experiment separates viscous and convective contributions rather than directly emulating blow-up scaling.

In contrast, once the sign at a base shape is established, the full scaling `S_m` preserves it exactly.

## 5. Research consequence

R11 further weakens the case for a universal **instantaneous scalar-angle Lyapunov law**. The more promising target remains R08's scale-invariant integrated high-amplitude tail action, where magnitude, support, frequency, and history all enter rather than only a degree-zero angle.

This theorem is purely structural: it neither proves P04's numerical sign in the continuum nor proves regularity/blow-up.
