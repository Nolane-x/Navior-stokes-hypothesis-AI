# R28 — Dual high-pass pressure-work ultraviolet escape

**Status:** `exact conditional reduction / productive-UV theorem`  
**Depends on:** R01, R05–R06, R18–R19, R25, R27, RD014  
**Clay status:** does not bound the surviving high-output work; no global regularity conclusion

R27 proves that a singular trajectory in the critical `L^3` endpoint framework must accumulate divergent balanced Lamb-channel action. RD014 shows that global P/Q channel balance does not imply that the two Lamb components occupy the same Fourier shells.

R28 therefore switches from channel energy to the quantity that actually drives the critical norm: the signed pressure work

`W_3`.

Let

`rho=|u|`, `G=rho u`, `L=omega×u`.

R03/R05 give the two exact representations

> `W_3=<Q L,Q G>`
>
> `   =-<P L,P G>`.

R28 proves that if the endpoint `L^3` mechanism blows up, then **both representations must push net positive work beyond every fixed Fourier cutoff**.

## 1. Exact low/high decomposition in the gradient representation

Let `Pi_{<=K}` be the sharp Fourier projector onto the finite nonzero set

`Lambda_K={k in Z^3:0<|k|<=K}`,

and let `Pi_{>K}=I-Pi_{<=K}` on nonzero modes. All these projectors commute with `P` and `Q`.

Because low and high Fourier supports are orthogonal,

`W_3`

`=<Pi_{<=K}Q L,Pi_{<=K}Q G>`

` +<Pi_{>K}Q L,Pi_{>K}Q G>`.

Define

`W_grad,<=K=<Pi_{<=K}Q L,Pi_{<=K}Q G>`,

`W_grad,>K=<Pi_{>K}Q L,Pi_{>K}Q G>`.

Then exactly

> `W_3=W_grad,<=K+W_grad,>K`.

R25 proves

> `int_0^T |W_grad,<=K| dt < infinity`

for every fixed `K` and every finite smooth interval, using only energy/enstrophy control.

## 2. The complementary solenoidal low/high decomposition

R05 also gives

`W_3=-<P L,P G>`.

The same Fourier orthogonality yields

`W_3`

`=-<Pi_{<=K}P L,Pi_{<=K}P G>`

` -<Pi_{>K}P L,Pi_{>K}P G>`.

Define

`W_sol,<=K=-<Pi_{<=K}P L,Pi_{<=K}P G>`,

`W_sol,>K=-<Pi_{>K}P L,Pi_{>K}P G>`.

Then

> `W_3=W_sol,<=K+W_sol,>K`.

The same finite-mode estimate used in R25 applies here. For every Fourier mode,

`|Ghat(k)|<=||G||_1=||u||_2^2`,

`|Lhat(k)|<=||L||_1<=||omega||_2||u||_2`.

Since `P` is an orthogonal contraction,

`||Pi_{<=K}P G||_2<=sqrt(N_K)||u||_2^2`,

`||Pi_{<=K}P L||_2<=sqrt(N_K)||omega||_2||u||_2`.

Thus

> `|W_sol,<=K|<=N_K||omega||_2||u||_2^3`,

and the energy inequality gives

> `int_0^T |W_sol,<=K|dt`
>
> `<=N_K E0^4 sqrt(T/(2nu))<infinity`.

So fixed low-output work is harmless in **both** Helmholtz representations.

## 3. Blow-up forces the total pressure work to diverge positively

Let

`Y(t)=||u(t)||_3^3`.

R01 gives

`(1/3)Y'(t)+nu D_3(t)=W_3(t)`.

Hence

`Y(T)/3 + nu int_0^T D_3 dt`

`=Y(0)/3 + int_0^T W_3 dt`.

If a putative finite maximal time `T*` is reached through the endpoint mechanism with

`Y(T)->infinity` as `T↑T*`,

then necessarily

> `int_0^T W_3(t)dt -> +infinity`.

This is stronger than saying only the absolute pressure work diverges: the cumulative signed work must defeat dissipation and grow without bound.

