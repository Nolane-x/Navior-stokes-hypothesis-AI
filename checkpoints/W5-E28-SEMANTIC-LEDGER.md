# W5-E28 Semantic Research Ledger

**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay status:** **NOT SOLVED**  
**Target:** periodic 3D incompressible Navier–Stokes, Clay statement (B)  
**Runtime:** Nolane World `0.5.0` / depth `W5`

## 1. Provenance discipline

Historical E23 remains frozen under the original research world:

- world: `world4_05c73a9403ba4574`;
- accepted epoch: `23`;
- historical E23 convergence gate: `FAILED / NONCONVERGED`;
- historical internal score: `0.8333333333333334`;
- canonical status: `NONCONVERGED_PARTIALS_ONLY`.

The old live World database was not present in the current execution filesystem. E24–E28 therefore used a **fresh continuation world** rather than pretending the old state persisted:

- continuation world: `world_e3fcf95bd269`;
- depth: `W5`;
- critical unknowns: `1`;
- continuation gate: `FAILED`;
- full public-safe gate details: `verification/W5_E28_gate_result.json`.

The two World gate scores are not numerically comparable. The invariant research fact is that the load-bearing arbitrary-data critical estimate remains open.

## 2. E28 aggregate verification

GitHub Actions run `32031960379` executed the repository-wide hardened Python certificate loop successfully. The E28 verification directory contains 32 Python checkers/fresh verifiers covered by this aggregate gate.

Recent load-bearing individual runs:

- `32029607416` — R24/RD013 transported-speed/direction representation and raw-amplitude-UV no-go;
- `32029668632` — R25 fixed-output pressure-work escape;
- `32030235082` — R26 complementary solenoidal critical action;
- `32030583668` — R27 exact balanced minimum-action criterion;
- `32030790881` — fresh physical-grid R27 reconstruction;
- `32031474432` — RD014 exact shell-separation counterexample;
- `32031706755` — R28 dual high-pass productive pressure work;
- `32031960379` — full E28 Python-certificate gate.

Every run certifies only its declared exact/computational/structural scope. None is a continuum global-regularity certificate.

## 3. R24 — transported speed is the Branch-G scalar

Let

`rho=|u|`, `e=u/rho` on `{rho>0}`, `S=(grad u+(grad u)^T)/2`.

R24 identifies

`q_amp=div(rho u)=u·grad rho`

and, almost everywhere away from velocity zeros,

`q_amp=(u^T S u)/rho=rho e^T S e=-rho^2 div e`.

Globally,

`Q(rho u)=grad Delta^{-1} q_amp`

and

`||Q(rho u)||_2^2=||q_amp||_{dot H^{-1}}^2`.

This replaces the ambiguous raw `|u|` spectrum by transported-speed / longitudinal-strain structure. The zero set is handled distributionally through `div(rho u)` rather than by assuming a smooth velocity direction there.

R24 interfaces conservatively with the classical velocity-direction regularity literature; it does not claim that literature identity as novel.

## 4. RD013 — raw amplitude ultraviolet is not physical pressure-test ultraviolet

For the smooth mean-zero divergence-free field

`u=(2 cos z, sin z,0)`,

the velocity has only the fundamental `|k|=1` modes, while

`|u|=sqrt((5+3 cos 2z)/2)`

has infinitely many Fourier harmonics. Nevertheless

`div(|u|u)=0`

and therefore

`Q(|u|u)=0`.

Thus high raw amplitude frequency can be purely kinematic and projection-null. The live Branch-G variable must retain longitudinal coupling / transported speed.

## 5. R25 — fixed Fourier output is harmless

For each fixed output cutoff `K`, if

`N_K=#{k in Z^3:0<|k|<=K}`,

then the Fourier `L^1` coefficient bound and Helmholtz contraction yield

`||P_{<=K}Q(|u|u)||_2 <= sqrt(N_K)||u||_2^2`,

`||P_{<=K}Q(omega×u)||_2 <= sqrt(N_K)||omega||_2||u||_2`.

Therefore

`|W_{3,<=K}| <= N_K ||omega||_2 ||u||_2^3`,

and energy/enstrophy imply

`int_0^T |W_{3,<=K}|dt < infinity`

for every finite smooth interval and fixed `K`.

Hence any nonintegrable critical pressure mechanism must escape every fixed output cutoff. In particular, high-high input interactions cannot hide a singular mechanism permanently at bounded output frequency.

## 6. R26 — both physical Lamb channels are individually continuation quantities

R05 gives the complementary exact pressure representation

`W_3=-<P(omega×u),P(|u|u)>`.

R26 derives a scale-critical solenoidal criterion: finiteness of

`A_sol(T)=int_0^T ||u||_(3/2)||P(omega×u)||_2^2 dt`

controls the same critical `L^3` endpoint barrier that R06 controls through

`A_grad(T)=int_0^T ||u||_(3/2)||Q(omega×u)||_2^2 dt`.

Thus the earlier R19 necessary statement `A_sol=infinity OR A_grad=infinity` is valid but not sharp: in this endpoint framework, a singularity requires both individual actions to diverge.

## 7. R27 — balanced minimum-action synchronization

R27 removes the irrelevant constant mode from the solenoidal test field. Periodicity gives

`mean(omega×u)=0`, hence `mean(P(omega×u))=0`.

With `G=|u|u`,

`W_3=-<PL,G-mean G>`.

The exact derivative geometry

`|grad G|^2/|u| <= 2 * (D_3 density)`

combined with weighted Holder and periodic `W^{1,6/5}->L^2` Sobolev–Poincare yields

