# R34 — Smooth common-mode productive work and balanced high-filter action escape

**Status:** `exact conditional reduction / smooth-filter singular-obstruction theorem`  
**Depends on:** R01, R06, R27–R30, R33, RD015  
**Clay status:** does not bound the surviving smooth commutator/common mode; no global regularity conclusion

R33 replaces the sharp-cutoff synchronization defect by an exact smooth square-partition commutator. R34 proves that this smooth redesign is not merely representational: the same singular endpoint mechanism must become productive and balanced in the smooth high-filter sector.

Let

`L=omega×u`, `G=|u|u`, `U=||u||_(3/2)`.

Choose real even self-adjoint Fourier multipliers `M_K,H_K` satisfying

`M_K^2+H_K^2=I`,

`|m_K|<=1`, `|h_K|<=1`,

with `m_K(0)=1`, `h_K(0)=0`, and with `m_K` compactly supported in

`|k|<=cK`

for a fixed profile constant `c>1`.

A smooth cosine/sine square partition as in R33 satisfies these conditions.

## 1. Smooth low-filter work is energy controlled

Because `M_K` has finite Fourier support and `|m_K|<=1`, the same coefficient bounds as R25 give

`||M_K G||_2<=sqrt(N_{cK})||u||_2^2`,

`||M_K L||_2<=sqrt(N_{cK})||omega||_2||u||_2`.

Helmholtz projection is a modewise `L^2` contraction, so the same bounds hold for `M_KQG`, `M_KQL`, `M_KPG`, `M_KPL`.

Hence both smooth low-filter pressure works satisfy

> `|W_grad,M|, |W_sol,M|`
>
> `<=B_K^M(t)`
>
> `:=N_{cK}||omega||_2||u||_2^3`.

For every finite smooth interval `[0,T]`,

> `int_0^T B_K^M dt`
>
> `<=N_{cK}E0^4 sqrt(T/(2nu))<infinity`.

Thus replacing a sharp cutoff by the smooth square partition preserves the finite-low-output property.

## 2. Smooth high-filter productive work must diverge

R33 gives exact decompositions

`W_3=W_grad,M+W_grad,H`,

`W_3=W_sol,M+W_sol,H`.

If the critical endpoint quantity `||u||_3^3` diverges at a finite maximal time `T*`, R28's balance argument gives

`int_0^T W_3 dt -> +infinity`.

Since both low smooth terms are absolutely integrable, for every fixed finite `K`,

> `int_0^T W_grad,H dt -> +infinity`,
>
> `int_0^T W_sol,H dt -> +infinity`

as `T↑T*`.

Therefore both smooth exact representations remain productively ultraviolet/high-filter.

## 3. High-filter test fields retain the R06/R27 diffusion control

Because `|h_K|<=1`, `H_K` is an `L^2` contraction.

R06 gives

`||QG||_2<=C_g sqrt(U D_3)`,

so

> `||H_KQG||_2<=C_g sqrt(U D_3)`.

R27 gives

`||G-mean(G)||_2<=C_s sqrt(U D_3)`.

Since `h_K(0)=0`,

`H_KPG=H_KP(G-mean G)`,

and therefore

> `||H_KPG||_2<=C_s sqrt(U D_3)`.

The constants are independent of `K` because only `L^2` contraction is used.

## 4. Smooth balanced high-filter continuation criterion

Define

`p_K^H=||H_KPL||_2`,

`q_K^H=||H_KQL||_2`.

The gradient decomposition gives

`|W_3|<=B_K^M+C_g sqrt(U D_3) q_K^H`,

while the solenoidal decomposition gives

`|W_3|<=B_K^M+C_s sqrt(U D_3) p_K^H`.

Let

`C_0=max(C_g,C_s)`.

Taking the better valid representation at each time,

> `|W_3|`
>
> `<=B_K^M+C_0 sqrt(U D_3)`
>
> ` * min(p_K^H,q_K^H)`.

Young's inequality gives

> `|W_3|`
>
> `<=B_K^M +(nu/2)D_3`
>
> ` +(C_0^2/(2nu)) U`
>
> `   *min((p_K^H)^2,(q_K^H)^2)`.

Define

> `A_bal,H^K(T)`
>
> `=int_0^T U(t)`
>
> ` min(`
>
> `  ||H_KP(omega×u)||_2^2,`
>
> `  ||H_KQ(omega×u)||_2^2`
>
> ` ) dt`.

Then finite `A_bal,H^K(T)` bounds the same critical `L^3` endpoint quantity, up to the already integrable low-filter term.

Consequently, within the same endpoint continuation framework as R27/R30, a finite-time singularity must satisfy

> `A_bal,H^K(T*)=infinity`

for **every fixed smooth scale `K`**.

## 5. Smooth high-filter representation mismatch is the R33 commutator

R33 proves

`W_grad,H-W_sol,H`

`=-< [M_K^2,C_u]omega,G>`,

where

`C_u omega=omega×u`.

The same low-filter finite-mode bound gives absolute time integrability of this mismatch for fixed `K`; R32-type improvements may be pursued using smooth multiplier theory without invoking the sharp-ball shortcut rejected in RD015.

Thus the singular high-filter mechanism has the form

> **divergent common productive work**
>
> `+` **divergent balanced minority high-filter action**
>
> `+` **a smooth commutator representation defect**.

The commutator is now load-bearing: controlling it and the common mode at critical scale would directly constrain the singularity obstruction.

## 6. Relation to sharp R29/R30

R34 does not replace the sharp results. The two frameworks have complementary strengths.

Sharp cutoffs provide:

- exact disjoint-shell localization;
- direct finite-output statements;
- R31 diagonal packets.

Smooth square partitions provide:

- exact bilinear decomposition through `M^2+H^2=I`;
- legitimate smooth-kernel/commutator interfaces;
- no need to assume a non-`L^2` sharp-ball multiplier bound.

A future proof may transfer information between them, but every such transfer must track its scale constants.

## 7. New harmonic-analysis bottleneck

After R34, the surviving obstruction may be attacked entirely in the smooth framework:

> prove that no arbitrary smooth Navier–Stokes trajectory can sustain simultaneously
>
> 1. divergent `A_bal,H^K` for every fixed `K`;
> 2. divergent positive common high-filter pressure work;
> 3. only a commutator-sized P/Q representation defect.

The exact commutator to control is

`<[M_K^2,C_u]omega,|u|u>`.

A useful estimate must exploit more than the naive first kernel moment, because the energy-level Hölder allocation does not by itself pair the resulting `L^1` commutator with `|u|u`.

## 8. Verification

`verification/check_R34_smooth_highfilter_escape.py` verifies:

- square-partition low/high work algebra;
- finite-support low-filter domination;
- high-filter `L^2` contraction;
- adaptive weaker-channel algebra;
- singular-endpoint finite-low/divergent-total logic.

It is paired with R33's independent physical-grid reconstruction of the smooth commutator identity.
