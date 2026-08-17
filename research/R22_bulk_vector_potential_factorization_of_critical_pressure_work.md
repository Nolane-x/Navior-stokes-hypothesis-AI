# R22 — Bulk vector-potential factorization of critical pressure work

**Status:** `exact structural theorem / level-set representation eliminated`  
**Depends on:** R01–R03, R09–R10, R21  
**Clay status:** no a-priori closure; the exact projected product remains uncontrolled

R21 removes the inter-component flux term from the iso-speed decomposition in the canonical zero-mean Galilean frame. R22 goes further: the surviving pressure work can be represented entirely in the bulk, with no regular-level decomposition and no surface Poincare constant in the identity itself.

As in R21, freeze the regularity-equivalent zero-mean periodic frame and write

`rho=|u|`.

Let `A` be the smooth periodic vector potential from R21,

> `curl A=u`.

## 1. Amplitude transport is a bulk divergence

For smooth positive `rho`, the vector identity

`div(A×grad rho)=grad rho·curl A - A·curl grad rho`

gives

> `div(A×grad rho)=u·grad rho`.

The same identity holds distributionally for `rho=|u|`, which is Lipschitz for smooth `u`: `curl grad rho=0` distributionally and `A` is smooth. Equivalently, one may regularize with `rho_eps=sqrt(|u|^2+eps^2)` and pass to the limit.

Thus the R01 transport scalar

`q=u·grad rho`

has the exact representation

> `q=div(A×grad rho)`.

Since `div u=0`, also

`div(rho u)=u·grad rho=q`.

Therefore

> `div[rho u - A×grad rho]=0`.

On the torus the gradient Helmholtz projector is determined by divergence on nonzero modes, while constant modes are divergence-free. Hence

> `Q(rho u)=Q(A×grad rho)`.

This is an exact equality of gradient fields.

## 2. Exact critical pressure-work factorization

R01 gives

`W_3=integral p q dx`.

Using the divergence form and periodic integration by parts,

`W_3=-integral grad p · (A×grad rho) dx`.

R03 gives

`Q(omega×u)=-grad B`,

`B=p+rho^2/2`.

Because

`grad(rho^2/2)=rho grad rho`

is parallel to `grad rho`, it is orthogonal pointwise to `A×grad rho`. Therefore

> `W_3 = integral Q(omega×u) · (A×grad rho) dx`.

Since `Q(omega×u)` is a gradient field, only the gradient projection of the second factor contributes:

> `W_3`
>
> `= <Q(omega×u), Q(A×grad rho)>`
>
> `= <Q(omega×u), Q(rho u)>`.

The last equality recovers the R02/R03 Helmholtz factorization, but through a new vector-potential representation of the nonlinear test field.

## 3. Why this removes the level-set topology from the identity

The coarea version of R10/R21 can be recovered from R22. On a regular level component `Sigma_s` with normal `n=grad rho/|grad rho|`, the surface identity

`u·n = div_{Sigma_s}(A×n)`

and surface integration by parts give

`integral_{Sigma_s} p u·n dS`

`= -integral_{Sigma_s} grad_{Sigma_s}p · (A×n)dS`.

But R22 shows that no regular-level decomposition is needed at all: after coarea recombination,

`|grad rho|(A×n)=A×grad rho`,

and the entire pressure work is the bulk identity above.

Thus disconnected components, component pressure means, and surface Poincare constants are **not intrinsic to the representation** of `W_3`. They arise only if one chooses to estimate the pressure fluctuation fiber-by-fiber.

This materially narrows the gradient-branch design space.

## 4. Critical scaling

Under Euclidean Navier–Stokes scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

a compatible vector potential scales as

`A_lambda(x,t)=A(lambda x,lambda^2 t)`,

so `A` has exponent `0`. The amplitude gradient has exponent `2`; therefore

`A×grad rho`

has exponent `2`, exactly matching `rho u`.

The equality

`Q(rho u)=Q(A×grad rho)`

is therefore scale-covariant at the same critical level as the original L3 test field.

## 5. A tempting but invalid shortcut

One might now try

`|W_3| <= ||Q L||_2 ||A×grad rho||_2`

and hope the full product norm is controlled by energy because `A` is one derivative smoother than `u`.

RD012 shows this loses the decisive Helmholtz cancellation: there is an exact mean-zero divergence-free high-frequency family for which

`||A×grad rho||_2 -> infinity`

while

`||Q(A×grad rho)||_2 = ||Q(rho u)||_2`

remains uniformly bounded.

Therefore the useful object is the **projected vector-potential product**

> `Q(A×grad rho)`,

not its raw L2 norm.

## 6. New gradient-branch frontier

R22 replaces the fiberwise pressure problem by a global projection/cancellation problem:

> control the scale-critical gradient projection of `A×grad|u|`, where `A=curl^{-1}u`, against the gradient Lamb/Bernoulli force.

Possible continuations must exploit structure invisible to the raw product norm, for example:

1. commutator/paraproduct cancellation in `Q[(curl^{-1}u)×grad|u|]`;
2. frequency separation created by the inverse derivative in `A`;
3. compensated-compactness/div-curl structure;
4. a scale-local bridge between this projected product and the R20/C01/C02 high-frequency criteria.

R22 does not prove any such estimate.

## 7. Verification

`verification/check_R22_RD012_vector_potential_factorization.py` certifies the modewise vector-potential identity, the divergence equivalence underlying `Q(rho u)=Q(A×grad rho)`, scaling, and RD012's high-frequency no-go showing that projection cannot be discarded.
