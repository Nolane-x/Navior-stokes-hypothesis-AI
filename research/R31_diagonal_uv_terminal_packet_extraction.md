# R31 — Diagonal ultraviolet terminal-packet extraction

**Status:** `exact conditional extraction theorem / compactness-ready corollary`  
**Depends on:** R28–R30  
**Clay status:** does not produce a contradiction or compactness limit; no global regularity conclusion

R29 synchronizes the two high-pass pressure-work representations above every fixed cutoff modulo a low-frequency compensator. R30 proves that the balanced minority high-pass Lamb action must also diverge above every fixed cutoff at a singular endpoint.

The constants in R29 are not uniform as `K->infinity`, because the finite-mode factor `N_K` grows. R31 shows that this does **not** prevent a diagonal ultraviolet extraction: the terminal time window may be shrunk together with the cutoff so that the representation mismatch becomes arbitrarily small while all three singular quantities remain arbitrarily large.

Let

`E0=||u_0||_2>0`,

and assume a finite maximal endpoint `T*` satisfying the R28/R30 singular scenario.

For fixed `K`, define

`A_grad^K(a,T)=int_a^T W_grad,>K dt`,

`A_sol^K(a,T)=int_a^T W_sol,>K dt`,

and

`A_bal^K(a,T)`

`=int_a^T ||u||_(3/2)`

` min(`

`   ||Pi_{>K}P(omega×u)||_2^2,`

`   ||Pi_{>K}Q(omega×u)||_2^2`

` ) dt`.

## 1. Every terminal subinterval still carries the divergence

R28 gives, for every fixed finite `K`,

`A_grad^K(0,T)->+infinity`,

`A_sol^K(0,T)->+infinity`

as `T↑T*`.

R30 gives

`A_bal^K(0,T)->+infinity`.

For every `a<T*`, the solution is smooth on `[0,a]`; hence all three corresponding quantities are finite on `[0,a]`.

Subtracting this finite compact-time contribution shows that for every `a<T*`,

> `A_grad^K(a,T)->+infinity`,
>
> `A_sol^K(a,T)->+infinity`,
>
> `A_bal^K(a,T)->+infinity`

as `T↑T*`.

Thus none of the three divergences can be stored away from the terminal time.

## 2. Quantitative synchronization-window choice

R29 proves that on every interval `[a,b]`,

`|A_grad^K(a,b)-A_sol^K(a,b)|`

`<= N_K E0^4 sqrt((b-a)/(2nu))`.

Fix any tolerance `epsilon>0`. If

> `delta <= 2nu epsilon^2 /(N_K^2 E0^8)`,

then every subinterval `[a,b]` with

`T*-delta <= a < b < T*`

satisfies

> `|A_grad^K(a,b)-A_sol^K(a,b)| <= epsilon`.

Therefore the representation mismatch can be made arbitrarily small by moving sufficiently close to the terminal time, even for a large fixed cutoff.

## 3. Diagonal extraction across `K->infinity`

Let

`K_n -> infinity`,

`epsilon_n -> 0`,

`M_n -> infinity`

be arbitrary prescribed sequences.

For each `n`, choose

`delta_n>0`

such that

> `delta_n <= min(`
>
> `  T*/2,`
>
> `  2nu epsilon_n^2 /(N_{K_n}^2 E0^8)`
>
> `)`.

Set

`a_n=T*-delta_n`.

By Section 1, all three cumulative quantities from `a_n` diverge as the upper endpoint approaches `T*`. Hence one may choose a finite

`b_n in (a_n,T*)`

so close to `T*` that simultaneously

> `A_grad^{K_n}(a_n,b_n) >= M_n`,
>
> `A_sol^{K_n}(a_n,b_n) >= M_n`,
>
> `A_bal^{K_n}(a_n,b_n) >= M_n`.

Section 2 guarantees at the same time

> `|A_grad^{K_n}(a_n,b_n)`
>
> ` -A_sol^{K_n}(a_n,b_n)| <= epsilon_n`.

Thus there exists a sequence of finite smooth **ultraviolet terminal packets** `I_n=[a_n,b_n]` with:

1. cutoff `K_n->infinity`;
2. time length `|I_n|<=delta_n->0`;
3. arbitrarily large productive gradient work;
4. arbitrarily large productive solenoidal work;
5. arbitrarily large balanced high-pass minority action;
6. arbitrarily small integrated cross-representation mismatch.

## 4. Canonical packet choice

A concrete canonical choice is

`epsilon_n=1/K_n`,

`M_n=K_n`.

Then one may take

`delta_n`

`<=2nu /(N_{K_n}^2 E0^8 K_n^2)`.

Since `N_K` grows cubically in the lattice-count sense, this crude energy-only choice is much shorter than a parabolic `K^-2` window. R31 does not hide this loss.

The significance is not the particular exponent but the existence of a fully synchronized diagonal sequence despite the nonuniform finite-mode constant.

## 5. What R31 buys for concentration/compactness

Before R31, R28–R30 were fixed-cutoff statements. A compactness argument needs a sequence in which frequency and time both move toward the putative singular scale.

R31 supplies exactly such a sequence.

Any future minimal-object or rescaling argument may now assume, after extraction, that on packet `I_n` above scale `K_n`:

- both exact pressure-work representations are strongly productive;
- the pointwise weaker Helmholtz tail carries large critical action;
- the two integrated pressure-work representations differ by `o(1)`.

This removes one bookkeeping freedom from the blow-up sequence.

## 6. The next quantitative bottleneck

R31 also exposes a concrete weakness in the current estimate.

The synchronization-window length is controlled through the factor `N_K` from the crude finite-mode `L^1 -> Fourier coefficient` estimate. On a parabolic window of size `K^-2`, the current R29 mismatch estimate is not uniform as `K->infinity`.

Therefore a materially stronger theorem would improve the low-frequency compensator estimate from the current `N_K` growth to a coefficient `M_K` satisfying, ideally,

> `M_K/K -> 0`.

Such an improvement would synchronize the two representations directly on parabolic time windows and would be substantially more useful for a scale-invariant blow-up limit.

This is now a precise falsifiable target rather than a vague request for better frequency control.

## 7. What R31 does not prove

R31 does not prove:

- spatial concentration of the packets;
- a nontrivial rescaled limit;
- parabolic-scale synchronization;
- same-shell P/Q overlap;
- boundedness of the packet action or work;
- contradiction with Navier–Stokes dynamics.

It is an extraction theorem preparing the next compactness/rigidity step, not that step itself.

## 8. Verification

`verification/check_R31_diagonal_uv_terminal_packets.py` checks the exact synchronization-window formula, terminal-locality logic and finite-packet extraction algebra.

The continuum argument itself is a direct consequence of R28–R30 plus local smoothness on compact pre-endpoint intervals.
