#!/usr/bin/env python3
"""Convert Research/raw X-post research files into Influencers/x/ Level 3 MDX pages."""

import re
from pathlib import Path

ROOT = Path("/Users/bryan/BGit/Bryan_git/charlie-kirk")
RAW = ROOT / "Research/raw"
OUT = ROOT / "site/docs/Influencers/x"

# trash filename -> (output slug, display name, x handle)
MAPPING = {
    "john_cullen_posts.md": ("john-cullen", "John Cullen", "@I_Am_JohnCullen"),
    "ian_carroll_posts.md": ("ian-carroll", "Ian Carroll", "@IanCarrollShow"),
    "jg_cstt_posts.md": ("jg-cstt", "JG CSTT", "@JG_CSTT"),
    "healthranger_posts.md": ("healthranger", "Health Ranger", "@HealthRanger"),
    "george_webb_posts.md": ("george-webb", "George Webb", "@RealGeorgeWebb1"),
    "diligent_denizen_posts_1.md": ("diligent-denizen", "Diligent Denizen", "@DiligentDenizen"),
    "diligent_denizen_posts_2.md": ("diligent-denizen-2", "Diligent Denizen (2)", "@DiligentDenizen"),
    "project_constitu_posts.md": ("project-constitution", "Project Constitution", "@ProjectConstitu"),
    "based_sam_parker_posts.md": ("based-sam-parker", "Based Sam Parker", "@BasedSamParker"),
    "zeb_boykin_posts.md": ("zeb-boykin", "Zeb Boykin", "@zeb_boykin"),
    "hustlebitch_posts.md": ("hustlebitch", "Hustlebitch", "@hustlebitch"),
    "intel_scif_posts.md": ("intel-scif", "Intel SCIF", "@intel_scif"),
    "paramounttactcl_posts_1.md": ("paramounttactcl", "Paramount Tactcl", "@paramounttactcl"),
    "paramounttactcl_posts_2.md": ("paramounttactcl-2", "Paramount Tactcl (2)", "@paramounttactcl"),
    "ryan_matta_media_posts.md": ("ryan-matta", "Ryan Matta Media", "@RyanMattaMedia"),
}


def normalize_raw(text: str) -> str:
    """Collapse Grok export line breaks into single-line claims."""
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if any(
            x in line
            for x in (
                "Thought for",
                "Make these files markdown",
                "Searching for a topic",
                "Quick Answer",
                "Summarize ",
                "Add claim categories",
            )
        ):
            continue
        if line.startswith("https://x.com/i/grok"):
            continue
        if re.match(r"^Expert\d", line):
            continue
        if re.match(r"^\d+ posts$", line):
            continue
        lines.append(line)
    return " ".join(lines)


SKIP_FRAGMENTS = (
    "The Topic is:",
    "Example sources:",
    "Make these files markdown",
    "Searching for a topic",
    "Output the results that are factual",
    "Look for a file in the directory",
    "X happened on June",
    "Y happened on April",
    "Z happened on Sept",
    "Expert10/",
    "Grok ",
    "Work on making a bullet",
    "Everything @",
    "Posts - Especially",
)


def extract_claims(text: str) -> list[str]:
    norm = normalize_raw(text)
    # Drop Grok prompt header before first real investigation claim
    for marker in (
        "Charlie Kirk was fatally shot",
        "Charlie Kirk was shot",
        "On September 10, 2025",
    ):
        idx = norm.find(marker)
        if idx > 0:
            norm = norm[idx:]
            break

    claims = []

    # Grok bullet format: "... claim. [Source: X Post. URL] @handle"
    for m in re.finditer(
        r"(.+?)\[Source:\s*(?:X Post|Article|YouTube[^.]*)\.\s*(https?://[^\]]+)\]",
        norm,
        re.IGNORECASE,
    ):
        body = m.group(1).strip()
        url = m.group(2).strip()
        if "x.com/" not in url and "twitter.com/" not in url:
            continue
        body = re.sub(r"\s*@\w+\s*$", "", body)
        body = re.sub(r"^@\w+\s+", "", body)
        body = re.sub(r"\s+", " ", body).strip(" -")
        if len(body) < 25:
            continue
        if any(s in body for s in SKIP_FRAGMENTS):
            continue
        claims.append(f"{body} [Source: X Post. {url}]")

    # Markdown bullet format from some raw files
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("- ") and "[Source:" in line and len(line) > 40:
            claims.append(line[2:].strip())

    seen = set()
    out = []
    for c in claims:
        key = c[:100]
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out


