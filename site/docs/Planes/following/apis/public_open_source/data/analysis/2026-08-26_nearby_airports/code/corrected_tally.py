#!/usr/bin/env python3
"""
The corrected overlap tally, and the before/after against the pass it replaces.

  BEFORE  ../../overlap_verification/overlap_verification.json        24 Aug 2026
  AFTER   ../../overlap_verification/overlap_verification_local.json  26 Aug 2026

The 26 August run is the one to quote. It is strictly same-day, it measures closest
approach point-by-point off the raw trace with on-ground fixes ranked above airborne
ones, and it runs against a corpus roughly an order of magnitude larger.

Run:  python3 code/corrected_tally.py
"""
import json, os, collections

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VDIR = os.path.join(HERE, '..', '..', 'overlap_verification')
new = json.load(open(os.path.join(VDIR, 'overlap_verification_local.json')))
old = json.load(open(os.path.join(VDIR, 'overlap_verification.json')))

N = {r['overlap_id']: r for r in new['rows']}
O = {r['overlap_id']: r for r in old['results']}
c = new['counts']

SUPPORT = ('AT_CLAIMED_AIRPORT',)
METRO   = ('SAME_METRO_WRONG_FIELD',)
AGAINST = ('ELSEWHERE',)
dec = c['AT_CLAIMED_AIRPORT'] + c['SAME_METRO_WRONG_FIELD'] + c['ELSEWHERE']

print('=' * 76)
print('CORRECTED OVERLAP TALLY  --  85 rows, verified %s' % new['verified_utc'])
print('=' * 76)
print()
print('  %-28s %8s %10s' % ('', '24 Aug', '26 Aug'))
for k in ['AT_CLAIMED_AIRPORT', 'SAME_METRO_WRONG_FIELD', 'ELSEWHERE',
          'NOT_HEARD', 'NO_ARCHIVE_COVERAGE', 'NO_TAIL_CLAIMED', 'NO_DATE_CLAIMED']:
    print('  %-28s %8s %10d' % (k, old['tally'].get(k, '-'), c.get(k, 0)))
print()
print('  decidable ................. %d of 85' % dec)
print('  corroborated .............. %d  (%.0f%% of decidable)'
      % (c['AT_CLAIMED_AIRPORT'], 100.0 * c['AT_CLAIMED_AIRPORT'] / dec))
print('  same metro, wrong field ... %d' % c['SAME_METRO_WRONG_FIELD'])
print('  refuted ................... %d  (%.0f%% of decidable)'
      % (c['ELSEWHERE'], 100.0 * c['ELSEWHERE'] / dec))
print('  on-ground corroborations .. %d  (strongest evidence class)'
      % new['on_ground_corroborations'])
print()

print('-' * 76)
print('THE 12 ROWS THE 24 AUG PASS CALLED "ELSEWHERE"')
print('-' * 76)
hold = ret = 0
for oid, o in sorted(O.items()):
    if o.get('verdict') != 'ELSEWHERE':
        continue
    v = N.get(oid, {}).get('verdict')
    still = v in AGAINST
    hold += still; ret += not still
    print('  %-11s %-10s -> %-24s %s'
          % (oid, o['date'], v, 'HOLDS' if still else 'RETRACTED'))
print('\n  refutations that survive: %d      retracted: %d' % (hold, ret))
print()
print('  Also downgraded, so the correction is not one-way:')
for oid, o in sorted(O.items()):
    v = N.get(oid, {}).get('verdict')
    if o.get('verdict') == 'AT_CLAIMED_AIRPORT' and v != 'AT_CLAIMED_AIRPORT':
        print('    %-11s %-10s AT_CLAIMED_AIRPORT -> %s' % (oid, o['date'], v))
print()

print('-' * 76)
print('CROSS-TAB: the X/Twitter accuracy audit vs recovered primary ADS-B')
print('-' * 76)
def band(v):
    return ('supports' if v in SUPPORT else 'metro' if v in METRO
            else 'contradicts' if v in AGAINST else 'cannot test')
b = collections.Counter((r.get('kanekoa_audit_verdict') or 'unscored', band(r['verdict']))
                        for r in new['rows'])
cols = ['supports', 'metro', 'contradicts', 'cannot test']
print('  %-13s %9s %6s %12s %13s %7s' % ('audit said', *cols, 'total'))
for a in ['accurate', 'partial', 'inaccurate', 'archive_gap', 'unpublished', 'unscored']:
    line = [b[(a, x)] for x in cols]
    if sum(line):
        print('  %-13s %9d %6d %12d %13d %7d' % (a, *line, sum(line)))
print()
i = [b[('inaccurate', x)] for x in cols]
print('  Of the %d rows the audit called INACCURATE:' % sum(i))
print('    %2d decidable on primary ADS-B; the audit is WRONG on %d of them' % (i[0]+i[1]+i[2], i[0]+i[1]))
print('    %2d cannot be tested by any free archive -- UNTESTED, not refuted' % i[3])
ap_s = b[('accurate','supports')] + b[('partial','supports')] + b[('accurate','metro')] + b[('partial','metro')]
ap_c = b[('accurate','contradicts')] + b[('partial','contradicts')]
print('  Of the %d rows it called ACCURATE or PARTIAL: %d supported, %d contradicted'
      % (sum(b[(a,x)] for a in ('accurate','partial') for x in cols), ap_s, ap_c))
print()
print('  Rows the audit called inaccurate that primary data SUPPORTS:')
for r in new['rows']:
    if r.get('kanekoa_audit_verdict') == 'inaccurate' and r['verdict'] in SUPPORT + METRO:
        print('    %-11s %-10s %-8s %-6s %6.2f km'
              % (r['overlap_id'], r['date'], '/'.join(r['tails']),
                 r['claimed_airport'], r['closest_approach_km']))
print()
print('=' * 76)
print('HEADLINE FOR PUBLICATION')
print('=' * 76)
print('  Of the %d rows primary position data can decide, %d are corroborated,' % (dec, c['AT_CLAIMED_AIRPORT']))
print('  %d is same-metro-wrong-field and %d are refuted.' % (c['SAME_METRO_WRONG_FIELD'], c['ELSEWHERE']))
print('  The 24 Aug pass published %d refutations; %d were retracted.'
      % (old['tally']['ELSEWHERE'], ret))
