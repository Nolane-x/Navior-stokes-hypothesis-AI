# R37 — Common-mode helical/Helmholtz channel bottleneck

**Status:** `exact structural theorem / frontier correction / not claimed novel`  
**Depends on:** R14–R16, R24, R27, R29, R33–R36  
**Clay status:** verified partial structure only; no arbitrary-data summability theorem is proved

E35–E36 concentrated on the smooth P/Q representation mismatch. That was useful for proving synchronization, but it is not by itself the load-bearing singular quantity: R29/R34 already allow the two productive high-frequency pressure-work representations to diverge together while their difference is integrable or asymptotically negligible.

R37 corrects that emphasis. It first isolates the **common productive mode** exactly. It then inserts the helical decomposition into the physical Lamb source feeding that mode and computes the P/Q geometry of an individual helical pair. The result narrows the full-strength balanced high-high source to explicit spin/radial/angular mechanisms.

Let

`L = omega × u`,

`G = rho u`, `rho=|u|`,

and let `P,Q` be the solenoidal/gradient Helmholtz projections. Let `M,H` be real even self-adjoint smooth Fourier multipliers satisfying

> `M^2 + H^2 = I`.

They commute with `P,Q` and derivatives.

## 1. The load-bearing object is the common mode, not the mismatch

Define the high-filter productive works

`W_grad,H = <H QL,H QG>`,

`W_sol,H  = -<H PL,H PG>`.

Introduce the Helmholtz reflection

> `J = Q-P = 2Q-I`.

`J` is a self-adjoint `L^2` isometry and involution on nonzero Fourier modes.

Define

`C_H = (W_grad,H+W_sol,H)/2`,

`D_H = W_grad,H-W_sol,H`.

Orthogonality of `P,Q` gives exactly

> `2 C_H = <H L, J H G>`,

while

> `D_H = <H L,H G>`.

R33 gives `D_H=-D_M`, where

`D_M=<M^2L,G>`.

Therefore

> smallness or summability of the representation mismatch `D_H` does **not** imply smallness of `C_H`.

R29/R34 in fact force the singular endpoint scenario, if it occurs within this proof spine, to carry divergent positive common-mode work. From E37 onward the primary object to exclude is therefore `C_H`; the commutator mismatch is a secondary synchronization constraint.

## 2. Exact stress representations

Let

> `T = u tensor u - (rho^2/2) I`.

For divergence-free velocity,

> `L = div T`.

Using self-adjointness and commutation of `H,J` with Fourier derivatives,

> `C_H = -(1/2)<H T, H grad(JG)>`.

There is also an exact dual representation of the R33 low defect. Since

`D_M=<M^2L,G>`

and `<L,G>=0` pointwise after integration (`L perpendicular u`),

`M^2=I-H^2` yields

`D_M=-<H^2L,G>`.

Using `L=div T`,

> `D_M = <H T,H grad G>`.

Thus the same synchronization defect that appears as a **low-filter commutator** also appears exactly as a **high-filter stress/test-gradient pairing**.

This identity does not make the defect small; it identifies the output-frequency object that a successful scale-local estimate must control.

## 3. Transported-speed scalar inside the stress pairing

Write `q_amp=div(rho u)=u·grad rho`, as in R24. A direct pointwise calculation using `div u=0` gives

> `T : grad G = (3/2) rho^2 q_amp`.

Indeed, with `G=rho u`,

`grad G = rho grad u + u tensor grad rho`,

and contraction against `u tensor u-(rho^2/2)I` leaves exactly `(3/2)rho^2 u·grad rho`.

Its full spatial integral vanishes because

`(3/2)rho^2 u·grad rho=(1/2)u·grad(rho^3)`

and `div u=0` on the torus.

The high-filter defect therefore measures failure of this exact transported-speed cancellation after scale separation; it is not a generic stress product.

## 4. Exact pair-symmetrized helical Lamb formula

For a nonzero Fourier mode `r`, decompose

`uhat(r)=uhat_+(r)+uhat_-(r)`

with

`i r × uhat_s(r)=s |r| uhat_s(r)`, `s in {+1,-1}`.

For `k=p+q`, the ordered convolution for `Lhat(k)` is

`sum_{p+q=k} omegahat(p) × uhat(q)`.

Pairing the ordered terms `(p,q)` and `(q,p)` gives the exact symmetrized formula

> `Lhat(k)`
>
> `= (1/2) sum_{p+q=k} sum_{s,t=+-1}`
>
> `  (s|p|-t|q|)`
>
> `  [uhat_s(p) × uhat_t(q)]`.

This is the frequency-local refinement of the R14 spin-conflict/radial-bandwidth factorization.

Consequences at pair level are immediate:

- **same spin** (`s=t`) carries the radial-difference factor `|p|-|q|`;
- **opposite spin** (`s=-t`) carries the radial-sum factor `|p|+|q|`.

Hence same-spin equal-radius pairs contribute **exactly zero** to the physical Lamb coefficient, while opposite-spin equal-radius pairs remain full strength.

## 5. The common mode inherits the helical coefficient exactly

By Parseval, up to the fixed Fourier-volume normalization convention,

