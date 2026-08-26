import os, re, json, glob, csv, collections, datetime, sys

PL = "/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes"
SPK = os.path.join(PL, "following", "speaking")
OUT = "/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad"

FOREIGN = ["SU-BGM","SU-BND","SU-BTT","SU-BTU","SU-BTV","T7-ELL"]
KIRK = ["N102DZ","N1098L","N2100L","N40JD","N560TW","N582MM","N59906","N872RA","N888KG"]
FLEET = FOREIGN + KIRK
CONTROLS = ["CONTROL-RYANAIR","CONTROL-LUFTHANSA"]

pat_miss = re.compile(r'^(?P<tail>.+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full\.miss\.json\.meta\.json$')
pat_held = re.compile(r'^(?P<tail>.+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<src>[a-z0-9\-]+)_trace_full\.json(?P<gz>\.gz)?$')

# state[(tail,date)] -> dict src -> 'HELD'/'ASKED_AND_EMPTY'
state = collections.defaultdict(dict)
other_files = collections.Counter()

for tail in FLEET + CONTROLS + ["N55906"]:
    d = os.path.join(PL, tail, "data", "recovered")
    if not os.path.isdir(d):
        continue
    for fn in os.listdir(d):
        if fn.endswith(".meta.json") and not fn.endswith(".miss.json.meta.json"):
            continue  # companion meta of a held payload
        m = pat_miss.match(fn)
        if m:
            state[(tail, m.group('date'))][m.group('src')] = 'ASKED_AND_EMPTY'
            continue
        m = pat_held.match(fn)
        if m:
            state[(tail, m.group('date'))][m.group('src')] = 'HELD'
            continue
        other_files[fn.split('_')[-1]] += 1

# collapse per aircraft-day
day_state = {}
day_srcs = {}
for k, srcs in state.items():
    day_srcs[k] = srcs
    day_state[k] = 'HELD' if 'HELD' in srcs.values() else 'ASKED_AND_EMPTY'

# ---------- event windows: the denominator ----------
import yaml
events = []
for y in sorted(glob.glob(os.path.join(SPK, "*.yaml"))):
    with open(y) as f:
        doc = yaml.safe_load(f)
    events.append((os.path.basename(y)[:-5], doc))
print("events:", len(events), file=sys.stderr)

def daterange(a, b):
    a = a if isinstance(a, datetime.date) else datetime.date.fromisoformat(str(a))
    b = b if isinstance(b, datetime.date) else datetime.date.fromisoformat(str(b))
    out = []
    while a <= b:
        out.append(a.isoformat()); a += datetime.timedelta(days=1)
    return out

