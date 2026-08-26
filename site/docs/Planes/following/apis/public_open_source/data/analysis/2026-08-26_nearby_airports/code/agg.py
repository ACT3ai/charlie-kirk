import csv, json, statistics as st
from collections import defaultdict
SCR='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad'
rows=list(csv.DictReader(open(SCR+'/temporal_series.csv')))
cov=json.load(open(SCR+'/_coverage_days.json'))
FOREIGN=list(cov['held'].keys())
held=defaultdict(int); asked=defaultdict(int)
for t in FOREIGN:
    for d in cov['held'][t]: held[d[:4]]+=1
    for d in cov['asked'][t]: asked[d[:4]]+=1

def F(v):
    try: return float(v)
    except: return None

print("TABLE A - foreign-fleet North American ground-visit DAYS, normalised by held aircraft-days")
print(f"{'year':5}{'asked':>7}{'held':>6}{'cov%':>7}{'visitDays':>10}{'per100held':>11}{'nearEvDays':>11}{'nearPer100':>11}{'sameAirDays':>12}{'nearbyDays':>11}")
byy=defaultdict(list)
for r in rows: byy[r['year']].append(r)
for y in sorted(byy):
    rs=byy[y]
    vd={(r['tail'],r['day']) for r in rs}
    near={(r['tail'],r['day']) for r in rs if F(r['w2_mi']) is not None and F(r['w2_mi'])<=100}
    same={(r['tail'],r['day']) for r in rs if r['match_class']=='SAME_AIRPORT'}
    nb={(r['tail'],r['day']) for r in rs if r['match_class']=='NEARBY_AIRPORT'}
    h=held[y]; a=asked[y]
    print(f"{y:5}{a:7d}{h:6d}{(100*h/a if a else 0):7.1f}{len(vd):10d}"
          f"{(100*len(vd)/h if h else float('nan')):11.1f}{len(near):11d}"
          f"{(100*len(near)/h if h else float('nan')):11.2f}{len(same):12d}{len(nb):11d}")

print()
print("TABLE B - distance from foreign-fleet visit to NEAREST North American Kirk/TPUSA event within +-2 days")
print(f"{'year':5}{'n(rec)':>7}{'median_mi':>11}{'mean_mi':>10}{'min_mi':>9}{'<=40mi':>8}{'40-100':>8}{'100-250':>9}{'>250':>7}{'noEvent':>9}")
for y in sorted(byy):
    rs=byy[y]; mis=[F(r['w2_mi']) for r in rs if F(r['w2_mi']) is not None]
    b=lambda lo,hi: sum(1 for m in mis if lo<=m<hi)
    print(f"{y:5}{len(rs):7d}"
          f"{(st.median(mis) if mis else float('nan')):11.1f}{(st.mean(mis) if mis else float('nan')):10.1f}"
          f"{(min(mis) if mis else float('nan')):9.1f}{b(0,40):8d}{b(40,100):8d}{b(100,250):9d}"
          f"{sum(1 for m in mis if m>=250):7d}{sum(1 for r in rs if r['match_class']=='NO_NA_EVENT_WITHIN_2D'):9d}")

print()
print("TABLE C - same, EXCLUDING KILG (documented transatlantic customs/fuel stop)")
print(f"{'year':5}{'n(rec)':>7}{'median_mi':>11}{'mean_mi':>10}{'min_mi':>9}")
for y in sorted(byy):
    rs=[r for r in byy[y] if r['is_kilg']=='no']
    mis=[F(r['w2_mi']) for r in rs if F(r['w2_mi']) is not None]
    print(f"{y:5}{len(rs):7d}{(st.median(mis) if mis else float('nan')):11.1f}"
          f"{(st.mean(mis) if mis else float('nan')):10.1f}{(min(mis) if mis else float('nan')):9.1f}")

print()
print("TABLE D - airport mix by year (visit records)")
ap=defaultdict(lambda: defaultdict(int))
for r in rows: ap[r['year']][r['airport']]+=1
for y in sorted(ap):
    print(y, ' '.join(f"{k}:{v}" for k,v in sorted(ap[y].items(), key=lambda kv:-kv[1])))

print()
print("TABLE E - ERA test: KPVU (Provo) foreign-fleet visit days before vs after 2025-09-10")
pre=sorted({(r['tail'],r['day']) for r in rows if r['airport']=='KPVU' and r['day']<='2025-09-10'})
post=sorted({(r['tail'],r['day']) for r in rows if r['airport']=='KPVU' and r['day']>'2025-09-10'})
print(' PRE  (<=2025-09-10):',len(pre)); print('  ',pre)
print(' POST (> 2025-09-10):',len(post)); print('  ',post)
h_pre=sum(1 for t in FOREIGN for d in cov['held'][t] if d<='2025-09-10')
h_post=sum(1 for t in FOREIGN for d in cov['held'][t] if d>'2025-09-10')
a_pre=sum(1 for t in FOREIGN for d in cov['asked'][t] if d<='2025-09-10')
a_post=sum(1 for t in FOREIGN for d in cov['asked'][t] if d>'2025-09-10')
print(f"  held pre={h_pre} (asked {a_pre}), held post={h_post} (asked {a_post})")
print(f"  Provo rate pre  = {100*len(pre)/h_pre:.2f} per 100 held aircraft-days")
print(f"  Provo rate post = {100*len(post)/h_post:.2f} per 100 held aircraft-days")

print()
print("TABLE F - all foreign-fleet visit records with nearest NA event <=100 mi, any year")
for r in sorted(rows,key=lambda x:x['day']):
    m=F(r['w2_mi'])
    if m is not None and m<=250:
        print(f"  {r['day']} {r['tail']:7} {r['airport']:5} {r['match_class']:22} {m:7.1f} mi  gap {r['w2_gap']}d  {r['w2_event']} ({r['w2_class']}, arr {r['w2_arr']})")
