import csv, json, os, sys, gzip, glob, datetime as dt, collections
CODE='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source/code'
sys.path.insert(0, os.path.join(CODE,'lib'))
import geo, traces

FOLL='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following'
PLANES='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes'
REC=os.path.join(FOLL,'apis/public_open_source/data/recovery')
IDX=json.load(open(os.path.join(REC,'trace_visit_index.json')))
MISS=traces.build_miss_index()
OUT='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad'

# --- raw trace access ---------------------------------------------------
FILES=collections.defaultdict(list)   # (tail,date) -> [(source,path)]
for tail,date,src,path in traces.trace_files():
    FILES[(tail,date)].append((src,path))

_cache={}
def load(path):
    if path in _cache: return _cache[path]
    with open(path,'rb') as fh: raw=fh.read()
    if raw[:2]==b'\x1f\x8b': raw=gzip.decompress(raw)
    try:
        doc=json.loads(raw.decode('utf-8'))
    except Exception:
        _cache[path]=[]; return []
    pts=[]
    for p in doc.get('trace') or []:
        if len(p)<4: continue
        t,lat,lon,alt=p[0],p[1],p[2],p[3]
        if lat is None or lon is None: continue
        pts.append((t,lat,lon,alt))
    _cache[path]=pts
    return pts

def hhmm(day,secs):
    b=dt.datetime.strptime(day,'%Y-%m-%d').replace(tzinfo=dt.timezone.utc)
    return (b+dt.timedelta(seconds=float(secs))).strftime('%H:%M:%SZ')

def analyse(tail,day,claimed):
    """Return per-source detail for one aircraft-day against one claimed airport code."""
    a=geo.airport_by_code(claimed)
    res=[]
    for src,path in FILES.get((tail,day),[]):
        pts=load(path)
        if not pts: continue
        r={'source':src,'points':len(pts)}
        if a:
            elev=float(a.get('elevation_ft') or 0)
            best=None; bestg=None
            for t,lat,lon,alt in pts:
                d=geo.haversine_km(a['lat'],a['lon'],lat,lon)
                agl=None if alt=='ground' else (None if not isinstance(alt,(int,float)) else alt-elev)
                if best is None or d<best[0]: best=(d,t,alt,agl)
                if alt=='ground' and (bestg is None or d<bestg[0]): bestg=(d,t)
            r['closest_km']=round(best[0],2); r['closest_time']=hhmm(day,best[1])
            r['closest_alt']=best[2]; r['closest_agl']=(None if best[3] is None else round(best[3]))
            r['ground_within_3km']= bestg is not None and bestg[0]<=3.0
            r['ground_closest_km']=None if bestg is None else round(bestg[0],2)
        # whole-day span
        gset=[]
        for rr in IDX.get(tail,{}).get(day,[]):
            if rr['source']!=src: continue
            for g in rr.get('ground_visits',[]):
                gset.append(g['airport_code'])
        r['ground_airports']=sorted(set(x for x in gset if x))
        res.append(r)
    return res

def tails_of(s):
    s=(s or '').strip()
    if not s or s.upper()=='UNKNOWN': return []
    for sep in [' or ','; ',';',' / ','/',',']:
        if sep in s: return [x.strip().upper() for x in s.split(sep) if x.strip()]
    return [s.upper()]

def codes_of(s):
    s=(s or '').strip()
    if not s or s.upper()=='UNKNOWN': return []
    out=[]
    for sep in ['/',';',',',' or ']:
        if sep in s:
            out=[x.strip().upper() for x in s.split(sep) if x.strip()]; break
    if not out: out=[s.upper()]
    return [c for c in out if c and c!='UNKNOWN' and geo.airport_by_code(c)]

