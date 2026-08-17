# R16 — Critical spin-conflict / bandwidth action criterion

**Status:** `exact conditional reduction / not claimed novel`  
**Depends on:** R08, R14, R15  
**Clay status:** the two critical actions are not proved finite for arbitrary data

R08 reduces the critical `L^3` barrier to the scale-invariant high-amplitude projected-Lamb tail action

`A_tail(T)=int_0^T U(t) ||Q(1_{rho>M_*} L)||_2^2 dt`,

where

`U=||u||_(3/2)`, `rho=|u|`, `L=omega×u`.

R14/R15 decompose the full Lamb force at the canonical center frequency `lambda_*` as

`L = 2 lambda_* u_+×u_- + r_*×u`,

where

`r_*=(D-lambda_*)u_+-(D-lambda_*)u_-`.

R16 turns this into two explicit critical spacetime actions.

## 1. Tail action is bounded by full Lamb action

The amplitude indicator is an `L^2` contraction and the Helmholtz projector `Q` is an orthogonal `L^2` contraction. Therefore

`||Q(1_{rho>M_*}L)||_2 <= ||L||_2`.

Hence

> `A_tail(T) <= int_0^T U ||L||_2^2 dt`.

## 2. Exact two-mechanism split

Set

`L_spin = 2 lambda_* u_+×u_-`,

`L_bw = r_*×u`.

Using `|a+b|^2<=2|a|^2+2|b|^2`,

`||L||_2^2`

`<= 8 lambda_*^2 ||u_+×u_-||_2^2`

`   + 2 ||r_*×u||_2^2`.

Define

> `A_spin(T) = int_0^T U lambda_*^2 ||u_+×u_-||_2^2 dt`,

and

> `A_bw(T) = int_0^T U ||r_*×u||_2^2 dt`.

Then

> `A_tail(T) <= 8 A_spin(T) + 2 A_bw(T)`.

Therefore:

> If both `A_spin(T)` and `A_bw(T)` are finite, then the R08 tail action is finite and the R08 critical `L^3` estimate closes on `[0,T]`.

This is a conditional criterion, not a proof that either action is finite for arbitrary smooth data.

## 3. Hölder-accessible upper versions

The two pointwise products admit

`||u_+×u_-||_2 <= ||u_+||_4 ||u_-||_4`,

`||r_*×u||_2 <= ||r_*||_4 ||u||_4`.

Thus sufficient (stronger) actions are

`A_spin^(4)=int U lambda_*^2 ||u_+||_4^2 ||u_-||_4^2 dt`,

`A_bw^(4)=int U ||r_*||_4^2 ||u||_4^2 dt`.

Their finiteness also implies `A_tail<infinity`.

## 4. Critical scaling audit

Under the Euclidean Navier–Stokes scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

- `U=||u||_(3/2)` has exponent `-1`;
- `lambda_*` has exponent `+1`;
- `||u_+×u_-||_2^2` has exponent `+1` because each `L^4` velocity factor has exponent `1/4`;
- `||r_*×u||_2^2` has exponent `+3`;
- `dt` has exponent `-2`.

For the spin action the total exponent is

`-1 + 2 + 1 - 2 = 0`.

For the bandwidth action it is

`-1 + 3 - 2 = 0`.

Hence both actions are genuinely scale invariant.

## 5. Necessary dichotomy for a tail-driven singularity

If a finite-time singularity forces

`A_tail(T*)=infinity`,

then the inequality above implies

> at least one of `A_spin(T*)`, `A_bw(T*)` must diverge.

Thus the R08/R13 ultraviolet obstruction has a true-helical dichotomy:

1. **spin-conflict divergence:** cross-helicity sectors sustain a nonintegrable critical interaction;
2. **bandwidth divergence:** radial spectral dispersion sustains a nonintegrable critical interaction;
3. or both.

This is more specific than saying simply that high frequencies grow.

## 6. Relation to Lerner–Vigneron

The known spin-conflict baseline says hypothetical blow-up requires simultaneous growth of both spin components. That makes `A_spin` a natural quantity rather than an artifact. R16 adds the second possibility `A_bw`, which is invisible if one reasons only from relative spin energies.

Primary source for the spin decomposition/blow-up baseline:
https://arxiv.org/abs/2203.07950

## 7. Remaining proof obligations

R16 does not prove finiteness of either critical action. The next theorem must do one of the following:

- bound `A_spin` from helicity/triad structure strongly enough to be finite;
- bound `A_bw` from dissipation or radial-frequency transport;
- prove that if one action becomes large the other is forced into a regime that regularizes the flow;
- construct a minimal rescaled ancient object with one divergent action and derive a rigidity contradiction.

R16 turns the single opaque R08 obstruction into two independently falsifiable critical mechanisms.
