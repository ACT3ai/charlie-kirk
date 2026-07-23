#!/usr/bin/env python3
# gen_videos_pages.py — Stages 1-4 of p_yaml_to_site.md.
#
# Reads   {ROOT}/videos/videos.yaml            (the plan; READ ONLY)
# Writes  {ROOT}/site/docs/Videos/**           (cluster pages + Vid_*.mdx video pages)
#         {ROOT}/site/static/img/video_posters/*.jpg
#         the CK_VIDEO_LAYOUT + CK_PLACED_VIDEOS blocks of custom.css
#         the CK_VIDEOS_TOC block of site/docs/Videos/overview.mdx
#         {ROOT}/pages.csv rows for the pages it wrote
#
# VIDEOS ONLY, ADDITIVE ONLY. It never reads or writes {ROOT}/images,
# image_planning, site/docs/Photos, static/img/evidence, or any CK_PLACED_IMAGES
# / CK_EVIDENCE_LAYOUT marked block.
#
# NOTHING IS EVER PINNED. A player is emitted only for a CID that is actually
# pinned on this node (verified at run time); everything else gets its full page
# with a poster and an honest media-pending note.
import os, re, sys, csv, json, html, subprocess, unicodedata, shutil
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sanitize_video import sanitize_prose, sanitize_block, validate_no_invisible

HERE     = os.path.dirname(os.path.abspath(__file__))
ROOT     = os.path.expanduser('~/BGit/Bryan_git/charlie-kirk')
YAML     = os.path.join(ROOT, 'videos', 'videos.yaml')
SITE     = os.path.join(ROOT, 'site')
DOCS     = os.path.join(SITE, 'docs')
L2DIR    = os.path.join(DOCS, 'Videos')
L2PAGE   = os.path.join(L2DIR, 'overview.mdx')
POSTERS  = os.path.join(SITE, 'static', 'img', 'video_posters')
CSSFILE  = os.path.join(SITE, 'internals', 'src', 'css', 'custom.css')
PAGESCSV = os.path.join(ROOT, 'pages.csv')
EXCLUDE  = os.path.join(ROOT, 'videos_planning', 'exclude_videos.txt')
OUTJSON  = os.path.join(HERE, 'generated_pages.json')
IPFS     = '/opt/homebrew/bin/ipfs'
FFPROBE  = '/opt/homebrew/bin/ffprobe'
FFMPEG   = '/opt/homebrew/bin/ffmpeg'

PROTECTED = {'overview.mdx', 'buckley-carlson-kash-patel-valhalla.mdx', '_category_.json'}

# ------------------------------------------------------------------ helpers
def run(args, timeout=180):
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except Exception as e:
        return 1, '', str(e)

EMOJI_RE = re.compile(
    '[\U0001F000-\U0001FAFF\U00002190-\U000021FF\U00002300-\U000027BF'
    '\U00002B00-\U00002BFF\U0001F1E6-\U0001F1FF☀-⛿]')

def clean_title(s, limit=95):
    s = sanitize_prose(s or '')
    s = EMOJI_RE.sub('', s)
    s = re.sub(r'\s*\|\s*$', '', s)
    s = re.sub(r'\s{2,}', ' ', s).strip(' -—–·')
    # X-post titles arrive as "Author - post text ...". Keep the whole thing but
    # trim the trailing ellipsis noise.
    s = re.sub(r'\s*\.\.\.$', '', s)
    s = re.sub(r'\s*\[\d{6,}\]\s*$', '', s)
    if len(s) > limit:
        cut = s[:limit].rsplit(' ', 1)[0]
        s = cut.rstrip(' ,;:-') + '…'
    return s or 'Untitled clip'

def short_label(s, limit=42):
    s = clean_title(s, limit * 3)
    if len(s) > limit:
        s = s[:limit].rsplit(' ', 1)[0].rstrip(' ,;:-') + '…'
    return s

STOP = {'the','a','an','of','and','or','to','in','on','at','for','with','is','it',
        'this','that','was','were','by','from','as','be','not','i','you','he','she',
        'they','we','his','her','their','its','my','me','but','so','if','then','than'}

def mint_key(title, seed):
    t = EMOJI_RE.sub(' ', sanitize_prose(title or ''))
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    words = [w for w in re.split(r'[^A-Za-z0-9]+', t) if w]
    picked, seen = [], set()
    for w in words:
        lw = w.lower()
        if lw in STOP or lw in seen:
            continue
        seen.add(lw)
        picked.append(w[:1].upper() + w[1:])
        if len(picked) == 4:
            break
    if not picked:
        picked = ['Clip']
    return 'Vid_' + '_'.join(picked) + '_' + str(seed)[:7]

def esc_yaml(s):
    return '"' + sanitize_prose(s).replace('\\', '\\\\').replace('"', '\\"') + '"'

def first_sentences(s, n=2, limit=300):
    s = sanitize_prose(s or '')
    parts = re.split(r'(?<=[.!?])\s+', s)
    out = ' '.join(parts[:n]).strip()
    if len(out) > limit:
        out = out[:limit].rsplit(' ', 1)[0].rstrip(' ,;:-') + '…'
    return out

def rel_url(path):
    return '/' + os.path.relpath(path, DOCS)[:-4].replace(os.sep, '/')

