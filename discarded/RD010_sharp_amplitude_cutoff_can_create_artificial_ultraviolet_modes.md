# RD010 — A sharp high-amplitude cutoff can create ultraviolet modes absent from the physical Lamb force

**Status:** `exact smooth periodic counterexample to an interpretation of R13; R13 inequality remains valid`  
**Depends on:** R08, R13  
**Does not imply:** blow-up, failure of R08/R13 estimates, or failure of global regularity

R13 Fourier-localizes

`F = 1_{|u|>M_*}(omega×u)`

and proves that if the R08 tail action diverges, then the Fourier action of `QF` escapes every fixed cutoff. The estimate is correct. However, an overly strong interpretation would identify high Fourier modes of `QF` with a genuine ultraviolet cascade already present in the untruncated physical Lamb force `L=omega×u`.

RD010 shows that this interpretation is false: the **sharp amplitude indicator itself can manufacture arbitrarily high Fourier modes**.

## 1. Exact globally smooth shear

Work on the normalized `2 pi`-periodic torus. Let

`u(t,x,y,z) = a(t) (0, cos x, 0)`,

`a(t)=A exp(-nu t)`.

Then `div u=0`, `(u·grad)u=0`, and the field is an exact global smooth Navier–Stokes solution with constant pressure because

`u_t = nu Delta u`.

Its vorticity and Lamb force are

`omega = (0,0,-a sin x)`,

and

> `L=omega×u = (a^2/2) sin(2x) e_x`.

Thus the velocity is supported on radial Fourier shell `1`, while the physical Lamb force is supported only on shell `2`.

## 2. Tune the R08 threshold to a nontrivial level set

Let

`C_{3/2}=||cos x||_{L^{3/2}(T^3)}`

under the fixed normalized measure convention. Then

`U=||u||_{3/2}=a C_{3/2}`,

and the R08 threshold is

`M_* = nu^2/(12 C_H^2 U)`.

Therefore

`M_*/a = nu^2/(12 C_H^2 C_{3/2} a^2)`.

Choose the initial amplitude so that

> `A^2 = nu^2/(6 C_H^2 C_{3/2})`.

At `t=0` this gives exactly

> `M_*/A = 1/2`.

Hence the R08 sharp tail field is

> `F = 1_{|cos x|>1/2} (A^2/2) sin(2x) e_x`.

## 3. The cutoff creates infinite Fourier support

The indicator switches at points such as `x=pi/3`, where

`|cos(pi/3)|=1/2`

but

`sin(2pi/3)=sqrt(3)/2 != 0`.

Consequently `F` has a nonzero jump across that level-set boundary. Any finite Fourier series is continuous, so `F` cannot have finite Fourier support. It has infinitely many Fourier modes even though the untruncated physical Lamb force `L` has only shell `2`.

Moreover, `F` depends only on `x` and points in the `e_x` direction. Every nonzero Fourier coefficient is therefore parallel to its wave vector `(n,0,0)`, so it is purely longitudinal. The gradient Helmholtz projector `Q` acts as the identity on those nonzero modes. The field is odd in `x`, hence has zero mean. Thus

> `QF=F`.

The artificial high modes survive exactly in the quantity Fourier-localized by R13.

## 4. What RD010 falsifies

RD010 does **not** falsify the R13 theorem. R13 correctly proves high-frequency escape of the *truncated projected field* `QF` if its action diverges.

What fails is the stronger semantic shortcut

> `high frequency of Q(1_{|u|>M_*}L)` = `high frequency already present in physical L`.

That equality of interpretations is false even along an exact globally smooth single-frequency shear.

Therefore a helical/triad analysis that treats the high modes of `QF` directly as physical high-frequency Lamb triads must first separate cutoff-generated modes from genuine modes of `L`.

## 5. Corrected route

R18 removes this representation hazard by introducing the cutoff-free full-Lamb action

`A_L(T)=int_0^T ||u||_{3/2} ||omega×u||_2^2 dt`.

Because `A_tail<=A_L` and every fixed low-frequency portion of the **full** Lamb action is energy-controlled, divergence of `A_tail` forces ultraviolet escape of the actual physical Lamb force itself. This restores a clean bridge to R14–R17.

## 6. Verification

`verification/check_R18_RD010_cutoff_free_uv.py` checks the exact shear identities, the threshold coefficient `M_*/A=1/2`, the nonzero cutoff jump, the critical scaling of the full-Lamb action, and the energy-bound coefficient used by R18.
