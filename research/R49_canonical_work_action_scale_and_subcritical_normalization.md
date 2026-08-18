# R49 — Canonical work-action scale and subcritical productive normalization

**Status:** `exact conditional normalization theorem + primary-source epsilon-regularity interface / not closure`  
**Depends on:** R39–R48, C004  
**Clay status:** **NOT SOLVED**

E48 produces R47-good unit common-work bursts with bounded critical `D_3` action and R48 productive-scale nontriviality, but the minimal positive-work quantile `R_theta` can still be an unstable normalization: the scalar architecture allows temporal mismatch and normalized-IR escape. R49 therefore changes the normalization itself.

The central idea is to normalize by the exact spacetime density that controls the full signed common-work tail.

For an R47-good burst `J`, define

> `X_J = int_J int_(T^3) |u|^2 |grad u|^2 dxdt`,
>
> `Sigma_J = sqrt(2) X_J`,
>
> `K_J = 2 Sigma_J = 2sqrt(2) X_J`.

This scale is not a minimal quantile and does not depend on a discontinuous stopping rule in frequency. It is selected by the physical-space work density itself.

The payoff is that after rescaling by `K_J`, several quantities become simultaneously normalized: the weighted-gradient action is exactly fixed, at least one half-unit of positive common work lies below normalized output frequency one, a work-linked velocity center remains nonzero, a nonzero `L^4` spacetime action survives, and the whole burst has a uniform **subcritical** `L^4_t L^12_x` bound.

The remaining obstruction becomes genuinely temporal: the present estimates do not force the work-linked center or active work layer to lie a fixed normalized parabolic distance from the boundary of the burst. RD028 records this route guard.

## 1. Input from R46–R48

Let `J` be an R47-good last-exit unit common-work burst at parent cutoff `L0`. Write

> `D_J = int_J D_3 dt <= D_* := 28/(3nu)`,
>
> `X_J = int_J int |u|^2|grad u|^2`,
>
> `Sigma_J=sqrt(2)X_J`.

R46 gives the full signed common-work tail

> `T_J(R)=sum_(|k|>R)|b_k(J)| <= Sigma_J/R`,

and unit normalization gives

> `sum_(|k|>L0)b_k(J)=1`,
>
> `Sigma_J >= L0`.

R47 also allows the resolved tolerances to be taken to zero on the terminal diagonal. Denote by `eps_J` the full-work discrepancy, so

> `|int_J W_3 dt - 1| <= eps_J`,
>
> `eps_J -> 0`.

For the uniform lower bounds below it is enough to work after the diagonal has reached `eps_J<=1/2`.

## 2. Canonical work-action frequency

Define

> `K_J := 2sqrt(2) X_J = 2 Sigma_J`.

Because `Sigma_J>=L0`,

> `L0 <= K_J/2`,

and because the absolute tail obeys `T_J(R)<=Sigma_J/R`,

> `T_J(K_J) <= 1/2`.

The total positive Jordan mass above `L0` is at least one, since the signed mass is exactly one. Hence

> `sum_(L0<|k|<=K_J) (b_k(J))_+ >= 1/2`.

Thus the canonical scale captures a **fixed positive amount of productive common work** below normalized output frequency one. No minimal-quantile continuity assumption is used.

## 3. Exact normalization of the weighted work density

Rescale at length `r_J=K_J^-1` around any chosen center `(x_J,t_J)`:

> `v_J(y,s)=K_J^-1 u(x_J+K_J^-1 y, t_J+K_J^-2 s)`.

The rescaled torus has volume `V_J=K_J^3 V`, where `V` is the volume of the canonical torus.

The spacetime functional

> `X[u;J]=int_J int |u|^2|grad u|^2`

has one power of frequency under Navier–Stokes scaling. Therefore

> `X[v_J;J'_J]=X_J/K_J=1/(2sqrt(2))`.

This is **exact**, not merely bounded above or below.

R48's high-amplitude set

> `H_J={|u|>=B_J/2}`,
>
> `B_J=X_J/D_J`,

carries at least `X_J/2`. Hence its image `H'_J` satisfies

