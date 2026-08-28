#!/usr/bin/env python3
"""
extract_wayback_trackpoll.py  --  OFFLINE. Makes no network request.

WHY THIS EXISTS
---------------
extract_wayback_flights.py reads FlightAware's SERVER-RENDERED activity table.
FlightAware stopped server-rendering that table somewhere between 2016 and 2022,
so every archived FlightAware page from 2022 onward was recorded in
data/recovery/wayback_flight_rows.json as

    "table_state": "JAVASCRIPT_SHELL_NO_SERVER_RENDERED_ROWS", rows_recovered: 0

That verdict is wrong about the BYTES. The rows are not in the HTML table, but the
same page ships a JSON blob, `var trackpollBootstrap = {...}`, that carries the
flight legs FlightAware was showing at capture time. This script parses that blob
out of the archived HTML already on disk and prints/writes the legs.

It recovers CONTENT ONLY. It says nothing about removal, and nothing about who was
on board. A leg here is what one tracking site displayed on one archived date.

USAGE
    python3 extract_wayback_trackpoll.py                 # print a table
    python3 extract_wayback_trackpoll.py --json OUT.json # also write JSON
"""
import re, json, glob, os, sys, datetime

PLANES = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                      '..', '..', '..', '..'))  # site/docs/Planes


def brace_match(s, start):
    """Return the substring of the balanced {...} beginning at s[start] == '{'."""
    depth, i, in_str, esc = 0, start, False, False
    while i < len(s):
        ch = s[i]
        if in_str:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return s[start:i + 1]
        i += 1
    return None


def utc(ts):
    if not ts:
        return None
    try:
        return datetime.datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%dT%H:%M:%SZ')
    except Exception:
        return None


def legs_from_file(path):
    h = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'var\s+trackpollBootstrap\s*=\s*', h)
    if not m:
        return None
    blob = brace_match(h, h.index('{', m.end() - 1))
    if not blob:
        return None
    try:
        d = json.loads(blob)
    except Exception as e:
        return {'parse_error': str(e)}
    out = []
    for key, fl in (d.get('flights') or {}).items():
        ac = fl.get('aircraft') or {}
        act = fl.get('activityLog') or {}
        origin = fl.get('origin') or {}
        dest = fl.get('destination') or {}
        base = {
            'bootstrap_key': key,
            'tail': ac.get('tail'),
            'type': ac.get('type'),
            'owner': ac.get('owner'),
            'owner_location': ac.get('ownerLocation'),
            'blocked_flag': fl.get('blocked'),
        }
        rows = act.get('flights') or []
        if not rows:
            out.append(dict(base, leg_source='summary', origin=origin.get('icao'),
                            destination=dest.get('icao'),
                            takeoff_utc=utc(fl.get('takeoffTimes', {}).get('actual')
                                            if isinstance(fl.get('takeoffTimes'), dict) else None)))
        for r in rows:
            o = r.get('origin') or {}
            de = r.get('destination') or {}
            out.append(dict(base,
                            leg_source='activityLog',
                            flight_id=r.get('flightId'),
                            ident=r.get('ident'),
                            origin=o.get('icao') or o.get('iata') or o.get('friendlyLocation'),
                            destination=de.get('icao') or de.get('iata') or de.get('friendlyLocation'),
                            takeoff_utc=utc((r.get('takeoffTimes') or {}).get('actual')),
                            landing_utc=utc((r.get('landingTimes') or {}).get('actual')),
                            gate_out_utc=utc((r.get('gateDepartureTimes') or {}).get('actual')),
                            gate_in_utc=utc((r.get('gateArrivalTimes') or {}).get('actual')),
                            aircraft_type=(r.get('aircraft') or {}).get('type')))
    return out


def main():
    results = []
    for f in sorted(glob.glob(os.path.join(PLANES, '*', 'data', 'recovered',
                                           '*wayback_flightaware.html'))):
        legs = legs_from_file(f)
        meta_path = f + '.meta.json'
        meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
        results.append({
            'file': os.path.relpath(f, PLANES),
            'snapshot_utc': meta.get('snapshot_utc'),
            'archive_http': meta.get('http_status'),
            'recorded_table_state': meta.get('table_state'),
            'recorded_rows': meta.get('flight_rows_recovered'),
            'trackpoll_present': legs is not None,
            'trackpoll_legs': 0 if not legs else len([l for l in legs
                                                      if l.get('leg_source') == 'activityLog']),
            'legs': legs or [],
        })
    for r in results:
        print('%-58s snap=%-15s recorded=%-40s trackpoll_legs=%d' % (
            os.path.basename(r['file']), r['snapshot_utc'],
            str(r['recorded_table_state']), r['trackpoll_legs']))
    if '--json' in sys.argv:
        out = sys.argv[sys.argv.index('--json') + 1]
        json.dump({'generated_utc': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                   'note': 'OFFLINE re-extraction of archived FlightAware pages already on disk. '
                           'Recovers CONTENT only; establishes no removal and no occupancy.',
                   'captures': results}, open(out, 'w'), indent=1)
        print('wrote', out)


if __name__ == '__main__':
    main()
