# R41 — Synchronized unit common-work burst extraction

**Status:** `exact conditional extraction theorem / normalized terminal-burst reduction`  
**Depends on:** R20, R28–R30, R38–R40  
**Clay status:** **NOT SOLVED**

R38–R40 force a hypothetical singular endpoint to carry arbitrarily large productive pressure work beyond every prescribed growing output cutoff while the resolved finite catalog becomes absolutely negligible.  R41 converts that unbounded terminal work into a sequence of **normalized unit-work sub-bursts** extracted from the actual hypothetical Navier–Stokes trajectory.

This is designed for the next concentration/rigidity stage: instead of studying packets whose work tends to infinity, one obtains many disjoint subintervals on which the common high-pass work is exactly one, the two Helmholtz representations are individually synchronized, resolved work is negligible, and both the time length and the unweighted enstrophy cost can be made arbitrarily small for a large fraction of the bursts.

## 1. Parent packet

Take an R40 terminal packet

`I=[a,b] subset [0,T*)`

with a sharp output cutoff `L` such that

> `A_grad^L(I) = int_I W_grad,>L(t) dt >= M`,
>
> `A_sol^L(I)  = int_I W_sol,>L(t) dt >= M`,

where `M>2`.

Assume the corresponding R39 resolved-catalog mismatch and R40 resolved absolute-work bounds on the ball `0<|k|<=L` are

> `int_I sum_(0<|k|<=L) |d_k(t)| dt <= eta`,

and

> `int_I sum_(0<|k|<=L)`
>
> ` (|w_grad,k(t)|+|w_sol,k(t)|) dt <= zeta`.

Let

> `C_L(t) = [W_grad,>L(t)+W_sol,>L(t)]/2`

be the high-pass common productive work density.

Then

> `int_I C_L(t)dt >= M`.

On the smooth preterminal interval, `C_L` is integrable and its indefinite integral is continuous.

## 2. Exact unit-work hitting intervals

Define

`F(t)=int_a^t C_L(s)ds`.

Let

> `N=floor(M)`.

Since `F(a)=0` and `F(b)>=M>=N`, continuity gives first hitting times

> `tau_j = inf{t in [a,b]: F(t)=j}`,

for `j=0,1,...,N`, with `tau_0=a` and

`a=tau_0 < tau_1 < ... < tau_N <= b`.

For the disjoint intervals

> `J_j=[tau_(j-1),tau_j]`, `j=1,...,N`,

one has exactly

> `int_(J_j) C_L(t)dt = 1`.

No positivity or monotonicity of `C_L(t)` is assumed; the construction uses first hitting of successive levels of the signed cumulative common work.

## 3. Each unit burst synchronizes the two high-pass representations

For every time `t`, the full representation difference is

`W_grad(t)-W_sol(t)=<L,G>=0`,

because `L=omega×u` is pointwise perpendicular to `G=|u|u`.

Therefore the high-pass mismatch is the negative of the resolved mismatch:

> `W_grad,>L-W_sol,>L`
>
> `= - sum_(0<|k|<=L) d_k`.

For every subinterval `J subset I`, R39's product-measure total-variation bound gives

> `|int_J (W_grad,>L-W_sol,>L)dt| <= eta`.

Applying this to each `J_j` and using the exact common-work normalization,

> `int_(J_j) W_grad,>L dt = 1 + delta_j/2`,
>
> `int_(J_j) W_sol,>L  dt = 1 - delta_j/2`,

with

> `|delta_j| <= eta`.

Hence if `eta->0`, **every** unit common-work burst carries asymptotically one unit of net productive work in each exact Helmholtz representation separately.

## 4. Resolved absolute work is negligible on every unit burst

R40 controls a nonnegative quantity on the parent packet.  Therefore every subinterval inherits

> `int_(J_j) sum_(0<|k|<=L)`
>
> ` (|w_grad,k|+|w_sol,k|)dt <= zeta`.

Thus none of the unit work can be supplied by a large cancellation hidden in the resolved catalog when `zeta` is small.  The burst is genuinely an ultraviolet common-work event relative to the prescribed cutoff.

## 5. Many unit bursts have vanishing duration and enstrophy cost

Let

`ell=|I|`

