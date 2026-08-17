# W5-E7 Semantic Research Ledger

**World:** `world4_05c73a9403ba4574`  
**Runtime:** Nolane World `0.5.0` Verified Distributed Cognition  
**Depth:** `W5`  
**Epoch:** `7`  
**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay claim:** **NOT SOLVED**

## Gate verdict

After accepting the R05–R10 representation shift with external attestation from GitHub Actions run `32013320427`, Nolane World returned:

```json
{
  "passed": false,
  "score": 0.08333333333333337,
  "blockers": [
    "insufficient cognitive epochs",
    "critical_unknowns unresolved",
    "fresh verification missing",
    "independent challenger missing",
    "robust/counterfactual worlds insufficient",
    "representation diversity insufficient",
    "material value-of-thought remains",
    "quality floor correctness",
    "quality floor evidence",
    "quality floor robustness",
    "quality floor verification"
  ]
}
```

No result in this checkpoint may be promoted to a Navier–Stokes global-regularity claim.

## Verified structural chain

### R01 — critical `L^3` identity

For smooth periodic incompressible solutions,

`(1/3)d/dt ||u||_3^3 + nu D_3 = W_3`,

with nonnegative amplitude/direction diffusion and

`W_3 = int p u·grad|u|`.

### RD001 — direct pressure absorption no-go

An explicit smooth mean-zero divergence-free family has

`W_3(eps)=(pi/6)eps^2+O(eps^3)>0`.

Amplitude scaling makes `W_3/D_3` unbounded, killing every universal statewise estimate `W_3<=C D_3` with fixed `C`.

### R02–R04 — Helmholtz/Lamb factorization

With `Q=I-P`,

`W_3=<Q[(u·grad)u],Q(|u|u)>`

and more sharply

`W_3=<Q(omega×u),Q(|u|u)>`.

Pointwise orthogonality `(omega×u)·(|u|u)=0` yields the sharp abstract projector bound

`|W_3| <= (1/2)||omega×u||_2 ||u||_4^2`.

### P01–P03 / RD002 — statewise projected-angle challenger

The preregistered expanded P03 challenger found a converged finite Fourier state with

`kappa_L(N=64)=0.5197256482415721`

and post-confirmation

`kappa_L(N=128)=0.519725873321033`.

Thus a candidate universal statewise projected-angle threshold `kappa_L<=1/2` is computationally falsified in that finite family. This does not contradict R04's full-norm half-bound.

### R05 — `L^p` Lamb–Leray complementarity

For `G_p=|u|^(p-2)u`,

`W_p=<Q(omega×u),QG_p>=-<P(omega×u),PG_p>`.

The `p=2` endpoint is protected because `QG_2=Qu=0`; `p=3` is the scale-critical velocity endpoint.

### RD003 — fixed quadratic Lyapunov no-go

For any fixed quadratic functional, its convective derivative is odd under `u->-u`. Therefore it cannot be strictly nonpositive on every state unless the convective contribution vanishes identically. Amplitude scaling then rules out arbitrary-data monotonicity based on a nonzero cubic convection term plus quadratic viscosity.

### R06 — critical Bernoulli/Lamb action

With periodic dual-Sobolev constant `C_H`,

`||Q(|u|u)||_2 <= (C_H/sqrt(2)) ||u||_(3/2)^(1/2) D_3^(1/2)`.

Hence finite

`A_L(T)=int_0^T ||u||_(3/2)||Q(omega×u)||_2^2 dt`

bounds `sup ||u||_3` and integrated `D_3`. `A_L` is scale invariant. **Its finiteness for arbitrary smooth data is unproved.**

### R07 — weighted local Lamb control

For `p>=2`,

`int |u|^(p-4)|omega×u|^2 <= [p/(p-1)] D_p`.

In particular,

`int |omega×u|^2/|u| <= (3/2)D_3`.

Thus the local full Lamb force is diffusion-controlled in a natural weight; the remaining difficulty is nonlocal Helmholtz transfer across a degenerate amplitude weight.

### RD004 — raw amplitude `A_2` route fails

The exact smooth global shear

`u=(exp(-4 pi^2 nu t) sin(2 pi z),0,0)`

has `|u|^{-1}` non-locally-integrable across its nodal planes, so `|u|` is not a Muckenhoupt `A_2` weight. Standard raw-amplitude weighted Riesz transfer therefore cannot be a universal route.

### R08 — intrinsic high-amplitude Lamb-tail reduction

Define

`M_*(t)=nu^2/[12 C_H^2 ||u(t)||_(3/2)]`.

All Lamb contribution from `{|u|<=M_*}` is absorbed into viscosity. The surviving scale-invariant action is

`A_tail(T)=int_0^T ||u||_(3/2)`

` * ||Q(1_{|u|>M_*}(omega×u))||_2^2 dt`.

Finite `A_tail` bounds the critical `L^3` norm. **Proving `A_tail<infinity` for arbitrary smooth data is now the primary analytic bottleneck.**

### R09 — pressure modulo functions of speed

For every admissible scalar function `F`,

`int F(|u|) u·grad|u| = 0`.

Therefore

`W_3=<p-E[p|sigma(|u|)], u·grad|u|>`.

Only pressure fluctuation relative to the amplitude-generated scalar subspace can drive critical `L^3` growth.

### RD005 / R10 — disconnected iso-speed geometry made explicit

Smooth incompressible Navier–Stokes shears can realize arbitrarily complicated speed-level geometry, so no universal 'nice level surface' assumption is allowed.

For a regular level with connected components `Sigma_{s,a}`, R10 decomposes the level pressure work into

1. intra-component pressure oscillation, whose tangential derivative is controlled by projected Lamb/Bernoulli force;
2. inter-component pressure-mean × compensating-flux covariance.

Any iso-speed proof that omits the second term is incomplete on disconnected levels.

## Independent GitHub gates

Successful runs through this checkpoint include:

- `32009509285` — R01/RD001 exact symbolic core;
- `32011037645` — R02–R04 + P01/P02 fresh replay;
- `32011675274` — P03 provenance/replay challenger;
- `32011934665` — R05/RD003 structural core;
- `32012411517` — R07 weighted Lamb structural core;
- `32013141403` — R08/R09/RD004/RD005 structural/adversarial core;
- `32013320427` — R08/R09/R10/RD004/RD005 extended gate after dependency-free R10 replay.

The earlier run `32013256258` failed only because the first R10 checker imported NumPy without installing it; the preceding R08/R09/RD004/RD005 step passed. The checker was replaced by a stdlib-only equivalent and run `32013320427` passed.

## Strongest live frontier

The project has not closed NS-P03/NS-P04/NS-P05/NS-P06. The strongest current positive target is:

> Prove that the scale-invariant high-amplitude projected-Lamb tail action `A_tail(T)` cannot diverge at finite time for an arbitrary smooth periodic Navier–Stokes solution.

Equivalent/supplementary formulations to attack are:

1. control `Q(1_{|u|>M_*}(omega×u))` using exact true-Leray/helical triad geometry;
2. control the quotient pressure `p modulo functions(|u|)` only on high-speed levels;
3. rule out sustained inter-component pressure-offset × flux covariance at the concentration scale;
4. derive a trajectory-dependent cancellation unavailable to arbitrary instantaneous divergence-free fields.

These remain open proof obligations. The W5 gate correctly refuses closure.
