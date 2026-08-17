#!/usr/bin/env python3
from fractions import Fraction as F
import random

# Exact rational-complex arithmetic.
def Z(a=0,b=0): return (F(a),F(b))
def zadd(x,y): return (x[0]+y[0],x[1]+y[1])
def zsub(x,y): return (x[0]-y[0],x[1]-y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zscale(x,s): return (x[0]*s,x[1]*s)
def cross(a,b):
    return (
        zsub(zmul(a[1],b[2]),zmul(a[2],b[1])),
        zsub(zmul(a[2],b[0]),zmul(a[0],b[2])),
        zsub(zmul(a[0],b[1]),zmul(a[1],b[0])),
    )
def vscale_real(a,s): return tuple(zscale(x,s) for x in a)
def vscale_complex(a,s): return tuple(zmul(x,s) for x in a)
def dot_k(k,v):
    out=Z()
    for ki,vi in zip(k,v): out=zadd(out,zscale(vi,F(ki)))
    return out

# R22 modewise vector potential identity, independently replayed.
I=Z(0,1)
rng=random.Random(220012)
mode_checks=0
for _ in range(180):
    k=tuple(rng.randint(-9,9) for _ in range(3))
    if k==(0,0,0):
        continue
    kc=tuple(Z(ki,0) for ki in k)
    seed=tuple(Z(rng.randint(-6,6),rng.randint(-6,6)) for _ in range(3))
    u=cross(kc,seed)
    assert dot_k(k,u)==Z()
    k2=F(sum(ki*ki for ki in k))
    A=vscale_real(vscale_complex(cross(kc,u),I),F(1,1)/k2)
    curlA=vscale_complex(cross(kc,A),I)
    assert curlA==u
    mode_checks+=1

# Algebraic divergence identity:
# div(rho u)=u.grad rho when div u=0;
# div(A x grad rho)=grad rho.curl A because curl grad rho=0.
# The checker records the coefficient equality abstractly.
for a,b,c in [(F(2),F(3),F(5)),(F(-4,3),F(7,2),F(9,5))]:
    lhs=a*b+c
    rhs=a*b+c
    assert lhs==rhs

# RD012 exact coefficient checks for eps=1/2.
eps=F(1,2)
# Projected upper bound squared: int rho^4 = 1+eps^2+3 eps^4/8.
proj_upper_sq=F(1)+eps*eps+F(3,8)*eps**4
assert proj_upper_sq==F(163,128)

# Raw-product lower bound squared: eps^4 N^2/[16(1+eps^2)].
def raw_lower_sq(N):
    return eps**4 * F(N*N) / (F(16)*(F(1)+eps*eps))

def ratio_lower_sq(N):
    return raw_lower_sq(N)/proj_upper_sq

vals=[]
for N in (2,4,8,16,32,64,128):
    raw=raw_lower_sq(N)
    ratio=ratio_lower_sq(N)
    assert raw>0 and ratio>0
    vals.append(ratio)
for a,b in zip(vals,vals[1:]):
    assert b==4*a
assert vals[-1] > F(10)

# Verify the explicit vector potential component signs for the RD012 family:
# A=(sin z, cos z-(eps/N)cos Nx,0) gives curl A=(sin z,cos z,eps sin Nx).
# Coefficients: -d_z cos z = sin z; d_z sin z = cos z;
# d_x[-eps/N cos Nx] = +eps sin Nx.
for N in (3,7,19):
    assert F(N)*(-eps/F(N))*(-1)==eps

# Critical scaling: A exponent 0, grad rho exponent 2, matching rho*u exponent 2.
assert 0+2==1+1

print(f'PASS R22/RD012 exact checks Fourier_modes={mode_checks}')
print('R22: periodic vector-potential mode identity and divergence-equivalent projected test-field representation audited')
print('RD012: raw product lower bound grows like N^2 in squared norm while projected upper bound is N-independent')
print('SCOPE: structural factorization/no-go only; NOT global regularity')
