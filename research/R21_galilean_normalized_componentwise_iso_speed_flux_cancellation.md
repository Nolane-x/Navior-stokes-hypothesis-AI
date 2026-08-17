# R21 — Galilean-normalized componentwise iso-speed flux cancellation

**Status:** `exact structural theorem / correction-sharpening of R10`  
**Depends on:** R09–R10  
**Clay status:** removes one pressure-geometry obstruction only; does not bound the surviving intra-component pressure oscillation

R10 decomposes the critical pressure work on a regular speed level into an inter-component pressure/flux covariance and an intra-component pressure-oscillation term. It only used the total cancellation

`sum_a J_a(s)=0`,

where

`J_a(s)=integral_{Sigma_{s,a}} u·n_rho dS`.

In the canonical zero-mean periodic frame, every component flux actually vanishes **separately**.

A frame qualification is essential: the original Clay periodic statement does not impose zero spatial mean, and an exact travelling shear shows that individual component fluxes can be nonzero before Galilean normalization.

## 1. Canonical zero-mean Galilean frame

Let `u` be a smooth periodic solution of unforced Navier–Stokes on the three-torus. Its spatial mean

`m = integral_{T^3} u(x,t) dx`

is constant in time, because spatial integration of the equation kills the divergence, Laplacian and pressure-gradient terms.

Define

> `v(x,t)=u(x+m t,t)-m`.

Then `v` is periodic, divergence-free, has zero spatial mean, and satisfies the same unforced Navier–Stokes equation with the translated pressure

`pi(x,t)=p(x+m t,t)`.

Conversely,

`u(x,t)=v(x-m t,t)+m`.

Thus global smoothness of the Clay periodic problem is equivalent to global smoothness in this zero-mean Galilean frame.

Because speed-based diagnostics are not Galilean invariant, the convention is now frozen:

> all R01–R10 amplitude/iso-speed quantities used downstream are to be interpreted in the canonical zero-mean field `v`, not switched between frames mid-proof.

For readability the rest of this theorem writes `u` for that normalized zero-mean field.

## 2. Every smooth zero-mean periodic divergence-free field is a global periodic curl

Use Fourier convention `exp(i k·x)` on the `2 pi` torus; the unit-period torus differs only by common `2 pi` factors. For `k!=0`, incompressibility gives

`k·uhat(k)=0`.

Define

> `Ahat(k)= i k×uhat(k) / |k|^2`,

and set `Ahat(0)=0`. Zero mean gives `uhat(0)=0`.

Then

`i k×Ahat(k)`

`= - k×(k×uhat(k))/|k|^2`

`= uhat(k)`

because `k·uhat(k)=0`.

Smoothness of `u` gives rapid Fourier decay, hence `A` is a smooth periodic vector potential satisfying

> `curl A=u`.

The zero-mean hypothesis is exactly what removes the harmonic constant mode that cannot be represented as a periodic curl.

## 3. Componentwise flux theorem

Let

`rho=|u|`,

and let `s>0` be a regular value of `rho`. Every connected component

`Sigma_{s,a}`

of `{rho=s}` is a compact smooth closed oriented surface in `T^3`, with orientation

`n_rho=grad rho/|grad rho|`.

By the surface Stokes theorem and `u=curl A`,

> `J_a(s)`
>
> `= integral_{Sigma_{s,a}} u·n_rho dS`
>
> `= integral_{Sigma_{s,a}} (curl A)·n_rho dS`
>
> `= integral_{boundary Sigma_{s,a}} A·dl`
>
> `= 0`.

Therefore, for every regular positive speed level and **every connected component separately**,

> `J_a(s)=0`.

This remains true even if the component is non-separating in the torus; the argument uses exactness as a curl, not the assumption that the surface bounds a three-dimensional region.

## 4. Exact correction of the R10 pressure decomposition

R10 writes the level contribution as

`I(s)=sum_a pbar_a(s) J_a(s)`

`     + sum_a integral_{Sigma_{s,a}} [p-pbar_a(s)] u·n_rho dS`.

R21 annihilates the first term identically in the canonical zero-mean frame:

> `C_inter(s)=sum_a pbar_a(s)J_a(s)=0`.

Hence exactly

> `I(s)=sum_a integral_{Sigma_{s,a}} [p-pbar_a(s)] u·n_rho dS`.

So disconnected iso-speed components do **not** create an independent pressure-offset × compensating-flux obstruction in this frame.

The R09 pressure-work route therefore needs only pressure variation **within** each connected regular speed component, together with control of singular/critical speed levels through an appropriate limiting or quotient-space formulation.

## 5. What survives from RD005

RD005 remains valid in its main claim: incompressibility alone does not provide uniform bounds on component count, curvature, neck geometry, topology or surface Poincare constants. The arbitrary-shear examples still show those quantities can be arbitrarily bad.

What R21 removes is only RD005's conditional component-flux warning. RD005 itself explicitly listed the possibility of proving that the component fluxes vanish separately; R21 closes exactly that option in the zero-mean periodic frame.

Thus the surviving geometric load is narrower:

- potentially bad surface Poincare constants;
- tangential Bernoulli/pressure oscillation on each component;
- behavior near critical values of `rho`;
- coarea/time integrability on dynamically selected high-amplitude levels.

There is no longer a separate inter-component pressure-mean covariance term.

## 6. Why the frame hypothesis cannot be omitted

Fix constants `a!=0`, `nu>0`, and define the exact smooth periodic travelling shear

> `u(x,y,z,t)=(exp(-nu t) sin(y-a t), a, 0)`.

It is divergence-free and satisfies unforced Navier–Stokes with constant pressure because the transport by the constant `a e_y` cancels the travelling phase derivative, leaving the one-dimensional heat equation.

Its mean is `m=(0,a,0)`. At any regular level of

`rho=sqrt(a^2+exp(-2nu t) sin^2(y-a t))`,

connected level components are coordinate two-tori `y=constant`, and

> `u·n_rho=+/- a`.

Thus individual component fluxes are nonzero in the unnormalized frame.

After the Galilean transformation by `m`, the same solution becomes

`v=(exp(-nu t) sin y,0,0)`,

whose regular iso-speed sheets have normal `+/- e_y` and satisfy `v·n=0` componentwise.

This exact witness prevents R21 from being accidentally promoted to a frame-free theorem.

## 7. New gradient-branch frontier

Combining R03, R09, R10 and R21, the Bernoulli-gradient branch is reduced to an intra-component problem:

`grad_{Sigma_s}p = -Proj_{T Sigma_s} Q(omega×u)`.

A successful continuation must convert this tangential projected-Lamb control into a scale-critical estimate on the coarea-integrated pressure work without assuming uniformly nice level geometry.

Promising forms include:

1. a weighted surface Poincare inequality whose degenerating geometric constant is compensated by coarea weight or dissipation;
2. a quotient-space/Dirichlet-form estimate that bypasses explicit component topology;
3. a high-amplitude theorem showing that bad Poincare geometry and large tangential `Q L` cannot persist together at a non-summable sequence of scales.

R21 proves none of these closing estimates.

## 8. Verification

`verification/check_R21_componentwise_flux_cancellation.py` independently certifies the Fourier vector-potential identity on exact rational-complex modes, audits mean conservation/Galilean algebra, and verifies the travelling-shear counterexample showing the mean-zero frame is necessary.
