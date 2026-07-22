#!/usr/bin/env python3
# update_hierarchy.py — carries out p_update_image_hierarchy.md against
# images/images.yaml. Single-writer, grow-only, no duplicates.
#
# Does, in one coherent pass:
#   * Stage 3 (pin refresh)  — record real ipfs_pinned (bool) from the local node's
#     pinset; leave cid untouched (already computed).
#   * Stage 8 (on_pages)     — repo-wide reverse index: every OTHER page in the repo
#     that shows each image, resolved by evidence-filename(sha256) and IPFS CID.
#     Recovers the previously CORRUPTED on_pages (dicts stringified by the old
#     emitter) and merges. on_pages present on EVERY entry ([] when empty).
#   * Stage 9 (sidecars)     — ai_description_file / ocr_file / transcription_file
#     paths via the Large File Bridge mirror mapping; fill inline ai_description
#     from the sidecar Overview when empty.
#   * Stage 10 (image_page)  — bind each entry to its Level 5 page under
#     site/docs/Photos via ck_image_sha256 + ck_node_key frontmatter.
#   * Stage 11 (counts)      — number_of_images / _recursive / needs_split, integrity.
#   * Emit with the FIXED emitter (spec order; ipfs_pinned boolean; on_pages block
#     mappings; identity fields \uXXXX-escaped) + invisible-char validation.
#
# Reads site pages; never creates, renames, or edits them. Never touches
# sidebars.ts or pages.csv.
import os, re, sys, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sanitize_common import q_prose, q_identity, validate_no_invisible

HOME = os.path.expanduser('~')
ROOT = os.path.join(HOME, 'BGit/Bryan_git/charlie-kirk')
YAML_PATH = os.path.join(ROOT, 'images/images.yaml')
PHOTOS_DIR = os.path.join(ROOT, 'site/docs/Photos')
DOCS_DIR = os.path.join(ROOT, 'site/docs')
TILDE_ROOT = '~/BGit/Bryan_git/charlie-kirk'
PINSET = '/tmp/ck_pinset.txt'

MIRROR_TILDE = '~/_Mirror/Politics/Charlie_Kirk_Mi'
MIRROR_SIDECAR = os.path.join(HOME, 'BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi')
MIRROR_SIDECAR_LEGACY = os.path.join(ROOT, '.lfbridge/_Mirror/Politics/Charlie_Kirk_Mi')
REPO_SIDECAR = os.path.join(ROOT, '.lfbridge')

def expu(p): return os.path.expanduser(p) if p else p

# ============================================================ load
doc = yaml.safe_load(open(YAML_PATH, encoding='utf-8'))

def child_list(node):
    for k, v in node.items():
        if k.startswith('level_') and isinstance(v, list):
            yield int(k.split('_')[1]), v

# Walk every media inner dict, carrying (node_key, ancestor_chain).
def each_media(cb):
    def rec(items, lvl, chain):
        for it in items:
            node = it[f'level_{lvl}']
            key = node['_key']
            for kind in ('images', 'videos'):
                for m in (node.get(kind) or []):
                    inner = m.get('image') or m.get('video')
                    if inner is not None:
                        cb(inner, key, chain, node)
            for nl, arr in child_list(node):
                rec(arr, nl, chain + [key])
    rec(doc['level_3'], 3, [])

# ============================================================ indexes
sha_to_inners = {}
cid_to_shas = {}
def _idx(inner, key, chain, node):
    sha = (inner.get('sha256') or '').lower()
    if sha:
        sha_to_inners.setdefault(sha, []).append(inner)
    cid = inner.get('cid') or ''
    if cid and sha:
        cid_to_shas.setdefault(cid, set()).add(sha)
each_media(_idx)
print('='*28); print('INDEX')
print(f'unique sha256: {len(sha_to_inners)}   unique cid->sha: {len(cid_to_shas)}')

# ============================================================ Stage 3: pin refresh
pins = set(l.strip() for l in open(PINSET) if l.strip()) if os.path.exists(PINSET) else set()
pin_true = pin_false = 0
def _pin(inner, *a):
    global pin_true, pin_false
    cid = inner.get('cid') or ''
    val = bool(cid and cid in pins)
    inner['ipfs_pinned'] = val
    if val: pin_true += 1
    else: pin_false += 1
each_media(_pin)
print('='*28); print('STAGE 3 (pin refresh)')
print(f'Pinned on local node: {pin_true}   Not pinned: {pin_false}   (cid untouched)')

