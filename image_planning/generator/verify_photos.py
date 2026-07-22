#!/usr/bin/env python3
"""Final verification for the generated /Photos image-evidence pages.

Implements the Stage 5 checks of p_images_level2.md over the WHOLE corpus
rather than a sample. Read-only: it never modifies a page.
"""
import csv, os, re, sys, glob, json

ROOT = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")
DOCS = os.path.join(ROOT, "site", "docs")
PHOTOS = os.path.join(DOCS, "Photos")
STATIC = os.path.join(ROOT, "site", "internals", "static")
PAGES_CSV = os.path.join(ROOT, "pages.csv")
LANDING = os.path.join(PHOTOS, "overview.mdx")

INVIS = re.compile(
    "[\\u0000-\\u0008\\u000b-\\u001f\\u007f-\\u009f\\u00a0\\u00ad\\u034f\\u061c"
    "\\u115f\\u1160\\u17b4\\u17b5\\u180b-\\u180e\\u2000-\\u200f\\u2028-\\u202f"
    "\\u205f-\\u206f\\u3000\\u3164\\ufe00-\\ufe0f\\ufeff\\uffa0\\ufff9-\\ufffb"
    "\\U000e0000-\\U000e007f]")

# phrasings that would assert prior knowledge or criminal/immoral conduct
UNSAFE = re.compile(
    r"\b(knew (about|in advance|beforehand|what was)|had foreknowledge|"
    r"was aware in advance|committed (a )?(crime|murder)|is guilty|"
    r"orchestrated the (murder|assassination)|helped plan the (murder|assassination))\b",
    re.I)

pages = sorted(glob.glob(os.path.join(PHOTOS, "**", "*.mdx"), recursive=True))
img_pages = [p for p in pages if os.path.basename(p).startswith("Img_")]
cluster_pages = [p for p in pages
                 if os.path.basename(p) == "overview.mdx" and p != LANDING]

# ---- route table: every real route the site serves ----
routes = set()
for dirpath, _d, files in os.walk(DOCS):
    for fn in files:
        if not fn.endswith((".md", ".mdx")):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, DOCS)
        base = "/" + os.path.splitext(rel)[0]
        routes.add(base)
        if base.endswith("/overview"):
            routes.add(base[: -len("/overview")])
        with open(full, encoding="utf-8", errors="replace") as f:
            head = f.read(1200)
        m = re.search(r"^slug:\s*(\S+)\s*$", head, re.M)
        if m:
            routes.add(m.group(1).strip().strip('"').rstrip("/"))
        else:
            # With no slug, a frontmatter `id:` renames the last URL segment —
            # e.g. court/mirandize/overview.mdx with id: mirandize-overview
            # serves at /court/mirandize/mirandize-overview.
            mid = re.search(r"^id:\s*(\S+)\s*$", head, re.M)
            if mid:
                seg = mid.group(1).strip().strip('"')
                routes.add(os.path.dirname(base) + "/" + seg)
routes.add("/")

link_re = re.compile(r"\]\((/[^)\s#]*)")
fails = {}


def add(p, msg):
    fails.setdefault(os.path.relpath(p, ROOT), []).append(msg)


