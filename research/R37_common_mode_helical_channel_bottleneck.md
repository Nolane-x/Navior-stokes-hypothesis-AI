# R37 — Common-mode helical/Helmholtz channel bottleneck

**Status:** `exact structural theorem / frontier correction / not claimed novel`  
**Depends on:** R14–R16, R24, R27, R29, R33–R36  
**Clay status:** verified partial structure only; no arbitrary-data summability theorem is proved

E35–E36 concentrated on the smooth P/Q representation mismatch. That was useful for synchronization, but it is not by itself the load-bearing singular quantity: R29/R34 already allow the two productive high-frequency pressure-work representations to diverge together while their difference is integrable or asymptotically negligible.

R37 corrects that emphasis. It isolates the **common productive mode** exactly, inserts the helical decomposition into the physical Lamb source feeding that mode, and computes closed formulas for the P/Q norms of every non-collinear helical pair. The result narrows the full-strength balanced high-high source to explicit spin/radial/angular mechanisms.

Let

`L=omega×u`, `G=rho u`, `rho=|u|`,

and let `P,Q` be the solenoidal/gradient Helmholtz projections. Let `M,H` be real even self-adjoint smooth Fourier multipliers satisfying

> `M^2+H^2=I`.

They commute with `P,Q` and derivatives.

## 1. The load-bearing object is the common mode

Define

`W_grad,H=<HQL,HQG>`,

`W_sol,H=-<HPL,HPG>`.

Introduce the Helmholtz reflection

> `J=Q-P=2Q-I`.

`J` is a self-adjoint `L^2` isometry/involution on nonzero modes. Set

`C_H=(W_grad,H+W_sol,H)/2`,

`D_H=W_grad,H-W_sol,H`.

Orthogonality gives exactly

> `2C_H=<HL,JHG>`,

> `D_H=<HL,HG>`.

R33 gives `D_H=-D_M`, with `D_M=<M^2L,G>`.

Therefore summability or smallness of the representation mismatch does **not** imply smallness of `C_H`. R29/R34 allow the singular endpoint scenario, if it occurs within this spine, to carry divergent positive common-mode work while the mismatch is negligible. From E37 onward the primary object to exclude is `C_H`; the commutator is a secondary synchronization constraint.

## 2. Exact stress representations

Let

> `T=u tensor u-(rho^2/2)I`.

For divergence-free `u`,

> `L=div T`.

Self-adjointness and commutation give

> `C_H=-(1/2)<HT,H grad(JG)>`.

There is also an exact dual representation of the R33 defect. Since `<L,G>=0` and `M^2=I-H^2`,

`D_M=<M^2L,G>=-<H^2L,G>`.

Using `L=div T`,

> `D_M=<HT,H grad G>`.

So the same mismatch that appears as a low-filter commutator also appears exactly as a high-filter stress/test-gradient pairing.

## 3. Transported-speed scalar in the stress geometry

Let `q_amp=div(rho u)=u·grad rho`, as in R24. Direct pointwise algebra gives

> `T:grad G=(3/2)rho^2 q_amp`.

Indeed `grad G=rho grad u+u tensor grad rho`; contraction with `u tensor u-(rho^2/2)I`, using `div u=0`, leaves `(3/2)rho^2 u·grad rho`.

Moreover

`(3/2)rho^2 u·grad rho=(1/2)u·grad(rho^3)`,

so the full spatial integral vanishes. The filtered defect measures failure of this exact transported-speed cancellation after scale separation, not a generic stress product.

## 4. Exact pair-symmetrized helical Lamb formula

For nonzero mode `r`, decompose

`uhat(r)=uhat_+(r)+uhat_-(r)`

with

`i r×uhat_s(r)=s|r|uhat_s(r)`, `s in {+1,-1}`.

For `k=p+q`, pairing ordered convolution terms `(p,q)` and `(q,p)` gives

> `Lhat(k)`
>
> `=(1/2) sum_(p+q=k) sum_(s,t=+-1)`
>
> ` (s|p|-t|q|)[uhat_s(p)×uhat_t(q)]`.

Thus same-spin pairs carry the radial difference `|p|-|q|`, whereas opposite-spin pairs carry the radial sum `|p|+|q|`. Same-spin equal-radius pairs vanish exactly at the physical Lamb-source level.

## 5. The common mode inherits the helical coefficient

By Parseval, up to the fixed Fourier-volume normalization,

> `C_H`
>
> `=(1/4) Re sum_k h_K(k)^2`
>
> ` sum_(p+q=k) sum_(s,t)`
>
> ` (s|p|-t|q|)`
>
> ` [uhat_s(p)×uhat_t(q)]`
>
> ` ·conjugate(J_k Ghat(k))`.

