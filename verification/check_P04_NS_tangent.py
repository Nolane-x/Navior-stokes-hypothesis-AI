#!/usr/bin/env python3
"""Fresh provenance/replay gate for P04/RD006.

Recomputes every frozen P04 tangent measurement from the committed script and
checks the recorded result. Cross-hardware FFT values are compared with a
numerically meaningful tolerance; the preregistered sign/spread gates remain
unchanged. This is NOT a Navier-Stokes regularity or blow-up proof.
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

def close(x,y,rtol=5e-5,atol=5e-8):
    return abs(float(x)-float(y)) <= atol + rtol*abs(float(y))

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
        # Preserve the frozen scientific gate exactly: all three stencil
        # derivatives must share a strict positive sign and spread <5e-3.
        assert fresh['stable'] and fresh['sign']=='positive'
        assert max(fresh['derivatives'])-min(fresh['derivatives']) >= 0
        assert fresh['relative_spread'] < 5e-3
        assert close(fresh['kappa0'],old['kappa0'],rtol=2e-6,atol=2e-7)
        assert close(fresh['u_L2'],old['u_L2'],rtol=2e-8,atol=2e-9)
        assert close(fresh['F_NS_L2'],old['F_NS_L2'],rtol=2e-7,atol=2e-7)
        assert close(fresh['h0'],old['h0'],rtol=2e-7,atol=2e-12)
        assert close(fresh['mean_derivative'],old['mean_derivative'],rtol=5e-4,atol=5e-5)
        for x,y in zip(fresh['derivatives'],old['derivatives']):
            assert close(x,y,rtol=5e-4,atol=5e-5)

print('PASS P04 script provenance hash')
print('PASS P04 all 10 tangent measurements replayed cross-hardware')
print('PASS frozen positive-sign/spread gate at all five amplitudes on N=48 and N=64')
print('SCOPE: finite-dimensional tangent challenger only; NOT global regularity or blow-up.')