> `int_(H'_J)|v_J|^2|grad v_J|^2 >= 1/(4sqrt(2))`.

Moreover

> `B_J/K_J=1/(2sqrt(2)D_J) >= 3nu/(56sqrt(2))`,

so a center chosen from `H_J` obeys

> `|v_J(0,0)| >= 3nu/(112sqrt(2))`.

Thus the canonical normalization is nontrivial both pointwise and in a scale-invariant spacetime measure.

## 4. A nonzero normalized `L^4` spacetime action

The full critical pressure work has the exact common-mode form

> `W_3=(1/2)<L,(Q-P)G>`,
>
> `L=omega x u`, `G=|u|u`.

Since `Q-P` is an `L^2` isometry,

> `|W_3| <= (1/2)||L||_2||G||_2`.

Pointwise,

> `||L||_2^2 <= int |u|^2|omega|^2 <= 2 X(t)`,

while

> `||G||_2=||u||_4^2`.

Therefore

> `|W_3(t)| <= 2^(-1/2) X(t)^(1/2) ||u(t)||_4^2`.

Cauchy–Schwarz in time and `|int_JW_3|>=1-eps_J` yield

> `int_J ||u||_4^4 dt >= 2(1-eps_J)^2/X_J`.

Under the canonical rescaling the `L^4_{t,x}` action gains the factor `K_J`, hence

> `int_(J'_J) ||v_J||_4^4 ds >= 4sqrt(2)(1-eps_J)^2`.

In particular, once `eps_J<=1/2`,

> `int_(J'_J) ||v_J||_4^4 ds >= sqrt(2)`.

So the normalized sequence cannot vanish in global spacetime `L^4`.

## 5. Uniform subcritical `L^4_t L^12_x` control

Let

> `f_J=|v_J|^2`.

On every dilate of the fixed periodic torus, the scale-invariant Sobolev–Poincare estimate gives a constant `C_T`, independent of `K_J`, such that

> `||f_J||_6^2`
>
> `<= C_T ||grad f_J||_2^2`
>
> ` + C_T V_J^(-5/3)||f_J||_1^2`.

This follows by applying homogeneous `H^1 -> L^6` to `f_J-mean(f_J)` and estimating the constant mode separately.

The chain rule gives

> `|grad |v_J|^2|^2 <= 4|v_J|^2|grad v_J|^2`.

Hence

> `int_(J'_J)||grad f_J||_2^2 ds`
>
> `<=4X_J/K_J=sqrt(2)`.

For the constant mode, the energy inequality gives

> `||v_J(s)||_2^2 <= K_J E0^2`.

Since `V_J=K_J^3V` and `ds=K_J^2dt`, the integrated mean-mode contribution is bounded by

> `E0^4 |J|/(K_J V^(5/3))`.

Along the terminal diagonal `|J|->0` and `K_J>=2L0->infinity`, so this term tends to zero. Therefore

> `int_(J'_J)||v_J||_12^4 ds`
>
> `<= C_T[sqrt(2)+o(1)]`.

This is the new load-bearing gain. The pair `(p,q)=(4,12)` is strictly subcritical:

> `2/p+3/q = 1/2+1/4 = 3/4 < 1`.

Unlike E48's critical `L^3_tL^9_x` bound, the canonical R49 normalization therefore carries a uniform **subcritical Serrin-space action**.

## 6. Uniform smallness of the velocity CKN functional at sufficiently small interior radii

Let `Q_r(z,s)` be a parabolic cylinder fully contained in the rescaled burst and torus. By spatial Holder,

> `int_(B_r)|v_J|^3`
>
> `<= |B_r|^(3/4)||v_J||_12^3`.

Holder in time over an interval of length `r^2` then gives

> `r^(-2) int_(Q_r)|v_J|^3`
>
> `<= C_B r^(3/4)`
>
> `    * [int_(J'_J)||v_J||_12^4 ds]^(3/4)`.

The right-hand side tends to zero as `r->0`, **uniformly in the R49 sequence**, provided the cylinder lies inside the normalized time interval.

