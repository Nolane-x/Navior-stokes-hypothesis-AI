# RD016 — Generic stress/Hölder/Bernstein route cannot beat the R32 cutoff scale

**Status:** `exact template no-go / exponent-optimization barrier`  
**Depends on:** R27, R32–R34  
**Kills:** the specific strategy `stress-divergence + generic L2/H1 interpolation + smooth Bernstein + Holder + Young + energy/enstrophy only` as a route to a compensator cutoff growth better than R32  
**Does not kill:** Navier–Stokes-specific commutator cancellation, div–curl/Hardy-space effects, transported-speed geometry, refined time-frequency localization, or estimates using stronger dynamically derived information

R33/R34 provide a legitimate smooth-filter framework. A natural attempt is to use the stress-divergence identity

`L=omega×u=div T`,

where

`T=u tensor u - |u|^2 I/2`,

and estimate the smooth low representation defect through

`D_M=<M^2L,G>`

`   =-<MT,M grad G>`.

RD016 optimizes this generic route and shows that, if one insists on closing the time integral with only the energy/enstrophy information already available a priori, the resulting cutoff growth is at least cubic. R32 already achieves quadratic lattice-scale growth.

## 1. Generic exponent family

Take

`1<=p<=3`,

`q=p/(p-1)`.

Holder gives

`|D_M|<=||MT||_p ||M grad G||_q`.

For a smooth low filter at scale `K`, Bernstein from the R27 exponent `6/5` to `q` costs

`K^alpha`,

with

> `alpha=3(5/6-1/q)`
>
> `     =3/p-1/2`.

Thus

`||M grad G||_q`

`<=C K^alpha ||grad G||_(6/5)`.

R27 gives

`||grad G||_(6/5)<=C sqrt(U D_3)`.

## 2. Stress interpolation

Since `|T|<=C|u|^2`,

`||T||_p<=C||u||_(2p)^2`.

Interpolate velocity between `L^2` and `L^6`:

`||u||_(2p)`

`<=C ||u||_2^(1-theta) ||u||_6^theta`,

where

> `theta=3(p-1)/(2p)`.

Sobolev gives `||u||_6<=C||omega||_2` in the canonical zero-mean periodic frame. Hence

`||T||_p`

`<=C E0^(2(1-theta)) ||omega||_2^(2theta)`.

Also `U=||u||_(3/2)<=E0` on the normalized torus.

Combining,

`|D_M|`

`<=C K^alpha`

` E0^(2(1-theta)+1/2)`

` ||omega||_2^(2theta) D_3^(1/2)`.

## 3. Young exposes the time-integrability requirement

Absorbing the `D_3^(1/2)` factor with Young yields a remainder proportional to

> `K^(2alpha) ||omega||_2^(4theta)`

up to fixed powers of `E0` and `nu`.

The base energy inequality supplies only

`int ||omega||_2^2 dt<infinity`.

On a finite interval, this also controls lower powers, but it does not control powers strictly above `2` without additional information.

Therefore this template can close from energy/enstrophy alone only if

> `4theta<=2`,

or

> `theta<=1/2`.

Using

`theta=3(p-1)/(2p)`,

this condition is equivalent to

> `p<=3/2`.

## 4. Optimize the cutoff exponent under that constraint

The Bernstein exponent is

`alpha=3/p-1/2`.

It decreases as `p` increases. Under `1<=p<=3/2`, the best choice is therefore

`p=3/2`.

At this endpoint,

`alpha=3/(3/2)-1/2=3/2`.

After Young the cutoff factor is

> `K^(2alpha)=K^3`.

For every smaller `p`, the power is worse.

Thus within this entire generic template:

> **energy/enstrophy-compatible stress/Hölder/Bernstein closure costs at least `K^3`.**

## 5. Comparison with R32

R32 obtains, before time integration,

`|D_K|<=C N_K^(2/3)E0^2||omega||_2^2`,

which corresponds to quadratic lattice-scale growth `~K^2`.

Therefore the optimized generic stress route is strictly weaker in cutoff growth than R32.

This is useful negative information: the visible divergence structure of `L` is not enough by itself when combined only with generic Holder/Bernstein estimates.

## 6. Consequence for R33

The promising object from R33 is

`<[M^2,C_u]omega,G>`.

RD016 says that replacing this commutator immediately by the stress divergence and then applying generic exponent bookkeeping throws away too much structure.

A genuine improvement beyond R32 must retain some structure that this template discards, such as

- cancellation in the velocity increment kernel of the commutator;
- incompressibility/div–curl compensation;
- R24 longitudinal-strain/transported-speed structure;
- helical or triadic geometry;
- trajectory-level frequency/time localization.

## 7. Verification

`verification/check_RD016_stress_holder_bernstein_barrier.py` verifies symbolically over exact rational exponents that

- `theta=3(p-1)/(2p)`;
- `4theta<=2` implies `p<=3/2`;
- `2alpha=6/p-1` is minimized at `p=3/2` under this constraint;
- the minimum cutoff exponent is exactly `3`.

RD016 is a no-go for a specified proof template, not a universal sharpness theorem for the Navier–Stokes compensator.
