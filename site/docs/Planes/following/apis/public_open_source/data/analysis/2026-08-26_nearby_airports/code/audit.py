import csv, json, os, sys, datetime as dt
sys.path.insert(0, '/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/apis/public_open_source/code/lib')
import geo, traces

FOLL='/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following'
REC=os.path.join(FOLL,'apis/public_open_source/data/recovery')
IDX=json.load(open(os.path.join(REC,'trace_visit_index.json')))
MISS=traces.build_miss_index()

rows=list(csv.DictReader(open(os.path.join(FOLL,'overlaps.csv'))))

def tails(s):
    s=(s or '').strip()
    if not s or s.upper()=='UNKNOWN': return []
    for sep in [' or ','; ',';',' / ','/',',']:
        if sep in s: return [x.strip().upper() for x in s.split(sep) if x.strip()]
    return [s.upper()]

def codes(s):
    s=(s or '').strip()
    if not s or s.upper()=='UNKNOWN': return []
    out=[]
    for sep in ['/',';',',',' or ']:
        if sep in s:
            out=[x.strip().upper() for x in s.split(sep) if x.strip()]
            break
    if not out: out=[s.upper()]
    return [c for c in out if c and c!='UNKNOWN']

def ap(code):
    try: return geo.airport_by_code(code)
    except Exception: return None

def daylist(d,n=1):
    b=dt.date.fromisoformat(d)
    return [(b+dt.timedelta(days=k)).isoformat() for k in range(-n,n+1)]

out=[]
for r in rows:
    oid=r['overlap_id']; date=r['date'].strip(); tl=tails(r['foreign_tail']); cc=codes(r['airport_code'])
    rec={'overlap_id':oid,'date':date,'foreign_tail':r['foreign_tail'],'claimed_airport':r['airport_code'],
         'city':r['city'],'state':r['state'],'subject':r['subject'],
         'audit_verdict':r['audit_verdict'],'existing_adsb_verdict':r['adsb_verified_verdict'],
         'existing_note':r['adsb_verified_note'],'overlap_page':r['overlap_page']}
    if not tl:
        rec.update(my_verdict='NO_TAIL_CLAIMED',evidence='no aircraft registration in the claim',
                   trace_sources='',ground_airports='',km_to_claimed='')
        out.append(rec); continue
    if not date or not date[:4].isdigit():
        rec.update(my_verdict='NO_DATE_CLAIMED',evidence='no date in the claim',
                   trace_sources='',ground_airports='',km_to_claimed='')
        out.append(rec); continue

    # gather traces on the claimed day, per tail
    same=[]; adj=[]
    for t in tl:
        for rr in IDX.get(t,{}).get(date,[]):
            same.append((t,date,rr))
        for d2 in daylist(date):
            if d2==date: continue
            for rr in IDX.get(t,{}).get(d2,[]):
                adj.append((t,d2,rr))
    asked=[]
    for t in tl:
        for s in MISS.get(t,{}).get(date,[]): asked.append((t,date,s))

    if not same:
        yr=int(date[:4])
        if yr<=2022:
            v='NO_ARCHIVE_COVERAGE'
            ev='2022 is an archive retention boundary (control aircraft 0/56 hits) — untestable by construction'
        elif asked:
            v='NOT_HEARD'
            ev='archives ASKED on this date and held nothing: '+','.join(sorted(set(s for _,_,s in asked)))
        else:
            v='NO_ARCHIVE_COVERAGE'; ev='no trace and no recorded miss for this tail/date'
        # adjacent-day context
        adjtxt=''
        if adj:
            gv=[]
            for t,d2,rr in adj:
                for g in rr.get('ground_visits',[]):
                    gv.append(f"{d2}:{g.get('airport_code')}")
            adjtxt='; adjacent-day ground contact '+','.join(sorted(set(gv))) if gv else ''
        rec.update(my_verdict=v,evidence=ev+adjtxt,trace_sources='',ground_airports='',km_to_claimed='')
        out.append(rec); continue

    srcs=sorted(set(rr['source'] for _,_,rr in same))
    gvs=[]
    for t,d,rr in same:
        for g in rr.get('ground_visits',[]):
            gvs.append((rr['source'],g))
    gcodes=sorted(set(g.get('airport_code') for _,g in gvs if g.get('airport_code')))
    nf=[]
    for t,d,rr in same:
        for n in rr.get('near_field',[]): nf.append(n)

    # distances from claimed airport(s) to each ground visit
    dists=[]
    for c in cc:
        a=ap(c)
        if not a: continue
        for s,g in gvs:
            if g.get('lat') is None: continue
            dists.append((c,g.get('airport_code'),geo.haversine_km(a['lat'],a['lon'],g['lat'],g['lon'])))
    mind=min([d[2] for d in dists],default=None)

    if not gvs:
        # airborne only that day
        nfc=sorted(set(n['airport_code'] for n in nf))
        hit = any(c in nfc for c in cc)
        rec.update(my_verdict='AIRBORNE_ONLY_NO_LANDING',
                   evidence=('trace held ('+','.join(srcs)+f", {sum(rr.get('trace_points',0) or 0 for _,_,rr in same)} pts) but NO on-ground position anywhere; near-field low passes: "+','.join(nfc[:6])+('  [includes claimed field]' if hit else '')),
                   trace_sources=','.join(srcs),ground_airports='',km_to_claimed='')
        out.append(rec); continue

    if cc and any(c in gcodes for c in cc):
        v='CONFIRMS_AT_CLAIMED_AIRPORT'
        ev='on-ground position at the claimed field '+'/'.join([c for c in cc if c in gcodes])
    elif mind is not None and mind<=80:
        v='CONFIRMS_METRO_CORRECTS_AIRPORT'
        ev=f'on-ground at {"/".join(gcodes)}, {mind:.1f} km from the claimed field — same metro, different airport'
    elif mind is not None and mind>1000:
        v='CONTRADICTS'
        ev=f'on-ground at {"/".join(gcodes)}, {mind:.0f} km from the claimed field'
    elif mind is not None:
        v='CONTRADICTS_SAME_REGION'
        ev=f'on-ground at {"/".join(gcodes)}, {mind:.0f} km from the claimed field'
    else:
        v='ON_GROUND_ELSEWHERE_UNRESOLVED'
        ev='on-ground at '+'/'.join(gcodes)+' ; claimed field has no coordinates'
    rec.update(my_verdict=v,evidence=ev,trace_sources=','.join(srcs),
               ground_airports=','.join(gcodes),km_to_claimed=('' if mind is None else f'{mind:.1f}'))
    out.append(rec)

