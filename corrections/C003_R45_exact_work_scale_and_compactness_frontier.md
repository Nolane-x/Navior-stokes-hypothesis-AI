# C003 — R45 exact work-scale sharpening and compactness-frontier correction

**Status:** `canonical sharpening / scope correction`  
**Applies to:** R45 and RD023  
**Clay status:** **NOT SOLVED**

R45 as first committed used the coarse scale

> `Gamma_J=A_J^2 q_J`,

where `A_J=sup_J ||u||_infinity` and `q_J=int_J||omega||_2^2dt`.

That statement is valid, but the proof itself gives a strictly sharper intrinsic scale before the supremum is taken:

> `Lambda_J := int_J ||u(t)||_infinity^2 ||omega(t)||_2^2 dt`.

The canonical E45 interpretation is therefore the following.

## 1. Sharp tail theorem

For the R41 unit common-work coefficients `b_k(J)`, Parseval, Cauchy--Schwarz, `|L|<=|u||omega|`, and `|grad(|u|u)|<=2|u||grad u|` give

> `T_J(R):=sum_(|k|>R)|b_k(J)|`
>
> `<= Lambda_J/R`
>
> `<= Gamma_J/R`.

Thus `Lambda_J`, not `Gamma_J`, is the sharp upper work-frequency produced by the argument.

Because the unit burst satisfies

> `sum_(|k|>L0)b_k(J)=1`,

one obtains

> `L0 <= Lambda_J <= Gamma_J`.

The per-burst amplitude consequence remains

> `A_J >= sqrt(L0/q_J)`.

## 2. Sharp positive-work quantile upper bound

For the R43 positive common-work quantile radius `R_theta`, `0<theta<1`,

> `R_theta(J,L0) <= Lambda_J/(1-theta)`
>
> `<= Gamma_J/(1-theta)`.

All amplitude lower bounds obtained in R45 remain valid by using the coarser final inequality `Lambda_J<=Gamma_J`.

## 3. High-frequency compactness is only spectral

Normalize the signed common-work measure by the sharp work scale:

> `mu_J=sum_(|k|>L0)b_k delta_(k/Lambda_J)`.

Then for every `r>0`,

> `|mu_J|({|xi|>r}) <= 1/r`.

This is uniform high-frequency total-variation tightness of the **work measure**.  It is not compactness of the velocity field.

Define the spectral spread

> `Delta_theta^work := Lambda_J/R_theta(J,L0)`.

R45 yields only

> `Delta_theta^work >= 1-theta`.

A bounded `Delta_theta^work` would give a nontrivial bounded normalized frequency window for a fixed fraction of productive work.  It would still not supply parabolic or spatial compactness.

## 4. RD023 survives the sharpening

RD023 is strengthened by taking, in its abstract high-multiplicity work cloud,

> `Lambda_n = Gamma_n = n^p`,  `p>1`.

Then all R42/R43/R45 scalar envelopes and the **sharp** tail bound

> `T_n(R)<=Lambda_n/R`

hold, while every productive output mode satisfies

> `|k|/Lambda_n -> 0`.

Therefore high-tail tightness at the exact R45 work scale still does not imply lower-frequency non-collapse.

## 5. Correct post-E45 compactness frontier

The spectral unknown is

> `Delta_theta^work=Lambda_J/R_theta`.

But it is not the only compactness issue.  Even if the spectral spread is bounded, the earlier route guards remain live:

- **parabolic scale:** quantities such as `R_theta^2 |J|` or `Lambda_J^2 |J|` are not yet controlled (RD021);
- **spatial scale:** a diverging amplitude center does not itself force local kinetic-energy tightness or an endpoint atom (RD022).

Hence the load-bearing next theorem must provide at least one genuinely PDE-level bridge:

1. spectral non-collapse / bounded `Delta_theta^work` from R36--R37 input-output geometry;
2. parabolic scale-time comparability for the same burst lineage;
3. local-energy propagation/tightness around the same center and scale;
4. or a many-body depletion theorem that rules out the burst before compactness is needed.

C003 prevents the invalid statement that R45 reduces the entire remaining problem to one scalar spread parameter.  It reduces the **spectral** part to that parameter while leaving time and space explicit.
