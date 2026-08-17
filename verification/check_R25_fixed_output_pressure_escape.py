import math
import numpy as np


def mode_count(K):
    c=0
    for a in range(-K,K+1):
        for b in range(-K,K+1):
            for c0 in range(-K,K+1):
                if (a,b,c0)!=(0,0,0) and a*a+b*b+c0*c0 <= K*K:
                    c += 1
    return c

for K in range(1,9):
    Nk=mode_count(K)
    assert Nk > 0
    assert Nk <= (2*K+1)**3-1

# Independent finite-field reproducibility sanity check on the normalized torus.
N=32
x=np.arange(N)/N*2*np.pi
X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
u=np.stack([
    np.sin(Y)+0.5*np.cos(Z),
    np.sin(Z)+0.4*np.cos(X),
    np.sin(X)+0.3*np.cos(Y),
],axis=-1)
omega=np.stack([
    -0.3*np.sin(Y)-np.cos(Z),
    -0.5*np.sin(Z)-np.cos(X),
    -0.4*np.sin(X)-np.cos(Y),
],axis=-1)
rho=np.linalg.norm(u,axis=-1)
G=rho[...,None]*u
L=np.cross(omega,u)

mean=lambda f: np.mean(f)
uL2=math.sqrt(mean(np.sum(u*u,axis=-1)))
wL2=math.sqrt(mean(np.sum(omega*omega,axis=-1)))
Ghat=np.fft.fftn(G,axes=(0,1,2),norm='forward')
Lhat=np.fft.fftn(L,axes=(0,1,2),norm='forward')
freq=(np.fft.fftfreq(N)*N).astype(int)

def Qhat(Fhat):
    out=np.zeros_like(Fhat,dtype=np.complex128)
    for i,k1 in enumerate(freq):
        for j,k2 in enumerate(freq):
            for l,k3 in enumerate(freq):
                k=np.array([k1,k2,k3],dtype=float)
                k2n=float(k@k)
                if k2n==0:
                    continue
                v=Fhat[i,j,l]
                out[i,j,l]=k*(k@v)/k2n
    return out

QG=Qhat(Ghat)
QL=Qhat(Lhat)

for K in (1,2,3):
    Nk=mode_count(K)
    sG=0.0
    sL=0.0
    inner=0j
    for i,k1 in enumerate(freq):
        for j,k2 in enumerate(freq):
            for l,k3 in enumerate(freq):
                r2=k1*k1+k2*k2+k3*k3
                if 0 < r2 <= K*K:
                    sG += float(np.vdot(QG[i,j,l],QG[i,j,l]).real)
                    sL += float(np.vdot(QL[i,j,l],QL[i,j,l]).real)
                    inner += np.vdot(QL[i,j,l],QG[i,j,l])
    lowG=math.sqrt(sG)
    lowL=math.sqrt(sL)
    boundG=math.sqrt(Nk)*(uL2**2)
    boundL=math.sqrt(Nk)*wL2*uL2
    assert lowG <= boundG*(1+1e-11)
    assert lowL <= boundL*(1+1e-11)
    assert abs(inner) <= lowG*lowL*(1+1e-11)+1e-13

print('PASS R25 fixed-output pressure escape: mode-count + finite-field sanity checks')
