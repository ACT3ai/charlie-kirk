import os, re, json, glob, csv, collections, datetime, sys, yaml

PL="/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes"
SPK=os.path.join(PL,"following","speaking")
OUT="/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad"
FOREIGN=["SU-BGM","SU-BND","SU-BTT","SU-BTU","SU-BTV","T7-ELL"]
KIRK6=["N102DZ","N40JD","N560TW","N582MM","N872RA","N888KG"]
N1098L3=["N1098L","N2100L","N59906"]
FLEET=FOREIGN+KIRK6+N1098L3
CONTROLS=["CONTROL-RYANAIR","CONTROL-LUFTHANSA"]
SIDE={**{t:"following" for t in FOREIGN},**{t:"kirk" for t in KIRK6},**{t:"n1098l" for t in N1098L3},**{t:"control" for t in CONTROLS}}

pm=re.compile(r'^(?P<tail>.+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full\.miss\.json\.meta\.json$')
ph=re.compile(r'^(?P<tail>.+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full\.json(\.gz)?$')

state=collections.defaultdict(dict)
for tail in FLEET+CONTROLS:
    d=os.path.join(PL,tail,"data","recovered")
    if not os.path.isdir(d): continue
    for fn in os.listdir(d):
        if fn.endswith(".meta.json") and not fn.endswith(".miss.json.meta.json"): continue
        m=pm.match(fn)
        if m: state[(tail,m['date'])].setdefault(m['src'],'ASKED_AND_EMPTY'); continue
        m=ph.match(fn)
        if m: state[(tail,m['date'])][m['src']]='HELD'
day={k:('HELD' if 'HELD' in v.values() else 'ASKED_AND_EMPTY') for k,v in state.items()}

def rng(a,b):
    a=a if isinstance(a,datetime.date) else datetime.date.fromisoformat(str(a))
    b=b if isinstance(b,datetime.date) else datetime.date.fromisoformat(str(b))
    o=[]
    while a<=b: o.append(a.isoformat()); a+=datetime.timedelta(days=1)
    return o

needed=set(); ev_windows={}
no_window=[]
for y in sorted(glob.glob(os.path.join(SPK,"*.yaml"))):
    slug=os.path.basename(y)[:-5]; doc=yaml.safe_load(open(y))
    if 'search' not in doc: no_window.append(slug); continue
    s=doc['search']; w=rng(s['window_from'],s['window_to']); ev_windows[slug]=(w,s['tails_searched'])
    for t in s['tails_searched']:
        for d0 in w: needed.add((t,d0))

# ---------- CSV 1: per tail per year ----------
rows=[]
for tail in FLEET+CONTROLS:
    per=collections.defaultdict(collections.Counter)
    for (t,d0),st in day.items():
        if t==tail: per[d0[:4]]['disk_'+st]+=1
    for (t,d0) in needed:
        if t!=tail: continue
        per[d0[:4]]['win_'+day.get((t,d0),'NEVER_ASKED')]+=1
    for yr in sorted(per):
        c=per[yr]
        wn=c['win_HELD']+c['win_ASKED_AND_EMPTY']+c['win_NEVER_ASKED']
        rows.append(dict(scope="tail_year",tail=tail,side=SIDE[tail],year=yr,
            window_aircraft_days_needed=wn,window_HELD=c['win_HELD'],
            window_ASKED_AND_EMPTY=c['win_ASKED_AND_EMPTY'],window_NEVER_ASKED=c['win_NEVER_ASKED'],
            window_coverage_pct=round(100*c['win_HELD']/wn,1) if wn else '',
            window_queried_pct=round(100*(wn-c['win_NEVER_ASKED'])/wn,1) if wn else '',
            disk_HELD_any_date=c['disk_HELD'],disk_ASKED_AND_EMPTY_any_date=c['disk_ASKED_AND_EMPTY']))
