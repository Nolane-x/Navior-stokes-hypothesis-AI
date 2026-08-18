# W5-E45 Semantic Research Ledger

**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay status:** **NOT SOLVED**  
**Target:** periodic 3D incompressible Navier–Stokes, Clay statement (B)  
**Runtime:** Nolane World `0.6.0` / depth `W5`

## 1. Why E45 exists

E44 extracted actual-trajectory unit common-work bursts carrying both a diverging amplitude center and a diverging productive-work quantile radius `R_theta`, but RD021/RD022 prevented promotion to parabolic or spatial compactness. E45 attacks a narrower load-bearing question: can the common productive work itself be given an **upper** frequency scale, so the burst is no longer known only to escape toward high frequency?

The answer is partially yes. R45 proves an absolute `1/R` tail bound for the full signed common-work measure. C003 sharpens the first formulation and identifies the exact work scale

> `Lambda_J = int_J ||u||_infinity^2 ||omega||_2^2 dt`,

with coarse cap

> `Gamma_J=A_J^2 q_J`.

RD023 then prevents the invalid leap from high-frequency tightness to full spectral compactness by exhibiting a high-multiplicity abstract family whose productive work collapses toward zero after work-scale normalization.

## 2. R45 — absolute common-work tail

For an R41 unit burst `J`, define

`c_k(t)=(V/2) Re[Lhat(k)·conj((Q_k-P_k)Ghat(k))]`,

`b_k(J)=int_J c_k(t)dt`,

with `G=|u|u`, `L=omega×u`, and

> `sum_(|k|>L0)b_k(J)=1`.

Parseval and Cauchy--Schwarz give

`sum_(|k|>R)|c_k(t)|`

`<= (V/2)||Lhat||_(ell2) ||1_(|k|>R) Ghat||_(ell2)`.

Using

> `|L|<=|u||omega|`,

> `|grad G|<=2|u||grad u|`,

and `||grad u||_2=||omega||_2`, one obtains

> `sum_(|k|>R)|c_k(t)|`
>
> `<= R^-1 ||u(t)||_infinity^2 ||omega(t)||_2^2`.

Thus, with

> `Lambda_J=int_J||u||_infinity^2||omega||_2^2dt`,

> `Gamma_J=A_J^2 q_J`,

R45/C003 gives the exact chain

> `T_J(R):=sum_(|k|>R)|b_k(J)|`
>
> `<= Lambda_J/R`
>
> `<= Gamma_J/R`.

This is a total-variation bound on the entire signed output tail, not merely a per-mode cap.

## 3. Every unit burst gets an intrinsic upper work scale and its own center

At `R=L0`, unit normalization yields

> `1 <= T_J(L0) <= Lambda_J/L0`,

so

> `L0 <= Lambda_J <= Gamma_J`.

Consequently every R41 unit burst itself satisfies

> `A_J >= sqrt(L0/q_J)`.

Therefore the amplitude-center selection no longer needs the many-burst parent argument of R44 merely to prove that an individual unit burst has a diverging peak. R44 remains useful for the exact `L^3`-balance parent-packet interpretation, but R45 gives a stronger per-burst spectral-action route.

After scaling frequency by `Lambda_J`,

> `mu_J=sum_(|k|>L0)b_k delta_(k/Lambda_J)`

satisfies

> `|mu_J|({|xi|>r})<=1/r`.

Hence the signed common-work measures are uniformly tight at **high normalized frequencies**.

## 4. Two-sided productive-radius architecture

R43 supplied lower floors for the positive-work quantile radius `R_theta`. R45/C003 supplies the first upper radius:

> `R_theta(J,L0) <= Lambda_J/(1-theta)`
>
> `<= Gamma_J/(1-theta)`.

R45 also adds the stress-form low-frequency capacity. Since

> `L=div(u tensor u-(|u|^2/2)I)`,

one has

> `|c_k(t)|<=V^-1 E0^4 |k|`,

and therefore

> `R_theta >= [theta V/(27E0^4 |J|)]^(1/4)`.

Combining the coarse upper `R_theta<=Gamma_J/(1-theta)` with the three lower floors gives, among others,

> `A_J >= sqrt(L0/q_J)`,

and the scale-critical law

> `A_J >= sqrt(1-theta)(theta V/26)^(1/4) E0^(-1/2) q_J^(-3/4)`.

Thus vanishing unweighted enstrophy cost on a normalized productive burst forces a quantitatively stronger amplitude price than the elementary `q_J^-1/2` scale alone.

## 5. C003 — correction against overclaim

The first R45 text named `Gamma_J=A_J^2q_J` as the upper active scale. C003 records the sharper fact that the proof actually produces

> `Lambda_J=int_J||u||_infinity^2||omega||_2^2dt`,

with `Lambda_J<=Gamma_J`.

More importantly, C003 separates three compactness questions that must not be conflated:

