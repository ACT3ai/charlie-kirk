#!/bin/sh
# Rebuild every generated section and page under /Planes/ from the recovered
# ADS-B data.  Order matters:
#
#   1. interesting dates   writes analysis/interesting_dates.json, which
#                          everything downstream reads
#   2. airport + incident  creates the pages that the tables link INTO, so they
#      pages               must exist before any link is emitted (links are
#                          gated on page existence and silently degrade to
#                          plain text if the page is missing)
#   3. the table sections  per-aircraft, per-person, per-event, per-claim
#   4. inbound links       scans the finished pages and links what they mention
#
# Safe to re-run: every generator writes only between its own markers.
set -e
cd "$(dirname "$0")"

python3 build_interesting_dates.py
python3 build_airport_incident_pages.py
python3 build_flight_record.py
python3 build_following_tables.py
python3 build_event_aircraft.py
python3 build_overlap_verdicts.py
python3 link_new_evidence.py

echo
echo "Now run:  cd site && npm run build"
