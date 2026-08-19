#!/usr/bin/env python3
"""Stage 7 verifier for p_4_squares.md.

Usage: python3 verify_blocks.py <file> [<file> ...]
Exit 0 = every file clean. Non-zero = at least one failure printed.
"""
import os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(os.path.expanduser("~/BGit/Bryan_git/charlie-kirk"))
WORK = ROOT / "prompts/four_squares"
ROUTES = set((WORK / "routes.txt").read_text().split())
MAX_WORDS = 17

BLOCKS = ["CK_INTERESTING_HERE", "CK_INTERESTING_OTHER", "CK_4SQ_SECTION", "CK_4SQ_SITEWIDE"]


def block_text(text, name):
    m = re.search(re.escape(name) + r"_START\s*(?:\*/\}|-->)(.*?)(?:\{/\*|<!--)\s*"
                  + re.escape(name) + r"_END", text, re.S)
    return m.group(1) if m else ""


def check(path):
    fails = []
    p = Path(path)
    rel = str(p.relative_to(ROOT)) if p.is_absolute() else path
    text = p.read_text(encoding="utf-8", errors="replace")
    ext = p.suffix.lstrip(".")

    # 1. marker hygiene
    for b in BLOCKS:
        ns, ne = text.count(b + "_START"), text.count(b + "_END")
        if ns > 1 or ne > 1:
            fails.append(f"duplicate block {b} (start={ns} end={ne})")
        if ns != ne:
            fails.append(f"unbalanced block {b} (start={ns} end={ne})")

    ours = "".join(block_text(text, b) for b in BLOCKS)

    # 2. comment form inside our blocks
    for b in BLOCKS:
        if ext == "mdx" and re.search(r"<!--\s*" + b, text):
            fails.append(f"HTML comment marker in .mdx for {b}")
        if ext == "md" and re.search(r"\{/\*\s*" + b, text):
            fails.append(f"JSX comment marker in .md for {b}")
    if ext == "md" and re.search(r"className=", ours):
        fails.append("JSX card markup emitted into a .md page")

    # 3. links resolve
    for url in set(re.findall(r'href="(/[^"#?]*)"', ours) + re.findall(r"\]\((/[^)\s#?]*)\)", ours)):
        if url.rstrip("/") not in ROUTES and url not in ROUTES:
            fails.append(f"unresolved link {url}")

    # 4. no self-card, no duplicate target inside one grid
    self_url = None
    for line in (WORK / "self_urls.txt").read_text().splitlines() if (WORK / "self_urls.txt").exists() else []:
        f, u = line.split("\t")
        if f == rel:
            self_url = u
            break
    for b in ("CK_4SQ_SECTION", "CK_4SQ_SITEWIDE"):
        seg = block_text(text, b)
        targets = re.findall(r'class[Nn]ame="ck-4sq-title"><a href="([^"]+)"', seg)
        if len(targets) != len(set(targets)):
            fails.append(f"{b}: duplicate card target")
        if self_url and self_url in targets:
            fails.append(f"{b}: page cards itself")
        if seg.strip() and len(targets) not in (0, 2, 3, 4):
            fails.append(f"{b}: {len(targets)} cards")
        if re.search(r"https?://(ipfs\.io|[a-z0-9]+\.ipfs\.dweb\.link)[^\"']*\.(jpg|jpeg|png|webp)", seg):
            fails.append(f"{b}: image served from an IPFS gateway")

    # 5. sentence length in the two interesting blocks
    for b in ("CK_INTERESTING_HERE", "CK_INTERESTING_OTHER"):
        for line in block_text(text, b).splitlines():
            if not line.strip().startswith("*"):
                continue
            plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line.strip()[1:])
            plain = re.sub(r"&[a-z]+;", " ", plain)
            n = len(plain.split())
            if n > MAX_WORDS:
                fails.append(f"{b}: {n}-word sentence: {plain.strip()[:60]}")

    # 6. embedded images are tracked and not ignored
    for src in set(re.findall(r'src="(/img/evidence/[^"]+)"', ours)):
        fp = "site/internals/static/img/" + src.split("/img/", 1)[1]
        if subprocess.run(["git", "ls-files", "--error-unmatch", fp], cwd=ROOT,
                          capture_output=True).returncode != 0:
            fails.append(f"untracked image {fp}")
        elif subprocess.run(["git", "check-ignore", fp], cwd=ROOT,
                            capture_output=True).stdout.strip():
            fails.append(f"gitignored image {fp}")
    return fails


def mdx_compile(files):
    files = [f for f in files if f.endswith(".mdx")]
    if not files:
        return {}
    script = r"""
import('@mdx-js/mdx').then(async m=>{const fs=require('fs');
  for (const f of process.argv.slice(1)) {
    let s=fs.readFileSync(f,'utf8').replace(/^---\n[\s\S]*?\n---\n/,'');
    try { await m.compile(s) } catch(e){ console.log('FAIL\t'+f+'\t'+String(e.message).split('\n')[0]) } }
})"""
    out = subprocess.run(["node", "-e", script] + files, cwd=ROOT / "site",
                         capture_output=True, text=True).stdout
    bad = {}
    for line in out.splitlines():
        if line.startswith("FAIL\t"):
            _, f, msg = line.split("\t", 2)
            bad[f] = msg
    return bad


if __name__ == "__main__":
    files = [str(Path(f).resolve()) for f in sys.argv[1:]]
    bad_mdx = mdx_compile(files)
    nfail = 0
    for f in files:
        fails = check(f)
        if f in bad_mdx:
            fails.insert(0, "MDX COMPILE: " + bad_mdx[f])
        if fails:
            nfail += 1
            print(f"FAIL {os.path.relpath(f, ROOT)}")
            for x in fails:
                print("   -", x)
    print(f"checked {len(files)} files, {nfail} failing")
    sys.exit(1 if nfail else 0)
