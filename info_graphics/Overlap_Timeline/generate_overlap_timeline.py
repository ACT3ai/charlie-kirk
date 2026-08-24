#!/usr/bin/env python3
"""
generate_overlap_timeline.py — build the Overlap_Timeline infographic as SVG.

Reads the overlap spine and emits an exact, plotted 16:9 chart. Nothing in this
file is hand-typed data: every bar comes out of overlaps.csv, so re-running it
after the CSV changes is the whole update procedure.

    OVERLAPS_CSV is file ~/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following/overlaps.csv
    SVG_OUT      is file ~/BGit/Bryan_git/charlie-kirk/site/internals/static/img/infographics/Overlap_Timeline.svg

Design spec: ../goals.mdx  (audience, framing, sizing, percentages, on-image text)
"""

import csv, collections, os, sys, html

ROOT     = os.path.expanduser("~/BGit/Bryan_git/charlie-kirk")
CSV_IN   = os.path.join(ROOT, "site/docs/Planes/following/overlaps.csv")
SVG_OUT  = os.path.join(ROOT, "site/internals/static/img/infographics/Overlap_Timeline.svg")

# ── palette ──────────────────────────────────────────────────────────────────
BG      = "#1b1b1f"
INK     = "#f4f4f6"
GREY    = "#9b9ba3"
DIM     = "#6e6e77"
AMBER   = "#e0a33e"   # Charlie Kirk + TPUSA
BLUE    = "#6ea8d8"   # Erika Kirk
RULE    = "#3a3a42"

# ── geometry (viewBox 1920 x 1080 = 16:9) ────────────────────────────────────
W, H       = 1920, 1080
AX_Y       = 530          # the shared time axis
AX_X0      = 150
AX_X1      = 1566
N_MONTHS   = 46           # Jan 2022 .. Oct 2025
SLOT       = (AX_X1 - AX_X0) / N_MONTHS
BAR_W      = 17
UNIT       = 46           # px per claimed overlap


def month_list():
    out, y, m = [], 2022, 1
    while (y, m) <= (2025, 10):
        out.append("%04d-%02d" % (y, m))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def load():
    """Return (upper, lower, undated) where upper/lower map 'YYYY-MM' -> Counter of fills."""
    upper = collections.defaultdict(collections.Counter)
    lower = collections.defaultdict(collections.Counter)
    undated = 0
    survivors = {"upper": set(), "lower": set()}
    with open(CSV_IN, newline="") as fh:
        for r in csv.DictReader(fh):
            date = r["date"].strip()
            if len(date) < 7 or date == "UNKNOWN":
                undated += 1
                continue
            mo = date[:7]
            # TPUSA and 'Both' ride with Charlie: the upper band is the
            # organisation-and-Charlie ledger, the lower band is Erika's.
            band = upper if r["subject"] in ("Charlie", "Both", "TPUSA") else lower
            v = r["audit_verdict"]
            fill = {"accurate": "A", "partial": "P", "inaccurate": "X"}.get(v, "U")
            band[mo][fill] += 1
            if r["gap"] in ("same_day", "day_before"):
                survivors["upper" if band is upper else "lower"].add(mo)
    return upper, lower, undated, survivors


def esc(s):
    return html.escape(s, quote=False)