# ============================================================ Stage 9: sidecars
def sidecar_paths(file_path):
    """Return (ai, ocr, trans) tilde-rooted sidecar paths that EXIST, else ''."""
    if not file_path:
        return '', '', ''
    fp = file_path
    # mirror-rooted original
    bases = []
    if fp.startswith(MIRROR_TILDE):
        rel = fp[len(MIRROR_TILDE):].lstrip('/')
        bases.append((os.path.join(MIRROR_SIDECAR, rel),
                      f'~/BGit/Bryan_git/personal_large_files_bridge/_Mirror/Politics/Charlie_Kirk_Mi/{rel}'))
        bases.append((os.path.join(MIRROR_SIDECAR_LEGACY, rel),
                      f'~/BGit/Bryan_git/charlie-kirk/.lfbridge/_Mirror/Politics/Charlie_Kirk_Mi/{rel}'))
    elif fp.startswith(TILDE_ROOT):
        rel = fp[len(TILDE_ROOT):].lstrip('/')
        bases.append((os.path.join(REPO_SIDECAR, rel),
                      f'~/BGit/Bryan_git/charlie-kirk/.lfbridge/{rel}'))
    out = []
    for ext in ('ai_description', 'ocr', 'transcription'):
        found = ''
        for disk_base, tilde_base in bases:
            cand = disk_base + '.' + ext
            if os.path.isfile(cand):
                found = tilde_base + '.' + ext
                break
        out.append(found)
    return tuple(out)

