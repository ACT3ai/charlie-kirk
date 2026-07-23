#!/usr/bin/env python3
"""plan_should_be.py — Stage 11 of p_update_image_hierarchy.md.

should_be_on_pages: where each image OUGHT to appear. Reasoned, not observed.

This script owns the MECHANICAL half of the stage — the half that must be exact:

  build     Build the stat()-verified candidate page index, score every image
            against it, and write per-agent shortlist slices to /tmp. The
            topical selection itself is judgment and is done by the agents that
            read those slices; an agent may only ever return an index key.
  write     Merge agent rows back in. Rejects any row whose path is not a key of
            the candidate index, applies the defamation gate and the per-page
            load cap, unions in on_pages, re-stats every path, and writes the
            YAML once through the shared emitter (single writer).

Never creates, moves, or edits a page. Never touches sidebars.ts or pages.csv.
"""
import os, re, sys, csv, json, math, yaml, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sanitize_common import q_prose, q_identity, validate_no_invisible

HOME = os.path.expanduser('~')
ROOT = os.path.join(HOME, 'BGit/Bryan_git/charlie-kirk')
TILDE_ROOT = '~/BGit/Bryan_git/charlie-kirk'
YAML_PATH = os.path.join(ROOT, 'images/images.yaml')
DOCS_DIR = os.path.join(ROOT, 'site/docs')
PAGES_CSV = os.path.join(ROOT, 'pages.csv')
EXCLUDE_FILE = os.path.join(ROOT, 'image_planning/exclude_images.txt')
SLICE_DIR = '/tmp/ck_stage11'
N_AGENTS = 12
SHORTLIST = 14
PER_PAGE_CAP = 12

def expu(p): return os.path.expanduser(p) if p else p

# ---------------------------------------------------------------- yaml walk
def child_list(node):
    for k, v in node.items():
        if k.startswith('level_') and isinstance(v, list):
            yield int(k.split('_')[1]), v

def each_media(doc, cb):
    """cb(inner, node, chain) where chain is the list of ancestor nodes incl. self."""
    def rec(items, lvl, chain):
        for it in items:
            node = it[f'level_{lvl}']
            ch = chain + [node]
            for kind in ('images', 'videos'):
                for m in (node.get(kind) or []):
                    inner = m.get('image') or m.get('video')
                    if inner is not None:
                        cb(inner, node, ch)
            for nl, arr in child_list(node):
                rec(arr, nl, ch)
    rec(doc['level_3'], 3, [])

# ---------------------------------------------------------------- candidate index
def build_index():
    """THE candidate index. Every should_be_on_pages value must be a key of this
    dict, byte for byte. Sources: pages.csv + a filesystem walk (the CSV lags),
    unioned, then stat()-verified. Nothing outside it may ever be written."""
    meta = {}
    from_csv = from_fs = dropped = 0
    with open(PAGES_CSV, encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            rel = (r.get('file_path') or '').strip()
            if not rel.startswith('site/docs/'):
                continue
            full = os.path.join(ROOT, rel)
            tilde = f'{TILDE_ROOT}/{rel}'
            if not os.path.isfile(full):
                dropped += 1
                continue
            if tilde in meta:
                continue
            meta[tilde] = {
                'path': tilde, 'rel': rel,
                'title': (r.get('title') or '').strip(),
                'desc': (r.get('description') or '').strip(),
                'ptype': (r.get('page_type') or '').strip(),
                'level': (r.get('level') or '').strip(),
                'l2': (r.get('level2_section') or r.get('level2_parent') or '').strip(),
                'url': (r.get('url_path') or '').strip(),
            }
            from_csv += 1
    for dp, dn, fns in os.walk(DOCS_DIR):
        for fn in fns:
            if not fn.endswith(('.md', '.mdx')):
                continue
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, ROOT)
            tilde = f'{TILDE_ROOT}/{rel}'
            if tilde in meta:
                continue
            parts = rel.split('/')
            meta[tilde] = {'path': tilde, 'rel': rel,
                           'title': os.path.splitext(fn)[0].replace('_', ' ').replace('-', ' '),
                           'desc': '', 'ptype': '', 'level': '',
                           'l2': parts[2] if len(parts) > 3 else '', 'url': ''}
            from_fs += 1
    # scope exclusions (spec: never target Photos, never Topics3, never outside docs)
    for k in list(meta):
        rel = meta[k]['rel']
        if rel.startswith('site/docs/Photos/') or rel.startswith('site/docs/Topics3/'):
            del meta[k]
    return meta, from_csv, from_fs, dropped

