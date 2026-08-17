# RD012 — The raw vector-potential product norm can lose arbitrarily large Helmholtz cancellation

**Status:** `exact high-frequency no-go for a naive continuation of R22`  
**Depends on:** R21–R22  
**Does not imply:** blow-up or failure of the projected R22 representation

R22 proves

`Q(rho u)=Q(A×grad rho)`, `curl A=u`,

and

`W_3=<Q(omega×u),Q(A×grad rho)>`.

Because `A` is one derivative smoother than `u`, a tempting shortcut is to estimate the **unprojected** product `A×grad rho` by an energy-level quantity and thereby close the pressure work.

RD012 shows that this loses an arbitrarily large divergence-free cancellation.

## 1. Exact mean-zero divergence-free family

On the normalized `2 pi` torus, fix `0<eps<=1` and an integer `N>=2`. Define

> `u_{N,eps}(x,y,z)=(sin z, cos z, eps sin(Nx))`.

This field is smooth, periodic, divergence-free and mean-zero. Its speed is

> `rho^2=1+eps^2 sin^2(Nx)`.

A smooth periodic vector potential is

> `A_{N,eps}=(sin z, cos z-(eps/N)cos(Nx),0)`.

Direct differentiation gives

`curl A_{N,eps}=u_{N,eps}`.

The amplitude gradient is purely in the x direction:

`grad rho = g_N(x)e_x`,

where

> `g_N(x)=eps^2 N sin(Nx)cos(Nx)/rho`.

Therefore

`A×grad rho`

is purely in the z direction and has magnitude

`|cos z-(eps/N)cos(Nx)| |g_N(x)|`.

## 2. The raw product grows linearly with frequency

Using `rho^2<=1+eps^2`, averaging first in `z`, and using

`average_z [cos z-(eps/N)cos(Nx)]^2`

`=1/2+(eps^2/N^2)cos^2(Nx) >=1/2`,

we obtain the rigorous lower bound

> `||A×grad rho||_2^2`
>
> `>= eps^4 N^2 / [16(1+eps^2)]`.

Indeed `average_x sin^2(Nx)cos^2(Nx)=1/8` for every nonzero integer `N`.

Thus, for fixed `eps>0`,

> `||A×grad rho||_2` grows at least linearly in `N`.

## 3. Its gradient projection stays uniformly bounded

R22 gives exactly

`Q(A×grad rho)=Q(rho u)`.

Since `Q` is an orthogonal L2 contraction,

`||Q(A×grad rho)||_2 <= ||rho u||_2`.

But `|u|=rho`, hence

`||rho u||_2^2=integral rho^4 dx`.

For this family

`rho^4=(1+eps^2 sin^2(Nx))^2`,

so exactly

> `||rho u||_2^2 = 1+eps^2+(3/8)eps^4`,

independent of `N`.

Therefore

> `||Q(A×grad rho)||_2`

remains uniformly bounded while the raw product norm diverges at least like `N`.

Quantitatively,

`||A×grad rho||_2^2 / ||Q(A×grad rho)||_2^2`

is bounded below by

> `eps^4 N^2`
>
> `/ [16(1+eps^2)(1+eps^2+3eps^4/8)]`,

which tends to infinity as `N->infinity`.

## 4. What is falsified

RD012 falsifies any R22 continuation that discards the Helmholtz projection and hopes to close the pressure work from a uniform estimate on the raw product based only on the bounded size of `rho u` or comparable amplitude norms.

The inverse derivative in `A` does **not** by itself regularize the product: a low-frequency vector-potential component can multiply a high-frequency amplitude gradient and create a large mostly divergence-free field.

## 5. What survives

The exact projected identity

`Q(A×grad rho)=Q(rho u)`

remains valid and is precisely the cancellation RD012 exposes.

A viable R22 proof must therefore exploit the projection structurally, for example through a commutator, symbol cancellation, div-curl mechanism, or frequency-local decomposition. Replacing `Q(A×grad rho)` by `A×grad rho` before estimating is not a harmless relaxation at high frequency.

## 6. Verification

`verification/check_R22_RD012_vector_potential_factorization.py` certifies the vector potential, exact speed formula, the lower-bound coefficient, the uniform projected-norm upper bound, and the quadratic growth of the lower-bound ratio over increasing integer frequencies.
