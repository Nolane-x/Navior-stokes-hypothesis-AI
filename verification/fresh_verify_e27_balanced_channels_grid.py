import numpy as np

# Fresh numerical reconstruction of R27's load-bearing identities.
# This intentionally does not import any project checker or theorem code.

def projector(F, solenoidal=True):
    N=F.shape[0]
    Fh=np.fft.fftn(F,axes=(0,1,2),norm='forward')
    kk=np.fft.fftfreq(N)*N
    K=np.stack(np.meshgrid(kk,kk,kk,indexing='ij'),axis=-1)
    k2=np.sum(K*K,axis=-1)
    dot=np.sum(Fh*K,axis=-1)
    Qh=np.zeros_like(Fh)
    nz=k2>0
    Qh[nz]=K[nz]*(dot[nz]/k2[nz])[...,None]
    H=Fh-Qh if solenoidal else Qh
    return np.fft.ifftn(H,axes=(0,1,2),norm='forward').real

def deriv(F,axis):
    N=F.shape[0]
    Fh=np.fft.fftn(F,axes=(0,1,2),norm='forward')
    kk=np.fft.fftfreq(N)*N
    shape=[1,1,1,1]
    shape[axis]=N
    mult=(1j*kk).reshape(shape)
    return np.fft.ifftn(Fh*mult,axes=(0,1,2),norm='forward').real

def mean_inner(A,B):
    return float(np.mean(np.sum(A*B,axis=-1)))

def check_case(N,phase,scale):
    x=np.arange(N)/N*2*np.pi
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    u=scale*np.stack([
        np.sin(Y+phase)+0.5*np.cos(Z-0.3*phase),
        np.sin(Z+0.2*phase)+0.4*np.cos(X+phase),
        np.sin(X-0.4*phase)+0.3*np.cos(Y+0.7*phase),
    ],axis=-1)
    du=np.empty((3,N,N,N,3))
    for j in range(3):
        du[j]=deriv(u,j)
    divu=du[0,...,0]+du[1,...,1]+du[2,...,2]
    assert np.max(np.abs(divu)) < 3e-11

    omega=np.stack([
        du[1,...,2]-du[2,...,1],
        du[2,...,0]-du[0,...,2],
        du[0,...,1]-du[1,...,0],
    ],axis=-1)
    L=np.cross(omega,u)
    rho=np.linalg.norm(u,axis=-1)
    assert float(np.min(rho)) > 1e-3
    G=rho[...,None]*u

    PL=projector(L,True); QL=projector(L,False)
    PG=projector(G,True); QG=projector(G,False)

    meanL=np.mean(L,axis=(0,1,2))
    assert np.linalg.norm(meanL) < 2e-11
    wq=mean_inner(QL,QG)
    wp=-mean_inner(PL,PG)
    assert abs(wq-wp) < 2e-9*max(1.0,abs(wq),abs(wp))
    assert abs(mean_inner(L,G)) < 2e-10*max(1.0,abs(wq),abs(wp))

    drho=np.stack([deriv(rho[...,None],j)[...,0] for j in range(3)],axis=-1)
    de=np.empty((3,N,N,N,3))
    e=u/rho[...,None]
    for j in range(3):
        de[j]=deriv(e,j)
    dG=np.empty((3,N,N,N,3))
    for j in range(3):
        dG[j]=deriv(G,j)

    gradG2=sum(np.sum(dG[j]*dG[j],axis=-1) for j in range(3))
    gradrho2=np.sum(drho*drho,axis=-1)
    grade2=sum(np.sum(de[j]*de[j],axis=-1) for j in range(3))
    D3_density=2*rho*gradrho2+rho**3*grade2
    lhs_density=gradG2/rho
    ratio=float(np.mean(lhs_density)/np.mean(D3_density))
    assert ratio <= 2.01

    Fnorm=np.sqrt(gradG2)
    norm65=float(np.mean(Fnorm**(6/5))**(5/6))
    weighted=float(np.mean(gradG2/rho)**0.5)
    U=float(np.mean(rho**1.5)**(2/3))
    rhs=weighted*np.sqrt(U)
    assert norm65 <= rhs*(1+2e-6)

    L2=mean_inner(L,L)
    split=mean_inner(PL,PL)+mean_inner(QL,QL)
    assert abs(L2-split) < 2e-9*max(1.0,L2)
    return {
        'N':N,'phase':phase,'scale':scale,'meanL':float(np.linalg.norm(meanL)),
        'pairing_error':float(abs(wq-wp)),'density_ratio':ratio,
        'holder_ratio':float(norm65/rhs),'channel_fraction':float(mean_inner(PL,PL)/L2)
    }

results=[]
for N in (18,22):
    for phase,scale in ((0.13,0.8),(0.71,1.0),(1.21,1.4)):
        results.append(check_case(N,phase,scale))
for r in results:
    print(r)
print(f'PASS fresh R27 physical-grid reconstruction: {len(results)} worlds')
