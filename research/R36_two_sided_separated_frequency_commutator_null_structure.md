# R36 — Two-sided separated-frequency null structure for the smooth synchronization commutator

**Status:** `exact Fourier structural theorem / verified partial`  
**Depends on:** R20, R33–R35  
**Clay status:** does not sum the remaining comparable high-high interactions; no global regularity conclusion

Let `A_K=M_K^2` be the smooth scalar multiplier from R33–R35 with symbol `a_K(xi)=a(xi/K)`, and let `C_u omega=omega×u`. R35 gives, for `p+q=k`,

`T_K(p,q)=[a_K(p+q)-a_K(p)] [omegahat(p)×uhat(q)]`.

Write `A_inf=||a||_infinity`, `L_a=||grad a||_infinity`, `C_a=max(L_a,2 A_inf)`. Then

`|a_K(p+q)-a_K(p)| <= min(2 A_inf,L_a |q|/K)`.

Hence

> `|T_K(p,q)| <= L_a (|q|/K)|omegahat(p)||uhat(q)|`.

This is the R35 low-multiplying-velocity gain.

For divergence-free nonzero Fourier modes,

`omegahat(r)=i r×uhat(r)` and `|omegahat(r)|=|r||uhat(r)|`.

Therefore

`|a_K(p+q)-a_K(p)| |uhat(q)|`

`<= min(2A_inf/|q|,L_a/K)|omegahat(q)|`

`<= (C_a/K)|omegahat(q)|`,

and consequently

> `|T_K(p,q)| <= C_a (|p|/K)|uhat(p)||omegahat(q)|`.

Thus for any `0<eta<1`, an individual triad with either `|q|<=eta K` or `|p|<=eta K` carries an explicit `O(eta)` one-leg suppression in one of the two natural velocity/vorticity orientations. If `p=0`, `omegahat(p)=0`; if `q=0`, the multiplier difference is zero.

So an individually full-strength commutator triad can avoid both one-leg gains only in the sector

> `|p|>eta K` and `|q|>eta K`.

In words: the unsuppressed sector requires **two velocity inputs at the active scale or higher**. This removes the E35 low-vorticity-frequency/high-multiplying-velocity regime from the list of individually full-strength interactions.

This is a triadwise theorem, not a summation theorem. A large collection of individually suppressed separated-frequency terms may still accumulate.

RD017 gives a comparable high-high saturation family. Take `p=(K,0,0)`, `q=(0,K,0)` and divergence-free polarizations `uhat(p)=(0,1,0)`, `uhat(q)=(1,0,0)`. Then `omegahat(p)×uhat(q)` is nonzero. For any smooth profile with different values at normalized radii `1` and `sqrt(2)`, the symbol gap is a fixed nonzero number independent of `K`. Hence no universal `K`-decay exists in the comparable high-high sector.

## Updated frontier

After R36 the live commutator problem is sharper:

1. separated interactions have a low-leg small factor, but accumulation must still be controlled;
2. comparable high-high interactions have no one-leg small parameter and are the primary full-strength sector.

The next load-bearing theorem must either give a norm/spacetime estimate for comparable high-high interactions or prove that the separated gains survive summation strongly enough to be absorbed by already-controlled critical quantities.

## Verification

`verification/check_R36_two_sided_commutator_null.py` independently checks both directional bounds on divergence-free random Fourier polarizations, zero-mode cancellation, and a comparable high-high saturation family. The continuum theorem uses only the R35 symbol identity, the mean-value theorem, symbol boundedness, and `|omegahat(k)|=|k||uhat(k)|` for divergence-free Fourier modes.