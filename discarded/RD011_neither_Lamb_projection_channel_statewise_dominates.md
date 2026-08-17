# RD011 — Neither Helmholtz channel of the Lamb force universally dominates the other statewise

**Status:** `exact finite-Fourier counterexamples to two channel-dominance shortcuts`  
**Depends on:** R19  
**Does not imply:** blow-up, divergence of either critical action, or failure of global regularity

R19 proves the orthogonal decomposition

`||L||_2^2=||P L||_2^2+||Q L||_2^2`, `L=omega×u`,

and splits the physical ultraviolet program into a solenoidal branch `P L` and a Bernoulli-gradient branch `Q L`.

A tempting simplification would be to prove only one branch and use a universal statewise ordering such as

`||P L||_2^2 <= ||Q L||_2^2`

or the reverse.

RD011 gives exact smooth real divergence-free finite-Fourier fields falsifying **both coefficient-one orderings**.

Use the `2 pi`-periodic torus and Fourier convention

`u(x)=sum_k uhat(k) exp(i k·x)`,

with `uhat(-k)=conj(uhat(k))`. All unlisted coefficients vanish. For each field below the listed coefficients satisfy `k·uhat(k)=0`, so the resulting real trigonometric polynomial is smooth, mean-zero and divergence-free.

For each state construct

`omegahat(k)=i k×uhat(k)`,

then convolve exactly to obtain `Lhat=widehat(omega×u)` and split every nonzero mode into the orthogonal Fourier projections `P` and `Q`.

## 1. Solenoidal-heavier exact state

Take

`k1=(1,1,0)`,

`uhat(k1)=(3/2+i, -3/2-i, 2-2i)`;

`k2=(1,-1,1)`,

`uhat(k2)=(-5/3+2i, -7/3-i, -2/3-3i)`;

`k3=(0,1,0)`,

`uhat(k3)=(1-3i, 0, -2-3i)`.

Include the conjugate coefficients at `-k1,-k2,-k3`.

Exact rational-complex convolution gives

> `||P L||_2^2 = 63275/27`,

> `||Q L||_2^2 = 50770/27`.

Hence

> `||P L||_2^2 / ||L||_2^2 = 12655/22809 = 0.5548248498... > 1/2`.

Therefore the universal ordering `||P L||_2^2 <= ||Q L||_2^2` is false.

## 2. Gradient-heavier exact state

Take

`k1=(1,1,0)`,

`uhat(k1)=(5/2+i, -5/2-i, 1-i)`;

`k2=(0,0,1)`,

`uhat(k2)=(3i, -3i, 0)`;

`k3=(1,1,-1)`,

`uhat(k3)=(1+3i, 1-3i, 2)`.

Again include conjugates at the negative modes.

Exact convolution gives

> `||P L||_2^2 = 4328/9`,

> `||Q L||_2^2 = 125641/9`.

Hence

> `||P L||_2^2 / ||L||_2^2 = 4328/129969 = 0.0333002485... < 1/2`.

Therefore the universal reverse ordering `||Q L||_2^2 <= ||P L||_2^2` is false.

## 3. Consequence

The R19 two-channel fork cannot be collapsed by a coefficient-one pointwise dominance principle valid for all smooth divergence-free states.

Amplitude scaling does not change either ratio, so this failure is not restricted to small fields.

This does **not** rule out:

- a trajectory-integrated comparison along actual Navier–Stokes evolution;
- a comparison under additional geometry, helicity, localization, or near-singularity hypotheses;
- a nontrivial inequality with larger constants plus an independently controlled remainder;
- a dynamical transfer theorem coupling the two channels.

Those remain viable, but they require genuinely new information beyond the instantaneous Helmholtz decomposition.

## 4. Verification

`verification/check_RD011_exact_Lamb_channel_counterexamples.py` reconstructs both real fields with exact rational-complex arithmetic, computes vorticity and Lamb convolution, performs exact Fourier Helmholtz projection, and certifies all four rational channel energies and both ratios.
