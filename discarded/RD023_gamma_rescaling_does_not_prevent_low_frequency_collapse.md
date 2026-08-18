# RD023 — Gamma-rescaling high-tail tightness does not prevent low-frequency collapse

**Status:** `exact abstract route guard / not a Navier–Stokes trajectory`  
**Targets:** invalid promotion of R45 high-frequency total-variation tightness into full spectral compactness  
**Clay status:** **NOT SOLVED**

R45 defines `Gamma_J=A_J^2 q_J` and proves

`sum_(|k|>R)|b_k|<=Gamma_J/R`.

After scaling frequencies by `Gamma_J`, this gives uniform high-frequency tightness.  It does **not** give a lower-frequency non-collapse estimate.  RD023 constructs a positive, high-multiplicity abstract work family satisfying the scalar envelopes of R42, R43 and R45 while all productive mass collapses to frequency zero in `k/Gamma_n`.

## 1. Productive mode cloud

For integer `n>=2`, take the lattice box

> `S_n={k in Z^3: n<=k_j<=2n-1 for j=1,2,3}`.

Then

> `M_n=|S_n|=n^3`,

and every mode satisfies

> `sqrt(3)n <= |k| <= 2sqrt(3)n`.

Assign equal positive integrated common work

> `b_k=1/M_n` for `k in S_n`,

and zero otherwise.  Thus

> `sum_k b_k=1`,

and the productive multiplicity is exactly `n^3->infinity`.

Choose a parent cutoff `L_n=n/2`, so all resolved work below `L_n` is identically zero.

## 2. Match the R42/R43 scalar envelopes

Set, with `E0=V=1`,

> `q_n=4sqrt(3)/n^2`,

> `ell_n=1/n^4`.

Then the R43 `1/|k|` cap is

`alpha_n/|k|=q_n/|k| >=2/n^3 >1/n^3=b_k`.

The R42 frequency-independent cap is

`sqrt(ell_n q_n)=sqrt(4sqrt(3))/n^3`,

which is also larger than `1/n^3`.

The R45 stress low-mode cap

`ell_n |k|`

is of order `n^-3` and already dominates `b_k` throughout the box with the project constant used in R45.  Thus the family satisfies all three per-mode/capacity envelopes simultaneously while `q_n->0`, `ell_n->0`, and multiplicity diverges.

## 3. Make the R45 upper scale much larger than the productive cloud

Fix any `p>1` and set

> `Gamma_n=n^p`.

Choose

> `A_n^2=Gamma_n/q_n`,

so by construction

> `A_n^2 q_n=Gamma_n`.

The R45 tail estimate is satisfied: below the support, the tail total variation equals one while `Gamma_n/R` is larger than one for all sufficiently large `n`; above the support the tail is zero.

Also `Gamma_n>=L_n`.

## 4. Collapse after Gamma normalization

Every productive mode obeys

> `|k|/Gamma_n <= 2sqrt(3) n^(1-p) ->0`.

Hence the normalized positive work measure

> `mu_n=sum_k b_k delta_(k/Gamma_n)`

has unit mass but converges weakly to a point mass at zero frequency.

At the same time

- multiplicity tends to infinity;
- the parent resolved catalog is empty of work;
- `q_n` and `ell_n` tend to zero;
- the R42/R43 mode caps hold;
- the R45 high-tail TV estimate holds.

Therefore

> **high-frequency TV tightness in the `Gamma=A^2q` scale does not by itself imply nontrivial annular spectral compactness.**

## 5. Exact frontier exposed by RD023

The missing parameter is the spread

> `Delta_theta=Gamma/R_theta`.

R45 controls the upper tail, while R43 forces `R_theta->infinity` in physical units.  RD023 shows that `Delta_theta` may still diverge within all scalar envelope constraints currently available.

A future theorem must use structure not represented in this abstract model, such as

- R36/R37 input-output/helical depletion;
- a PDE relation between `Gamma` and an actual velocity/vorticity frequency quantile;
- parabolic local-energy propagation;
- Oseen/backward-uniqueness rigidity;
- another invariant that forbids the `Delta_theta->infinity` branch.

## 6. Scope

RD023 is **not** a Navier–Stokes solution or blow-up construction.  It is an exact logical countermodel to the inference

> `R42 + R43 + R45 scalar spectral envelopes => full spectral compactness after Gamma rescaling`.

The route guard exists to prevent E45 from overstating what the new upper-tail theorem achieves.
