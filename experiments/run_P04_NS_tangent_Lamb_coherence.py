#!/usr/bin/env python3
"""P04 preregistered Navier-Stokes tangent challenger.

Uses the committed P03 winner, exact spectral derivatives/Leray projection, and
the frozen derivative protocol in P04_preregistered_NS_tangent_Lamb_coherence.md.
This is a finite-dimensional numerical trajectory diagnostic, NOT a proof of
Navier-Stokes regularity or blow-up.
"""
import argparse, hashlib, json, math, pathlib, time
import numpy as np

WAVEVECTORS=np.array([
    (0,0,1),(0,1,-1),(0,1,0),(0,1,1),
    (1,-1,-1),(1,-1,0),(1,-1,1),
    (1,0,-1),(1,0,0),(1,0,1),
    (1,1,-1),(1,1,0),(1,1,1)
],dtype=float)
COEFF=np.array([
0.5016708978853571,-0.1219964116665458,-0.001255006754030708,-0.08399147133127532,
-0.09847439717897939,-0.08551687488171743,0.1584268112718571,0.0352091966268361,
-0.036371581263444155,0.05841548813443032,0.035157959086053535,-0.13705911844230145,
-0.16726796997353402,0.1300522239905492,0.014785897975220626,-0.06607006358368221,
-0.10260657593319555,0.043862369514323464,0.12478852619033935,-0.13825784305684838,
0.14229933424504146,0.16966898278364023,-0.03630903919237615,-0.12419412236320804,
0.1272588092314737,-0.08379266423971417,0.027161187481870536,-0.02788790904118733,
-0.17165864035719422,-0.09856006297058206,0.23600196500530154,-0.09530439786060656,
0.035513078297826045,-0.016178110498890137,-0.30949472785300236,-0.3249440452881142,
0.05664889574422015,-0.1239195207284787,-0.08046014363679285,0.2125408369381787,
0.012792673326167799,-0.011817659381589875,0.15465825896378377,0.01534753799658004,
-0.02897738892965079,-0.05661047987408721,-0.1566551084708309,-0.11634794694395127,
-0.057889000832231426,0.12044663369562335,-0.02233823654528806,0.09563408689010848
],dtype=float)
AMPLITUDES=(0.5,1.0,2.0,4.0,8.0)
NU=1.0

def polarizations(k):
    kn=k/np.linalg.norm(k)
    ref=np.array([0.,0.,1.]) if abs(kn[2])<0.9 else np.array([0.,1.,0.])
    e1=np.cross(kn,ref); e1/=np.linalg.norm(e1)
    e2=np.cross(kn,e1); e2/=np.linalg.norm(e2)
    return e1,e2
POL1=np.array([polarizations(k)[0] for k in WAVEVECTORS])
POL2=np.array([polarizations(k)[1] for k in WAVEVECTORS])

def freqgrids(N):
    f=np.fft.fftfreq(N,d=1/N)
    KX,KY,KZ=np.meshgrid(f,f,f,indexing='ij')
    return KX,KY,KZ,KX*KX+KY*KY+KZ*KZ

def q_project_hat(vh,KX,KY,KZ,k2):
    dot=KX*vh[0]+KY*vh[1]+KZ*vh[2]
    q=np.zeros_like(vh); mask=k2>0
    for j,K in enumerate((KX,KY,KZ)):
        q[j][mask]=K[mask]*dot[mask]/k2[mask]
    return q

def build_initial(N,a):
    t=np.arange(N)/N
    X,Y,Z=np.meshgrid(t,t,t,indexing='ij')
    u=np.zeros((3,N,N,N),float)
    for m,k in enumerate(WAVEVECTORS):
        phase=2*np.pi*(k[0]*X+k[1]*Y+k[2]*Z)
        co,si=np.cos(phase),np.sin(phase)
        c0,c1,c2,c3=COEFF[4*m:4*m+4]
        A=c0*POL1[m]+c2*POL2[m]
        B=c1*POL1[m]+c3*POL2[m]
        for j in range(3):
            u[j]+=A[j]*co+B[j]*si
    return a*u

def l2norm(u):
    return float(np.sqrt(np.mean(np.sum(u*u,axis=0))))

