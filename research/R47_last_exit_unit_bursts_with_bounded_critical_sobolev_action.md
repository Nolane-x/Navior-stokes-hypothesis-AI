# R47 — Last-exit unit bursts with uniformly bounded critical Sobolev/Serrin action

**Status:** `exact conditional extraction theorem / critical compactness input / not closure`  
**Depends on:** R01, R38–R46  
**Clay status:** **NOT SOLVED**

R41 normalized the hypothetical terminal mechanism into unit common-work bursts, but its first-hitting intervals may contain arbitrarily deep temporal backtracking of the signed cumulative common work. That leaves two avoidable defects: the work can oscillate violently inside a nominally normalized burst, and the exact `L^3` balance does not by itself give a uniform critical-diffusion budget on each chosen burst.

R47 changes the extraction, not the PDE. It uses **last-exit / first-hit** intervals. On each refined burst the cumulative common work has no drawdown, and by choosing the number of extracted work units only *after* the terminal start time has been fixed, the total `L^3` diffusion can be averaged across arbitrarily many normalized bursts. A positive fraction of them consequently have a uniform scale-critical `D_3` action. The nonlinear change of variables

> `Z=|u|^(1/2)u`

then converts the `D_3` bound into a uniform critical

> `L^3_t L^9_x`

bound on those actual-trajectory bursts.

This is a real compactness/transfer input absent from E46. It is **not** a Serrin continuation theorem because the bound is per burst, not summable over the infinite terminal family and not small.

## 1. Parent packet and cumulative common work

Fix a finite high-pass cutoff `L`. On an R40/R41 parent interval `I=[a,b]`, let

> `C_L=(W_grad,>L+W_sol,>L)/2`,
>
> `F(t)=int_a^t C_L(s)ds`.

Assume the parent carries at least `N` units of common work,

> `F(b)>=N`,

and the R39/R40 resolved controls are

> `int_I sum_(0<|k|<=L)|d_k(t)|dt <= eta`,

> `int_I sum_(0<|k|<=L)(|w_grad,k|+|w_sol,k|)dt <= zeta`.

Write

> `eps=eta/2+zeta`.

For the extraction below, `a`, `L`, `eta`, `zeta` are fixed first. R28/R30 terminal divergence then permits `N` to be chosen arbitrarily large before selecting the upper endpoint `b<T*`. In particular we may impose

> `N>=max(1,Y(a))`,
>
> `Y(a)=||u(a)||_3^3`,

and, by taking the terminal tolerances sufficiently strong, `eps<=1`.

## 2. Last-exit / first-hit unit intervals

Let

> `tau_j=inf{t>=a:F(t)=j}`, `j=0,...,N`,

with `tau_0=a`.

For `j>=1`, define

> `sigma_j=max{t in [tau_(j-1),tau_j]:F(t)=j-1}`.

The maximum exists by continuity. Set

> `K_j=[sigma_j,tau_j]`.

By the defining **last** hit of `j-1` and **first** hit of `j`, every interior point satisfies

> `j-1 < F(t) < j`, `t in (sigma_j,tau_j)`.

Hence for every prefix `t in K_j`,

> `0 <= int_(sigma_j)^t C_L(s)ds <= 1`,

and at the endpoint

> `int_(K_j) C_L dt=1`.

The `K_j` are ordered and pairwise disjoint. Backtracking excursions that occurred between the first hit of `j-1` and the last exit from `j-1` are discarded.

## 3. The full critical pressure work has bounded prefix cumulative variation

For every subinterval `J subset I`, R39 gives

> `|int_J(W_grad,>L-W_sol,>L)dt|<=eta`.

Therefore on any prefix of any `K_j`, high-pass gradient work differs from common work by at most `eta/2`. R40 gives an absolute low-pass gradient-work error at most `zeta` on every subinterval. Thus for every `t in K_j`,

> `-eps <= int_(sigma_j)^t W_3(s)ds <= 1+eps`.

In particular each complete last-exit burst satisfies

> `int_(K_j)W_3dt = 1+O(eps)`.

This prefix statement is strictly stronger than the net normalization in R41: large hidden temporal drawdown of the full critical work is excluded up to the already verified resolved-catalog tolerance.

## 4. Total `D_3` budget over arbitrarily many work units

At the first hit `tau_N`, the common high-pass work from `a` is exactly `N`. The same mismatch/low-pass bounds give

> `int_a^(tau_N) W_3 dt <= N+eps`.

The exact R01 balance

> `(1/3)dY/dt + nu D_3=W_3`

therefore yields

> `int_a^(tau_N)D_3dt`
>
> `<= [Y(a)+3(N+eps)]/(3nu)`.

Because the last-exit bursts are disjoint subsets of `[a,tau_N]`,

> `sum_(j=1)^N int_(K_j)D_3dt`
>
> `<= [Y(a)+3(N+eps)]/(3nu)`.

Under `N>=Y(a)`, `N>=1`, `eps<=1`, the average is bounded by

> `(1/N) sum_j int_(K_j)D_3dt <= 7/(3nu)`.

This is the key new averaging gain. The value `Y(a)` may be huge near a hypothetical singular time, but terminal work divergence lets us choose *more work units than `Y(a)`* after `a` is already fixed.

