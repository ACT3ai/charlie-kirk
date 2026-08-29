/**
 * build_overlap_svg.ts — Plane Overlap infographic generator.
 *
 * Reads an info.yaml describing ONE overlap — one following/intelligence
 * aircraft, one Charlie/Erika/both aircraft, one airport, one date — and emits
 * the 16:9 SVG for it.
 *
 * The bars are VALUES A READER READS OFF THE PICTURE, so they are PLOTTED here
 * from the data and never drawn by a generative model. See
 * site/docs/Planes/CLAUDE.md, "PLOTTED vs MODEL-GENERATED".
 *
 * THREE THINGS THIS GENERATOR REFUSES TO DO, each one a rule from the root
 * charter that a prettier graphic would quietly break:
 *
 *   1. It will not draw a bar from a missing or "unknown" time. A drawn bar is
 *      a claim about a duration. Missing times fail the run, loudly.
 *   2. It will not merge two ground segments in one day into one bar. Two
 *      segments are a FLIGHT, not a wait — N59906 on 2025-09-10 is exactly that
 *      case. Every segment is drawn separately and the gap stays visible.
 *   3. It will not say "arrived" or "departed" for ADS-B ground contacts. What
 *      the archives hold is the first and last position a volunteer receiver
 *      HEARD. Set evidence_basis: published_flight_record only when a real
 *      arrival/departure record exists.
 *
 * Usage
 *   node build_overlap_svg.ts <dir-or-info.yaml> [more...]
 *   node build_overlap_svg.ts --all <root-dir>
 *   node build_overlap_svg.ts --all <root-dir> --check     report only, no write
 *   node build_overlap_svg.ts <dir> --out /path/out.svg
 *
 * Node 22+ runs this .ts directly (type stripping). js-yaml resolves from
 * site/node_modules.
 *
 * Exit 0 = everything requested was written (or --check was clean)
 *      2 = at least one input was not drawable
 *      3 = bad usage / unreadable input
 */

import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, basename, resolve, dirname } from "node:path";
import yaml from "js-yaml";

/* ------------------------------------------------------------------ layout */
/* Keep in step with template.svg. Move a constant there, move it here too.   */

const L = {
  W: 1920,
  H: 1080,

  marginL: 64,
  marginR: 64,

  titleY: 60,
  titleSize: 42,
  titleMaxW: 1760,

  // Big name block, frame left, under the title.
  // NEVER WIDER THAN 15% OF THE FRAME.
  nameX: 64,
  nameTopY: 156,
  nameMaxW: 0.15 * 1920, // 288
  nameSizeMax: 78,
  nameLineFactor: 1.06,

  // Airport / state / city / year, frame right, high up, under the title.
  // NEVER WIDER THAN 50% OF THE FRAME.
  rightX: 1856,
  rightTopY: 150,
  rightMaxW: 0.5 * 1920, // 960
  rightAirportSize: 54,
  rightPlaceSize: 46,
  rightYearSize: 88,
  rightLineFactor: 1.1,

  // The town, behind the field. Label rises out of the town centre.
  townX: 660,
  townMarkerY: 330,
  townNameSize: 32,
  townPopSize: 26,

  // Shared time axis.
  axisX0: 260,
  axisX1: 1660,
  axisCapY: 716,
  axisCapSize: 20,
  axisDateY: 754,
  axisDateSize: 26,
  axisTimeY: 792,
  axisTimeSize: 34,
  axisRuleTop: 804,
  axisRuleBottom: 1032,

  // The two bars.
  barLabelSize: 26,
  upperLabelY: 862,
  upperRectY: 872,
  lowerLabelY: 958,
  lowerRectY: 968,
  rectH: 60,
  rectStroke: 5,
  barInset: 6,
  segMinW: 5,

  innerTickBottom: 1038,
  innerLabelY: 1052,
  innerLabelSize: 20,
  innerLabelMinGap: 240,

  footCaptionY: 630,
  footSourceY: 662,
  footSize: 22,
  footMaxW: 1500,
};

const C = {
  green: "#5F9C6C",       // medium green, a shade lighter than mid-range
  grey: "#D9D9D9",
  greyOpacity: 0.5,
  ink: "#000000",
  paper: "#FFFFFF",
  red: "#9B1B1E",         // following / intelligence aircraft
  yellow: "#FFE21F",      // Charlie / Erika / both aircraft
};