# ---------------------------------------------------------------- text scoring
STOP = set('''a an the and or of to in on at for with by from as is are was were be been being
this that these those it its into over under about after before not no yes he she they them his
her their our your you we i s t re ve ll d m image images photo photos screenshot shows showing
shown view digital vertical horizontal frame background foreground text page document post
featuring features visible appears white black gray grey blue red green color colour picture
overview index page_key mdx md site docs'''.split())

def toks(s):
    return [w for w in re.findall(r'[a-z0-9]+', (s or '').lower())
            if len(w) > 2 and w not in STOP]

def read_head(path, n=1200):
    p = expu(path)
    try:
        return open(p, encoding='utf-8', errors='replace').read(n)
    except OSError:
        return ''

def read_ocr(path, n=1400):
    """The .ocr sidecar is a small YAML doc: metadata keys, then `text: |-` and
    the literal on-screen text indented under it. Only the text block is useful
    for matching — the metadata (source path, engine, timestamp) is noise that
    would otherwise dominate the term vector."""
    raw = read_head(path, n + 400)
    if not raw:
        return ''
    i = raw.find('text: |')
    if i < 0:
        return ''
    body = raw[raw.find('\n', i) + 1:]
    lines = [ln[2:] if ln.startswith('  ') else ln for ln in body.split('\n')]
    return ' '.join(l.strip() for l in lines if l.strip())[:n]

# ---------------------------------------------------------------- build
def cmd_build():
    doc = yaml.safe_load(open(YAML_PATH, encoding='utf-8'))
    index, n_csv, n_fs, n_drop = build_index()
    keys = list(index)

    excluded = set()
    if os.path.exists(EXCLUDE_FILE):
        for line in open(EXCLUDE_FILE, encoding='utf-8'):
            line = line.split('#', 1)[0].strip()
            if re.fullmatch(r'[0-9a-f]{64}', line):
                excluded.add(line)

    # ---- page term vectors
    page_toks = {}
    for k, m in index.items():
        url_words = re.sub(r'[/_\-]', ' ', m['rel'][len('site/docs/'):])
        page_toks[k] = collections.Counter(
            toks(m['title']) * 3 + toks(m['desc']) * 2 + toks(url_words) + toks(m['l2']))
    df = collections.Counter()
    for c in page_toks.values():
        df.update(c.keys())
    N = len(page_toks)
    idf = {w: math.log(1 + N / (1 + d)) for w, d in df.items()}
    inverted = collections.defaultdict(list)
    for k, c in page_toks.items():
        norm = math.sqrt(sum((v * idf.get(w, 0)) ** 2 for w, v in c.items())) or 1.0
        for w, v in c.items():
            inverted[w].append((k, v * idf.get(w, 0) / norm))

    # ---- collect entries
    entries = []
    def collect(inner, node, chain):
        sha = (inner.get('sha256') or '').lower()
        entries.append({'inner': inner, 'sha': sha, 'node': node, 'chain': chain})
    each_media(doc, collect)

    # ---- structural candidates: every ancestor node's site_page, self first
    def structural(e):
        out = []
        for node in reversed(e['chain']):
            sp = node.get('site_page') or ''
            if sp:
                t = f'{TILDE_ROOT}/{sp}' if not sp.startswith('~') else sp
                if t in index and t not in out:
                    out.append(t)
        # the level_3's site_level_2 dirs -> their overview pages
        for d in (e['chain'][0].get('site_level_2') or []):
            for cand in (f'{TILDE_ROOT}/site/docs/{d}/overview.mdx',
                         f'{TILDE_ROOT}/site/docs/{d}/overview.md'):
                if cand in index and cand not in out:
                    out.append(cand)
        return out

    os.makedirs(SLICE_DIR, exist_ok=True)
    rows = []
    for e in entries:
        inner = e['inner']
        if e['sha'] in excluded:
            continue                                   # defamation gate: never planned
        ocr = read_ocr(inner.get('ocr_file') or '', 1000)
        desc = (inner.get('ai_description') or '')
        mirror_dir = ''
        fp = inner.get('file_path') or ''
        if '/Charlie_Kirk_Mi/' in fp:
            mirror_dir = os.path.dirname(fp.split('/Charlie_Kirk_Mi/', 1)[1])
        chain_titles = ' '.join(n['title'] for n in e['chain'])
        qc = collections.Counter(
            toks(desc) + toks(ocr) * 2 + toks(chain_titles) * 2
            + toks(mirror_dir.replace('/', ' ').replace('_', ' ')) * 2)
        scores = collections.defaultdict(float)
        for w, v in qc.items():
            wt = v * idf.get(w, 0)
            if wt <= 0:
                continue
            for k, pv in inverted.get(w, ()):
                scores[k] += wt * pv
        struct = structural(e)
        for i, k in enumerate(struct):                 # structural prior
            scores[k] = scores.get(k, 0.0) + (2.5 if i == 0 else 1.2)
        top = sorted(scores.items(), key=lambda x: -x[1])[:SHORTLIST]
        cands = [k for k, _ in top]
        for k in struct:                               # structural always shortlisted
            if k not in cands:
                cands.append(k)
        rows.append({
            'sha': e['sha'],
            'node': e['node']['_key'],
            'node_title': e['node']['title'],
            'l3': e['chain'][0]['_key'],
            'mirror_dir': mirror_dir,
            'desc': re.sub(r'\s+', ' ', desc)[:420],
            'ocr': re.sub(r'\s+', ' ', ocr)[:320],
            'on_pages': [p['page'] for p in (inner.get('on_pages') or [])],
            'candidates': [{'p': k, 't': index[k]['title'][:70],
                            'd': index[k]['desc'][:130], 'lv': index[k]['level'],
                            'ty': index[k]['ptype']} for k in cands],
        })

    with open(os.path.join(SLICE_DIR, 'index.json'), 'w') as fh:
        json.dump(sorted(keys), fh)
    per = math.ceil(len(rows) / N_AGENTS)
    for i in range(N_AGENTS):
        chunk = rows[i * per:(i + 1) * per]
        if not chunk:
            continue
        with open(os.path.join(SLICE_DIR, f'slice_{i:02d}.json'), 'w') as fh:
            json.dump(chunk, fh, indent=1)
    print('=' * 28)
    print('STAGE 11 BUILD')
    print(f'Candidate index: {len(index)} pages ({n_csv} from pages.csv, {n_fs} from filesystem walk, {n_drop} dropped as non-existent)')
    print(f'Image entries: {len(entries)}   planned (not publish-excluded): {len(rows)}   excluded by exclude_images.txt: {len(entries) - len(rows)}')
    print(f'Slices written: {SLICE_DIR}/slice_00..{min(N_AGENTS, math.ceil(len(rows)/per))-1:02d}  ({per} entries each)')
    print('=' * 28)

