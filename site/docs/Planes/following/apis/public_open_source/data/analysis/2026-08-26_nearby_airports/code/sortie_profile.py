import glob,gzip,json,math,os,datetime as dt
PVU=(40.2181,-111.7233)
def hav(a,b,c,d):
    R=6371.0;p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a);dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))
def load(p):
    o=gzip.open if p.endswith('.gz') else open
    with o(p,'rt') as f: return json.load(f)
base="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes"
for tail,d in [("SU-BND","2026-06-02"),("SU-BND","2026-06-04"),("SU-BND","2025-09-10"),("SU-BGM","2025-04-10"),("SU-BND","2025-09-05")]:
    fs=[f for f in sorted(glob.glob(f"{base}/{tail}/data/recovered/{tail}_{d}_airplanes-live_trace_full.json")) if '.meta.' not in f]
    if not fs: fs=[f for f in sorted(glob.glob(f"{base}/{tail}/data/recovered/{tail}_{d}_adsb-lol_trace_full.json")) if '.meta.' not in f]
    if not fs: continue
    t=load(fs[0]); tr=t.get('trace') or []
    t0=t.get('timestamp')
    print(f"\n===== {tail} {d}  ({len(tr)} pts)")
    # summarise into phases
    prev=None; phase=[]
    for p in tr:
        sec=p[0]; lat,lon=p[1],p[2]; alt=p[3]
        g = (alt=='ground')
        km=hav(PVU[0],PVU[1],lat,lon)
        st='GND' if g else 'AIR'
        if prev is None or prev[0]!=st:
            if prev: phase.append(prev)
            prev=[st,sec,sec,km,km,(0 if g else alt)]
        else:
            prev[2]=sec; prev[4]=max(prev[4],km)
            if not g and isinstance(alt,(int,float)): prev[5]=max(prev[5],alt)
    if prev: phase.append(prev)
    for ph in phase:
        st,s0,s1,k0,k1,ma=ph
        f0=dt.datetime.utcfromtimestamp(t0+s0).strftime('%H:%M:%S')
        f1=dt.datetime.utcfromtimestamp(t0+s1).strftime('%H:%M:%S')
        dur=(s1-s0)/60.0
        print(f"  {st} {f0}-{f1}Z  {dur:6.1f} min  dist_from_KPVU {k0:6.1f}->{k1:6.1f} km  max_alt {ma}")