So the helical cancellation sits **inside the actual common productive mode** that survives R29/R34; it is not only a norm bound on `L`.

## 6. Closed P/Q formulas for every non-collinear helical pair

Assume `p,q` are non-collinear and write

`a=|p|`, `b=|q|`, `c=|k|`,

`mu=(p·q)/(ab)=cos(theta)`,

`n=(p×q)/|p×q|`.

Choose the common-plane helical basis

> `h_s(r)=[n+i s(rhat×n)]/sqrt(2)`, `r=p,q`.

Then `i r×h_s(r)=s|r|h_s(r)` and

> `h_s(p)×h_t(q)`
>
> `=(i/2)(t qhat-s phat)`
>
> ` -(st/2)sin(theta)n`.

For the pair-symmetrized unit-amplitude source

`F_st=(s a-t b)h_s(p)×h_t(q)`,

the gradient projection is

> `Q_k[h_s(p)×h_t(q)]`
>
> `=(i/2c)[t(b+a mu)-s(a+b mu)] khat`.

The resulting channel norms have closed forms.

### 6.1 Same spin `t=s`

> `|Q_k F_ss|`
>
> `=((a-b)^2(1-mu))/(2c)`,

> `|P_k F_ss|`
>
> `=(|a-b| sin(theta)/2)`
>
> ` *sqrt(1+(a+b)^2/c^2)`.

Hence the **gradient** channel has a quadratic radial-gap factor, while the solenoidal channel has a linear radial-gap factor. If `a=b`, the whole same-spin pair is exactly zero.

### 6.2 Opposite spin `t=-s`

> `|Q_k F_(s,-s)|`
>
> `=((a+b)^2(1+mu))/(2c)`,

> `|P_k F_(s,-s)|`
>
> `=((a+b)sin(theta)/2)`
>
> ` *sqrt(1+(a-b)^2/c^2)`.

For the important equal-radius case `a=b`, these simplify to

> `|Q_k F_(s,-s)|=c`,

> `|P_k F_(s,-s)|=c sin(theta/2)`.

Thus equal-radius opposite-spin pairs retain a full gradient channel, but the solenoidal channel is depleted linearly when the two input wavevectors become nearly collinear.

The formulas are invariant in norm under independent helical phase choices; the common-plane convention only fixes a convenient representative.

## 7. Direct interface with the balanced P/Q obstruction

R27/R30/R34 force the pointwise weaker Helmholtz Lamb channel to accumulate non-summable critical action in the singular scenario. R37 therefore rules out several pair-level geometries as standalone full-strength balanced mechanisms:

1. **same-spin equal shell:** exact zero;
2. **same-spin near-equal shell:** radial-gap depletion, with quadratic suppression in `Q`;
3. **opposite-spin near-collinear equal shell:** `P` suppression by `sin(theta/2)`.

The maximally dangerous narrow-shell pair sector is consequently centered on

> **opposite-spin, non-collinear, active-scale interactions**,

while substantial radial dispersion supplies the alternative same-spin route.

This is strictly sharper than the E36 label “comparable high-high”: the surviving pair mechanism must carry a quantitative **spin/radial/angular conflict** compatible with both Helmholtz channels.

## 8. Accumulation is the remaining mathematical obstruction

R37 is pairwise algebra. It does **not** justify

`min(||sum F_P||,||sum F_Q||)`

being bounded by a sum of pairwise minima. Many depleted interactions can accumulate coherently, and different triads can populate P and Q separately.

Therefore R37 does not prove spacetime summability of `C_H` or of the balanced action.

The load-bearing next theorem must control accumulation of

- opposite-spin/non-collinear annular interactions;
- radial-dispersive same-spin interactions;

in a scale-critical spacetime quantity, or prove that R31 terminal packets cannot maintain the required spin/radial/angular geometry under rescaling.

## 9. Literature interface

Lerner–Vigneron diagonalize curl into spin-definite components and prove constraints showing that a hypothetical finite-time blow-up cannot be reduced to growth of only one spin sector. R37 is consistent with that baseline: the most dangerous narrow-shell pair mechanism here is explicitly cross-spin.

Primary source:

- J. Lerner, N. Vigneron, *On some properties of the curl operator and their consequences for the Navier–Stokes system*, arXiv:2203.07950.

The formulas above are proved directly in this repository and are not claimed as a novelty statement relative to the broader helical-triad literature.

## 10. Verification scope

`verification/check_R37_common_mode_helical_bottleneck.py` checks the common-mode reflection identity, dual stress identity, transported-speed stress contraction, helical eigenvector convention, pair-symmetrized coefficient, exact Q formula, full same/opposite-spin P/Q norm formulas, and equal-shell special cases across large random and structured families.

The verifier is structural only. It is **not** a continuum global-regularity certificate.
