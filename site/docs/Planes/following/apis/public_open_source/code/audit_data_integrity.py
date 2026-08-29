#!/usr/bin/env python3
"""DATA INTEGRITY AUDIT -- find evidence that is on disk but UNREADABLE,
MIS-ATTRIBUTED, or SILENTLY DROPPED by our own tooling.

This is the audit that matters most, because every other number in this
investigation is computed from files this one checks. A payload that exists but
cannot be parsed is worse than a missing one: the missing one is counted as
missing, and the unreadable one is counted as present and then contributes
nothing.

Seven classes, each of which has actually occurred here:

  A  CORRUPT META      .meta.json that json.load() refuses. One on disk was
                       written TWICE, so the file is two concatenated objects.
  B  CONTAINER LIE     a payload whose bytes are gzip but whose name ends .json
                       (or the reverse). Readers that switch on the extension
                       silently skip it.
  C  UNPARSEABLE       a payload that decompresses but is not valid JSON.
  D  NEGATIVE OFFSET   trace points with a negative seconds-after-midnight,
                       i.e. positions belonging to the PREVIOUS UTC day. Naive
                       timestamping puts them on the wrong day.
  E  ORPHAN PAYLOAD    a payload with no .meta.json beside it -- no provenance,
                       so it can never be cited.
  F  ORPHAN META       a .meta.json claiming success with no payload beside it.
  G  EMPTY TRACE       a payload that parses but carries zero position points.

Nothing is deleted or rewritten by this script. It reports.

    python3 audit_data_integrity.py [--json]
"""
import glob, gzip, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
PLANES = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
GZIP_MAGIC = b"\x1f\x8b"


def read_payload(path):
    """Return (obj, container, note). Never trusts the file extension."""
    with open(path, "rb") as fh:
        head = fh.read(2)
    is_gz = head == GZIP_MAGIC
    named_gz = path.endswith(".gz")
    note = ""
    if is_gz != named_gz:
        note = ("GZIP BYTES UNDER A .json NAME" if is_gz
                else "PLAIN JSON UNDER A .gz NAME")
    try:
        opener = gzip.open if is_gz else open
        with opener(path, "rt") as fh:
            return json.load(fh), ("gzip" if is_gz else "plain"), note
    except Exception as e:
        return None, ("gzip" if is_gz else "plain"), (note + f" | UNPARSEABLE: {type(e).__name__}").strip(" |")


def main():
    findings = collections.defaultdict(list)
    payloads = sorted(
        glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*_trace_full.json"))
        + glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*_trace_full.json.gz")))
    metas = sorted(glob.glob(os.path.join(PLANES, "*", "data", "recovered", "*.meta.json")))

    for m in metas:
        try:
            json.load(open(m))
        except Exception as e:
            # A double-written file is recoverable: raw_decode reads the first object.
            salvage = None
            try:
                obj, idx = json.JSONDecoder().raw_decode(open(m).read())
                salvage = f"first object ends at byte {idx}; salvageable"
            except Exception:
                salvage = "not salvageable by raw_decode"
            findings["A_CORRUPT_META"].append(
                dict(path=os.path.relpath(m, PLANES), error=type(e).__name__, salvage=salvage))

    for p in payloads:
        obj, container, note = read_payload(p)
        rel = os.path.relpath(p, PLANES)
        if "GZIP BYTES UNDER" in note or "PLAIN JSON UNDER" in note:
            findings["B_CONTAINER_LIE"].append(dict(path=rel, note=note, readable=obj is not None))
        if obj is None:
            findings["C_UNPARSEABLE"].append(dict(path=rel, note=note))
            continue
        pts = obj.get("trace") or []
        if not pts:
            findings["G_EMPTY_TRACE"].append(dict(path=rel))
        neg = [q for q in pts if isinstance(q, list) and q and float(q[0]) < 0]
        if neg:
            findings["D_NEGATIVE_OFFSET"].append(
                dict(path=rel, points=len(neg), earliest_sec=min(float(q[0]) for q in neg),
                     total_points=len(pts)))
        if not os.path.exists(p + ".meta.json"):
            findings["E_ORPHAN_PAYLOAD"].append(dict(path=rel))

    payload_set = set(payloads)
    for m in metas:
        if m.endswith(".miss.json.meta.json"):
            continue
        target = m[: -len(".meta.json")]
        if target.endswith("_trace_full.json") or target.endswith("_trace_full.json.gz"):
            if target not in payload_set:
                findings["F_ORPHAN_META"].append(dict(path=os.path.relpath(m, PLANES)))

    # ---- HANDLED vs DANGEROUS ---------------------------------------------
    # Two of these conditions are properties of the ARCHIVE'S OWN FILES and can
    # never be "fixed" without altering evidence, which we do not do. What can
    # be fixed is whether our readers cope with them. A condition that every
    # reader handles correctly is not a finding; a condition that silently
    # corrupts a number is. This pass proves the handling rather than assuming
    # it, by re-reading the offending files through the real production reader.
    sys.path.insert(0, os.path.join(HERE, "lib"))
    import traces as _t                                             # noqa: E402
    handled, dangerous = collections.defaultdict(list), collections.defaultdict(list)
    for k, rows in findings.items():
        for r in rows:
            path = os.path.join(PLANES, r["path"])
            if k == "B_CONTAINER_LIE":
                rec = _t.visits_from_trace(path, "2000-01-01")
                ok = not rec.get("unreadable") and rec.get("trace_points")
                r["handled_by_reader"] = bool(ok)
                r["reader_sees_points"] = rec.get("trace_points")
                (handled if ok else dangerous)[k].append(r)
            elif k == "D_NEGATIVE_OFFSET":
                base = os.path.basename(path)
                day = base.split("_")[1]
                rec = _t.visits_from_trace(path, day)
                ok = rec.get("points_from_previous_utc_day", 0) == r["points"] and \
                     len(rec.get("actual_utc_dates") or []) >= 1
                r["straddle_detected_by_reader"] = bool(ok)
                r["true_utc_dates"] = rec.get("actual_utc_dates")
                (handled if ok else dangerous)[k].append(r)
            else:
                dangerous[k].append(r)

    print(f"payloads scanned: {len(payloads)}   meta files scanned: {len(metas)}", file=sys.stderr)
    if handled:
        print("\nHANDLED — condition present in the archive's files, and our readers cope:")
        for k in sorted(handled):
            print(f"  {k}: {len(handled[k])}")
            for r in handled[k][:8]:
                extra = (f"reader reads {r['reader_sees_points']} points"
                         if "reader_sees_points" in r
                         else f"true dates {r.get('true_utc_dates')}")
                print(f"     {r['path']}  ->  {extra}")
    findings = dangerous
    total = 0
    for k in sorted(findings):
        rows = findings[k]
        total += len(rows)
        print(f"\n{k}: {len(rows)}")
        for r in rows[:12]:
            print("   " + json.dumps(r))
        if len(rows) > 12:
            print(f"   ... and {len(rows) - 12} more")
    if not total:
        print("\nCLEAN — every payload on disk is readable through the production reader, "
              "correctly dated, and has provenance.")
    else:
        print(f"\n{total} integrity findings.")
    if "--json" in sys.argv:
        out = os.path.join(HERE, "..", "data", "analysis", "data_integrity.json")
        json.dump({k: v for k, v in findings.items()}, open(out, "w"), indent=1)
        print("wrote " + os.path.normpath(out), file=sys.stderr)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
