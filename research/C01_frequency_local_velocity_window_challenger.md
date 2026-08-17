# C01 — Independent Littlewood–Paley velocity-window challenger

**Status:** `external theorem audit / independent conditional mechanism survives`  
**Primary source:** Z. Grujic and Z. Bradshaw, *Frequency localized regularity criteria for the 3D Navier-Stokes equations*, arXiv:1501.01043  
**Clay status:** conditional regularity criterion only; does not prove arbitrary-data global smoothness

The R18–R20 program represents a possible singularity through divergent physical Lamb action and then proves that ultraviolet Lamb output requires high-frequency velocity input. C01 challenges any implicit assumption that this Lamb-force representation is the unique useful high-frequency route.

## 1. Independent theorem mechanism

Grujic–Bradshaw establish frequency-localized regularity criteria for 3D Navier–Stokes. In their Theorem 1, under the stated Besov continuity hypothesis for a Leray–Hopf weak solution, regularity beyond a candidate time `T` follows if a **finite moving window of Littlewood–Paley velocity frequencies** remains sufficiently subdued at a finite collection of times.

The mechanism is stated directly in terms of velocity blocks `Delta_j u`, with low and high endpoint frequencies `J_low(t)` and `J_high(t)`. Its proof architecture uses frequency localization, local well-posedness, low-frequency energy suppression and weak–strong uniqueness; it does not require the R19 Helmholtz split of `omega×u` into `P L` and `Q L`.

## 2. Discriminating comparison with R20

R20 proves only the support implication

`high Lamb output >K  =>  at least one velocity input >K/2`.

That implication does **not** provide the Besov/L-infinity smallness or finite-window amplitude control required by the Grujic–Bradshaw criterion.

Conversely, the frequency-window theorem does not provide a bound on

`A_sol = int ||u||_(3/2)||P(omega×u)||_2^2 dt`

or

`A_grad = int ||u||_(3/2)||Q(omega×u)||_2^2 dt`.

Therefore neither representation currently subsumes the other.

## 3. Challenger verdict

C01 survives as an **independent conditional route to regularity**. It falsifies only the methodological monoculture claim

> every useful ultraviolet regularity mechanism must first be phrased as finiteness of the R19 Lamb-channel actions.

That claim is false: a velocity-window theorem can certify regularity without first estimating those actions.

C01 does not falsify R18–R20 themselves. The two programs are compatible and may be bridgeable.

## 4. New research target created by the comparison

The valuable bridge question is now:

> can the R20 high-input interaction actions be quantitatively converted into the moving-window velocity control required by a frequency-local criterion, or can failure of the frequency-window criterion be shown to force a more rigid version of the R19 two-channel ultraviolet cascade?

A successful theorem in either direction would reduce representation uncertainty. No such bridge is claimed here.

## 5. Falsifier / scope

C01 would cease to be independent if a rigorous equivalence were proved between its moving-window criterion and the R19/R20 action formulation. No such equivalence is presently established in this ledger.

This artifact is a source-grounded challenger audit, not an original regularity theorem and not a solution of the Millennium problem.