hdr=['overlap_id','date','foreign_tail','claimed_airport','city','state','subject',
     'audit_verdict','existing_adsb_verdict','my_verdict','agrees_with_existing',
     'trace_sources','ground_airports','km_to_claimed','evidence','existing_note','overlap_page']
MAP={'CONFIRMS_AT_CLAIMED_AIRPORT':'AT_CLAIMED_AIRPORT','CONFIRMS_METRO_CORRECTS_AIRPORT':'AT_CLAIMED_AIRPORT',
     'CONTRADICTS':'ELSEWHERE','CONTRADICTS_SAME_REGION':'ELSEWHERE','ON_GROUND_ELSEWHERE_UNRESOLVED':'ELSEWHERE',
     'AIRBORNE_ONLY_NO_LANDING':'ELSEWHERE','NOT_HEARD':'NOT_HEARD','NO_ARCHIVE_COVERAGE':'NO_ARCHIVE_COVERAGE',
     'NO_TAIL_CLAIMED':'NO_TAIL_CLAIMED','NO_DATE_CLAIMED':'NO_DATE_CLAIMED'}
for r in out:
    r['agrees_with_existing']='yes' if MAP.get(r['my_verdict'])==r['existing_adsb_verdict'] else 'NO'
p='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad/claims_audit.csv'
with open(p,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=hdr); w.writeheader()
    for r in out: w.writerow({k:r.get(k,'') for k in hdr})
import collections
print(collections.Counter(r['my_verdict'] for r in out))
print('disagreements:',sum(1 for r in out if r['agrees_with_existing']=='NO'))
for r in out:
    if r['agrees_with_existing']=='NO':
        print(' ',r['overlap_id'],r['date'],r['foreign_tail'],'claimed',r['claimed_airport'],'| existing',r['existing_adsb_verdict'],'-> mine',r['my_verdict'],'|',r['evidence'][:150])