def linkify_sources(claim: str) -> str:
    def repl(m):
        url = m.group(1).rstrip("]")
        return f" ([Source]({url}))"
    claim = re.sub(r"\[Source:\s*X Post\.\s*(https?://[^\]]+)\]", repl, claim)
    claim = re.sub(r"\[Source:\s*Article\.\s*(https?://[^\]]+)\]", repl, claim)
    claim = re.sub(r"\[Source:\s*YouTube[^\]]*\.\s*(https?://[^\]]+)\]", repl, claim)
    claim = re.sub(r"\s*@\w+\s*$", "", claim)
    return claim.strip()


def build_mdx(slug: str, title: str, handle: str, claims: list[str]) -> str:
    bullets = "\n".join(f"- {linkify_sources(c)}" for c in claims[:60])
    if len(claims) > 60:
        bullets += f"\n\n*({len(claims) - 60} additional claims in Research/raw — expand as needed.)*"

    return f"""---
title: "{title} — X Posts"
sidebar_label: "{title}"
description: "Compiled factual claims and theories from {handle} X posts about the Charlie Kirk assassination investigation, with source links."
keywords:
  - Charlie Kirk
  - Charlie Kirk assassination
  - September 10 2025
  - Utah Valley University
  - X posts
  - {title}
image: "/img/docusaurus-social-card.jpg"
---

<a href="../x" style={{{{display:'inline-block', marginBottom:'1rem',
padding:'0.35rem 0.9rem', background:'#1a73e8', color:'#fff',
borderRadius:'4px', textDecoration:'none', fontSize:'0.9rem'}}}}>← X Coverage</a>

# {title} — X Posts

{handle} is among the citizen investigators posting flight data, ballistics questions, drone sightings, and agency-involvement theories about the UVU shooting. The bullets below are **claims attributed to their X posts** — not confirmed findings. Each line links to the cited post where available.

## Claims from X posts

{bullets}

## Laws (Charlie Kirk)

* Posts alleging withheld flight logs, drone footage, sealed warrants, or agency interference describe records the [Charlie Kirk Investigation Laws](/Fix/overview) are designed to force into the open.

## Related

<div style={{{{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'0.5rem 2rem', marginTop:'0.5rem'}}}}>
<div>

* [X (Twitter) Coverage](../x)
* [John Cullen podcast](/Influencers/podcasts)
* [Planes / N1098L](/Planes/N1098L/overview)

</div>
<div>

* [Drones](/Drones/overview)
* [FBI](/FBI/overview)
* [Timeline](/Timeline/overview)

</div>
</div>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    created = []
    for raw_name, (slug, title, handle) in MAPPING.items():
        raw_path = RAW / raw_name
        if not raw_path.exists():
            print(f"SKIP missing {raw_name}")
            continue
        text = raw_path.read_text(encoding="utf-8", errors="replace")
        claims = extract_claims(text)
        if not claims:
            print(f"SKIP no claims {raw_name}")
            continue
        out_path = OUT / f"{slug}.mdx"
        out_path.write_text(build_mdx(slug, title, handle, claims), encoding="utf-8")
        created.append((slug, len(claims)))
        print(f"OK {slug}.mdx ({len(claims)} claims)")
    print(f"Created {len(created)} pages in {OUT}")


if __name__ == "__main__":
    main()