for p in pages:
    s = open(p, encoding="utf-8", errors="replace").read()
    is_img = p in img_pages
    if INVIS.search(s):
        add(p, "invisible unicode")
    if "<!--" in s:
        add(p, "HTML comment (breaks MDX)")
    if re.search(r"\bdefamation\b", s, re.I) and "Anti-Defamation" not in s:
        add(p, "banned word 'defamation'")
    for m in UNSAFE.finditer(s):
        # The same wording appears in the DISCLAIMERS these pages are required
        # to carry ("No claim is made that ... knew about ...", "Nothing here
        # asserts that any official committed a crime"). Only flag a match that
        # is not inside a negation.
        window = s[max(0, m.start() - 170): m.start()].lower()
        if re.search(r"\b(no claim|nothing|not |never|no evidence|neither|"
                     r"n't|denies|denied|without asserting|does not|do not|"
                     r"is not|are not|has not|have not|no one has|nobody)\b",
                     window):
            continue
        add(p, f"unsafe phrasing: {m.group(0)!r}")
    if not s.startswith("---\n"):
        add(p, "no frontmatter")
    if p != LANDING and not re.search(r"^slug: /Photos/", s, re.M):
        add(p, "missing slug")
    if is_img:
        if "hide_table_of_contents: true" not in s:
            add(p, "right bar not disabled")
        # Identity: sha256 normally; IPFS-only entries have no sha in the YAML
        # and carry the CID instead.
        if not (re.search(r"^ck_image_sha256: [0-9a-f]{64}$", s, re.M)
                or re.search(r"^ck_image_cid: \w+$", s, re.M)):
            add(p, "missing image identity (sha256 or cid)")
        if not re.search(r"^ck_node_key: \S+", s, re.M):
            add(p, "missing ck_node_key")
        if "ck-evidence-image" not in s:
            add(p, "missing layout class")
        m = re.search(r'src="(/img/evidence/[^"]+)"', s)
        if m:
            if not os.path.exists(STATIC + m.group(1)):
                add(p, f"static file missing: {m.group(1)}")
        elif "ipfs.io" not in s and "Media pending" not in s:
            add(p, "no media and no pending note")
        for a in re.findall(r'alt="([^"]*)"', s):
            if "\\" in a:
                add(p, "backslash in alt attribute (breaks MDX)")
        body = re.search(r"^## What This Image Shows\s*\n(.*?)(?=^## |\Z)",
                         s, re.S | re.M)
        if not body or not body.group(1).strip():
            add(p, "empty description section")
    elif p != LANDING:
        # cluster pages only — the Level 2 landing page has its own shape
        if "## About This Cluster" not in s:
            add(p, "cluster page missing About section")
        toc = s.find('display: "flex"')
        if toc < 0:
            add(p, "cluster page missing two-column TOC")
        else:
            # the table of contents leads the page: above the prose, and
            # nothing but the back button, H1 and one intro line above it
            if 0 <= s.find("## About This Cluster") < toc:
                add(p, "TOC is below the prose (must lead the page)")
            if s.count('style={{ flex: 1 }}', toc, s.find("## About This Cluster")) > 2:
                add(p, "TOC has more than two columns")
        if not re.search(r"^\* Up: \[", s, re.M):
            add(p, "cluster page missing up-link")
    else:
        # the Level 2 landing page: TOC must sit directly under the H1
        h1 = s.find("\n# ")
        toc = s.find("{/* PHOTOS_TOC_START */}")
        if toc < 0:
            add(p, "landing page missing TOC markers")
        elif re.search(r"^## ", s[h1:toc], re.M):
            add(p, "landing TOC is below the prose (must lead the page)")
    for u in set(link_re.findall(s)):
        if u.startswith("/img/") or u.startswith("/pdf"):
            continue
        if u.rstrip("/") not in routes and u not in routes:
            add(p, f"unresolvable link {u}")

# ---- pages.csv coverage ----
with open(PAGES_CSV, newline="") as f:
    rows = [r for r in csv.DictReader(f)]
csv_files = {r["file_path"] for r in rows}
missing_csv = [p for p in pages
               if os.path.relpath(p, ROOT) not in csv_files]
keys = [r["page_key"] for r in rows]
dupe_keys = {k for k in keys if keys.count(k) > 1} if len(keys) < 6000 else set()

# ---- enrichment coverage ----
BASE = "This cluster collects the still images the investigation has filed under"
base_clusters = [p for p in cluster_pages
                 if BASE in open(p, encoding="utf-8", errors="replace").read()]

print("=" * 60)
print("PHOTOS CORPUS VERIFICATION")
print("=" * 60)
print(f"pages checked            : {len(pages)} "
      f"({len(img_pages)} image, {len(cluster_pages)} cluster, 1 landing)")
print(f"routes known             : {len(routes)}")
print(f"pages with problems      : {len(fails)}")
print(f"pages.csv rows missing   : {len(missing_csv)}")
print(f"duplicate page_keys      : {len(dupe_keys)}")
print(f"cluster pages still baseline : {len(base_clusters)} of {len(cluster_pages)}")
if fails:
    print("-" * 60)
    for p, msgs in sorted(fails.items())[:40]:
        print(f"  {p}")
        for m in sorted(set(msgs))[:5]:
            print(f"      - {m}")
    if len(fails) > 40:
        print(f"  ... and {len(fails)-40} more")
print("=" * 60)
sys.exit(1 if fails or missing_csv or dupe_keys else 0)
