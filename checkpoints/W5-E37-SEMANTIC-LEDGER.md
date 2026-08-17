# W5-E37 Semantic Research Ledger

**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay status:** **NOT SOLVED**  
**Target:** periodic 3D incompressible Navier–Stokes, Clay statement (B)  
**Runtime:** Nolane World `0.5.0` / depth `W5`

## 1. Provenance and nonconvergence discipline

E37 was developed after a deliberate audit of E36 rather than by extending the old frontier mechanically.

The uploaded verified Nolane World `0.5.0` source package was materialized into the research environment. An editable pip install could not fetch its build dependency because the execution container has no external package-network access; the runtime was therefore executed source-resident through `PYTHONPATH`. Import reports version `0.5.0`, and the locally re-run core `convergence/engine/store` subset passed `8/8` tests. No claim is made that all package tests were re-run locally.

Fresh E37 World:

- world id: `world_dd0ae94e7143`;
- depth: `W5`;
- best candidate: R37 + strengthened R38;
- critical unknowns: `1`;
- unresolved high-severity attacks: `2`;
- World gate: **FAILED**;
- gate record: `verification/W5_E37_gate_result.json`.

The World gate intentionally retains both mathematical and process blockers. Its candidate-quality/material-improvement numbers are governance diagnostics, **not percentages of the Millennium problem solved**.

## 2. Repository-wide verification

Final E37 aggregate GitHub Actions run:

> `32043127917`

The independent Ubuntu/Python 3.12 runner log records

> `verification_scripts=45`
>
> `PASS verification_scripts=45`.

New E37-specific verification includes:

- R37 primary CI: `32042430114` — PASS;
- strengthened R38 CI: `32043077881` — PASS;
- final aggregate: `32043127917` — `45/45` PASS.

Inside the final aggregate:

- `check_R37_common_mode_helical_bottleneck.py` passed `282912` checks with maximum closed-form projection error about `2.93e-14`;
- independent `fresh_verify_e37_common_mode_helical.py` passed `70000` checks using eigendecomposition rather than the theorem's explicit helical basis, with maximum error about `3.91e-14`;
- `check_R38_uniform_multicutoff_packets.py` passed `23701` lattice/extraction/shell-algebra checks.

All such checks certify only their declared structural/computational scope.

## 3. E37 methodological correction: the mismatch is not the load-bearing object

E35–E36 focused heavily on the difference between the gradient and solenoidal high-frequency pressure-work representations. That was useful for proving synchronization, but E37 records a high-severity correction:

> even an integrable or vanishing representation mismatch does not control the **common productive mode** through which both high-frequency works may diverge together.

Let

`L=omega×u`,

`G=|u|u`,

and in the smooth square-partition framework define

`W_grad,H=<HQL,HQG>`,

`W_sol,H=-<HPL,HPG>`.

With the Helmholtz reflection

`J=Q-P=2Q-I`,

R37 proves exactly

> `2 C_H=<HL,JHG>`,

where

`C_H=(W_grad,H+W_sol,H)/2`.

The mismatch remains

`D_H=W_grad,H-W_sol,H=<HL,HG>`.

Thus `D_H` is a synchronization constraint; `C_H` is the primary productive quantity to exclude.

This correction prevents further milestones from being inflated by progressively smaller mismatch estimates that leave the common singular mechanism untouched.

## 4. R37 — exact common-mode stress geometry

With

`rho=|u|`,

`T=u tensor u-(rho^2/2)I`,

one has

`L=div T`.

R37 gives the exact common-mode stress representation

> `C_H=-(1/2)<HT,H grad(JG)>`.

The R33 mismatch also has the dual high-filter form

> `D_M=<HT,H grad G>`.

Moreover the unfiltered stress/test contraction is not generic:

> `T:grad G=(3/2)rho^2 q_amp`,

where R24's scalar

`q_amp=div(rho u)=u·grad rho`.

Since

`(3/2)rho^2 u·grad rho=(1/2)u·grad(rho^3)`,

the full spatial integral cancels for divergence-free flow. The filtered defect/common mode therefore measures destruction of an exact transported-speed cancellation across scales.

## 5. R37 — exact helical pair factorization inside the common mode

For helical curl eigenmodes

`i r×u_s(r)=s|r|u_s(r)`, `s=+-1`,

pair-symmetrizing the physical Lamb convolution gives

