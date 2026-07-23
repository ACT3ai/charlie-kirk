#!/usr/bin/env python3
"""Generate the /Photos image-evidence pages from images/images.yaml.

Driven by image_planning/p_level2_update.md (navigation pages: the Level 2
landing page and every Level 3/4/5 cluster page — table of contents at the top,
two balanced columns, modeled on the site home page) and by
image_planning/p_yaml_to_site.md (the individual image pages). Writes:
  * site/docs/Photos/<cluster dirs>/overview.mdx        (cluster pages)
  * site/docs/Photos/<cluster dirs>/<Img_key>.mdx       (one page per image)
  * site/internals/static/img/evidence/<sha256>.<ext>   (served copies)
  * marked TOC section inside site/docs/Photos/overview.mdx
  * marked CSS block inside site/internals/src/css/custom.css
  * merged rows in pages.csv

Idempotent: pages are rewritten in full; static copies are skipped when the
target already exists. Run with --csv-only to refresh pages.csv line counts
after agents have enriched page bodies.
"""
import csv, glob, os, re, shutil, subprocess, sys, unicodedata
import yaml

ROOT = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")
THIS = os.path.join(ROOT, "image_planning")
HIER = os.path.join(ROOT, "images", "images.yaml")
DOCS = os.path.join(ROOT, "site", "docs")
PHOTOS = os.path.join(DOCS, "Photos")
STATIC = os.path.join(ROOT, "site", "internals", "static", "img", "evidence")
CSS = os.path.join(ROOT, "site", "internals", "src", "css", "custom.css")
PAGES_CSV = os.path.join(ROOT, "pages.csv")
LANDING = os.path.join(PHOTOS, "overview.mdx")

TOC_START = "{/* PHOTOS_TOC_START */}"
TOC_END = "{/* PHOTOS_TOC_END */}"
CSS_START = "/* CK_EVIDENCE_LAYOUT_START */"
CSS_END = "/* CK_EVIDENCE_LAYOUT_END */"

INVIS = re.compile(
    "[\\u0000-\\u0008\\u000b-\\u001f\\u007f-\\u009f\\u00a0\\u00ad\\u034f\\u061c"
    "\\u115f\\u1160\\u17b4\\u17b5\\u180b-\\u180e\\u2000-\\u200f\\u2028-\\u202f"
    "\\u205f-\\u206f\\u3000\\u3164\\ufe00-\\ufe0f\\ufeff\\uffa0\\ufff9-\\ufffb"
    "\\U000e0000-\\U000e007f]")
SPACELIKE = re.compile("[\\u00a0\\u2000-\\u200a\\u202f\\u205f\\u3000]")


def sanitize_prose(s):
    if not s:
        return ""
    s = SPACELIKE.sub(" ", s)
    s = INVIS.sub("", s)
    return re.sub(r"\s+", " ", s).strip()


