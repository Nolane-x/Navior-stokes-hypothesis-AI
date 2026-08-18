# RD027 — Global productive-scale weighted mass does not force local spatial tightness

**Status:** `exact smooth divergence-free fragmentation route guard / not an NSE trajectory`  
**Targets:** invalid promotion of C004 global weighted-gradient nontriviality into local compactness  
**Clay status:** **NOT SOLVED**

C004 strengthens R48 by proving that productive-scale rescaling carries a fixed positive amount of `int |v|^2|grad v|^2` on a set where `|v|` is bounded away from zero. The rescaled periodic domain, however, expands to `R^3`. A global lower bound on this measure does not by itself guarantee that a fixed ball around the selected center captures positive mass.

RD027 exhibits the exact fragmentation mechanism with smooth divergence-free fields.

Let `phi` be any nonzero smooth compactly supported divergence-free vector field on the unit ball with `||phi||_infinity=1`; for example take `phi=curl(0,0,psi)` from a smooth compactly supported scalar bump and normalize. Write

> `C_X=int |phi|^2|grad phi|^2`,
>
> `C_D=int d_3(phi)`,
>
> `C_9=int |phi|^9`.

Fix amplitude `c>0`. For integers `M_n->infinity`, set `r_n=M_n^-1`. On expanding periodic boxes choose `M_n` centers whose mutual distances tend to infinity and define the disjoint-support field

> `v_n(x)=sum_j c phi((x-x_(n,j))/r_n)`.

It is smooth and divergence-free, with a distinguished center of fixed positive amplitude.

For one bump,

> `int |v|^2|grad v|^2=c^4 r_n C_X`.

Hence by disjointness

> `X_n=M_n c^4 r_n C_X=c^4 C_X`,

so the global C004 weighted-gradient mass remains a fixed positive constant.

Likewise the critical diffusion of one bump is `c^3 r_n C_D`, so

> `D_3[v_n]=c^3 C_D`,

uniformly bounded. Moreover

> `int |v_n|^9=c^9 C_9 M_n^-2`,
>
> `||v_n||_9^3=c^3 C_9^(1/3) M_n^(-2/3)->0`.

Fix any finite physical radius `R`. For large `n`, the ball `B_R(x_(n,1))` meets only the first bump, and therefore

> `int_(B_R(x_(n,1))) |v_n|^2|grad v_n|^2`
>
> `=c^4 C_X/M_n ->0`.

Thus global weighted-gradient nonvanishing, nonzero center amplitude, bounded critical `D_3`, and bounded `L^9` do **not** imply local spatial tightness on an expanding domain.

This is not a Navier–Stokes orbit and does not model the R48 common-work Fourier measure. It falsifies only the functional shortcut from C004 global rescaled nonvanishing to a fixed-ball local atom. A future closure theorem must use genuine PDE/common-work structure to prevent fragmentation: local-energy propagation, a work-to-space concentration theorem, concentration-compactness rigidity, or many-body depletion.