/* ------------------------------------------------------------------- types */

type Stamp = { utc?: string; source_zone?: string; source?: string } | string | Date | null | undefined;

type Segment = {
  from?: Stamp;
  to?: Stamp;
  ground_points?: number;
  sources?: string;
  note?: string;
};

type Plane = {
  tail?: string;
  type?: string;
  operator?: string;
  segments?: Segment[];
};

type Info = {
  overlap_id?: string;
  date?: string;
  person?: string;
  dir_name?: string;
  evidence_basis?: string;   // adsb_ground_contact | published_flight_record
  airport?: {
    code?: string;
    name?: string;
    city?: string;
    state?: string;
    state_name?: string;
    timezone?: string;
    town_population?: number | string | null;
    town_population_source?: string;
  };
  following_plane?: Plane;
  kirk_plane?: Plane;
  first_on_ground?: string;
  last_on_ground?: string;
  times_status?: string;
  as_of?: string;
  source_line?: string;
  caption?: string;
  notes?: string;
};

/* --------------------------------------------------------------- utilities */

function esc(s: unknown): string {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/** Rough advance width for a bold-ish sans face. Only used to shrink to fit. */
function textW(s: string, size: number, weight = 700): number {
  return s.length * size * (weight >= 700 ? 0.575 : 0.53);
}

/** Largest size <= max that keeps every line inside maxW. */
function fitSize(lines: string[], max: number, maxW: number, weight = 700): number {
  for (let size = max; size > 10; size--) {
    if (lines.every((l) => textW(l, size, weight) <= maxW)) return size;
  }
  return 10;
}

function parseStamp(v: Stamp, what: string, errs: string[]): number | null {
  if (v === null || v === undefined) { errs.push(`${what}: missing`); return null; }
  if (v instanceof Date) {
    // js-yaml's DEFAULT_SCHEMA turns an ISO timestamp into a Date and throws the
    // zone away. We load with CORE_SCHEMA so this cannot happen — but if a caller
    // loads differently, refuse rather than trust a value we can no longer audit.
    errs.push(`${what}: arrived as a parsed Date, not the original string — load the YAML with js-yaml CORE_SCHEMA so timestamps stay text`);
    return null;
  }
  const raw = typeof v === "string" ? v : v.utc;
  if (raw === null || raw === undefined) { errs.push(`${what}: no "utc:" key`); return null; }
  const s = String(raw).trim();
  if (/^unknown$/i.test(s)) { errs.push(`${what}: unknown — a bar is a claim about a duration and is never estimated`); return null; }
  if (!/(Z|[+-]\d{2}:?\d{2})$/.test(s)) { errs.push(`${what}: "${s}" has no zone designator — an instant must end in Z or an offset`); return null; }
  const t = Date.parse(s);
  if (Number.isNaN(t)) { errs.push(`${what}: unparseable instant "${s}"`); return null; }
  return t;
}

type Seg = { a: number; b: number; points?: number; sources?: string };

function readSegments(p: Plane | undefined, who: string, errs: string[]): Seg[] {
  const segs = p?.segments;
  if (!Array.isArray(segs) || segs.length === 0) {
    errs.push(`${who}.segments: missing or empty — nothing to plot`);
    return [];
  }
  const out: Seg[] = [];
  segs.forEach((s, i) => {
    const a = parseStamp(s.from, `${who}.segments[${i}].from`, errs);
    const b = parseStamp(s.to, `${who}.segments[${i}].to`, errs);
    if (a === null || b === null) return;
    if (b < a) { errs.push(`${who}.segments[${i}]: ends before it starts`); return; }
    out.push({ a, b, points: s.ground_points, sources: s.sources });
  });
  return out.sort((x, y) => x.a - y.a);
}

/* ------------------------------------------------- airport-local formatting */
/* EVERY date and time on this graphic is LOCAL TO THE AIRPORT. Never UTC.    */

function parts(ms: number, tz: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const p of new Intl.DateTimeFormat("en-US", {
    timeZone: tz, weekday: "short", day: "numeric", month: "short",
    year: "numeric", hour: "numeric", minute: "2-digit", hour12: true,
  }).formatToParts(ms)) out[p.type] = p.value;
  return out;
}

