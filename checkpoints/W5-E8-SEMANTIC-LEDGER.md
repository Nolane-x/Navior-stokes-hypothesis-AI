# W5-E8 Semantic Research Ledger

**World:** `world4_05c73a9403ba4574`  
**Runtime:** Nolane World `0.5.0` Verified Distributed Cognition  
**Depth:** `W5`  
**Epoch:** `8`  
**Canonical status:** `NONCONVERGED_PARTIALS_ONLY`  
**Clay claim:** **NOT SOLVED**

## Epoch-8 convergence gate

After the P04 true-Navier–Stokes tangent challenger and the exact R11 scaling theorem were independently gated by GitHub Actions run `32014074332`, Nolane World accepted the artifact as material novelty and advanced to epoch 8.

The convergence gate still returned

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

Therefore no theorem or computation in this checkpoint may be promoted to a proof of 3D Navier–Stokes global regularity.

## New epoch-8 results

### P04 — true Navier–Stokes tangent challenger

P04 froze the P03 high-coherence Fourier shape `v`, amplitudes

`a in {0.5,1,2,4,8}`,

viscosity `nu=1`, and measured the directional derivative of the projected Lamb coherence

`kappa_L = <Q(omega×u),Q(|u|u)> / (||Q(omega×u)||_2 ||Q(|u|u)||_2)`

along the true spectral Navier–Stokes tangent

`F_NS(u)=Delta u-P[(u·grad)u]`.

All five amplitudes had robust **positive** derivatives at both N=48 and N=64. At N=64 the mean derivatives were

```text
a=0.5 : +3.7344154154
a=1   : +3.5066161710
a=2   : +3.0510176814
a=4   : +2.1398207017
a=8   : +0.3174267395
```

All three-stencil relative spreads were below `1.5e-7`, far inside the preregistered `5e-3` gate.

Frozen verdict: `H-nonrepel`.

This is finite-dimensional numerical evidence, not a continuum proof.

### RD006 — simple instantaneous angle repulsion is not viable

P04 falsifies, in the tested finite representation, the simple local hypothesis

`high kappa_L => d_NS kappa_L/dt < 0`.

The actual Navier–Stokes tangent initially moves the P03 state toward *higher* projected Lamb coherence, not lower coherence.

This does **not** indicate blow-up. It only removes a one-variable local angle-Lyapunov shortcut.

### R11 — exact scaling law for degree-zero diagnostics

For every differentiable positive-amplitude-invariant diagnostic `Phi(a u)=Phi(u)`, with

`F_nu(u)=nu Delta u-B(u,u)`, `B=P[(u·grad)u]`,

we have the exact amplitude-only tangent law

`D Phi_{a u}[F_nu(a u)]`

`= nu D Phi_u[Delta u] - a D Phi_u[B(u,u)]`.

Thus the tangent derivative is affine in amplitude when spatial shape is fixed.

For the integer torus concentration scaling

`S_m u(x)=m u(m x)`, `m in N`,

the Navier–Stokes vector field obeys

`F_nu(S_m u)=m^3 [F_nu(u)](m x)`.

For a scale-invariant diagnostic such as `kappa_L`,

`D Phi_{S_m u}[F_nu(S_m u)]`

`= m^2 D Phi_u[F_nu(u)]`.

Hence any rigorously certified tangent sign is preserved under every integer Navier–Stokes concentration scaling. R11 is exact, but P04's base sign remains numerical rather than interval-certified.

## Independent verification lineage

The P04 result initially encountered a failed GitHub run because the first replay checker required cross-hardware FFT agreement at an unrealistic ~1e-10 tolerance. The script SHA-256 provenance check had already passed. The replay tolerance was changed to a numerically meaningful cross-hardware tolerance **without changing the preregistered scientific sign/spread gate, input field, amplitudes, resolutions, stencil, or result**.

- `32013974768` — P04 cross-hardware replay: **SUCCESS**.
- `32014074332` — P04 replay + exact R11 homogeneity audit: **SUCCESS**.

## Current strongest positive reduction

The strongest live analytic target remains R08.

Let

`M_*(t)=nu^2/[12 C_H^2 ||u(t)||_(3/2)]`.

Define the scale-invariant high-amplitude projected-Lamb tail action

`A_tail(T)=int_0^T ||u(t)||_(3/2)`

` * ||Q(1_{|u|>M_*(t)} (omega×u))||_2^2 dt`.

R08 proves that finite `A_tail(T)` yields an a priori bound on the critical `L^3` norm and integrated `D_3` dissipation. The Millennium problem is **not** closed because the project has not proved

`A_tail(T)<infinity`

for arbitrary smooth periodic initial data up to every finite time.

## Current negative knowledge

The program has now ruled out or sharply weakened several tempting shortcuts:

1. **RD001:** no universal fixed-constant statewise pressure absorption `W_3<=C D_3`;
2. **RD002:** no projected Lamb-coherence half-gap `kappa_L<=1/2` in the tested expanded Fourier family;
3. **RD003:** no generic fixed quadratic functional can make convection strictly dissipative on every state;
4. **RD004:** the raw velocity-amplitude weight need not lie in Muckenhoupt `A_2`, even along an exact global smooth shear;
5. **RD005:** smooth incompressible solutions do not force universally nice iso-speed topology/geometry;
6. **RD006:** dangerous projected Lamb coherence need not be instantaneously repelled by the true Navier–Stokes tangent.

These no-gos are useful because they prevent the W5 program from repeatedly rediscovering invalid closure mechanisms.

## Epoch-8 frontier

The next theorem must use more than one instantaneous normalized angle. Highest-priority routes are:

1. prove a true-Leray/helical triad restriction on sustained growth of the R08 high-amplitude projected-Lamb tail;
2. derive a time-integrated cancellation between defect **size**, coherence, and high-amplitude support;
3. control the R09/R10 pressure quotient only on the R08 high-speed levels, including inter-component pressure-offset × flux covariance;
4. formulate a minimal-blow-up/rescaling object for which divergence of `A_tail` is mandatory, then seek a Liouville contradiction using the Lamb/Helmholtz structure;
5. independently reconstruct the R06–R11 chain in fresh context and continue adversarial counterexample search.

The canonical status remains `NONCONVERGED_PARTIALS_ONLY`.