def dur_human(d):
    if not d:
        return ''
    m = re.match(r'^(\d+):(\d+):(\d+)$', d.strip())
    if not m:
        return d.strip()
    h, mi, s = (int(x) for x in m.groups())
    return (f'{h}:{mi:02d}:{s:02d}' if h else f'{mi}:{s:02d}')

# ------------------------------------------------------------------ load YAML
import yaml as _yaml
print('loading videos.yaml ...', flush=True)
DATA = _yaml.safe_load(open(YAML, encoding='utf-8'))

excluded = set()
if os.path.exists(EXCLUDE):
    for line in open(EXCLUDE, encoding='utf-8'):
        line = line.split('#')[0].strip()
        if line:
            excluded.add(line)

class Node:
    __slots__ = ('lvl','key','title','raw','parent','kids','vids','rec','dirpath','page','bypass','bypass_target')
    def __init__(self, lvl, raw, parent):
        self.lvl, self.raw, self.parent = lvl, raw, parent
        self.key   = raw.get('_key')
        self.title = sanitize_prose(raw.get('title') or self.key)
        self.kids, self.vids = [], []
        self.rec = 0
        self.bypass = False
        self.bypass_target = None

nodes, roots = [], []
def build(items, lvl, parent):
    key = 'level_%d' % lvl
    out = []
    for it in items or []:
        raw = it.get(key) if isinstance(it, dict) and key in it else it
        n = Node(lvl, raw, parent)
        nodes.append(n)
        out.append(n)
        n.kids = build(raw.get('level_%d' % (lvl + 1)), lvl + 1, n)
    return out
roots = build(DATA['level_3'], 3, None)

# ------------------------------------------------- unique videos, owner nodes
seen_ident, videos = {}, []
dupes = 0
for n in nodes:
    for item in n.raw.get('videos') or []:
        v = item.get('video') if isinstance(item, dict) and 'video' in item else item
        ident = v.get('cid') or v.get('sha256') or v.get('file_path')
        if not ident:
            continue
        if ident in seen_ident:
            seen_ident[ident]['also_nodes'].append(n)
            dupes += 1
            continue
        rec = dict(v=v, owner=n, also_nodes=[], ident=ident)
        seen_ident[ident] = rec
        videos.append(rec)
        n.vids.append(rec)

# recursive counts recomputed from the tree, never trusted from the file
def recount(n):
    n.rec = len(n.vids) + sum(recount(k) for k in n.kids)
    return n.rec
for r in roots:
    recount(r)

# ------------------------------------------------------ exclusion + publishable
skipped_excluded = [r for r in videos
                    if (r['v'].get('cid') in excluded or r['v'].get('sha256') in excluded)]
for r in skipped_excluded:
    r['owner'].vids.remove(r)
videos = [r for r in videos if r not in skipped_excluded]
for r in roots:
    recount(r)

pub_nodes = [n for n in nodes if n.rec > 0]
empty_nodes = [n for n in nodes if n.rec == 0]

# ------------------------------------------------------------- paths and keys
for n in pub_nodes:
    chain, c = [], n
    while c is not None:
        chain.append(c.key)
        c = c.parent
    n.dirpath = os.path.join(L2DIR, *reversed(chain))
    n.page = os.path.join(n.dirpath, 'overview.mdx')

used_keys = set(n.key for n in pub_nodes)
for r in videos:
    v = r['v']
    seed = ''
    m = re.search(r'\[(\d{8,})\]', v.get('file_path') or '')
    if m:
        seed = m.group(1)
    if not seed:
        m = re.search(r'/(\d{8,})(?:_\d+)?\.\w+$', v.get('file_path') or '')
        if m:
            seed = m.group(1)
    if not seed:
        seed = (v.get('cid') or v.get('sha256') or 'x')[-12:]
    k = mint_key(v.get('title'), seed)
    base, i = k, 2
    while k in used_keys:
        k = f'{base}_{i}'; i += 1
    used_keys.add(k)
    r['key'] = k
    r['page'] = os.path.join(r['owner'].dirpath, k + '.mdx')
    r['url'] = rel_url(r['page'])

# ------------------------------------------------------------- bypass set
def resolve_single(n):
    """Return the one video rec a node's subtree resolves to, or None."""
    if n.rec != 1:
        return None
    if n.vids:
        return n.vids[0]
    for k in n.kids:
        got = resolve_single(k)
        if got:
            return got
    return None
for n in pub_nodes:
    tgt = resolve_single(n)
    if tgt is not None:
        n.bypass, n.bypass_target = True, tgt

# ------------------------------------------------------- pin status (run time)
print('reading local pin set ...', flush=True)
rc, out, _ = run([IPFS, 'pin', 'ls', '--type=recursive'], timeout=300)
PINNED = set(l.split()[0] for l in out.splitlines() if l.strip()) if rc == 0 else set()
print(f'  {len(PINNED)} recursive pins on the node', flush=True)

B32 = {}
def base32(cid):
    if cid in B32:
        return B32[cid]
    rc, o, _ = run([IPFS, 'cid', 'base32', cid], timeout=20)
    B32[cid] = o if rc == 0 and o else ''
    return B32[cid]

# -------------------------------------------------- probe + posters (parallel)
os.makedirs(POSTERS, exist_ok=True)

