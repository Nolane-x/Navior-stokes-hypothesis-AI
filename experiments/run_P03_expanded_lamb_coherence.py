#!/usr/bin/env python3
"""P03 preregistered expanded-family Lamb-defect coherence challenger.

The search protocol is frozen in experiments/P03_preregistered_expanded_Lamb_coherence_search.md.
This implementation uses a Numba-compiled pointwise evaluator and FFT only for the
H^{-1}/Helmholtz inner products. It does not alter the registered basis, seed,
optimizer, trial counts, thresholds, or confirmation grids.
"""
import argparse, hashlib, json, math, pathlib, time
import numpy as np
from numba import njit

WAVEVECTORS = np.array([
    (0,0,1),
    (0,1,-1),(0,1,0),(0,1,1),
    (1,-1,-1),(1,-1,0),(1,-1,1),
    (1,0,-1),(1,0,0),(1,0,1),
    (1,1,-1),(1,1,0),(1,1,1)
], dtype=np.float64)
SEED = 20260819
RANDOM_TRIALS = 3000
HILL_TRIALS = 8000
SIGMA0 = 0.20
SIGMA1 = 0.015


def polarizations(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([0.,0.,1.]) if abs(kn[2]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1); e2 /= np.linalg.norm(e2)
    return e1, e2

POL1 = np.array([polarizations(k)[0] for k in WAVEVECTORS], dtype=np.float64)
POL2 = np.array([polarizations(k)[1] for k in WAVEVECTORS], dtype=np.float64)


def make_cache(N):
    t = np.arange(N, dtype=np.float64)/N
    X,Y,Z = np.meshgrid(t,t,t,indexing='ij')
    coords = np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=0)
    phases = 2*np.pi*(WAVEVECTORS @ coords)
    cs, sn = np.cos(phases), np.sin(phases)
    freq = np.fft.fftfreq(N,d=1/N)
    KX,KY,KZ=np.meshgrid(freq,freq,freq,indexing='ij')
    k2=KX*KX+KY*KY+KZ*KZ
    weight=np.zeros_like(k2,dtype=np.float64)
    mask=k2>0
    weight[mask]=1.0/((2*np.pi)**2*k2[mask])
    return cs, sn, weight


@njit(cache=True, fastmath=False)
def physical_divergences(c, cs, sn, wave, pol1, pol2):
    """Return div(omega x u) and div(|u|u) at all grid points.

    u and grad u are evaluated analytically from the frozen trigonometric basis.
    At u=0, div(|u|u) is set to its C1 extension 0.
    """
    M=cs.shape[1]
    source=np.empty(M,np.float64)
    q=np.empty(M,np.float64)
    twopi=2*math.pi
    for x in range(M):
        u0=u1=u2=0.0
        # grad[j,i] = partial_j u_i
        g00=g01=g02=g10=g11=g12=g20=g21=g22=0.0
        lap0=lap1=lap2=0.0
        for m in range(wave.shape[0]):
            c0,c1,c2,c3=c[4*m],c[4*m+1],c[4*m+2],c[4*m+3]
            A0=c0*pol1[m,0]+c2*pol2[m,0]
            A1=c0*pol1[m,1]+c2*pol2[m,1]
            A2=c0*pol1[m,2]+c2*pol2[m,2]
            B0=c1*pol1[m,0]+c3*pol2[m,0]
            B1=c1*pol1[m,1]+c3*pol2[m,1]
            B2=c1*pol1[m,2]+c3*pol2[m,2]
            co,si=cs[m,x],sn[m,x]
            u0 += A0*co+B0*si
            u1 += A1*co+B1*si
            u2 += A2*co+B2*si
            d0=twopi*(-A0*si+B0*co)
            d1=twopi*(-A1*si+B1*co)
            d2=twopi*(-A2*si+B2*co)
            k0,k1,k2=wave[m,0],wave[m,1],wave[m,2]
            g00 += k0*d0; g01 += k0*d1; g02 += k0*d2
            g10 += k1*d0; g11 += k1*d1; g12 += k1*d2
            g20 += k2*d0; g21 += k2*d1; g22 += k2*d2
            kk=k0*k0+k1*k1+k2*k2
            lapfac=-(twopi*twopi)*kk
            lap0 += lapfac*(A0*co+B0*si)
            lap1 += lapfac*(A1*co+B1*si)
            lap2 += lapfac*(A2*co+B2*si)
        om0=g12-g21
        om1=g20-g02
        om2=g01-g10
        # div(omega x u) = u.curl(omega) - |omega|^2; curl omega=-Delta u.
        source[x] = -(u0*lap0+u1*lap1+u2*lap2) - (om0*om0+om1*om1+om2*om2)
        rho=math.sqrt(u0*u0+u1*u1+u2*u2)
        if rho>1e-14:
            a0=u0*g00+u1*g01+u2*g02
            a1=u0*g10+u1*g11+u2*g12
            a2=u0*g20+u1*g21+u2*g22
            q[x]=(u0*a0+u1*a1+u2*a2)/rho
        else:
            q[x]=0.0
    return source,q


