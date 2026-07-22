#!/usr/bin/env python3
"""Generate the /Photos image-evidence pages from hierarchy_images.yaml.

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
HIER = os.path.join(THIS, "hierarchy_images.yaml")
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


def norm_key(k):
    k = re.sub(r"[^A-Za-z0-9_]", "_", k or "X")
    return k


# ---------- publish-time exclusion gate ----------
# Some entries in the hierarchy must never be published (private personal
# material swept into the mirror by accident). The YAML is read-only to this
# generator, so the gate lives here and is re-applied on every run.
EXCLUDE_FILE = os.path.join(THIS, "exclude_images.txt")
EXCLUDED = set()
if os.path.exists(EXCLUDE_FILE):
    with open(EXCLUDE_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if re.fullmatch(r"[0-9a-f]{64}", line):
                EXCLUDED.add(line)


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
        if (i.get("sha256") or "") in EXCLUDED:
            continue
        node["images"].append(i)
    child_key = {3: "level_4", 4: "level_5", 5: None}[depth]
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

# ---------- classify IPFS-only entries as image or video ----------
# Some hierarchy entries have no local file, only an ipfs_url, and a few of
# those CIDs are .mp4 videos. The YAML does not record media type, so learn it
# from how the CID is already embedded on the site's own (non-generated) pages:
# a CID inside <video>/<source> is a video, inside <img>/![]() an image.
def classify_ipfs_cids():
    blob = []
    for dirpath, _d, files in os.walk(DOCS):
        if dirpath.startswith(PHOTOS):
            continue
        for fn in files:
            if fn.endswith((".mdx", ".md")):
                try:
                    with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                        blob.append(f.read())
                except OSError:
                    pass
    blob = "\n".join(blob).lower()
    kind = {}
    for n in nodes:
        for i in n["images"]:
            u = i.get("ipfs_url") or ""
            m = re.search(r"/ipfs/(\w+)", u)
            if not m or m.group(1) in kind:
                continue
            cid = m.group(1)
            for occ in re.finditer(re.escape(cid.lower()), blob):
                ctx = blob[max(0, occ.start() - 300): occ.start() + 80]
                best = max([(ctx.rfind("<video"), "video"),
                            (ctx.rfind("<source"), "video"),
                            (ctx.rfind("<img"), "image"),
                            (ctx.rfind("!["), "image")])
                if best[0] >= 0:
                    kind[cid] = best[1]
                    break
    return kind


IPFS_KIND = classify_ipfs_cids()


def is_video_src(src):
    if src.lower().endswith((".mp4", ".webm", ".mov")):
        return True
    m = re.search(r"/ipfs/(\w+)", src or "")
    return bool(m) and IPFS_KIND.get(m.group(1)) == "video"


# ---------- mint image page identities ----------
HASHY = re.compile(r"^(?=.*\d)[A-Za-z0-9\-]{8,}$")
DATEY = re.compile(r"^\d")


def humanize_stem(fp):
    stem = os.path.splitext(os.path.basename(fp or ""))[0]
    words = [w for w in re.split(r"[_\-\s.]+", sanitize_prose(stem)) if w]
    good = [w for w in words
            if len(w) >= 3 and not HASHY.match(w) and not DATEY.match(w)
            and re.search(r"[A-Za-z]{3}", w) and w.lower() not in ("screenshot", "img", "image", "photo")]
    return good


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
    fm_desc = first_sentence(desc, 200) or f"Photo evidence in the {n['title']} cluster of the Charlie Kirk investigation."
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
             back_button(n["url"], n["title"]),
             f"# {mdx_escape(pg['title'])}", ""]
    lay = layout_class(sha)
    if src and is_video_src(src):
        lines += [f"<div className=\"ck-evidence-image-wrap ck-evidence-wide\">",
                  f"  <video className=\"ck-evidence-image\" controls preload=\"metadata\">",
                  f"    <source src=\"{src}\" type=\"video/mp4\" />",
                  f"    <a href=\"{src}\">Open the video</a>",
                  "  </video>",
                  "</div>", ""]
    elif src:
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
    hosts = i.get("on_site_pages") or []
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
    lines += ["## Related Areas", "",
              f"* Cluster: [{mdx_escape(n['title'])}]({n['url']})"]
    for r in rel:
        lines.append(f"* Section: {r}")
    lines.append("* All photo evidence: [Photos](/Photos/overview)")
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
    # tell at a glance which links go deeper and which end at a picture.
    items = [f"**[{mdx_escape(c['title'])}]({c['url']})** — {plural(c['rec_count'])}" for c in kids]
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
    fm_desc = (f"Photo evidence cluster for {n['title']} in the Charlie Kirk investigation — "
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
            f"Images are grouped here by concept rather than by date or source, so related evidence "
            f"sits together. Descriptions summarize what is visible and, where known, where the "
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
             f"# {mdx_escape(n['title'])} — Photo Evidence", "",
             f"Photo evidence filed under **{mdx_escape(n['title'])}** — {plural(len(own))} on this page"
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
        lines.append("* All photo evidence: [Photos](/Photos/overview)")
    if peers:
        # Every peer, never a silent cap — inline so a wide peer set stays
        # compact instead of becoming a wall of bullets.
        lines += ["",
                  "**Peer clusters:** "
                  + " · ".join(f"[{mdx_escape(s['title'])}]({s['url']})" for s in peers)]
    lines.append("")
    emit(os.path.join(n["dir"], "overview.mdx"), "\n".join(lines))

# ---------- landing page TOC ----------
with open(LANDING, encoding="utf-8") as f:
    landing = f.read()
# YAML order, not by size: the hierarchy file is the source of truth for the
# order the clusters are presented in.
l3 = [n for n in nodes if n["depth"] == 3]
total_imgs = sum(n["rec_count"] for n in l3)
toc = [TOC_START, "", "## Photo Evidence Clusters", "",
       f"The photo archive holds {plural(total_imgs)} filed into "
       f"{plural(len(l3), 'concept cluster')}. Open a cluster to see its images and its "
       "sub-areas; every image has its own page with a full-size view and a write-up.", "",
       toc_cols([f"[{mdx_escape(n['title'])}]({n['url']}) — {plural(n['rec_count'])}"
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
/* Image-evidence pages under /Photos — layout per
   image_planning/layout_guidelines.txt (that file is authoritative):

     1. The image lives IN THE PAGE, not pinned to the browser window. It is a
        float in the document flow, so it scrolls up with the prose. Never
        position: fixed and never position: sticky here.
     2. The image is OPAQUE and paints above everything else. Transparent PNGs
        get an opaque backing so page text can never show through them.
     3. The prose WRAPS AROUND the image — line boxes shorten beside the float
        and resume full width below it. Nothing flows under or over the image.

   The viewport still sets the BOUNDING BOX (so a tall image cannot occupy more
   than one screen), but the box travels with the page. */
.ck-evidence-image-wrap {{
  float: right;
  clear: right;
  display: block;
  position: relative;
  z-index: 3;
  margin: 0 0 1.25rem 1.5rem;
  max-width: min(55%, calc((100vw - var(--doc-sidebar-width, 300px)) * 0.55));
  background: var(--ifm-background-surface-color, #fff);
  border-radius: 4px;
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.35);
  overflow: hidden;
  line-height: 0;
  isolation: isolate;
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
  border-radius: 4px;
}}
/* The prose column is never width-capped: the float is what reserves the
   space, and the text wraps around it. !important overrides the inline
   maxWidth that older generated pages still carry. */
.ck-evidence-text {{
  position: static;
  max-width: none !important;
}}
/* A heading must not sit in the narrow gutter beside a tall image — give it a
   full line by clearing only when it would otherwise be squeezed. */
.ck-evidence-text > h2 {{
  overflow-wrap: break-word;
}}
@media (max-width: 996px) {{
  .ck-evidence-image-wrap {{
    float: none;
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
        f"Photo evidence cluster: {n['title']} — {n['rec_count']} images.")
for pg in img_pages:
    n = pg["node"]
    d = first_sentence(sanitize_prose(pg["img"].get("ai_description") or ""), 200) \
        or f"Photo evidence in the {n['title']} cluster."
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
expected = {os.path.join(n["dir"], "overview.mdx") for n in nodes}
expected |= {pg["file"] for pg in img_pages}
expected.add(LANDING)
orphans = []
for dirpath, _dirs, files in os.walk(PHOTOS):
    for fn in files:
        fp = os.path.join(dirpath, fn)
        if fn.endswith(".mdx") and fp not in expected:
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
print(f"Landing TOC rows: {len(l3)}")
print(f"Invisible-unicode scan: clean ({len(written)} files)")
print(f"Unresolvable internal links: {len(missing)}", sorted(missing)[:10])
print("============================")
