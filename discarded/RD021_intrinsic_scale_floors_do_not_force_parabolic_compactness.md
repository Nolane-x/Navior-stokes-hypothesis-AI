# RD021 — Intrinsic scale floors do not force parabolic compactness

**Status:** `abstract route guard / exact capacity countermodels / not a Navier–Stokes trajectory`  
**Targets:** invalid promotion of R43 into `R_theta^2|J| ~ 1` or compactness  
**Clay status:** **NOT SOLVED**

R43 gives two exact mode envelopes for an R41/R42 unit common-work burst,

`|b_k| <= beta`,

`|b_k| <= alpha/|k|`,

where, suppressing fixed `E0,V` constants,

`alpha ~ q`, `beta ~ sqrt(ell q)`,

with `ell=|J|` and `q=int_J ||omega||_2^2dt`.

A tempting but invalid next step is to infer a parabolic law `R_theta^2 ell ~ 1`. RD021 constructs finite positive lattice measures satisfying **both R43 envelopes**, carrying one unit of positive work, while the parabolic product tends either to zero or infinity. These are abstract coefficient measures, not Navier–Stokes trajectories.

## 1. Sub-parabolic family

Set `E0=V=1` and for integer `n>=8` choose

> `q_n=n^-2`, `ell_n=n^-8`.

Then `alpha_n=n^-2`, `beta_n=n^-5`.

Let

> `B_n={k in Z^3: n^3 <= k_j < n^3+n^2, j=1,2,3}`.

The box contains exactly `n^6` modes and every mode has `|k|<2n^3` for `n>=8`. Hence

`alpha_n/|k| > 1/(2n^5)`,

while `beta_n=1/n^5`.

Choose any `2n^5` modes and set

> `b_k=1/(2n^5)`.

Then the positive mass is exactly one and both R43 caps hold. Every occupied positive-work quantile has radius `O(n^3)`, so

> `R_theta^2 ell_n = O(n^-2) -> 0`.

Thus the caps permit a sub-parabolic intrinsic scale.

## 2. Super-parabolic family

Choose instead

> `q_n=n^-8`, `ell_n=n^-2`.

Then `alpha_n=n^-8`, `beta_n=n^-5`.

Let

> `C_n={k in Z^3: n^4 <= k_j < 3n^4, j=1,2,3}`.

It contains `8n^12` modes and every mode satisfies `|k|<6n^4`. Thus

`alpha_n/|k| > 1/(6n^12)`,

and `beta_n` is much larger for large `n`.

Choose any `6n^12` modes and set

> `b_k=1/(6n^12)`.

Again the positive mass is exactly one and both caps hold. Every occupied mode has `|k|>=sqrt(3)n^4`, hence

> `R_theta^2 ell_n >= 3 n^6 -> infinity`.

Thus the same caps permit a super-parabolic intrinsic scale.

## 3. Consequence

R43 supplies critical lower floors, but not the dynamical relation between frequency and burst duration. Therefore R43 alone does not imply

- upper/lower universal bounds on `R_theta^2|J|`;
- compactness after rescaling by `R_theta`;
- a nontrivial parabolic blow-up profile;
- spatial concentration at scale `R_theta^-1`.

A closing argument must add PDE information absent from coefficient envelopes: semigroup propagation, local energy/Oseen structure, inter-burst orbit constraints, or a many-body geometric depletion theorem.

## 4. Verification

`verification/check_RD021_intrinsic_scale_parabolic_countermodels.py` checks the finite boxes, cardinalities, radii, both R43 coefficient caps, exact unit positive mass, and the two opposite parabolic limits.

**RD021 is a logical countermodel to a proof step, not a Navier–Stokes blow-up construction.**
