#!/usr/bin/env python3
# audit_image_publication.py — repo-wide check that every image we downloaded is
# actually visible to a real visitor.
#
# WHY THIS EXISTS
# ---------------
# ck_add_text verifies the images of the run it just did. Nothing verified the ones
# from every PREVIOUS run. An audit on 2026-08-12 of four months of skill runs found
# three separate failure modes that had accumulated silently:
#
#   1. 85 downloaded images had never been copied to
#      site/internals/static/img/evidence/, so nothing served them.
#   2. 265 page embeds used src="https://ipfs.io/ipfs/<CID>" instead of the local
#      /img/evidence/<sha>.jpg path. Most CIDs in videos.yaml/manifest.yaml were
#      produced with `ipfs add -n` and live on no node, so 11 of them returned 504
#      from the public gateway — a broken image for every visitor, while rendering
#      perfectly on the machine that had the file locally.
#   3. 15 images were downloaded and pinned but never embedded on any page at all.
#
# Each mode is invisible in local dev. This script makes all three fail loudly.
#
# USAGE
#   python3 image_planning/generator/audit_image_publication.py            # fast
#   python3 image_planning/generator/audit_image_publication.py --gateway  # also
#          probes every remaining ipfs.io image embed against the public gateway
#          (slow, ~1s/CID, needs network) to catch newly-unpinned CIDs.
#
# Exit code 0 = clean, 1 = at least one image is not reachable by a visitor.
# Banned and privacy-listed images are expected to be unpublished and are counted
# as WITHHELD, never as failures.
import os, re, sys, csv, glob, hashlib, subprocess

ROOT = os.path.expanduser('~/BGit/Bryan_git/charlie-kirk')
SRC_DIR = os.path.join(ROOT, 'images')
STATIC = os.path.join(ROOT, 'site/internals/static')
DOCS = os.path.join(ROOT, 'site/docs')
IMG_EXT = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif')


def sha_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ban_set():
    """Union of the two ban gates, exactly as CLAUDE.md defines it."""
    banned = set()
    exc = os.path.join(ROOT, 'image_planning/exclude_images.txt')
    if os.path.exists(exc):
        for line in open(exc, encoding='utf-8'):
            line = line.split('#', 1)[0].strip()
            if re.fullmatch(r'[0-9a-f]{64}', line):
                banned.add(line)
    csv_path = os.path.join(ROOT, 'images/ban_images.csv')
    if os.path.exists(csv_path):
        for row in csv.DictReader(open(csv_path, encoding='utf-8')):
            if (row.get('banned') or '').strip().lower() == 'true' and row.get('sha256'):
                banned.add(row['sha256'].strip())
    return banned


def privacy_set():
    """images/.gitignore is the hand-curated keep-out-of-the-repo list."""
    p = os.path.join(SRC_DIR, '.gitignore')
    if not os.path.exists(p):
        return set()
    return {l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')}


def docs_text():
    out = []
    for pat in ('**/*.mdx', '**/*.md'):
        for fp in glob.glob(os.path.join(DOCS, pat), recursive=True):
            out.append(open(fp, encoding='utf-8', errors='replace').read())
    return '\n'.join(out)


def served_map():
    """sha256 -> list of site-root-relative URLs that serve those exact bytes."""
    m = {}
    for root, _, files in os.walk(STATIC):
        for f in files:
            if f.lower().endswith(IMG_EXT):
                p = os.path.join(root, f)
                m.setdefault(sha_of(p), []).append('/' + os.path.relpath(p, STATIC))
    return m


def gateway_ok(cid):
    r = subprocess.run(
        ['curl', '-s', '-o', '/dev/null', '-m', '40', '-w', '%{http_code} %{content_type}',
         f'https://ipfs.io/ipfs/{cid}'], capture_output=True, text=True)
    code, _, ctype = r.stdout.partition(' ')
    return code == '200' and ctype.startswith('image/')


def main():
    probe = '--gateway' in sys.argv
    banned, private = ban_set(), privacy_set()
    text, served = docs_text(), served_map()

    unserved, unplaced, withheld, ok = [], [], [], []
    for f in sorted(os.listdir(SRC_DIR)):
        if not f.lower().endswith(IMG_EXT):
            continue
        path = os.path.join(SRC_DIR, f)
        h = sha_of(path)
        if h in banned or f in private:
            withheld.append(f)
            # A withheld image must NOT be served. That is a real failure.
            if h in served:
                unserved.append((f, h, 'BANNED BUT STILL SERVED: ' + ', '.join(served[h])))
            continue
        if h not in served:
            unserved.append((f, h, 'no copy under site/internals/static/'))
            continue
        if not any(u in text for u in served[h]):
            unplaced.append((f, h, served[h][0]))
            continue
        ok.append(f)

    # Any image still embedded straight off the public gateway is a latent 504.
    ipfs_embeds = sorted(set(re.findall(
        r'<img\b[^>]*?src=["\']https://ipfs\.io/ipfs/(Qm[1-9A-HJ-NP-Za-km-z]+)', text, re.S)))
    dead = []
    if probe:
        for cid in ipfs_embeds:
            if not gateway_ok(cid):
                dead.append(cid)

    print('=' * 60)
    print('IMAGE PUBLICATION AUDIT')
    print(f'  images/ scanned      : {len(ok) + len(unserved) + len(unplaced) + len(withheld)}')
    print(f'  reader can see them  : {len(ok)}')
    print(f'  withheld (ban/privacy): {len(withheld)}')
    print(f'  NOT SERVED           : {len(unserved)}')
    for f, h, why in unserved:
        print(f'      {f}  {h[:12]}  {why}')
    print(f'  SERVED BUT ON NO PAGE: {len(unplaced)}')
    for f, h, u in unplaced:
        print(f'      {f}  {h[:12]}  -> {u}')
    print(f'  <img> tags still pointing at ipfs.io: {len(ipfs_embeds)}')
    if probe:
        print(f'  ...of which DEAD on the public gateway: {len(dead)}')
        for c in dead:
            print(f'      {c}')
    elif ipfs_embeds:
        print('      (re-run with --gateway to probe them)')
    print('=' * 60)

    failed = bool(unserved or unplaced or dead)
    print('RESULT:', 'FAIL' if failed else 'CLEAN')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