/** "Wed 10 Sep" — deliberately NO YEAR. The year lives in the frame-right block. */
const fmtDate = (ms: number, tz: string) => { const p = parts(ms, tz); return `${p.weekday} ${p.day} ${p.month}`; };
/** "3:30 pm" */
const fmtTime = (ms: number, tz: string) => { const p = parts(ms, tz); return `${p.hour}:${p.minute} ${(p.dayPeriod || "").toLowerCase()}`.trim(); };
const fmtYear = (ms: number, tz: string) => parts(ms, tz).year;
const dayKey  = (ms: number, tz: string) => { const p = parts(ms, tz); return `${p.year}-${p.month}-${p.day}`; };
const commas  = (n: number) => n.toLocaleString("en-US");

function durationText(ms: number): string {
  const mins = Math.round(ms / 60000);
  if (mins < 60) return `${mins} min`;
  const h = Math.floor(mins / 60), m = mins % 60;
  if (h < 48) return m ? `${h} hr ${m} min` : `${h} hr`;
  return `${Math.floor(h / 24)} days ${h % 24} hr`;
}

/* -------------------------------------------------------------- name blocks */

const personTitle = (p: string) =>
  p === "charlie" ? "Charlie Kirk" : p === "erika" ? "Erika Kirk" : p === "both" ? "Charlie and Erika Kirk" : p;

/** 2 rows for one name, 3 rows for both — the spec's row counts. */
const personRows = (p: string): string[] =>
  p === "charlie" ? ["Charlie", "Kirk"]
  : p === "erika" ? ["Erika", "Kirk"]
  : p === "both"  ? ["Charlie", "&", "Erika"]
  : personTitle(p).split(/\s+/);

const kirkBarPerson = (p: string) =>
  p === "charlie" ? "Charlie Kirk" : p === "erika" ? "Erika Kirk" : p === "both" ? "Charlie and Erika" : p;

/* ------------------------------------------------------------------ render */

