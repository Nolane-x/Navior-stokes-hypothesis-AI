# R43 — Intrinsic positive-common-work quantile scale

**Status:** `exact conditional active-scale theorem / not a compactness theorem`  
**Depends on:** R39–R42, especially R41 unit common-work bursts and R42 modewise anti-sparsity  
**Clay status:** **NOT SOLVED**

R41–R42 produce actual-trajectory terminal bursts `J` carrying one unit of net common high-pass pressure work while `|J| -> 0`, the unweighted enstrophy cost `q_J -> 0`, resolved work evacuates every prescribed finite catalog, and productive output multiplicity diverges. R42, however, gives only a frequency-independent per-mode cap. It therefore does not select an intrinsic active radius from the burst itself.

R43 adds one derivative of the exact test field `G=|u|u`. The resulting Fourier envelope decays as `1/|k|`. Combining it with R42 yields a canonical positive-work quantile radius whose lower bounds are critical-homogeneous under Navier–Stokes concentration scaling.

This is the first post-E42 theorem that attaches an **intrinsic scale** to the normalized productive common work. It does not establish parabolic compactness, a spatial center, or global regularity.

## 1. Setup and Fourier convention

Work on the periodic torus `Omega=T^3` of volume `V`, in the canonical Galilean zero-mean frame. Use

`fhat(k)=V^{-1} int_Omega f(x) exp(-ik·x) dx`.

Let

`rho=|u|`, `G=rho u`, `L=omega × u`,

and for each nonzero output mode `k`, let `P_k,Q_k` be the Helmholtz projections. Define

`c_k(t)=[w_grad,k(t)+w_sol,k(t)]/2`.

With the Helmholtz reflection `J_k=Q_k-P_k=2Q_k-I`, orthogonal complementarity gives exactly

> `c_k(t)=(V/2) Re[Lhat(k,t) · conj(J_k Ghat(k,t))]`.

The operator `J_k` is an isometry. Let `E0=sup_(t<T*) ||u(t)||_2`. For a preterminal burst interval `J`, write

> `q_J=int_J ||omega(t)||_2^2 dt`.

## 2. One derivative of `G=|u|u`

The map `u -> |u|u` is locally Lipschitz and differentiable almost everywhere. At points where `rho>0`,

`partial_j G=(partial_j rho)u+rho partial_j u`,

while the same weak estimate follows at the zero set by the Lipschitz chain rule / smooth regularization. Since `|grad rho| <= |grad u|`,

> `|grad G| <= 2 |u| |grad u|`

almost everywhere. Therefore, by Cauchy–Schwarz and the periodic divergence-free identity `||grad u||_2=||omega||_2`,

> `||grad G||_1 <= 2 ||u||_2 ||grad u||_2 <= 2 E0 ||omega||_2`.

For each nonzero Fourier mode,

> `|k| |Ghat(k)| <= V^{-1} ||grad G||_1 <= 2 V^{-1} E0 ||omega||_2`.

Thus

> `|Ghat(k)| <= 2 V^{-1} E0 ||omega||_2 / |k|`.

## 3. Frequency-decaying common-work envelope

The physical Lamb coefficient satisfies

`|Lhat(k)| <= V^{-1} ||L||_1 <= V^{-1} E0 ||omega||_2`.

Using the exact common-mode formula and the isometry of `J_k`,

> `|c_k(t)| <= V^{-1} E0^2 ||omega(t)||_2^2 / |k|`.

Integrating over any preterminal interval `J`, with `b_k(J)=int_J c_k(t)dt`, gives

> `|b_k(J)| <= alpha_J/|k|`,

where

> `alpha_J=V^{-1}E0^2 q_J`.

R42 simultaneously gives

> `|b_k(J)| <= beta_J`,

with

> `beta_J=V^{-1}E0^3 sqrt(|J| q_J)`.

Hence

> `|b_k(J)| <= min(beta_J, alpha_J/|k|)`.

The crossover radius is

> `K_cross(J)=alpha_J/beta_J = sqrt(q_J/|J|)/E0`,

whenever `|J|q_J>0`.

## 4. Positive-work quantile radius

Let `J` be an R41 unit common-work burst at parent cutoff `L`. R42 gives

`sum_(|k|>L) b_k(J)=1`

