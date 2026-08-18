# R39 — Finite-catalog spacetime total-variation synchronization

**Status:** `exact conditional extraction theorem / verified-partials target / not a global-regularity proof`  
**Depends on:** R24, R28–R30, R32, R38  
**Clay status:** **NOT SOLVED**

R38 synchronizes the two productive Helmholtz pressure-work representations uniformly over every sharp radial cutoff in a growing hierarchy, and therefore over every signed radial shell.  The remaining warning in E37 was that uniform signed cumulative control does not by itself imply total-variation control: arbitrarily rapid positive/negative shell oscillation could in principle remain hidden.

R39 removes that warning on every **prescribed finite Fourier output catalog**.  The upgrade is not a consequence of signed-tail cancellation.  It uses a separate coefficientwise estimate coming only from finite energy and the terminal enstrophy tail.  The conclusion is a spacetime `L^1_t ell^1_k` estimate for the P/Q representation mismatch itself.

The unresolved object after R39 is therefore not a resolved-frequency mismatch.  It is the common productive mode carried by an output-frequency tail that may escape every prescribed finite catalog, together with the many-triad accumulation inside each output mode.

## 1. Fourier convention and output-mode work

Let `Omega=T^3` have volume `V`, and use

`fhat(k)=V^{-1} int_Omega f(x) exp(-i k·x) dx`.

Set

`L=omega×u`,

`G=|u|u`.

For every nonzero Fourier mode `k`, let `P_k,Q_k` be the solenoidal/gradient Helmholtz projections.  Define the real modewise pressure-work contributions

`w_grad,k(t)=V Re[(Q_k Lhat(k)) · conjugate(Q_k Ghat(k))]`,

`w_sol,k(t)=-V Re[(P_k Lhat(k)) · conjugate(P_k Ghat(k))]`.

Because `P_k,Q_k` are orthogonal complementary projections,

> `d_k(t):=w_grad,k(t)-w_sol,k(t)`
>
> `=V Re[Lhat(k) · conjugate(Ghat(k))]`.

This identity is exact mode by mode.  No summation over `k` and no radial shell cancellation is used.

The full sum satisfies `sum_k d_k=0`, since `L·G=|u|(omega×u)·u=0` pointwise, but R39 will not use cancellation between different modes.

## 2. Frequency-independent coefficient bound

Let

`E0 = sup_(0<=t<T*) ||u(t)||_2`,

which is finite by the energy equality/inequality on the smooth preterminal branch.  For every `k`, Cauchy–Schwarz and `||G||_1=||u||_2^2` give

> `|Lhat(k)| <= V^{-1} ||omega||_2 ||u||_2`,

and

> `|Ghat(k)| <= V^{-1} ||u||_2^2`.

Therefore

> `|d_k(t)| <= V^{-1} E0^3 ||omega(t)||_2`.

The crucial point is that the bound is **independent of the location of `k`**.  Only the number of modes in a finite catalog will appear.

## 3. Spacetime total variation on an arbitrary finite catalog

Let `F subset Z^3\{0}` be finite, and let `I=[a,b] subset [a,T*)`.  Summing the absolute modewise mismatch before integrating in time gives

> `int_I sum_(k in F) |d_k(t)| dt`
>
> `<= V^{-1}|F| E0^3 int_I ||omega(t)||_2 dt`.

Define the terminal enstrophy tail

`q(a)=int_a^{T*} ||omega(t)||_2^2 dt`.

Then Cauchy–Schwarz in time yields the exact finite-catalog estimate

> `int_I sum_(k in F) |d_k(t)| dt`
>
> `<= V^{-1}|F| E0^3 |I|^(1/2) q(a)^(1/2)`
>
> `<= V^{-1}|F| E0^3 [(T*-a) q(a)]^(1/2)`.

Because both `T*-a -> 0` and `q(a)->0` as `a↑T*`, the final factor tends to zero.

This is stronger than a signed integrated estimate.  It controls the **total variation in time and output mode** of the representation mismatch on `F`; temporal sign cancellation cannot rescue a counterexample inside the resolved catalog.

## 4. Simultaneous extraction with R38

Assume the same hypothetical singular endpoint used by R28/R30/R38.  Prescribe arbitrarily:

- finite output catalogs `F_n` (their cardinalities may grow arbitrarily fast);
- radial ceilings `L_n->infinity`;
- productive thresholds `M_n->infinity`;
- R38 mismatch tolerances `epsilon_n->0`;
- finite-catalog TV tolerances `eta_n->0`;
- terminal-window bounds `delta_n->0`.