A primary-source one-scale epsilon-regularity theorem of Wang–Wu–Zhou (arXiv:1811.09927, Theorem 1.1) states that for suitable weak solutions, for every `delta>0`, sufficiently small `int_(Q_1)|u|^(5/2+delta)` implies boundedness on a smaller cylinder. Choosing `delta=1/2` and rescaling `Q_r` to unit size, the R49 bound supplies exactly the required small scale-invariant `L^3` velocity integral on every sufficiently small **time-interior** cylinder. Fixed positive viscosity is normalized in the standard deterministic way; constants may depend on `nu`.

This theorem is imported only as an epsilon-regularity interface. R49 does not claim originality for it and does not reproduce its proof by script. The source/scope interface is pinned in

> `sources/R49_wang_wu_zhou_epsilon_regular_without_pressure.md`.

## 7. What this changes about RD027 spatial fragmentation

R49 does **not** prove global spatial tightness of the weighted-gradient measure on the expanding torus. However, it changes the obstruction materially:

- the total normalized `X` action is fixed exactly;
- a fixed amount of normalized `L^4` spacetime mass survives;
- a work-linked nonzero center survives;
- the whole normalized burst has a subcritical `L^4_tL^12_x` budget;
- any sufficiently small parabolic cylinder that lies a fixed normalized time distance inside the burst satisfies a uniform epsilon-regularity smallness condition.

Thus a new singular micro-concentration cannot be generated **inside a time-interior productive-scale cylinder** merely by the static fragmentation mechanism of RD027. To defeat compactness, the active work/center can still crowd a temporal boundary, the normalized interval can collapse, or the productive work can migrate toward normalized frequency zero.

The surviving obstruction is therefore more dynamic and more precise than E48's generic spatial-fragmentation warning.

## 8. RD028 — why temporal interiority is still not a corollary

R49's integrated bounds do not force a fixed parabolic time margin. RD028 constructs abstract normalized action profiles (not Navier–Stokes trajectories) with

- unit monotone work;
- exact canonical `X` action;
- nonzero `L^4` spacetime action;
- bounded subcritical `L^4_tL^12_x` action;
- bounded `D_3` action;
- a nonzero center proxy and at least half a unit of productive band work;

while either

> the entire active normalized interval has length `tau_n->0`,

or

> the nominal burst length tends to infinity but every nontrivial action is packed into a boundary layer of length `tau_n->0`.

Therefore no scalar/envelope argument through R49 can provide the temporal interiority needed by Section 6. Actual Navier–Stokes orbit dynamics is still required.

## 9. Canonical post-R49 frontier

R49 reduces the compactness problem to a narrower dynamic alternative:

> **Either prove that a fixed fraction of the unit productive work and the work-linked center persist for a fixed positive amount of `K_J^2`-normalized time, or prove that temporal collapse / normalized-IR migration itself consumes a scale-critical Navier–Stokes cost that cannot occur on infinitely many R47 bursts.**

Duhamel/heat propagation, local-energy propagation tied to the work density, dissipation-wavenumber control, and the upstream R37 many-body helical geometry remain the leading candidates.

R49 does not prove temporal alignment, a compact ancient limit preserving common work, a Liouville contradiction, or global regularity.

## 10. Verification scope

`verification/check_R49_canonical_work_action_subcritical_normalization.py` checks the canonical scale algebra, positive-work capture, normalized weighted action, work-linked amplitude, `L^4` lower action, large-torus mean scaling, subcritical `L^4_tL^12_x` budget, local `r^(3/4)` velocity-smallness exponent, and Navier–Stokes scaling.

`verification/fresh_verify_e49_physical_work_action.py` independently reconstructs smooth divergence-free trigonometric fields and Helmholtz channels, testing the exact common-mode identity and load-bearing physical inequalities without importing the primary checker.

`verification/check_RD028_R49_temporal_boundary_escape.py` verifies the temporal-boundary route guard.

**R49 is a verified-partial candidate until independent and repository-wide gates pass. It is not a solution of the Navier–Stokes Millennium Problem.**
