# R29 — Cutoffwise cumulative cross-representation synchronization

**Status:** `exact structural theorem / dynamic scale-time coupling`  
**Depends on:** R03–R05, R25, R27–R28  
**Clay status:** does not bound the surviving common ultraviolet work; no global regularity conclusion

R28 proves that, near a putative critical `L^3` endpoint singularity, both exact pressure-work representations must carry unbounded net positive work above every fixed Fourier cutoff. RD014 warns that this does not imply shell-by-shell or instantaneous overlap.

R29 identifies the exact defect between the two high-pass representations and proves that this defect is entirely low-frequency and energy-controlled.

Let

`rho=|u|`, `G=rho u`, `L=omega×u`,

and let `P,Q` be the Leray/gradient Helmholtz projectors. For a fixed Fourier cutoff `K`, let `Pi_{<=K}` and `Pi_{>K}` be the orthogonal low/high projectors used in R28. The zero mode causes no issue because `mean(L)=0` on the periodic domain.

Define

`W_grad,>K=<Pi_{>K} QL, Pi_{>K} QG>`,

`W_sol,>K=-<Pi_{>K} PL, Pi_{>K} PG>`.

## 1. Exact high-pass mismatch identity

Because `P` and `Q` are orthogonal complementary projectors commuting with the Fourier cutoff,

`W_grad,>K-W_sol,>K`

`=<Pi_{>K} QL,Pi_{>K} QG>`

` +<Pi_{>K} PL,Pi_{>K} PG>`

`=<Pi_{>K}L,Pi_{>K}G>`.

But pointwise

`L·G=(omega×u)·(|u|u)=0`.

Hence

`<L,G>=0`.

Fourier low/high orthogonality therefore gives

`<Pi_{>K}L,Pi_{>K}G>`

`=-<Pi_{<=K}L,Pi_{<=K}G>`.

Thus the exact synchronization identity is

> `W_grad,>K-W_sol,>K`
>
> `=-<Pi_{<=K}L,Pi_{<=K}G>`.

The right-hand side is a **low-frequency compensator**. No unresolved high-frequency quantity appears in the mismatch.

Similarly,

> `W_grad,<=K-W_sol,<=K`
>
> `=<Pi_{<=K}L,Pi_{<=K}G>`.

Therefore the low- and high-frequency representation defects cancel exactly.

## 2. Energy control of the compensator

For every Fourier mode,

`|Ghat(k)|<=||G||_1=||u||_2^2`,

while

`|Lhat(k)|<=||L||_1<=||omega||_2||u||_2`.

If

`N_K=#{k in Z^3:0<|k|<=K}`,

then Parseval on the finite low set gives

`||Pi_{<=K}G||_2<=sqrt(N_K)||u||_2^2`,

`||Pi_{<=K}L||_2<=sqrt(N_K)||omega||_2||u||_2`.

Consequently

> `|W_grad,>K-W_sol,>K|`
>
> `<=N_K||omega||_2||u||_2^3`.

Let `E0=||u_0||_2`. On every smooth interval the energy inequality yields

`sup_t ||u(t)||_2<=E0`,

and

`2nu int ||omega||_2^2 dt<=E0^2`.

Therefore, for every interval `[a,b]` contained in the smooth lifespan,

> `| int_a^b (W_grad,>K-W_sol,>K) dt |`
>
> `<=N_K E0^4 sqrt((b-a)/(2nu))`.

This estimate is uniform in the location of the interval and depends on its length only through `sqrt(b-a)`.

## 3. Terminal-window synchronization

Suppose a finite maximal time `T*` is approached through the R28 endpoint scenario. For each fixed `K`, define terminal high-pass cumulative works

`A_grad^K(a,T)=int_a^T W_grad,>K dt`,

`A_sol^K(a,T)=int_a^T W_sol,>K dt`.

R29 gives

> `sup_{a<T<T*} |A_grad^K(a,T)-A_sol^K(a,T)|`
>
> `<=N_K E0^4 sqrt((T*-a)/(2nu))`.

Hence