and

`q_I=int_I ||omega(t)||_2^2 dt`.

The `J_j` are disjoint, so

> `sum_(j=1)^N |J_j| <= ell`,

and

> `sum_(j=1)^N int_(J_j)||omega||_2^2dt <= q_I`.

By counting/Markov:

- fewer than `N/4` intervals can satisfy `|J_j|>4 ell/N`;
- fewer than `N/4` intervals can satisfy

  `int_(J_j)||omega||_2^2dt > 4 q_I/N`.

Therefore at least

> `N/2`

of the unit-work bursts satisfy **both**

> `|J_j| <= 4 ell/N`,

and

> `int_(J_j)||omega||_2^2dt <= 4 q_I/N`.

This conclusion uses no independence assumption between work, duration and dissipation.

## 6. Diagonal singular sequence

Now use the freedom in R38–R40 to prescribe

`L_n->infinity`,

`M_n->infinity`,

`eta_n->0`,

`zeta_n->0`,

and parent-window bounds `delta_n->0`.

Choose the corresponding parent packets `I_n` and write

`N_n=floor(M_n)`.

The terminal enstrophy tail also gives

`q_n=int_(I_n)||omega||_2^2dt ->0`.

R41 then supplies at least `N_n/2` good unit bursts in each parent packet.  Choosing one good burst `J_n` from each parent gives a sequence such that

> `int_(J_n) C_(L_n) dt = 1`,

> `int_(J_n) W_grad,>L_n dt = 1+o(1)`,

> `int_(J_n) W_sol,>L_n  dt = 1+o(1)`,

> `int_(J_n) sum_(0<|k|<=L_n)`
>
> ` (|w_grad,k|+|w_sol,k|)dt ->0`,

> `|J_n| <= 4 delta_n/N_n ->0`,

and

> `int_(J_n)||omega||_2^2dt <= 4 q_n/N_n ->0`.

Thus a hypothetical singular endpoint generates a canonical sequence of **unit critical-work ultraviolet bursts whose unweighted viscous cost and duration vanish**.

## 7. High-input consequence

Because the unit work is supported in output frequencies `|k|>L_n`, the high-pass Lamb force cannot vanish identically on `J_n`.  By R20, an output Lamb mode above `L_n` cannot be generated by two velocity inputs both confined below `L_n/2`.

Hence each R41 burst necessarily involves genuine velocity input at frequencies above `L_n/2` somewhere in the interaction producing its productive Lamb output.  R41 does not convert this support fact into a quantitative norm lower bound.

## 8. Relation to RD020

RD020 gives an abstract lacunary scaling-budget countermodel in which each increasingly fine burst contributes `O(1)` critical work at vanishing energy/enstrophy cost.  R41 shows that **if the actual Navier–Stokes singular endpoint exists within this proof spine, a normalized sequence with the same qualitative budget signature can be extracted from the true trajectory itself**.

The difference is decisive:

- RD020 says energy accounting cannot exclude such a cascade;
- R41 identifies the exact normalized object that a genuine PDE rigidity theorem must now exclude.

## 9. What R41 does not prove

R41 does not establish a canonical spatial center, a canonical active frequency comparable to `L_n`, a parabolic relation between frequency and burst duration, compactness after rescaling, or a nontrivial ancient/minimal limit.

The productive work may still live far above the chosen cutoff `L_n`, and many R37-admissible helical input pairs may coherently build one output mode.

The live frontier after R41 is therefore:

> **choose an intrinsic active scale/center for each unit burst and prove enough compactness or many-body helical depletion to rule out a normalized limit carrying one unit of positive common pressure work at vanishing unweighted dissipation cost.**

That is a substantially more concrete rigidity target than an unnormalized divergent terminal tail.

## 10. Verification scope

`verification/check_R41_unit_common_work_bursts.py` verifies the first-hitting construction, exact common/mismatch algebra, inherited resolved-work bounds, and the simultaneous counting lemma for duration/enstrophy over large randomized signed cumulative-work paths.

A fresh verifier independently reconstructs the extraction using piecewise-linear signed work traces with strong backtracking.

**R41 is a conditional normalized-burst extraction theorem, not a Navier–Stokes global-regularity proof.**
