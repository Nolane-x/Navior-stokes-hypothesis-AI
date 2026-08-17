# W5 Research Protocol — 3D Navier–Stokes

## 1. Frozen target

Primary target is Clay statement (B): for every smooth, periodic, divergence-free initial velocity `u_0` on `R^3/Z^3`, zero forcing and viscosity `nu>0`, prove existence of a smooth periodic solution `(u,p)` for all `t>=0`.

A route may switch to Clay statements (A), (C), or (D) only through an explicit representation-shift record. No statement weaker than one of the four official Clay alternatives counts as closure.

### 1.1 Canonical Galilean normalization

Clay statement (B) does not impose zero spatial mean. For unforced periodic Navier–Stokes, however, the spatial mean

`m = integral_{T^3} u_0(x) dx`

is conserved. The exact Galilean transformation

`v(x,t)=u(x+m t,t)-m`,

`pi(x,t)=p(x+m t,t)`

produces a periodic divergence-free solution of the same equation with zero spatial mean, and the inverse transformation recovers `u`. Global smoothness is therefore equivalent in the original and zero-mean frames.

The project freezes the **zero-mean Galilean frame** as the canonical frame for every diagnostic depending on velocity amplitude or direction, including

- `rho=|u|`;
- high-amplitude thresholds and tail sets;
- iso-speed level sets and component fluxes;
- conditional expectations modulo functions of `rho`;
- vector-potential identities using `curl^{-1}u`;
- amplitude commutators such as `Q(rho u)=[Q,rho]u`.

These quantities are not Galilean invariant. A proof may not compute them in one frame and invoke a theorem established in another without an explicit transformation of the diagnostic itself. R21 and C001 record an exact travelling-shear falsifier showing why this discipline is load-bearing.

Fourier/curl statements that require a periodic vector potential must also state the zero-mean hypothesis explicitly; the removed harmonic constant mode is not a periodic curl.

## 2. Scaling audit

For viscosity normalized to `nu=1`, the Euclidean scaling is

`u_lambda(x,t)=lambda u(lambda x, lambda^2 t)`, `p_lambda(x,t)=lambda^2 p(lambda x,lambda^2 t)`.

Every candidate norm/estimate must be labeled:

- subcritical,
- critical,
- supercritical,

with the scaling exponent shown. Any proposed global proof that closes only through a supercritical bound must state the additional mechanism that defeats concentration.

## 3. Proof-obligation ladder

A regularity route must close all of the following:

- **NS-P01 Local theory:** precise class in which a unique smooth/maximal solution exists.
- **NS-P02 Continuation criterion:** an explicit criterion whose boundedness extends the solution beyond a putative `T*`.
- **NS-P03 Critical bridge:** derive the continuation quantity from scale-critical or stronger information without circularity.
- **NS-P04 Nonlinear structure:** use identities/geometry specific to the true incompressible Navier–Stokes nonlinearity and Leray projection.
- **NS-P05 Pressure:** control pressure/nonlocal Riesz effects in the same scale regime.
- **NS-P06 Concentration:** rule out concentration/escape scenarios compatible with the energy inequality.
- **NS-P07 Degenerate cases:** cover zero sets, alignment degeneracies, symmetry-breaking perturbations and endpoint exponents used by the argument.
- **NS-P08 Limit operations:** justify weak/strong convergence, compactness, differentiation, Fourier rearrangement, and limit exchanges.
- **NS-P09 Arbitrary data:** remove all smallness, symmetry, sign, analyticity-radius, spectral-support, and finite-mode restrictions unless they are proved dynamically for arbitrary smooth data.
- **NS-P10 Bootstrap:** convert the closed critical estimate into full smoothness for all time.
- **NS-P11 Independent verification:** fresh-context reconstruction of every load-bearing lemma.
- **NS-P12 Clay match:** final theorem is checked line-by-line against an official Clay statement.

A blow-up route has the dual burden: construct smooth admissible data/forcing in one Clay breakdown statement and prove that no global smooth solution in the required class exists.

## 4. Automatic rejection rules

Reject any route containing one of these unsupported jumps:

1. finite numerical resolution => continuum regularity;
2. bounded `L^2` energy => bounded critical norm;
3. shell-model or averaged-operator behavior => true Navier–Stokes behavior;
4. a regularity criterion => proof of its hypothesis;
5. almost-everywhere regularity => no singular points;
6. small-data theorem => arbitrary-data theorem;
7. axisymmetric / 2D / helical / Beltrami special case => general 3D case;
8. an inequality with a coefficient depending on the unknown blow-up norm => closed a priori bound;
9. assuming pressure is local or sign-definite;
10. using Euler invariants as if viscosity preserved them exactly;
11. assuming a self-similar singularity exhausts all possible blow-up mechanisms;
12. invoking compactness without a topology strong enough to pass the nonlinearity;
13. relying on hidden regularity to justify a step whose purpose is to prove regularity;
14. post-hoc tuning of an experiment after seeing the result without recording the change;
15. switching Galilean frames after defining a speed/amplitude/iso-speed diagnostic without transforming that diagnostic explicitly.

## 5. Falsification-first route scoring

Each route receives:

- a mechanism statement;
- a critical quantity;
- a predicted inequality or obstruction;
- a smallest falsifier;
- a decisive symbolic/numerical experiment if available;
- a scope tag (`heuristic`, `computational`, `verified-partial`, `exact-theorem`, `candidate-global-proof`);
- a dependency list.

Routes with a verified counterexample move to `discarded/` but remain in the ledger.

## 6. Computational evidence

Computation may:

- find counterexamples to candidate inequalities;
- discover exact identities;
- certify finite-dimensional inequalities with interval/rational arithmetic;
- test scaling and constants;
- explore triad/shell geometry;
- search for candidate barriers.

Computation may not by itself certify global regularity of the PDE. Any finite-dimensional theorem must include a continuum-transfer obligation before it can support closure.

## 7. Literature independence and provenance

Primary-source baselines are preferred. A claim copied through multiple secondary sources counts as one evidence lineage. Any alleged novelty must be phrased conservatively until checked against the literature.

Published conditional regularity criteria are maintained as independent challengers where useful. They do not become proof steps until their hypotheses are derived a priori for arbitrary smooth data.

## 8. Nolane World closure policy

World depth is `W5`. The resident model cannot grant itself closure. The repository may use `verified-partial` for independently checked lemmas. `SOLVED` is forbidden unless:

- all NS-P01..NS-P12 obligations are closed,
- adversarial falsification finds no surviving gap,
- independent verification reproduces the proof,
- the Nolane World convergence gate passes,
- the final theorem exactly matches a Clay alternative.

An internal World gate score is a research-governance diagnostic, **not a percentage of the Millennium problem solved**.

Until every closure condition above is met, the canonical status is `NONCONVERGED_PARTIALS_ONLY`.
