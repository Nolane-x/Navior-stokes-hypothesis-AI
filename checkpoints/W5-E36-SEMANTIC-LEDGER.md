# W5-E36 Semantic Research Ledger

**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay status:** **NOT SOLVED**  
**Target:** periodic 3D incompressible Navier–Stokes, Clay statement (B)  
**Runtime:** Nolane World `0.5.0` / depth `W5`

## 1. Provenance and verification

W5-E35 remains the frozen predecessor checkpoint. E36 continues from its smooth square-partition synchronization frontier and does not reinterpret older World scores as mathematical completion percentages.

Fresh E36 continuation World:

- world id: `world_3757ca3c24da`;
- depth: `W5`;
- gate: `FAILED`;
- critical unknowns: `1`;
- gate record: `verification/W5_E36_gate_result.json`.

The fresh World also reports process blockers such as residency/diversity because this continuation state was newly constructed. Those are distinct from the mathematical blocker and are intentionally not hidden.

GitHub Actions run `32040436862` executed the hardened repository-wide Python verification loop successfully. Its job log records

> `verification_scripts=42`
>
> `PASS verification_scripts=42`.

New E36 individual gates:

- `32040266484` — R36 two-sided separated-frequency commutator null structure;
- `32040402213` — RD018 generic separated-frequency summation barrier;
- `32040436862` — aggregate 42-certificate E36 gate.

Every checker certifies only its declared algebraic/computational/structural scope. None is a global-regularity certificate.

## 2. E35 starting point

E35 reduced the synchronization defect to the smooth commutator

`<[A_K,C_u] omega, |u|u>`,

with

`C_u omega=omega×u`,

and symbol

`T_K(p,q)`

`=[a_K(p+q)-a_K(p)]`

` [omegahat(p)×uhat(q)]`.

R35 proved the one-sided gain

`|a_K(p+q)-a_K(p)|`

`<= min(2||a||_infinity, ||grad a||_infinity |q|/K)`,

so low multiplying-velocity frequency `q` is suppressed by `|q|/K`.

The E35 frontier still listed low-vorticity/high-multiplying-velocity interactions, comparable high-high interactions, and accumulation of many individually small interactions.

## 3. R36 — the smooth commutator has a two-sided low-leg null structure

For every nonzero divergence-free Fourier mode `r`,

`omegahat(r)=i r×uhat(r)`

and therefore

`|omegahat(r)|=|r||uhat(r)|`.

Let

`A_inf=||a||_infinity`,

`L_a=||grad a||_infinity`,

`C_a=max(L_a,2A_inf)`.

R35 already gives

> `|T_K(p,q)|`
>
> `<=L_a (|q|/K)`
>
> ` |omegahat(p)| |uhat(q)|`.

R36 uses the same symbol bound in the opposite velocity/vorticity orientation:

`|a_K(p+q)-a_K(p)| |uhat(q)|`

`<=min(2A_inf/|q|,L_a/K)|omegahat(q)|`

`<=(C_a/K)|omegahat(q)|`.

Since `|omegahat(p)|=|p||uhat(p)|`,

> `|T_K(p,q)|`
>
> `<=C_a (|p|/K)`
>
> ` |uhat(p)| |omegahat(q)|`.

Thus, for any `0<eta<1`, an individual triad with

`|p|<=eta K`

**or**

`|q|<=eta K`

carries an explicit `O(eta)` one-leg suppression in one of the two natural orientations.

Hence an individually full-strength commutator triad can avoid both gains only if

> `|p|>eta K` and `|q|>eta K`.

The previously dangerous E35 regime “low-vorticity-frequency / high-multiplying-velocity” is therefore not individually full-strength. The unsuppressed sector requires two velocity inputs at the active scale or higher.

R36 is triadwise and does not prove that a large number of separated interactions cannot accumulate.

## 4. RD017 — comparable high-high interactions can remain order one

RD017 prevents the false conclusion that R36 makes the whole commutator small as `K->infinity`.

Take

`p=(K,0,0)`,

`q=(0,K,0)`,

with divergence-free polarizations

`uhat(p)=(0,1,0)`,

`uhat(q)=(1,0,0)`.

Then

`omegahat(p)×uhat(q)!=0`.

For the explicit smooth verifier profile

`a(xi)=exp(-|xi|^2)`,

the normalized symbol gap is

