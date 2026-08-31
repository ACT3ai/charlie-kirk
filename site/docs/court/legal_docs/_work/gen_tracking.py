#!/usr/bin/env python3
"""Regenerate tracking.txt for the State v. Robinson legal-document archive.

Walks the filings tree, pulls a description out of the extracted text for each
PDF, reconciles what we hold against the 867-entry docket index, and writes
tracking.txt. Safe to re-run: it rebuilds the file from the archive on disk.
"""
import hashlib, json, os, re, subprocess, collections

ROOT = "/Users/bryan/BGit/Bryan_git/charlie-kirk"
FIL  = ROOT + "/site/internals/static/court/filings"
LD   = ROOT + "/site/docs/court/legal_docs"
TXT  = LD + "/_text"
WORK = LD + "/_work"
OUT  = LD + "/tracking.txt"

SUBS = ["2025", "2026", "burkhart", "warrants", "mirandize", "transcripts", "misc", "analysis"]
LABEL = {
    "2025":       "Docket filings, Sept-Dec 2025",
    "2026":       "Docket filings, Jan-Apr 2026",
    "burkhart":   "Docket filings pulled from the Burkhart index (full docket, Sept 2025 - Aug 2026)",
    "warrants":   "Search warrants and supporting affidavits",
    "mirandize":  "Arrest / Miranda / probable-cause material",
    "transcripts":"Hearing transcripts",
    "misc":       "Other primary-source material",
    "analysis":   "NOT PRIMARY SOURCE - commentary and AI analysis, kept separate on purpose",
}

CAP_END = re.compile(r"(Case\s*No\.?\s*:?\s*251403576|Case Number\s*:?\s*251403576|"
                     r"Judge\s+Tony\s+F\.?\s+Graf|Hon\.\s*Tony\s+F\.?\s+Graf|Defendant\.?\s*\))", re.I)
NOISE   = re.compile(r"(pro hac vice|Telephone:|Facsimile:|Email:|Attorney for|"
                     r"Deputy Utah County Attorneys|#\s?\d{4,5}\b)", re.I)

def textpath(sub, fn):
    tsub = sub if sub in ("2025", "2026") else "other"
    return os.path.join(TXT, tsub, fn[:-4] + ".txt")

def describe(sub, fn):
    p = textpath(sub, fn)
    if not os.path.exists(p):
        return ""
    raw = open(p, errors="ignore").read()
    if not raw.strip():
        return ""
    ms = list(CAP_END.finditer(raw[:4000]))
    body = raw[ms[-1].end():] if ms else raw
    out, total = [], 0
    for ln in body.split("\n"):
        s = ln.strip()
        if len(s) < 3: continue
        if NOISE.search(s) and len(s) < 90: continue
        if re.fullmatch(r"[_\-=*/\\.:;,|\s]+", s): continue
        if len(s) < 25 and re.fullmatch(r"[A-Z\s,\.\)\(v]*", s): continue
        out.append(s); total += len(s)
        if total > 700: break
    return re.sub(r"\s+", " ", " ".join(out)).strip()[:480]

def filedate(fn):
    m = re.match(r"^\d{3}_(\d{4})-(\d{2})-(\d{2})_", fn)
    if m: return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.match(r"^(\d{1,2})_(\d{1,2})_(\d{2})_", fn)
    if m:
        try:
            return f"20{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
        except ValueError:
            return ""
    m = re.match(r"^(\d{4})-(\d{2})", fn)
    return m.group(0) if m else ""

def pages(p):
    try:
        info = subprocess.run(["pdfinfo", p], capture_output=True, text=True, timeout=60).stdout
        m = re.search(r"^Pages:\s+(\d+)", info, re.M)
        return int(m.group(1)) if m else None
    except Exception:
        return None

def collect():
    items = collections.OrderedDict()
    for sub in SUBS:
        d = os.path.join(FIL, sub)
        if not os.path.isdir(d): continue
        rows = []
        for fn in sorted(os.listdir(d)):
            if not fn.lower().endswith(".pdf"): continue
            p = os.path.join(d, fn)
            rows.append(dict(fn=fn, sub=sub, bytes=os.path.getsize(p), pages=pages(p),
                             date=filedate(fn), desc=describe(sub, fn),
                             sha=hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]))
        rows.sort(key=lambda r: (r["date"] or "9999", r["fn"]))
        items[sub] = rows
    return items

