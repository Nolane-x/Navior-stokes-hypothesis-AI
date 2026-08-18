# R49 external theorem interface — Wang, Wu, Zhou epsilon-regularity without pressure

**Primary source:** Yanqing Wang, Gang Wu, Daoguo Zhou, *A epsilon-regularity criterion without pressure of suitable weak solutions to the Navier-Stokes equations at one scale*, arXiv:1811.09927.

**Imported statement used by R49:** Theorem 1.1 states that if `(u,Pi)` is a suitable weak solution in `Q(1)`, then for every `delta>0` there exists an epsilon such that

`int_(Q(1)) |u|^(5/2+delta) <= epsilon`

implies `u` is bounded in a smaller cylinder (`Q(1/16)` in the theorem statement).

R49 uses only `delta=1/2`, i.e. the exponent `3`, after parabolically rescaling an interior `Q_r` to unit size. The internally proved `L^4_tL^12_x` estimate gives the needed scale-invariant `L^3` velocity integral smallness as `r->0`.

**Scope guard:** This primary theorem is not reproved by the repository's Python certificates. The certificates verify only the new algebra/scaling that places R49 inside the theorem's smallness regime when a parabolic cylinder is temporally interior. The theorem does not provide the missing temporal interiority itself.

**Clay status:** not a global regularity proof.
