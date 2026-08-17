# C02 — Independent short-time high-frequency vorticity challenger

**Status:** `external theorem audit / independent conditional mechanism survives`  
**Primary source:** A. Cheskidov and M. Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611  
**Clay status:** conditional regularity criterion only; does not prove arbitrary-data global smoothness

C02 supplies a second challenger to representation monoculture, now phrased directly in the high-frequency vorticity rather than velocity windows or Lamb-force actions.

## 1. Independent theorem mechanism

Cheskidov–Dai prove a regularity criterion of the following form: a 3D Navier–Stokes solution does not blow up at `t=T` if the limiting high-frequency short-time quantity

`limsup_{q->infinity} int_{T_q}^T ||Delta_q omega||_infinity dt`

is sufficiently small, for a suitable sequence `T_q -> T` defined in their framework.

This mechanism is directly vorticity-based and frequency-local. It does not start from the critical `L^3` pressure work, the Bernoulli quotient, or the R19 `P/Q` Lamb split.

## 2. Discriminating comparison with R20

R20 says that physical Lamb output above frequency `K` requires at least one velocity/vorticity input above `K/2`. This establishes **support necessity**, but it gives no `L^infinity` bound and no short-time smallness of individual vorticity blocks.

Thus R20 does not imply the Cheskidov–Dai criterion.

Conversely, the vorticity-block criterion does not directly bound the R19 scale-critical actions

`A_sol` and `A_grad`,

so it does not subsume the present Lamb-action program either.

## 3. Challenger verdict

C02 survives as a second independent conditional mechanism. Together C01 and C02 show that the high-frequency frontier admits at least three non-equivalent current representations:

1. R19/R20 physical Lamb-channel actions and high-input interactions;
2. C01 moving velocity Littlewood–Paley windows;
3. C02 short-time vorticity block integrals.

All three are compatible with the same unresolved global-regularity problem, and none is currently derivable from the energy inequality alone.

## 4. New research target created by the comparison

The sharp bridge question is:

> does divergence of the R20 high-input interaction action force a quantitative lower bound on the Cheskidov–Dai short-time vorticity-block integral at a sequence of scales, and can the converse regularity smallness be translated into summability of the R19 physical-UV channels?

This is not proved here. Establishing such a bridge would turn the independent challenger into a usable closure mechanism rather than merely a comparison route.

## 5. Falsifier / scope

C02 is not an original theorem. Its role in this research ledger is to keep an independent published mechanism alive and prevent premature closure around the Lamb representation.

It does not prove global regularity, does not establish the required smallness for arbitrary data, and does not resolve the Millennium problem.