cols=list(rows[0].keys())
with open(os.path.join(OUT,"gap_ledger.csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow(r)
    # totals by side
    for side in ["following","kirk","n1098l","control"]:
        agg=collections.Counter()
        for r in rows:
            if r['side']!=side: continue
            for k in ['window_aircraft_days_needed','window_HELD','window_ASKED_AND_EMPTY','window_NEVER_ASKED','disk_HELD_any_date','disk_ASKED_AND_EMPTY_any_date']: agg[k]+=r[k]
        n=agg['window_aircraft_days_needed']
        w.writerow(dict(scope="SIDE_TOTAL",tail="ALL",side=side,year="ALL",
            window_aircraft_days_needed=n,window_HELD=agg['window_HELD'],
            window_ASKED_AND_EMPTY=agg['window_ASKED_AND_EMPTY'],window_NEVER_ASKED=agg['window_NEVER_ASKED'],
            window_coverage_pct=round(100*agg['window_HELD']/n,1) if n else '',
            window_queried_pct=round(100*(n-agg['window_NEVER_ASKED'])/n,1) if n else '',
            disk_HELD_any_date=agg['disk_HELD_any_date'],disk_ASKED_AND_EMPTY_any_date=agg['disk_ASKED_AND_EMPTY_any_date']))
    agg=collections.Counter()
    for r in rows:
        if r['side']=='control': continue
        for k in ['window_aircraft_days_needed','window_HELD','window_ASKED_AND_EMPTY','window_NEVER_ASKED','disk_HELD_any_date','disk_ASKED_AND_EMPTY_any_date']: agg[k]+=r[k]
    n=agg['window_aircraft_days_needed']
    w.writerow(dict(scope="FLEET_TOTAL",tail="ALL",side="15_case_tails",year="ALL",
        window_aircraft_days_needed=n,window_HELD=agg['window_HELD'],
        window_ASKED_AND_EMPTY=agg['window_ASKED_AND_EMPTY'],window_NEVER_ASKED=agg['window_NEVER_ASKED'],
        window_coverage_pct=round(100*agg['window_HELD']/n,1),
        window_queried_pct=round(100*(n-agg['window_NEVER_ASKED'])/n,1),
        disk_HELD_any_date=agg['disk_HELD_any_date'],disk_ASKED_AND_EMPTY_any_date=agg['disk_ASKED_AND_EMPTY_any_date']))
print("gap_ledger.csv rows:",len(rows))

# ---------- CSV 2: per event ----------
summ={r['slug']:r for r in csv.DictReader(open(os.path.join(SPK,"_airports_near_summary.csv")))}
erows=[]
for slug in sorted(summ):
    s=summ[slug]
    if slug in ev_windows:
        w,tails=ev_windows[slug]
        c=collections.Counter(); cf=collections.Counter()
        for t in tails:
            for d0 in w:
                st=day.get((t,d0),'NEVER_ASKED'); c[st]+=1
                if t in FOREIGN: cf[st]+=1
        n=len(w)*len(tails); nf=len(w)*sum(1 for t in tails if t in FOREIGN)
        erows.append(dict(slug=slug,date=s['date_first'],who=s['who'],attendee_class=s['attendee_class'],
            city=s['city'],state=s['state'],window_from=w[0],window_to=w[-1],window_days=len(w),tails=len(tails),
            testable="YES" if not s['archive_control_verdict'].startswith('ARCHIVE RETENTION') else "NO_ARCHIVE_RETENTION_BOUNDARY",
            control_verdict=s['archive_control_verdict'][:34],
            aircraft_days_needed=n,HELD=c['HELD'],ASKED_AND_EMPTY=c['ASKED_AND_EMPTY'],NEVER_ASKED=c['NEVER_ASKED'],
            coverage_pct=round(100*c['HELD']/n,1),queried_pct=round(100*(n-c['NEVER_ASKED'])/n,1),
            following_needed=nf,following_HELD=cf['HELD'],following_ASKED_AND_EMPTY=cf['ASKED_AND_EMPTY'],
            following_NEVER_ASKED=cf['NEVER_ASKED'],
            following_coverage_pct=round(100*cf['HELD']/nf,1) if nf else '',
            yaml_agrees="YES" if (s['aircraft_days_needed'] and int(s['aircraft_days_needed'])==n and int(s['aircraft_days_held'])==c['HELD']) else "MISMATCH"))
    else:
        erows.append(dict(slug=slug,date=s['date_first'],who=s['who'],attendee_class=s['attendee_class'],
            city=s['city'],state=s['state'],window_from='',window_to='',window_days=0,tails=0,
            testable="NO_SEARCH_WINDOW_GEOCODE_FAILED",control_verdict='',
            aircraft_days_needed=0,HELD=0,ASKED_AND_EMPTY=0,NEVER_ASKED=0,coverage_pct=0.0,queried_pct=0.0,
            following_needed=0,following_HELD=0,following_ASKED_AND_EMPTY=0,following_NEVER_ASKED=0,
            following_coverage_pct='',yaml_agrees="N/A"))
with open(os.path.join(OUT,"gap_ledger_by_event.csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(erows[0].keys())); w.writeheader(); w.writerows(erows)
print("by_event rows:",len(erows),"mismatches:",sum(1 for r in erows if r['yaml_agrees']=='MISMATCH'))
print("no_window:",no_window)
tot=collections.Counter()
for r in erows:
    for k in ['aircraft_days_needed','HELD','ASKED_AND_EMPTY','NEVER_ASKED','following_needed','following_HELD','following_ASKED_AND_EMPTY','following_NEVER_ASKED']: tot[k]+=r[k]
print(dict(tot))
json.dump(dict(tot),open(os.path.join(OUT,"totals.json"),"w"),indent=1)