and therefore `sum_(|k|>L) (b_k(J))_+ >= 1`.

Fix `0<theta<1`. Define the **positive common-work theta-quantile radius** `R_theta(J,L)` as the infimum of `R>L` for which

> `sum_(L<|k|<=R) (b_k(J))_+ >= theta`.

For smooth preterminal bursts the work pairing is absolutely summable, so this radius is finite. Unlike the externally prescribed cutoff `L`, `R_theta` is selected by the actual productive common-work distribution.

## 5. Two lattice capacities

For `R>=1`, let `N(R)=#{k in Z^3:0<|k|<=R}`. The containing cube gives

> `N(R) <= 27 R^3`.

For the weighted sum, partition by max-norm shell `m=max(|k_1|,|k_2|,|k_3|)`. The shell has exactly

> `(2m+1)^3-(2m-1)^3=24m^2+2`

points and `|k|>=m`. Thus for integer `R>=1`,

> `sum_(0<|k|<=R) 1/|k| <= 26 R^2`.

For arbitrary real radii the same statement holds after harmless universal-constant adjustment by `ceil(R)`.

## 6. Intrinsic scale floors

At `R=R_theta`, the R42 envelope yields

`theta <= 27 beta_J R_theta^3`,

hence

> `R_theta(J,L) >= [theta V/(27 E0^3 sqrt(|J|q_J))]^(1/3)`.

The new R43 envelope gives independently

`theta <= 26 alpha_J R_theta^2`,

hence

> `R_theta(J,L) >= [theta V/(26 E0^2 q_J)]^(1/2)`.

Therefore

> `R_theta(J,L) >= max{ [theta V/(27 E0^3 sqrt(|J|q_J))]^(1/3), [theta V/(26 E0^2 q_J)]^(1/2) }`.

Along the R41 good-burst sequence, `|J_n|->0` and `q_(J_n)->0`, so both floors diverge. A fixed positive fraction of normalized productive common work is forced to an intrinsically diverging output radius.

## 7. Scale-time form and critical homogeneity

Equivalently,

> `R_theta^3 E0^3 sqrt(|J|q_J)/V >= theta/27`,

and

> `R_theta^2 E0^2 q_J/V >= theta/26`.

Under the formal Navier–Stokes concentration scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

one has

`E0 -> lambda^(-1/2)E0`, `|J| -> lambda^(-2)|J|`, `q_J -> lambda^(-1)q_J`, `R_theta -> lambda R_theta`.

Both products are invariant. Thus the floors live at critical scaling rather than being artifacts of a subcritical norm.

## 8. What R43 changes after E42

E42 showed that productive modes must become numerous and escape every prescribed finite prefix. R43 adds a canonical quantitative statement:

> the normalized burst itself selects a positive-work quantile scale whose minimum possible radius is dictated by the burst's actual enstrophy cost and duration.

The `q_J^(-1/2)` floor is especially important: an R41 burst with vanishing unweighted viscous cost cannot place a fixed fraction of its unit common work at frequencies substantially below that intrinsic radius.

## 9. What R43 does not prove

R43 does not establish

- `R_theta^2 |J| ~ 1` or any parabolic comparability;
- an upper bound on the productive radius;
- spatial localization at radius `R_theta^-1`;
- tightness after rescaling by `R_theta`;
- a nontrivial critical/ancient limit;
- summability of the many-body common mode;
- global regularity.

The two mode envelopes alone permit abstract productive distributions with `R_theta^2|J| ->0` or `->infinity`; RD021 records this route guard explicitly.

The next load-bearing theorem must add genuine PDE information coupling the intrinsic spectral radius to time/spatial concentration, or use R37 geometry plus R42 multiplicity to deplete the many-body common mode directly.

## 10. Verification scope

`verification/check_R43_intrinsic_quantile_scale.py` audits the lattice capacities, randomized cap/quantile inequalities and critical homogeneity. `verification/fresh_verify_e43_intrinsic_scale_grid.py` independently reconstructs smooth divergence-free finite-Fourier worlds in physical space and verifies the derivative envelope, Lamb coefficient envelope and common-mode `1/|k|` bound without importing the primary checker.

**R43 is an exact conditional intrinsic-scale theorem for R41/R42 bursts. It is not a compactness theorem and not a solution of the Navier–Stokes Millennium Problem.**