def kappa_l(u):
    N=u.shape[1]; KX,KY,KZ,k2=freqgrids(N); twopi=2*np.pi
    uh=np.fft.fftn(u,axes=(1,2,3))
    omh=np.empty_like(uh)
    omh[0]=1j*twopi*(KY*uh[2]-KZ*uh[1])
    omh[1]=1j*twopi*(KZ*uh[0]-KX*uh[2])
    omh[2]=1j*twopi*(KX*uh[1]-KY*uh[0])
    om=np.fft.ifftn(omh,axes=(1,2,3)).real
    L=np.moveaxis(np.cross(np.moveaxis(om,0,-1),np.moveaxis(u,0,-1)),-1,0)
    rho=np.sqrt(np.sum(u*u,axis=0)); G=rho[None,...]*u
    Lh=np.fft.fftn(L,axes=(1,2,3)); Gh=np.fft.fftn(G,axes=(1,2,3))
    QLh=q_project_hat(Lh,KX,KY,KZ,k2); QGh=q_project_hat(Gh,KX,KY,KZ,k2)
    normfac=float(N**6)
    W=float(np.sum(np.conj(QLh)*QGh).real/normfac)
    nL=float(np.sum(np.abs(QLh)**2).real/normfac)
    nG=float(np.sum(np.abs(QGh)**2).real/normfac)
    return W/math.sqrt(nL*nG)

def ns_tangent(u,nu=NU):
    N=u.shape[1]; KX,KY,KZ,k2=freqgrids(N); Ks=(KX,KY,KZ); twopi=2*np.pi
    uh=np.fft.fftn(u,axes=(1,2,3))
    grads=np.empty((3,3,N,N,N),float)
    for j,K in enumerate(Ks):
        for i in range(3):
            grads[j,i]=np.fft.ifftn(1j*twopi*K*uh[i]).real
    conv=np.zeros_like(u)
    for i in range(3):
        for j in range(3):
            conv[i]+=u[j]*grads[j,i]
    ch=np.fft.fftn(conv,axes=(1,2,3)); Pch=ch-q_project_hat(ch,KX,KY,KZ,k2)
    lap=-(twopi**2*k2)[None,...]*uh
    return np.fft.ifftn(nu*lap-Pch,axes=(1,2,3)).real

def measure(N,a):
    u=build_initial(N,a); F=ns_tangent(u)
    un,fn=l2norm(u),l2norm(F); h0=2e-5*un/fn; k0=kappa_l(u)
    ds=[]
    for fac in (0.5,1.0,2.0):
        h=h0*fac
        ds.append((kappa_l(u+h*F)-kappa_l(u-h*F))/(2*h))
    mean=float(np.mean(ds)); spread=(max(ds)-min(ds))/max(1.0,abs(mean))
    sign='positive' if min(ds)>0 else ('negative' if max(ds)<0 else 'unstable')
    return {'N':N,'amplitude':a,'kappa0':k0,'u_L2':un,'F_NS_L2':fn,'h0':h0,
            'derivatives':ds,'mean_derivative':mean,'relative_spread':spread,
            'sign':sign,'stable':bool(spread<5e-3 and sign!='unstable')}

def run(out='P04_NS_tangent_Lamb_coherence_result.json'):
    t0=time.time(); rows=[]
    for N in (48,64):
        for a in AMPLITUDES:
            r=measure(N,a); rows.append(r); print(r,flush=True)
    by={(r['N'],r['amplitude']):r for r in rows}
    conclusive=all(by[(N,a)]['stable'] for N in (48,64) for a in AMPLITUDES)
    any_nonnegative=any(by[(N,a)]['sign']!='negative' for N in (48,64) for a in AMPLITUDES)
    if not conclusive: verdict='INCONCLUSIVE'
    elif any_nonnegative: verdict='H-nonrepel'
    else: verdict='H-repel'
    result={'experiment':'P04','nu':NU,'amplitudes':list(AMPLITUDES),
            'resolutions':[48,64],'rows':rows,'verdict':verdict,
            'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.time()-t0,
            'scope':'finite-dimensional true-NS tangent diagnostic; NOT global regularity or blow-up proof'}
    pathlib.Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='P04_NS_tangent_Lamb_coherence_result.json')
    args=ap.parse_args(); run(args.out)