> `|a_K(p+q)-a_K(p)|=e^-1-e^-2`,

independent of `K`.

Thus no universal `K`-smallness is available for comparable high-high interactions. The same qualitative obstruction applies to any admissible smooth profile whose values differ at the corresponding normalized points.

RD017 is not a blow-up construction. It is a route guard: the full-strength high-high sector is real and cannot be discarded by the R36 one-leg gain.

## 5. RD018 — generic summation of the separated gain still misses the energy time budget

R36 leaves open whether individually suppressed separated triads can accumulate. RD018 audits the most direct Bernstein–Holder–energy/enstrophy summation template.

Choose

`3/2<=r<=2`,

and `s` by

`1/r=1/2+1/s`.

Using the R36 `L/K` low-leg factor, Bernstein on a low block `L<=K`, dyadic Cauchy–Schwarz and the enstrophy square sum gives

> `||B_sep||_r`
>
> `<=C K^(2-3/r)||omega||_2^2`.

For `G=|u|u`, interpolation between `L^2` energy and `H^1 -> L^6` yields

> `||G||_(r')`
>
> `<=C E0^(2-3/r)||omega||_2^(3/r)`.

Therefore the generic defect estimate is

> `|D_sep|`
>
> `<=C K^(2-3/r) E0^(2-3/r)`
>
> `  ||omega||_2^(2+3/r)`.

Across `3/2<=r<=2`, the time exponent of `||omega||_2` lies in

> `[7/2,4]`.

The first energy inequality controls only

`int ||omega||_2^2 dt`.

Hence this entire generic template fails to make the separated commutator time-integrable from energy/enstrophy alone.

This does not rule out structured paraproduct estimates, weighted `D_3` estimates, balanced-tail arguments, cancellation, Besov/Lorentz refinements, or compactness/rigidity.

## 6. Canonical E36 obstruction

Combining R29–R36 and the no-go ledger, a hypothetical endpoint singular mechanism compatible with this proof spine must now support all of the E35 balanced/productive UV constraints **and** overcome the following new restriction:

1. separated-frequency commutator triads are individually suppressed whenever either velocity leg is below the active scale;
2. generic first-energy Bernstein/Holder summation is insufficient to turn that gain into spacetime integrability;
3. comparable high-high interactions can retain order-one commutator strength;
4. a successful proof must therefore use structure beyond generic energy/enstrophy bookkeeping.

The principal full-strength mathematical sector has narrowed to

> **comparable high-high smooth-commutator interactions plus any structured accumulation of separated interactions that survives the R36 low-leg gains.**

## 7. Exact live frontier after E36

The load-bearing question is now:

> Can the comparable high-high synchronization commutator, together with the residual accumulation of separated interactions, be bounded in a scale-critical spacetime quantity already controlled by Navier–Stokes dissipation and the balanced/productive-UV structure, strongly enough to exclude the R31/R34 terminal packets or force a known continuation criterion?

The most promising interfaces are narrower than at E35:

- retain the weighted `D_3` geometry of R07 instead of replacing it by unweighted enstrophy powers;
- combine R36 with R24 transported-speed / longitudinal-strain structure;
- exploit balanced high-pass action from R30/R34 so the weaker Helmholtz tail enters the estimate rather than being discarded;
- seek cancellation or helicity depletion inside comparable high-high triads using R14–R20;
- use the synchronized terminal packets of R31 in a concentration-compactness/rigidity argument.

A theorem using only “one-leg commutator gain + generic Holder/Bernstein + first energy inequality” is now explicitly excluded by RD018.

## 8. W5 nonconvergence

Fresh World `world_3757ca3c24da` retains

- `critical_unknowns=1`;
- best candidate: R36 + RD017/RD018 narrowing;
- two high-severity attack families: high-high saturation and generic separated-summation failure;
- gate: `FAILED`.

The critical unknown is deliberately unresolved. E36 does not prove a critical summable high-high estimate and does not exclude the productive balanced ultraviolet mechanism for arbitrary smooth data.

## 9. Nonconvergence statement

W5-E36 does **not** prove:

- a-priori finiteness of the balanced high-pass action;
- summability of the smooth synchronization commutator;
- control of comparable high-high interactions;
- rigidity of the terminal packet sequence;
- periodic 3D Navier–Stokes global regularity.

**W5-E36 is a verified research checkpoint, not a solution of the Navier–Stokes Millennium Prize Problem.**
