# R46 — Spatially local common-work scale and singularity-to-ancient bridge

**Status:** `exact internal tail/localisation theorem + primary-literature bridge / not closure`  
**Depends on:** R41–R45, C003  
**External theorem interface:** Albritton–Barker, arXiv:1811.00507v2, Theorems 1.1 and 1.2  
**Clay status:** **NOT SOLVED**

E45 proves that a unit common-work burst has a sharp signed-work upper scale

`Lambda_J=int_J ||u||_infinity^2 ||omega||_2^2 dt`,

but `Lambda_J` still uses a spatial supremum and therefore does not by itself tie the productive work to a spatial concentration set. R46 replaces that coarse step by a genuinely spacetime-local weighted-gradient density and then uses the resulting work-linked large-amplitude points to identify an actual singular point. A primary-source theorem then supplies local `L^3` concentration and a non-trivial ancient blow-up object at that same singular endpoint.

The gain is conceptual and structural:

> the project no longer needs to prove from scratch that a hypothetical endpoint singularity has *some* spatial singular point or *some* non-trivial ancient blow-up object.

The new open problem is sharper: align the project-specific productive-work scales/helical structure with a standard singularity blow-up normalization, or bypass that transfer with many-body depletion.

## 1. Setup

On a preterminal R41 unit common-work burst `J`, let

`rho=|u|`, `G=rho u`, `L=omega×u`,

and

`c_k(t)=(V/2) Re[Lhat(k,t)·conj((Q_k-P_k)Ghat(k,t))]`,

`b_k(J)=int_J c_k(t)dt`.

At the parent cutoff `L0`,

> `sum_(|k|>L0)b_k(J)=1`.

Let

> `q_J=int_J ||omega(t)||_2^2dt`
>
> `=int_J ||grad u(t)||_2^2dt`

in the periodic divergence-free frame.

## 2. Replace the supremum tail scale by a spatially local density

For every output radius `R>0`, the same Parseval step as R45 gives

`sum_(|k|>R)|c_k(t)|`

`<= (1/(2R)) ||L(t)||_2 ||grad G(t)||_2`.

Define

> `X(t)=int_(T^3) |u(x,t)|^2 |grad u(x,t)|^2 dx`.

Two pointwise estimates are enough.

First,

`|omega|^2 <= 2|grad u|^2`,

hence

> `||L||_2^2 <= 2X(t)`.

Second, the weak chain rule gives

`|grad(rho u)| <= |grad rho||u|+rho|grad u|`

and `|grad rho|<=|grad u|`, so

> `||grad G||_2^2 <= 4X(t)`.

Therefore

> `sum_(|k|>R)|c_k(t)| <= sqrt(2) X(t)/R`.

This estimate no longer uses `||u||_infinity`.

## 3. The local weighted-work frequency

Define

> `Sigma_J := sqrt(2) int_J int_(T^3) |u|^2|grad u|^2 dxdt`.

Then Tonelli gives the burstwise full signed tail

> `T_J(R):=sum_(|k|>R)|b_k(J)| <= Sigma_J/R`.

Since

`X(t)<=||u(t)||_infinity^2||grad u(t)||_2^2`,

R46 fits inside the E45 hierarchy:

> `Sigma_J <= sqrt(2) Lambda_J <= sqrt(2) Gamma_J`.

At the unit-burst cutoff,

`1=|sum_(|k|>L0)b_k| <= T_J(L0)`,

so

> `Sigma_J >= L0`.

Thus a singularity-compatible unit burst satisfies the exact spacetime-local lower bound

> `int_J int_(T^3)|u|^2|grad u|^2 dxdt >= L0/sqrt(2)`.

This is stronger spatial information than the R45 supremum consequence alone.

## 4. A work-linked high-amplitude/gradient set must carry macroscopic weighted mass

Let

> `a_J^2 := L0/(2sqrt(2) q_J)`

and define the spacetime set

> `H_J={(x,t) in T^3×J : |u(x,t)|>=a_J}`.

On the complement of `H_J`,

`|u|^2 < a_J^2`,

so

`int_((T^3×J)\H_J)|u|^2|grad u|^2`

`<=a_J^2 q_J=L0/(2sqrt(2))`.

Combining with the R46 lower bound yields

> `int_(H_J)|u|^2|grad u|^2 dxdt >= L0/(2sqrt(2))`.

In particular `H_J` is nonempty.  Therefore every unit burst contains an actual spacetime point `(x_J,t_J)` satisfying

> `|u(x_J,t_J)| >= sqrt[L0/(2sqrt(2)q_J)]`.

Along the R41 diagonal extraction,

`L0->infinity`, `q_J->0`, and `J` approaches the terminal time `T*`. Hence

