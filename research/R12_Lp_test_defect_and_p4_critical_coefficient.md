# R12 — General `L^p` test-field Helmholtz defect and the distinguished `p=4` closure point

**Status:** `exact structural/conditional theorem; not claimed novel`  
**Depends on:** R05, R07  
**Clay status:** small-critical-norm conditional only; not arbitrary-data regularity

R05 factorizes every `L^p` pressure work as

`W_p=<Q(omega×u),Q(|u|^(p-2)u)>`.

R12 derives the general Helmholtz-defect estimate for the nonlinear test field and shows why `p=4` is distinguished: at exactly that exponent, R07 controls the **unweighted** Lamb force needed by the projector pairing.

Let

`rho=|u|`, `G_p=rho^(p-2)u`, `p>=2`,

and let `C_H` be the periodic dual-Sobolev constant

`||grad(-Delta)^(-1) f||_2 <= C_H ||f||_(6/5)`

for zero-mean scalar `f`.

## 1. General test-field defect

Because `div u=0`,

`div G_p = (p-2)rho^(p-3) u·grad rho`

`        = (p-2)rho^(p-2) n·grad rho`.

Using

`grad(rho^(p/2))=(p/2)rho^(p/2-1)grad rho`,

we have

`|div G_p|`

`<= [2(p-2)/p] rho^((p-2)/2) |grad(rho^(p/2))|`.

Holder with exponents `3` and `2` gives

`||div G_p||_(6/5)`

`<= [2(p-2)/p]`

`   * ||u||_(3(p-2)/2)^((p-2)/2)`

`   * ||grad(rho^(p/2))||_2`.

R05's diffusion decomposition is

`D_p = int[(p-1)rho^(p-2)|grad rho|^2 + rho^p|grad n|^2]`.

Hence

`||grad(rho^(p/2))||_2`

`<= [p/(2 sqrt(p-1))] D_p^(1/2)`.

Therefore

> `||QG_p||_2`

> `<= C_H [(p-2)/sqrt(p-1)]`

> `   * ||u||_(3(p-2)/2)^((p-2)/2) D_p^(1/2)`.

For `p=3` this is exactly the R06 coefficient

`C_H/sqrt(2) * ||u||_(3/2)^(1/2) D_3^(1/2)`.

## 2. Why `p=4` is special

R07 states

`int rho^(p-4)|omega×u|^2 <= [p/(p-1)]D_p`.

Only at

> `p=4`

does the amplitude weight disappear. Thus

`||omega×u||_2 <= sqrt(4/3) D_4^(1/2)`.

At the same exponent, the general test-field estimate becomes

`||Q(|u|^2u)||_2`

`<= (2 C_H/sqrt(3)) ||u||_3 D_4^(1/2)`.

Using the R05 factorization and `Q` contraction,

> `|W_4| <= (4 C_H/3) ||u||_3 D_4`.

Therefore the exact `L^4` balance obeys

> `(1/4)d/dt ||u||_4^4`

> ` + [nu-(4 C_H/3)||u||_3] D_4 <= 0`.

## 3. Small-critical-norm corollary

Whenever

> `||u(t)||_3 < 3 nu/(4 C_H)`,

the `L^4` quantity is instantaneously dissipative.

If the critical `L^3` norm is kept uniformly below that threshold on a time interval, `||u||_4` cannot increase there and the corresponding `D_4` is integrable with a positive coercivity margin.

This is a **conditional small-critical-norm statement**, not a proof that arbitrary large data ever enter or remain in that regime.

## 4. Structural meaning

R12 identifies a bridge between the protected energy endpoint and the critical barrier:

- `p=3`: the velocity norm is scale critical, but R07's Lamb control carries the singular weight `1/rho`;
- `p=4`: the Lamb weight becomes exactly unweighted, but the price is the critical coefficient `||u||_3` in front of dissipation;
- `p>4`: R07 weights the Lamb force toward high amplitude, and a direct unweighted projector pairing again requires additional information.

Thus the unresolved arbitrary-data problem reappears precisely as control of the critical `L^3` coefficient. R12 does not bypass the Millennium bottleneck; it locates it consistently from the entire `L^p` family.

## 5. Relation to R08

R08 attacks the `p=3` weight mismatch by splitting in amplitude and absorbing the low-speed part. R12 shows an alternative interpretation: moving to `p=4` removes the local weight but converts the obstruction into the size of the critical `L^3` norm itself.

A successful proof would need a genuinely dynamical mechanism connecting these two views, for example showing that high-amplitude tail activity strong enough to threaten R08 necessarily drives a compensating `p=4` dissipation before `||u||_3` can diverge.

No such mechanism is proved here.
