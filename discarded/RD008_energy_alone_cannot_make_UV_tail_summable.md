# RD008 — Energy alone cannot force summable ultraviolet decay of the R08 tail action

**Status:** `exact scaling no-go`  
**Depends on:** R08, R13  
**Kills:** attempts to close R13 by deriving a scale-summable ultraviolet tail estimate from the `L^2` energy/enstrophy budget alone, without an additional critical structural mechanism  
**Does not kill:** true-triad cancellations, helicity/alignment depletion, critical-space estimates, epsilon-regularity, or trajectory compactness

R13 proves that every fixed finite-frequency part of the R08 tail action is finite by energy. The remaining hope might be that the same energy budget yields a decaying bound as the frequency scale tends to infinity, so that the shell actions become summable.

The Navier–Stokes scaling forbids such a conclusion from energy alone.

## 1. Local parabolic scaling

On `R^3`, or on a sufficiently small chart before embedding a compactly supported smooth divergence-free profile into the torus, use the standard scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`.

Then

`||u_lambda(t)||_2^2 = lambda^(-1)||u(lambda^2 t)||_2^2`.

Thus the kinetic energy of a geometrically similar concentrated structure **decreases** as its characteristic frequency `lambda` increases.

The integrated enstrophy has the same energy homogeneity:

`int ||grad u_lambda||_2^2 dt`

`= lambda^(-1) int ||grad u||_2^2 dt`.

So the complete energy-dissipation budget assigned to a scaled copy becomes smaller at finer scales.

## 2. R08 tail action is critical

R08's local Euclidean scaling audit gives

`U_lambda=||u_lambda||_(3/2)=lambda^(-1) U`,

`M_*(u_lambda)=lambda M_*(u)`,

and

`Q(1_{|u_lambda|>M_*(u_lambda)}(omega_lambda×u_lambda))`

has `L^2` norm squared scaling like `lambda^3`.

Since `dt` scales like `lambda^(-2)`, the product

`U * ||Q(tail Lamb)||_2^2 * dt`

has total scaling exponent

`-1 + 3 - 2 = 0`.

Therefore

> the R08 tail action of a parabolically rescaled copy is invariant even while its `L^2` energy budget tends to zero like `lambda^(-1)`.

## 3. Consequence for ultraviolet shell estimates

Suppose one attempted to prove a universal per-scale estimate of the schematic form

`A_tail at frequency ~lambda <= epsilon(lambda) * E(u_0)`

with `epsilon(lambda)->0` based only on the energy inequality and scale-insensitive universal constants.

Applying it to a rescaled compactly supported profile would make the right-hand side decay faster with concentration while the critical left-hand action remains invariant. Unless the estimate includes an additional quantity with critical homogeneity, this contradicts scaling.

More generally, an energy-only argument cannot create the missing **positive power of inverse frequency** required to make an arbitrary critical defect cascade summable.

## 4. Relation to R13

R13 is still valid: for each *fixed* Fourier cutoff, low frequencies are controlled. Its bound worsens with the cutoff, consistent with RD008.

Together R13 and RD008 establish a sharp division:

1. energy removes every fixed infrared/finite-frequency obstruction;
2. energy cannot suppress the ultraviolet critical cascade uniformly;
3. the missing theorem must use structure with critical scaling.

## 5. What additional structure could evade the no-go

A successful ultraviolet estimate must contain information absent from plain energy, for example:

- exact helical/Leray triad coefficients;
- a scale-critical velocity/pressure quantity;
- geometric depletion of vortex stretching/Lamb forcing;
- cancellation between neighboring frequency shells;
- a dynamically enforced sparsity/coherence condition;
- epsilon-regularity/compactness that forbids recurrence of a normalized critical bubble.

RD008 prevents the project from mistaking the supercritical `L^2` energy budget for the missing critical invariant.