def probe_and_poster(r):
    v = r['v']
    fp = os.path.expanduser(v.get('file_path') or '')
    r['w'] = r['h'] = 0
    r['poster'] = ''
    r['assumed_ratio'] = False
    if not fp or not os.path.exists(fp) or v.get('media_present') != 'video':
        r['assumed_ratio'] = True
        return
    rc, o, _ = run([FFPROBE, '-v', 'error', '-select_streams', 'v:0',
                    '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', fp], 60)
    if rc == 0 and 'x' in o:
        try:
            w, h = o.split('\n')[0].split('x')[:2]
            r['w'], r['h'] = int(w), int(h)
        except Exception:
            pass
    if not r['w']:
        r['assumed_ratio'] = True
    sha = v.get('sha256') or ''
    if not sha:
        return
    dest = os.path.join(POSTERS, sha + '.jpg')
    if os.path.exists(dest):
        r['poster'] = '/img/video_posters/%s.jpg' % sha
        return
    rc, _, _ = run([FFMPEG, '-nostdin', '-y', '-ss', '3', '-i', fp, '-frames:v', '1',
                    '-vf', "scale='min(1600,iw)':-2", '-q:v', '4', dest], 180)
    if rc != 0 or not os.path.exists(dest):
        rc, _, _ = run([FFMPEG, '-nostdin', '-y', '-ss', '0', '-i', fp, '-frames:v', '1',
                        '-vf', "scale='min(1600,iw)':-2", '-q:v', '4', dest], 180)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        r['poster'] = '/img/video_posters/%s.jpg' % sha
    elif os.path.exists(dest):
        os.remove(dest)

print(f'probing {len(videos)} videos and extracting posters ...', flush=True)
with ThreadPoolExecutor(max_workers=6) as ex:
    list(ex.map(probe_and_poster, videos))
print('  posters on disk:', len([r for r in videos if r['poster']]), flush=True)

# ---------------------------------------------------------- playback decision
for r in videos:
    v = r['v']
    cid = (v.get('cid') or '').strip()
    plat = (v.get('source_platform') or '').lower()
    url = (v.get('source_url') or '').strip()
    r['mode'] = 'pending'
    r['embed_url'] = ''
    if plat in ('youtube', 'rumble') and url:
        if 'playlist' in url:
            r['mode'] = 'link'
        else:
            r['mode'] = 'thirdparty'
        r['embed_url'] = url
    elif cid and cid in PINNED:
        r['mode'] = 'ipfs'
    r['pending_reason'] = ''
    if r['mode'] == 'pending':
        if not cid:
            r['pending_reason'] = 'no-cid'
        elif v.get('media_present') == 'audio_only':
            r['pending_reason'] = 'audio-only'
        elif v.get('media_present') == 'none':
            r['pending_reason'] = 'no-media'
        else:
            r['pending_reason'] = 'unpinned'

# ------------------------------------------------------------------ templates
GEN_NOTE = ('{/* Generated by videos_planning/generator/gen_videos_pages.py from '
            'videos/videos.yaml. Structure between the CK_NAV markers is rewritten '
            'on every run; prose between the CK_PROSE markers is preserved. */}')

def yt_id(u):
    m = re.search(r'[?&]v=([A-Za-z0-9_-]{6,})', u) or re.search(r'youtu\.be/([A-Za-z0-9_-]{6,})', u)
    return m.group(1) if m else ''

def player_block(r):
    v = r['v']
    cid = (v.get('cid') or '').strip()
    poster = r['poster']
    wrap_mod = 'ck-video-wrap--full'
    if r['w'] and r['h'] and (r['w'] / r['h']) < 1.0:
        wrap_mod = 'ck-video-wrap--wrapped'
    ratio_note = ''
    if r['assumed_ratio'] and r['mode'] == 'ipfs':
        ratio_note = '\n{/* aspect ratio assumed 16:9 - no local copy to measure */}'
    if r['mode'] == 'ipfs':
        b32 = base32(cid)
        alt = ('\n    <source src="https://%s.ipfs.dweb.link/" type="video/mp4" />' % b32) if b32 else ''
        return (f'{ratio_note}\n<div className="ck-video-wrap {wrap_mod}">\n'
                f'  <video className="ck-video-media" controls preload="metadata"'
                + (f' poster="{poster}"' if poster else '') + '>\n'
                f'    <source src="https://ipfs.io/ipfs/{cid}" type="video/mp4" />{alt}\n'
                '    Your browser does not support the video tag.\n'
                '  </video>\n</div>\n')
    if r['mode'] == 'thirdparty':
        u = r['embed_url']
        if 'youtube' in u:
            vid = yt_id(u)
            src = f'https://www.youtube.com/embed/{vid}'
        else:
            src = u if '/embed/' in u else u
        return ('\n<div className="ck-video-wrap ck-video-wrap--full ck-video-wrap--embed">\n'
                f'  <iframe className="ck-video-media" src="{src}" title="Video" loading="lazy"\n'
                '          allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"\n'
                '          allowFullScreen></iframe>\n</div>\n')
    # pending
    lines = []
    if poster:
        lines.append('\n<div className="ck-video-wrap ck-video-wrap--full ck-video-wrap--pending">\n'
                     f'  <img className="ck-video-media" src="{poster}" alt="Frame from this video" loading="lazy" />\n'
                     '</div>\n')
    reason = r['pending_reason']
    if reason == 'unpinned':
        body = ('**Media pending.** This footage is held locally and has not yet been published '
                'to IPFS, so it cannot be played here yet. The write-up below is complete.  \n'
                f'CID (computed): `{v.get("cid")}`')
    elif reason == 'audio-only':
        body = ('**Media pending.** Only the audio of this item is held locally, and it has not '
                'yet been published, so there is nothing to play here yet. The write-up below is '
                'drawn from the transcript.')
    elif reason == 'no-cid':
        body = ('**Media pending.** No content identifier has been recorded for this item yet, '
                'so it cannot be played here. The write-up below is complete.')
    else:
        body = ('**Media pending.** The media for this item is not held locally and has not been '
                'published, so it cannot be played here. The write-up below is drawn from the '
                'records that describe it.')
    lines.append('\n:::note\n\n' + body + '\n\n:::\n')
    return ''.join(lines)

