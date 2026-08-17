#!/usr/bin/env python3
"""Fresh replay checks for R02-R04 and P01/P02 winning states.

This verifier re-evaluates committed winner coefficients at N=64. It does not
rerun the optimizers and does not certify Navier-Stokes global regularity.
"""
import importlib.util, json, math, pathlib
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parent.parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

p01=load('p01',ROOT/'experiments/run_P01_helmholtz_coherence.py')
p02=load('p02',ROOT/'experiments/run_P02_lamb_coherence.py')
r1=json.loads((ROOT/'verification/P01_Helmholtz_coherence_result.json').read_text())
r2=json.loads((ROOT/'verification/P02_Lamb_coherence_result.json').read_text())

for module,result,key in [(p01,r1,'QN_L2'),(p02,r2,'QLamb_L2')]:
    c=np.array(result['winner_coefficients'],dtype=float)
    k,d=module.eval_kappa(c,64,None,True)
    target=result['confirmation'][-1]
    assert abs(k-target['kappa'])<2e-10
    assert abs(d['W3']-target['W3'])<2e-10
    assert abs(d[key]-target[key])<2e-10
    assert abs(d['QG_L2']-target['QG_L2'])<2e-10

# R03: the transport-pressure and Lamb/Bernoulli representations converge to
# the same W3. The tiny tolerance covers pseudospectral sampling of |u|.
c=np.array(r2['winner_coefficients'],dtype=float)
_,d_transport=p01.eval_kappa(c,64,None,True)
_,d_lamb=p02.eval_kappa(c,64,None,True)
assert abs(d_transport['W3']-d_lamb['W3'])<2e-7

# R04 abstract half-bound: exact sharp example.
x=np.array([1.0,1.0])/math.sqrt(2.0)
y=np.array([1.0,-1.0])/math.sqrt(2.0)
Qx=np.array([x[0],0.0]); Qy=np.array([y[0],0.0])
assert abs(np.dot(x,y))<1e-15
assert abs(abs(np.dot(Qx,Qy))-0.5)<1e-15

# Random orthogonal/projector stress checks.
rng=np.random.default_rng(404)
for n in (3,5,11):
    for _ in range(300):
        x=rng.normal(size=n); x/=np.linalg.norm(x)
        y=rng.normal(size=n); y-=x*np.dot(x,y)
        if np.linalg.norm(y)<1e-12:
            continue
        y/=np.linalg.norm(y)
        M=rng.normal(size=(n,n)); U,_,_=np.linalg.svd(M,full_matrices=False)
        rank=int(rng.integers(1,n))
        Q=U[:,:rank]@U[:,:rank].T
        w=abs(np.dot(Q@x,Q@y))
        assert w<=0.5+2e-12

print('PASS P01 winner replay N=64')
print('PASS P02 winner replay N=64')
print('PASS R03 transport/Lamb pressure-work agreement at confirmation resolution')
print('PASS R04 sharp 1/2 projector bound stress checks')
print('SCOPE: structural reductions and finite challengers only; NOT global regularity.')
