# RD028 — R49 integrated subcritical bounds do not force temporal interiority

**Status:** `verified abstract route guard / not an NSE counterexample`

R49 fixes the work-action scale and obtains a uniform subcritical `L^4_tL^12_x` action. It is tempting to infer that the normalized productive burst automatically contains a fixed parabolic time-interior cylinder. That inference is invalid at the level of the current integrated inequalities.

Let the canonical normalized constants be fixed:

- unit cumulative common work;
- `X'=1/(2sqrt(2))`;
- a fixed nonzero `L^4` spacetime action;
- a fixed upper `L^4_tL^12_x` action;
- a fixed upper `D_3` action;
- a nonzero center-amplitude proxy;
- at least one half-unit of productive work below normalized output frequency one.

There are two elementary abstract time-profile families satisfying all of these integral constraints.

## Short branch

Take an active interval of length `tau_n=1/n` and make every action density constant on that interval with height equal to its prescribed integral divided by `tau_n`. The common-work density is `1/tau_n`, so its cumulative work is monotone from zero to one. Every R49 integrated quantity is exactly preserved while

> `tau_n -> 0`.

No fixed normalized time-interior cylinder remains.

## Long-but-boundary-active branch

Let the nominal normalized burst have length `n`, but put all work and all nonzero action in a left boundary layer of length `1/n`; set the rest to zero. Again every integrated R49 quantity is unchanged, while the active fraction is `1/n^2 ->0`.

Thus even a very long normalized interval need not make the productive object time-interior.

These constructions are deliberately **not Navier–Stokes trajectories**. Their role is logical: they prove that temporal interiority cannot follow from the scalar/integrated architecture through R49. A successful next theorem must use the PDE evolution — e.g. heat/Duhamel propagation, local energy, a dissipation-range mechanism, or a dynamic many-body constraint.
