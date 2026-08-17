# R38 — Uniform multi-cutoff and shellwise terminal-packet synchronization

**Status:** `exact conditional extraction theorem / stronger than R31 single-cutoff diagonalization`  
**Depends on:** R28, R30–R32  
**Clay status:** no global regularity conclusion; the theorem applies under the same hypothetical singular-endpoint scenario as R28/R30

R31 extracts a terminal packet synchronized at one prescribed cutoff `K_n`. R32 replaces the crude window-length mismatch estimate by

> `int_I |D_K|dt`
>
> `<=C_1 N_K^(2/3)E0^2 int_I ||omega||_2^2dt`,

where `D_K=W_grad,>K-W_sol,>K`.

R38 spends this terminal absolute continuity globally in cutoff. It synchronizes **every sharp cutoff in an entire growing finite frequency hierarchy on the same terminal packet**, and sharp-shell orthogonality then upgrades the result to **every shell inside that hierarchy** at the level of signed integrated pressure work.

## 1. Setup

Assume the same finite maximal endpoint `T*` and singular scenario used by R28/R30. For finite cutoff `K`, set

`A_grad^K(a,b)=int_a^b W_grad,>K dt`,

`A_sol^K(a,b)=int_a^b W_sol,>K dt`,

`A_bal^K(a,b)=int_a^b U(t) min(||Pi_>K PL||_2^2,||Pi_>K QL||_2^2)dt`,

with `L=omega×u`, `U=||u||_(3/2)`.

R28/R30 imply that for every fixed finite `K` and every `a<T*`, all three quantities tend to `+infinity` as `b↑T*`.

Let

> `q(a)=int_a^{T*}||omega||_2^2dt`.

The first energy inequality gives `q(a)->0` as `a↑T*`.

## 2. Uniform synchronization below a finite ceiling

Fix a finite ceiling `L` with `N_L>0` and tolerance `epsilon>0`. (If `N_L=0`, the low projector is trivial and the mismatch statement is vacuous.)

For every `0<=K<=L`, `N_K<=N_L`. R32 therefore gives, for every `[a,b] subset [a,T*)`,

> `|A_grad^K(a,b)-A_sol^K(a,b)|`
>
> `<=C_1 N_L^(2/3)E0^2 q(a)`.

Choose `a` sufficiently close to `T*` that

> `q(a)<=epsilon/[C_1 N_L^(2/3)E0^2]`.

Then **simultaneously for every real sharp cutoff `K in [0,L]`** and every `b in (a,T*)`,

> `|A_grad^K(a,b)-A_sol^K(a,b)|<=epsilon`.

No universal decay modulus for `q(a)` is assumed; the start time may depend on `L` and `epsilon`.

## 3. One upper endpoint makes every cutoff productive

Although `K` is continuous, on the periodic lattice `Pi_<=K` changes only when `K` crosses one of the finitely many radii

`{|k|: k in Z^3, |k|<=L}`.

Thus only finitely many distinct high-pass projectors occur below finite `L`.

For each distinct projector, R28/R30 give terminal divergence of `A_grad^K`, `A_sol^K`, and `A_bal^K`. Given `M>0`, take for each cutoff class a time beyond which all three exceed `M`; the maximum of these finitely many thresholds is still below `T*`. Hence one common `b<T*` satisfies, **for every `K<=L` simultaneously**,

> `A_grad^K(a,b)>=M`,
>
> `A_sol^K(a,b)>=M`,
>
> `A_bal^K(a,b)>=M`.

The Section 2 mismatch estimate remains valid on the same interval.

## 4. Growing-hierarchy theorem with arbitrary terminal-window scale

Let arbitrary prescribed sequences satisfy

`L_n->infinity`,

`epsilon_n->0`,

`M_n->infinity`,

`delta_n->0`, `delta_n>0`.

Choose `a_n<T*` so close to `T*` that

> `T*-a_n<=delta_n`

and

> `q(a_n)<=epsilon_n/[C_1 N_{L_n}^(2/3)E0^2]`.