PAGE_TITLES = {}
def _load_page_titles():
    try:
        for row in csv.DictReader(open(PAGESCSV, encoding='utf-8')):
            fp = row.get('file_path') or ''
            if fp:
                PAGE_TITLES[os.path.join(ROOT, fp)] = row.get('title') or ''
    except Exception:
        pass
_load_page_titles()

def page_label(path):
    t = PAGE_TITLES.get(path, '')
    if not t:
        m = re.search(r'^title:\s*(.+)$', open(path, encoding='utf-8').read()[:2000], re.M)
        t = m.group(1).strip().strip('\'"') if m else ''
    return sanitize_prose(t) or rel_url(path)

def existing_fm(path):
    """Frontmatter of an existing page, or {}."""
    if not os.path.exists(path):
        return {}
    txt = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = re.match(r'^([A-Za-z0-9_]+):\s*(.*)$', line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"')
    return out

def extract_prose(path, marker='CK_PROSE'):
    if not os.path.exists(path):
        return None
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'\{/\* %s_START \*/\}(.*?)\{/\* %s_END \*/\}' % (marker, marker), txt, re.S)
    if not m:
        return None
    body = m.group(1)
    if 'CK_PROSE_BASELINE' in body:
        return None          # our own boilerplate — refresh it from current data
    return body.strip('\n')

# --------------------------------------------------------- video page write-up
def baseline_writeup(r):
    v = r['v']
    out = ['{/* CK_PROSE_BASELINE */}', '']
    out.append('## What This Video Shows')
    out.append('')
    desc = sanitize_block(v.get('ai_description') or '').strip()
    if desc:
        out.append(desc)
    else:
        out.append('A visual account of this clip has not been recorded yet.')
    out.append('')

    src_bits = []
    d = dur_human(v.get('duration'))
    if d:
        src_bits.append(f'Running time {d}.')
    plat = (v.get('source_platform') or '').lower()
    auth = sanitize_prose(v.get('source_author') or '')
    url = (v.get('source_url') or '').strip()
    if plat == 'x' and auth:
        src_bits.append(f'Captured from a post by {auth} on X.')
    elif plat == 'youtube':
        src_bits.append('Hosted on YouTube by its publisher, who can remove it at any time.')
    elif plat == 'rumble':
        src_bits.append('Hosted on Rumble by its publisher, who can remove it at any time.')
    elif plat == 'local':
        src_bits.append('Held in the investigation’s own capture archive.')
    if url:
        src_bits.append(f'Source: [{url}]({url})')
    if src_bits:
        out.append('### Where It Came From')
        out.append('')
        out.append(' '.join(src_bits))
        out.append('')

    people = sanitize_block(v.get('people_seen') or '').strip()
    if people and people.lower() not in ('no people appear.', 'none.', 'n/a'):
        out.append('### Who Appears')
        out.append('')
        out.append(people)
        out.append('')

    ost = sanitize_block(v.get('onscreen_text') or '').strip()
    if ost and ost.lower() not in ('none.', 'n/a', 'no on-screen text.'):
        out.append('### On-Screen Text')
        out.append('')
        out.append(ost)
        out.append('')

    tl = sanitize_block(v.get('shot_timeline') or '').strip()
    if tl:
        out.append('### Shot By Shot')
        out.append('')
        out.append(tl)
        out.append('')
    return '\n'.join(out).rstrip() + '\n'

def nav_block_video(r):
    n = r['owner']
    anc = n
    while anc is not None and anc.bypass:
        anc = anc.parent
    lines = ['{/* CK_NAV_START */}', '']

    appears = []
    for item in r['v'].get('on_pages') or []:
        p = item.get('page') if isinstance(item, dict) else str(item)
        p = os.path.expanduser(str(p).strip())
        if p.startswith(DOCS) and os.path.exists(p):
            appears.append(p)
    if appears:
        lines += ['## Where This Video Also Appears', '']
        for p in sorted(set(appears)):
            lines.append(f'* [{page_label(p)}]({rel_url(p)})')
        lines.append('')

    also = sorted({m.key: m for m in r['also_nodes'] if m.rec > 0}.values(), key=lambda x: x.title)
    if also:
        lines += ['## Also Filed Under', '']
        for m in also:
            tgt = rel_url(m.bypass_target['page']) if m.bypass else rel_url(m.page)
            lines.append(f'* [{m.title}]({tgt})')
        lines.append('')

    peers = [p for p in n.vids if p is not r]
    if peers:
        lines += ['## Other Videos In This Section', '']
        for p in peers[:12]:
            lines.append(f'* [{clean_title(p["v"].get("title"), 80)}]({p["url"]})')
        lines.append('')

    if anc is not None:
        lines += ['', f'[← Back to {anc.title}]({rel_url(anc.page)}) · '
                      f'[All video evidence](/Videos/overview)', '']
    else:
        lines += ['', '[← All video evidence](/Videos/overview)', '']
    lines += ['{/* CK_NAV_END */}']
    return '\n'.join(lines)

