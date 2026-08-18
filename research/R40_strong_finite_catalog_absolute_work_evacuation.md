# R40 — Strong finite-catalog absolute-work evacuation

**Status:** `exact conditional diagonal-extraction theorem / verified-partials target`  
**Depends on:** R25, R28, R30, R38–R39  
**Clay status:** **NOT SOLVED**

R25 proves that pressure work at any one fixed finite output cutoff is absolutely time-integrable. R38 then extracts terminal packets on which high-pass productive work and balanced high-pass action are arbitrarily large throughout a prescribed finite hierarchy. R39 strengthens P/Q synchronization on every prescribed finite output catalog.

R40 makes a different and stronger diagonal conclusion: on the same type of hypothetical singular terminal packets, the **absolute pressure work of each Helmholtz representation inside any prescribed growing finite output catalog can be made arbitrarily small**, while both representations still carry arbitrarily large net positive work beyond the prescribed ceiling.

Thus a singular mechanism compatible with the current proof spine must evacuate productive pressure work to output frequencies faster than every preassigned finite-resolution schedule.

## 1. Modewise work and absolute coefficient bounds

Use the Fourier convention of R39 on `Omega=T^3` of volume `V`:

`fhat(k)=V^{-1} int_Omega f(x) exp(-i k·x) dx`.

Let

`L=omega×u`,

`G=|u|u`,

and define for each nonzero `k`

`w_grad,k=V Re[(Q_k Lhat(k))·conj(Q_k Ghat(k))]`,

`w_sol,k=-V Re[(P_k Lhat(k))·conj(P_k Ghat(k))]`.

The coefficient estimates used in R25/R39 give

`|Lhat(k)| <= V^{-1} ||omega||_2 ||u||_2`,

`|Ghat(k)| <= V^{-1} ||u||_2^2`.

Since `P_k,Q_k` are orthogonal contractions, both exact representations satisfy separately

> `|w_grad,k(t)| <= V^{-1} ||omega(t)||_2 ||u(t)||_2^3`,
>
> `|w_sol,k(t)|  <= V^{-1} ||omega(t)||_2 ||u(t)||_2^3`.

Writing

`E0=sup_(t<T*) ||u(t)||_2`,

we obtain the frequency-independent bound

> `|w_grad,k|+|w_sol,k|`
>
> `<= 2 V^{-1} E0^3 ||omega||_2`.

Unlike R39, no difference `w_grad-w_sol` is taken here: R40 controls the absolute work of the two representations themselves on a finite catalog.

## 2. Finite-catalog absolute-work estimate

Let `F subset Z^3\{0}` be finite and `I=[a,b] subset [a,T*)`. Then

> `int_I sum_(k in F)`
>
> ` (|w_grad,k|+|w_sol,k|) dt`
>
> `<= 2 V^{-1}|F| E0^3 int_I ||omega||_2 dt`.

With the terminal enstrophy tail

`q(a)=int_a^{T*} ||omega(t)||_2^2 dt`,

Cauchy-Schwarz in time yields

> `int_I sum_(k in F)`
>
> ` (|w_grad,k|+|w_sol,k|) dt`
>
> `<= 2 V^{-1}|F| E0^3 |I|^(1/2) q(a)^(1/2)`
>
> `<= 2 V^{-1}|F| E0^3 [(T*-a)q(a)]^(1/2)`.

Since both `T*-a` and `q(a)` tend to zero as `a↑T*`, this can beat the cardinality of **any one prescribed finite catalog** by taking the packet start sufficiently close to the endpoint.

## 3. Arbitrary growing-catalog evacuation on one R38 packet

Assume the same hypothetical singular endpoint used by R28/R30/R38. Prescribe arbitrary sequences

- finite catalogs `F_n`;
- radial ceilings `L_n->infinity`;
- absolute-work tolerances `zeta_n->0`;
- P/Q mismatch tolerances `epsilon_n->0`;
- productive thresholds `M_n->infinity`;
- time-window bounds `delta_n->0`.

Choose `a_n<T*` sufficiently close to `T*` that all R38/R39 start-time requirements hold and also

> `T*-a_n <= delta_n`,

> `2 V^{-1}|F_n|E0^3[(T*-a_n)q(a_n)]^(1/2) <= zeta_n`.

R38 then selects one `b_n in (a_n,T*)` such that on `I_n=[a_n,b_n]`, for every sharp cutoff `K<=L_n`,