## 5. Simultaneously good duration, enstrophy and critical diffusion

Let

> `delta=T*-a`,
>
> `q(a)=int_a^(T*)||omega||_2^2dt`.

Disjointness gives

> `sum_j |K_j| <= delta`,
>
> `sum_j q_(K_j) <= q(a)`,
>
> `sum_j D_(K_j) <= 7N/(3nu)`.

Apply Markov counting with factor `4` to all three nonnegative lists. Fewer than `N/4` bursts violate each one of

> `|K_j| <= 4delta/N`,
>
> `q_(K_j) <= 4q(a)/N`,
>
> `D_(K_j) <= 28/(3nu)`.

By the union bound, at least `N/4` last-exit unit bursts satisfy **all three simultaneously**.

Taking the same growing-cutoff terminal diagonal as R38–R41, but after choosing each start time selecting

> `N_n >= max(n,Y(a_n))`,

produces actual-trajectory unit bursts `J_n` with

> `int_(J_n) C_(L_n)dt=1`,
>
> `|J_n|->0`,
>
> `q_(J_n)->0`,
>
> `int_(J_n)D_3dt <= 28/(3nu)`,

while retaining R39/R40 synchronization and resolved-work evacuation. R43–R46 therefore continue to apply to these refined bursts.

## 6. Exact nonlinear Sobolev variable

On `{rho=|u|>0}`, write `u=rho n`, `|n|=1`, and define

> `Z=rho^(1/2)u=rho^(3/2)n`.

The R01 critical diffusion is

> `D_3 = int [2rho|grad rho|^2 + rho^3|grad n|^2]dx`.

Direct differentiation gives

> `||grad Z||_2^2`
>
> `=int [(9/4)rho|grad rho|^2 + rho^3|grad n|^2]dx`.

Consequently, pointwise in time,

> `D_3 <= ||grad Z||_2^2 <= (9/8)D_3`.

The zero set is handled by the same standard regularization/weak-chain-rule interpretation already used in R06/R07.

Also

> `||Z||_2^2=||u||_3^3`,
>
> `||Z||_6^2=||u||_9^3`.

## 7. Uniform critical `L^3_t L^9_x` action

Let `C_T` be a fixed inhomogeneous Sobolev constant on the canonical torus such that

> `||f||_6^2 <= C_T (||grad f||_2^2+||f||_2^2)`.

Then on a selected R47 burst `J`,

> `int_J ||u||_9^3dt`
>
> `<= C_T[(9/8)int_JD_3dt + int_J||u||_3^3dt]`.

The energy inequality and periodic Sobolev interpolation give, for a fixed torus constant `C_S`,

> `||u||_3 <= C_S^(1/2)E0^(1/2)||omega||_2^(1/2)`.

Hence Hölder in time gives

> `int_J||u||_3^3dt`
>
> `<= C_S^(3/2)E0^(3/2)|J|^(1/4)q_J^(3/4)`
>
> `->0`.

Therefore the selected sequence satisfies the uniform scale-critical estimate

> `int_(J_n)||u||_9^3dt`
>
> `<= C_T[21/(2nu)+o(1)]`.

The mixed norm `L^3_t L^9_x` lies exactly on the Serrin scaling line

> `3/9+2/3=1`.

So E47's normalized unit-work objects now carry a genuine **uniform critical PDE-space bound**, not merely scalar frequency/amplitude floors.

## 8. Interface with the E46 ancient blow-up

R46 already identifies a genuine singular point and imports the existence of a non-trivial bounded mild ancient blow-up object. R47 adds a critical compactness ingredient on a positive-density subfamily of the project-specific productive bursts:

- exact unit common work;
- no cumulative-work drawdown on prefixes;
- vanishing duration and ordinary enstrophy cost;
- bounded critical `D_3` action;
- bounded critical `L^3_tL^9_x` action;
- the R43–R46 productive frequency/spatial-work structure.

This makes the scale-transfer problem materially narrower. A successful R48-type theorem may try to align one of these last-exit bursts with the standard singularity blow-up normalization and pass the critical bound plus a nonzero piece of productive work to the limit.

## 9. What R47 does **not** prove

R47 does not prove

- smallness of the `L^3_tL^9_x` norm;
- summability of that norm over the infinitely many disjoint terminal bursts;
- a global Serrin continuation criterion;
- time alignment `R_theta^2|J|~1`;
- alignment with the Albritton–Barker blow-up scale;
- survival of unit common work in an ancient limit;
- a Liouville theorem for the resulting ancient solution;
- global regularity.

Uniform critical control on each member of an infinite disjoint family is compatible with divergence of the total terminal critical norm. This attack remains explicit in the E47 World state and in RD025.

## 10. Verification

`verification/check_R47_last_exit_critical_bursts.py` verifies the last-exit combinatorics under strong synthetic backtracking, the prefix work conversion, the simultaneous three-budget Markov extraction, exact `Z` geometry and critical scaling.

A fresh verifier reconstructs the extraction from an independent piecewise-linear trace generator and separately checks the Sobolev-variable identities.

RD025 supplies an exact scalar route guard showing that bounded critical action on every shrinking unit burst need not be summable over the terminal union.

**R47 is a verified-partial candidate until its independent and repository-wide gates pass. It is not a solution of Navier–Stokes global regularity.**