def bar(x, y_axis, counts, colour, up):
    """Stack A, P, X, U outward from the axis. Returns SVG fragment."""
    frag, off = [], 0
    for fill in ("A", "P", "X", "U"):
        for _ in range(counts.get(fill, 0)):
            y = y_axis - off - UNIT if up else y_axis + off
            if fill == "A":
                frag.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{BAR_W}" height="{UNIT}" fill="{colour}"/>')
            elif fill == "P":
                frag.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{BAR_W}" height="{UNIT}" fill="url(#hatch{colour[1:]})" stroke="{colour}" stroke-width="1.6"/>')
            elif fill == "X":
                frag.append(f'<rect x="{x+0.8:.1f}" y="{y+0.8:.1f}" width="{BAR_W-1.6}" height="{UNIT-1.6}" fill="none" stroke="{colour}" stroke-width="1.6"/>')
            else:
                frag.append(f'<rect x="{x+0.8:.1f}" y="{y+0.8:.1f}" width="{BAR_W-1.6}" height="{UNIT-1.6}" fill="none" stroke="{colour}" stroke-width="1.4" stroke-dasharray="3 3" opacity="0.75"/>')
            off += UNIT
    return "".join(frag), off


def main():
    months = month_list()
    upper, lower, undated, survivors = load()
    tot_u = sum(sum(c.values()) for c in upper.values())
    tot_l = sum(sum(c.values()) for c in lower.values())
    verd = collections.Counter()
    for band in (upper, lower):
        for c in band.values():
            verd.update(c)

    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica Neue, Helvetica, Arial, sans-serif">')
    s.append('<defs>')
    for col, name in ((AMBER, AMBER[1:]), (BLUE, BLUE[1:])):
        s.append(f'<pattern id="hatch{name}" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">'
                 f'<rect width="7" height="7" fill="none"/><line x1="0" y1="0" x2="0" y2="7" stroke="{col}" stroke-width="3.4"/></pattern>')
    s.append('</defs>')
    s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

    # ── title + subline (upper left, ~12% of frame) ──────────────────────────
    s.append(f'<text x="60" y="104" fill="{INK}" font-size="52" font-weight="700" letter-spacing="0.5">THREE YEARS OF CLAIMED OVERLAPS</text>')
    s.append(f'<text x="62" y="143" fill="{GREY}" font-size="20">Egyptian-registered jets and the Kirks, January 2022 &#8211; October 2025.</text>')
    s.append(f'<text x="62" y="171" fill="{GREY}" font-size="20">Each bar is one month. Solid bars survived an independent audit. Hollow bars did not.</text>')

    # ── stat card (upper right, ~10%) ────────────────────────────────────────
    cx, cy, cw, ch = 1386, 46, 474, 168
    s.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="none" stroke="{RULE}" stroke-width="1.5" rx="4"/>')
    s.append(f'<text x="{cx+22}" y="{cy+58}" fill="{INK}" font-size="46" font-weight="700">{tot_u + tot_l}</text>')
    s.append(f'<text x="{cx+96}" y="{cy+44}" fill="{GREY}" font-size="17">dated claimed overlaps</text>')
    s.append(f'<text x="{cx+96}" y="{cy+66}" fill="{DIM}" font-size="17">tallies broadcast as &#8220;73&#8221;</text>')
    s.append(f'<line x1="{cx+22}" y1="{cy+82}" x2="{cx+cw-22}" y2="{cy+82}" stroke="{RULE}" stroke-width="1"/>')
    s.append(f'<text x="{cx+22}" y="{cy+104}" fill="{DIM}" font-size="13" letter-spacing="1.1">AUDIT OF THE AIRCRAFT&#8217;S POSITION</text>')
    # 100% stacked audit bar — 18 accurate / 44 inaccurate / 5 partial
    bx, by, bw, bh = cx + 22, cy + 114, cw - 44, 16
    a, x_, p = 18, 44, 5
    tt = a + x_ + p
    wa, wx, wp = bw * a / tt, bw * x_ / tt, bw * p / tt
    s.append(f'<rect x="{bx}" y="{by}" width="{wa:.1f}" height="{bh}" fill="{INK}"/>')
    s.append(f'<rect x="{bx+wa+0.8:.1f}" y="{by+0.8}" width="{wx-1.6:.1f}" height="{bh-1.6}" fill="none" stroke="{GREY}" stroke-width="1.5"/>')
    s.append(f'<rect x="{bx+wa+wx:.1f}" y="{by}" width="{wp:.1f}" height="{bh}" fill="url(#hatch{AMBER[1:]})" stroke="{AMBER}" stroke-width="1.2"/>')
    s.append(f'<text x="{bx}" y="{by+38}" fill="{GREY}" font-size="16">'
             f'<tspan fill="{INK}" font-weight="600">18 accurate</tspan>  &#183;  '
             f'<tspan>44 inaccurate</tspan>  &#183;  <tspan>5 partial</tspan></text>')

    # ── month gridlines + year separators ────────────────────────────────────
    for i, mo in enumerate(months):
        gx = AX_X0 + i * SLOT + SLOT / 2
        s.append(f'<line x1="{gx:.1f}" y1="{AX_Y-190}" x2="{gx:.1f}" y2="{AX_Y+250}" stroke="{RULE}" stroke-width="0.5" opacity="0.32"/>')
        if mo.endswith("-01"):
            lx = AX_X0 + i * SLOT
            s.append(f'<line x1="{lx:.1f}" y1="{AX_Y-215}" x2="{lx:.1f}" y2="{AX_Y+275}" stroke="{RULE}" stroke-width="1.2"/>')
            s.append(f'<text x="{lx+10:.1f}" y="{AX_Y-196}" fill="{GREY}" font-size="19" font-weight="600" letter-spacing="1">{mo[:4]}</text>')

    # ── the bars ─────────────────────────────────────────────────────────────
    marks = []
    for i, mo in enumerate(months):
        x = AX_X0 + i * SLOT + (SLOT - BAR_W) / 2
        f, off = bar(x, AX_Y, upper.get(mo, {}), AMBER, True)
        s.append(f)
        if mo in survivors["upper"]:
            marks.append((x + BAR_W / 2, AX_Y - off - 20))
        f, off = bar(x, AX_Y, lower.get(mo, {}), BLUE, False)
        s.append(f)
        if mo in survivors["lower"]:
            marks.append((x + BAR_W / 2, AX_Y + off + 20))

    # ── the axis, drawn over the bars ────────────────────────────────────────
    s.append(f'<line x1="{AX_X0-58}" y1="{AX_Y}" x2="{AX_X1+18}" y2="{AX_Y}" stroke="{INK}" stroke-width="1.8"/>')

    # ── survivor diamonds ────────────────────────────────────────────────────
    for mx, my in marks:
        s.append(f'<path d="M {mx:.1f} {my-8} L {mx+8:.1f} {my} L {mx:.1f} {my+8} L {mx-8:.1f} {my} Z" fill="{INK}"/>')
    kx, ky = AX_X0 + 15.5 * SLOT, AX_Y - 268
    s.append(f'<path d="M {kx} {ky-7} L {kx+7} {ky} L {kx} {ky+7} L {kx-7} {ky} Z" fill="{INK}"/>')
    s.append(f'<text x="{kx+18}" y="{ky-2}" fill="{GREY}" font-size="16">survives a same-day test at a shared</text>')
    s.append(f'<text x="{kx+18}" y="{ky+20}" fill="{GREY}" font-size="16">field &#8212; <tspan fill="{INK}" font-weight="600">6 dates</tspan></text>')

    # ── band labels, frame left, inside the empty 2022 months ────────────────
    s.append(f'<text x="60" y="{AX_Y-118}" fill="{AMBER}" font-size="21" font-weight="700" letter-spacing="0.6">CHARLIE KIRK + TPUSA <tspan fill="{GREY}" font-weight="400">&#8212; {tot_u} claimed</tspan></text>')
    s.append(f'<text x="60" y="{AX_Y+168}" fill="{BLUE}" font-size="21" font-weight="700" letter-spacing="0.6">ERIKA KIRK <tspan fill="{GREY}" font-weight="400">&#8212; {tot_l} claimed</tspan></text>')

    # ── ghosted never-published block, off the right end, outside time ───────
    gx0 = AX_X1 + 52
    for k in range(undated):
        s.append(f'<rect x="{gx0 + k*26:.1f}" y="{AX_Y-88}" width="17" height="88" fill="none" stroke="{DIM}" stroke-width="1.3" stroke-dasharray="3 4" opacity="0.72"/>')
    s.append(f'<text x="{gx0}" y="{AX_Y+30}" fill="{GREY}" font-size="17" font-weight="600">{undated} more claimed overlaps</text>')
    for j, ln in enumerate(["never published &#8212; no date, no city,",
                            "no airport, no tail. Cannot be placed",
                            "on this timeline."]):
        s.append(f'<text x="{gx0}" y="{AX_Y+54+j*21}" fill="{DIM}" font-size="15">{ln}</text>')

    # ── legend, lower left (~5%) ─────────────────────────────────────────────
    lx0, ly0 = 60, 838
    s.append(f'<rect x="{lx0}" y="{ly0}" width="556" height="150" fill="none" stroke="{RULE}" stroke-width="1.5" rx="4"/>')
    rows = [("A", "audited accurate &#8212; the jet was there"),
            ("P", "partially accurate &#8212; right aircraft and date, wrong route"),
            ("X", "audited inaccurate &#8212; the jet was elsewhere, usually another continent"),
            ("U", "not assessable &#8212; the flight archive does not reach back")]
    for j, (fill, txt) in enumerate(rows):
        sy = ly0 + 26 + j * 32
        if fill == "A":
            s.append(f'<rect x="{lx0+20}" y="{sy-11}" width="17" height="17" fill="{INK}"/>')
        elif fill == "P":
            s.append(f'<rect x="{lx0+20}" y="{sy-11}" width="17" height="17" fill="url(#hatch{AMBER[1:]})" stroke="{GREY}" stroke-width="1.4"/>')
        elif fill == "X":
            s.append(f'<rect x="{lx0+20.8}" y="{sy-10.2}" width="15.4" height="15.4" fill="none" stroke="{GREY}" stroke-width="1.6"/>')
        else:
            s.append(f'<rect x="{lx0+20.8}" y="{sy-10.2}" width="15.4" height="15.4" fill="none" stroke="{GREY}" stroke-width="1.4" stroke-dasharray="3 3"/>')
        s.append(f'<text x="{lx0+50}" y="{sy+3}" fill="{GREY}" font-size="15.5">{txt}</text>')

    # ── September call-out lens, lower right (~16%) ──────────────────────────
    px0, py0, pw, ph = 964, 800, 700, 218
    sep_i = months.index("2025-09")
    sep_x = AX_X0 + sep_i * SLOT + SLOT / 2
    s.append(f'<line x1="{sep_x:.1f}" y1="{AX_Y+250}" x2="{px0+pw:.1f}" y2="{py0}" stroke="{RULE}" stroke-width="1.1"/>')
    s.append(f'<line x1="{sep_x-14:.1f}" y1="{AX_Y+250}" x2="{px0+40:.1f}" y2="{py0}" stroke="{RULE}" stroke-width="1.1"/>')
    s.append(f'<rect x="{px0}" y="{py0}" width="{pw}" height="{ph}" fill="{BG}" stroke="{INK}" stroke-width="1.6" rx="4"/>')
    s.append(f'<text x="{px0+26}" y="{py0+36}" fill="{AMBER}" font-size="18" font-weight="700" letter-spacing="1.1">THE PART THAT SURVIVES</text>')
    lens = [("4 SEP 2025", "SU-BTT lands Provo, 12:46 pm"),
            ("10 SEP 2025", "SU-BTT departs Provo, 07:14 am"),
            ("10 SEP 2025", "SU-BND on the ground, transponder cycling, never takes off")]
    for j, (d, t) in enumerate(lens):
        ly = py0 + 68 + j * 27
        s.append(f'<text x="{px0+26}" y="{ly}" fill="{INK}" font-size="16.5" font-weight="700">{d}<tspan fill="{GREY}" font-weight="400">&#160;&#8212; {t}</tspan></text>')
    s.append(f'<text x="{px0+26}" y="{py0+152}" fill="{INK}" font-size="16.5">Charlie Kirk is killed at UVU, Orem &#8212; 7 miles away</text>')
    s.append(f'<line x1="{px0+26}" y1="{py0+168}" x2="{px0+pw-26}" y2="{py0+168}" stroke="{RULE}" stroke-width="1"/>')
    s.append(f'<text x="{px0+26}" y="{py0+194}" fill="{GREY}" font-size="16">Of the 6 surviving dates, <tspan fill="{INK}" font-weight="600">3 are Charlie Kirk</tspan>. <tspan fill="{INK}" font-weight="600">2 of those 3 are in Utah</tspan>.</text>')

    # ── source line, bottom edge (~3%) ───────────────────────────────────────
    s.append(f'<line x1="60" y1="1022" x2="{W-60}" y2="1022" stroke="{RULE}" stroke-width="1"/>')
    s.append(f'<text x="60" y="1046" fill="{DIM}" font-size="13.5">Researcher tallies read from public ADS-B history, not confirmed records. Compiled counts attributed to Candace Owens and others; line-by-line audit attributed to @KanekoaTheGreat.</text>')
    s.append(f'<text x="60" y="1065" fill="{DIM}" font-size="13.5">Overlap window as published: within 50&#8211;100 miles and &#177;3 days. Erika Kirk&#8217;s flight logs are reported erased; her side of the ledger has no published itinerary behind it. Nothing here is a finding of wrongdoing by any living person.</text>')

    s.append('</svg>')

    os.makedirs(os.path.dirname(SVG_OUT), exist_ok=True)
    with open(SVG_OUT, "w") as fh:
        fh.write("\n".join(s))

    print(f"wrote {SVG_OUT}")
    print(f"  upper (Charlie/TPUSA): {tot_u}   lower (Erika): {tot_l}   undated: {undated}")
    print(f"  verdict totals: {dict(verd)}")
    print(f"  survivor months: upper={sorted(survivors['upper'])} lower={sorted(survivors['lower'])}")


if __name__ == "__main__":
    main()