`||G-mean G||_2 <= C_SP sqrt(2 ||u||_(3/2) D_3)`.

Therefore the same critical `L^3`-diffusion left-hand side has both a solenoidal and a gradient bound. Define

`A_bal(T)`

`=int_0^T ||u||_(3/2)`

` min(||P(omega×u)||_2^2,||Q(omega×u)||_2^2) dt`.

R27 proves

`||u(T)||_3^3 + (3nu/2)int_0^T D_3 dt`

`<= ||u(0)||_3^3 + 3 C_* A_bal(T)`.

Hence finite `A_bal` controls the endpoint barrier. Within the corresponding periodic/local endpoint continuation framework, a finite-time singularity must force

`A_bal(T*)=infinity`.

This is stronger than separate divergence of `A_sol` and `A_grad`: the pointwise weaker physical Helmholtz channel must itself accumulate non-summable critical action.

C002 records this as the canonical sharpening of R19.

## 8. Fresh verification of R27

`verification/fresh_verify_e27_balanced_channels_grid.py` independently reconstructs the load-bearing identities in physical/Fourier-grid form without importing the exact rational checker.

Across six test worlds and two grid resolutions it verifies, within numerical tolerance:

- mean Lamb-force cancellation;
- equality of the complementary pressure pairings;
- Helmholtz channel orthogonality;
- the weighted derivative-density bound;
- the weighted Holder transfer.

GitHub Actions run `32030790881` passed this fresh lineage.

This reduces common-mode implementation risk but is not a proof of arbitrary-data regularity.

## 9. RD014 — global channel synchronization is not scale synchronization

An exact smooth real divergence-free three-mode field was constructed with

`||PL||_2^2 = 79378456/21`,

`||QL||_2^2 = 227945624/21`,

so the global solenoidal fraction is

`9922307/38415510 = 0.2582890868...`.

However, grouping output modes by the exact shell `s=|k|^2`, the overlap functional

`O_shell=sum_s min(P_s,Q_s)`

satisfies

`O_shell/min(||PL||_2^2,||QL||_2^2)`

`=430977/19844614`

`=0.0217175804...`.

Several shells are almost purely solenoidal while others are almost or exactly gradient-only.

Therefore R27's global/timewise balanced action cannot be silently promoted into same-shell P/Q balance. A new dynamical scale-synchronization mechanism is required.

## 10. R28 — both exact pressure-work representations must become productively ultraviolet

The critical pressure work has two exact representations:

`W_3=<QL,QG>=-<PL,PG>`,

where `G=|u|u` and `L=omega×u`.

For any fixed Fourier cutoff `K`, orthogonality gives exact low/high decompositions in both representations. R25-type finite-mode bounds show each fixed low-output contribution is absolutely time-integrable.

R01 gives

`(1/3)d/dt ||u||_3^3 + nu D_3 = W_3`.

If the endpoint `L^3` quantity diverges at a finite maximal time, then cumulative signed work must satisfy

`int_0^T W_3 dt -> +infinity`.

Subtracting the finite low-output pieces yields, for every fixed `K`,

`int_0^T W_grad,>K dt -> +infinity`,

and

`int_0^T W_sol,>K dt -> +infinity`.

Thus both exact representations contain ultraviolet sequences of **productive positive pressure-work shells**. RD014 allows the two productive sequences to remain separated in scale/time; R28 does not assume otherwise.

## 11. Exact live frontier after E28

The earlier E23 frontier was two largely separate channel problems. E28 reduces it to a more constrained singular mechanism.

A hypothetical singular trajectory compatible with this proof spine must simultaneously sustain:

1. divergent scale-critical balanced action
   `A_bal=int U min(||PL||_2^2,||QL||_2^2)dt`;
2. unbounded net positive pressure work above every fixed Fourier cutoff in the gradient representation;
3. unbounded net positive pressure work above every fixed Fourier cutoff in the solenoidal representation;
4. possible scale/time separation of the two representations, because RD014 rules out assuming statewise same-shell balance.

The load-bearing open problem is therefore:

> **Prove that actual Navier–Stokes dynamics cannot sustain this balanced/productive dual-ultraviolet mechanism for arbitrary smooth periodic data, or prove that it forces a known endpoint continuation criterion.**

Possible mechanisms still worth attacking include:

- frequency-local complementarity identities between the two pressure-work representations;
- triad/helical coupling between R17 bandwidth production and R24 longitudinal strain;
- commutator/paraproduct cancellation retaining the exact pointwise orthogonality `(omega×u)·u=0`;
- concentration-compactness/rigidity for a minimal object carrying two separated productive UV sequences.

No such arbitrary-data closing theorem is proved at E28.

## 12. W5 continuation gate

The fresh continuation world `world_e3fcf95bd269` currently records:

- `critical_unknowns=1`;
- `verifications=7`;
- `fresh_context_verifications=2`;
- `robustness_worlds=10`;
- two high-severity falsification families, including RD013 and RD014;
- best candidate: R27 balanced-min criterion + R28 dual productive-UV escape;
- gate: `FAILED`.

The continuation world also has formal W5 residency/diversity requirements still unmet because it is a newly reconstructed runtime. Those process blockers are distinct from the mathematical blocker. The mathematical blocker is intentionally left unresolved.

## 13. Nonconvergence statement

W5-E28 does **not** prove an a-priori arbitrary-data bound on `A_bal`, does not rule out the dual productive ultraviolet pressure-work mechanism, does not close NS-P01..NS-P12, and does not match a complete Clay alternative.

**W5-E28 is a verified research checkpoint, not a solution of the Navier–Stokes Millennium Prize Problem.**