def read_overview(ai_tilde):
    """readDesc() convention from gen_hierarchy.js: description body -> Overview para."""
    p = expu(ai_tilde)
    try:
        raw = open(p, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''
    i = raw.find('description:')
    if i < 0: return ''
    body = re.sub(r'^description:\s*[>|][-+]?\s*\n?', '', raw[i:])
    body = '\n'.join(re.sub(r'^ {2}', '', s) for s in body.split('\n')).strip()
    ov = re.sub(r'^##\s*Overview\s*\n', '', body, flags=re.I)
    ov = re.split(r'\n##\s', ov)[0].strip()
    return ov

s9 = {'ai': 0, 'ocr': 0, 'tr': 0, 'filled': 0, 'none': 0}
def _side(inner, *a):
    ai, ocr, tr = sidecar_paths(inner.get('file_path') or '')
    # never clear a valid existing value if recompute misses but old still on disk
    for key, val in (('ai_description_file', ai), ('ocr_file', ocr), ('transcription_file', tr)):
        if val:
            inner[key] = val
        else:
            old = inner.get(key) or ''
            inner[key] = old if (old and os.path.isfile(expu(old))) else ''
    if inner['ai_description_file']: s9['ai'] += 1
    if inner['ocr_file']: s9['ocr'] += 1
    if inner['transcription_file']: s9['tr'] += 1
    if not (inner.get('ai_description') or '').strip() and inner['ai_description_file']:
        ov = read_overview(inner['ai_description_file'])
        if ov:
            inner['ai_description'] = ov
            s9['filled'] += 1
    if not inner['ai_description_file'] and not inner['ocr_file'] and not inner['transcription_file']:
        s9['none'] += 1
each_media(_side)
print('='*28); print('STAGE 9 (sidecars)')
print(f'ai_description_file: {s9["ai"]}   ocr_file: {s9["ocr"]}   transcription_file: {s9["tr"]}')
print(f'inline descriptions filled from sidecar: {s9["filled"]}   entries with no sidecar: {s9["none"]}')

# ============================================================ Stage 8: on_pages
# on_pages records PUBLISHED PAGES that show the image — renderable page files
# under site/ (docs non-Photos, blog, src components). Data manifests
# (videos.csv, videos/manifest.yaml, Research/x_posts/*.yaml) merely LIST a CID;
# they are not pages that show the image, so they never go in on_pages.
PAGE_EXT = {'.md', '.mdx', '.html', '.tsx', '.jsx', '.js', '.ts'}
def valid_on_page(tilde_path):
    p = tilde_path
    if '/site/' not in p: return False
    if '/site/docs/Photos/' in p: return False
    if '/site/internals/static/' in p: return False
    return os.path.splitext(p)[1].lower() in PAGE_EXT

# 1) recover corrupted / prior on_pages values into a set of tilde page paths per inner.
def recover_on_pages(inner):
    got = set()
    for src_key in ('on_pages', 'on_site_pages'):
        v = inner.get(src_key)
        if not v: continue
        items = v if isinstance(v, list) else [v]
        for x in items:
            if isinstance(x, dict):
                p = x.get('page') or ''
            elif isinstance(x, str):
                m = re.search(r"'page':\s*'([^']+)'", x)      # stringified dict
                if m: p = m.group(1)
                elif x.startswith('~/'): p = x
                elif x.startswith('site/'): p = f'{TILDE_ROOT}/{x}'   # legacy repo-relative
                else: p = ''
            else:
                p = ''
            if p and valid_on_page(p): got.add(p)
    inner.pop('on_site_pages', None)
    return got

existing_pages = {}   # id(inner) -> set
def _rec_op(inner, *a):
    existing_pages[id(inner)] = recover_on_pages(inner)
each_media(_rec_op)
recovered_total = sum(len(s) for s in existing_pages.values())

# 2) repo-wide reverse sweep.
SKIP_DIRS = {'node_modules', 'build', '.git', '.docusaurus'}
TEXT_EXT = {'.md', '.mdx', '.html', '.tsx', '.jsx', '.ts', '.js', '.json', '.csv', '.yaml', '.yml'}
def in_scope(path):
    rel = os.path.relpath(path, ROOT)
    if rel.startswith('site/docs/Photos/'): return False          # images L2 itself
    if rel.startswith('site/internals/static/'): return False     # binaries
    if rel.startswith('image_planning/'): return False            # planning layer
    if rel == 'pages.csv': return False
    if rel.startswith('images/'): return False                    # the YAML + assets data
    if rel.startswith('.lfbridge/'): return False                 # sidecar data
    return True

RE_EVID = re.compile(r'/img/evidence/([0-9a-f]{64})')
RE_IPFS = re.compile(r'(?:ipfs\.io/ipfs/|ipfs://|dweb\.link/ipfs/)([A-Za-z0-9]{40,})'
                     r'|([A-Za-z0-9]{46,})\.ipfs\.dweb\.link')

files_read = 0
refs_found = 0
resolved_evid = resolved_cid = 0
unresolved = []
sweep_pages = {}   # sha256 -> set(tilde page path)

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        ext = os.path.splitext(fn)[1].lower()
        if ext not in TEXT_EXT: continue
        full = os.path.join(dirpath, fn)
        if not in_scope(full): continue
        try:
            txt = open(full, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        files_read += 1
        rel = os.path.relpath(full, ROOT)
        tilde_page = f'{TILDE_ROOT}/{rel}'
        record = valid_on_page(tilde_page)   # scan all for unresolved report, record only pages
        shas = set()
        for m in RE_EVID.finditer(txt):
            shas.add(m.group(1).lower()); refs_found += 1; resolved_evid += 1
        for m in RE_IPFS.finditer(txt):
            cid = m.group(1) or m.group(2)
            refs_found += 1
            got = cid_to_shas.get(cid)
            if got:
                shas |= got; resolved_cid += 1
            else:
                unresolved.append((rel, cid))
        if record:
            for sha in shas:
                if sha in sha_to_inners:
                    sweep_pages.setdefault(sha, set()).add(tilde_page)

# 3) merge recovered + swept onto every inner, set on_pages (always present).
op_nonempty = 0
op_bindings = 0
def _set_op(inner, key, chain, node):
    global op_nonempty, op_bindings
    sha = (inner.get('sha256') or '').lower()
    merged = set(existing_pages.get(id(inner), set()))
    if sha:
        merged |= sweep_pages.get(sha, set())
    merged = sorted(merged)
    inner['on_pages'] = [{'page': p} for p in merged]
    if merged:
        op_nonempty += 1
        op_bindings += len(merged)
each_media(_set_op)
print('='*28); print('STAGE 8 (on_pages)')
print(f'Files read: {files_read}   image references found: {refs_found}')
print(f'Resolved by evidence-filename(sha256): {resolved_evid}   by CID: {resolved_cid}')
print(f'Unresolved CID references: {len(unresolved)}')
print(f'Prior/corrupted on_pages recovered: {recovered_total}')
print(f'Entries with on_pages non-empty: {op_nonempty}   total page bindings: {op_bindings}')

# ============================================================ Stage 10: image_page
EXCLUDE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'exclude_images.txt')
EXCLUDED = set()
if os.path.exists(EXCLUDE_FILE):
    for line in open(EXCLUDE_FILE, encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if re.fullmatch(r'[0-9a-f]{64}', line):
            EXCLUDED.add(line)

TILDE_PHOTOS = f'{TILDE_ROOT}/site/docs/Photos'
pages_total = pages_with_sha = 0
pages_without = []
by_pair = {}
by_sha = {}
for dp, dn, fns in os.walk(PHOTOS_DIR):
    for fn in fns:
        if not fn.endswith('.mdx') or fn == 'overview.mdx':
            continue
        full = os.path.join(dp, fn)
        head = open(full, encoding='utf-8', errors='replace').read(4000)
        if not head.startswith('---'): continue
        fm = head.split('---', 2)[1] if head.count('---') >= 2 else ''
        m = re.search(r'^ck_image_sha256:\s*([0-9a-fA-F]{64})\s*$', fm, re.M)
        pages_total += 1
        if not m:
            pages_without.append(os.path.relpath(full, ROOT)); continue
        sha = m.group(1).lower()
        nk = re.search(r'^ck_node_key:\s*(\S+)\s*$', fm, re.M)
        nk = nk.group(1).strip('"\'') if nk else ''
        tilde = f'{TILDE_PHOTOS}/{os.path.relpath(full, PHOTOS_DIR)}'
        pages_with_sha += 1
        by_pair.setdefault((sha, nk), tilde)
        by_sha.setdefault(sha, []).append((nk, tilde))

ip = {'pair': 0, 'sha': 0, 'kept': 0, 'empty': 0, 'excluded': 0, 'vanished': []}
def _imgpage(inner, key, chain, node):
    sha = (inner.get('sha256') or '').lower()
    prev = inner.get('image_page') or ''
    if sha in EXCLUDED:
        inner['image_page'] = ''; ip['excluded'] += 1; ip['empty'] += 1; return
    val = ''
    if sha:
        if (sha, key) in by_pair:
            val = by_pair[(sha, key)]; ip['pair'] += 1
        else:
            cands = by_sha.get(sha) or []
            if len(cands) == 1:
                val = cands[0][1]; ip['sha'] += 1
            elif cands:
                for a in reversed(chain):
                    for nk, tp in cands:
                        if nk == a: val = tp; break
                    if val: break
                if val: ip['sha'] += 1
    if not val and prev:
        if os.path.isfile(expu(prev)):
            val = prev; ip['kept'] += 1
        else:
            ip['vanished'].append(prev); val = prev
    if not val:
        ip['empty'] += 1
    inner['image_page'] = val
each_media(_imgpage)
print('='*28); print('STAGE 10 (image_page)')
print(f'Photos pages indexed: {pages_total} ({pages_with_sha} with sha, {len(pages_without)} without)')
print(f'image_page by (sha,node): {ip["pair"]}   by sha only: {ip["sha"]}   kept prior: {ip["kept"]}')
print(f'image_page "": {ip["empty"]} (of which {ip["excluded"]} publish-excluded)')
print(f'Recorded pages now missing from disk: {len(ip["vanished"])}')

# ============================================================ Stage 11: counts / integrity
s11 = {'needs_split': 0}
def recount(items, lvl):
    total = 0
    for it in items:
        node = it[f'level_{lvl}']
        direct = len(node.get('images') or []) + len(node.get('videos') or [])
        sub = sum(recount(arr, nl) for nl, arr in child_list(node))
        node['number_of_images'] = direct
        node['number_of_images_recursive'] = direct + sub
        if direct > 12:
            node['needs_split'] = True; s11['needs_split'] += 1
        elif 'needs_split' in node:
            del node['needs_split']
        total += direct + sub
    return total
recount(doc['level_3'], 3)

seen, dupk, dupsha = set(), [], []
cnt = {}
def check(items, lvl):
    for it in items:
        node = it[f'level_{lvl}']
        cnt[lvl] = cnt.get(lvl, 0) + 1
        k = node['_key']
        if k in seen: dupk.append(k)
        seen.add(k)
        for kind in ('images', 'videos'):
            local = set()
            for m in (node.get(kind) or []):
                inner = m.get('image') or m.get('video')
                ident = (inner.get('sha256') or inner.get('ipfs_url') or '')
                if ident and ident in local: dupsha.append((k, ident[:12]))
                if ident: local.add(ident)
        for nl, arr in child_list(node):
            check(arr, nl)
check(doc['level_3'], 3)

# ============================================================ emit (FIXED)
MEDIA_ORDER = ['cid', 'ipfs_pinned', 'sha256', 'file_path', 'ai_description',
               'ai_description_file', 'ocr_file', 'transcription_file',
               'image_page', 'on_pages', 'ipfs_url', 'also_filed_in']
PROSE_FIELDS = {'title', 'ai_description'}
q = q_identity

out = []
for line in open(YAML_PATH, encoding='utf-8'):
    if line.startswith('#'): out.append(line.rstrip('\n'))
    else: break
if not out or not out[0].startswith('#'):
    out = ['# images.yaml — master image list / image evidence hierarchy for the Charlie Kirk site.']

def emit_media(m, pad):
    kind = 'image' if 'image' in m else 'video'
    inner = m[kind]
    out.append(f'{pad}- {kind}:')
    p2 = pad + '    '
    keys = MEDIA_ORDER + [k for k in inner if k not in MEDIA_ORDER]
    for k in keys:
        if k not in inner: continue
        v = inner[k]
        if k == 'ipfs_pinned':
            out.append(f'{p2}ipfs_pinned: {"true" if v else "false"}')
        elif k == 'on_pages':
            if v:
                out.append(f'{p2}on_pages:')
                for pg in v:
                    path = pg['page'] if isinstance(pg, dict) else pg
                    out.append(f'{p2}  - page: {q(path)}')
            else:
                out.append(f'{p2}on_pages: []')
        elif k == 'sha256':
            out.append(f'{p2}sha256: {v if v else chr(34)+chr(34)}')
        elif isinstance(v, list):
            if v: out.append(f'{p2}{k}: [{", ".join(q(x) for x in v)}]')
        elif k in PROSE_FIELDS:
            out.append(f'{p2}{k}: {q_prose(v)}')
        else:
            out.append(f'{p2}{k}: {q(v)}')

def emit_node(it, lvl, indent):
    node = it[f'level_{lvl}']
    pad = ' ' * indent
    out.append(f'{pad}- level_{lvl}:')
    p2 = pad + '    '
    out.append(f'{p2}title: {q_prose(node["title"])}')
    out.append(f'{p2}_key: {node["_key"]}')
    if 'site_level_2' in node:
        out.append(f'{p2}site_level_2: [{", ".join(q(x) for x in node["site_level_2"])}]')
    if node.get('site_page'):
        out.append(f'{p2}site_page: {q(node["site_page"])}')
    out.append(f'{p2}number_of_images: {node["number_of_images"]}')
    out.append(f'{p2}number_of_images_recursive: {node["number_of_images_recursive"]}')
    if node.get('needs_split'):
        out.append(f'{p2}needs_split: true   # over the 12 ceiling — split on a later pass')
    for kind in ('images', 'videos'):
        arr = node.get(kind) or []
        if not arr:
            if kind == 'images': out.append(f'{p2}images: []')
            continue
        out.append(f'{p2}{kind}:')
        for m in arr: emit_media(m, p2 + '  ')
    for nl, arr in child_list(node):
        if arr:
            out.append(f'{p2}level_{nl}:')
            for c in arr: emit_node(c, nl, indent + 6)

out.append('level_3:')
for it in doc['level_3']:
    emit_node(it, 3, 2)
open(YAML_PATH, 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# ============================================================ validate
re_doc = yaml.safe_load(open(YAML_PATH, encoding='utf-8'))
validate_no_invisible(YAML_PATH)

# round-trip: an escaped identity path resolves on disk
sample_ok = False
def _samp(inner, *a):
    global sample_ok
    if sample_ok: return
    fp = inner.get('file_path') or ''
    if fp and os.path.isfile(expu(fp)): sample_ok = True
# re-walk re_doc
def each_media2(cb):
    def rec(items, lvl):
        for it in items:
            node = it[f'level_{lvl}']
            for kind in ('images', 'videos'):
                for m in (node.get(kind) or []):
                    inner = m.get('image') or m.get('video')
                    if inner is not None: cb(inner)
            for nl, arr in child_list(node): rec(arr, nl)
    rec(re_doc['level_3'], 3)
each_media2(_samp)

print('='*28); print('STAGE 11 (counts/integrity)')
print(f'Nodes: ' + '  '.join(f'level_{k}: {v}' for k, v in sorted(cnt.items())))
print(f'needs_split nodes: {s11["needs_split"]}')
print(f'Duplicate _keys: {len(dupk)}   Duplicate sha256 within a node: {len(dupsha)}')
print(f'YAML re-parses: yes   invisible-char scan: clean   sample path resolves: {sample_ok}')
print('='*28)