rows=list(csv.DictReader(open(os.path.join(FOLL,'overlaps.csv'))))
results=[]
for r in rows:
    oid=r['overlap_id']; date=r['date'].strip()
    tl=tails_of(r['foreign_tail']); cc=codes_of(r['airport_code'])
    rec={'overlap_id':oid,'date':date,'foreign_tail':r['foreign_tail'],'claimed_airport':r['airport_code'],
         'city':r['city'],'state':r['state'],'subject':r['subject'],'audit_verdict':r['audit_verdict'],
         'existing_adsb_verdict':r['adsb_verified_verdict'],'existing_km':r['adsb_closest_approach_km'],
         'existing_note':r['adsb_verified_note'],'overlap_page':r['overlap_page'],
         'sources':'','closest_km':'','closest_agl':'','ground_at_claimed':'','ground_airports_that_day':'','detail':''}
    if not tl:
        rec.update(my_verdict='NO_TAIL_CLAIMED',evidence='the claim names no aircraft registration'); results.append(rec); continue
    if not date or not date[:4].isdigit():
        rec.update(my_verdict='NO_DATE_CLAIMED',evidence='the claim names no date'); results.append(rec); continue
    have=[(t,s,p) for t in tl for (s,p) in FILES.get((t,date),[])]
    if not have:
        yr=int(date[:4])
        asked=sorted(set(s for t in tl for s in MISS.get(t,{}).get(date,[])))
        # adjacent-day asked
        adj_asked=[]
        for t in tl:
            for k in (-2,-1,1,2):
                d2=(dt.date.fromisoformat(date)+dt.timedelta(days=k)).isoformat()
                adj_asked+=MISS.get(t,{}).get(d2,[])
        adj_ground=[]
        for t in tl:
            for k in (-2,-1,1,2):
                d2=(dt.date.fromisoformat(date)+dt.timedelta(days=k)).isoformat()
                for rr in IDX.get(t,{}).get(d2,[]):
                    for g in rr.get('ground_visits',[]): adj_ground.append(f"{d2} {g['airport_code']}")
        if yr<=2022:
            v='NO_ARCHIVE_COVERAGE'; ev='2022 is an archive RETENTION BOUNDARY (control aircraft 0 of 56 hits, both archives) - this date cannot be tested at all'
        elif asked:
            v='NOT_HEARD'; ev='both free archives were ASKED for this exact date and hold nothing ('+','.join(asked)+'). Not evidence of absence.'
        elif adj_asked:
            v='NOT_HEARD'; ev='no trace for this date; adjacent days were asked and empty. Not evidence of absence.'
        else:
            v='NO_ARCHIVE_COVERAGE'; ev='no trace on disk and no recorded query for this tail on this date'
        if adj_ground: ev+='  | adjacent-day ground contact: '+', '.join(sorted(set(adj_ground)))
        rec.update(my_verdict=v,evidence=ev); results.append(rec); continue

    # we hold at least one trace
    per=[]
    for t in tl:
        for c in (cc or [None]):
            if c is None:
                for src,path in FILES.get((t,date),[]):
                    per.append((t,None,{'source':src,'points':len(load(path)),'ground_airports':sorted(set(g['airport_code'] for rr in IDX.get(t,{}).get(date,[]) if rr['source']==src for g in rr.get('ground_visits',[]) if g.get('airport_code')))}))
            else:
                for a in analyse(t,date,c): per.append((t,c,a))
    srcs=sorted(set(a['source'] for _,_,a in per))
    gall=sorted(set(x for _,_,a in per for x in a.get('ground_airports',[])))
    if not cc:
        rec.update(my_verdict='NO_AIRPORT_CLAIMED',sources=','.join(srcs),ground_airports_that_day=','.join(gall),
                   evidence='trace held but the claim names no resolvable airport; on-ground that day: '+(','.join(gall) or 'none'))
        results.append(rec); continue

    withk=[(t,c,a) for t,c,a in per if a.get('closest_km') is not None]
    best=min(withk,key=lambda x:x[2]['closest_km']) if withk else None
    ground_hit=any(a.get('ground_within_3km') for _,_,a in per)
    minkm=best[2]['closest_km'] if best else None
    agl=best[2]['closest_agl'] if best else None

    det=' ; '.join(f"{t} {a['source']}: closest {a.get('closest_km')}km to {c} at {a.get('closest_time')} "
                   f"(alt {a.get('closest_alt')}, AGL {a.get('closest_agl')}), on-ground that day: {','.join(a.get('ground_airports') or []) or 'none'}"
                   for t,c,a in per)
    if ground_hit:
        v='CONFIRMS_ON_GROUND_AT_CLAIMED_FIELD'
        ev=f'on-ground position within 3 km of {best[1]} on the claimed date'
    elif minkm is not None and minkm<=3 and agl is not None and agl<=1500:
        v='CONFIRMS_APPROACH_OR_DEPARTURE'
        ev=f'trace passes {minkm} km from {best[1]} at {agl} ft AGL - an arrival or departure at the claimed field, but the archive holds no on-ground point'
    elif minkm is not None and minkm<=15 and agl is not None and agl<=5000:
        v='CONSISTENT_LOW_OVER_CLAIMED_METRO'
        ev=f'closest {minkm} km from {best[1]} at {agl} ft AGL - low over the claimed metro, no landing recorded'
    elif minkm is not None and minkm<=80:
        v='NEARBY_NOT_AT_CLAIMED_FIELD'
        ev=f'closest {minkm} km from {best[1]} (alt {best[2]["closest_alt"]}); on-ground that day at {",".join(gall) or "none"}'
    elif minkm is not None:
        v='CONTRADICTS'
        ev=f'no position within {minkm:.0f} km of {best[1]} at any point on the claimed date; on-ground that day at {",".join(gall) or "none"}'
    else:
        v='INDETERMINATE'; ev='trace held but no comparable geometry'
    rec.update(my_verdict=v,evidence=ev,sources=','.join(srcs),closest_km=('' if minkm is None else minkm),
               closest_agl=('' if agl is None else agl),ground_at_claimed=('yes' if ground_hit else 'no'),
               ground_airports_that_day=','.join(gall),detail=det)
    results.append(rec)

