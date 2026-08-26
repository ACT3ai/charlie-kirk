import glob,gzip,json,math,datetime as dt
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
days=[("SU-BND","2025-09-05"),("SU-BND","2025-09-06"),("SU-BND","2025-09-07"),("SU-BND","2025-09-08"),
      ("SU-BND","2025-09-09"),("SU-BND","2025-09-10"),("SU-BND","2025-09-12"),
      ("SU-BND","2026-05-13"),("SU-BND","2026-05-14"),("SU-BND","2026-05-20"),
      ("SU-BND","2026-06-02"),("SU-BND","2026-06-04"),("SU-BGM","2025-04-10")]
for tail,d in days:
    fs=[f for f in sorted(glob.glob(f"{base}/{tail}/data/recovered/{tail}_{d}_*trace_full.json*")) if '.meta.' not in f and '.miss.' not in f]
    if not fs:
        print(f"\n===== {tail} {d}: NO PAYLOAD ON DISK")
        continue
    for fp in fs:
        t=load(fp); tr=t.get('trace') or []; t0=t.get('timestamp')
        src=fp.split('_')[-3] if 'trace' in fp else '?'
        print(f"\n===== {tail} {d}  {fp.split('/')[-1]}  ({len(tr)} pts)")
        gnd=[(p[1],p[2]) for p in tr if p[3]=='ground']
        if gnd:
            la=[g[0] for g in gnd]; lo=[g[1] for g in gnd]
            print(f"   ground pts {len(gnd)} lat {min(la):.5f}..{max(la):.5f} lon {min(lo):.5f}..{max(lo):.5f}")
            # dwell cluster: most common rounded pos
            from collections import Counter
            c=Counter((round(g[0],4),round(g[1],4)) for g in gnd)
            print(f"   modal parking pos {c.most_common(3)}")
        prev=None; phase=[]
        for p in tr:
            sec=p[0]; lat,lon=p[1],p[2]; alt=p[3]
            g=(alt=='ground'); km=hav(PVU[0],PVU[1],lat,lon)
            st='GND' if g else 'AIR'
            if prev is None or prev[0]!=st:
                if prev: phase.append(prev)
                prev=[st,sec,sec,km,km,(0 if g else alt)]
            else:
                prev[2]=sec; prev[4]=max(prev[4],km)
                if not g and isinstance(alt,(int,float)): prev[5]=max(prev[5],alt)
        if prev: phase.append(prev)
        for st,s0,s1,k0,k1,ma in phase:
            f0=dt.datetime.utcfromtimestamp(t0+s0).strftime('%H:%M:%S')
            f1=dt.datetime.utcfromtimestamp(t0+s1).strftime('%H:%M:%S')
            print(f"   {st} {f0}-{f1}Z {(s1-s0)/60.0:6.1f}min  KPVU dist {k0:6.1f}->{k1:6.1f}km  maxalt {ma}")