needed = set()   # (tail, date)
no_window = []
ev_rows = []
disagreements = []
for slug, doc in events:
    if 'search' not in doc:
        ev_rows.append(dict(slug=slug, window_from='', window_to='', days=0, tails=0,
            needed=0, held=0, empty=0, never=0, f_needed=0, f_held=0, f_empty=0, f_never=0,
            yaml_needed=None, yaml_held=None, yaml_empty=None, yaml_never=None,
            yaml_cov_pct=None, yaml_verdict='NO SEARCH WINDOW', yaml_verdict_full='NO SEARCH WINDOW - geocode FAILED, city UNKNOWN/AMBIGUOUS in tpusa_events.csv',
            yaml_ctrl_pct=None, yaml_f_needed=None, yaml_f_held=None, yaml_f_empty=None,
            yaml_f_never=None, yaml_f_cov=None, yaml_f_qry=None))
        no_window.append(slug)
        continue
    s = doc['search']
    wdays = daterange(s['window_from'], s['window_to'])
    tails = s['tails_searched']
    cov = doc['coverage'] if 'coverage' in doc else doc.get('adsb',{}).get('coverage')
    # find coverage block wherever it is
    def findcov(o):
        if isinstance(o, dict):
            if 'aircraft_days_needed' in o and 'aircraft_days_held' in o:
                return o
            for v in o.values():
                r = findcov(v)
                if r: return r
        elif isinstance(o, list):
            for v in o:
                r = findcov(v)
                if r: return r
        return None
    cov = findcov(doc)
    my = collections.Counter()
    my_by_side = {'following': collections.Counter(), 'kirk': collections.Counter()}
    for t in tails:
        for d in wdays:
            needed.add((t, d))
            st = day_state.get((t, d), 'NEVER_ASKED')
            my[st] += 1
            if t in FOREIGN:
                my_by_side['following'][st] += 1
    ev_rows.append(dict(slug=slug, window_from=str(s['window_from']), window_to=str(s['window_to']),
        days=len(wdays), tails=len(tails),
        needed=len(wdays)*len(tails),
        held=my['HELD'], empty=my['ASKED_AND_EMPTY'], never=my['NEVER_ASKED'],
        f_needed=len(wdays)*sum(1 for t in tails if t in FOREIGN),
        f_held=my_by_side['following']['HELD'],
        f_empty=my_by_side['following']['ASKED_AND_EMPTY'],
        f_never=my_by_side['following']['NEVER_ASKED'],
        yaml_needed=cov['aircraft_days_needed'] if cov else None,
        yaml_held=cov['aircraft_days_held'] if cov else None,
        yaml_empty=cov['aircraft_days_asked_and_archive_empty'] if cov else None,
        yaml_never=cov['aircraft_days_never_asked'] if cov else None,
        yaml_cov_pct=cov.get('coverage_pct') if cov else None,
        yaml_verdict=(cov.get('archive_control_test') or {}).get('verdict','')[:60] if cov else '',
        yaml_verdict_full=(cov.get('archive_control_test') or {}).get('verdict','') if cov else '',
        yaml_ctrl_pct=(cov.get('archive_control_test') or {}).get('control_hit_pct_this_year') if cov else None,
        yaml_f_needed=(cov.get('by_side',{}).get('following',{}) or {}).get('aircraft_days_needed') if cov else None,
        yaml_f_held=(cov.get('by_side',{}).get('following',{}) or {}).get('aircraft_days_held') if cov else None,
        yaml_f_empty=(cov.get('by_side',{}).get('following',{}) or {}).get('aircraft_days_asked_and_archive_empty') if cov else None,
        yaml_f_never=(cov.get('by_side',{}).get('following',{}) or {}).get('aircraft_days_never_asked') if cov else None,
        yaml_f_cov=(cov.get('by_side',{}).get('following',{}) or {}).get('coverage_pct') if cov else None,
        yaml_f_qry=(cov.get('by_side',{}).get('following',{}) or {}).get('queried_pct') if cov else None,
        ))

json.dump(dict(ev_rows=ev_rows), open(os.path.join(OUT,"ev_rows.json"),"w"), indent=1)

# ---------- per tail per year ----------
rows = []
for tail in FLEET + CONTROLS:
    per = collections.defaultdict(collections.Counter)
    for (t, d), st in day_state.items():
        if t != tail: continue
        per[d[:4]][st] += 1
    # never-asked from needed set
    for (t, d) in needed:
        if t != tail: continue
        if (t, d) not in day_state:
            per[d[:4]]['NEVER_ASKED'] += 1
    for yr in sorted(per):
        c = per[yr]
        rows.append(dict(tail=tail, side=('FOREIGN' if tail in FOREIGN else 'KIRK' if tail in KIRK else 'CONTROL'),
                         year=yr, held=c['HELD'], asked_and_empty=c['ASKED_AND_EMPTY'],
                         never_asked=c['NEVER_ASKED']))
json.dump(rows, open(os.path.join(OUT,"tail_year.json"),"w"), indent=1)

# source breakdown
srcc = collections.Counter()
for k, srcs in day_srcs.items():
    for s, st in srcs.items():
        srcc[(s, st)] += 1
json.dump({f"{a}|{b}": c for (a,b),c in sorted(srcc.items())}, open(os.path.join(OUT,"src_counts.json"),"w"), indent=1)
json.dump(no_window, open(os.path.join(OUT,"no_window.json"),"w"), indent=1)
print("wrote intermediates; no_window=", no_window, file=sys.stderr)