As in R06/R27, using `Y` divergence as the singularity marker relies on the corresponding periodic/localized endpoint `L^infinity_t L^3_x` continuation theorem.

## 4. Both high-pass representations must carry divergent productive work

Fix any finite `K`.

From Section 1,

`int_0^T W_grad,>K dt`

`=int_0^T W_3 dt-int_0^T W_grad,<=K dt`.

The second term remains finite absolutely as `T↑T*`, while the first tends to `+infinity`. Therefore

> `int_0^T W_grad,>K dt -> +infinity`.

Likewise, Section 2 gives

> `int_0^T W_sol,>K dt -> +infinity`.

Thus for **every fixed output cutoff** a singular endpoint trajectory must generate unbounded net positive high-frequency pressure work in both exact representations:

> `Q/Bernoulli representation:  <Q L,Q G>`;
>
> `P/dynamical representation: -<P L,P G>`.

The two ultraviolet contributions need not occur on the same shell or at the same instant; RD014 prevents that inference without further dynamics.

## 5. Dyadic productive-shell consequence

Let `{Delta_j}` be any orthogonal sharp Fourier-shell partition of the nonzero modes. Define

`w_j^grad=<Delta_j QL,Delta_j QG>`,

`w_j^sol=-<Delta_j PL,Delta_j PG>`.

Then

`W_3=sum_j w_j^grad=sum_j w_j^sol`.

For every fixed shell threshold `J`, Section 4 implies that the cumulative high-shell sums in each representation have unbounded positive integral near a singular endpoint.

Consequently the positive shell contributions cannot be summable:

> `sum_{j>J} int_0^{T*} (w_j^grad)_+ dt = infinity`,

and

> `sum_{j>J} int_0^{T*} (w_j^sol)_+ dt = infinity`.

Therefore each representation contains an infinite ultraviolet sequence of **productive pressure-work shells**.

The productive shell sequences for the two representations may differ. R28 does not prove shell-by-shell P/Q synchronization.

## 6. Relation to R27 and RD014

R27 says the weaker global physical Lamb channel must accumulate divergent scale-critical action.

RD014 says global channel balance alone does not enforce common-shell overlap.

R28 adds a different constraint that RD014 cannot remove:

> both exact pressure-work representations must themselves become productively ultraviolet above every fixed cutoff.

This means spectral separation cannot make one representation remain a bounded low-frequency bookkeeping device while the other alone drives critical growth.

The surviving freedom is narrower:

- the productive P and Q shell sequences can be different;
- their times can be offset;
- their test-field alignments can differ;
- but both must escape to arbitrarily high output and accumulate unbounded positive work.

## 7. New frontier: dynamic cross-representation scale synchronization

The next load-bearing question is now:

> Can the two productive ultraviolet pressure-work sequences remain indefinitely separated in scale/time along an actual Navier–Stokes trajectory, or does the nonlinear triad/commutator structure force enough interaction to make them jointly controllable by dissipation or a known continuation criterion?

This is more precise than the original E23 request to control two independent channel norms.

Candidate mechanisms include:

1. frequency-local complementarity defects between the P and Q pressure-work representations;
2. paraproduct commutators exploiting the pointwise identity `(omega×u)·(|u|u)=0`;
3. helical triad geometry coupling the R17 solenoidal bandwidth source to the R24 longitudinal-strain/Bernoulli source;
4. a concentration-compactness argument for a minimal object carrying two separated productive UV sequences.

R28 proves none of these closing mechanisms.

## 8. Verification

`verification/check_R28_dual_highpass_pressure_work_escape.py` independently reconstructs the two Helmholtz pressure pairings on a smooth divergence-free periodic field, verifies exact low/high Fourier decompositions numerically to machine precision across several cutoffs, and checks the abstract finite-low/divergent-total escape logic.

The continuum theorem itself uses only Fourier orthogonality, R01/R05 identities, R25-type finite-mode bounds, Cauchy–Schwarz and the energy inequality.
