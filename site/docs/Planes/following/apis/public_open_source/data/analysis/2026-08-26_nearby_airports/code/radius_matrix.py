import json, csv, math, datetime as dt, collections, os
SCR='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad'
ROOT='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk'
POS=ROOT+'/site/docs/Planes/following/apis/public_open_source'

FOREIGN=['SU-BGM','SU-BND','SU-BTT','SU-BTU','SU-BTV','T7-ELL']
KIRK=['N102DZ','N1098L','N2100L','N40JD','N560TW','N582MM','N59906','N872RA','N888KG']

def hav(a,b,c,d):
    R=3958.7613
    p1,p2=math.radians(a),math.radians(c)
    dp=p2-p1; dl=math.radians(d-b)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))

events_all=json.load(open(SCR+'/events.json'))
events=[e for e in events_all if e['lat'] is not None and e['lon'] is not None]
print('events total',len(events_all),'geocoded',len(events))
tvi=json.load(open(POS+'/data/recovery/trace_visit_index.json'))

# ourairports coords for near_field join
ap={}
with open(POS+'/data/ourairports/airports.csv') as f:
    for r in csv.DictReader(f):
        for k in (r['ident'],r['gps_code'],r['icao_code'],r['local_code'],r['iata_code']):
            if k and k not in ap:
                try: ap[k]=(float(r['latitude_deg']),float(r['longitude_deg']),r['type'])
                except: pass

# Flatten trace index -> per tail: list of (day, kind, code, lat, lon, time, alt)
GV=collections.defaultdict(list)   # tail -> list of dict
NF=collections.defaultdict(list)
DAYS_HELD=collections.defaultdict(set)   # tail -> set of days with a trace payload
for tail,days in tvi.items():
    for day,recs in days.items():
        DAYS_HELD[tail].add(day)
        for r in recs:
            src=r.get('source')
            for g in r.get('ground_visits',[]):
                GV[tail].append(dict(day=day,code=g['airport_code'],name=g.get('airport_name'),
                    lat=g['lat'],lon=g['lon'],t0=g.get('first_seen_utc'),t1=g.get('last_seen_utc'),
                    pts=g.get('ground_points'),src=src))
            for n in r.get('near_field',[]):
                c=n.get('airport_code')
                if c in ap:
                    NF[tail].append(dict(day=day,code=c,name=n.get('airport_name'),
                        lat=ap[c][0],lon=ap[c][1],alt=n.get('altitude_ft'),
                        t=n.get('time_utc'),dist_ap=n.get('distance_mi'),src=src))

RADII=[40,75,100,150]
WINDOWS=[2,3,5,7]

def daylist(ev,w):
    a=dt.date.fromisoformat(ev['first'])-dt.timedelta(days=w)
    b=dt.date.fromisoformat(ev['last'])+dt.timedelta(days=w)
    d=a; out=[]
    while d<=b: out.append(d.isoformat()); d+=dt.timedelta(days=1)
    return out

# ---------- MATRIX ----------
rows=[]
detail=collections.defaultdict(dict)   # (fleet) -> {(r,w): set of (slug,tail)}
pairsets={}
for fleet,tails in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    for R in RADII:
        for W in WINDOWS:
            gpairs=set(); npairs=set(); cov_cells=0; held_cells=0
            for ev in events:
                dl=set(daylist(ev,W))
                for t in tails:
                    cov_cells+=len(dl)
                    held_cells+=len(dl & DAYS_HELD[t])
                    for g in GV[t]:
                        if g['day'] in dl and hav(ev['lat'],ev['lon'],g['lat'],g['lon'])<=R:
                            gpairs.add((ev['slug'],t)); break
                    for n in NF[t]:
                        if n['day'] in dl and hav(ev['lat'],ev['lon'],n['lat'],n['lon'])<=R:
                            npairs.add((ev['slug'],t)); break
            pairsets[(fleet,R,W)]=(gpairs,npairs)
            rows.append(dict(fleet=fleet,radius_mi=R,window_days=W,
                n_tails=len(tails), n_events=len(events),
                possible_pairs=len(events)*len(tails),
                ground_pairs=len(gpairs), ground_events=len({p[0] for p in gpairs}),
                nearfield_pairs=len(npairs), nearfield_events=len({p[0] for p in npairs}),
                either_pairs=len(gpairs|npairs),
                aircraft_days_in_window=cov_cells, aircraft_days_with_trace=held_cells,
                coverage_pct=round(100*held_cells/cov_cells,2) if cov_cells else 0)) 

