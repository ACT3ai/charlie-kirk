#!/usr/bin/env python3
"""
Corrected overlap tally.

The published 24-confirmed / 12-refuted tally in
    ../../overlap_verification/overlap_verification.json
was produced by a pass that section 5 of _claims_audit.md shows to be defective in
five specific, enumerated ways: closest approach computed on one fix or on the
wrong archive's trace, "both archives agree" asserted where they hold different
amounts of the day, ten rows verdicted on a date other than the claimed date, an
overflight at 3,357 ft AGL read as a landing, and NOT_HEARD mixed with
NO_ARCHIVE_COVERAGE.

This script re-tallies the same 85 rows using the per-row verdict the 2026-08-26
audit reached by reading every fix in every recovered trace, and prints the
before/after so a page can quote it.

Run:  python3 code/corrected_tally.py
"""
import csv, json, os, collections

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT = os.path.join(HERE, 'claims_audit.csv')
PRIOR = os.path.join(HERE, '..', '..', 'overlap_verification', 'overlap_verification.json')

SUPPORTS = (
    'CONFIRMS_ON_GROUND_AT_CLAIMED_FIELD',
    'CONFIRMS_DEPARTURE_FROM_CLAIMED_FIELD',
    'CONFIRMS_APPROACH_OR_DEPARTURE',
    'CONSISTENT_ARRIVAL_COVERAGE_ENDS',
    'CONSISTENT_LOW_OVER_CLAIMED_METRO',
    'PARTIAL_ST_LOUIS_CONFIRMED_GOOSE_BAY_UNTESTED',
)
CONTRADICTS = ('CONTRADICTS', 'CONTRADICTS_WEAKLY')
SILENT = ('NOT_HEARD', 'NO_ARCHIVE_COVERAGE', 'NO_DATE_CLAIMED', 'NO_TAIL_CLAIMED')

rows = list(csv.DictReader(open(AUDIT)))
prior = json.load(open(PRIOR))
prior_by_id = {r['overlap_id']: r for r in prior['results']}

sup = [r for r in rows if r['my_verdict'] in SUPPORTS]
con = [r for r in rows if r['my_verdict'] in CONTRADICTS]
sil = [r for r in rows if r['my_verdict'] in SILENT]
assert len(sup) + len(con) + len(sil) == len(rows), 'unclassified verdict'

decidable = len(sup) + len(con)

print('=' * 78)
print('CORRECTED OVERLAP TALLY  --  %d rows of overlaps.csv' % len(rows))
print('=' * 78)
print()
print('PRIOR PASS (overlap_verification.json, 24 Aug 2026), as published:')
for k, v in prior['tally'].items():
    print('   %-22s %3d' % (k, v))
p_dec = prior['tally']['AT_CLAIMED_AIRPORT'] + prior['tally']['ELSEWHERE']
print('   decidable %d ; refuted %d = %.0f%% of decidable'
      % (p_dec, prior['tally']['ELSEWHERE'], 100.0 * prior['tally']['ELSEWHERE'] / p_dec))
print()
print('CORRECTED PASS (26 Aug 2026, every fix in every recovered trace):')
print('   supported by same-day primary position data   %3d' % len(sup))
print('   contradicted by same-day primary position data %3d' % len(con))
print('   primary data says nothing either way           %3d' % len(sil))
print('   decidable %d ; contradicted %d = %.1f%% of decidable'
      % (decidable, len(con), 100.0 * len(con) / decidable))
print('   supported = %.1f%% of decidable' % (100.0 * len(sup) / decidable))
print()

print('-' * 78)
print('THE 12 ROWS THE PRIOR PASS CALLED "ELSEWHERE" (refuted)')
print('-' * 78)
kept = retracted = 0
for oid, pr in sorted(prior_by_id.items()):
    if pr.get('verdict') != 'ELSEWHERE' and pr.get('adsb_verified_verdict') != 'ELSEWHERE':
        continue
    a = next((r for r in rows if r['overlap_id'] == oid), None)
    if not a:
        continue
    now = a['my_verdict']
    still = now in CONTRADICTS
    kept += still
    retracted += not still
    print('  %-11s %-10s %-7s %-6s  prior=ELSEWHERE  now=%s  %s'
          % (oid, a['date'], a['foreign_tail'], a['claimed_airport'], now,
             'HOLDS' if still else 'RETRACTED'))