def write_video_page(r):
    v = r['v']
    old = existing_fm(r['page'])
    authored = old.get('ck_authored') == 'true'
    title = old.get('title') if authored and old.get('title') else clean_title(v.get('title'))
    label = old.get('sidebar_label') if authored and old.get('sidebar_label') else short_label(v.get('title'))
    prose = extract_prose(r['page']) or baseline_writeup(r)
    desc = (old.get('description') if authored and old.get('description')
            else first_sentences(v.get('ai_description') or v.get('manifest_description') or title, 2, 260))
    r['title'] = title
    fm = ['---',
          'title: ' + esc_yaml(title),
          'sidebar_label: ' + esc_yaml(label),
          'hide_table_of_contents: true',
          'description: ' + esc_yaml(desc),
          'ck_authored: ' + ('true' if authored else 'false'),
          'ck_video_cid: ' + esc_yaml(v.get('cid') or ''),
          'ck_video_sha256: ' + esc_yaml(v.get('sha256') or ''),
          'ck_node_key: ' + esc_yaml(r['owner'].key),
          '---', '']
    body = [GEN_NOTE, '', '# ' + title, '',
            player_block(r), '',
            '<div className="ck-video-text">', '',
            '{/* CK_PROSE_START */}', '', prose, '', '{/* CK_PROSE_END */}', '',
            nav_block_video(r), '',
            '</div>', '']
    txt = '\n'.join(fm + body)
    txt = re.sub(r'\n{4,}', '\n\n\n', txt)
    os.makedirs(os.path.dirname(r['page']), exist_ok=True)
    existed = os.path.exists(r['page'])
    open(r['page'], 'w', encoding='utf-8').write(txt)
    return existed

# ------------------------------------------------------------- cluster pages
def toc_rows_for(n):
    """(label, url, count) rows for a node's children, bypass applied."""
    rows = []
    for k in sorted([k for k in n.kids if k.rec > 0], key=lambda x: x.title):
        if k.bypass:
            t = k.bypass_target
            rows.append((clean_title(t['v'].get('title'), 80), t['url'], 1, 'video'))
        else:
            rows.append((k.title, rel_url(k.page), k.rec, 'cluster'))
    return rows

def baseline_cluster_prose(n):
    kids = [k for k in n.kids if k.rec > 0]
    bits = ['{/* CK_PROSE_BASELINE */}', '']
    what = f'This section collects the video evidence filed under **{n.title}**'
    if n.rec == 1:
        what += ' — one clip.'
    else:
        what += f' — {n.rec} clips'
        if kids:
            what += f' across {len(kids)} sub-section' + ('s' if len(kids) != 1 else '')
        what += '.'
    bits.append(what)
    bits.append('')
    sp = (n.raw.get('site_page') or '').strip()
    l2 = [s for s in (n.raw.get('site_level_2') or []) if s]
    if sp:
        p = os.path.expanduser(sp)
        p = p if os.path.isabs(p) else os.path.join(ROOT, sp)
        if os.path.exists(p) and p.startswith(DOCS):
            bits.append(f'The written analysis for this area lives at '
                        f'[{rel_url(p)}]({rel_url(p)}). The footage below is the '
                        'visual record behind it.')
            bits.append('')
    elif l2:
        bits.append('Related written analysis: ' +
                    ', '.join(f'[/{s}/overview](/{s}/overview)' for s in l2[:4]) + '.')
        bits.append('')
    bits.append('Each clip has its own page with the full write-up, the source it came '
                'from, and what the footage does and does not establish.')
    return '\n'.join(bits) + '\n'

def nav_block_cluster(n):
    lines = ['{/* CK_NAV_START */}', '']
    rows = toc_rows_for(n)
    clusters = [x for x in rows if x[3] == 'cluster']
    kidvids = [x for x in rows if x[3] == 'video']
    if clusters:
        lines += ['## Sub-Sections', '', '| Section | Videos |', '|---|---|']
        for label, url, cnt, _ in clusters:
            lines.append(f'| [{label}]({url}) | {cnt} |')
        lines.append('')
    own = list(n.vids) + []
    if own or kidvids:
        lines += ['## Videos In This Section', '', '| Video | Length | What it shows |', '|---|---|---|']
        for r in own:
            t = clean_title(r['v'].get('title'), 70)
            d = dur_human(r['v'].get('duration')) or '—'
            cap = first_sentences(r['v'].get('ai_description'), 1, 150).replace('|', '—')
            lines.append(f'| [{t}]({r["url"]}) | {d} | {cap} |')
        for label, url, cnt, _ in kidvids:
            lines.append(f'| [{label}]({url}) | — | — |')
        lines.append('')
    sibs = []
    parent_kids = [k for k in (n.parent.kids if n.parent else roots) if k.rec > 0 and k is not n]
    for k in sorted(parent_kids, key=lambda x: x.title):
        if k.bypass:
            t = k.bypass_target
            sibs.append((clean_title(t['v'].get('title'), 70), t['url'], 1))
        else:
            sibs.append((k.title, rel_url(k.page), k.rec))
    if sibs:
        lines += ['## Elsewhere In Video Evidence', '']
        lines.append(' · '.join(f'[{l}]({u})' for l, u, _ in sibs[:24]))
        lines.append('')
    up = rel_url(n.parent.page) if (n.parent and n.parent.rec > 0) else '/Videos/overview'
    upt = n.parent.title if (n.parent and n.parent.rec > 0) else 'All video evidence'
    lines += ['', f'[← Back to {upt}]({up})', '', '{/* CK_NAV_END */}']
    return '\n'.join(lines)