> as `a↑T*`, the two high-pass cumulative work functions become arbitrarily close in **absolute** difference.

This is a genuine scale-time synchronization statement. It is stronger than merely saying that both representations diverge somewhere in the ultraviolet.

## 4. Singular-endpoint consequence: asymptotic common mode

R28 proves that for every fixed `K` and every fixed `a<T*`,

`A_grad^K(a,T)->+infinity`,

`A_sol^K(a,T)->+infinity`

as `T↑T*`.

Since their difference stays bounded — and on terminal windows can be made arbitrarily small — the two divergent cumulative works are asymptotically the same:

> `A_grad^K(a,T)/A_sol^K(a,T) -> 1`

for every fixed `K` and `a<T*`.

Equivalently, define the common-mode and defect variables

`C_K=(W_grad,>K+W_sol,>K)/2`,

`D_K=W_grad,>K-W_sol,>K`.

Then

`W_grad,>K=C_K+D_K/2`,

`W_sol,>K=C_K-D_K/2`,

while `D_K` is exactly the energy-controlled low-frequency compensator from Section 1. Thus the unresolved singular mechanism is no longer two independent productive ultraviolet processes:

> it is one divergent **common ultraviolet pressure-work mode**, plus an integrable low-frequency representation defect.

## 5. Dyadic formulation

For an orthogonal shell partition `{Delta_j}`, write

`w_j^grad=<Delta_j QL,Delta_j QG>`,

`w_j^sol=-<Delta_j PL,Delta_j PG>`,

and

`d_j=<Delta_j L,Delta_j G>`.

Then exactly

> `w_j^grad-w_j^sol=d_j`,

and pointwise orthogonality implies

> `sum_j d_j=0`.

For every fixed shell threshold `J`,

> `sum_{j>J}(w_j^grad-w_j^sol)`
>
> `=-sum_{j<=J} d_j`.

The right side contains only finitely many output shells and is time-integrable by the same energy argument. Hence the two productive high-shell sums are synchronized modulo a finite-output defect even though RD014 permits strong shell-by-shell separation.

## 6. What R29 does not prove

R29 does **not** show:

- `w_j^grad=w_j^sol` for an individual shell;
- simultaneous positivity of the two shell works at each time;
- pointwise-in-time equality of high-pass work;
- a uniform estimate as `K->infinity`;
- finiteness of the common-mode work `C_K`.

RD014 remains fully compatible with R29. The theorem synchronizes the **cumulative tail** of the two exact representations, not their microscopic shell allocation.

## 7. Sharpened frontier after R29

E28 asked whether two productive ultraviolet sequences could remain indefinitely separated in scale/time. R29 answers part of that question:

> above every fixed cutoff, their cumulative signed work cannot separate by more than an energy-controlled low-frequency compensator, and on shrinking terminal windows the mismatch tends to zero.

The remaining problem is therefore sharper:

> **Can the common-mode productive ultraviolet work itself be bounded, cancelled, or forced into a known continuation criterion?**

Promising next mechanisms are now specifically common-mode mechanisms:

1. estimate `C_K` through a commutator retaining the exact pointwise orthogonality `L·G=0`;
2. derive a scale-local flux identity whose boundary term is precisely the low-frequency compensator;
3. connect the common-mode high-pass work to R17 bandwidth production and R24 longitudinal strain;
4. seek concentration-compactness rigidity for a minimal object with divergent common-mode UV work.

R29 does not provide that final bound.

## 8. Verification

`verification/check_R29_cutoffwise_cumulative_synchronization.py` independently constructs smooth real divergence-free periodic velocity fields, reconstructs `L`, `G`, the Helmholtz split and several Fourier cutoffs, and verifies:

- pointwise/global `L·G=0`;
- the exact high-pass mismatch identity;
- the complementary low-pass identity;
- raw low/high defect cancellation;
- the terminal-window and bounded-defect asymptotic algebra.

The continuum proof itself uses only pointwise Lamb/test orthogonality, orthogonal Fourier/Helmholtz decompositions, the finite-mode coefficient bounds already used in R25, Cauchy–Schwarz and the energy inequality.
