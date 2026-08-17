# RD018 — Generic separated-frequency commutator summation still misses energy-time integrability

**Status:** `exact exponent audit / route guard`  
**Depends on:** R35–R36  
**Scope:** a specific generic Bernstein–Hölder–energy/enstrophy summation template; does not rule out structured paraproduct, weighted, balanced-tail, or cancellation estimates

R36 proves that an individual separated-frequency commutator triad has a small low-leg / active-scale factor. RD018 asks whether that gain alone closes the smooth synchronization defect after standard dyadic summation using only the first energy inequality.

The answer is **no for the template below**.

## 1. Template

Let the active smooth filter scale be `K`, and let `L<=K` denote a dyadic low velocity leg. Use the R36 gain `L/K`.

Choose a product exponent `r` with

`3/2 <= r <= 2`,

and choose `s` from

`1/r = 1/2 + 1/s`.

Estimate the vorticity leg in `L^2`, the low velocity block in `L^s`, and the commutator output in `L^r`.

Bernstein gives

`||u_L||_s <= C L^beta ||u_L||_2`,

where

> `beta = 3(1/2-1/s)=3(1-1/r)`.

Thus the R36 low-leg factor produces the dyadic coefficient

`(L/K)L^beta ||u_L||_2`

`=(L^beta/K)(L||u_L||_2)`.

Cauchy–Schwarz over dyadic `L<=K` and the enstrophy square sum give

> `||B_sep||_r`
>
> `<= C K^(beta-1) ||omega||_2^2`.

Since

> `beta-1 = 2-3/r`,

this is

`||B_sep||_r <= C K^(2-3/r)||omega||_2^2`.

The reverse R36 orientation, where the source velocity leg is low and the multiplier vorticity leg is the `L^2` factor, has the same exponent bookkeeping.

## 2. Pair with the nonlinear test field

Let `r'=r/(r-1)`. Since `G=|u|u`,

`||G||_(r') = ||u||_(2r')^2`.

For `3/2<=r<=2`, the exponent `2r'` lies between `4` and `6`, so interpolation between `L^2` energy and `H^1 -> L^6` gives

> `||G||_(r')`
>
> `<= C E0^(2-3/r) ||omega||_2^(3/r)`.

Consequently the generic separated-frequency defect estimate becomes

> `|D_sep|`
>
> `<= C K^(2-3/r) E0^(2-3/r)`
>
> `   ||omega||_2^(2+3/r)`.

## 3. Optimization

For

`3/2<=r<=2`,

`2-3/r` lies in `[0,1/2]`, while

> `2+3/r` lies in `[7/2,4]`.

The two endpoints are

- `r=3/2`: `|D_sep| <= C ||omega||_2^4`;
- `r=2`: `|D_sep| <= C K^(1/2) E0^(1/2)||omega||_2^(7/2)`.

Every member of the family requires a time power of `||omega||_2` strictly larger than `2`.

But the first energy inequality only supplies

`int ||omega||_2^2 dt < infinity`.

Therefore this generic summation template cannot make the separated commutator defect time-integrable from energy/enstrophy alone.

## 4. What is rejected

The following route is rejected:

> R36 one-leg gain + generic low-frequency Bernstein + Hölder + only `L^2` energy/enstrophy interpolation is enough to close the synchronization commutator.

It is not.

This is analogous in spirit to RD016, but it audits the **new R36 separated-frequency commutator gain**, not the earlier generic stress representation.

## 5. What remains live

RD018 does **not** rule out estimates that retain structure discarded by this template, including

- the weighted `D_3` geometry of R07/R27;
- R24 transported-speed / longitudinal-strain structure;
- balanced high-pass action from R30/R34;
- cancellation among comparable high-high triads;
- helical constraints from R14–R20;
- concentration-compactness/rigidity of R31 terminal packets;
- sharper Besov/Lorentz/paraproduct bookkeeping not reducible to this generic Lebesgue template.

Together R36/RD017/RD018 say that the next positive theorem must use more than a one-leg symbol gain plus first-energy Hölder estimates.

## Verification

`verification/check_RD018_generic_separated_summation_barrier.py` verifies the exponent identities and endpoint ranges with exact rational arithmetic.