def write_cluster_page(n):
    old = existing_fm(n.page)
    authored = old.get('ck_authored') == 'true'
    prose = extract_prose(n.page) or baseline_cluster_prose(n)
    desc = (old.get('description') if authored and old.get('description') else
            (f'Video evidence filed under {n.title} in the Charlie Kirk investigation '
             f'— {n.rec} clip' + ('s' if n.rec != 1 else '') + ' with write-ups and sources.'))
    fm = ['---',
          'title: ' + esc_yaml(n.title),
          'sidebar_label: ' + esc_yaml(short_label(n.title)),
          'description: ' + esc_yaml(desc),
          'ck_authored: ' + ('true' if authored else 'false'),
          'ck_node_key: ' + esc_yaml(n.key),
          '---', '']
    body = [GEN_NOTE, '', '# ' + n.title, '',
            '{/* CK_PROSE_START */}', '', prose, '', '{/* CK_PROSE_END */}', '',
            nav_block_cluster(n), '']
    txt = re.sub(r'\n{4,}', '\n\n\n', '\n'.join(fm + body))
    os.makedirs(os.path.dirname(n.page), exist_ok=True)
    existed = os.path.exists(n.page)
    open(n.page, 'w', encoding='utf-8').write(txt)
    return existed

# ------------------------------------------------------------------ emit
print('writing cluster pages ...', flush=True)
c_new = c_old = 0
for n in pub_nodes:
    if write_cluster_page(n): c_old += 1
    else: c_new += 1
print('writing video pages ...', flush=True)
v_new = v_old = 0
for r in videos:
    if write_video_page(r): v_old += 1
    else: v_new += 1

# ------------------------------------------------------------- orphan sweep
keep = set(n.page for n in pub_nodes) | set(r['page'] for r in videos)
orphans = []
for dirpath, dirnames, filenames in os.walk(L2DIR):
    for f in filenames:
        p = os.path.join(dirpath, f)
        if dirpath == L2DIR and f in PROTECTED:
            continue
        if f == '_category_.json':
            continue
        if p not in keep:
            orphans.append(p)
for p in orphans:
    os.remove(p)
for dirpath, dirnames, filenames in os.walk(L2DIR, topdown=False):
    if dirpath != L2DIR and not os.listdir(dirpath):
        os.rmdir(dirpath)


# ------------------------------------------------------------------ CSS block
CSS_VIDEO = """/* CK_VIDEO_LAYOUT_START */
/* Owned by videos_planning/generator/gen_videos_pages.py. Implements
   videos_planning/layout_guidelines.txt. Do not hand-edit; do not write into
   the CK_EVIDENCE_LAYOUT or CK_PLACED_IMAGES blocks from the videos pipeline. */
.ck-video-wrap {
  position: static;
  display: block;
  margin: 0 0 1.25rem 0;
  padding: 0;
  border-radius: 0;
  background: var(--ifm-background-color);
  opacity: 1;
  z-index: 1;
  line-height: 0;
}
.ck-video-wrap .ck-video-media {
  display: block;
  border-radius: 0;
  background: #000;
  opacity: 1;
  max-width: 100%;
  max-height: calc(100vh - var(--ifm-navbar-height, 60px) - 6rem);
}
.ck-video-wrap--full {
  width: 85%;
  max-width: 85%;
  clear: both;
}
.ck-video-wrap--full .ck-video-media {
  width: 100%;
  height: auto;
}
.ck-video-wrap--wrapped {
  float: left;
  width: auto;
  max-width: 45%;
  margin: 0 1.75rem 1rem 0;
}
.ck-video-wrap--wrapped .ck-video-media {
  width: auto;
  height: calc(100vh - var(--ifm-navbar-height, 60px) - 6rem);
  max-width: 100%;
}
.ck-video-wrap--embed {
  aspect-ratio: 16 / 9;
}
.ck-video-wrap--embed .ck-video-media {
  width: 100%;
  height: 100%;
  border: 0;
}
.ck-video-wrap--pending .ck-video-media {
  width: 100%;
  height: auto;
}
.ck-video-text {
  max-width: none !important;
  width: auto !important;
  line-height: var(--ifm-line-height-base);
}
.ck-video-text::after {
  content: "";
  display: block;
  clear: both;
}
@media (max-width: 996px) {
  .ck-video-wrap--wrapped,
  .ck-video-wrap--full {
    float: none;
    width: 100%;
    max-width: 100%;
    margin: 0 0 1.25rem 0;
  }
  .ck-video-wrap--wrapped .ck-video-media {
    width: 100%;
    height: auto;
  }
}
/* CK_VIDEO_LAYOUT_END */"""