def eval_kappa(c,N,cache=None,details=False):
    if cache is None: cache=make_cache(N)
    cs,sn,weight=cache
    source,q=physical_divergences(c,cs,sn,WAVEVECTORS,POL1,POL2)
    sh=np.fft.fftn(source.reshape(N,N,N))
    qh=np.fft.fftn(q.reshape(N,N,N))
    normfac=float(N**6)
    n2=float(np.sum(weight*np.abs(sh)**2).real/normfac)
    g2=float(np.sum(weight*np.abs(qh)**2).real/normfac)
    W=float(np.sum(weight*np.conj(sh)*qh).real/normfac)
    denom=math.sqrt(max(n2,0.0)*max(g2,0.0))
    kappa=W/denom if denom>0 else 0.0
    if details:
        return kappa, {'kappa':kappa,'W3':W,'QLamb_L2':math.sqrt(max(n2,0.0)),
                       'QG_L2':math.sqrt(max(g2,0.0))}
    return kappa


def normalize(c):
    n=np.linalg.norm(c)
    return c/n if n else c


def run(random_trials=RANDOM_TRIALS,hill_trials=HILL_TRIALS,optN=24,
        confirm=(24,32,48,64),out='P03_expanded_Lamb_coherence_result.json'):
    rng=np.random.default_rng(SEED)
    cache=make_cache(optN)
    # Compile before timing the registered measurement.
    warm=normalize(np.ones(4*WAVEVECTORS.shape[0],dtype=np.float64))
    eval_kappa(warm,optN,cache)
    bestk=-2.0; best=None
    t0=time.time()
    for j in range(random_trials):
        c=normalize(rng.standard_normal(4*WAVEVECTORS.shape[0]))
        k=eval_kappa(c,optN,cache)
        if k>bestk: bestk,best=k,c.copy()
        if (j+1)%500==0: print(f'random {j+1}/{random_trials} best={bestk:.9f}',flush=True)
    random_best=bestk
    for j in range(hill_trials):
        frac=j/(hill_trials-1) if hill_trials>1 else 1.0
        sig=SIGMA0*(SIGMA1/SIGMA0)**frac
        cand=normalize(best+sig*rng.standard_normal(4*WAVEVECTORS.shape[0]))
        k=eval_kappa(cand,optN,cache)
        if k>bestk: bestk,best=k,cand
        if (j+1)%1000==0: print(f'hill {j+1}/{hill_trials} best={bestk:.9f} sigma={sig:.5f}',flush=True)
    confirms=[]
    for N in confirm:
        kap,d=eval_kappa(best,N,None,True); d['N']=N; confirms.append(d)
        print('confirm',N,d,flush=True)
    converged=abs(confirms[-1]['kappa']-confirms[-2]['kappa'])<2e-4
    verdict='INCONCLUSIVE_DISCRETIZATION'
    if converged: verdict='H-break-half' if confirms[-1]['kappa']>=0.50 else 'H-below-half'
    source=pathlib.Path(__file__).read_bytes()
    result={
      'experiment':'P03','seed':SEED,'basis_wavevectors':WAVEVECTORS.astype(int).tolist(),
      'random_trials':random_trials,'hill_trials':hill_trials,'optimization_N':optN,
      'random_best_kappa':random_best,'hill_best_kappa_N24':bestk,
      'winner_coefficients':best.tolist(),'confirmation':confirms,
      'convergence_tolerance':2e-4,'converged_last_two':converged,'verdict':verdict,
      'script_sha256':hashlib.sha256(source).hexdigest(),'elapsed_seconds':time.time()-t0,
      'scope':'finite-dimensional preregistered expanded true-Lamb-defect challenger; NOT a Navier-Stokes regularity proof'
    }
    pathlib.Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--quick',action='store_true')
    ap.add_argument('--out',default='P03_expanded_Lamb_coherence_result.json')
    args=ap.parse_args()
    if args.quick:
        run(random_trials=20,hill_trials=30,optN=12,confirm=(12,16),out=args.out)
    else:
        run(out=args.out)
