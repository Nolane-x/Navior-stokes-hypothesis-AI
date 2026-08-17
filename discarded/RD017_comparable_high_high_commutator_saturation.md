# RD017 — Comparable high-high commutator interactions do not inherit one-leg smallness

**Status:** `exact structural no-go / route guard`  
**Depends on:** R35–R36  
**Does not show:** Navier–Stokes blow-up, failure of all commutator estimates, or failure of high-high cancellation after summation

R36 proves that an individual smooth-commutator triad receives an explicit small factor when either velocity leg is low compared with the active filter scale `K`.

RD017 prevents the incorrect extrapolation that the **entire** commutator must therefore become small as `K->infinity`.

Take

`p=(K,0,0)`, `q=(0,K,0)`, `k=p+q=(K,K,0)`

and divergence-free polarizations

`uhat(p)=(0,1,0)`, `uhat(q)=(1,0,0)`.

Then

`omegahat(p)=i p×uhat(p)=i(0,0,K)`

and

`omegahat(p)×uhat(q)=i(0,K,0) != 0`.

For the smooth profile

`a(xi)=exp(-|xi|^2)`,

`a_K(xi)=a(xi/K)` gives

`a_K(p)=e^-1`,

`a_K(k)=e^-2`.

Hence the normalized symbol gap is exactly

> `|a_K(k)-a_K(p)|=e^-1-e^-2`,

independent of `K`.

Therefore the commutator triad has magnitude

`(e^-1-e^-2)|omegahat(p)×uhat(q)|`,

with no factor tending to zero as `K` grows.

The Gaussian is only a convenient explicit verifier profile. The same obstruction occurs for any admissible smooth low-pass profile whose values differ at the two normalized points `(1,0,0)` and `(1,1,0)`; a compactly supported smooth profile can be chosen with that property.

## Route consequence

The following shortcut is rejected:

> “R35/R36 give low-leg gains, therefore the whole synchronization commutator is automatically small at high filter scale.”

False. Comparable high-high interactions can stay full-strength.

After R36/RD017 the correct frontier is:

- **separated-frequency triads:** individually suppressed by the lower leg / active-scale ratio, but accumulation still needs a norm-level proof;
- **comparable high-high triads:** no one-leg small parameter; any closure must use cancellation, balanced-tail structure, transported-speed geometry, helical/triad constraints, or a genuinely critical spacetime estimate.

`verification/check_R36_two_sided_commutator_null.py` includes the explicit saturation family and verifies that its normalized gap stays bounded away from zero for increasing `K`.