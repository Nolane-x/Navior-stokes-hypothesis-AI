# RD014 — Global Helmholtz-channel balance does not imply shellwise balance

**Status:** `exact finite-Fourier no-go / scale-synchronization hazard`  
**Depends on:** R19, R27  
**Kills:** any proof step that silently promotes global `min(||PL||_2^2,||QL||_2^2)` balance into comparable P/Q mass on the same Fourier shells  
**Does not kill:** a dynamical theorem forcing scale synchronization along actual Navier–Stokes trajectories

R27 proves that a singular trajectory compatible with the critical `L^3` endpoint spine must have divergent balanced action

`A_bal = int U min(||P L||_2^2,||Q L||_2^2) dt`,

where `L=omega×u` and `U=||u||_(3/2)`.

A tempting next inference is:

> if the two global channel norms are simultaneously substantial, then the solenoidal and gradient Lamb components must overlap substantially on the same Fourier scales.

That inference is false for smooth real divergence-free finite-Fourier states.

## 1. Exact three-mode velocity field

Use the `2 pi`-periodic torus and Fourier convention

`u(x)=sum_k uhat(k) exp(i k·x)`,

with conjugate coefficients at negative wavevectors. Take the three positive modes

`k1=(1,3,-3)`,

`uhat(k1)=(-6-15i, 9+11i, 7+6i)`;

`k2=(1,-2,2)`,

`uhat(k2)=(-2-2i, 1, 2+i)`;

`k3=(1,0,2)`,

`uhat(k3)=(-6-2i, -9+i, 3+i)`.

Each coefficient satisfies

`k_j · uhat(k_j)=0`,

so the resulting real trigonometric polynomial is smooth, mean-zero and divergence-free.

Construct exactly

`omegahat(k)=i k×uhat(k)`

and then convolve to obtain

`Lhat=widehat(omega×u)`.

For each nonzero output mode, split

`Lhat=P Lhat+Q Lhat`.

## 2. Global channels are both substantial

Exact rational-complex arithmetic gives

> `||P L||_2^2 = 79378456/21`,

> `||Q L||_2^2 = 227945624/21`.

Therefore

> `||P L||_2^2 / ||L||_2^2`
>
> `= 9922307/38415510`
>
> `= 0.2582890868...`.

Thus the weaker global channel still carries more than one quarter of the full Lamb energy. This is not a near-pure-gradient state.

## 3. But the spectral shells are strongly separated

Group output modes by the exact shell label

`s=|k|^2`.

Let `P_s` and `Q_s` be the total squared P/Q energies on shell `s`. The exact shell table is:

| `s` | `P_s` | `Q_s` | P fraction |
|---:|---:|---:|---:|
| 4 | 7392 | 8992 | 0.45117... |
| 6 | 260000/3 | 27460/3 | 0.90447... |
| 14 | 12894680/7 | 184904/7 | 0.98586... |
| 20 | 0 | 145440 | 0 |
| 24 | 35840/3 | 71968/3 | 0.33244... |
| 34 | 1813224 | 8584 | 0.99529... |
| 36 | 0 | 2880 | 0 |
| 50 | 18600 | 745300 | 0.02435... |
| 76 | 0 | 9883800 | 0 |

In particular:

- shell `34` is more than `99.5%` solenoidal;
- shell `50` is more than `97.5%` gradient;
- shell `76` is exactly gradient-only;
- multiple other shells are strongly one-sided.

Define the shell-overlap functional

`O_shell = sum_s min(P_s,Q_s)`.

Normalize by the weaker global channel:

> `O_shell / min(||P L||_2^2,||Q L||_2^2)`
>
> `= 430977/19844614`
>
> `= 0.0217175804...`.

So only about **2.17%** of the minority global channel energy is forced to overlap shellwise under this natural metric, despite the global P fraction being about **25.8%**.

This exact state therefore rules out any universal shell-overlap lower bound with coefficient larger than `430977/19844614` based solely on the global channel norms. More importantly, it falsifies the qualitative shortcut that global R27 balance automatically means same-shell balance.

It does **not** prove that no smaller positive universal coefficient exists, nor does it construct a Navier–Stokes blow-up trajectory.

## 4. Consequence for the post-R27 frontier

R27 provides **timewise global channel synchronization**:

`min(||P L||_2^2,||Q L||_2^2)`

must accumulate non-summable critical action along a hypothetical singular trajectory.

RD014 shows that this is not yet **scale synchronization**. The two global norms may be fed by very different output shells.

Therefore the next load-bearing theorem cannot simply replace

`min(global P energy, global Q energy)`

by

`sum_j min(P-shell energy_j,Q-shell energy_j)`

without a new dynamical argument.

The live question becomes:

> Does actual Navier–Stokes evolution force enough P/Q overlap in common high-frequency scale-time boxes, or can the two channels remain spectrally separated while their global balanced action diverges?

That is a strictly sharper unknown than the E23 two-branch problem.

## 5. Verification

`verification/check_RD014_exact_shell_separation.py` reconstructs the real finite-Fourier field with exact rational-complex arithmetic, computes vorticity and Lamb convolution, performs exact Helmholtz projection, reproduces every shell energy in the table, and certifies the exact global and shell-overlap ratios.
