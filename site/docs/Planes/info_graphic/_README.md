# Planes Infographic Templates

This directory holds TEMPLATES ONLY. It is the pattern library for every
infographic made for the Planes Level 2 section. Nothing here is a finished
infographic and nothing here is published.

Files lead with an underscore on purpose: `**/_*.{md,mdx}` is in the Docusaurus
docs `exclude` list, so these never become pages.

    _README.md                              this file
    _goals_template.mdx                     copy to {infographic dir}/goals.mdx
    _nana_banana_pro_prompt_template.txt    copy to {infographic dir}/nana_banana_pro_prompt.txt

## The Plane Overlap template

The first NAMED template in this library, and the only one so far with a real
generator behind it. One graphic = one following aircraft x one overlap x one
Kirk side (Charlie / Erika / both).

    p_create_svgs.md            the prompt that walks the overlaps and builds them
    template.svg                the pattern. A real rendering, annotated. Read the
                                header comment for the anatomy of the graphic.
    code/build_overlap_svg.ts   the generator. Reads info.yaml, writes the SVG.
    code/package.json           marks code/ as ESM so node runs the .ts directly

Run it:

    node code/build_overlap_svg.ts <dir>                     one graphic
    node code/build_overlap_svg.ts --all <root>              everything
    node code/build_overlap_svg.ts --all <root> --check      report only

Output goes to site/internals/static/img/infographics/overlaps/{DIR}/, where
{DIR} is {YYYY}_{MM}_{DD}_{AIRPORT}_{Charlie|Erika|Both}_{ST}_{city}.

THE BARS ARE PLOTTED, NOT PROMPTED. A reader reads values off them, so a
generative model never draws them. The town/airport scene behind them may be
model-generated; the bars never are. The generator refuses missing times,
refuses to merge two ground contacts in a day, and refuses to say "arrived" for
data that only says "heard". Do not work around any of those - they are the
rules from site/docs/Planes/CLAUDE.md expressed as code.

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
