# RD025 — Uniform per-burst critical action does not imply terminal summability

**Status:** `exact scalar route guard / not a Navier–Stokes trajectory`  
**Targets:** overpromotion of the R47 per-burst `D_3` / `L^3_tL^9_x` bounds  
**Clay status:** **NOT SOLVED**

R47 extracts infinitely many disjoint terminal unit-work bursts with uniformly bounded critical diffusion and uniformly bounded critical `L^3_tL^9_x` action. A Serrin continuation theorem, however, needs finiteness on an entire terminal neighborhood, not merely a common bound on each disjoint member.

The logical gap is exact and elementary.

For `n>=1`, take disjoint abstract shrinking intervals accumulating at one endpoint and assign the scalar burst data

> `common_work(J_n)=1`,
>
> `|J_n|=2^(-2n)`,
>
> `q_n=2^(-3n)`,
>
> `D3_n=1/nu`,
>
> `Serrin_n=int_(J_n)||u||_9^3dt=1`.

The exact scalar `L^3` balance is compatible with constant endpoint `Y_n` because

> `Delta Y_n/3 + nu D3_n = 0 + 1 = common_work(J_n)`.

Thus, at the level of all scalar consequences used in the R47 averaging step,

- each burst carries one positive work unit;
- duration tends to zero;
- unweighted enstrophy cost tends to zero;
- `D3_n` is uniformly bounded;
- the critical Serrin action is uniformly bounded;

but

> `sum_n Serrin_n=infinity`,

and likewise `sum_n D3_n=infinity`.

This is not an NSE construction. It proves only that

> **uniform critical control per normalized burst is not terminal summability or critical smallness.**

A future closure theorem must exploit additional orbit structure: scale alignment, compactness/rigidity, many-body depletion, or a summable improvement beyond R47.
