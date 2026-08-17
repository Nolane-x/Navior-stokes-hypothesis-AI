# R24 — Streamline-speed / velocity-direction / longitudinal-strain factorization

**Status:** `exact structural theorem / literature-linked representation`  
**Depends on:** R01–R03, R21–R23  
**Clay status:** no a-priori closure; the surviving weighted direction/strain quantity is uncontrolled

R23 writes the critical test defect as

`Q(rho u)=[Q,rho]u`, `rho=|u|`.

That formula is exact, but a dyadic decomposition of `rho` alone can be misleading because the nonlinear modulus can generate arbitrarily high amplitude frequencies even from low-frequency velocity fields. R24 identifies the canonical scalar actually seen by the Helmholtz projector.

Freeze the canonical zero-mean periodic Galilean frame from R21. Let

`rho=|u|`,

and on the nonzero set `{rho>0}` define the velocity direction

`e=u/rho`.

Let

`S=(grad u + (grad u)^T)/2`

be the rate-of-strain tensor.

## 1. The projector only sees transported speed

Because `div u=0`,

`div(rho u)=u·grad rho`.

Define the canonical scalar

> `q_amp := u·grad rho = div(rho u)`.

Then, on nonzero Fourier modes,

> `Q(rho u)=grad Delta^{-1} q_amp`.

Therefore

> `||Q(rho u)||_2^2 = ||q_amp||_{dot H^{-1}}^2`

with the homogeneous periodic `H^{-1}` norm defined through nonzero Fourier modes.

This equality is global and distributional. It does **not** require `rho` to be smooth at velocity zeros. Since `rho` is Lipschitz when `u` is smooth, `rho u` is well defined and `q_amp=div(rho u)` is the canonical distribution.

Thus the Branch-G object is not the raw amplitude spectrum; it is the negative-derivative norm of **speed transported along the flow**.

## 2. Exact longitudinal-strain identity

At every point where `rho>0`, the chain rule gives

`grad rho = (grad u)^T u / rho`.

Hence

`q_amp = u·grad rho`

`      = u^T (grad u) u / rho`.

The antisymmetric part of `grad u` drops out of the quadratic form, so

> `q_amp = u^T S u / rho`
>
> `      = rho e^T S e`.

Only the component of strain acting **along the velocity direction** changes speed along a streamline. Pure rotational deformation does not enter this scalar.

The formula extends a.e. by setting the right-hand side to zero on `{rho=0}`; the distributional definition `q_amp=div(rho u)` remains canonical across the zero set.

## 3. Exact velocity-direction identity

On `{rho>0}`,

`0=div u=div(rho e)=e·grad rho + rho div e`.

Multiplying by `rho`,

> `q_amp = rho e·grad rho`
>
> `      = -rho^2 div e`.

Thus the three descriptions are exactly the same scalar:

> `q_amp`
>
> `= u·grad|u|`
>
> `= (u^T S u)/|u|`
>
> `= -|u|^2 div(u/|u|)`  on `{u!=0}`.

At velocity zeros the last expression should **not** be read as a classical pointwise formula because the direction is undefined. The weighted distribution is defined canonically by

`-|u|^2 div(u/|u|) := div(|u|u)`

when one wants a global notation. No unweighted regularity of `u/|u|` at zeros is assumed.

## 4. Connection to the velocity-direction regularity literature

Alexis Vasseur observed the underlying incompressibility identity

`|u| div(u/|u|) = -(u/|u|)·grad|u|`

and used control of the divergence of the velocity direction as a sufficient regularity condition for 3D Navier–Stokes.

Primary source:

- A. Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.

R24 does **not** claim this classical identity as novel. Its role in this repository is different: it identifies the exact scalar generating the R22/R23 Helmholtz test defect and therefore gives a clean interface between the Branch-G pressure route and an independent velocity-direction regularity mechanism.

The literature criterion is conditional. Energy does not supply the required direction-divergence norm, so it is not a global solution.

## 5. Why raw amplitude UV is the wrong frontier variable

A high Fourier mode of `rho=|u|` contributes to Branch G only through the combination

`q_amp=u·grad rho`.

Amplitude oscillation transverse to the velocity can be arbitrarily complicated while producing

`q_amp=0`

and hence

`Q(rho u)=0`.

RD013 gives a smooth, positive-speed, exactly low-frequency transverse shear for which `rho` has infinitely many Fourier harmonics but the entire test defect vanishes.

Therefore the R23 label `low-u/high-rho` must not be interpreted as automatically dangerous. The physically relevant refinement is:

> high-frequency **transported-speed / longitudinal-strain output**, not high-frequency amplitude by itself.

## 6. Critical scaling

Under the Euclidean Navier–Stokes scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

`rho` has exponent `1`, `S` has exponent `2`, and `q_amp` has exponent `3`.

Applying one inverse derivative through `grad Delta^{-1}` lowers the exponent by one, so

`Q(rho u)` has exponent `2`,

exactly matching the original quadratic test field.

Thus R24 preserves the critical scaling rather than obtaining control by moving to a subcritical quantity.

## 7. New Branch-G frontier

R24 replaces the ambiguous phrase “high amplitude frequency” by the exact object

> `q_amp = rho e^T S e = -rho^2 div e`.

A positive proof through Branch G now needs one of the following genuinely dynamical statements:

1. a scale-critical time-integrated bound on `q_amp` in `dot H^{-1}` strong enough to control the R03 pressure work;
2. a coupling showing that large longitudinal strain along the velocity direction forces the solenoidal Lamb channel into a regime controlled by Branch S;
3. a frequency-local direction-divergence estimate derived a priori from the true Navier–Stokes trajectory;
4. a rigidity theorem for any rescaled object carrying non-summable `q_amp` ultraviolet action.

R24 proves none of these closing estimates.

## 8. Verification

`verification/check_R24_RD013_transport_direction.py` checks the exact pointwise strain/direction identities on rational divergence-free jets, verifies the modewise `H^{-1}` norm relation, and certifies the transverse-shear projection firewall used by RD013.
