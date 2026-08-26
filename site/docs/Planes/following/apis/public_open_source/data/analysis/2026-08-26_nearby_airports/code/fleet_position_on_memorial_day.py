import glob,gzip,json,os
def load(p):
    o=gzip.open if p.endswith('.gz') else open
    with o(p,'rt') as f: return json.load(f)
for tail in ['SU-BND','SU-BTT','SU-BTV','SU-BGM']:
    for f in sorted(glob.glob(f"{tail}/data/recovered/{tail}_2025-09-2[01]_airplanes-live_trace_full.json")):
        if '.meta.' in f: continue
        t=load(f); tr=t.get('trace') or []
        if not tr: continue
        lats=[p[1] for p in tr]; lons=[p[2] for p in tr]
        print(f"{tail} {os.path.basename(f).split('_')[1]}  n={len(tr):5d}  lat {min(lats):7.2f}..{max(lats):7.2f}  lon {min(lons):8.2f}..{max(lons):8.2f}")
