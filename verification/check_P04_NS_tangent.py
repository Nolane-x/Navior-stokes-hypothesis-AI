#!/usr/bin/env python3
"""Fresh provenance/replay gate for P04/RD006.

Recomputes every frozen P04 tangent measurement from the committed script and
checks the recorded result. This is a finite-dimensional numerical verification,
not a Navier-Stokes regularity or blow-up proof.
"""
import hashlib
import importlib.util
import json
import pathlib

ROOT=pathlib.Path(__file__).resolve().parent.parent
SCRIPT=ROOT/'experiments/run_P04_NS_tangent_Lamb_coherence.py'
RESULT=ROOT/'verification/P04_NS_tangent_Lamb_coherence_result.json'

def load_module(path):
    spec=importlib.util.spec_from_file_location('p04_replay',path)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load P04 module')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

result=json.loads(RESULT.read_text())
assert hashlib.sha256(SCRIPT.read_bytes()).hexdigest()==result['script_sha256']
assert result['verdict']=='H-nonrepel'
assert result['amplitudes']==[0.5,1.0,2.0,4.0,8.0]
assert result['resolutions']==[48,64]

p04=load_module(SCRIPT)
recorded={(int(r['N']),float(r['amplitude'])):r for r in result['rows']}
for N in (48,64):
    for a in (0.5,1.0,2.0,4.0,8.0):
        fresh=p04.measure(N,a); old=recorded[(N,a)]
        assert fresh['stable'] and fresh['sign']=='positive'
        for key in ('kappa0','u_L2','F_NS_L2','h0','mean_derivative','relative_spread'):
            assert abs(float(fresh[key])-float(old[key])) < 3e-10*(1+abs(float(old[key])))
        for x,y in zip(fresh['derivatives'],old['derivatives']):
            assert abs(float(x)-float(y)) < 3e-10*(1+abs(float(y)))

print('PASS P04 script provenance hash')
print('PASS P04 all 10 tangent measurements replayed')
print('PASS positive derivative at all five amplitudes on N=48 and N=64')
print('SCOPE: finite-dimensional tangent challenger only; NOT global regularity or blow-up.')