def mdx_escape(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("{", "&#123;").replace("}", "&#125;")


def yq(s):
    """YAML-safe double-quoted scalar (JSON string is valid YAML)."""
    import json
    return json.dumps(s, ensure_ascii=True)


def first_sentence(s, cap=200):
    s = sanitize_prose(s)
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    out = m.group(1) if m else s
    return (out[: cap - 1] + "…") if len(out) > cap else out


# ---------- load pages.csv ----------
with open(PAGES_CSV, newline="") as f:
    rdr = csv.DictReader(f)
    CSV_FIELDS = rdr.fieldnames
    csv_rows = list(rdr)
for r in csv_rows:
    r.pop(None, None)  # rows with extra columns beyond the header
# Drop rows this generator owns (everything under site/docs/Photos/ except the
# landing page) so reruns mint the same deterministic keys instead of dodging
# their own previous rows.
GENERATED_PREFIX = "site/docs/Photos/"
LANDING_REL = "site/docs/Photos/overview.mdx"
csv_rows = [r for r in csv_rows
            if not (r["file_path"].startswith(GENERATED_PREFIX)
                    and r["file_path"] != LANDING_REL)]
csv_by_key = {r["page_key"]: r for r in csv_rows}
csv_by_file = {r["file_path"]: r for r in csv_rows}
known_urls = {r["url_path"] for r in csv_rows}


def _route_for(repo_path, csv_url):
    """Overview files really serve at /<dir>/overview even when pages.csv
    records the bare /<dir> path — always link the /overview route."""
    p = re.sub(r"^site/docs/", "", repo_path)
    p = re.sub(r"\.(mdx?|md)$", "", p)
    real = "/" + p
    if csv_url and csv_url != real and not real.endswith("/overview"):
        return csv_url
    return real


def site_page_link(repo_path):
    """site/docs/X/y.mdx -> (url, title) using pages.csv, else derived."""
    r = csv_by_file.get(repo_path)
    if r:
        return _route_for(repo_path, r["url_path"]), r["title"]
    return _route_for(repo_path, None), \
        repo_path.split("/")[-1].rsplit(".", 1)[0].replace("_", " ").replace("-", " ")


def level2_link(dirname):
    for ext in ("mdx", "md"):
        fp = f"site/docs/{dirname}/overview.{ext}"
        r = csv_by_file.get(fp)
        if r:
            return _route_for(fp, r["url_path"]), r["title"]
    return None


# ---------- load hierarchy ----------
with open(HIER) as f:
    data = yaml.safe_load(f)

nodes = []          # flat list of included cluster nodes
all_keys_seen = set()


# Deepest YAML cluster level walked. The tree currently bottoms out at
# level_7; the cap is a runaway guard, not a structural limit.
MAX_DEPTH = 7


def norm_key(k):
    k = re.sub(r"[^A-Za-z0-9_]", "_", k or "X")
    return k


# ---------- publish-time exclusion gate ----------
# Some entries in the hierarchy must never be published (private personal
# material swept into the mirror by accident, or content we will not show). The
# YAML is read-only to this generator, so the gate lives here and is re-applied
# on every run.
#
# THE BAN SET is the UNION of two sources (see the repo charter, "Banned Media"):
#   images/ban_images.csv            — the newer master, carries reason + a
#                                      true/false switch, so a row can un-ban.
#   image_planning/exclude_images.txt — the older one-sha256-per-line list.
# An item banned in EITHER gets no page and no served copy, and any page or
# static copy it already has is deleted.
EXCLUDE_FILE = os.path.join(THIS, "exclude_images.txt")
BAN_CSV = os.path.join(ROOT, "images", "ban_images.csv")
EXCLUDED = set()
BANNED_IDENTS = set()          # sha256 + cid + file_path forms, for CSV matching
UNBANNED_IDENTS = set()
if os.path.exists(EXCLUDE_FILE):
    with open(EXCLUDE_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if re.fullmatch(r"[0-9a-f]{64}", line):
                EXCLUDED.add(line)
if os.path.exists(BAN_CSV):
    with open(BAN_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ids = [str(row.get(k) or "").strip()
                   for k in ("sha256", "cid", "file_path")]
            ids = [i for i in ids if i]
            if not ids:
                continue
            if str(row.get("banned") or "").strip().lower() == "false":
                UNBANNED_IDENTS.update(ids)   # explicit un-ban; the row records it
            else:
                BANNED_IDENTS.update(ids)
BANNED_IDENTS -= UNBANNED_IDENTS
EXCLUDED -= UNBANNED_IDENTS
# A CSV row identified by sha256 also feeds the sha-keyed static purge below.
EXCLUDED |= {i for i in BANNED_IDENTS if re.fullmatch(r"[0-9a-f]{64}", i)}


def entry_is_banned(i):
    """True when this hierarchy entry matches a ban row by sha256, cid, or path."""
    for k in ("sha256", "cid", "file_path"):
        v = str(i.get(k) or "").strip()
        if v and v in BANNED_IDENTS:
            return True
    return False


# ---------- publish-time media-type gate: /Photos is STILL IMAGES ONLY ----------
# images/images.yaml carries video that an earlier revision of
# p_update_image_hierarchy.md harvested into it: `video:` items, plus `image:`
# items whose CID is really an .mp4. This generator used to render those with a
# <video> player on an Img_*.mdx page, which is how nine video pages came to be
# published inside the image hierarchy. Video belongs to the sibling pipeline:
# videos/videos.yaml -> site/docs/Videos, Vid_*.mdx, ck-video-* classes.
#
# The type test is kept — knowing which CIDs are videos is exactly what is
# needed — but it now SKIPS the entry instead of choosing different markup.
# There is deliberately no code path in this file that can emit <video>,
# <source>, <audio>, or a media-player <iframe>: a generator that can render a
# video will render one the next time a mistyped entry reaches it.
VIDEO_EXT = (".mp4", ".mov", ".webm", ".m4v", ".mkv", ".avi")
VIDEOS_YAML = os.path.join(ROOT, "videos", "videos.yaml")
VIDEO_MANIFEST = os.path.join(ROOT, "videos", "manifest.yaml")
IPFS_TXT = os.path.join(ROOT, "IPFS", "ipfs.txt")
VIDEOS_L2 = os.path.join(DOCS, "Videos")


def _cid(s):
    m = re.search(r"/ipfs/(\w+)", s or "") or re.search(r"^(Qm\w{44})$", (s or "").strip())
    return m.group(1) if m else ""


def load_video_cids():
    """CIDs known to be video.

    Every source is parsed by FILENAME, never by scraping CIDs wholesale — the
    video pipeline's records describe a mixed corpus, and a blanket scrape
    suppresses real images. Measured: scraping every CID out of these files
    typed 70 image entries as video when only 9 are.

    videos/videos.yaml is deliberately NOT consulted. Per
    videos_planning/CLAUDE.md it is still a schema shell whose data is the
    inherited IMAGE corpus — every cid in it currently describes an image.
    Add it here once the video pipeline has populated it for real.
    """
    cids = set()
    # 1a. videos/manifest.yaml — per-file records, filename + ipfs_cid.
    try:
        with open(VIDEO_MANIFEST, encoding="utf-8") as f:
            for rec in yaml.safe_load(f) or []:
                fn = (rec.get("filename") or "").lower()
                if fn.endswith(VIDEO_EXT) and rec.get("ipfs_cid"):
                    cids.add(rec["ipfs_cid"])
    except (OSError, yaml.YAMLError):
        pass
    # 1b. IPFS/ipfs.txt — blocks of `ipfs get <cid>` / `ipfs add "<filename>"`
    #     / `ipfs pin add <cid>`. It holds .jpg, .txt and .pdf entries too, so
    #     a block only contributes when its filename is a video.
    try:
        with open(IPFS_TXT, encoding="utf-8") as f:
            for block in re.split(r"\n\s*\n", f.read()):
                m = re.search(r'ipfs\s+add\s+"([^"]+)"', block)
                if m and m.group(1).lower().endswith(VIDEO_EXT):
                    cids.update(re.findall(r"\b(Qm[1-9A-HJ-NP-Za-km-z]{44})\b", block))
    except OSError:
        pass
    # 2. Site pages outside /Photos: a CID inside <video>/<source>, or any
    #    reference carrying a video extension, is a video.
    for dirpath, _d, files in os.walk(DOCS):
        if dirpath.startswith(PHOTOS) or dirpath.startswith(VIDEOS_L2):
            continue
        for fn in files:
            if not fn.endswith((".mdx", ".md")):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                    txt = f.read()
            except OSError:
                continue
            for tag in re.findall(r"<(?:video|source)\b.*?>", txt, re.S | re.I):
                c = _cid(tag)
                if c:
                    cids.add(c)
            for m in re.finditer(r"/ipfs/(\w+)[^\s\"'<>]*(?:%s)" % "|".join(
                    re.escape(e) for e in VIDEO_EXT), txt, re.I):
                cids.add(m.group(1))
    return cids


VIDEO_CIDS = load_video_cids()
SKIPPED_VIDEO = []      # entries skipped because they are video, not image


def entry_is_video(i):
    """True when a hierarchy entry is video rather than a still image.
    Extension wins; then the known-video CID set. An entry that cannot be
    typed is NOT assumed to be an image by this function — see skip_entry()."""
    for field in ("file_path", "ipfs_url", "cid"):
        v = (i.get(field) or "").strip()
        if v.lower().endswith(VIDEO_EXT):
            return True
        c = _cid(v)
        if c and c in VIDEO_CIDS:
            return True
    return False


def skip_entry(i):
    """Publish gate for one hierarchy entry. Returns a reason string to skip,
    or "" to publish. UNKNOWN is skipped, not published: every known bad entry
    is an extensionless IPFS CID with an empty sha256, and assuming that shape
    is an image is exactly what published the nine video pages."""
    if (i.get("sha256") or "") in EXCLUDED or entry_is_banned(i):
        return "excluded"
    if entry_is_video(i):
        return "video"
    if not (i.get("sha256") or "").strip() and not (i.get("file_path") or "").strip():
        # No local identity at all — only a CID. Publishable only if the CID is
        # positively known NOT to be a video, which means it must appear on the
        # site inside an <img>/![]() form somewhere. Otherwise it is UNKNOWN.
        c = _cid(i.get("ipfs_url") or i.get("cid") or "")
        if c and c not in IMAGE_CIDS:
            return "unknown-type"
    return ""


def load_image_cids():
    """CIDs positively observed on the site inside an image form."""
    cids = set()
    for dirpath, _d, files in os.walk(DOCS):
        if dirpath.startswith(PHOTOS) or dirpath.startswith(VIDEOS_L2):
            continue
        for fn in files:
            if not fn.endswith((".mdx", ".md")):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                    txt = f.read()
            except OSError:
                continue
            for tag in re.findall(r"<img\b.*?>", txt, re.S | re.I):
                c = _cid(tag)
                if c:
                    cids.add(c)
            for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", txt):
                c = _cid(m.group(1))
                if c:
                    cids.add(c)
    return cids - VIDEO_CIDS


IMAGE_CIDS = load_image_cids()


def walk(raw, depth, parents):
    node = {
        "key": norm_key(raw.get("_key", "")),
        "title": sanitize_prose(raw.get("title", "")) or raw.get("_key", ""),
        "depth": depth,
        "parents": parents,          # list of ancestor node dicts (nearest last)
        "site_level_2": raw.get("site_level_2") or [],
        "site_page": raw.get("site_page") or "",
        "children": [],
        "images": [],
        "rec_count": 0,
    }
    for im in raw.get("images") or []:
        i = im.get("image", im)
        why = skip_entry(i)
        if why:
            if why != "excluded":
                SKIPPED_VIDEO.append((why, node["key"],
                                      i.get("cid") or i.get("file_path") or "?"))
            continue
        node["images"].append(i)
    # `videos:` arrays are never published from this hierarchy at all. They are
    # counted so the run reports the contamination it is stepping over.
    for im in raw.get("videos") or []:
        i = im.get("video", im)
        SKIPPED_VIDEO.append(("video-array", node["key"],
                              i.get("cid") or i.get("file_path") or "?"))
    # Descend to whatever depth the YAML actually has. This used to stop at
    # level_5, which silently dropped every image filed deeper — the YAML holds
    # level_6 and level_7 nodes (e.g. Aircraft > MEMEs > Versions > SpyPlane_2).
    # Empty deep nodes still fall out later via included() / rec_count == 0.
    child_key = f"level_{depth + 1}" if depth < MAX_DEPTH else None
    if child_key:
        for c in raw.get(child_key) or []:
            ch = walk(c.get(child_key, c), depth + 1, parents + [node])
            node["children"].append(ch)
    node["rec_count"] = len(node["images"]) + sum(c["rec_count"] for c in node["children"])
    return node


tree = [walk(item["level_3"], 3, []) for item in data["level_3"]]


def included(n):
    return n["rec_count"] > 0


def collect(nlist):
    for n in nlist:
        if included(n):
            nodes.append(n)
            collect(n["children"])


collect(tree)

# assign dirs/urls/page keys
used_page_keys = set(csv_by_key)
for n in nodes:
    path_keys = [a["key"] for a in n["parents"] if included(a)] + [n["key"]]
    n["dir"] = os.path.join(PHOTOS, *path_keys)
    n["rel_dir"] = "Photos/" + "/".join(path_keys)
    n["url"] = "/" + n["rel_dir"] + "/overview"
    pk = "Photo_" + n["key"]
    while pk in used_page_keys:
        pk += "_P"
    used_page_keys.add(pk)
    n["page_key"] = pk

node_by_id = {id(n): n for n in nodes}

# ---------- stage static copies ----------
os.makedirs(STATIC, exist_ok=True)
copied = downscaled = skipped = 0
sha_ext = {}
sha_dims = {}
try:
    from PIL import Image
except ImportError:
    Image = None

EXT_NORM = {".jpeg": ".jpg"}
for n in nodes:
    for i in n["images"]:
        fp = i.get("file_path") or ""
        sha = i.get("sha256") or ""
        if not fp or not sha or sha in sha_ext:
            continue
        src = os.path.expanduser(fp)
        if not os.path.exists(src):
            continue
        ext = os.path.splitext(src)[1].lower()
        ext = EXT_NORM.get(ext, ext)
        big = os.path.getsize(src) > 2 * 1024 * 1024
        if big:
            ext = ".jpg"
        dst = os.path.join(STATIC, sha + ext)
        if not os.path.exists(dst):
            if big:
                subprocess.run(["sips", "-Z", "2000", "-s", "format", "jpeg",
                                "-s", "formatOptions", "85", src, "--out", dst],
                               check=True, capture_output=True)
                downscaled += 1
            else:
                shutil.copy2(src, dst)
                copied += 1
        else:
            skipped += 1
        sha_ext[sha] = ext
        if Image:
            try:
                with Image.open(dst) as img:
                    sha_dims[sha] = img.size
            except Exception:
                pass

# Media typing happens in the publish gate above (skip_entry / entry_is_video),
# before an entry ever reaches page generation. There is intentionally no
# is_video_src() here and no markup branch for video: /Photos publishes still
# images only, and video pages are generated into site/docs/Videos by the
# sibling pipeline from videos/videos.yaml.


# ---------- mint image page identities ----------
HASHY = re.compile(r"^(?=.*\d)[A-Za-z0-9\-]{8,}$")
DATEY = re.compile(r"^\d")


def strip_forbidden_wording(words):
    """Drop 'hand off' / 'handoff' from words derived off a source filename.

    Titles and slugs here are derived from the mirror's own filenames, and the
    mirror still uses the old 'Hand_Off' filing wording. Published pages must
    not: 'hand off' asserts a deliberate transfer between named living people,
    which is exactly the kind of factual accusation the repo's defamation rules
    forbid. The approved wording is 'Table and Charlie' / 'security team
    reaching Charlie'. Dropping the tokens usually leaves too few words, so the
    page falls back to the neutral '<cluster title> - Photo N' form.

    Only the 'hand off' pairing is forbidden. A standalone 'hand' is fine and
    must be kept -- a hand on a trigger, a hand in a product photo -- so this
    strips the adjacency and the closed-up spelling, nothing more.
    """
    out = []
    for w in words:
        lw = w.lower()
        if lw in ("handoff", "handsoff"):
            continue
        if lw == "off" and out and out[-1].lower() == "hand":
            out.pop()
            continue
        out.append(w)
    return out


def host_pages(i):
    """Other repo pages that embed this image, as repo-relative paths.

    Two schemas are in play. The hierarchy passes originally wrote
    on_site_pages: a flat list of repo-relative strings. A later pass renamed it
    to on_pages: a list of {page: <tilde-absolute path>} mappings. Read both --
    the YAML is written by more than one process, so assuming a single shape is
    how the 'Where This Image Appears' sections silently vanished once already.
    """
    out = []
    for hp in (i.get("on_pages") or []):
        p = hp.get("page") if isinstance(hp, dict) else hp
        if p:
            out.append(p)
    out.extend(i.get("on_site_pages") or [])
    rel = []
    for p in out:
        p = os.path.expanduser(str(p))
        if p.startswith(ROOT + os.sep):
            p = os.path.relpath(p, ROOT)
        if p not in rel:
            rel.append(p)
    return rel


def humanize_stem(fp):
    stem = os.path.splitext(os.path.basename(fp or ""))[0]
    words = [w for w in re.split(r"[_\-\s.]+", sanitize_prose(stem)) if w]
    good = [w for w in words
            if len(w) >= 3 and not HASHY.match(w) and not DATEY.match(w)
            and re.search(r"[A-Za-z]{3}", w) and w.lower() not in ("screenshot", "img", "image", "photo")]
    return strip_forbidden_wording(good)


img_pages = []       # dicts describing every image page
for n in nodes:
    prev = None
    for idx, i in enumerate(n["images"], 1):
        sha = i.get("sha256") or ""
        good = humanize_stem(i.get("file_path"))
        if len(good) >= 2:
            title = " ".join(w.replace("_", " ") for w in good)[:70]
        else:
            title = f"{n['title']} — Photo {idx}"
        base = "_".join(re.sub(r"[^A-Za-z0-9]", "", w) for w in good[:3]) or "Photo"
        key = f"Img_{base}_{sha[:6]}" if sha else f"Img_{base}_{n['key']}_{idx}"
        while key in used_page_keys:
            key += "_x"
        used_page_keys.add(key)
        pg = {
            "node": n, "img": i, "sha": sha, "key": key, "title": sanitize_prose(title),
            "idx": idx, "file": os.path.join(n["dir"], key + ".mdx"),
            "rel_file": "site/docs/" + n["rel_dir"] + "/" + key + ".mdx",
            "url": "/" + n["rel_dir"] + "/" + key,
        }
        img_pages.append(pg)
        prev = pg  # (prev/next threaded below, after the bypass set is known)

# ---------- single-image bypass (navigation only) ----------
# p_yaml_to_site.md: a cluster node whose whole subtree resolves to exactly ONE
# image page is BYPASSED in navigation. Parents/peers/landing link straight to
# that image page instead of the cluster page; the image page's back link points
# at the nearest NON-bypassed ancestor; prev/next put the image in that
# ancestor's sequence rather than alone. The bypassed cluster page is still
# generated, still gets its pages.csv row, and is never an orphan — only the
# links a visitor follows change. rec_count == 1 is exactly "subtree resolves to
# one image" (any included child would push the count to >= 2).
from collections import defaultdict

imgs_under = defaultdict(list)          # node id -> image pages anywhere below it
for pg in img_pages:
    imgs_under[id(pg["node"])].append(pg)
    for a in pg["node"]["parents"]:
        imgs_under[id(a)].append(pg)


def is_bypassed(n):
    return included(n) and n["rec_count"] == 1


def resolved_img(n):
    """The one image page a bypassed node resolves to."""
    return imgs_under[id(n)][0]


def nearest_visible(n):
    """The node a visitor is actually sent to for n: n itself when it is a real
    (non-bypassed) cluster, else its nearest non-bypassed ancestor, else None
    (the Photos landing page)."""
    if not is_bypassed(n):
        return n
    for a in reversed(n["parents"]):
        if included(a) and not is_bypassed(a):
            return a
    return None


# Home node of every image page: the visible cluster whose sequence it sits in.
for pg in img_pages:
    pg["home"] = nearest_visible(pg["node"])

# Rebuild prev/next so each image sits in its home cluster's visitor sequence:
# the images reachable directly from that cluster's TOC — its bypassed children
# (in child order) first, then its own images — chained in that order.
for pg in img_pages:
    pg.pop("prev", None)
    pg.pop("next", None)
for V in nodes:
    if is_bypassed(V):
        continue
    seq = [resolved_img(c) for c in V["children"]
           if included(c) and is_bypassed(c)]
    seq += [pg for pg in img_pages if pg["node"] is V]
    prev = None
    for pg in seq:
        if prev:
            prev["next"] = pg
            pg["prev"] = prev
        prev = pg

# ---------- page emit helpers ----------
BTN = ("style={{display:'inline-block', marginBottom:'1rem', "
       "padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff', "
       "borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}")


def back_button(url, label):
    return f"<a href=\"{url}\" {BTN}>← {mdx_escape(label)}</a>\n"


TOC_COLUMNS = 2


def toc_cols(items):
    """Balanced {TOC_COLUMNS}-column bullet list, in the site home page's idiom.

    Two columns rather than the home page's three: the main area on these pages
    is narrower, and two columns stay readable on a laptop.
    """
    if not items:
        return ""
    k = len(items)
    per = (k + TOC_COLUMNS - 1) // TOC_COLUMNS
    cols = [items[i:i + per] for i in range(0, k, per)] or [items]
    out = ['<div style={{ display: "flex", justifyContent: "space-between", gap: "2rem" }}>']
    for col in cols:
        out.append('<div style={{ flex: 1 }}>\n')
        for it in col:
            out.append(f"* {it}")
        out.append("\n</div>")
    out.append("</div>\n")
    return "\n".join(out)


def plural(n, word="image"):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


written = []

# ---------- preserve human/agent enrichment across reruns ----------
# A rerun refreshes structure (frontmatter mechanics, image block, TOCs, nav)
# but must NEVER discard prose an enrichment pass wrote. For an existing page
# we carry forward its title/labels/description and its authored prose section.
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def read_existing(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def fm_get(text, name):
    m = FM_RE.match(text or "")
    if not m:
        return None
    mm = re.search(rf"^{name}:\s*(.*)$", m.group(1), re.M)
    if not mm:
        return None
    v = mm.group(1).strip()
    if v.startswith('"') and v.endswith('"'):
        import json
        try:
            return json.loads(v)
        except Exception:
            return v[1:-1]
    return v


def section_body(text, heading):
    """Return the prose under '## heading' up to the next '## ', or None."""
    if not text:
        return None
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
                  text, re.S | re.M)
    if not m:
        return None
    body = m.group(1).strip()
    return body or None


def alt_of(text):
    if not text:
        return None
    m = re.search(r'<img className="ck-evidence-image"[^>]*?alt="([^"]*)"', text)
    return m.group(1) if m else None


BASELINE_CLUSTER_MARK = "This cluster collects the still images the investigation has filed under"


def emit(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    written.append(path)


# NOTE: there is deliberately no text_width() any more. The old layout pinned
# the image to the viewport with position:fixed and then hand-computed a prose
# column narrow enough to dodge it. layout_guidelines.txt rejects that: the
# image belongs in the page and the text wraps around it, so the float reserves
# its own space and the prose column is never capped.


# ---------- wide vs tall: reconciling full width with text wrap ----------
# layout_guidelines.txt, "RECONCILING FULL WIDTH WITH TEXT WRAP". The bounding
# box may take up to 85% of the main area, but an image that actually renders
# that wide leaves a gutter too narrow to read in. So each image gets one of two
# layouts, decided here from its intrinsic dimensions:
#
#   ck-evidence-wide  full-width block (up to 85%), prose resumes below it.
#   ck-evidence-tall  floats right, prose wraps beside it and resumes below.
#
# Both are in the document flow and both scroll with the page — the choice is
# about wrapping, never about anchoring.
#
# The arithmetic, on a reference desktop (1440px viewport, 300px sidebar, ~2rem
# padding each side -> main area ~1076px; height ceiling 100vh - navbar - 6rem
# -> ~744px):
#     rendered width = min(0.85 * 1076, 744 * aspect)
#     gutter         = 1076 - rendered width - 1.5rem margin
# A readable gutter is ~18rem (288px), which needs a rendered width <= ~764px,
# i.e. an aspect ratio at or below about 1.05. Landscape images are therefore
# width-limited and go full width; portrait and squarish images are
# height-limited, come out narrow on their own, and get the wrap.
WRAP_ASPECT_MAX = 1.05


def layout_class(sha):
    """'ck-evidence-tall' (float, text wraps) or 'ck-evidence-wide' (full width).

    Unknown dimensions (IPFS-only entries, missing files, video) default to
    wide: a full-width block is never wrong, whereas a wrong float squeezes the
    prose into an unreadable sliver.
    """
    dims = sha_dims.get(sha)
    if not dims or not dims[1]:
        return "ck-evidence-wide"
    return "ck-evidence-tall" if (dims[0] / dims[1]) <= WRAP_ASPECT_MAX \
        else "ck-evidence-wide"


# ---------- emit image pages ----------
for pg in img_pages:
    n, i, sha = pg["node"], pg["img"], pg["sha"]
    desc = sanitize_prose(i.get("ai_description") or "")
    ipfs = i.get("ipfs_url") or ""
    if sha in sha_ext:
        src = f"/img/evidence/{sha}{sha_ext[sha]}"
    elif ipfs:
        src = ipfs
    else:
        src = ""
    prior = read_existing(pg["file"])
    alt = first_sentence(desc, 160) or pg["title"]
    # JSX attribute value: no backslashes, no double quotes (yq's JSON escapes
    # are invalid inside an MDX/JSX string attribute)
    alt_attr = (alt_of(prior) or alt).replace("\\", "").replace('"', "'")
    fm_desc = first_sentence(desc, 200) or f"Image in the {n['title']} cluster of the Charlie Kirk investigation."
    # carry forward enrichment
    title = fm_get(prior, "title") or pg["title"]
    label = fm_get(prior, "sidebar_label") or pg["title"][:40]
    fm_desc = fm_get(prior, "description") or fm_desc
    pg["title"] = title
    lines = ["---",
             "displayed_sidebar: docs",
             f"slug: {pg['url']}",
             f"title: {yq(title)}",
             f"sidebar_label: {yq(label)}",
             f"description: {yq(fm_desc)}",
             "hide_table_of_contents: true",
             (f"ck_image_sha256: {sha}" if sha
              else f"ck_image_cid: {re.search(r'/ipfs/(\\w+)', ipfs).group(1) if re.search(r'/ipfs/(\\w+)', ipfs) else 'none'}"),
             f"ck_node_key: {n['key']}",
             "---", "",
             back_button(pg["home"]["url"] if pg["home"] else "/Photos/overview",
                         pg["home"]["title"] if pg["home"] else "Photos"),
             f"# {mdx_escape(pg['title'])}", ""]
    lay = layout_class(sha)
    if src:
        lines += [f"<a className=\"ck-evidence-image-wrap {lay}\" href=\"{src}\" "
                  f"target=\"_blank\" rel=\"noopener noreferrer\">",
                  f"  <img className=\"ck-evidence-image\" src=\"{src}\" alt=\"{alt_attr}\" />",
                  "</a>", ""]
    # No inline width cap. The image is a float in the page flow and the prose
    # wraps around it — see the CK_EVIDENCE_LAYOUT CSS block and
    # image_planning/layout_guidelines.txt.
    lines += ["<div className=\"ck-evidence-text\">", ""]
    lines += ["## What This Image Shows", ""]
    body = section_body(prior, "What This Image Shows") \
        or (mdx_escape(desc) if desc else
            "*Description pending — this image has not yet been written up.*")
    lines += [body, ""]
    if not src:
        lines += ["*Media pending — the image file for this entry is not yet hosted.*", ""]
    hosts = host_pages(i)
    if hosts:
        lines += ["## Where This Image Appears", "",
                  "This image is used on the following investigation page" + ("s" if len(hosts) > 1 else "") + ":", ""]
        for hp in hosts:
            u, t = site_page_link(hp)
            lines.append(f"* [{mdx_escape(t)}]({u})")
        lines.append("")
    rel = []
    for d in n["site_level_2"]:
        lk = level2_link(d)
        if lk:
            rel.append(f"[{mdx_escape(lk[1])}]({lk[0]})")
    home = pg["home"] or n
    lines += ["## Related Areas", "",
              f"* Cluster: [{mdx_escape(home['title'])}]({home['url']})"]
    for r in rel:
        lines.append(f"* Section: {r}")
    lines.append("* All photos: [Photos](/Photos/overview)")
    lines.append("")
    nav = []
    if pg.get("prev"):
        nav.append(f"* Previous: [{mdx_escape(pg['prev']['title'])}]({pg['prev']['url']})")
    if pg.get("next"):
        nav.append(f"* Next: [{mdx_escape(pg['next']['title'])}]({pg['next']['url']})")
    if nav:
        lines += ["## More In This Cluster", ""] + nav + [""]
    lines += ["</div>", ""]
    emit(pg["file"], "\n".join(lines))

# ---------- emit cluster pages ----------
for n in nodes:
    parent = next((a for a in reversed(n["parents"]) if included(a)), None)
    p_url = parent["url"] if parent else "/Photos/overview"
    p_title = parent["title"] if parent else "Photos"
    kids = [c for c in n["children"] if included(c)]
    own = [p for p in img_pages if p["node"] is n]
    peers = [s for s in (parent["children"] if parent else tree) if included(s) and s is not n]
    # Child clusters first (bolded, with their recursive count) so a visitor can
    # tell at a glance which links go deeper and which end at a picture. A
    # single-image child is BYPASSED: link straight to its image page instead of
    # to a cluster page whose entire TOC is one link.
    items = []
    for c in kids:
        if is_bypassed(c):
            ci = resolved_img(c)
            items.append(f"[{mdx_escape(ci['title'])}]({ci['url']}) — 1 image")
        else:
            items.append(f"**[{mdx_escape(c['title'])}]({c['url']})** — {plural(c['rec_count'])}")
    items += [f"[{mdx_escape(p['title'])}]({p['url']})" for p in own]
    # Cross-links out to the written pages this cluster mirrors: the node's
    # site_page first, then each site_level_2 section it covers.
    rel_links, seen_rel = [], set()
    if n["site_page"]:
        u, t = site_page_link(n["site_page"])
        rel_links.append((t, u))
        seen_rel.add(u)
    for d in n["site_level_2"]:
        lk = level2_link(d)
        if lk and lk[0] not in seen_rel:
            rel_links.append((lk[1], lk[0]))
            seen_rel.add(lk[0])
    fm_desc = (f"Photo cluster for {n['title']} in the Charlie Kirk investigation — "
               f"{n['rec_count']} images" + (f" across {len(kids)} sub-clusters" if kids else "") + ".")
    prior = read_existing(os.path.join(n["dir"], "overview.mdx"))
    fm_desc = fm_get(prior, "description") or fm_desc
    about_prior = section_body(prior, "About This Cluster")
    if about_prior and BASELINE_CLUSTER_MARK not in about_prior:
        about_body = about_prior          # enrichment pass wrote this — keep it
    else:
        about_body = "\n\n".join([
            f"This cluster collects the still images the investigation has filed under "
            f"**{mdx_escape(n['title'])}**. Every entry links to its own page, where the image is "
            f"shown at full size next to a written description of what it shows and how it connects "
            f"to the rest of the investigation. The images come from public sources - social media "
            f"posts, news coverage, official releases, and citizen research shared online.",
            f"Images are grouped here by concept rather than by date or source, so related images "
            f"sit together. Descriptions summarize what is visible and, where known, where the "
            f"image has been used elsewhere on this site. Claims that appear inside the images "
            f"themselves are the posters' claims, reported here with attribution rather than "
            f"adopted as conclusions.",
            f"Open any image above to start, then use the previous and next links on each image "
            f"page to walk the whole cluster without coming back to this list."
            + (" For the investigative context behind this area, see "
               + ", ".join(f"[{mdx_escape(t)}]({u})" for t, u in rel_links) + "."
               if rel_links else ""),
        ])
    lines = ["---",
             "displayed_sidebar: docs",
             f"slug: {n['url']}",
             f"title: {yq(n['title'])}",
             f"sidebar_label: {yq(n['title'][:40])}",
             f"description: {yq(fm_desc)}",
             f"ck_node_key: {n['key']}",
             "---", "",
             back_button(p_url, p_title),
             f"# {mdx_escape(n['title'])} — Photos", "",
             f"Photos filed under **{mdx_escape(n['title'])}** — {plural(len(own))} on this page"
             + (f" and {plural(len(kids), 'sub-cluster')} ({plural(n['rec_count'])} in total)" if kids else "") + ". "
             "Scan the list and open any image for the full picture and its write-up.", "",
             toc_cols(items),
             "## About This Cluster", "",
             about_body, "",
             "## Related Areas", ""]
    for t, u in rel_links:
        lines.append(f"* Written record: [{mdx_escape(t)}]({u})")
    lines.append(f"* Up: [{mdx_escape(p_title)}]({p_url})")
    if p_url != "/Photos/overview":     # on a Level 3, "up" already is Photos
        lines.append("* All photos: [Photos](/Photos/overview)")
    if peers:
        # Every peer, never a silent cap — inline so a wide peer set stays
        # compact instead of becoming a wall of bullets.
        peer_links = []
        for s in peers:
            if is_bypassed(s):
                si = resolved_img(s)
                peer_links.append(f"[{mdx_escape(si['title'])}]({si['url']})")
            else:
                peer_links.append(f"[{mdx_escape(s['title'])}]({s['url']})")
        lines += ["",
                  "**Peer clusters:** " + " · ".join(peer_links)]
    lines.append("")
    emit(os.path.join(n["dir"], "overview.mdx"), "\n".join(lines))

# ---------- landing page TOC ----------
with open(LANDING, encoding="utf-8") as f:
    landing = f.read()
# YAML order, not by size: the hierarchy file is the source of truth for the
# order the clusters are presented in.
l3 = [n for n in nodes if n["depth"] == 3]
total_imgs = sum(n["rec_count"] for n in l3)
toc = [TOC_START, "", "## Photo Clusters", "",
       f"The photo archive holds {plural(total_imgs)} filed into "
       f"{plural(len(l3), 'concept cluster')}. Open a cluster to see its images and its "
       "sub-areas; every image has its own page with a full-size view and a write-up.", "",
       toc_cols([(f"[{mdx_escape(resolved_img(n)['title'])}]({resolved_img(n)['url']}) — 1 image"
                  if is_bypassed(n) else
                  f"[{mdx_escape(n['title'])}]({n['url']}) — {plural(n['rec_count'])}")
                 for n in l3]),
       TOC_END]
block = "\n".join(toc)
# The table of contents leads the page: strip any earlier placement and re-insert
# it directly under the H1, above the prose.
landing = re.sub(re.escape(TOC_START) + r".*?" + re.escape(TOC_END) + r"\n*",
                 "", landing, flags=re.S)
m_h1 = re.search(r"^# .*$", landing, re.M)
if m_h1:
    cut = m_h1.end()
    landing = landing[:cut] + "\n\n" + block + "\n" + landing[cut:].lstrip("\n")
else:
    landing = landing.rstrip() + "\n\n" + block + "\n"
with open(LANDING, "w", encoding="utf-8") as f:
    f.write(landing)
written.append(LANDING)

# ---------- CSS ----------
css_block = f"""{CSS_START}
/* Image-evidence pages under /Photos. This block is the single implementation
   of image_planning/layout_guidelines.txt — that file is authoritative, this is
   generated from it by image_planning/generator/gen_photos_pages.py. Do not
   hand-edit; change the guidelines, change the generator, rerun.

     1. The image lives IN THE PAGE, not pinned to the browser window. It is in
        the document flow and scrolls up with the prose. Never position: fixed
        and never position: sticky here.
     2. The image is OPAQUE and paints above everything else. Transparent PNGs
        get an opaque backing so page text can never show through them.
     3. The prose WRAPS AROUND the image where there is a readable gutter, and
        resumes full width below it. Nothing flows under or over the image.
     4. Square corners. An image never loses its corners to a border radius.

   THE BOUNDING BOX. Width ceiling: up to 85% of the main area (the content
   column, sidebar excluded). Height ceiling: one screen, less the navbar and
   6rem of breathing room. The image scales inside the box preserving aspect
   ratio and whichever ceiling it meets first governs; it is never upscaled
   past its intrinsic size. A wide image hits the width ceiling and SHOULD take
   the full 85%. A tall image hits the height ceiling and comes out narrower
   than 85% on its own — that is correct, and it is not padded out.

   Sizing by the viewport is not anchoring to the viewport: the viewport says
   how big the box may be, then the box travels with the page.

   TWO LAYOUTS, chosen per image by the generator from its intrinsic aspect
   ratio (see layout_class()):
     .ck-evidence-wide  full-width block up to 85%, prose resumes below it —
                        used when a float would leave a gutter under ~18rem.
     .ck-evidence-tall  floats right, prose wraps beside it and below it. */
.ck-evidence-image-wrap {{
  display: block;
  position: relative;
  z-index: 3;
  width: fit-content;
  background: var(--ifm-background-surface-color, #fff);
  border-radius: 0;
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.35);
  overflow: hidden;
  line-height: 0;
  isolation: isolate;
}}
/* Wide / landscape: width-limited, so it takes the full 85% of the main area
   and the prose runs full width underneath rather than in a narrow gutter. */
.ck-evidence-image-wrap.ck-evidence-wide {{
  float: none;
  clear: both;
  margin: 0 auto 1.5rem auto;
  max-width: 85%;
}}
/* Tall / portrait / square: height-limited, so it comes out narrow on its own
   and leaves a readable column beside it. Float it and let the text wrap. */
.ck-evidence-image-wrap.ck-evidence-tall {{
  float: right;
  clear: right;
  margin: 0 0 1.25rem 1.5rem;
  max-width: 85%;
}}
.ck-evidence-image {{
  display: block;
  max-width: 100%;
  max-height: calc(100vh - var(--ifm-navbar-height, 60px) - 6rem);
  width: auto;
  height: auto;
  object-fit: contain;
  background: var(--ifm-background-surface-color, #fff);
  opacity: 1;
  border-radius: 0;
}}
/* The prose column is never width-capped: the image reserves its own space and
   the text flows around what is left. !important overrides the inline maxWidth
   that older generated pages still carry from the superseded pinned layout. */
.ck-evidence-text {{
  position: static;
  max-width: none !important;
}}
/* A heading must not be squeezed into the gutter beside a floated image. */
.ck-evidence-text > h2 {{
  overflow-wrap: break-word;
}}
/* Below the mobile breakpoint every image is a full-width block: a side-by-side
   float has no room to work at this width. */
@media (max-width: 996px) {{
  .ck-evidence-image-wrap,
  .ck-evidence-image-wrap.ck-evidence-wide,
  .ck-evidence-image-wrap.ck-evidence-tall {{
    float: none;
    clear: both;
    max-width: 100%;
    margin: 1rem 0;
  }}
  .ck-evidence-image {{
    max-height: none;
  }}
}}
{CSS_END}"""
with open(CSS, encoding="utf-8") as f:
    css = f.read()
if CSS_START in css:
    css = re.sub(re.escape(CSS_START) + r".*?" + re.escape(CSS_END), css_block, css, flags=re.S)
else:
    css = css.rstrip() + "\n\n" + css_block + "\n"
with open(CSS, "w", encoding="utf-8") as f:
    f.write(css)
written.append(CSS)

# ---------- pages.csv merge ----------
def linecount(p):
    with open(p, encoding="utf-8") as f:
        return sum(1 for _ in f)


def row(pk, parent, level, ptype, url, rel_file, title, label, directory, desc):
    return {"page_key": pk, "parent_key": parent, "level": str(level),
            "level2_parent": "Photos", "level2_section": "Photos", "page_type": ptype,
            "url_path": url, "file_path": rel_file, "title": title,
            "sidebar_label": label, "directory": directory, "extension": "mdx",
            "has_frontmatter": "yes", "line_count": str(linecount(os.path.join(ROOT, rel_file))),
            "description": desc}


new_rows = {}
for n in nodes:
    parent = next((a for a in reversed(n["parents"]) if included(a)), None)
    pk_parent = parent["page_key"] if parent else "Photos"
    rel_file = "site/docs/" + n["rel_dir"] + "/overview.mdx"
    new_rows[n["page_key"]] = row(
        n["page_key"], pk_parent, n["depth"], "topic", n["url"], rel_file,
        n["title"], n["title"][:40], n["rel_dir"],
        f"Photo cluster: {n['title']} — {n['rec_count']} images.")
for pg in img_pages:
    n = pg["node"]
    d = first_sentence(sanitize_prose(pg["img"].get("ai_description") or ""), 200) \
        or f"Image in the {n['title']} cluster."
    new_rows[pg["key"]] = row(
        pg["key"], n["page_key"], n["depth"] + 1, "image", pg["url"], pg["rel_file"],
        pg["title"], pg["title"][:40], n["rel_dir"], d)

merged, replaced = [], 0
for r in csv_rows:
    if r["page_key"] in new_rows:
        merged.append(new_rows.pop(r["page_key"]))
        replaced += 1
    else:
        merged.append(r)
merged.extend(new_rows.values())
with open(PAGES_CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore", restval="")
    w.writeheader()
    w.writerows(merged)

# ---------- purge any already-published copy of an excluded image ----------
# Excluding an image after it was published is the common case (the problem is
# usually noticed once the page exists), so actively remove the static file as
# well as the page. The page itself is caught by the orphan sweep below.
purged_static = []
for sha in EXCLUDED:
    for f in glob.glob(os.path.join(STATIC, sha + ".*")):
        os.remove(f)
        purged_static.append(os.path.basename(f))

# ---------- orphan sweep: generated files no longer expected ----------
# PROTECTED: pages already published under /Photos that carry a video player.
# Their entries are now skipped by the media-type gate, so the sweep would see
# them as orphans and delete them — but they are written, published pages with
# inbound links and no replacement under /Videos yet. Leave them byte-identical
# and report them. Migrating them to site/docs/Videos and only then withdrawing
# them from here is a separate, explicitly-approved job.
VIDEO_TAG = re.compile(r"<(?:video|source|audio)\b", re.I)
protected_video_pages = []
expected = {os.path.join(n["dir"], "overview.mdx") for n in nodes}
expected |= {pg["file"] for pg in img_pages}
expected.add(LANDING)
orphans = []
for dirpath, _dirs, files in os.walk(PHOTOS):
    for fn in files:
        fp = os.path.join(dirpath, fn)
        if not fn.endswith(".mdx") or fp in expected:
            continue
        try:
            with open(fp, encoding="utf-8") as f:
                if VIDEO_TAG.search(f.read()):
                    protected_video_pages.append(fp)
                    continue
        except OSError:
            pass
        orphans.append(fp)
for fp in orphans:
    os.remove(fp)
# prune now-empty dirs
for dirpath, dirs, files in sorted(((d, x, f) for d, x, f in os.walk(PHOTOS)),
                                   key=lambda t: -len(t[0])):
    if dirpath != PHOTOS and not os.listdir(dirpath):
        os.rmdir(dirpath)

# ---------- invisible-unicode validation ----------
bad = []
for p in written:
    with open(p, encoding="utf-8") as f:
        if INVIS.search(f.read()):
            bad.append(p)
if bad:
    print("FAIL: invisible unicode in:", bad[:10])
    sys.exit(1)

# ---------- link validation ----------
# Build the route table the way Docusaurus actually resolves routes: every
# doc file's path, plus `slug:` overrides, plus `id:` renames of the last
# segment, plus the bare form of a /overview page. Anything less produces
# false alarms (pages.csv records section overviews at their bare path).
def _site_routes():
    routes = set()
    for dirpath, _d, files in os.walk(DOCS):
        for fn in files:
            if not fn.endswith((".md", ".mdx")):
                continue
            full = os.path.join(dirpath, fn)
            base = "/" + os.path.splitext(os.path.relpath(full, DOCS))[0]
            routes.add(base)
            if base.endswith("/overview"):
                routes.add(base[: -len("/overview")])
            with open(full, encoding="utf-8", errors="replace") as fh:
                head = fh.read(1200)
            m = re.search(r"^slug:\s*(\S+)\s*$", head, re.M)
            if m:
                routes.add(m.group(1).strip().strip('"').rstrip("/"))
            else:
                mid = re.search(r"^id:\s*(\S+)\s*$", head, re.M)
                if mid:
                    routes.add(os.path.dirname(base) + "/"
                               + mid.group(1).strip().strip('"'))
    routes.add("/")
    return routes


gen_urls = _site_routes()
missing = set()
link_re = re.compile(r"\]\((/[^)#\s]+)")
for p in written:
    if not p.endswith(".mdx"):
        continue
    with open(p, encoding="utf-8") as f:
        for u in link_re.findall(f.read()):
            if u.startswith("/img/") or u.startswith("/pdf"):
                continue
            if u.rstrip("/") not in gen_urls:
                missing.add(u)

print("============================")
print("GENERATION COMPLETE")
print(f"Cluster pages: {len(nodes)}  Image pages: {len(img_pages)}")
print(f"Static: {copied} copied, {downscaled} downscaled, {skipped} already present")
print(f"pages.csv: {replaced} rows replaced, {len(merged) - len(csv_rows)} added, total {len(merged)}")
print(f"Orphan generated files removed: {len(orphans)}")
print(f"Excluded images: {len(EXCLUDED)} (static copies purged: {len(purged_static)})")

# ---------- media-type report: /Photos is still images only ----------
_by_why = {}
for why, key, ident in SKIPPED_VIDEO:
    _by_why.setdefault(why, []).append((key, ident))
print(f"Video/UNKNOWN entries skipped (not published): {len(SKIPPED_VIDEO)}"
      + ("  " + ", ".join(f"{w}={len(v)}" for w, v in sorted(_by_why.items())) if _by_why else ""))
print(f"Known video CIDs: {len(VIDEO_CIDS)}   confirmed image CIDs: {len(IMAGE_CIDS)}")
print(f"PROTECTED pre-existing /Photos pages carrying a video player: "
      f"{len(protected_video_pages)} (left in place, not orphaned)")
for fp in sorted(protected_video_pages):
    print(f"    {os.path.relpath(fp, ROOT)}")
_leaked = [f for f in written if f.startswith(PHOTOS) and f.endswith(".mdx")
           and VIDEO_TAG.search(open(f, encoding="utf-8").read())]
print(f"Media players emitted into /Photos this run: {len(_leaked)} (must be 0)")
if _leaked:
    print("FAIL: this generator wrote a media player into the image hierarchy.")
    for f in _leaked:
        print(f"    {os.path.relpath(f, ROOT)}")
    sys.exit(1)
print(f"Landing TOC rows: {len(l3)}")
print(f"Invisible-unicode scan: clean ({len(written)} files)")
print(f"Unresolvable internal links: {len(missing)}", sorted(missing)[:10])
print("============================")
