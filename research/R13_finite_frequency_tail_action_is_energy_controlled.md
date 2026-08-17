# R13 — Every fixed finite-frequency part of the R08 tail action is controlled by energy

**Status:** `exact structural reduction / standard Bernstein-energy inputs; not claimed novel`  
**Depends on:** R08  
**Clay status:** does not control the ultraviolet limit; not global regularity

R08 shows that a possible finite-time singularity through this route must make the scale-critical high-amplitude projected-Lamb tail action diverge:

`A_tail(T)=int_0^T U(t) ||Q F(t)||_2^2 dt`,

where

`U(t)=||u(t)||_(3/2)`,

`F(t)=1_{|u|>M_*(t)} (omega×u)`,

and

`M_*(t)=nu^2/[12 C_H^2 U(t)]`.

R13 proves that this divergence cannot be carried by any fixed bounded set of Fourier modes.

Work on the unit torus. Let `P_{<=K}` be the orthogonal Fourier projector onto modes `|k|<=K` for a fixed finite `K`. Since the Leray gradient projector `Q` is also a Fourier multiplier, it commutes with `P_{<=K}` and is an `L^2` contraction.

## 1. Finite-frequency Bernstein estimate

For any vector field `f in L^1(T^3)`, finite-dimensional Fourier/Bernstein control gives

`||P_{<=K} f||_2 <= C_B(K) ||f||_1`,

where one may take `C_B(K)` proportional to the square root of the number of retained Fourier modes, hence `C_B(K)=O(K^(3/2))`.

Therefore

`||P_{<=K} QF||_2`

`<= C_B(K)||F||_1`

`<= C_B(K)||omega×u||_1`

`<= C_B(K)||omega||_2 ||u||_2`.

The high-amplitude indicator can only decrease the `L^1` norm and introduces no constant.

## 2. Energy control

On the unit torus,

`U=||u||_(3/2) <= ||u||_2`.

Let

`E0=||u_0||_2`.

For a smooth unforced solution (and likewise at the Leray energy-inequality level),

`||u(t)||_2 <= E0`,

and

`2 nu int_0^T ||grad u||_2^2 dt <= E0^2`.

For periodic divergence-free fields,

`||omega||_2 = ||grad u||_2`.

Consequently

`int_0^T U ||P_{<=K}QF||_2^2 dt`

`<= C_B(K)^2 E0^3 int_0^T ||omega||_2^2 dt`

> `<= [C_B(K)^2/(2 nu)] E0^5`.

Thus:

> For every fixed finite Fourier cutoff `K`, the low-frequency part of the R08 tail action is finite with an explicit energy-dependent bound.

No critical-norm assumption is used.

## 3. Ultraviolet escape theorem

Because `P_{<=K}` and `P_{>K}` are orthogonal and commute with `Q`,

`||QF||_2^2`

`= ||P_{<=K}QF||_2^2 + ||P_{>K}QF||_2^2`.

Hence if

`A_tail(T*)=infinity`

at a finite time `T*`, then for **every fixed finite `K`**,

> `int_0^{T*} U(t) ||P_{>K}QF(t)||_2^2 dt = infinity`.

The dangerous action therefore cannot remain at low or intermediate fixed frequencies. It must escape through arbitrarily high Fourier modes.

This is stronger than merely saying that derivatives become large: the specific R08 high-amplitude projected-Lamb obstruction is forced into the ultraviolet.

## 4. Dyadic formulation

Let `Delta_j` be orthogonal/disjoint Fourier shell projectors (or use a square-function Littlewood–Paley decomposition with the corresponding constants). Then formally/orthogonally

`A_tail = sum_j A_j`,

with

`A_j(T)=int_0^T U ||Delta_j QF||_2^2 dt`.

Every fixed shell has finite action. Therefore divergence of `A_tail` can only occur through a non-summable cascade across shells `j->infinity`.

The theorem does **not** assert that individual high-shell actions are large; a divergent total can be formed by many small shell contributions. This prevents an unjustified jump from ultraviolet escape to a one-scale epsilon contradiction.

## 5. New proof frontier

R13 changes the R08 problem from

`prove the high-amplitude tail action is finite`

into the more structured question

> can the true Navier–Stokes nonlinearity sustain a non-summable **ultraviolet cascade of high-amplitude projected Lamb action** while obeying the energy/enstrophy budget?

Potential next attacks are now frequency-specific:

1. paraproduct/helical-triad decomposition of `P_{>K}(1_{|u|>M_*}(omega×u))`;
2. prove that high-high or high-low interactions carrying the tail action incur a summable enstrophy cost;
3. derive an epsilon-regularity criterion from small tail action on one frequency-time scale;
4. combine amplitude super-level geometry with frequency-local regularity criteria;
5. construct a minimal ultraviolet defect-cascade object and seek a Liouville/rigidity contradiction.

## 6. Limitation

The bound deteriorates like `K^3` (up to projector conventions), so R13 provides no uniform control as `K->infinity`. That ultraviolet limit is exactly the remaining Millennium-scale obstruction.
