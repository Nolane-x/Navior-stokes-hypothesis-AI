# RD015 — No uniform `L^p` shortcut for sharp spherical Fourier cutoffs

**Status:** `literature-backed route rejection / proof-scope guard`  
**Depends on:** R25, R28–R32  
**Kills:** any step that silently treats the sharp spherical projector `Pi_{<=K}=1_{|k|<=K}(D)` as a uniformly `L^p`-bounded smooth Littlewood–Paley projector for `p != 2`, with a constant independent of `K`  
**Does not kill:** fixed-`K` finite-dimensional bounds with explicit `K` dependence, `L^2` orthogonality, Hausdorff–Young counting arguments, rectangular coordinate cutoffs, or genuinely smooth Fourier multipliers

R25/R28/R29 use the sharp spherical cutoff

`Pi_{<=K}`

only in places where `L^2` orthogonality or explicit finite-mode counting is sufficient. Those uses are safe.

After R32, a tempting shortcut is to combine the stress-divergence identity

`omega×u = div(u tensor u - |u|^2 I/2)`

with an estimate of the form

`||Pi_{<=K} f||_p <= C_p ||f||_p`

and then pretend `C_p` is independent of `K` for `p=6/5`, `3/2`, or another non-Hilbert exponent.

That shortcut is not available without a new theorem.

## 1. Classical ball-multiplier obstruction

Charles Fefferman's 1971 theorem, *The multiplier problem for the ball*, establishes the fundamental obstruction for the characteristic function of a Euclidean ball as an `L^p` Fourier multiplier away from `p=2` in dimension at least two.

Primary source:

- C. Fefferman, *The multiplier problem for the ball*, Annals of Mathematics **94** (1971), 330–336, DOI 10.2307/1970864.

The repository does **not** use that Euclidean theorem as a black-box proof of a precise torus operator-norm growth rate. The narrower and sufficient governance conclusion is:

> one may not import a `K`-uniform non-`L^2` multiplier bound for the sharp spherical cutoff as though it were a standard smooth Littlewood–Paley projection.

Any periodic estimate needed by the proof must be proved in the exact periodic setting with its cutoff dependence exposed.

## 2. Safe existing uses

The following remain valid:

1. `L^2` orthogonality of disjoint sharp Fourier supports;
2. commutation of the sharp cutoff with the Helmholtz projectors;
3. contraction in `L^2`;
4. finite-mode estimates such as
   `||Pi_{<=K}f||_2 <= sqrt(N_K) sup_k |fhat(k)|`;
5. Hausdorff–Young plus finite-set `ell^q -> ell^2` estimates, as in R32, with explicit `N_K` dependence.

RD015 changes none of R25–R32.

## 3. Unsafe proof pattern

The following pattern is now explicitly rejected:

`sharp spherical Pi_{<=K}`

`+ generic L^p multiplier boundedness with K-independent constant`

`+ stress/commutator estimate`

`=> subquadratic compensator`.

The middle step is precisely what requires proof and cannot be assumed.

## 4. Surviving redesign

A promising redesign is to replace the sharp binary split by self-adjoint smooth multipliers `M_K,H_K` satisfying

`M_K^2 + H_K^2 = I`

on nonzero Fourier modes.

Such a square partition can retain the exact pressure-work decomposition because the squares, rather than the supports, sum to the identity. A smooth symbol can then be chosen so that standard kernel/Mikhlin-type bounds and commutator methods become legitimate candidates.

This redesign must re-derive every exact P/Q work identity; one may not simply swap a sharp projector for a smooth filter inside R28/R29 and assume orthogonal-support formulas survive unchanged.

## 5. Frontier consequence

RD015 makes the next harmonic-analysis target precise:

> build an **exact smooth square-partition analogue** of R29, then test whether its low-frequency commutator admits a genuinely better estimate using Navier–Stokes structure.

That route preserves exact representation algebra while avoiding a hidden sharp-ball `L^p` assumption.

RD015 is a proof-integrity guard, not a Navier–Stokes regularity theorem.