Section 3 supplies `b_n in (a_n,T*)` such that, for `I_n=[a_n,b_n]`, **every sharp cutoff `K<=L_n` simultaneously satisfies**

> `A_grad^K(I_n)>=M_n`,
>
> `A_sol^K(I_n)>=M_n`,
>
> `A_bal^K(I_n)>=M_n`,

and

> `|A_grad^K(I_n)-A_sol^K(I_n)|<=epsilon_n`.

Moreover

> `|I_n|<=delta_n->0`.

Thus the frequency ceiling and terminal-window scale may be prescribed independently. This does **not** localize the active spectrum near `L_n`; it says that all cumulative tails beginning below `L_n` remain large and synchronized on the same arbitrarily short terminal packet.

## 5. Shellwise signed-work synchronization

The sharp projectors are orthogonal. For `0<=K_1<K_2<=L_n`, define the integrated shell works on `I_n`

`S_grad^(K1,K2)=A_grad^K1(I_n)-A_grad^K2(I_n)`,

`S_sol^(K1,K2)=A_sol^K1(I_n)-A_sol^K2(I_n)`.

These are exactly the signed productive pressure works carried by Fourier modes in the shell `K_1<|k|<=K_2` for the gradient and solenoidal representations, respectively.

Let

`Delta_n(K)=A_grad^K(I_n)-A_sol^K(I_n)`.

Then

> `S_grad^(K1,K2)-S_sol^(K1,K2)`
>
> `=Delta_n(K_1)-Delta_n(K_2)`.

Since `sup_(K<=L_n)|Delta_n(K)|<=epsilon_n`, R38 obtains the uniform shell corollary

> `sup_(0<=K1<K2<=L_n)`
>
> `|S_grad^(K1,K2)-S_sol^(K1,K2)|`
>
> `<=2epsilon_n`.

Thus the two productive representations synchronize not only as cumulative tails but on **every sharp annulus inside the expanding hierarchy**, at the level of signed time-integrated work.

This is stronger than R31/R32 single-cutoff synchronization.

## 6. What the theorem rules out — and what survives

R38 rules out macroscopic separation of the two pressure-work representations both cumulatively and on any fixed signed shell inside the extracted hierarchy.

It still does **not** prove:

- positivity of each shell work;
- same-shell overlap of the P/Q **Lamb energies** or of the balanced minimum;
- total-variation closeness of the two signed work measures;
- absence of cancellation among positive and negative sub-shell contributions;
- spatial concentration;
- spectral localization near `L_n`;
- a nontrivial compact rescaled limit.

Therefore RD014 is not contradicted: its obstruction concerns channel energy overlap, whereas R38 controls signed integrated pressure-work representations.

## 7. Interface with R37

R37 narrows an individual full-strength balanced Lamb source to opposite-spin/non-collinear activity or substantial radial dispersion. R38 narrows the **scale organization** of a hypothetical terminal packet: the gradient and solenoidal productive works must agree, up to vanishing error, on every cumulative cutoff and every signed shell in an expanding hierarchy.

A future rigidity theorem can therefore target a much more constrained object:

> a terminal packet maintaining R37 spin/radial/angular conflict while its two productive pressure-work representations remain uniformly shell-synchronized throughout an expanding frequency hierarchy.

The live obstruction is coherent signed accumulation compatible with both R37 pair geometry and R38 shell synchronization.

## 8. Verification

`verification/check_R38_uniform_multicutoff_packets.py` verifies finite lattice-threshold classes, monotonic `N_K` domination, uniform tolerance selection, finite-family common-endpoint extraction, arbitrary terminal-window scales, and the shell-difference consequence of a uniformly small cumulative mismatch.

The analytic theorem uses only R28/R30 terminal divergence, R32's enstrophy-tail estimate, orthogonality of sharp periodic Fourier shells, finiteness of lattice modes below finite radius, and absolute continuity of the enstrophy integral.

**R38 is a stronger necessary-structure theorem for a hypothetical singular endpoint, not a global-regularity proof.**
