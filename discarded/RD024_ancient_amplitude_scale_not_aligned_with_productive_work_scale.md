# RD024 — Ancient/amplitude blow-up scale is not formally aligned with the productive-work scale

**Status:** `exact abstract two-branch route guard / not a Navier–Stokes trajectory`  
**Targets:** invalid inference `R43–R46 + ancient object existence => productive structure survives amplitude-normalized blow-up`  
**Clay status:** **NOT SOLVED**

R46 identifies a genuine singular spatial point and imports a theorem guaranteeing a non-trivial mild bounded ancient blow-up solution.  It is tempting to conclude that the R43/R45/R46 productive-work structure automatically appears at `O(1)` frequency in an amplitude-normalized blow-up.  That conclusion is not justified by the current scalar estimates.

The natural dimensionless alignment parameter is

> `Chi_theta(J)=R_theta(J,L0)/A_J`,

because both a velocity amplitude and a Fourier frequency scale linearly under Navier–Stokes concentration scaling.

RD024 constructs two abstract families satisfying the project’s scalar burst constraints while

> `Chi_theta -> 0`

in one family and

> `Chi_theta -> infinity`

in another.

These families are not PDE solutions.  They prove only that scale alignment requires genuine orbit/helical/localisation structure beyond the scalar envelopes.

## 1. Common parameters

Fix `theta=1/2`, `V=E0=1`, and let

> `q_n=4sqrt(3)n^-2`,
>
> `ell_n=n^-4`,
>
> `L_n=n/4`.

Then `q_n->0`, `ell_n->0`, and `L_n->infinity`.

The three lower productive-radius floors through R45 are all only `O(n)`:

- R43 `q` floor: `R_theta >= c_2 n`;
- R43 multiplicity floor: `R_theta >= c_3 n`;
- R45 stress floor: `R_theta >= c_4 n`.

The per-burst R45/R46 amplitude condition is

> `A_n^2 q_n >= L_n`.

The R46 local-work upper scale `Sigma_n` must satisfy schematically

> `L_n <= Sigma_n <= sqrt(2) A_n^2 q_n`,

and the positive quantile upper bound is

> `R_theta <= Sigma_n/(1-theta)=2Sigma_n`.

## 2. Branch A — productive frequency collapses under amplitude normalization

Choose

> `A_n=n^(3/2)`,
>
> `R_n=4n`,
>
> `Sigma_n=4n`.

For sufficiently large `n`, all three lower floors are below `R_n`, while

`A_n^2 q_n=4sqrt(3)n >= Sigma_n >= L_n`.

Also

`R_n=Sigma_n <=2Sigma_n`,

so the upper radius constraint holds.

But

> `Chi_n=R_n/A_n=4n^-1/2 ->0`.

Thus productive output may move to zero frequency in an amplitude-normalized blow-up while all scalar bounds remain valid.

A concrete high-multiplicity coefficient cloud can be placed on `O(n)` lattice modes using the same box construction as RD023; the R42/R43 per-mode caps are compatible after the fixed constants above are included.

## 3. Branch B — productive frequency escapes to infinity under amplitude normalization

Keep `q_n`, `ell_n`, and `L_n`, but choose

> `A_n=n^3`,
>
> `R_n=n^(7/2)`,
>
> `Sigma_n=n^(7/2)`.

Then

`A_n^2q_n=4sqrt(3)n^4`,

so for large `n`

`L_n << Sigma_n <=sqrt(2)A_n^2q_n`.

Again the lower R43/R45 radius floors are only `O(n)` and hence are satisfied, and

`R_n=Sigma_n<=2Sigma_n`.

Now

> `Chi_n=R_n/A_n=n^(1/2) ->infinity`.

A high-multiplicity cloud can be placed near radius `n^(7/2)` with enough modes to satisfy both the R42 frequency-independent cap and the R43 `q/|k|` cap; lattice capacity at that radius is vastly larger than the required multiplicity.

## 4. Consequence

Current scalar burst inequalities allow both extreme failures of scale alignment:

> productive frequency `<<` amplitude blow-up frequency,

and

> productive frequency `>>` amplitude blow-up frequency.

Therefore the existence of a non-trivial ancient solution at the R46 singular point does not by itself transfer

- the unit common-work normalization;
- R42 multiplicity explosion;
- R43/R45 productive radii;
- R37 helical depletion

into that ancient limit.

## 5. Exact post-R46 proof obligation

A material next theorem must use information absent from RD024, for example

1. a PDE relation between amplitude growth and the common-work output scale;
2. persistence of a fixed positive common-work fraction under an amplitude-normalized blow-up;
3. a rescaling chosen from `R_theta`/`Sigma_J` with independent compactness estimates;
4. local-energy/vorticity concentration that quantitatively aligns the spatial and spectral scales;
5. or many-body depletion that avoids the ancient-limit transfer problem entirely.

## 6. Scope

RD024 is an exact logical route guard, not a blow-up construction.  Its role is to prevent a literature-backed ancient-solution theorem from being overpromoted into a solution of the project-specific productive-work rigidity problem.
