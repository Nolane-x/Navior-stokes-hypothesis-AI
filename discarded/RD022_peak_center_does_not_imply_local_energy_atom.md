# RD022 — A diverging velocity peak does not imply a local-energy atom

**Status:** `exact smooth divergence-free concentration route guard / not a Navier–Stokes trajectory`  
**Targets:** invalid promotion of the R44 amplitude center into spatial compactness or an endpoint energy atom  
**Clay status:** **NOT SOLVED**

R44 extracts an actual-trajectory point `(x_n,t_n)` where the velocity amplitude diverges on a unit common-work burst. That is a genuine spatial center, but by itself it does not imply that a fixed amount of kinetic energy is concentrated near the center.

RD022 records a sharp functional countermodel: smooth divergence-free periodic fields can have arbitrarily large `L^infinity` peaks while the total and local `L^2` energy around that peak tend to zero. Moreover, after assigning sufficiently short abstract time intervals, their integrated enstrophy cost can tend to zero as well. The family is not claimed to solve Navier–Stokes in time; it only falsifies a purely functional inference from the R44 outputs.

## 1. A compactly supported divergence-free seed

Choose any nonzero `psi in C_c^infinity(B(0,1/10))` on `R^3` whose gradient is not identically zero, and define

> `v(y)=(partial_2 psi(y), -partial_1 psi(y), 0)`.

Then `div v=0`, `v` is smooth and compactly supported, and after rescaling `psi` by a constant we may assume

> `||v||_infinity=1`.

Embed the support inside one coordinate chart of the torus `T^3`; periodic extension is smooth because the field vanishes in a neighborhood of the chart boundary.

Let

`C_0=||v||_2^2>0`, `C_1=||grad v||_2^2>0`.

## 2. Amplitude-radius concentration family

For amplitudes `A_n->infinity` and radii `r_n->0`, define near a fixed point `x_0`

> `u_n(x)=A_n v((x-x_0)/r_n)`.

For all sufficiently large `n` the support remains inside the chosen torus chart. The field is smooth and divergence-free, with

> `||u_n||_infinity=A_n`,

> `||u_n||_2^2=C_0 A_n^2 r_n^3`,

> `||grad u_n||_2^2=C_1 A_n^2 r_n`.

The entire kinetic energy lies inside a ball of radius `O(r_n)` around the peak center.

## 3. Peak divergence with vanishing local energy

Take

> `A_n=n`, `r_n=n^-1`.

Then

> `||u_n||_infinity=n -> infinity`,

but

> `||u_n||_2^2=C_0 n^-1 -> 0`.

Consequently, for every fixed multiple `R r_n` large enough to contain the support,

> `int_(B(x_0,Rr_n)) |u_n|^2 dx = C_0 n^-1 ->0`.

Thus a diverging peak does not even force a nonzero local-energy atom at the natural concentration radius of the field.

## 4. Compatibility with vanishing integrated enstrophy cost as a route guard

For the same family,

> `||grad u_n||_2^2=C_1 n`.

Assign an abstract interval length

> `ell_n=n^-2`.

If the field were held at this scale for that duration, the integrated enstrophy budget would be

> `ell_n ||grad u_n||_2^2=C_1 n^-1 ->0`.

This does **not** assert that the time-independent family is an unforced Navier–Stokes solution. It shows only that the three scalar outputs

- `L^infinity` amplitude diverges,
- interval length tends to zero,
- integrated `H^1`/enstrophy cost tends to zero,

are functionally compatible with vanishing local energy. Therefore those outputs alone cannot prove compactness.

## 5. Consequence for E44

R44's center is valuable because it chooses where to look, but a closing concentration-compactness theorem must add genuinely dynamical information, for example one of:

- a local-energy lower bound at a radius tied to the R43 productive scale;
- a backward persistence/propagation estimate around the peak;
- a critical norm lower bound that survives rescaling;
- a local pressure/Oseen mechanism preventing arbitrarily thin high-amplitude spikes;
- a many-body depletion theorem that bypasses spatial compactness.

The invalid shortcut

> `large peak + bounded global energy + small burst enstrophy cost => local-energy atom`

is therefore rejected.

## 6. Verification

`verification/check_RD022_peak_center_local_energy_countermodel.py` checks the exact scaling exponents and a range of amplitude-radius-time choices, including the canonical `A=n`, `r=n^-1`, `ell=n^-2` family.

**RD022 is a route guard against an unjustified compactness step. It is not a Navier–Stokes blow-up construction.**
