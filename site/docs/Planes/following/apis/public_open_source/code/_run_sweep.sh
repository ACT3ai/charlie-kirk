#!/bin/sh
# Drive geo_sweep.py to completion.
#
# A day that ends TRUNCATED or PROBE_UNRESOLVED is deliberately NOT counted as
# done by already_swept(), so simply running the sweep again retries exactly the
# days that did not resolve and skips the ones that did. Five passes, because a
# transient network failure should not become a permanent hole in the coverage
# record -- and a day still unresolved after five tries stays on disk saying so,
# which is the honest outcome, not a silent zero.
cd "$(dirname "$0")"
for pass in 1 2 3 4 5; do
  echo "=========== PASS $pass  $(date -u +%Y-%m-%dT%H:%M:%SZ) ==========="
  python3 -u geo_sweep.py --run --jobs 4 || true
  left=$(python3 - <<'PY'
import json, glob, os
n = 0
for mp in glob.glob(os.path.join("..", "data", "geo_sweep", "2*", "_sweep.meta.json")):
    try:
        if json.load(open(mp)).get("status") not in ("SWEPT", "NO_RELEASE_FOR_THIS_DATE"):
            n += 1
    except Exception:
        n += 1
print(n)
PY
)
  echo "PASS $pass done; $left day(s) still unresolved"
  [ "$left" = "0" ] && break
done
echo "=========== SWEEP FINISHED $(date -u +%Y-%m-%dT%H:%M:%SZ) ==========="
python3 -u analyse_geo_sweep.py --json