CSS_CARDS = """/* CK_PLACED_VIDEOS_START */
/* Cards placed on topic pages by the videos pipeline. Never a player: the
   player lives on the video's own page under /Videos and everything else
   links to it. */
.ck-placed-videos {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.25rem;
  margin: 1rem 0 1.5rem 0;
}
.ck-placed-video {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--ifm-color-emphasis-300);
  background: var(--ifm-background-surface-color);
}
.ck-placed-video img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 0;
  background: #000;
}
.ck-placed-video-body {
  padding: 0.6rem 0.75rem 0.75rem 0.75rem;
  font-size: 0.9rem;
}
.ck-placed-video-title {
  font-weight: 600;
  display: block;
  margin-bottom: 0.3rem;
  line-height: 1.3;
}
.ck-placed-video-caption {
  color: var(--ifm-color-emphasis-800);
  line-height: 1.4;
}
.ck-placed-video-meta {
  margin-top: 0.4rem;
  font-size: 0.8rem;
  color: var(--ifm-color-emphasis-600);
}
/* CK_PLACED_VIDEOS_END */"""

def upsert_block(text, start, end, block):
    pat = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if pat.search(text):
        return pat.sub(lambda _: block, text, count=1)
    return text.rstrip() + '\n\n' + block + '\n'

css = open(CSSFILE, encoding='utf-8').read()
before_ev = re.search(r'/\* CK_EVIDENCE_LAYOUT_START \*/.*?/\* CK_EVIDENCE_LAYOUT_END \*/', css, re.S)
before_pi = re.search(r'/\* CK_PLACED_IMAGES_START \*/.*?/\* CK_PLACED_IMAGES_END \*/', css, re.S)
ev_snapshot = before_ev.group(0) if before_ev else None
pi_snapshot = before_pi.group(0) if before_pi else None
css = upsert_block(css, '/* CK_VIDEO_LAYOUT_START */', '/* CK_VIDEO_LAYOUT_END */', CSS_VIDEO)
css = upsert_block(css, '/* CK_PLACED_VIDEOS_START */', '/* CK_PLACED_VIDEOS_END */', CSS_CARDS)
after_ev = re.search(r'/\* CK_EVIDENCE_LAYOUT_START \*/.*?/\* CK_EVIDENCE_LAYOUT_END \*/', css, re.S)
after_pi = re.search(r'/\* CK_PLACED_IMAGES_START \*/.*?/\* CK_PLACED_IMAGES_END \*/', css, re.S)
assert (after_ev.group(0) if after_ev else None) == ev_snapshot, 'CK_EVIDENCE_LAYOUT was modified'
assert (after_pi.group(0) if after_pi else None) == pi_snapshot, 'CK_PLACED_IMAGES was modified'
open(CSSFILE, 'w', encoding='utf-8').write(css)

# ------------------------------------------------------- Level 2 landing TOC
l2 = open(L2PAGE, encoding='utf-8').read()
toc = ['{/* VIDEOS_TOC_START */}', '',
       '## Browse The Video Evidence', '',
       f'{len(videos)} clips are catalogued below, grouped by what they show or '
       'claim. Each clip has its own page with the footage, a write-up, and its '
       'source.', '',
       '| Section | Videos |', '|---|---|']
for k in sorted([k for k in roots if k.rec > 0], key=lambda x: x.title):
    if k.bypass:
        t = k.bypass_target
        toc.append(f'| [{clean_title(t["v"].get("title"), 80)}]({t["url"]}) | 1 |')
    else:
        toc.append(f'| [{k.title}]({rel_url(k.page)}) | {k.rec} |')
toc += ['', 'Also in this section: '
        '[Buckley Carlson on the "Valhalla" comment](/Videos/buckley-carlson-kash-patel-valhalla).',
        '', '{/* VIDEOS_TOC_END */}']
toc_txt = '\n'.join(toc)
if 'VIDEOS_TOC_START' in l2:
    l2 = re.sub(r'\{/\* VIDEOS_TOC_START \*/\}.*?\{/\* VIDEOS_TOC_END \*/\}', lambda _: toc_txt, l2, flags=re.S)
else:
    m = re.search(r'^#\s+.*$', l2, re.M)
    if m:
        l2 = l2[:m.end()] + '\n\n' + toc_txt + '\n' + l2[m.end():]
    else:
        l2 = l2.rstrip() + '\n\n' + toc_txt + '\n'
open(L2PAGE, 'w', encoding='utf-8').write(l2)

# ------------------------------------------------------------------ pages.csv
rows = list(csv.DictReader(open(PAGESCSV, encoding='utf-8')))
fields = rows[0].keys() if rows else []
fields = list(csv.reader(open(PAGESCSV, encoding='utf-8')))[0]
by_key = {r['page_key']: r for r in rows}
mine = set()
added = updated = 0

