# RD026 — Productive-scale nontriviality does not force parabolic time alignment

**Status:** `exact abstract route guard / not a Navier–Stokes trajectory`  
**Targets:** invalid promotion of R47–R48 into parabolic compactness  
**Clay status:** **NOT SOLVED**

R48 closes one amplitude/frequency escape branch on the R47-good unit bursts. It gives a work-linked effective amplitude `B_J`, a productive radius `R_theta`, a uniform critical `D_3` budget, and a center for which the velocity remains nonzero after rescaling by `R_theta`.

None of those statements alone controls

> `Tau_J := R_theta^2 |J|`.

RD026 constructs two abstract scalar/productive-work families satisfying the proved envelope architecture through R48 while `Tau_J -> 0` in one family and `Tau_J -> infinity` in the other. The construction is deliberately not an NSE trajectory; its role is to forbid an algebraic shortcut from productive-scale nontriviality to parabolic compactness.

## Common skeleton

Fix `theta=1/2`, normalize `E0=V=1`, and for integer `n>=4` set

> `R_n=n`, `L_n=n/2`, `q_n=n^-2`, `D_n=1`, `B_n=n`,
>
> `Sigma_n=sqrt(2) B_n D_n=sqrt(2)n`.

Take `M_n=n^3` productive modes in an abstract shell with radii comparable to `n`, each carrying positive integrated common work `1/M_n`.

Then `R_n/B_n=1`, `Sigma_n/R_n=sqrt(2)>1`, and a work-linked center may have amplitude `B_n/2`, so the productive-scale normalized center amplitude is `1/2`.

## Fast branch

Let `ell_n=n^-4`. Then

> `R_n^2 ell_n=n^-2 ->0`.

Moreover

> `sqrt(ell_n q_n)=n^-3=1/M_n`,
>
> `q_n/R_n=n^-3`,
>
> `R_n^3 sqrt(ell_n q_n)=1`,
>
> `R_n^4 ell_n=1`.

Thus the R42/R43/R45 scalar capacity architecture is compatible with a burst much shorter than the parabolic time `R_n^-2`.

## Slow branch

Let `ell_n=n^-1`. Then

> `R_n^2 ell_n=n -> infinity`,

while `ell_n->0` and `q_n->0`. Also

> `sqrt(ell_n q_n)=n^-3/2 >=n^-3`,
>
> `q_n/R_n=n^-3`,
>
> `R_n^3 sqrt(ell_n q_n)=n^(3/2)`,
>
> `R_n^4 ell_n=n^3`.

So the long branch is compatible with the same scalar floors.

Assign on every abstract burst `int D_3=1` and `int||u||_9^3=1`. Both are uniformly critical in the spirit of R47; they do not distinguish the two time branches.

## Scope

RD026 rejects only

> `R47 critical bounds + R48 productive-scale nontriviality => R_theta^2|J| ~ 1`.

A future theorem must use genuine orbit dynamics — e.g. Duhamel/heat propagation at the productive scale, local-energy cylinder estimates, or another PDE compactness mechanism — to control time alignment.

RD026 does **not** construct a Navier–Stokes singularity.
