# C004 — R48 productive-scale nontriviality strengthens from a point to weighted-gradient mass

**Status:** `exact strengthening / no retraction of R48`  
**Applies to:** R48  
**Clay status:** **NOT SOLVED**

R48 proves, on every R47-good unit common-work burst `J`,

> `R_theta <= Sigma_J/(1-theta)`,
>
> `Sigma_J=sqrt(2) X_J`,
>
> `X_J=int_J int |u|^2|grad u|^2`,

and identifies a work-linked set `H_J={|u|>=B_J/2}` carrying at least `X_J/2`, where

> `B_J=X_J/D_J`, `D_J=int_J D_3`.

The original R48 statement emphasized the pointwise consequence after rescaling by `R_theta`.  The same inequalities give a stronger scale-invariant measure consequence.

From the quantile upper bound,

> `X_J/R_theta >= (1-theta)/sqrt(2)`.

Let `r_J=1/R_theta` and

> `v_J(y,s)=r_J u(x_J+r_J y,t_J+r_J^2s)`.

The spacetime weighted-gradient action scales by one power of `r_J`, hence exactly

> `int |v_J|^2|grad v_J|^2 dy ds = X_J/R_theta`.

Therefore

> `int |v_J|^2|grad v_J|^2 dy ds >= (1-theta)/sqrt(2)`.

Moreover, the rescaled image `H'_J` of the R48 work-linked high-amplitude set satisfies

> `int_(H'_J)|v_J|^2|grad v_J|^2 dy ds >= (1-theta)/(2sqrt(2))`,

and throughout that set R48 gives

> `|v_J| >= 3nu(1-theta)/(56sqrt(2))`.

Thus productive-scale nontriviality is not merely the existence of one nonzero point: a fixed positive amount of a scale-invariant weighted-gradient measure lives where the rescaled velocity is uniformly bounded away from zero.

This still does **not** prove spatial tightness.  `H'_J` and its measure may spread to spatial infinity on the expanding rescaled torus, and RD026 separately shows that the rescaled burst duration may collapse to zero or diverge.  C004 therefore strengthens the compactness input without closing the remaining parabolic/spatial concentration problem.
