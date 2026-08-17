# W5-E23 Full Verification Result

**Status:** `PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY`  
**Milestone:** W5 / epoch 23  
**Clay status:** **NOT SOLVED**

## GitHub full-suite gate

Canonical full-suite workflow:

`.github/workflows/verify-w5-e23-all-python.yml`

Final hardened run:

- run id: `32021561231`
- head: `6131f59da26d063e6c165c4b02b5522a2f00289a`
- conclusion: **success**
- Python certificates discovered by the E23 package: `25`

The workflow installs the declared numerical dependencies and runs every `verification/*.py` certificate. Before each certificate it removes dynamic Numba/Python cache directories so legacy dynamically imported Numba experiment modules are independently replayable.

## Local artifact replay

The public-safe E23 package produced by GitHub Actions was materialized into the research runtime and replayed independently from the packaged files.

Clean-cache replay:

- first group: `11/11 PASS`;
- second group: `14/14 PASS`;
- total: **`25/25 PASS`**.

The suite includes exact symbolic/algebraic checks, finite-dimensional adversarial challengers, scaling certificates, R17–R23 structural checks, RD009–RD012 no-go certificates, P05 robustness worlds and two fresh-context verification lineages.

Every script retains its own scope statement. Passing this suite does **not** imply arbitrary-data global regularity.

## Harness correction retained for provenance

An earlier aggregate run `32021153556` failed before any certificate executed because `actions/setup-python` was configured with `cache: pip` while the repository had no cache dependency manifest. The mathematical verification step was skipped.

The harness was corrected and then hardened further against dynamic Numba cache reuse. The final run `32021561231` passed.

During local repeated replay, two legacy challenger scripts also exposed a reproducibility hazard: dynamically imported modules using Numba `cache=True` can leave on-disk cache entries referring to module name `<dynamic>`. Those entries are not tracked in GitHub and are not present in the public-safe package, but a second run in the same workspace can attempt to reload them. The aggregate workflow therefore removes `__pycache__` between independent certificate processes.

This is classified as a verifier-harness issue, not a theorem assertion failure.

## Current World gate

The Nolane World W5 convergence gate remains **FAILED / NONCONVERGED** with internal score

`0.8333333333333334`.

Remaining blockers:

- `critical_unknowns unresolved`;
- `material value-of-thought remains`.

The all-green certificate suite establishes consistency of the current partial theorem/counterexample ledger. It does not remove those two research blockers.
