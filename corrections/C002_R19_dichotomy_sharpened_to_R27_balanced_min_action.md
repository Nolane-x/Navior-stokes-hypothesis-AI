# C002 — R19 channel dichotomy sharpened to R27 balanced minimum-action co-divergence

**Status:** `canonical sharpening / prior theorem remains valid but non-sharp`  
**Affects:** R19, R26  
**Canonical replacement:** R27

R19 proved the valid necessary statement that divergence of the full physical Lamb action forces

`A_sol=infinity` or `A_grad=infinity`, or both.

R26 then proved a stronger endpoint consequence: finiteness of either individual critical channel action controls the same `L^3` barrier, so a singular trajectory in this proof framework must have

`A_sol=infinity` **and** `A_grad=infinity`.

R27 sharpens the statement again. The same critical `L^3`-diffusion left-hand side admits both a solenoidal and a gradient upper bound. After removing the invisible constant mode of `G=|u|u`, the solenoidal estimate is homogeneous and scale critical. Therefore the left side is bounded by the pointwise minimum of the two channel bounds.

Define

`A_bal(T)`

`= int_0^T ||u||_(3/2)`

`  min( ||P(omega×u)||_2^2, ||Q(omega×u)||_2^2 ) dt`.

R27 proves:

> finite `A_bal(T)` implies an a-priori finite `L^infinity_t L^3_x` bound and integrated `D_3` on `[0,T]`.

Consequently, within the R01/R06 endpoint continuation framework, a finite-time singularity must satisfy

> `A_bal(T*)=infinity`.

This implies both individual channel actions diverge, but is strictly stronger: the weaker channel at each time must itself accumulate non-summable critical mass. Purely separated alternation in which one channel is always negligible cannot support the singular mechanism unless the minority contribution is still nonintegrable.

## Canonical interpretation

The valid decomposition and physical meanings in R19 remain unchanged:

- `P(omega×u)` is the solenoidal/dynamical channel;
- `Q(omega×u)=-grad B` is the Bernoulli-gradient channel;
- both are scale critical;
- divergent channel action escapes every fixed Fourier cutoff.

What is superseded is only R19 Section 1's **sharpness** and the final framing of the frontier.

The canonical post-R27 frontier is no longer:

> close S and G separately, or show one controls the other.

It is:

> exclude or control a balanced high-output ultraviolet Lamb cascade for which even the weaker Helmholtz channel carries non-summable critical action.

R25 additionally proves fixed low-output pressure work is time-integrable, so the surviving obstruction is genuinely ultraviolet output.

## Scope

C002 is a sharpening, not a claim of global regularity. No a-priori arbitrary-data bound on `A_bal` has been proved. The Navier–Stokes Millennium problem remains unsolved by this repository.