1. **spectral:** prevent productive mass from collapsing toward zero after `Lambda_J` normalization;
2. **parabolic:** control a scale-time quantity such as `R_theta^2|J|` or `Lambda_J^2|J|`;
3. **spatial:** obtain local-energy/tightness around the selected amplitude center.

E45 does not solve items 1--3 simultaneously.

## 6. RD023 — exact work-scale high-tail tightness is not spectral non-collapse

RD023 strengthens its abstract family by taking

> `Lambda_n=Gamma_n=n^p`, `p>1`,

with an `n^3`-mode productive cloud at physical output frequency `~n`, unit positive work, `q_n~n^-2`, and `ell_n~n^-4`.

It satisfies the R42 frequency-independent cap, the R43 `1/|k|` cap, the R45 stress low-mode cap, and the **sharp** tail inequality

> `T_n(R)<=Lambda_n/R`.

Nevertheless

> `|k|/Lambda_n ->0`

for every productive mode.

RD023 is not a Navier–Stokes trajectory. It is a route guard proving that all scalar spectral envelopes through R45 still permit normalized low-frequency collapse. Genuine PDE/orbit geometry is needed.

## 7. Verification

R45 specific self-reporting GitHub Actions gate:

> run `32093191615`

at source head

> `a97571d4eaea308e4ce12046ae8389c92910d1f6`

recorded

> `R45_PRIMARY_PASS checks=145492`,
>
> `R45_FRESH_GRID_PASS checks=312`,
>
> `RD023_PASS checks=974`.

The fresh physical-grid reconstruction reported maximum ratios

- tail: `0.00206567`;
- stress: `0.000118287`;
- `grad G` chain-rule: `0.457424`.

A local clean-bytecode replay was split into bounded batches after a single long shell invocation hit the execution timeout. Every one of the 64 E45 Python certificates passed across those batches; no timeout was counted as a pass. The canonical repository-wide result is the GitHub aggregate below.

Final E45 aggregate GitHub Actions run:

> `32093839544`

verified theorem/checker HEAD

> `9e7cdc361030dc686be2575f31c02d72a128aa0d`

and recorded

> `verification_scripts=64`
>
> `W5_E45_FULL_SUITE=PASS`.

Result commit:

> `6c5116b44cec757b8d32b7f737adbd5b292b2c54`.

All certificates retain partial scope. Passing the suite does not certify global regularity.

## 8. Nolane World 0.6 W5 state

Fresh E45 World:

> `world5_712c95ada64ec9f250d5`.

Research session:

> `research_4287f73fff43913e47`.

The World was seeded with rival hypotheses: the R45 tail theorem, the overstrong full-compactness promotion, and the corrected multi-branch compactness frontier. Primary algebra, fresh physical/Fourier reconstruction, and RD023 were registered as distinct evidence lineages. RD023 was promoted to a verified counterexample against the overstrong hypothesis.

Final public-safe diagnostics:

- correctness `0.965`;
- evidence `0.95`;
- robustness `0.94`;
- verification `0.97`;
- fresh verifications `1`;
- critical unknowns `1`;
- gate score `0.2142857142857143`;
- gate **FAILED**;
- research closure **blocked**.

The public-safe record is

> `verification/W5_E45_world_gate_result.json`.

World gate scores are governance diagnostics, not mathematical completion percentages.

## 9. Exact live frontier after E45

A singularity compatible with the full spine must still create R41/R42 unit common-work bursts with vanishing duration/enstrophy cost and exploding productive multiplicity. E45 adds:

1. every such burst has an exact upper work-frequency `Lambda_J>=L0`;
2. the full signed work tail is uniformly TV-tight above multiples of `Lambda_J`;
3. every unit burst has its own diverging amplitude center;
4. the productive radius is squeezed between R43/R45 lower floors and `Lambda_J/(1-theta)`;
5. scalar envelope logic still permits collapse toward zero normalized frequency.

The remaining compactness problem is therefore **three-part**:

> **spectral non-collapse + parabolic scale-time control + spatial/local-energy tightness**, 

unless the alternative R37/R42 many-body route can rule out the bursts before compactness is needed.

For the spectral branch define

> `Delta_theta^work=Lambda_J/R_theta`.

A material next theorem would either bound/exploit this spread using genuine input-output/helical PDE structure, or bypass it with a many-body depletion theorem. Even bounded spectral spread would still require a time/space compactness bridge before an ancient/minimal object or rigidity argument is legitimate.

## 10. Nonconvergence statement

E45 does **not** prove

- bounded `Delta_theta^work`;
- parabolic comparability of burst duration with `R_theta` or `Lambda_J`;
- local-energy tightness around the selected center;
- compactness of rescaled velocity fields;
- existence or exclusion of a nontrivial ancient solution;
- a Liouville/backward-uniqueness contradiction;
- many-body summability of the R37 helical common mode;
- global periodic 3D Navier–Stokes regularity.

**W5-E45 is a verified-partial research checkpoint. It is not a solution of the Navier–Stokes Millennium Prize Problem.**
