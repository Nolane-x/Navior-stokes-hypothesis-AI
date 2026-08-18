# RD019 — Finite-catalog total-variation synchronization does not imply tightness

**Status:** `exact logical countermodel / route guard`  
**Depends on:** R38, R39, R39-C  
**Scope:** falsifies an inference between abstract work-measure properties; **not** a Navier–Stokes blow-up construction

R39 upgrades the P/Q representation mismatch to spacetime total-variation synchronization on every prescribed finite Fourier catalog.  It is tempting to infer that such synchronization yields a compact or tight terminal work profile.  That inference is false without an additional estimate on the common mode.

## Countermodel

Let

- `F_n` be any finite catalog;
- `L_n->infinity` be any prescribed resolved radial ceiling;
- `M_n->infinity` be any prescribed productive threshold;
- `I_n` be any interval of positive length `delta_n`.

Choose one lattice mode `kappa_n` satisfying

> `|kappa_n| > L_n`

and

> `kappa_n notin F_n`.

Define abstract modewise work densities on `I_n` by

> `w_grad,kappa_n(t)=w_sol,kappa_n(t)=M_n/delta_n`,

and set both work densities to zero at every other mode.

Then:

1. `w_grad-w_sol=0` identically, so the R39 spacetime `L^1_t ell^1_k` mismatch is exactly zero on **every** catalog, not merely on `F_n`;
2. for every cutoff `K<=L_n`, the high-pass net works satisfy

   `A_grad^K(I_n)=A_sol^K(I_n)=M_n`;

3. every radial/signed-shell mismatch below `L_n` is zero;
4. the common mode

   `c_k=(w_grad,k+w_sol,k)/2`

   is positive and has mass `M_n`, but all of that mass sits at `kappa_n`;
5. if `|kappa_n|->infinity`, the common productive measures are not tight in frequency.

Thus even **perfect** P/Q synchronization, including total-variation synchronization, is compatible with arbitrary escape of the common productive work to unresolved frequencies.

## What is falsified

RD019 falsifies each shortcut

> `R39 TV synchronization => frequency tightness`,

> `R39 TV synchronization => compact terminal work profile`,

and

> `P/Q agreement => common-mode smallness`.

None follows without a separate common-mode estimate.

## What is not falsified

The countermodel is an abstract assignment of output-mode work densities.  It is not asserted to arise from

`L=omega×u`, `G=|u|u`

for an actual Navier–Stokes solution.  Therefore it does not falsify the possibility that the PDE itself supplies an additional tightness or rigidity mechanism.

R37 remains relevant precisely because an actual escaping mode must be built from helical input interactions, and R38/R39 remain relevant because any such actual mechanism must synchronize its two exact Helmholtz representations.

## Post-RD019 frontier

After R39/RD019, another synchronization estimate is not load-bearing.  A closing argument must attack at least one of:

1. **frequency tightness:** prevent the positive common-mode work from outrunning every controlled catalog;
2. **within-output many-body rigidity:** show that R37-admissible helical pairs cannot coherently build the required common mode at an escaping output scale;
3. **spatial/physical rigidity:** extract a terminal object and rule it out using a continuation/Liouville/adjoint mechanism.

This is the route guard for E39.