function build(info: Info, dirName: string): { svg: string; warnings: string[] } {
  const errs: string[] = [];
  const warn: string[] = [];

  const person = String(info.person || "").toLowerCase();
  if (!["charlie", "erika", "both"].includes(person)) {
    errs.push(`person: must be charlie | erika | both, got "${info.person}"`);
  }

  const ap = info.airport || {};
  const tz = ap.timezone;
  if (!tz) errs.push("airport.timezone: missing (IANA zone, e.g. America/Denver)");
  else { try { new Intl.DateTimeFormat("en-US", { timeZone: tz }); } catch { errs.push(`airport.timezone: "${tz}" is not an IANA time zone`); } }

  const fSegs = readSegments(info.following_plane, "following_plane", errs);
  const kSegs = readSegments(info.kirk_plane, "kirk_plane", errs);

  if (errs.length) throw new Error("cannot draw this overlap:\n  " + errs.join("\n  "));

  const TZ = tz as string;
  const fp = info.following_plane || {};
  const kp = info.kirk_plane || {};

  const start = Math.min(fSegs[0].a, kSegs[0].a);
  const end = Math.max(fSegs[fSegs.length - 1].b, kSegs[kSegs.length - 1].b);
  const span = end - start;
  if (span <= 0) throw new Error("the time window is zero or negative — nothing to plot");

  /* Do the two aircraft share any ground time at all? Same field on the same
     day is NOT the same as being there together, and the graphic must not let a
     reader assume it was. */
  let simultaneous = 0;
  for (const f of fSegs) for (const k of kSegs) simultaneous += Math.max(0, Math.min(f.b, k.b) - Math.max(f.a, k.a));
  if (simultaneous === 0) {
    warn.push("THE TWO AIRCRAFT WERE NEVER HEARD ON THE GROUND AT THE SAME MOMENT — same field, same day, different hours. The graphic shows the gap; the page must say so too.");
  }

  const heard = (info.evidence_basis || "adsb_ground_contact") === "adsb_ground_contact";
  const vFirst = heard ? "first heard" : "arrived";
  const vLast = heard ? "last heard" : "departed";
  const axisCapL = heard ? "first heard on the ground" : "first arrival";
  const axisCapR = heard ? "last heard on the ground" : "last departure";

  const axisW = L.axisX1 - L.axisX0;
  const xOf = (t: number) => L.axisX0 + ((t - start) / span) * axisW;

  const place = (segs: Seg[]) => segs.map((s) => {
    const x = xOf(s.a);
    let w = xOf(s.b) - x;
    let thin = false;
    if (w < L.segMinW) { w = L.segMinW; thin = true; }
    return { x, w, thin, seg: s };
  });
  const fBars = place(fSegs);
  const kBars = place(kSegs);
  if (fBars.some((b) => b.thin)) warn.push(`following aircraft has a ground contact too short to draw to scale (${durationText(Math.min(...fSegs.map((s) => s.b - s.a)))}) — widened to a visible minimum`);
  if (kBars.some((b) => b.thin)) warn.push(`Kirk-side aircraft has a ground contact too short to draw to scale (${durationText(Math.min(...kSegs.map((s) => s.b - s.a)))}) — widened to a visible minimum`);
  if (fSegs.length > 1) warn.push(`following aircraft has ${fSegs.length} separate ground contacts on this axis — drawn separately, never merged: a gap between two segments is a FLIGHT, not a wait`);
  if (kSegs.length > 1) warn.push(`Kirk-side aircraft has ${kSegs.length} separate ground contacts on this axis — drawn separately, never merged`);

  const multiDay = span >= 24 * 3600 * 1000 || dayKey(start, TZ) !== dayKey(end, TZ);

  /* The two events that are NOT the axis ends: the later of the two first-ons,
     and the earlier of the two last-offs. */
  const laterFirst = fSegs[0].a >= kSegs[0].a ? fSegs[0].a : kSegs[0].a;
  const earlierLast = fSegs[fSegs.length - 1].b <= kSegs[kSegs.length - 1].b ? fSegs[fSegs.length - 1].b : kSegs[kSegs.length - 1].b;

  type Inner = { x: number; trueX: number; lines: string[] };
  const inners: Inner[] = [];
  const innerLines = (t: number, verb: string) =>
    multiDay ? [`${verb} ${fmtDate(t, TZ)} ${fmtTime(t, TZ)}`] : [`${verb} ${fmtTime(t, TZ)}`];
  if (laterFirst > start) inners.push({ x: xOf(laterFirst), trueX: xOf(laterFirst), lines: innerLines(laterFirst, vFirst) });
  if (earlierLast < end) inners.push({ x: xOf(earlierLast), trueX: xOf(earlierLast), lines: innerLines(earlierLast, vLast) });
  // Keep every inner label inside the frame — an early first-contact sits at the
  // far left and a long "first heard Mon 8 Sep 10:20 am" would otherwise clip.
  for (const inner of inners) {
    const half = textW(inner.lines[0], L.innerLabelSize, 500) / 2 + 8;
    inner.x = Math.min(Math.max(inner.x, L.marginL + half), L.W - L.marginR - half);
  }
  if (inners.length === 2 && Math.abs(inners[0].x - inners[1].x) < L.innerLabelMinGap) {
    const mid = (inners[0].x + inners[1].x) / 2, half = L.innerLabelMinGap / 2;
    const [lo, hi] = inners[0].x <= inners[1].x ? [0, 1] : [1, 0];
    inners[lo].x = Math.max(L.marginL + 110, mid - half);
    inners[hi].x = Math.min(L.W - L.marginR - 110, mid + half);
    warn.push("the two inner time labels were pushed apart to stay legible — the tick lines still mark the true positions");
  }

  /* ------------------------------------------------------------ text content */

  const title = `Following plane overlaps with ${personTitle(person)}`;
  const titleSize = fitSize([title], L.titleSize, L.titleMaxW, 600);

  const nameRows = personRows(person);
  const nameSize = fitSize(nameRows, L.nameSizeMax, L.nameMaxW, 800);

  const year = fmtYear(start, TZ);
  const rightRows: { text: string; size: number }[] = [];
  if (ap.name) rightRows.push({ text: String(ap.name), size: L.rightAirportSize });
  const stateText = ap.state_name || ap.state;
  if (stateText) rightRows.push({ text: String(stateText), size: L.rightPlaceSize });
  if (ap.city) rightRows.push({ text: String(ap.city), size: L.rightPlaceSize });
  rightRows.push({ text: year, size: L.rightYearSize });
  for (const r of rightRows) r.size = fitSize([r.text], r.size, L.rightMaxW, 800);

  const contacts = (n: number) => `${n} ground contact${n === 1 ? "" : "s"}`;
  const planeLabel = (p: Plane, lead: string, n: number) =>
    `${lead} — ${p.tail || "tail unknown"}${p.type ? ` (${p.type})` : ""} · ${contacts(n)}`;
  const fLabel = planeLabel(fp, "Following aircraft", fSegs.length);
  const kLabel = planeLabel(kp, `${kirkBarPerson(person)} aircraft`, kSegs.length);
  const barLabelSize = fitSize([fLabel, kLabel], L.barLabelSize, axisW, 600);

  const pop = ap.town_population;
  const popText = pop === null || pop === undefined || pop === "" || String(pop).toLowerCase() === "unknown"
    ? null : `population ${typeof pop === "number" ? commas(pop) : String(pop)}`;
  const townName = [ap.city, ap.state_name || ap.state].filter(Boolean).join(", ");

  const sourceLine = info.source_line ||
    `Source: overlaps.csv + recovered ADS-B traces${info.as_of ? `, as of ${info.as_of}` : ""}`;
  const caption = info.caption || (heard
    ? "ADS-B ground contacts heard by volunteer receivers. Presence only — this places no person aboard either aircraft."
    : "Aircraft ground times only. This places no person aboard either aircraft.");

  /* -------------------------------------------------------------------- svg */

  const out: string[] = [];
  const p = (s: string) => out.push(s);
  const T = (cls: string, x: number, y: number, s: string, anchor?: string, size?: number) =>
    p(`  <text class="t ${cls}"${size ? ` font-size="${size}"` : ""} x="${Math.round(x)}" y="${Math.round(y)}"` +
      `${anchor ? ` text-anchor="${anchor}"` : ""}>${esc(s)}</text>`);
  const line = (x1: number, y1: number, x2: number, y2: number, w = 3) =>
    p(`  <line x1="${Math.round(x1)}" y1="${Math.round(y1)}" x2="${Math.round(x2)}" y2="${Math.round(y2)}" stroke="${C.ink}" stroke-width="${w}"/>`);

  p(`<?xml version="1.0" encoding="UTF-8"?>`);
  p(`<!-- GENERATED by site/docs/Planes/info_graphic/code/build_overlap_svg.ts from info.yaml.`);
  p(`     Do not hand-edit — the next run overwrites it. Edit info.yaml or the generator.`);
  p(`     overlap_id: ${esc(info.overlap_id || "unset")}   built: ${new Date().toISOString().slice(0, 10)} -->`);
  p(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${L.W} ${L.H}" width="${L.W}" height="${L.H}" role="img">`);
  p(`  <title>${esc(title)} — ${esc(ap.name || ap.code || "")}, ${esc(townName)}, ${esc(year)}</title>`);
  p(`  <desc>${esc(`${fLabel}. ${kLabel}. Shared axis runs ${fmtDate(start, TZ)} ${fmtTime(start, TZ)} to ${fmtDate(end, TZ)} ${fmtTime(end, TZ)} ${year}, airport local time, a window of ${durationText(span)}. ${caption}`)}</desc>`);
  p(`  <rect x="0" y="0" width="${L.W}" height="${L.H}" fill="${C.green}"/>`);
  p(`  <!-- BACKGROUND IMAGE SLOT — the generated town/airport scene goes here when it exists.`);
  p(`       <image href="${esc(dirName)}_bg.jpg" x="0" y="0" width="${L.W}" height="${L.H}" preserveAspectRatio="xMidYMid slice"/> -->`);
  p(`  <style>`);
  p(`    .t  { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;`);
  p(`          fill: ${C.paper}; stroke: ${C.ink}; paint-order: stroke; stroke-linejoin: round; }`);
  p(`    .xl { font-weight: 800; stroke-width: 3.5px; }`);
  p(`    .lg { font-weight: 600; stroke-width: 2.5px; }`);
  p(`    .md { font-weight: 700; stroke-width: 2px; }`);
  p(`    .sm { font-weight: 600; stroke-width: 1.6px; }`);
  p(`    .xs { font-size: ${L.innerLabelSize}px; font-weight: 500; stroke-width: 1.2px; }`);
  p(`  </style>`);

  p(`  <!-- title, centred across the whole frame -->`);
  T("lg", L.W / 2, L.titleY, title, "middle", titleSize);

  p(`  <!-- big name block: frame left, never wider than 15% of the frame -->`);
  nameRows.forEach((row, i) => T("xl", L.nameX, L.nameTopY + i * nameSize * L.nameLineFactor, row, undefined, nameSize));

  p(`  <!-- airport / state / city / year: frame right, high, never wider than 50% -->`);
  let ry = L.rightTopY;
  rightRows.forEach((r, i) => {
    T("xl", L.rightX, ry, r.text, "end", r.size);
    const next = rightRows[i + 1];
    // Advance by the NEXT row's size: a big year under a small city line needs
    // the gap sized for the year, not for the city.
    if (next) ry += (r.size * 0.34 + next.size * 0.86);
  });

  if (townName) {
    p(`  <!-- the town behind the field: label rises out of the town centre -->`);
    T("sm", L.townX, L.townMarkerY - (popText ? 106 : 70), townName, "middle", L.townNameSize);
    if (popText) T("sm", L.townX, L.townMarkerY - 70, popText, "middle", L.townPopSize);
    line(L.townX, L.townMarkerY - 54, L.townX, L.townMarkerY);
    p(`  <circle cx="${L.townX}" cy="${L.townMarkerY}" r="6" fill="${C.paper}" stroke="${C.ink}" stroke-width="3"/>`);
  }

  p(`  <!-- shared time axis: left = ${axisCapL}, right = ${axisCapR}. Airport local time. -->`);
  T("xs", L.axisX0, L.axisCapY, axisCapL, "middle");
  T("sm", L.axisX0, L.axisDateY, fmtDate(start, TZ), "middle", L.axisDateSize);
  T("md", L.axisX0, L.axisTimeY, fmtTime(start, TZ), "middle", L.axisTimeSize);
  line(L.axisX0, L.axisRuleTop, L.axisX0, L.axisRuleBottom);
  T("xs", L.axisX1, L.axisCapY, axisCapR, "middle");
  T("sm", L.axisX1, L.axisDateY, fmtDate(end, TZ), "middle", L.axisDateSize);
  T("md", L.axisX1, L.axisTimeY, fmtTime(end, TZ), "middle", L.axisTimeSize);
  line(L.axisX1, L.axisRuleTop, L.axisX1, L.axisRuleBottom);
  T("xs", L.W / 2, L.axisCapY, `window ${durationText(span)} · times local to the airport`, "middle");

  const bg = (y: number) =>
    p(`  <rect x="${L.axisX0}" y="${y}" width="${axisW}" height="${L.rectH}" fill="${C.grey}" fill-opacity="${C.greyOpacity}" stroke="${C.ink}" stroke-width="${L.rectStroke}"/>`);
  const segRects = (bars: ReturnType<typeof place>, y: number, fill: string) => {
    for (const b of bars) {
      p(`  <rect x="${b.x.toFixed(1)}" y="${y + L.barInset}" width="${b.w.toFixed(1)}" height="${L.rectH - 2 * L.barInset}" fill="${fill}">` +
        `<title>${esc(`${fmtTime(b.seg.a, TZ)} to ${fmtTime(b.seg.b, TZ)} (${durationText(b.seg.b - b.seg.a)})${b.seg.points ? `, ${b.seg.points} ground points` : ""}${b.seg.sources ? `, ${b.seg.sources}` : ""}`)}</title></rect>`);
    }
  };

  p(`  <!-- upper bar: the following / intelligence aircraft -->`);
  T("sm", L.axisX0, L.upperLabelY, fLabel, undefined, barLabelSize);
  bg(L.upperRectY);
  segRects(fBars, L.upperRectY, C.red);

  p(`  <!-- lower bar: the ${esc(kirkBarPerson(person))} aircraft -->`);
  T("sm", L.axisX0, L.lowerLabelY, kLabel, undefined, barLabelSize);
  bg(L.lowerRectY);
  segRects(kBars, L.lowerRectY, C.yellow);

  if (inners.length) {
    p(`  <!-- inner labels: the later first-contact and the earlier last-contact -->`);
    for (const inner of inners) {
      line(inner.trueX, L.upperRectY, inner.trueX, L.innerTickBottom);
      if (Math.abs(inner.x - inner.trueX) > 1) line(inner.trueX, L.innerTickBottom, inner.x, L.innerTickBottom + 8, 2);
      inner.lines.forEach((l, i) =>
        T("xs", inner.x, L.innerLabelY + (i - (inner.lines.length - 1)) * 22, l, "middle"));
    }
  }

  p(`  <!-- required furniture: the claim this picture must not be read as, and the source -->`);
  const footSize = fitSize([caption, sourceLine], L.footSize, L.footMaxW, 500);
  T("xs", L.marginL, L.footCaptionY, caption, undefined, footSize);
  T("xs", L.marginL, L.footSourceY, sourceLine, undefined, footSize);
  p(`</svg>`);

  return { svg: out.join("\n") + "\n", warnings: warn };
}

/* -------------------------------------------------------------------- main */

function findInfoDirs(root: string): string[] {
  const found: string[] = [];
  const walk = (d: string) => {
    for (const e of readdirSync(d, { withFileTypes: true })) {
      if (e.name.startsWith(".") || e.name === "node_modules") continue;
      if (e.isDirectory()) walk(join(d, e.name));
    }
    if (existsSync(join(d, "info.yaml"))) found.push(d);
  };
  walk(root);
  return found.sort();
}

function main() {
  const argv = process.argv.slice(2);
  if (!argv.length) {
    console.error("usage: node build_overlap_svg.ts <dir-or-info.yaml>... | --all <root> [--check] [--out <file>]");
    process.exit(3);
  }
  const check = argv.includes("--check");
  const outIdx = argv.indexOf("--out");
  const explicitOut = outIdx >= 0 ? argv[outIdx + 1] : null;

  let targets: string[];
  const allIdx = argv.indexOf("--all");
  if (allIdx >= 0) {
    const root = argv[allIdx + 1];
    if (!root) { console.error("--all needs a root directory"); process.exit(3); }
    targets = findInfoDirs(resolve(root));
    if (!targets.length) { console.error(`no info.yaml found under ${root}`); process.exit(3); }
  } else {
    targets = argv.filter((a, i) => !a.startsWith("--") && argv[i - 1] !== "--out" && argv[i - 1] !== "--all").map((a) => resolve(a));
  }

  let failed = 0, made = 0;
  for (const t of targets) {
    if (!existsSync(t)) { console.error(`MISSING  ${t}`); failed++; continue; }
    const isDir = statSync(t).isDirectory();
    const dir = isDir ? t : dirname(t);
    const yamlPath = isDir ? join(t, "info.yaml") : t;
    if (!existsSync(yamlPath)) { console.error(`MISSING  ${yamlPath}`); failed++; continue; }

    const dirName = basename(dir);
    let info: Info;
    try {
      // CORE_SCHEMA on purpose: the DEFAULT schema parses an ISO timestamp into a
      // JS Date, which discards the written zone designator and would let an
      // unzoned local clock time through as if it were an instant. Keep them text
      // and validate the zone ourselves.
      info = (yaml.load(readFileSync(yamlPath, "utf8"), { schema: yaml.CORE_SCHEMA }) as Info) || {};
    }
    catch (e) { console.error(`BAD YAML ${yamlPath}\n  ${(e as Error).message}`); failed++; continue; }

    try {
      const { svg, warnings } = build(info, dirName);
      const outPath = explicitOut || join(dir, `${info.dir_name || dirName}.svg`);
      if (!check) writeFileSync(outPath, svg, "utf8");
      made++;
      console.log(`${check ? "OK     " : "WROTE  "} ${check ? yamlPath : outPath}`);
      for (const w of warnings) console.log(`  WARN  ${w}`);
    } catch (e) {
      console.error(`CANNOT ${yamlPath}\n  ${(e as Error).message}`);
      failed++;
    }
  }
  console.log(`\n${made} drawable, ${failed} not drawable, ${targets.length} examined.`);
  process.exit(failed ? 2 : 0);
}

main();