def main():
    items = collect()
    total = sum(len(v) for v in items.values())
    prim  = sum(len(v) for k, v in items.items() if k != "analysis")

    docket = []
    dj = os.path.join(WORK, "docket_867.json")
    if os.path.exists(dj):
        docket = json.load(open(dj))

    L = []
    w = L.append
    w("=" * 78)
    w("TRACKING - COURT DOCUMENT ARCHIVE")
    w("State of Utah v. Tyler James Robinson, Case No. 251403576")
    w("Fourth Judicial District Court, Utah County, Provo Department")
    w("Hon. Tony F. Graf, Jr.")
    w("=" * 78)
    w("")
    w("This file is the working index of every court document held in this repository.")
    w("It is regenerated from the archive on disk by:")
    w("    python3 site/docs/court/legal_docs/_work/gen_tracking.py")
    w("Re-run it after adding documents. Do not hand-edit the FILES HELD section; edit")
    w("the GAPS and ROUTES sections by hand, they are preserved narrative.")
    w("")
    w("WHERE THE FILES LIVE")
    w("  PDFs      site/internals/static/court/filings/<subdir>/")
    w("            served publicly at /court/filings/<subdir>/<name>.pdf")
    w("  Text      site/docs/court/legal_docs/_text/   (searchable text of every PDF,")
    w("            produced with pdftotext, or OCR for the scanned signed orders)")
    w("  Work      site/docs/court/legal_docs/_work/   (indexes, logs, docket data)")
    w("A PDF under site/docs/ is NOT served and 404s for every real visitor, which is")
    w("why the PDFs sit under site/internals/static/ instead.")
    w("")

    w("-" * 78)
    w("COMPLETENESS SCOREBOARD")
    w("-" * 78)
    if docket:
        dtot = len(docket)
        dpdf = sum(1 for r in docket if r["has_pdf"])
        dpriv = sum(1 for r in docket if r.get("private"))
        w(f"* Docket entries known to exist ................. {dtot}")
        w(f"* Of those, a PDF is publicly available for ..... {dpdf}")
        w(f"* Marked PRIVATE / sealed on the docket ......... {dpriv}")
        w(f"* Docket entries with no public copy anywhere ... {dtot - dpdf}")
        w("")
    w(f"* PDFs held in this archive (primary source) .... {prim}")
    w(f"* Plus commentary/analysis PDFs (not source) .... {total - prim}")
    w("")
    w("The docket is numbered continuously, so the entry count is the denominator for")
    w("'100% of the documents'. A large share of the missing entries are Returns of")
    w("Electronic Notification and other clerical entries with no substantive content;")
    w("the substantive gaps are listed under CONFIRMED GAPS below.")
    w("")

    w("-" * 78)
    w("FILES HELD")
    w("-" * 78)
    w("Format:  * <filename>")
    w("             <date> | <pages> pp | <bytes> | sha256:<first 12>")
    w("             <what the document says>")
    w("")
    for sub, rows in items.items():
        if not rows: continue
        w("")
        w(f"### {sub}/  -  {LABEL.get(sub, sub)}   ({len(rows)} files)")
        w("")
        for r in rows:
            w(f"* {r['fn']}")
            pp = f"{r['pages']} pp" if r["pages"] else "? pp"
            w(f"    {r['date'] or 'date unknown':<10} | {pp:>7} | {r['bytes']:>9} B | sha256:{r['sha']}")
            w(f"    {r['desc'] or '(no extractable text - see the PDF itself)'}")
        w("")

    # preserve hand-written sections if a previous tracking.txt had them
    keep = ""
    if os.path.exists(OUT):
        old = open(OUT, errors="ignore").read()
        i = old.find("CONFIRMED GAPS")
        if i > 0:
            keep = old[old.rfind("-" * 78, 0, i):]
    if keep:
        L.append(keep.rstrip())
    else:
        w("-" * 78)
        w("CONFIRMED GAPS")
        w("-" * 78)
        w("(hand-maintained - see _work/mislabeled_gaps.txt and the docket reconciliation)")
        w("")

    open(OUT, "w").write("\n".join(L) + "\n")
    print(f"wrote {OUT}: {total} files, {sum(1 for l in L)} lines")

if __name__ == "__main__":
    main()
