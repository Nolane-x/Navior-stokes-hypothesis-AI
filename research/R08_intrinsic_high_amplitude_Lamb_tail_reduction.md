# R08 — Intrinsic high-amplitude Lamb-tail reduction

**Status:** `verified-partial conditional reduction / not claimed novel`  
**Depends on:** R06, R07  
**Clay status:** does not prove the tail action is finite; not global regularity

R06 shows that the critical `L^3` barrier is controlled by a scale-invariant Bernoulli/Lamb action. R07 shows that the full Lamb force is already diffusion-controlled after division by one power of velocity amplitude. R08 combines them to prove that **low-amplitude regions can be absorbed into viscosity exactly**. Only a dynamically defined high-amplitude Lamb tail remains as a possible obstruction.

Let

`rho=|u|`, `L=omega x u`, `U=||u||_(3/2)`

and use the periodic dual-Sobolev constant `C_H` from R06:

`||Q(|u|u)||_2 <= (C_H/sqrt(2)) U^(1/2) D_3^(1/2)`.

Assume `U>0`; the zero solution is trivial.

## 1. Amplitude splitting

For any threshold `M>0`, define

`L_low = 1_{rho<=M} L`,

`L_high = 1_{rho>M} L`.

R07 gives

`∫ |L|^2/rho <= (3/2)D_3`.

Therefore

`||L_low||_2^2`

`= ∫_{rho<=M}|L|^2`

`<= M ∫_{rho<=M}|L|^2/rho`

`<= (3M/2)D_3`.

Since `Q` is an `L^2` contraction,

> `||Q L_low||_2 <= sqrt(3M/2) D_3^(1/2)`.

## 2. Low-amplitude pressure work

Using R03/R06,

`W_3=<QL,Q(|u|u)>`

and the low piece satisfies

`|<Q L_low,Q(|u|u)>|`

`<= [C_H sqrt(3 M U)/2] D_3`.

Choose the intrinsic threshold

> `M_*(t) = nu^2 / [12 C_H^2 U(t)]`.

Then

`C_H sqrt(3 M_* U)/2 = nu/4`,

so

> `|<Q L_low,Q(|u|u)>| <= (nu/4)D_3`.

Thus the entire low-amplitude Lamb contribution is harmless at this threshold.

## 3. High-amplitude tail

For

`L_+ = 1_{rho>M_*} L`,

R06 gives

`|<Q L_+,Q(|u|u)>|`

`<= (C_H/sqrt(2)) U^(1/2) ||Q L_+||_2 D_3^(1/2)`.

Young with coefficient `nu/4` yields

`|<Q L_+,Q(|u|u)>|`

`<= (nu/4)D_3`

`   + [C_H^2/(2nu)] U ||Q L_+||_2^2`.

Combining low and high pieces,

> `|W_3| <= (nu/2)D_3`

> `          + [C_H^2/(2nu)] U ||Q(1_{rho>M_*} (omega x u))||_2^2`.

Substituting in R01 gives

> `(1/3)d/dt ||u||_3^3 + (nu/2)D_3`

> `<= [C_H^2/(2nu)] U ||Q(1_{rho>M_*}(omega x u))||_2^2`.

Hence

> `||u(T)||_3^3 + (3nu/2) int_0^T D_3 dt`

> `<= ||u(0)||_3^3 + [3 C_H^2/(2nu)] A_tail(T)`,

where

> `A_tail(T) = int_0^T U(t)`

> `  * ||Q(1_{|u|>M_*(t)} (omega x u))||_2^2 dt`.

## 4. Scaling audit

Under local Euclidean scaling,

`U=||u||_(3/2)` scales as `lambda^(-1)`.

Therefore

`M_* = nu^2/(12 C_H^2 U)`

scales as `lambda`, exactly like velocity amplitude. The condition

`|u|>M_*`

is scale covariant.

The tail action has exponent

`(-1) + 3 + (-2) = 0`,

so

> `A_tail` is scale invariant.

Thus R08 does not hide the hard region behind a supercritical cutoff.

## 5. Meaning

R08 strengthens R06 conceptually:

- zeros and low-amplitude regions are **not** where the critical obstruction lives;
- the raw-amplitude `A_2` failure in RD004 therefore does not by itself doom the program;
- a finite-time singularity along this proof route must concentrate enough **projected Lamb force on a scale-covariant high-amplitude set** to make `A_tail` diverge.

This is a substantially narrower target than the full Bernoulli/Lamb action.

## 6. What remains open

R08 does not control the high-amplitude tail. The remaining question is now:

> Can exact Navier–Stokes triad/vorticity geometry prevent divergence of the projected Lamb force generated where `|u|` exceeds the intrinsic threshold `M_*`?

Potential mechanisms to attack next:

1. amplitude-level energy flux: show the high-amplitude set cannot simultaneously support large `QL` and remain compatible with energy/enstrophy dissipation;
2. localized helicity/Beltrami depletion: `|omega x u|` is small when velocity and vorticity align;
3. concentration geometry: estimate projection leakage from a small high-amplitude set using cancellation/moment information rather than raw `A_2` bounds;
4. dynamic threshold transport: derive an evolution inequality for the measure/geometry of `{|u|>M_*(t)}`;
5. helical-triad constraints on the production of `Q(1_{rho>M_*}L)`.

R08 turns the global critical-norm problem into a high-amplitude, true-nonlinearity tail problem without assuming regularity.
