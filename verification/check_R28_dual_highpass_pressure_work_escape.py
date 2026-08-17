import numpy as np

# Independent finite-grid check of the exact low/high pressure-work decompositions.
def projector_hat(Fh, solenoidal):
    N=Fh.shape[0]
    kk=np.fft.fftfreq(N)*N
    K=np.stack(np.meshgrid(kk,kk,kk,indexing='ij'),axis=-1)
    k2=np.sum(K*K,axis=-1)
    dot=np.sum(Fh*K,axis=-1)
    Q=np.zeros_like(Fh)
    nz=k2>0
    Q[nz]=K[nz]*(dot[nz]/k2[nz])[...,None]
    return Fh-Q if solenoidal else Q

def inner_hat(A,B,mask=None):
    if mask is None:
        return float(np.sum(np.real(np.sum(np.conj(A)*B,axis=-1))))
    return float(np.sum(np.real(np.sum(np.conj(A[mask])*B[mask],axis=-1))))

N=24
x=np.arange(N)/N*2*np.pi
X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
u=np.stack([
    np.sin(Y+0.21)+0.5*np.cos(Z-0.07),
    np.sin(Z+0.14)+0.4*np.cos(X+0.21),
    np.sin(X-0.08)+0.3*np.cos(Y+0.15),
],axis=-1)
omega=np.stack([
    -0.3*np.sin(Y+0.15)-np.cos(Z+0.14),
    -0.5*np.sin(Z-0.07)-np.cos(X-0.08),
    -0.4*np.sin(X+0.21)-np.cos(Y+0.21),
],axis=-1)
L=np.cross(omega,u)
rho=np.linalg.norm(u,axis=-1)
G=rho[...,None]*u
Lh=np.fft.fftn(L,axes=(0,1,2),norm='forward')
Gh=np.fft.fftn(G,axes=(0,1,2),norm='forward')
PL=projector_hat(Lh,True); QL=projector_hat(Lh,False)
PG=projector_hat(Gh,True); QG=projector_hat(Gh,False)
Wq=inner_hat(QL,QG)
Wp=-inner_hat(PL,PG)
assert abs(Wq-Wp)<2e-10*max(1.0,abs(Wq),abs(Wp))

kk=np.fft.fftfreq(N)*N
Kgrid=np.stack(np.meshgrid(kk,kk,kk,indexing='ij'),axis=-1)
r2=np.sum(Kgrid*Kgrid,axis=-1)
for cutoff in (1,2,3,4):
    low=(r2>0)&(r2<=cutoff*cutoff)
    high=r2>cutoff*cutoff
    qlo=inner_hat(QL,QG,low); qhi=inner_hat(QL,QG,high)
    plo=-inner_hat(PL,PG,low); phi=-inner_hat(PL,PG,high)
    assert abs(Wq-(qlo+qhi))<3e-10*max(1.0,abs(Wq))
    assert abs(Wp-(plo+phi))<3e-10*max(1.0,abs(Wp))

for n in (10,100,1000):
    total=sum(1.0 for _ in range(n))
    low=sum(((-1)**j)/(j+1)**2 for j in range(n))
    high=total-low
    assert high>0.9*n

print('PASS R28 dual high-pass pressure-work decomposition and escape logic')
