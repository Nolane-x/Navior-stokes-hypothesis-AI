# R39-C — Product-measure and Jordan-part synchronization

**Status:** `exact corollary of R39 / same milestone, not a new proof obligation`  
**Depends on:** R39  
**Clay status:** **NOT SOLVED**

R39 proves, on the extracted terminal packets `I_n` and prescribed finite output catalogs `F_n`,

> `int_(I_n) sum_(k in F_n) |d_k(t)| dt <= eta_n`,

where

`d_k=w_grad,k-w_sol,k`.

This is already the total variation of the signed representation-mismatch measure on the product space

`I_n × F_n`

with reference measure `dt × counting_measure`.

R39-C records two consequences that are stronger than signed-shell synchronization and are useful for the next rigidity step.

## 1. Uniformity over arbitrary time/mode subsets

For every measurable `E subset I_n` and every subset `A subset F_n`,

> `| int_E sum_(k in A) d_k(t) dt | <= eta_n`.

More generally, if the catalog is partitioned into arbitrary cells and the time interval is partitioned into arbitrary measurable pieces, the sum of the absolute mismatches over all product cells is at most `eta_n`.

Thus a resolved-catalog counterexample cannot hide a large P/Q mismatch by alternating

- between different Fourier modes;
- between different radial/angular sectors;
- between early and late parts of the same terminal packet;
- or between any finite collection of time-frequency cells.

The estimate is measure-level, not merely an equality of cumulative integrals.

## 2. Positive and negative productive-work parts synchronize

For real numbers `a,b`,

`|a_+-b_+| <= |a-b|`

and

`|a_--b_-| <= |a-b|`,

where `a_+=max(a,0)` and `a_-=max(-a,0)`.

Applying this pointwise to `w_grad,k,w_sol,k` and summing gives

> `int_(I_n) sum_(k in F_n)`
>
> `|(w_grad,k)_+-(w_sol,k)_+| dt <= eta_n`,

and likewise

> `int_(I_n) sum_(k in F_n)`
>
> `|(w_grad,k)_--(w_sol,k)_-| dt <= eta_n`.

Therefore the **productive positive-work measures themselves** become indistinguishable in total variation on every resolved finite catalog.  The same is true of the destructive negative-work measures.

This closes another ambiguity left by R38: within the resolved catalog, gradient and solenoidal productive work cannot remain macroscopically separated by sign, time, shell, or angular sector.

## 3. Common-mode consequence

Let

`c_k=(w_grad,k+w_sol,k)/2`.

Since

`w_grad,k-c_k=d_k/2`,

`w_sol,k-c_k=-d_k/2`,

R39 immediately yields

> `int_(I_n) sum_(k in F_n) |w_grad,k-c_k| dt <= eta_n/2`,

> `int_(I_n) sum_(k in F_n) |w_sol,k-c_k| dt <= eta_n/2`.

Hence both exact Helmholtz representations collapse, in spacetime total variation on the resolved catalog, onto **one common output-mode work measure**.

The post-R39 issue is therefore genuinely the magnitude/tightness/triad structure of the common mode, not residual P/Q synchronization.

## 4. Remaining escape hatch

The corollary does not control the internal mode distribution of the unresolved exterior `|k|>L_n`.  R38 controls only its aggregate signed mismatch.  A hypothetical singular mechanism may therefore continue to move the common productive work to frequencies faster than the resolved catalog expands.

It also does not turn R37 pairwise helical depletion into a many-body estimate at a fixed output mode.

Thus the live frontier after R39-C is:

> **tightness or rigidity of the escaping positive common-mode work, plus coherent many-triad accumulation inside each escaping output mode.**

No global regularity conclusion is asserted.
