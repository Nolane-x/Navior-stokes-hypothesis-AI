# R42 — Unit-burst spectral multiplicity explosion

**Status:** `exact conditional many-output theorem / first quantitative anti-sparsity result after R41`  
**Depends on:** R20, R39–R41  
**Clay status:** **NOT SOLVED**

R41 extracts normalized terminal sub-bursts `J_n` with exactly one unit of net high-pass common pressure work, vanishing duration, vanishing unweighted enstrophy cost, and negligible resolved work.  RD019 showed that synchronization alone is logically compatible with a single common-work atom escaping to frequency infinity.

R42 proves that this one-mode/few-mode escape cannot describe the **actual R41 Navier–Stokes bursts**.  The same coefficient bound behind R39–R40 makes the amount of common work that one Fourier output mode can accumulate on a short, low-enstrophy burst tend to zero.  Since the total normalized net common work remains one, the number of output modes required to carry any fixed positive fraction of that productive work must diverge.

This is a genuine many-output consequence: the terminal mechanism must become spectrally high-dimensional, not merely high-frequency.

## 1. Modewise common-work envelope

Use the R39 Fourier convention on `Omega=T^3` of volume `V`.  Let

`c_k(t)=[w_grad,k(t)+w_sol,k(t)]/2`.

R40 gives separately

`|w_grad,k(t)| <= V^{-1} E0^3 ||omega(t)||_2`,

`|w_sol,k(t)|  <= V^{-1} E0^3 ||omega(t)||_2`.

Therefore

> `|c_k(t)| <= V^{-1}E0^3 ||omega(t)||_2`.

For any preterminal interval `J`, define

> `q_J=int_J ||omega(t)||_2^2dt`,

and

> `beta_J=V^{-1}E0^3 |J|^(1/2) q_J^(1/2)`.

Then every individual Fourier mode obeys

> `int_J |c_k(t)|dt <= beta_J`.

In particular, for the signed integrated coefficient

`b_k(J)=int_J c_k(t)dt`,

> `|b_k(J)| <= beta_J`.

No frequency location enters this estimate.

## 2. Positive common-work mass of an R41 burst

Let `J` be one R41 unit burst at cutoff `L`.  By construction,

> `sum_(|k|>L) b_k(J)=1`.

For a smooth preterminal burst the Fourier pairing is absolutely summable, for example by Cauchy–Schwarz in the output mode index. Hence the positive and negative parts of the sequence are well defined and

> `sum_(|k|>L) (b_k)_+ >= 1`.

Fix `0<theta<1`.  Define the positive-work concentration number

> `m_theta(J,L)`

as the smallest cardinality of a finite set

`A subset {k: |k|>L}`

such that

> `sum_(k in A) (b_k)_+ >= theta`.

Such a finite set exists because the positive series has mass at least one.

Since every `(b_k)_+ <= beta_J`, any such set satisfies

> `theta <= |A| beta_J`.

Therefore

> `m_theta(J,L) >= theta / beta_J`
>
> `= theta V / [E0^3 sqrt(|J| q_J)]`.

This is the basic R42 anti-sparsity bound.

## 3. Quantitative explosion on the R41 good bursts

For an R41 parent packet `I` with

`N=floor(M)`

unit bursts, at least `N/2` good bursts satisfy

`|J| <= 4|I|/N`,

and

`q_J <= 4q_I/N`.

Hence for every good burst

> `sqrt(|J|q_J) <= 4 sqrt(|I|q_I)/N`.

Substituting into Section 2 gives

> `m_theta(J,L)`
>
> `>= theta V N / [4 E0^3 sqrt(|I|q_I)]`.

Along the R41 diagonal sequence,

`N_n->infinity`,

`|I_n|->0`,

and

`q_(I_n)->0`.

Therefore

> `m_theta(J_n,L_n) -> infinity`

for every fixed `theta in (0,1)`.

In particular, taking `theta=1/2`, any set of Fourier output modes carrying half of the positive common work must have cardinality tending to infinity.

## 4. Stronger than frequency escape

R40 says the common productive work evacuates every prescribed finite frequency prefix.  R42 adds an independent statement:

> after it escapes, the normalized productive work cannot remain concentrated on a bounded number of output modes.

Thus the surviving mechanism must exhibit both

1. **frequency escape:** output radii tend to infinity;
2. **spectral multiplicity explosion:** the number of productive output modes needed to carry a fixed fraction of one normalized burst tends to infinity.

The abstract one-mode escape countermodel RD019 is therefore not realizable as an R41 burst under the Navier–Stokes coefficient/enstrophy constraints. RD019 remains valid as a warning that R39 synchronization *alone* does not imply this conclusion; R42 needs the additional R41 vanishing duration/enstrophy normalization.

## 5. High-input multiplicity interface

R20 says every Lamb output mode `|k|>L` requires at least one velocity input above `L/2`.  R42 therefore forces the normalized terminal burst to create productive Lamb output across an increasing number of high-frequency output modes, each of which has genuine high-frequency velocity ancestry.

R42 does not imply that these output modes arise from disjoint input pairs; one high-frequency input can participate in many output interactions.

## 6. Interface with R37 helical geometry

R37 constrains every helical input pair contributing to the common mode: same-spin narrow-shell pairs are radially depleted, while opposite-spin near-collinear narrow-shell pairs are depleted in the minority solenoidal channel.

R42 now prevents a surviving singular mechanism from evading those pairwise restrictions by placing all normalized common work into one exceptional output mode.  It must instead assemble a fixed positive amount of common work across an increasing number of escaping output modes.

The remaining many-body question becomes sharper:

> can R37-admissible helical interactions coherently populate an exploding family of output modes with one unit of common productive work while the burst duration and unweighted enstrophy cost vanish?

## 7. What R42 does not prove

R42 does not control the angular distribution, radial bandwidth, spatial localization, or mutual orthogonality of the productive output modes.  The modes could lie on one large lattice sphere, in a narrow cone, or in a highly anisotropic set.

It also does not prove an intrinsic active scale comparable to the R41 cutoff, because all productive modes may lie far above `L_n`.

Finally, mode multiplicity alone does not create a contradiction: nonlinear Fourier convolution can populate very many modes.

The next load-bearing target is therefore **geometric multiplicity** rather than cardinality alone: prove that the large productive mode set must consume radial/angular/spin dispersion or spatial concentration at a critical cost incompatible with the R41 unit-work/vanishing-dissipation normalization.

## 8. Verification scope

`verification/check_R42_spectral_multiplicity_explosion.py` verifies the coefficient-to-concentration-number inequality, the good-burst quantitative lower bound, and adversarial positive/negative mode distributions with severe cancellation.

A fresh verifier uses exact rational sequences to audit the minimal-cardinality bound independently.

**R42 is a conditional quantitative anti-sparsity theorem for the normalized singular bursts; it is not global regularity.**
