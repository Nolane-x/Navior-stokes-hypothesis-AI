# P05 — Ten-world robustness stress suite for the R19 two-channel physical-UV representation

**Status:** `preregistered-style structural stress suite / 10 worlds passed`  
**Depends on:** R17–R19, RD009–RD011  
**Clay status:** **NOT a global-regularity proof**

R19 represents the surviving cutoff-free physical ultraviolet obstruction by two orthogonal critical channels:

- `A_sol = int ||u||_(3/2) ||P(omega×u)||_2^2 dt`,
- `A_grad = int ||u||_(3/2) ||Q(omega×u)||_2^2 dt`.

P05 asks whether this representation survives a deliberately heterogeneous collection of exact structural edge cases. The purpose is not to estimate a probability of regularity; it is to expose representation mistakes, hidden one-channel assumptions, scaling errors, and overfitting to one Fourier example.

## Frozen stress worlds

### W1 — Beltrami null endpoint

Take an exact Beltrami field such as `u=(sin z,cos z,0)`, for which `curl u=u`. Then

`L=(curl u)×u=0`.

Both R19 channels vanish. The representation must include this exact nonlinear-depletion endpoint without singular normalization.

### W2 — Gradient-only smooth shear

For the RD010 shear `u=a(t)(0,cos x,0)`, the physical Lamb force is longitudinal:

`P L=0`, `Q L=L`.

This stresses the Bernoulli-gradient extreme.

### W3 — Nonzero solenoidal triad forcing

RD009 certifies

`<(D-4)^2v,P L>=-4/5`.

Thus `P L` is nonzero in an exact smooth `3–4–5` interaction. This stresses the dynamical/solenoidal branch.

### W4 — RD009 below the nonlinear-production threshold

For the amplitude family `u_A=A v` with `nu=1`,

`(sigma_D^2)'(0)=(8/5)A^3-34A^2`.

At `A=20`, viscosity wins and the derivative is negative.

### W5 — RD009 above the nonlinear-production threshold

At `A=22`, the same exact geometry gives a positive derivative. W4/W5 ensure the representation does not silently hard-code a sign of the bandwidth dynamics.

### W6 — Solenoidal-heavier exact state

RD011 gives an exact finite-Fourier field with

`||P L||_2^2 / ||L||_2^2 = 12655/22809 > 1/2`.

### W7 — Gradient-heavier exact state

RD011 gives another exact field with

`||P L||_2^2 / ||L||_2^2 = 4328/129969 < 1/2`.

W6/W7 jointly stress the no-dominance conclusion.

### W8 — Sharp-cutoff boundary perturbation

For a shear-level threshold ratio `0<c<1`, the cutoff boundary lies at `x=arccos c`, and the Lamb value there has squared sine factor

`sin^2(2 arccos c)=4c^2(1-c^2)>0`.

The checker evaluates `c=1/3,1/2,2/3`. Thus RD010's cutoff-generated jump is not a knife-edge accident at the single value `1/2`.

### W9 — Coordinate-rotated shear

Rotate the RD010 shear so its wave vector and longitudinal Lamb force lie on another coordinate axis. Orthogonal projection still gives `P L=0`, showing the gradient-only witness is not tied to the x-axis convention.

### W10 — Critical scaling audit

For either R19 channel under Navier–Stokes scaling, the exponents are

`||u||_(3/2): -1`, `||channel||_2^2: +3`, `dt: -2`,

which sum to zero.

## Verdict

All 10 frozen structural worlds pass the R19 representation.

This means only that no contradiction was found among these exact stress cases. It does **not** establish:

- finiteness of `A_sol` or `A_grad`;
- a trajectory-level comparison between the channels;
- exclusion of a physical ultraviolet cascade;
- compactness or Liouville closure;
- global smoothness of 3D Navier–Stokes.

The strongest surviving unknown remains dynamical:

> prove a scale-critical trajectory-level mechanism that prevents a smooth Navier–Stokes trajectory from sustaining a non-summable physical ultraviolet sequence in either R19 channel, or derive a coupling that forces one divergent branch into a rigorously controlled regime of the other.

## Verification

`verification/check_P05_R19_robustness_worlds.py` executes all ten exact/algebraic stress worlds with Python standard-library arithmetic and emits `PASS P05 R19 robustness worlds=10` only if every frozen assertion survives.