> `C_H`
>
> `= (1/4) Re sum_k h_K(k)^2`
>
> `  sum_{p+q=k} sum_{s,t}`
>
> `  (s|p|-t|q|)`
>
> `  [uhat_s(p) × uhat_t(q)]`
>
> `  · conjugate(J_k Ghat(k))`.

Thus the helical cancellation is not merely a bound on the full Lamb norm: it sits **inside the actual common productive mode** that survives R29/R34.

## 6. Exact P/Q geometry of one helical pair

Assume `p,q` are non-collinear. Set

`a=|p|`, `b=|q|`, `c=|k|`,

`mu=(p·q)/(ab)=cos(theta)`,

`n=(p×q)/|p×q|`.

Use the common-plane helical basis

> `h_s(r)=[n+i s(rhat×n)]/sqrt(2)`

for `r=p,q`. It satisfies `i r×h_s(r)=s|r|h_s(r)`.

A direct cross-product calculation gives

> `h_s(p) × h_t(q)`
>
> `= (i/2)(t qhat-s phat)`
>
> `  -(st/2) sin(theta) n`.

Let the pair-symmetrized Lamb source be

`F_st=(s a-t b) h_s(p)×h_t(q)`

(times the two scalar Fourier amplitudes, omitted here for readability).

The gradient projection at output `k` is exactly

> `Q_k[h_s(p)×h_t(q)]`
>
> `= (i/2c)`
>
> ` [t(b+a mu)-s(a+b mu)] khat`.

### 6.1 Same-spin: quadratic depletion in the gradient channel

When `t=s`,

> `Q_k F_ss`
>
> `= -(i/2)`
>
> `  ((a-b)^2(1-mu)/c) khat`.

So the same-spin gradient Lamb channel carries a **quadratic radial-gap factor** `(a-b)^2`, not merely the linear radial gap visible in the full Lamb coefficient.

In particular, `a=b` kills the entire same-spin pair exactly.

### 6.2 Opposite-spin equal-radius: angular depletion in the minority channel

Now take `t=-s` and `a=b`. Then `c=2a cos(theta/2)`, and the exact channel norms for unit helical amplitudes are

> `|Q_k F_{s,-s}| = c`,

> `|P_k F_{s,-s}| = c sin(theta/2)`.

Thus an equal-radius opposite-spin pair can be full-strength in the gradient channel, but as `theta->0` its **solenoidal** channel is suppressed linearly by `sin(theta/2)`.

Because R27/R30/R34 force the pointwise weaker Helmholtz Lamb channel to accumulate divergent critical action in the singular scenario, an exactly or nearly collinear opposite-spin pair cannot by itself supply a full-strength **balanced** P/Q mechanism.

## 7. Sharpened E37 bottleneck

At the level of an individual helical source pair, full-strength balanced production is therefore depleted in three geometrically distinct ways:

1. **same-spin equal shell:** exact zero;
2. **same-spin near-equal shell:** radial-gap depletion, with the gradient channel quadratic in the gap;
3. **opposite-spin near-collinear equal shell:** solenoidal depletion proportional to `sin(theta/2)`.

The pair-level sector that remains maximally dangerous is consequently centered on

> **opposite-spin, non-collinear, active-scale interactions**,

with radial dispersion supplying the alternative same-spin route.

This is a stricter mechanism than the E36 label “comparable high-high”. It directly couples the common productive mode to the balanced P/Q obstruction.

## 8. Why this is still not a global proof

The theorem is exact pairwise algebra. It does **not** justify exchanging

`min(||sum F_P||,||sum F_Q||)`

with a sum of pairwise minima. Many individually depleted interactions can accumulate coherently, and different triads can populate P and Q channels separately.

Therefore R37 does not prove spacetime summability of the common mode or balanced action.

A closing theorem must now control accumulation of the surviving

- opposite-spin/non-collinear annular interactions;
- radial-dispersive same-spin interactions;

in a scale-critical spacetime norm, or show that the R31 terminal packet sequence cannot maintain the required spin/radial/angular geometry.

## 9. Literature interface

Lerner–Vigneron diagonalize curl into spin-definite components and show that a hypothetical finite-time blow-up cannot be reduced to growth of only one spin sector. R37 is consistent with that constraint: the maximally dangerous narrow-shell pair mechanism is explicitly cross-spin rather than single-spin.

Primary source:

- J. Lerner, N. Vigneron, *On some properties of the curl operator and their consequences for the Navier–Stokes system*, arXiv:2203.07950.

The present formulas are proved directly in the repository and are not claimed as a novelty statement relative to the broader helical-triad literature.

## 10. Verification scope

`verification/check_R37_common_mode_helical_bottleneck.py` checks:

- the exact common-mode Helmholtz-reflection identity on several random finite Fourier worlds;
- the dual high-filter stress identity for the R33 defect;
- the transported-speed pointwise stress contraction on random divergence-free jets;
- the helical curl eigenvector convention;
- the pair-symmetrized coefficient `s|p|-t|q|` on thousands of random integer triads;
- the exact Q-channel formula;
- the same-spin quadratic radial-gap formula;
- equal-radius opposite-spin P/Q norm formulas;
- exact same-spin equal-radius cancellation.

The checker is a structural verifier only. It is **not** a continuum global-regularity certificate.
