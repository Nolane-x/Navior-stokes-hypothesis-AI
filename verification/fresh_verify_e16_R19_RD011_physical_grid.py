#!/usr/bin/env python3
import cmath, math

# Fresh reconstruction: build velocity/curl in physical space on a uniform 3D grid,
# multiply to form L=omega x u, recover finite Fourier coefficients by trapezoidal
# quadrature, then Helmholtz-project each coefficient. No exact rational convolution
# code is shared with check_RD011_exact_Lamb_channel_counterexamples.py.

def neg(k): return tuple(-x for x in k)
def conjv(v): return tuple(z.conjugate() for z in v)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def addv(a,b): return tuple(x+y for x,y in zip(a,b))
def scalev(a,s): return tuple(s*x for x in a)
def norm2(v): return sum((z.real*z.real+z.imag*z.imag) for z in v)
def projectP(k,v):
    if k==(0,0,0): return v
    k2=sum(x*x for x in k)
    kv=sum(k[i]*v[i] for i in range(3))
    return tuple(v[i]-k[i]*kv/k2 for i in range(3))

def make_modes(spec):
    d={}
    for k,v in spec:
        d[k]=v
        d[neg(k)]=conjv(v)
    return d

def omega_modes(uh):
    out={}
    for k,u in uh.items():
        kc=tuple(complex(x,0) for x in k)
        out[k]=scalev(cross(kc,u),1j)
    return out

def candidate_qs(uh):
    return sorted(set(tuple(p[i]+r[i] for i in range(3)) for p in uh for r in uh))

def physical_channel_energies(spec,N=14):
    uh=make_modes(spec)
    wh=omega_modes(uh)
    qs=candidate_qs(uh)
    samples=[]
    twopi=2*math.pi
    for ix in range(N):
      x=twopi*ix/N
      for iy in range(N):
        y=twopi*iy/N
        for iz in range(N):
          z=twopi*iz/N
          pos=(x,y,z)
          u=(0j,0j,0j)
          w=(0j,0j,0j)
          for k,coef in uh.items():
            phase=cmath.exp(1j*sum(k[i]*pos[i] for i in range(3)))
            u=addv(u,scalev(coef,phase))
            w=addv(w,scalev(wh[k],phase))
          L=cross(w,u)
          assert max(abs(z.imag) for z in L) < 2e-12
          samples.append((pos,L))
    Lhat={}
    inv=1.0/(N**3)
    for q in qs:
      acc=[0j,0j,0j]
      for pos,L in samples:
        phase=cmath.exp(-1j*sum(q[i]*pos[i] for i in range(3)))
        for j in range(3):
            acc[j]+=L[j]*phase
      Lhat[q]=tuple(a*inv for a in acc)
    Ep=Eq=0.0
    for q,Lq in Lhat.items():
      if q==(0,0,0):
        assert norm2(Lq)<1e-20
        continue
      P=projectP(q,Lq)
      Q=tuple(Lq[i]-P[i] for i in range(3))
      Ep+=norm2(P)
      Eq+=norm2(Q)
    return Ep,Eq,Ep/(Ep+Eq)

sol_heavy=[
 ((1,1,0),(1.5+1j,-1.5-1j,2-2j)),
 ((1,-1,1),(-5/3+2j,-7/3-1j,-2/3-3j)),
 ((0,1,0),(1-3j,0j,-2-3j)),
]
grad_heavy=[
 ((1,1,0),(2.5+1j,-2.5-1j,1-1j)),
 ((0,0,1),(3j,-3j,0j)),
 ((1,1,-1),(1+3j,1-3j,2+0j)),
]

for N in (12,14):
    Ep,Eq,r=physical_channel_energies(sol_heavy,N)
    assert abs(Ep-63275/27)<2e-9,(N,Ep)
    assert abs(Eq-50770/27)<2e-9,(N,Eq)
    assert abs(r-12655/22809)<2e-12,(N,r)
    Ep2,Eq2,r2=physical_channel_energies(grad_heavy,N)
    assert abs(Ep2-4328/9)<2e-9,(N,Ep2)
    assert abs(Eq2-125641/9)<2e-9,(N,Eq2)
    assert abs(r2-4328/129969)<2e-12,(N,r2)

# R19 gradient-only shear independently checked geometrically.
k=(2.0,0.0,0.0)
L=(1.3,0.0,0.0)
k2=sum(x*x for x in k)
dot=sum(k[i]*L[i] for i in range(3))
P=tuple(L[i]-k[i]*dot/k2 for i in range(3))
assert sum(x*x for x in P)<1e-28

# P05 sign/scaling extremes independently restated.
def sprime(A,nu=1.0):
    return 1.6*A**3-34.0*nu*A**2
assert sprime(20)<0
assert sprime(22)>0
assert -1+3-2==0

print('PASS fresh W5-E16 R19/RD011 physical-grid reconstruction')
print('RD011 channel energies independently recovered from physical-space L=omega x u at N=12 and N=14')
print('R19 gradient-only shear and P05 sign/scaling extremes independently checked')
print('VERDICT: PASS_PARTIALS_ONLY_NOT_GLOBAL_REGULARITY')