# ---------------------------------------------------------------- write
def cmd_write():
    doc = yaml.safe_load(open(YAML_PATH, encoding='utf-8'))
    index, *_ = build_index()
    excluded = set()
    if os.path.exists(EXCLUDE_FILE):
        for line in open(EXCLUDE_FILE, encoding='utf-8'):
            line = line.split('#', 1)[0].strip()
            if re.fullmatch(r'[0-9a-f]{64}', line):
                excluded.add(line)

    # agent rows: {"sha": ..., "node": ..., "pages": [path, ...]}
    picks = collections.defaultdict(set)
    rejected = accepted = 0
    for fn in sorted(os.listdir(SLICE_DIR)):
        if not fn.startswith('out_') or not fn.endswith('.json'):
            continue
        for r in json.load(open(os.path.join(SLICE_DIR, fn))):
            for p in (r.get('pages') or []):
                if p in index:
                    picks[(r['sha'], r.get('node', ''))].add(p); accepted += 1
                else:
                    rejected += 1
    print(f'Agent rows: accepted {accepted} assignments, REJECTED {rejected} (path not in candidate index)')

    # per-page load: cap at PER_PAGE_CAP across the corpus, keep earliest-scored
    load = collections.Counter()
    overflow = collections.Counter()
    stats = collections.Counter()
    carried = new = 0
    total = 0
    nonempty = 0

    def apply(inner, node, chain):
        nonlocal carried, new, total, nonempty
        sha = (inner.get('sha256') or '').lower()
        if sha in excluded:
            inner['should_be_on_pages'] = []
            stats['excluded'] += 1
            return
        cur = set()
        for pg in (inner.get('should_be_on_pages') or []):
            p = pg.get('page') if isinstance(pg, dict) else pg
            if p in index:
                cur.add(p)
        sel = set(picks.get((sha, node['_key']), set())) | set(picks.get((sha, ''), set()))
        union_on = set()
        for pg in (inner.get('on_pages') or []):
            p = pg.get('page') if isinstance(pg, dict) else pg
            if p and p in index:
                union_on.add(p)
        want = cur | sel | union_on
        keep = []
        for p in sorted(want, key=lambda x: (x not in union_on, load[x], x)):
            if load[p] >= PER_PAGE_CAP and p not in union_on:
                overflow[p] += 1
                continue
            load[p] += 1
            keep.append(p)
        keep = sorted(keep)
        carried += len(union_on & set(keep))
        new += len(set(keep) - union_on)
        inner['should_be_on_pages'] = [{'page': p} for p in keep]
        total += len(keep)
        if keep:
            nonempty += 1
            stats[f'n{min(len(keep),5)}'] += 1
        else:
            stats['empty'] += 1
    each_media(doc, apply)

    # verify-before-write
    bad = []
    def check(inner, node, chain):
        for pg in (inner.get('should_be_on_pages') or []):
            p = pg['page']
            if ('...' in p or 'TODO' in p or 'TBD' in p or '<' in p or '>' in p
                    or not p.startswith('~/') or not p.endswith(('.md', '.mdx'))
                    or '/site/docs/Photos/' in p or '/site/docs/' not in p
                    or not os.path.isfile(expu(p))):
                bad.append(p)
    each_media(doc, check)
    if bad:
        raise SystemExit(f'STAGE 11 FAIL: {len(bad)} invalid should_be_on_pages paths, e.g. {bad[:5]}')

    emit(doc)

    # verify-after-write
    re_doc = yaml.safe_load(open(YAML_PATH, encoding='utf-8'))
    n_ok = 0; n_bad = []
    def recheck(inner, node, chain):
        nonlocal n_ok
        for pg in (inner.get('should_be_on_pages') or []):
            if os.path.isfile(expu(pg['page'])): n_ok += 1
            else: n_bad.append(pg['page'])
    each_media(re_doc, recheck)
    validate_no_invisible(YAML_PATH)
    if n_bad:
        raise SystemExit(f'STAGE 11 FAIL after write: {len(n_bad)} paths do not resolve')

    print('=' * 28)
    print('STAGE 11 COMPLETE')
    print(f'Image entries processed: {sum(stats.values())}')
    print(f'Entries with should_be_on_pages non-empty: {nonempty}   total page assignments: {total}')
    print(f'Assignments carried over from on_pages: {carried}   new assignments proposed: {new}')
    print(f'Entries left []: {stats["empty"]} ({stats["excluded"]} excluded by exclude_images.txt, '
          f'{stats["empty"] - stats["excluded"]} no topical match)')
    print(f'Distribution: 1 page {stats["n1"]}   2 {stats["n2"]}   3 {stats["n3"]}   4 {stats["n4"]}   5+ {stats["n5"]}')
    print(f'Pages over the {PER_PAGE_CAP}-image load (overflowed): {len(overflow)}   overflow assignments dropped: {sum(overflow.values())}')
    print(f'Path validation: {n_ok}/{n_ok} resolve to an existing file on disk — placeholders found: 0')
    print('=' * 28)