# --- annotate: does the PUBLISHED note rest on a different date than the claim?
import re as _re
_src={r['overlap_id']:r for r in rows}
for r in results:
    n=_src[r['overlap_id']]['adsb_verified_note'] or ''
    m=_re.search(r'tracked (?:on )?(\d{4}-\d{2}-\d{2})',n)
    r['note_cites_date']=m.group(1) if m else ''
    r['note_uses_wrong_day']='YES' if (m and m.group(1)!=r['date']) else ''

hdr=['overlap_id','date','foreign_tail','claimed_airport','city','state','subject','audit_verdict',
     'existing_adsb_verdict','my_verdict','agrees','sources','closest_km','closest_agl',
     'ground_at_claimed','ground_airports_that_day','note_cites_date','note_uses_wrong_day','evidence','detail','existing_km','existing_note','overlap_page']
MAP={'CONFIRMS_ON_GROUND_AT_CLAIMED_FIELD':'AT_CLAIMED_AIRPORT','CONFIRMS_APPROACH_OR_DEPARTURE':'AT_CLAIMED_AIRPORT',
     'CONSISTENT_LOW_OVER_CLAIMED_METRO':'AT_CLAIMED_AIRPORT','NEARBY_NOT_AT_CLAIMED_FIELD':'ELSEWHERE',
     'CONTRADICTS':'ELSEWHERE','NOT_HEARD':'NOT_HEARD','NO_ARCHIVE_COVERAGE':'NO_ARCHIVE_COVERAGE',
     'NO_TAIL_CLAIMED':'NO_TAIL_CLAIMED','NO_DATE_CLAIMED':'NO_DATE_CLAIMED','NO_AIRPORT_CLAIMED':'ELSEWHERE',
     'INDETERMINATE':'ELSEWHERE'}
for r in results:
    r['agrees']='yes' if MAP.get(r['my_verdict'])==r['existing_adsb_verdict'] else 'NO'
with open(os.path.join(OUT,'claims_audit.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=hdr); w.writeheader()
    for r in results: w.writerow({k:r.get(k,'') for k in hdr})
json.dump(results,open(os.path.join(OUT,'claims_audit.json'),'w'),indent=1)
print(collections.Counter(r['my_verdict'] for r in results))
print('disagree',sum(1 for r in results if r['agrees']=='NO'))
for r in results:
    if r['agrees']=='NO':
        print(f"  {r['overlap_id']} {r['date']} {r['foreign_tail']} claim={r['claimed_airport']} | existing {r['existing_adsb_verdict']} -> {r['my_verdict']} | {r['evidence'][:160]}")