with open(SCR+'/radius_window_matrix.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---------- BLIND SPOT PAIRS ----------
bs=[]
for fleet,tails in (('FOREIGN',FOREIGN),('KIRK',KIRK)):
    base_g,base_n=pairsets[(fleet,40,2)]
    for R in RADII:
        for W in WINDOWS:
            if (R,W)==(40,2): continue
            g,n=pairsets[(fleet,R,W)]
            for kind,cur,base in (('GROUND',g,base_g),('NEARFIELD_LOWPASS',n,base_n)):
                for slug,t in sorted(cur-base):
                    ev=[e for e in events if e['slug']==slug][0]
                    dl=set(daylist(ev,W))
                    src=GV[t] if kind=='GROUND' else NF[t]
                    hits=[]
                    for x in src:
                        if x['day'] in dl:
                            dd=hav(ev['lat'],ev['lon'],x['lat'],x['lon'])
                            if dd<=R: hits.append((dd,x))
                    hits.sort(key=lambda z:z[0])
                    dd,x=hits[0]
                    off=(dt.date.fromisoformat(x['day'])-dt.date.fromisoformat(ev['first'])).days
                    bs.append(dict(fleet=fleet,kind=kind,first_seen_at_radius=R,first_seen_at_window=W,
                        driver=('WINDOW_ONLY' if R==40 else ('RADIUS_ONLY' if W==2 else 'RADIUS_AND_WINDOW')),
                        slug=slug,tail=t,event_date=ev['first'],event_city=ev['city'],
                        event_state=ev['state'],attendee_class=ev['attendee_class'],
                        charlie_present=ev['charlie_present'],erika_present=ev['erika_present'],
                        event_arrival_airport=ev['arrival_airport'],
                        plane_day=x['day'], day_offset_from_event=off,
                        plane_airport=x['code'], plane_airport_name=x.get('name'),
                        dist_event_to_plane_airport_mi=round(dd,1),
                        altitude_ft=x.get('alt',''), ground_points=x.get('pts',''),
                        first_seen_utc=x.get('t0',x.get('t','')), last_seen_utc=x.get('t1',''),
                        source=x['src'], n_hits_in_window=len(hits)))
# dedupe: keep smallest (radius,window) at which the pair first appears, per kind
best={}
for r in bs:
    k=(r['fleet'],r['kind'],r['slug'],r['tail'])
    cur=best.get(k)
    if cur is None or (r['first_seen_at_radius'],r['first_seen_at_window'])<(cur['first_seen_at_radius'],cur['first_seen_at_window']):
        best[k]=r
bs=sorted(best.values(),key=lambda r:(r['fleet'],r['kind'],r['first_seen_at_radius'],r['event_date'],r['tail']))
with open(SCR+'/blind_spot_pairs.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(bs[0].keys())); w.writeheader(); w.writerows(bs)

print("matrix rows",len(rows),"blindspot rows",len(bs))
# quick console summary
for fleet in ('FOREIGN','KIRK'):
    print('---',fleet)
    for R in RADII:
        print(' R=%3d '%R + ' '.join('W%d g=%2d n=%2d'%(W,len(pairsets[(fleet,R,W)][0]),len(pairsets[(fleet,R,W)][1])) for W in WINDOWS))
