# R15 — Canonical helical center frequency and spectral-variance Lamb bound

**Status:** `exact structural theorem / not claimed novel`  
**Depends on:** R14  
**Clay status:** no global regularity conclusion

R14 gives, for every reference frequency `lambda>0`,

`omega×u = 2 lambda u_+×u_- + r_lambda×u`,

where

`r_lambda=(D-lambda)u_+-(D-lambda)u_-`, `D=sqrt(-Delta)`.

R15 removes the free choice of `lambda` by minimizing the radial-dispersion defect exactly.

Assume `u` is a nonzero mean-zero periodic divergence-free field, with helical decomposition `u=u_++u_-` as in R14.

## 1. Exact dispersion quadratic

The two helical subspaces are orthogonal and are invariant under `D`. Therefore

`||r_lambda||_2^2`

`= ||(D-lambda)u_+||_2^2 + ||(D-lambda)u_-||_2^2`

`= ||D u||_2^2 - 2 lambda <D u,u> + lambda^2 ||u||_2^2`.

This is a strictly convex quadratic in `lambda`.

## 2. Canonical center frequency

The unique minimizer is

> `lambda_* = <D u,u> / ||u||_2^2`.

Because `D` is positive on the mean-zero torus spectrum, `lambda_*>0` for `u!=0`.

Equivalently,

`lambda_* = ||D^(1/2)u||_2^2 / ||u||_2^2`.

Thus `lambda_*` is the energy-weighted mean radial frequency of the field.

The minimum squared dispersion is

> `sigma_D^2 = ||D u||_2^2 - lambda_*^2 ||u||_2^2`.

By Cauchy-Schwarz, `sigma_D^2>=0`. Spectrally, this is exactly

`sum_k (|k|-lambda_*)^2 |u_hat(k)|^2`

up to the Fourier normalization convention for `D`.

Hence `sigma_D/||u||_2` is the energy-weighted standard deviation of radial frequency.

## 3. Canonical optimized Lamb bound

Substituting `lambda=lambda_*` into R14 gives

> `||omega×u||_1`

> `<= 2 lambda_* ||u_+||_2 ||u_-||_2`

> `   + sigma_D ||u||_2`.

Define

`E=||u||_2^2`,

`m_spin = 2||u_+||_2||u_-||_2 / E`,

and the relative radial bandwidth

`b_D = sigma_D / (lambda_* ||u||_2)`.

Then

> `||omega×u||_1 <= lambda_* E [m_spin + b_D]`.

Here

`0<=m_spin<=1`, `b_D>=0`.

The bound is now parameter-free: the two defects are a dimensionless spin-conflict factor and a dimensionless radial-bandwidth factor.

## 4. Exact monochromatic helicity relation

Suppose the field is supported on one radial shell, so `D u=lambda_* u`. Then `b_D=0`. Let the helicity be

`H=<u,curl u>`.

Because

`curl u_+=+lambda_*u_+`,

`curl u_-=-lambda_*u_-`,

we have

`H=lambda_*(||u_+||_2^2-||u_-||_2^2)`.

Writing

`h_rel = H/(lambda_* E)`,

one obtains exactly

> `m_spin = sqrt(1-h_rel^2)`.

Thus on a single shell the R15 bound becomes

> `||omega×u||_1 <= lambda_* E sqrt(1-h_rel^2)`.

The Beltrami endpoints `|h_rel|=1` are exactly single-spin and have zero Lamb force. The maximally spin-balanced shell `h_rel=0` permits the largest bound.

## 5. Scaling audit

Under the Euclidean Navier–Stokes scaling `u_lambda(x)=lambda u(lambda x)`:

- `lambda_*` scales as one inverse length;
- `sigma_D/||u||_2` scales as one inverse length;
- `m_spin` and `b_D` are dimensionless;
- `lambda_* E` has the same `L^1` Lamb-force scaling as `||omega×u||_1`.

So the canonical defects are compatible with the R13 ultraviolet scaling problem.

## 6. What R15 says about an ultraviolet tail cascade

R13 says any divergent R08 tail action must escape to arbitrarily high frequencies. R15 says that at any such scale a large full Lamb force can only be supported through at least one of two canonical defects:

1. **spin conflict:** `m_spin` stays appreciable;
2. **radial bandwidth:** `b_D` stays appreciable.

A narrow-band nearly single-spin packet is quantitatively Lamb-depleted.

This does not yet control the projected, high-amplitude-truncated Lamb force in R08, and it does not prove either defect is small along a hypothetical singular trajectory.

## 7. Literature interface

Lerner–Vigneron show that hypothetical finite-time blow-up requires simultaneous growth of both spin components. Therefore a global proof cannot simply assume `m_spin -> 0` near singularity. R15 instead provides a quantitative two-defect language in which a minimal-blow-up object would need to sustain spin conflict, radial bandwidth, or both at successively higher frequencies.

Primary reference for the spin decomposition/blow-up conflict baseline:
https://arxiv.org/abs/2203.07950

## 8. Next proof obligation

The next useful theorem must be dynamical. Candidate statements are:

- an integrated bound on `lambda_* E m_spin` at high amplitude/frequency;
- a dissipation inequality forcing `b_D` to be summable over ultraviolet scale-time boxes;
- a rigidity theorem excluding simultaneous scale persistence of both defects in a normalized minimal tail cascade;
- a frequency-local version of R15 compatible with the R08 amplitude truncation and the Leray projection.

R15 supplies the canonical coordinates for those questions but does not close them.
