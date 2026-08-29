# Planes Infographic Templates

This directory holds TEMPLATES ONLY. It is the pattern library for every
infographic made for the Planes Level 2 section. Nothing here is a finished
infographic and nothing here is published.

Files lead with an underscore on purpose: `**/_*.{md,mdx}` is in the Docusaurus
docs `exclude` list, so these never become pages.

    _README.md                              this file
    _goals_template.mdx                     copy to {infographic dir}/goals.mdx
    _nana_banana_pro_prompt_template.txt    copy to {infographic dir}/nana_banana_pro_prompt.txt

## Where a real infographic goes

NOT here. A real infographic goes where Docusaurus can serve the image at a
public URL:

    site/internals/static/img/infographics/{TAIL}_{Type}/

Everything under `site/internals/static/` is copied verbatim into the build, so
a file at

    site/internals/static/img/infographics/N1098L_Flight_Record/N1098L_Flight_Record.jpg

is served at

    /img/infographics/N1098L_Flight_Record/N1098L_Flight_Record.jpg

The directory name is the aircraft plus the infographic type, underscores
between words, no spaces and no special characters — it behaves like a page key.
One directory per (aircraft, type) pair.

## How to use these templates

1. Pick the aircraft and the infographic type. Make the directory
   `site/internals/static/img/infographics/{TAIL}_{Type}/`.
2. Copy `_goals_template.mdx` to `goals.mdx` in it and fill in EVERY section.
   Plan first. The prompt is written FROM the goals, never the other way round.
3. Copy `_nana_banana_pro_prompt_template.txt` to `nana_banana_pro_prompt.txt`
   and write it from the finished goals.
4. Generate into the same directory, 16:9, 2K.
5. Embed on the page by local repo path — `/img/infographics/...` — never by an
   IPFS gateway URL.

The full rules live in `site/docs/Planes/CLAUDE.md`. Read that before making one.
