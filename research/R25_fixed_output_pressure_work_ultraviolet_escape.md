# R25 — Fixed-output pressure work is energy-controlled; Branch G must escape to ultraviolet output

**Status:** `exact finite-output theorem / closes R23 high-high-to-low output regime`  
**Depends on:** R02–R03, R18, R23–R24  
**Clay status:** no summable high-frequency control; no global regularity conclusion

R23 left four dyadic interaction regimes for the test defect `Q(|u|u)`. In particular, it noted that high-high interactions producing low output might be harmless, but did not prove the required summability.

R25 closes that fixed-output issue without resolving the input decomposition at all.

Work on the normalized unit periodic torus. Let

`G=|u|u`,

`L=omega×u`,

and let `P_{<=K}` be the Fourier projector onto the finite nonzero set

`Lambda_K={k in Z^3: 0<|k|<=K}`.

Write

`N_K=#Lambda_K`.

## 1. Low-output test defect is controlled by energy alone

For every Fourier mode `k`,

`|Ghat(k)| <= ||G||_1`

by the Fourier coefficient `L^1` bound. But

`||G||_1 = int |u|^2 = ||u||_2^2`.

Because `Q_k` is an orthogonal projection and therefore a contraction,

`|Q_k Ghat(k)| <= ||u||_2^2`.

Parseval over the finite output set gives

> `||P_{<=K} Q(|u|u)||_2`
>
> `<= sqrt(N_K) ||u||_2^2`.

This bound is independent of how the output was produced. In particular, infinitely high input frequencies may interact and nearly cancel into a low output; the whole low-output sum is still energy-controlled.

## 2. Low-output gradient Lamb force is also energy/enstrophy controlled

For the Lamb force,

`||L||_1 <= ||omega||_2 ||u||_2`.

Thus each low Fourier coefficient obeys

`|Q_k Lhat(k)| <= ||omega||_2 ||u||_2`,

and therefore

> `||P_{<=K} Q(omega×u)||_2`
>
> `<= sqrt(N_K) ||omega||_2 ||u||_2`.

This is the Branch-G analogue of the finite-frequency physical-Lamb estimate used in R18, now retaining the gradient channel and pairing it with the exact nonlinear `L^3` test defect.

## 3. The complete low-output pressure work is time-integrable

By R03,

`W_3=<Q(omega×u),Q(|u|u)>`.

Define its fixed-output part

`W_{3,<=K}=<P_{<=K}Q(omega×u), P_{<=K}Q(|u|u)>`.

Cauchy and Sections 1–2 give

> `|W_{3,<=K}|`
>
> `<= N_K ||omega||_2 ||u||_2^3`.

Let

`E0=||u_0||_2`.

For a smooth solution on `[0,T]`, the energy inequality gives

`sup_{t<=T}||u(t)||_2 <= E0`

and, for periodic divergence-free velocity,

`2 nu int_0^T ||omega||_2^2 dt <= E0^2`.

Hence

`int_0^T ||omega||_2 dt`

`<= sqrt(T) [int_0^T ||omega||_2^2 dt]^(1/2)`

`<= E0 sqrt(T/(2 nu))`.

Therefore

> `int_0^T |W_{3,<=K}(t)| dt`
>
> `<= N_K E0^4 sqrt(T/(2 nu)) < infinity`.

This is an a-priori arbitrary-data finite-output bound obtained from energy alone.

## 4. Exact ultraviolet-output consequence

Suppose the R01 critical `L^3` mechanism becomes nonintegrable at a finite maximal time `T*` through the pressure work. For every fixed `K`, R25 says the entire contribution at output frequencies `|k|<=K` is absolutely time-integrable.

Therefore any nonintegrable pressure-work sequence must escape every fixed output cutoff:

> the obstruction cannot remain at bounded Fourier output frequency.

This conclusion is independent of whether the contributing inputs are:

- low-high,
- high-low,
- high-high,
- or an infinite superposition of near-cancelling high modes.

In particular, the R23 **high-high -> low** regime is closed as a possible source of non-summable finite-time pressure work.

## 5. What R25 does and does not remove

R25 removes a whole *output* regime, not the high-frequency problem itself.

It proves:

- low output is harmless for Branch G;
- raw amplitude high frequencies cannot hide a singular mechanism at a fixed low output;
- any surviving Branch-G obstruction must be an actual ultraviolet **output** of `Q(|u|u)` coupled to ultraviolet output of `Q(omega×u)`.

It does **not** prove summability as `K->infinity`. The factor `N_K` grows with the cutoff, so the theorem is not a uniform critical estimate.

The remaining high-output interactions are therefore the correct place to use R23's null symbol and R24's transported-speed/longitudinal-strain representation.

## 6. Updated Branch-G dyadic frontier

After R24/RD013/R25, the old four-way R23 list sharpens to:

1. **high-u / low-amplitude-frequency -> high output:** exact low/high commutator gain from R23;
2. **low-u / high-amplitude-frequency -> high output:** raw amplitude frequency is not enough; must carry nonzero transported-speed scalar `q_amp` (R24/RD013);
3. **high-high -> high output:** still genuinely critical and unresolved;
4. **any inputs -> fixed low output:** energy-controlled and time-integrable by R25.

Thus Branch G is now a genuinely **high-output longitudinal-strain/commutator** problem.

## 7. Relation to R18

R18 proves that any divergent full physical Lamb action must escape every fixed Fourier cutoff. R25 proves the complementary statement for the pressure-work pairing:

- R18: physical Lamb-force action cannot diverge at fixed low output;
- R25: critical pressure work cannot diverge at fixed low output.

Together they eliminate finite-output concentration from both sides of the R03 Helmholtz pairing.

What remains is a scale-by-scale ultraviolet coupling problem, not a low-mode pressure problem.

## 8. Verification

`verification/check_R25_fixed_output_pressure_escape.py` checks finite-mode counting and reproduces the analytic Fourier bounds on a smooth exactly divergence-free trigonometric field using an independent discrete Fourier implementation.

The continuum theorem itself follows from the `L^1` Fourier-coefficient bound, orthogonality/contraction of `Q`, Parseval on a finite output set, Cauchy–Schwarz, and the energy inequality.