`A_grad^K(I_n)>=M_n`,

`A_sol^K(I_n)>=M_n`,

`A_bal^K(I_n)>=M_n`,

and the R38 mismatch is at most `epsilon_n`.

At the same time R40 gives

> `int_(I_n) sum_(k in F_n)`
>
> ` (|w_grad,k|+|w_sol,k|)dt <= zeta_n`.

The packet therefore contains arbitrarily large productive high-frequency work while the two exact pressure-work representations carry vanishing absolute work on the entire prescribed finite catalog.

## 4. Growing Fourier-ball theorem

Take specifically

> `F_n={k in Z^3\{0}: |k|<=L_n}`.

Then

> `int_(I_n) sum_(0<|k|<=L_n)`
>
> ` (|w_grad,k|+|w_sol,k|)dt <= zeta_n -> 0`.

But R38 at the cutoff `K=L_n` simultaneously gives

> `int_(I_n) sum_(|k|>L_n) w_grad,k dt >= M_n`,
>
> `int_(I_n) sum_(|k|>L_n) w_sol,k dt >= M_n`.

Hence the positive Jordan parts satisfy

> `int_(I_n) sum_(|k|>L_n) (w_grad,k)_+ dt >= M_n`,
>
> `int_(I_n) sum_(|k|>L_n) (w_sol,k)_+ dt >= M_n`.

Thus both representations must carry arbitrarily large **positive productive work** outside the prescribed ball while all absolute work inside the ball tends to zero.

Since `L_n` may grow according to any preassigned sequence, the singular packet's productive output scale must outrun every prescribed finite-resolution schedule after the packet start is chosen correspondingly close to `T*`.

## 5. Common-mode evacuation

Let the output-mode common work be

`c_k=(w_grad,k+w_sol,k)/2`.

On the resolved ball,

`|c_k| <= (|w_grad,k|+|w_sol,k|)/2`,

so R40 also gives

> `int_(I_n) sum_(0<|k|<=L_n) |c_k|dt <= zeta_n/2 -> 0`.

Therefore the load-bearing common productive mode identified in R37 is itself evacuated from every prescribed growing finite output prefix.

This is stronger than merely saying that the two representations agree there: their common absolute work there vanishes.

## 6. Relation to R25 and R39

R40 is not a restatement of R25.

- R25: for each **fixed** `K`, low-output pressure work is absolutely integrable on a finite time interval, with a bound growing like the finite mode count.
- R40: for an **arbitrarily growing sequence** of finite catalogs/cutoffs, a diagonal terminal-packet extraction makes the absolute work of both representations on the entire resolved catalog tend to zero, while the exterior productive work tends to infinity.

R40 is also stronger in a different direction than R39.

- R39 controls `|w_grad-w_sol|` on a finite catalog.
- R40 controls `|w_grad|+|w_sol|` there.

Hence after R40, resolved-catalog P/Q mismatch, sign alternation, temporal alternation, and common-mode magnitude are all excluded as the source of the terminal productive divergence.

## 7. What R40 still does not prove

R40 does **not** provide frequency tightness; it proves the opposite necessary behavior under the singular hypothesis: the productive work must escape.

It does not give a quantitative lower relation between the escaping scale and the remaining time `T*-t`, because the diagonal start time may depend arbitrarily on the prescribed catalog size. In particular it does not prove a parabolic law such as `L_n sqrt(T*-a_n)` bounded above or below.

It also does not resolve how the escaping common mode is assembled. At an output mode beyond `L_n`, many R37-admissible helical input pairs may accumulate coherently.

The new live frontier is therefore:

> **derive a scale/time law or rescaled rigidity theorem for the necessarily escaping positive common-mode work, and control the many-triad helical accumulation at the escaping output scale.**

## 8. Verification scope

`verification/check_R40_absolute_work_evacuation.py` checks

- modewise P/Q absolute-work coefficient bounds;
- finite-catalog `L^1_t ell^1_k` estimates;
- arbitrary catalog-size diagonal tolerance selection;
- simultaneous vanishing resolved absolute work and diverging exterior positive work on synthetic R38-compatible packets;
- common-mode resolved evacuation.

A separate fresh verifier reconstructs the coefficient/projection bounds without importing the primary checker.

**R40 is a stronger necessary concentration-at-frequency-infinity theorem under the hypothetical singular endpoint; it is not a global-regularity proof.**