# ---------------------------------------------------------------- emitter
MEDIA_ORDER = ['cid', 'ipfs_pinned', 'sha256', 'file_path', 'ai_description',
               'ai_description_file', 'ocr_file', 'transcription_file',
               'image_page', 'on_pages', 'should_be_on_pages',
               'ipfs_url', 'also_filed_in']
PAGE_LIST_FIELDS = ('on_pages', 'should_be_on_pages')
PROSE_FIELDS = {'title', 'ai_description'}
q = q_identity

def emit(doc):
    out = []
    for line in open(YAML_PATH, encoding='utf-8'):
        if line.startswith('#'): out.append(line.rstrip('\n'))
        else: break

    def emit_media(m, pad):
        kind = 'image' if 'image' in m else 'video'
        inner = m[kind]
        out.append(f'{pad}- {kind}:')
        p2 = pad + '    '
        for k in MEDIA_ORDER + [k for k in inner if k not in MEDIA_ORDER]:
            if k not in inner: continue
            v = inner[k]
            if k == 'ipfs_pinned':
                out.append(f'{p2}ipfs_pinned: {"true" if v else "false"}')
            elif k in PAGE_LIST_FIELDS:
                if v:
                    out.append(f'{p2}{k}:')
                    for pg in v:
                        out.append(f'{p2}  - page: {q(pg["page"] if isinstance(pg, dict) else pg)}')
                else:
                    out.append(f'{p2}{k}: []')
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

if __name__ == '__main__':
    {'build': cmd_build, 'write': cmd_write}[sys.argv[1]]()
