# R44 — Unit-work amplitude center and intrinsic-scale extraction

**Status:** `exact conditional center-scale extraction theorem / not compactness`  
**Depends on:** R01, R39–R43  
**Clay status:** **NOT SOLVED**

R41 produces consecutive first-hitting intervals carrying exactly one unit of high-pass common pressure work. R43 adds an intrinsic productive-work quantile radius to any such unit burst. What remained missing for a concentration/rigidity program was even a canonical **spatial center** chosen from the actual trajectory.

R44 derives one directly from the exact critical `L^3` balance. A parent packet containing many unit common-work bursts must develop a quantitatively large velocity maximum. The unit burst containing that maximum inherits the R43 intrinsic spectral scale, vanishing duration/enstrophy cost, and the ultraviolet work normalization.

Thus the same actual-trajectory burst carries both a spatial peak center and a canonical productive Fourier scale. R44 still does not prove spatial compactness, an energy atom, or a parabolic relation between the two scales.

## 1. Consecutive unit bursts and full pressure work

Take an R41 parent packet `I=[a,b]` at cutoff `L`, with `N=floor(M)` first-hitting unit common-work intervals `J_j=[tau_(j-1),tau_j]`, `j=1,...,N`. They are consecutive and tile `K=[a,tau_N]`.

By construction,

> `int_K C_L(t)dt=N`,

where `C_L=[W_grad,>L+W_sol,>L]/2`.

Assume the R39 resolved mismatch total-variation bound and R40 resolved absolute-work bound are

> `int_I sum_(0<|k|<=L)|d_k|dt <= eta`,

and

> `int_I sum_(0<|k|<=L)(|w_grad,k|+|w_sol,k|)dt <= zeta`.

The full representation difference is zero, so the high-pass mismatch is the negative resolved mismatch. Hence

`|int_K(W_grad,>L-W_sol,>L)dt| <= eta`.

Therefore

> `int_K W_grad,>L dt >= N-eta/2`.

The low-pass gradient work has absolute integral at most `zeta`, so the full critical pressure work satisfies

> `int_K W_3(t)dt >= N-eta/2-zeta`.

## 2. Exact `L^3` balance over the tiled interval

Let `Y(t)=||u(t)||_3^3`. R01 gives

> `(1/3) dY/dt + nu D_3 = W_3`.

Integrating on `K` and multiplying by three,

> `Y(tau_N)+3nu int_K D_3dt = Y(a)+3 int_K W_3dt >=3(N-eta/2-zeta)`.

## 3. Both left-hand terms are controlled by one velocity peak

Set

> `A_K=sup_((x,t) in T^3 x K)|u(x,t)|`.

The energy inequality gives `||u(t)||_2<=E0`, so

> `Y(tau_N)<=A_K E0^2`.

R01 defines

`D_3=int [rho|grad u|^2 + rho^-1 sum_j(u·partial_j u)^2]`.

Since `rho^-1(u·partial_j u)^2 <= rho|partial_j u|^2`,

> `D_3(t) <= 2 ||u(t)||_infinity ||grad u(t)||_2^2`.

For periodic divergence-free velocity, `||grad u||_2=||omega||_2`. Writing `q_I=int_I ||omega||_2^2dt` and using `K subset I`,

> `int_K D_3dt <= 2 A_K q_I`.

Substitution gives

> `A_K >= 3(N-eta/2-zeta)/(E0^2+6nu q_I)`.

This is the main R44 estimate.

## 4. Diagonal consequence and amplitude center

Along the R41 diagonal extraction one may prescribe `N_n->infinity`, `eta_n,zeta_n->0`, while `q_(I_n)->0`. Therefore

> `A_(K_n) >= (3-o(1))N_n/E0^2 -> infinity`.

Because the preterminal solution is smooth and `T^3 x K_n` is compact, choose a maximizing point `(x_n,t_n)` with

> `|u(x_n,t_n)|=A_(K_n)`.

This supplies an actual-trajectory amplitude center for each parent packet.

## 5. Put the center and R43 intrinsic scale on the same unit burst

The intervals `J_1,...,J_N` tile `K`. Choose one `J_n^*` containing `t_n` (if `t_n` is a shared endpoint, choose either adjacent burst).

That burst retains

- exactly one unit of high-pass common work;
- asymptotically one unit in each Helmholtz representation;
- negligible resolved absolute work;
- `|J_n^*|<=|I_n|->0`;
- `q_(J_n^*)<=q_(I_n)->0`;
- the spatial center `(x_n,t_n)` with amplitude tending to infinity.

R43 applies to that same burst. For every fixed `0<theta<1`,

> `R_theta(J_n^*,L_n) >= [theta V/(26E0^2 q_(J_n^*))]^(1/2) -> infinity`,

as well as the R42/R43 cubic floor.

Thus a hypothetical singular endpoint yields actual-trajectory unit bursts carrying simultaneously

> **a diverging spatial amplitude peak and a diverging intrinsic productive spectral scale.**

## 6. What R44 enables

R41 lacked a canonical center and R42 lacked an intrinsic radius. R43 supplied the radius; R44 now supplies a center on the same normalized object. The natural next rescaling candidate is therefore centered at `(x_n,t_n)` and measured relative to `R_theta,n`.

## 7. What R44 does not prove

The peak center may carry arbitrarily small local energy mass. R44 does not prove

- energy concentration around `x_n`;
- spatial tightness at radius `R_theta^-1`;
- `R_theta^2 |J_n^*|` bounded above or below;
- an endpoint energy atom;
- a nontrivial rescaled Navier–Stokes limit;
- a Liouville/rigidity contradiction;
- global regularity.

RD021 shows that R43's spectral floors do not force parabolic compactness. Likewise, a large `L^infinity` peak plus bounded global `L^2` energy does not by itself give a local-energy lower bound.

The critical unknown therefore remains: obtain a **local-energy/parabolic tightness theorem** for the R44 center-scale bursts, or prove many-body depletion without compactness.

## 8. Verification scope

`verification/check_R44_unit_work_amplitude_center.py` stress-tests the exact budget algebra and diagonal asymptotics. `verification/fresh_verify_e44_amplitude_d3_grid.py` independently verifies `||u||_3^3<=||u||_infinity||u||_2^2`, the periodic `||grad u||_2^2=||omega||_2^2` identity, and `D_3<=2||u||_infinity||omega||_2^2` on smooth divergence-free finite-Fourier worlds.

**R44 is a conditional center-scale extraction theorem. It is not spatial compactness and not a solution of the Navier–Stokes Millennium Problem.**
