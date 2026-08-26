import sys, os, glob, gzip, json, math
sys.path.insert(0, "/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source/code/lib")
PVU=(40.2181,-111.7233)
def hav(a,b,c,d):
    R=6371.0
    p1,p2=math.radians(a),math.radians(c)
    dp=math.radians(c-a); dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))
def load(p):
    o=gzip.open if p.endswith('.gz') else open
    with o(p,'rt') as f: return json.load(f)
base="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes"
days=["2025-09-04","2025-09-05","2025-09-06","2025-09-07","2025-09-08","2025-09-09","2025-09-10","2025-09-11","2025-09-12","2025-09-13",
      "2026-05-13","2026-05-14","2026-05-20","2026-06-02","2026-06-04",
      "2024-04-19","2025-05-23","2025-04-10"]
print(f"{'tail':8} {'date':12} {'src':18} {'pts':>6} {'maxkm_fromPVU':>14} {'maxalt':>8} {'grd_pts':>7}  verdict")
for tail in ["SU-BND","SU-BGM","SU-BTT"]:
    for d in days:
        for f in sorted(glob.glob(f"{base}/{tail}/data/recovered/{tail}_{d}_*_trace_full.json")):
            if '.meta.' in f: continue
            try: t=load(f)
            except Exception as e: continue
            tr=t.get('trace') or []
            if not tr: continue
            src=os.path.basename(f).split('_')[2]
            mx=0.0; mxalt=0; g=0
            for p in tr:
                lat,lon=p[1],p[2]
                km=hav(PVU[0],PVU[1],lat,lon)
                mx=max(mx,km)
                a=p[3]
                if a=='ground': g+=1
                elif isinstance(a,(int,float)): mxalt=max(mxalt,a)
            v = "CLOSED-LOOP (never left Wasatch Front)" if mx<120 else ("REGIONAL" if mx<800 else "DEPARTED REGION")
            print(f"{tail:8} {d:12} {src:18} {len(tr):6} {mx:14.1f} {mxalt:8} {g:7}  {v}")