R38 already chooses a terminal start sufficiently late to satisfy its uniform radial-cutoff mismatch requirement.  Move that start farther toward `T*`, if necessary, until also

> `T*-a_n <= delta_n`

and

> `V^{-1}|F_n| E0^3 [(T*-a_n) q(a_n)]^(1/2) <= eta_n`.

This is always possible because `F_n` is finite for each fixed `n` and `[(T*-a)q(a)]^(1/2)->0`.

R38's finite-family terminal divergence argument then selects one `b_n in (a_n,T*)` so that on `I_n=[a_n,b_n]`, simultaneously for every `K<=L_n`,

`A_grad^K(I_n)>=M_n`,

`A_sol^K(I_n)>=M_n`,

`A_bal^K(I_n)>=M_n`,

and

`|A_grad^K(I_n)-A_sol^K(I_n)|<=epsilon_n`.

At the same time R39 gives

> `int_(I_n) sum_(k in F_n)`
>
> `|w_grad,k(t)-w_sol,k(t)| dt <= eta_n`.

Thus R38 productivity and hierarchy synchronization are compatible with arbitrarily strong **mode-resolved spacetime total-variation synchronization** on any preassigned finite catalog.

## 5. Growing Fourier-ball corollary

Take

`F_n={k in Z^3\{0}: |k|<=L_n}`.

Then

> `int_(I_n) sum_(0<|k|<=L_n)`
>
> `|w_grad,k-w_sol,k| dt -> 0`.

Consequently every partition of the resolved Fourier ball inherits the same vanishing discrepancy.  This includes, without additional argument,

- every radial shell;
- every angular sector;
- every finite union of lattice modes;
- any mixed radial/angular partition chosen before the packet is extracted.

There is no factor equal to the number of partition cells after the `ell^1_k` estimate has been established: the estimate already controls the sum over individual modes.

R38 also gives

`|A_grad^L_n(I_n)-A_sol^L_n(I_n)|<=epsilon_n`

for the unresolved tail `|k|>L_n`.  Therefore, if all modes inside the ball are kept as individual atoms and the entire exterior is collapsed to one tail atom, the total-variation distance between the two resulting signed work measures is at most

> `eta_n+epsilon_n -> 0`.

## 6. What R39 closes from E37

R39 removes one E37 ambiguity:

> P/Q synchronization cannot fail through arbitrarily oscillatory signed work on a **resolved finite output catalog**.

The two representations become indistinguishable there even before time integration cancellation is used.

In particular, RD014-style output-shell separation cannot remain a macroscopic signed-work mechanism on the resolved prefix of the R39 packets.  RD014 remains a valid instantaneous Lamb-energy counterexample and is not contradicted.

## 7. What R39 does not close

R39 deliberately does **not** claim any of the following.

1. **No tightness.**  The productive common mode may live at frequencies much larger than `L_n`; the exterior tail is only one aggregated atom.
2. **No common-mode bound.**  `w_grad,k` and `w_sol,k` may be almost identical while both are arbitrarily large with the same sign.
3. **No triadwise TV bound.**  At a fixed output mode `k`, many helical input pairs may still accumulate coherently.  R37 constrains each pair geometrically but does not permit summing pairwise minima.
4. **No positivity.**  The individual common-mode work coefficients remain signed.
5. **No arbitrary-data continuation estimate.**  Nothing here proves finiteness of the critical balanced action or boundedness of `L^3`.

## 8. Sharpened post-R39 frontier

Combining R37–R39, a hypothetical singular mechanism can no longer rely on a persistent mismatch between the two Helmholtz work representations on any prescribed growing finite collection of output modes.

The live obstruction is therefore sharpened to

> **an escaping common productive tail whose individual output modes are built from coherent many-triad R37-admissible helical interactions, while the resolved P/Q work measures synchronize in spacetime total variation.**

A closing theorem must supply either

- a tightness mechanism that prevents the common productive work from outrunning every controlled output catalog; or
- a many-body cancellation/rigidity estimate at each escaping output scale that turns R37 pair geometry into a scale-critical spacetime bound.

This is a narrower target than E37's generic signed-shell-cancellation warning.

## 9. Verification scope

`verification/check_R39_finite_catalog_tv_sync.py` checks the exact P/Q modewise algebra, the finite-catalog `L^1_t ell^1_k` extraction inequality on large randomized synthetic families, growing-catalog tolerance selection, and the partition/one-tail-atom total-variation consequences.

A fresh-context verifier should reconstruct the modewise identity using independent random orthogonal projectors rather than importing the theorem checker.

**R39 is a necessary-structure theorem under the hypothetical singular-endpoint proof spine; it is not a proof of Navier–Stokes global regularity.**