> `Lhat(k)`
>
> `=(1/2) sum_(p+q=k) sum_(s,t)`
>
> ` (s|p|-t|q|)[u_s(p)×u_t(q)]`.

The exact factor `s|p|-t|q|` appears inside the Parseval formula for `C_H`, so the cancellation is attached to the load-bearing common mode rather than merely to a norm bound on the full Lamb force.

Consequences:

- same-spin pairs carry radial difference `|p|-|q|`;
- opposite-spin pairs carry radial sum `|p|+|q|`;
- same-spin equal-shell pairs vanish exactly.

## 6. R37 — closed P/Q formulas for every non-collinear helical pair

For non-collinear `p,q`, write

`a=|p|`, `b=|q|`, `c=|p+q|`, `mu=cos(theta)`.

For the pair source

`F_st=(s a-t b) h_s(p)×h_t(q)`,

R37 derives closed channel norms.

### Same spin

> `|Q F_ss|=((a-b)^2(1-mu))/(2c)`,

> `|P F_ss|=(|a-b| sin(theta)/2)`
>
> ` *sqrt(1+(a+b)^2/c^2)`.

The gradient channel therefore has a **quadratic radial-gap depletion**, while the solenoidal channel has a linear radial-gap depletion.

### Opposite spin

> `|Q F_(s,-s)|=((a+b)^2(1+mu))/(2c)`,

> `|P F_(s,-s)|=((a+b)sin(theta)/2)`
>
> ` *sqrt(1+(a-b)^2/c^2)`.

At equal radius `a=b`,

> `|Q F_(s,-s)|=c`,
>
> `|P F_(s,-s)|=c sin(theta/2)`.

Thus a narrow-shell opposite-spin pair can retain a full gradient channel, but near collinearity its solenoidal channel is depleted.

Because R27/R30/R34 force the pointwise weaker Helmholtz Lamb channel to accumulate divergent critical action in the hypothetical singular scenario, the pair-level maximally dangerous narrow-shell source is narrowed to

> **opposite-spin, non-collinear, active-scale activity**,

with substantial radial dispersion providing the alternative same-spin route.

## 7. R37 high-severity attack: pairwise geometry does not sum automatically

R37 does **not** permit the invalid step

`min(||sum F_P||,||sum F_Q||)`

`<= or ~ sum min(||F_P||,||F_Q||)`.

Different triads can populate the two channels differently, and many individually depleted terms can accumulate coherently.

This remains a live high-severity attack. No global balanced-action estimate is inferred from pairwise P/Q formulas.

## 8. R38 — one packet synchronizes an entire growing cutoff hierarchy

R31 synchronized one prescribed moving cutoff. R38 upgrades this using R32's terminal enstrophy-tail estimate.

Let

`q(a)=int_a^{T*}||omega||_2^2dt -> 0`.

R32 gives, for each sharp cutoff,

`|A_grad^K-A_sol^K|`

`<=C N_K^(2/3)E0^2 q(a)`.

For any finite ceiling `L`, `N_K<=N_L` for all `K<=L`. Hence one can move the packet start sufficiently close to `T*` so that the mismatch is uniformly small for **all** `K<=L`.

Below finite `L` there are only finitely many distinct periodic sharp Fourier projectors. R28/R30 give terminal divergence for each fixed projector. Therefore one common packet endpoint makes, simultaneously for every `K<=L`,

- gradient high-pass productive work arbitrarily large;
- solenoidal high-pass productive work arbitrarily large;
- balanced high-pass action arbitrarily large;
- representation mismatch arbitrarily small.

## 9. R38 — arbitrary frequency ceilings and arbitrary terminal-window scales

Given arbitrary prescribed

`L_n->infinity`,

`epsilon_n->0`,

`M_n->infinity`,

`delta_n->0`,

R38 extracts terminal packets `I_n` satisfying

> `|I_n|<=delta_n`

and for **every** `K<=L_n`, simultaneously,

> `A_grad^K(I_n)>=M_n`,
>
> `A_sol^K(I_n)>=M_n`,
>
> `A_bal^K(I_n)>=M_n`,
>
> `|A_grad^K(I_n)-A_sol^K(I_n)|<=epsilon_n`.

The frequency ceiling and terminal-window upper scale may therefore be prescribed independently. This does not mean the active spectrum is localized near `L_n`; the work may be carried at much higher frequencies.

## 10. R38 — every signed shell is synchronized too

For `0<=K_1<K_2<=L_n`, sharp orthogonality gives shell work as a difference of cumulative tails:

`S_grad^(K1,K2)=A_grad^K1-A_grad^K2`,

`S_sol^(K1,K2)=A_sol^K1-A_sol^K2`.

Writing

`Delta_n(K)=A_grad^K-A_sol^K`,

one obtains exactly

> `S_grad^(K1,K2)-S_sol^(K1,K2)`
>
> `=Delta_n(K_1)-Delta_n(K_2)`.

Therefore

> `sup_(K1<K2<=L_n)`
>
> `|S_grad^(K1,K2)-S_sol^(K1,K2)|`
>
> `<=2epsilon_n`.

So the two productive representations cannot remain macroscopically separated even on an arbitrary **signed sharp shell** inside the expanding hierarchy.

This is stronger than R31/R32 single-cutoff synchronization.

## 11. What R38 still does not give

The shell result controls signed integrated pressure work. It does **not** imply:

- shellwise positivity;
- total-variation closeness;
- same-shell P/Q Lamb-energy overlap;
- control of the nonlinear balanced minimum shell-by-shell;
- absence of positive/negative sub-shell cancellation;
- spatial concentration or compactness;
- spectral localization near the selected ceiling.

Thus RD014 remains relevant at the energy/channel-overlap level.

## 12. Canonical E37 obstruction

Combining R27–R38, a hypothetical finite-time singular trajectory compatible with this proof spine must now support a terminal mechanism with all of the following properties:

1. **common productive UV mode:** both Helmholtz pressure-work representations diverge through a synchronized common mode;
2. **balanced minority strength:** the weaker Helmholtz Lamb tail has divergent critical action above every fixed sharp or smooth scale;
3. **helical pair geometry:** narrow-shell same-spin interactions are radially depleted, and narrow-shell opposite-spin near-collinear interactions are depleted in the solenoidal channel;
4. **uniform cutoff synchronization:** on extracted packets the two productive tails are uniformly close for every cutoff throughout an expanding hierarchy;
5. **uniform signed-shell synchronization:** the two integrated work representations differ by vanishing error on every sharp annulus in that hierarchy;
6. **arbitrarily short terminal support:** the synchronized hierarchy can be extracted on any prescribed shrinking upper time scale;
7. **coherent accumulation remains possible:** signed cancellation and many-triad accumulation can still evade pairwise or shellwise naive bounds.

The live mathematical object is therefore much narrower than E36's generic “comparable high-high commutator”:

> **coherent accumulation of R37-admissible spin/radial/angular common-mode sources, compatible with R38 uniform signed-shell synchronization and the divergent balanced minority action.**

## 13. Exact live frontier after E37

The next load-bearing theorem must do one of two things:

1. derive a scale-critical spacetime bound for the coherent common-mode accumulation using structure retained by `D_3`, transported-speed geometry, helicity/spin conflict, and the balanced minority channel; or
2. construct a concentration-compactness/rigidity argument showing that no nontrivial terminal object can satisfy the simultaneous R37 geometry and R38 shell-synchronization constraints.

Another representation identity or another generic Hölder/Bernstein estimate is not enough.

The critical unknown recorded by Nolane World remains:

> Can the R37 surviving common-mode sources be summed in an a-priori controlled scale-critical quantity, or ruled out by rigidity of the synchronized terminal packets?

No result in E37 answers this question.

## 14. W5 World gate

World `world_dd0ae94e7143` records:

- hypotheses: `6`;
- verifications: `6`;
- experiments: `5`;
- robustness worlds: `4`;
- fresh-context verifications: `3`;
- unresolved critical unknowns: `1`;
- unresolved high-severity attacks: `2`;
- candidate quality: `0.86`;
- estimated material improvement: `0.29`;
- gate: **FAILED**.

Failure reasons include the live critical unknown/high-severity contradiction and fresh-state process requirements such as residency/diversity/adversarial coverage.

These metrics are governance state, not mathematical completion percentages.

## 15. Nonconvergence statement

E37 does **not** prove:

- an a-priori bound on the common productive mode for arbitrary smooth data;
- summability of the balanced ultraviolet action;
- total-variation or positivity control of shellwise pressure work;
- a global pairwise-to-many-body helical cancellation theorem;
- existence/rigidity of a minimal blow-up object;
- periodic 3D Navier–Stokes global regularity.

**W5-E37 is a verified research checkpoint, not a solution of the Navier–Stokes Millennium Prize Problem.**