> `|u(x_J,t_J)|->infinity`,
>
> `t_J->T*`.

Unlike an arbitrary global supremum point, this point is selected from a set that carries a fixed fraction of the **work-forced amplitude-weighted gradient mass**.

## 5. The work-linked centers accumulate at an actual singular spatial point

The torus is compact, so after passing to a subsequence

> `x_J -> x* in T^3`.

Suppose `(x*,T*)` were regular. Then by the definition/local characterization of a regular point there would exist a parabolic neighborhood

`B_r(x*)×(T*-delta,T*)`

on which `u` is bounded. For all sufficiently late bursts, `(x_J,t_J)` lies in that neighborhood, contradicting

`|u(x_J,t_J)|->infinity`.

Therefore

> **`(x*,T*)` is a genuine interior singular point of the hypothetical periodic solution.**

This implication is internal and elementary once the R46 work-linked point sequence has been extracted.

## 6. Imported PDE theorem: local critical concentration at the same singular point

The smooth preterminal periodic solution, restricted to a sufficiently small Euclidean chart around `x*`, is an interior suitable weak solution. Positive constant viscosity may be normalized to one by the standard deterministic rescaling.

Albritton–Barker, arXiv:1811.00507v2, Theorem 1.1, proves for the stated suitable-solution class that an interior singular point forces the local critical norm to diverge in every fixed neighborhood. Applied here, for every sufficiently small fixed `r>0`,

> `||u(t)||_(L^3(B_r(x*))) -> infinity`
>
> as `t -> T*_-`.

This is a primary-literature import, not an internally reproved theorem. The exact source/scope interface is recorded in

> `sources/R46_albritton_barker_interior_singularity_ancient_bridge.md`.

## 7. Imported PDE theorem: a non-trivial mild bounded ancient solution exists

The same paper, Theorem 1.2, states that an **interior singularity** of the suitable solution class generates

> a non-trivial mild bounded ancient Navier–Stokes solution on `R^3`

as a blow-up limit of the original solution.

Therefore, under the finite-time singularity hypothesis already assumed throughout the proof-by-contradiction spine, R46 closes a previously vague structural gap:

> **the singular endpoint identified by the work-linked R46 centers has a non-trivial ancient blow-up object available by established PDE theory.**

No new claim of originality is made for the imported ancient-solution theorem.

## 8. Why this is not the final compactness theorem

The Albritton–Barker blow-up normalization is not identified by R46 with the project-specific scales

- `R_theta` from R43;
- `Lambda_J` from R45/C003;
- `Sigma_J` from R46;
- the R37 helical common-mode geometry.

Thus existence of an ancient solution does **not** imply that the normalized R41–R45 common-work measure, spectral multiplicity, or helical depletion survives in that limit.

The next bridge is now sharper and dimensionless. For an amplitude-based blow-up scale `A_J` and productive output scale `R_theta`, define for example

> `Chi_theta(J)=R_theta(J,L0)/A_J`.

To transfer productive spectral structure into an amplitude-normalized ancient limit, one needs quantitative control of this or an equivalent alignment parameter, or a different rescaling built directly from the productive work that has PDE compactness.

RD024 shows that the scalar inequalities through R46 permit both `Chi_theta->0` and `Chi_theta->infinity`; alignment is not a formal corollary.

## 9. Canonical post-R46 frontier

R46 changes the compactness program from

> `find a spatial singular object somehow`

into

> `align the already-known ancient blow-up object with the productive-work/helical scales`.

The material routes are now:

1. **scale alignment:** prove `R_theta`, `Sigma_J`/`Lambda_J`, and an amplitude/ancient blow-up scale remain comparable on a subsequence;
2. **transfer theorem:** show R37–R45 common-work structure survives an appropriate singularity rescaling even without full scale comparability;
3. **ancient rigidity:** after transfer, use a Liouville/backward-uniqueness/Oseen argument to exclude the resulting structured ancient solution;
4. **many-body bypass:** prove R37 pairwise depletion plus R42 multiplicity already forbids the unit bursts, avoiding the ancient limit.

## 10. Verification scope

Internal R46 inequalities and extraction logic are checked by

- `verification/check_R46_local_weighted_work_scale.py`;
- `verification/fresh_verify_e46_local_work_grid.py`.

The singular-point subsequence/regular-neighborhood contradiction is checked as logical extraction code, but no finite script is represented as a proof of Albritton–Barker Theorems 1.1/1.2. Those theorems are explicitly imported from the primary source.

RD024 has its own exact scalar countermodel checker.

**R46 is a verified-partial bridge only after its CI and repository-wide gates pass. It does not prove global regularity.**
