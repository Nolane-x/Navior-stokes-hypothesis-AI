# W5-E46 Semantic Research Ledger

**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay status:** **NOT SOLVED**  
**Target:** periodic 3D incompressible Navier–Stokes, Clay statement (B)  
**Runtime:** Nolane World `0.6.0` / depth `W5`

## 1. Why E46 exists

E45 gave every R41 unit common-work burst an exact signed-work upper frequency scale and an amplitude center, but C003/RD021/RD022/RD023 left spectral, parabolic, and spatial compactness separated. E46 attacks the spatial side without pretending to solve the scale-transfer problem.

The internal advance is R46: the full signed common-work tail is controlled by the **spatially local** density `|u|^2|grad u|^2`, not only by `||u||_infinity^2||omega||_2^2`. A unit burst therefore forces macroscopic amplitude-weighted gradient mass and contains a work-linked large-amplitude point. Terminal work-linked points accumulate at an actual singular point.

At that point, E46 deliberately imports established interior suitable-solution theorems of Albritton–Barker (arXiv:1811.00507v2): local `L^3` divergence and existence of a non-trivial mild bounded ancient blow-up solution. The external theorem is not represented as reproved by a script.

RD024 then kills the overstrong next step: all scalar envelopes through R46 permit the productive Fourier scale to collapse to zero or escape to infinity under amplitude normalization. Thus the live unknown becomes **scale/structure transfer into the ancient blow-up**, or a many-body bypass.

## 2. R46 — spatially local signed-work tail

For a unit burst `J`,

`c_k(t)=(V/2) Re[Lhat(k)·conj((Q_k-P_k)Ghat(k))]`,

`b_k(J)=int_J c_k(t)dt`,

with `G=|u|u`, `L=omega×u` and

> `sum_(|k|>L0)b_k(J)=1`.

Parseval gives

> `sum_(|k|>R)|c_k(t)| <= (1/(2R)) ||L(t)||_2 ||grad G(t)||_2`.

Define

> `X(t)=int_(T^3)|u|^2|grad u|^2 dx`.

The pointwise bounds

> `|omega|^2<=2|grad u|^2`,
>
> `|grad(|u|u)|<=2|u||grad u|`

give

> `||L||_2^2<=2X(t)`,
>
> `||grad G||_2^2<=4X(t)`.

Hence

> `sum_(|k|>R)|c_k(t)| <= sqrt(2)X(t)/R`.

Define the spatially local work frequency

> `Sigma_J=sqrt(2) int_J int_(T^3)|u|^2|grad u|^2 dxdt`.

Then

> `T_J(R):=sum_(|k|>R)|b_k(J)|<=Sigma_J/R`,

and

> `Sigma_J<=sqrt(2)Lambda_J<=sqrt(2)Gamma_J`.

## 3. Work-linked amplitude/gradient concentration

At `R=L0`, unit normalization gives

> `Sigma_J>=L0`,

or

> `int_J int |u|^2|grad u|^2 >= L0/sqrt(2)`.

Let

> `q_J=int_J||grad u||_2^2dt=int_J||omega||_2^2dt`,
>
> `a_J^2=L0/(2sqrt(2)q_J)`,
>
> `H_J={(x,t):|u(x,t)|>=a_J}`.

The complement of `H_J` contributes at most `L0/(2sqrt(2))` to the weighted-gradient mass, so

> `int_(H_J)|u|^2|grad u|^2 dxdt >= L0/(2sqrt(2))`.

Every unit burst therefore contains a work-linked point `(x_J,t_J)` satisfying

> `|u(x_J,t_J)|>=sqrt[L0/(2sqrt(2)q_J)]`.

Along the R41 terminal diagonal, `L0->infinity`, `q_J->0`, and `t_J->T*`, so these amplitudes diverge.

## 4. Internal singular-point localization

The torus is compact; after a subsequence `x_J->x*`. If `(x*,T*)` were regular, the velocity would be bounded in a sufficiently small terminal parabolic neighborhood. The terminal work-linked points eventually lie there while their amplitudes diverge, a contradiction.

Therefore

> **`(x*,T*)` is an actual interior singular point of the hypothetical periodic solution.**

This part is internal and independent of the external ancient-solution theorem.

## 5. Primary-literature bridge

The smooth preterminal periodic solution restricted to a small Euclidean chart around `x*` is an interior suitable weak solution; positive constant viscosity can be normalized deterministically.

