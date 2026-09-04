#!/usr/bin/env python3
"""Regenerate site/internals/src/citizenNoticePages.ts — the 100 pages that show
the citizen-investigator notice in place of the right-hand table of contents.

Selection, in order:
  * every page in pages.csv whose file exists, is under site/docs/, is not in the
    generated per-image /Photos or per-video /Videos trees, and has at least
    1500 characters of body (enough that a rail beside it is not absurd);
  * ranked by interesting_pages.csv rank where the page has one, then by size;
  * taken ROUND-ROBIN across level 2 sections so the 100 are spread over the
    whole site rather than piling into whichever section ranks best. Ranking
    alone put 40 of 100 in laws/ and 36 in Influencers/;
  * the site root '/' is excluded on purpose. The homepage keeps its normal
    table of contents: it is the width reference the narrow rail is sized
    against, and the request was to add the rail elsewhere, not to change it.

Rerun after adding sections or re-ranking interesting_pages.csv:
    python3 tools/gen_citizen_pages.py
"""
import csv, os, re, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'site/internals/src/citizenNoticePages.ts')
TARGET = 100
MIN_BODY = 1500


def main():
    rank = {}
    with open(os.path.join(ROOT, 'interesting_pages.csv'), encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            try:
                rank[r['url_path']] = int(r['rank'])
            except (ValueError, KeyError):
                pass

    cand = []
    with open(os.path.join(ROOT, 'pages.csv'), encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            fp = r.get('file_path', '')
            if not fp.startswith('site/docs/'):
                continue
            full = os.path.join(ROOT, fp)
            if not os.path.isfile(full):
                continue
            if '/Photos/' in fp or '/Videos/' in fp:
                continue
            txt = open(full, encoding='utf-8', errors='replace').read()
            parts = txt.split('---', 2)
            body = parts[2] if (txt.startswith('---') and len(parts) >= 3) else txt
            if len(body) < MIN_BODY:
                continue
            url = r.get('url_path', '')
            if not url or url == '/':
                continue
            cand.append({
                'url': url, 'file': fp,
                'sec': r.get('level2_section') or fp.split('/')[2],
                'title': r.get('title', ''),
                'rank': rank.get(url, 9999), 'size': len(body),
            })

    buckets = collections.OrderedDict()
    seen = set()
    for c in sorted(cand, key=lambda x: (x['rank'], -x['size'])):
        if c['url'] in seen:
            continue
        seen.add(c['url'])
        buckets.setdefault(c['sec'], []).append(c)

    order = sorted(buckets, key=lambda s: (buckets[s][0]['rank'], s))
    sel, i = [], 0
    while len(sel) < TARGET:
        progressed = False
        for s in order:
            if i < len(buckets[s]):
                sel.append(buckets[s][i])
                progressed = True
                if len(sel) == TARGET:
                    break
        if not progressed:
            break
        i += 1

    sel.sort(key=lambda x: x['url'])
    urls = [s['url'] for s in sel]
    assert len(urls) == len(set(urls)), 'duplicate url in selection'

    out = [
        '// GENERATED — the 100 pages that show the citizen-investigator notice in place',
        '// of the right-hand table of contents. See internals/src/components/CitizenNotice/.',
        '//',
        '// Regenerate with: python3 tools/gen_citizen_pages.py',
        '//',
        "// Paths are url_path values from pages.csv, no trailing slash. The site root '/'",
        '// is deliberately NOT in this list: the homepage keeps its normal table of',
        '// contents and is the width reference the narrow notice is sized against.',
        '',
        'const CITIZEN_NOTICE_PAGES: string[] = [',
    ]
    out += [f'  {json.dumps(s["url"])},   // {s["sec"]}' for s in sel]
    out += [
        '];',
        '',
        'export default CITIZEN_NOTICE_PAGES;',
        '',
        '/** Normalize a pathname the way the router hands it to us, then test membership. */',
        'export function isCitizenNoticePage(pathname: string): boolean {',
        '  if (!pathname) return false;',
        "  let p = pathname.split('?')[0].split('#')[0];",
        "  if (p.length > 1 && p.endsWith('/')) p = p.slice(0, -1);",
        '  return CITIZEN_NOTICE_SET.has(p);',
        '}',
        '',
        'const CITIZEN_NOTICE_SET = new Set(CITIZEN_NOTICE_PAGES);',
        '',
    ]
    open(OUT, 'w', encoding='utf-8').write('\n'.join(out))
    print(f'wrote {OUT}')
    print(f'  {len(sel)} pages across {len(set(s["sec"] for s in sel))} sections')


if __name__ == '__main__':
    main()
