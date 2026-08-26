import json,csv,collections
D='/private/tmp/claude-501/-Users-bryanstarbuck-BGit-Bryan-git-charlie-kirk-site-docs-Planes/9300dd48-3a6d-45a1-960c-5f5606096c22/scratchpad/'
rs=json.load(open(D+'claims_audit.json'))
BY={r['overlap_id']:r for r in rs}

# hand-verified overrides (each one opened in the raw trace and read fix by fix)
OV={
 'OWENS-012':('CONSISTENT_ARRIVAL_COVERAGE_ENDS',
   'airplanes.live trace runs Paris LFPG 09:01Z to a stabilised descent that ends 27.6 km from KICT at 5,050 ft baro (3,717 ft AGL), 18:18:17Z, still closing. Consistent with an arrival in the Wichita area; touchdown is not in the trace. The published note computed 7,411 km from the FIRST fix of the day and ignored the rest of the trace, while its own text says the last fix was 11 km from a Topeka airpark.',
   'RETRACT "REFUTED". Change adsb_verified_verdict ELSEWHERE -> CONSISTENT_NOT_PROVEN and rewrite the note.'),
 'OWENS-015':('PARTIAL_ST_LOUIS_CONFIRMED_GOOSE_BAY_UNTESTED',
   'Same-day trace departs KCPS St Louis Downtown 20:02Z and ends over La Tuque, Quebec at FL410 22:10Z, 1,063 km short of Goose Bay and still north-eastbound; the next trace picks the aircraft up over Ireland at 04:18Z. A Goose Bay fuel stop fits the gap and is neither shown nor excluded.',
   'RETRACT "REFUTED". The St Louis half of this row is CONFIRMED by primary data; the Goose Bay half is untested.'),
 'OWENS-024':('CONFIRMS_DEPARTURE_FROM_CLAIMED_FIELD',
   'airplanes.live trace OPENS with SU-BTT climbing out of Wichita: 13:43:30Z, 1.4 km from KICT, 1,675 ft baro (342 ft AGL), then a continuous FL410 leg to a landing at Wilmington KILG at 16:05Z. The adsb.lol trace for the same day does not start until 14:15Z over Missouri, which is why the published note reports a 1,853 km closest approach and calls the claim REFUTED.',
   'RETRACT "REFUTED". Change ELSEWHERE -> AT_CLAIMED_AIRPORT (departure). This is a hard reversal.'),
 'SITE-003':('CONFIRMS_DEPARTURE_FROM_CLAIMED_FIELD',
   'Identical evidence to OWENS-024: departure roll out of KICT at 13:43:30Z, 342 ft AGL, 1.4 km from the field, then nonstop to KILG.',
   'RETRACT "REFUTED". Change ELSEWHERE -> AT_CLAIMED_AIRPORT (departure).'),
 'OWENS-036':('CONTRADICTS_WEAKLY',
   'Only 7-9 fixes exist for the whole day and they put SU-BTT at FL320 between Alexandria and El Alamein, Egypt, at 06:23-06:28Z, 10,140 km from Omaha. A same-day Omaha arrival is not geometrically excluded by five minutes of coverage, but it would require a Cairo departure and a fuel stop.',
   'Keep ELSEWHERE but say the coverage is five minutes, not a day.'),
 'OWENS-050':('CONTRADICTS',
   'Same-day trace runs Paris Le Bourget 07:25Z to Inshas Air Base, Cairo 11:15Z, never closer than 7,034 km to St Louis. Combined with the 09 May trace showing the aircraft leaving St Louis for Europe, the claim cannot stand.',
   'Keep ELSEWHERE. This one is genuinely refuted by primary data.'),
}
DOWNGRADE={  # published REFUTED that rests on the wrong day and is physically compatible with the claim
 'OWENS-016':'Cairo-area local flying on 11 Jun 2023 ends 09:16Z, 11,330 km from Provo, with 38.7 h before the claimed day closes and 14.2 h of cruise needed.',
 'OWENS-030':'Cairo-area local flying on 7 Dec 2024 ends 17:48Z, 11,431 km from Provo, 30.2 h available against 14.3 h needed.',
 'OWENS-052':'Cairo-area local flying on 24 Jun 2023 ends 08:27Z, 9,228 km from Wilmington, 39.5 h available against 11.5 h needed.',
 'OWENS-028':'Local Egyptian sectors on 21 Jul 2024 begin 06:33Z, 10,405 km from Omaha; that leaves the first ~16 h of 20 Jul unaccounted for, and no trace covers it.',
 'OWENS-029':'Local Egyptian sectors on 18 Aug 2024 begin 09:36Z, 10,402 km from Omaha; 33.6 h available against 13.0 h needed.',
 'OWENS-055':'Cairo sectors on 16 Apr 2024 begin 16:42Z, 10,400 km from Omaha; 40.7 h available against 13.0 h needed.',
}
for r in rs:
    oid=r['overlap_id']
    r['correction_action']=''
    if oid in OV:
        v,e,a=OV[oid]; r['my_verdict']=v; r['evidence']=e; r['correction_action']=a
    if oid in DOWNGRADE:
        r['correction_action']=('RETRACT "REFUTED" - the note rests on '+r['note_cites_date']+
          ', not on the claimed day, and the claim is physically compatible with it. '+DOWNGRADE[oid]+
          ' Change ELSEWHERE -> NOT TESTED.')
    if oid in ('OWENS-042','EXTRA-006','SITE-001','SITE-005') and r.get('note_uses_wrong_day'):
        r['correction_action']=('Note cites '+r['note_cites_date']+', not the claimed day. Same-day primary data exists and is stronger - '
                                'restate the note on the claimed date.')
hdr=['overlap_id','date','foreign_tail','claimed_airport','city','state','subject','audit_verdict',
     'existing_adsb_verdict','my_verdict','agrees','note_cites_date','note_uses_wrong_day','correction_action',
     'sources','closest_km','closest_agl','ground_at_claimed','ground_airports_that_day','evidence','detail',
     'existing_km','existing_note','overlap_page']
with open(D+'claims_audit.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=hdr); w.writeheader()
    for r in rs: w.writerow({k:r.get(k,'') for k in hdr})
json.dump(rs,open(D+'claims_audit.json','w'),indent=1)
print(collections.Counter(r['my_verdict'] for r in rs))
print('corrections queued:',sum(1 for r in rs if r['correction_action']))
