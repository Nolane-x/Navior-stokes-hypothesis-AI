# RD020 — Lacunary critical-burst cascade defeats energy-only closure

**Status:** `exact scaling-budget countermodel / route guard`  
**Depends on:** RD008, R08, R28, R38–R40  
**Scope:** an abstract cascade of rescaled smooth profiles; **not** an exact Navier–Stokes solution and not a blow-up construction

RD008 proves the one-bubble scaling obstruction: a parabolically rescaled critical structure has scale-invariant critical action while its kinetic-energy/integrated-enstrophy budget decays like one inverse frequency.

R38–R40 reveal a stronger terminal pattern: a hypothetical singular trajectory may carry arbitrarily large critical/productive work on shrinking packets even though the remaining unweighted enstrophy budget tends to zero and all resolved finite output catalogs evacuate.

RD020 shows that this pattern is fully compatible with the Navier–Stokes **scaling budget alone**. Therefore no argument using only energy/enstrophy accounting plus the R40 evacuation statement can close the problem. A successful theorem must couple successive bursts through genuine PDE structure, critical compactness, or many-body cancellation.

## 1. Prototype critical packet

Take a fixed smooth divergence-free spacetime profile `U(x,s)` supported in a bounded spatial chart and time interval `0<s<1`. It need not solve Navier–Stokes; it is a scaling probe.

Assume its chosen critical pressure-work/tail functional has a finite nonzero value

> `W_* > 0`,

and write its integrated enstrophy budget as

> `Q_* = int_0^1 ||grad U(s)||_2^2 ds < infinity`.

The standard parabolic rescaling at frequency `N` is

> `U_N(x,t)=N U(Nx,N^2(t-t_0))`.

On a sufficiently small chart this can be embedded in the torus for the purpose of homogeneity testing, as in RD008.

## 2. Exact scaling of one burst

The rescaled duration is

> `Delta t_N = N^(-2)`.

The kinetic energy scales as

> `||U_N||_2^2 = N^(-1)||U||_2^2`.

The integrated enstrophy scales as

> `int ||grad U_N||_2^2 dt = N^(-1) Q_*`.

Every scale-critical integrated pressure-work/tail quantity in the R06/R08/R28 spine has exponent zero, so

> `W(U_N)=W_*`.

Thus one burst pays energy/dissipation cost `O(N^-1)` but contributes `O(1)` critical work.

## 3. Lacunary cascade

Choose a strictly increasing frequency sequence `N_j` satisfying

> `sum_j N_j^(-1) < infinity`

and

> `sum_j N_j^(-2) < infinity`.

For example

> `N_j=2^(j^2)`

or even a much more rapidly growing sequence.

Place the rescaled packets on disjoint time intervals with lengths `N_j^-2`, ordered so that their right endpoints accumulate at one finite terminal time `T*`.

Ignoring interactions between packets — this is why RD020 is a budget countermodel rather than a PDE solution — the formal cumulative budgets are

> `sum_j Q_* N_j^(-1) < infinity`,

while

> `sum_j W_* = infinity`.

Even more sharply, after the start of burst `J`,

> `sum_(j>=J) Q_* N_j^(-1) -> 0`

as `J->infinity`, whereas

> `sum_(j>=J) W_* = infinity`

for every `J`.

Hence **vanishing terminal enstrophy budget and divergent terminal critical work are perfectly compatible with scaling**.

## 4. Compatibility with R40-style frequency evacuation

Let `L_J` be any prescribed finite output resolution. Because the cascade frequencies may be chosen recursively, impose

> `N_J > L_J`

and, if desired, an arbitrarily large gap

> `N_J / L_J -> infinity`.

Then every late prototype burst sits beyond the prescribed resolved scale while its critical work remains `W_*` and its energy cost continues to shrink.

Thus an arbitrarily lacunary critical-burst cascade reproduces the qualitative budget signature left alive by R40:

- resolved finite frequencies evacuate;
- terminal unweighted dissipation tends to zero;
- critical productive work remains non-summable;
- active scales can run to infinity arbitrarily rapidly at the level of scaling bookkeeping.

## 5. What RD020 falsifies

RD020 kills any proposed closing argument whose only inputs are

1. finite total kinetic energy;
2. finite total integrated enstrophy;
3. shrinking terminal time intervals;
4. R40-type frequency evacuation;
5. scale homogeneity,

and which claims these facts alone force summability of the critical pressure/Lamb work.

The lacunary model satisfies the same homogeneity budget while violating that conclusion.

It also shows why the statement

> `the terminal enstrophy tail tends to zero, therefore infinitely much critical work is impossible`

is false on scaling grounds.

## 6. What RD020 does not falsify

RD020 is **not** a Navier–Stokes trajectory. In particular it ignores the constraints that may be decisive:

- the nonlinear evolution coupling one burst to the next;
- pressure nonlocality across scales;
- helical pair and many-body structure from R37;
- conservation/balance laws linking spin sectors;
- backward/forward uniqueness;
- analyticity and parabolic propagation between bursts;
- concentration-compactness or minimal-element rigidity;
- spatial endpoint-measure constraints such as atomic full-tail rigidity.

Those are precisely the kinds of structure a successful proof must exploit.

## 7. Post-RD020 frontier

After R40 + RD020, the research target should no longer be another energy/enstrophy tail estimate. The missing theorem must obstruct a **sequence of scale-critical bursts** that becomes increasingly fine and increasingly cheap in the subcritical energy budget.

Two genuinely load-bearing possibilities remain:

1. **inter-burst rigidity / scale-time law:** prove that an actual Navier–Stokes trajectory cannot move between the required escaping scales with the timing/amplitude pattern needed for infinitely many critical bursts;
2. **within-burst many-body depletion:** prove that R37-admissible helical interactions cannot generate `O(1)` positive common pressure work at a normalized critical burst once the balanced P/Q constraints are imposed.

This sequential route guard is stronger than RD008's one-bubble scaling observation and is tailored to the E40 terminal-packet frontier.
