# R19 — Solenoidal versus Bernoulli-gradient physical ultraviolet dichotomy

**Status:** `exact structural representation split / not claimed novel`  
**Depends on:** R03, R17, R18, RD010  
**Clay status:** neither channel is proved finite for arbitrary data

R18 replaces the sharp-cutoff Fourier interpretation of R13 by the cutoff-free full physical Lamb action

`A_L(T)=int_0^T U(t)||L(t)||_2^2 dt`,

where

`U=||u||_{3/2}`, `L=omega×u`.

If the R08 tail action diverges, then R18 proves `A_L=infinity` and forces the full physical Lamb action through arbitrarily high Fourier modes.

R19 makes one further representation split that is essential for choosing the next mechanism.

Let `P` be the divergence-free Leray projector and `Q=I-P` the gradient Helmholtz projector used throughout R02–R03. Since `P` and `Q` are orthogonal in `L^2`,

> `||L||_2^2 = ||P L||_2^2 + ||Q L||_2^2`.

Define the two scale-critical physical actions

> `A_sol(T)=int_0^T U ||P L||_2^2 dt`,

and

> `A_grad(T)=int_0^T U ||Q L||_2^2 dt`.

Then exactly

> `A_L=A_sol+A_grad`.

## 1. Necessary two-channel blow-up dichotomy

If the R08 route reaches a finite-time obstruction with

`A_tail(T*)=infinity`,

then R18 gives `A_L(T*)=infinity`. Since both channel actions are nonnegative,

> `A_sol(T*)=infinity` or `A_grad(T*)=infinity`, or both.

This distinction matters because the two pieces have different mathematical meanings.

## 2. Solenoidal channel: dynamical nonlinear transport

Using

`(u·grad)u = L + grad(|u|^2/2)`,

we have

`P L=P((u·grad)u)`.

The projected velocity equation is

> `u_t + P L = -nu D^2 u`.

Thus `P L` is the part of the Lamb force that directly changes the divergence-free velocity. In particular, the R17 canonical-center and bandwidth-variance evolution laws are driven by `P L`.

Therefore R17 is naturally a mechanism for the **solenoidal UV branch**.

## 3. Gradient channel: Bernoulli/pressure obstruction

R03 gives the exact Bernoulli identity

> `Q L = -grad B`,

where

`B=p+|u|^2/2`.

Hence

> `A_grad(T)=int_0^T U ||grad B||_2^2 dt`.

This is the physical pressure/Bernoulli branch of the UV obstruction. It is also the component entering the critical `L^3` pressure-work factorization in R03.

Therefore R09–R10 style amplitude/iso-speed geometry is naturally a mechanism for the **gradient UV branch**.

## 4. Each divergent channel must itself escape every fixed Fourier cutoff

For every fixed finite `K`, orthogonal contraction and R18's Bernstein-energy argument give

`||P_{<=K} P L||_2 <= ||P_{<=K}L||_2`,

`||P_{<=K} Q L||_2 <= ||P_{<=K}L||_2`,

because all projectors are commuting Fourier multipliers. Consequently each channel separately satisfies

> `int_0^T U ||P_{<=K}P L||_2^2 dt`
>
> `<= [C_B(K)^2/(2nu)] E0^5`,

and

> `int_0^T U ||P_{<=K}Q L||_2^2 dt`
>
> `<= [C_B(K)^2/(2nu)] E0^5`.

Thus if `A_sol=infinity`, its solenoidal action escapes every fixed physical cutoff; if `A_grad=infinity`, its Bernoulli-gradient action does the same.

## 5. Both actions are critical

Under

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

`U` has exponent `-1`, both `||P L||_2^2` and `||Q L||_2^2` have exponent `+3`, and `dt` has exponent `-2`. Hence

> `A_sol` and `A_grad` are both scale invariant.

Neither branch can be discarded by a simple subcriticality argument.

## 6. Exact warning: the solenoidal branch cannot be assumed

The globally smooth shear used in RD010,

`u=a(t)(0,cos x,0)`,

has

`L=(a^2/2)sin(2x)e_x`.

Every nonzero Fourier coefficient of `L` is parallel to its wave vector `(+-2,0,0)`. Therefore

> `P L=0`, `Q L=L`.

So a nonzero, even large, physical Lamb force need not contain any solenoidal component at a given state. This does not produce blow-up, but it proves that a proof cannot simply infer `A_sol` divergence from large full-Lamb forcing without an additional trajectory argument.

## 7. Corrected proof fork

The live W5 frontier is now a genuine two-branch problem:

### Branch S — solenoidal physical UV

Control or exclude

`int U ||P_{>K}P(omega×u)||_2^2 dt`

through R17 centered spectral production, helical triad transfer, dissipation, or a compactness/rigidity argument.

### Branch G — Bernoulli-gradient physical UV

Control or exclude

`int U ||P_{>K}grad B||_2^2 dt`

through pressure/Bernoulli structure, iso-speed conditional oscillation, level-set geometry, or a new nonlocal cancellation mechanism.

A complete proof through this program must close **both** branches, or prove a dynamical principle forcing one branch into a regime controlled by the other.

R19 is a representation theorem, not that missing dynamical principle.

## 8. Verification

`verification/check_R19_Lamb_channel_dichotomy.py` checks the orthogonal action algebra, critical scaling, inherited fixed-frequency contraction, and the exact shear witness `P L=0, Q L=L`.