print()
print('  refutations that survive primary data: %d' % kept)
print('  refutations retracted:                 %d' % retracted)
print()

print('-' * 78)
print('WHY EACH RETRACTION HAPPENED (correction_action, from the audit)')
print('-' * 78)
reasons = collections.Counter()
for r in rows:
    ca = r['correction_action']
    if not ca:
        continue
    if 'rests on' in ca and 'not on the claimed day' in ca:
        reasons['refuted on a DIFFERENT DAY than the one claimed'] += 1
    elif 'hard reversal' in ca.lower() or 'AT_CLAIMED_AIRPORT (departure)' in ca:
        reasons['aircraft was AT the claimed field - refutation reversed'] += 1
    elif 'CONSISTENT_NOT_PROVEN' in ca:
        reasons['closest approach was read off the shorter archive trace'] += 1
    elif 'St Louis half' in ca:
        reasons['half the row confirmed, half untested - not refuted'] += 1
    elif 'Keep ELSEWHERE' in ca:
        reasons['refutation KEPT - genuinely contradicted'] += 1
    else:
        reasons['note restated on the claimed date'] += 1
for k, v in reasons.most_common():
    print('   %-58s %2d' % (k, v))
print()

print('-' * 78)
print('CROSS-TAB: the X/Twitter accuracy audit vs recovered primary ADS-B')
print('-' * 78)
buckets = collections.Counter()
for r in rows:
    av = r['audit_verdict'] or 'unscored'
    mv = ('supported' if r['my_verdict'] in SUPPORTS else
          'contradicted' if r['my_verdict'] in CONTRADICTS else 'cannot test')
    buckets[(av, mv)] += 1
labels = ['supported', 'contradicted', 'cannot test']
print('   %-14s %11s %13s %13s %7s' % ('audit said', *labels, 'total'))
for av in ['accurate', 'partial', 'inaccurate', 'archive_gap', 'unpublished', 'unscored']:
    line = [buckets[(av, l)] for l in labels]
    if not sum(line):
        continue
    print('   %-14s %11d %13d %13d %7d' % (av, *line, sum(line)))
print()
ina_sup = buckets[('inaccurate', 'supported')]
ina_con = buckets[('inaccurate', 'contradicted')]
ina_non = buckets[('inaccurate', 'cannot test')]
ina_tot = ina_sup + ina_con + ina_non
print('  Of the %d rows the audit called INACCURATE:' % ina_tot)
print('    %2d are CONFIRMED by same-day primary position data (audit wrong)' % ina_sup)
print('    %2d are contradicted by same-day primary position data (audit right)' % ina_con)
print('    %2d cannot be tested by primary data at all' % ina_non)
if ina_sup + ina_con:
    print('    -> on its own decidable rows the audit is wrong %d of %d = %.0f%%'
          % (ina_sup, ina_sup + ina_con, 100.0 * ina_sup / (ina_sup + ina_con)))
print()

acc_sup = buckets[('accurate', 'supported')] + buckets[('partial', 'supported')]
acc_con = buckets[('accurate', 'contradicted')] + buckets[('partial', 'contradicted')]
print('  Of the %d rows the audit called ACCURATE or PARTIAL:' % (
    sum(buckets[(a, l)] for a in ('accurate', 'partial') for l in labels)))
print('    %2d are confirmed by primary position data' % acc_sup)
print('    %2d are contradicted by primary position data' % acc_con)
print()

print('=' * 78)
print('HEADLINE NUMBERS FOR PUBLICATION')
print('=' * 78)
print('  decidable on primary ADS-B ............. %d of %d rows' % (decidable, len(rows)))
print('  supported .............................. %d  (%.0f%% of decidable)'
      % (len(sup), 100.0 * len(sup) / decidable))
print('  contradicted ........................... %d  (%.0f%% of decidable)'
      % (len(con), 100.0 * len(con) / decidable))
print('  on a different continent, primary data .. %d  (%.0f%% of decidable)'
      % (len(con), 100.0 * len(con) / decidable))
print('  untestable ............................. %d' % len(sil))
print('  prior published refuted count .......... %d' % prior['tally']['ELSEWHERE'])
print('  of which retracted ..................... %d' % retracted)