def csv_row(page_key, parent_key, level, url, path, title, label, page_type, desc, lines):
    return {
        'page_key': page_key, 'parent_key': parent_key, 'level': str(level),
        'level2_parent': 'Videos', 'level2_section': 'Videos', 'page_type': page_type,
        'url_path': url, 'file_path': os.path.relpath(path, ROOT),
        'title': title, 'sidebar_label': label,
        'directory': os.path.relpath(os.path.dirname(path), DOCS),
        'extension': 'mdx', 'has_frontmatter': 'yes',
        'line_count': str(lines), 'description': desc,
    }

for n in pub_nodes:
    lines = sum(1 for _ in open(n.page, encoding='utf-8'))
    parent = n.parent.key if (n.parent and n.parent.rec > 0) else 'Videos'
    row = csv_row(n.key, parent, n.lvl, rel_url(n.page), n.page, n.title,
                  short_label(n.title), 'index',
                  f'Video evidence filed under {n.title}.', lines)
    mine.add(n.key)
    if n.key in by_key:
        by_key[n.key].update(row); updated += 1
    else:
        by_key[n.key] = row; rows.append(row); added += 1
for r in videos:
    lines = sum(1 for _ in open(r['page'], encoding='utf-8'))
    t = r.get('title') or clean_title(r['v'].get('title'))
    row = csv_row(r['key'], r['owner'].key, r['owner'].lvl + 1, r['url'], r['page'],
                  t, short_label(r['v'].get('title')), 'video',
                  first_sentences(r['v'].get('ai_description') or t, 1, 200), lines)
    mine.add(r['key'])
    if r['key'] in by_key:
        by_key[r['key']].update(row); updated += 1
    else:
        by_key[r['key']] = row; rows.append(row); added += 1

removed = 0
kept = []
for row in rows:
    fp = os.path.join(ROOT, row.get('file_path', ''))
    if row['page_key'] in mine or not fp.startswith(L2DIR + os.sep) or row['page_key'] in ('Videos', 'Videos_Buckley_Kash'):
        kept.append(row)
    else:
        removed += 1
rows = kept
with open(PAGESCSV, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore')
    w.writeheader()
    for row in rows:
        w.writerow({k: sanitize_prose(str(row.get(k, ''))) for k in fields})

# ------------------------------------------------------------------ manifest
man = []
for r in videos:
    v = r['v']
    man.append(dict(
        key=r['key'], page=r['page'], url=r['url'], node=r['owner'].key,
        node_title=r['owner'].title, node_page=r['owner'].page,
        cid=v.get('cid') or '', sha256=v.get('sha256') or '', mode=r['mode'],
        pending_reason=r['pending_reason'], poster=r['poster'],
        title=clean_title(v.get('title')), raw_title=v.get('title'),
        duration=v.get('duration'), file_path=v.get('file_path'),
        transcription_file=v.get('transcription_file') or '',
        ai_description_file=v.get('ai_description_file') or '',
        ocr_file=v.get('ocr_file') or '',
        source_url=v.get('source_url') or '', source_author=v.get('source_author') or '',
        source_platform=v.get('source_platform') or '',
        on_pages=[x.get('page') if isinstance(x, dict) else x for x in (v.get('on_pages') or [])],
        should_be_on_pages=[x.get('page') if isinstance(x, dict) else x
                            for x in (v.get('should_be_on_pages') or [])],
        also_nodes=[m.key for m in r['also_nodes']],
    ))
json.dump(dict(videos=man,
               nodes=[dict(key=n.key, title=n.title, level=n.lvl, page=n.page,
                           url=rel_url(n.page), rec=n.rec, bypass=n.bypass,
                           parent=(n.parent.key if n.parent else ''),
                           site_level_2=n.raw.get('site_level_2') or [],
                           site_page=n.raw.get('site_page') or '')
                      for n in pub_nodes]),
          open(OUTJSON, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ scan
bad = 0
for n in pub_nodes:
    validate_no_invisible(n.page)
for r in videos:
    validate_no_invisible(r['page'])
validate_no_invisible(L2PAGE)

modes = {}
for r in videos:
    modes[r['mode']] = modes.get(r['mode'], 0) + 1
pend = {}
for r in videos:
    if r['mode'] == 'pending':
        pend[r['pending_reason']] = pend.get(r['pending_reason'], 0) + 1

print('=' * 60)
print('STAGE 1-4 COMPLETE')
print(f'YAML nodes: {len(nodes)}   publishable: {len(pub_nodes)}   empty skipped: {len(empty_nodes)}')
print(f'Videos: {len(videos)} unique  (duplicate cross-filings folded: {dupes}, excluded: {len(skipped_excluded)})')
print(f'Cluster pages: {c_new} created, {c_old} rewritten   bypassed in nav: {len([n for n in pub_nodes if n.bypass])}')
print(f'Video pages:   {v_new} created, {v_old} rewritten')
print(f'Players: {modes.get("ipfs",0)} IPFS (pinned), {modes.get("thirdparty",0)} third-party embed, '
      f'{modes.get("link",0)} link-only, {modes.get("pending",0)} media pending {pend}')
print(f'Posters written/present: {len([r for r in videos if r["poster"]])}')
print(f'Orphans removed: {len(orphans)}')
print(f'pages.csv: {added} added, {updated} updated, {removed} stale Videos rows dropped')
print(f'Invisible-unicode findings: {bad}')
print('=' * 60)