The exact theorem interface is pinned in

> `sources/R46_albritton_barker_interior_singularity_ancient_bridge.md`.

Albritton–Barker, arXiv:1811.00507v2:

- **Theorem 1.1:** for the stated suitable-solution class, an interior singular point forces the local `L^3` norm to diverge in every fixed neighborhood;
- **Theorem 1.2:** an interior singularity generates a non-trivial mild bounded ancient Navier–Stokes solution on `R^3` as a blow-up limit.

Thus, under the finite-time singularity hypothesis, E46 no longer treats *existence of some ancient blow-up object* as an open internal theorem. This is an imported known result, not a novelty claim and not something Python certificates reprove.

## 6. RD024 — ancient-object existence is not productive-scale transfer

Define

> `Chi_theta=R_theta/A_J`.

Both numerator and denominator scale linearly under Navier–Stokes concentration scaling.

RD024 constructs two abstract families satisfying the scalar R43–R46 lower/upper scale constraints:

- one with `Chi_theta->0`;
- one with `Chi_theta->infinity`.

The families are not Navier–Stokes trajectories. They prove only that the current scalar envelopes do not guarantee that productive modes remain at `O(1)` frequency in an amplitude-normalized ancient blow-up.

## 7. Verification

Specific R46 self-reporting gate:

> run `32094667211`
>
> source head `aa9385eb12cc01de297d1c5506f441b759e67364`

recorded

> `R46_PRIMARY_PASS checks=300095`,
>
> `R46_FRESH_GRID_PASS checks=220`,
>
> `RD024_PASS checks=1802`.

Fresh-grid maximum ratios:

- local-tail ratio `0.00440068`;
- Lamb/`2X` ratio `0.0409545`;
- `grad G`/`4X` ratio `0.274772`.

The specific gate records

> `external_bridge=PRIMARY_SOURCE_SCOPE_PINNED_NOT_REPROVED_BY_SCRIPT`.

Canonical E46 aggregate:

> run `32094820170`
>
> verified head `961be1b878eacd69b81e72f495ea29c21dbc9fc7`
>
> `verification_scripts=67`
>
> result commit `f7e641357931c6886b00eb884104bb23001644c3`.

All machine certificates retain partial scope.

## 8. Nolane World 0.6 W5 state

Fresh World:

> `world5_20d12077702c0290f6e2`

Research session:

> `research_df9d394fb13dd9672f`

Verified RD024 counterexample:

> `cx_6d8b8bddf945352c82`

Open epistemic debt:

> `debt_ea0489eace6a5a9978`.

Quality attestation:

- correctness `0.97`;
- evidence `0.96`;
- robustness `0.945`;
- verification `0.975`.

The W5 gate **FAILED**, score `0.2142857142857143`, with `critical_unknowns=1`; research closure remains blocked. Public-safe record:

> `verification/W5_E46_world_gate_result.json`.

World scores are governance diagnostics, not mathematical completion percentages.

## 9. Exact live frontier after E46

The singularity-compatible mechanism now has two linked lineages.

**Productive-work lineage:** unit common high-pass work, P/Q synchronization, resolved absolute-work evacuation, exploding productive multiplicity, R37 helical pair depletion, R43 lower productive radius, R45 exact signed-work upper scale, and R46 spatially local amplitude-weighted gradient mass.

**Established singularity lineage:** at a subsequential R46 work-linked singular point, local `L^3` diverges in every fixed neighborhood and a non-trivial mild bounded ancient solution exists as a blow-up limit.

The load-bearing gap is now the **transfer/alignment theorem** between these lineages.

A decisive next result must do one of the following:

1. prove productive `R_theta`/`Sigma` scales remain comparable to an amplitude/ancient blow-up scale;
2. prove a fixed fraction of R41 common work and R37 helical restrictions survives some PDE-compact singularity rescaling;
3. derive a Liouville/backward-uniqueness contradiction for the transferred structured ancient solution;
4. bypass the limit with a many-body depletion theorem.

## 10. Nonconvergence statement

E46 does **not** prove bounded `Chi_theta`, transfer of unit common work or helical geometry to the ancient limit, a Liouville theorem for that limit, many-body common-mode summability, or global regularity.

**W5-E46 is a verified-partial bridge. It is not a solution of the Navier–Stokes Millennium Prize Problem.**
