#!/usr/bin/env node
// BULK PULL. Walks the two spine CSVs, works out every (tail, date) that somebody
// has CLAIMED an aircraft was somewhere, and tries to pull the primary ADS-B trace
// for it from adsb.lol globe history.
//
// It writes into THREE places, on purpose:
//
//   1. apis/public_open_source/data/adsb_lol_globe_history/<REG>/   the raw archive
//   2. site/docs/Planes/<REG>/data/adsb/                            the aircraft's own directory
//   3. site/docs/Planes/following/overlap/<KEY>/data/               the overlap's own directory
//
// And where a flight was ALLEGED but no data came back, it writes a MISSING_DATA.md
// into the relevant directory saying what was claimed, who claimed it, what we tried,
// and what we got. THAT FILE IS THE POINT AS MUCH AS THE DATA IS. An absent trace is
// a coverage gap first and a transponder-off event second, and this tool cannot tell
// the two apart - the file says so every time.
//
//   node pull_all.js            dry run, prints the plan
//   node pull_all.js --apply    do it

import { readFile, mkdir, writeFile } from "node:fs/promises";
import { fetchTrace } from "./globe_history.js";
import { FLEET, byReg } from "./lib/fleet.js";

const REPO = "/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk";
const FOLLOW = `${REPO}/site/docs/Planes/following`;
const PLANES = `${REPO}/site/docs/Planes`;
const APPLY = process.argv.includes("--apply");

// T7ELL and EJM36 share one page; everything else is its own directory.
const PAGE_DIR = { T7ELL: "T7ELL-EJM36", EJM36: "T7ELL-EJM36", "T7-ELL": "T7ELL-EJM36" };
const pageDir = (reg) => PAGE_DIR[reg] ?? reg;
const canonical = (reg) => (reg === "T7ELL" ? "T7-ELL" : reg);

function parseCSV(text) {
  const rows = []; let row = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; } else if (c === '"') q = false; else cell += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n") { row.push(cell); rows.push(row); row = []; cell = ""; }
    else if (c !== "\r") cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const head = rows.shift();
  return rows.filter((r) => r.length > 1).map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ""])));
}

const ok = (d) => /^\d{4}-\d{2}-\d{2}$/.test(d);
const shift = (d, n) => { if (!ok(d)) return ""; const x = new Date(d + "T00:00:00Z"); x.setUTCDate(x.getUTCDate() + n); return x.toISOString().slice(0, 10); };

// ---------------------------------------------------------------- build the plan
const flights = parseCSV(await readFile(`${FOLLOW}/flights.csv`, "utf8"));
const overlaps = parseCSV(await readFile(`${FOLLOW}/overlaps.csv`, "utf8"));

/** key: `${reg}|${date}` -> { reg, date, why:[], planeDirs:Set, overlapDirs:Set } */
const plan = new Map();
function want(reg, date, why, overlapKey) {
  reg = canonical((reg || "").trim());
  if (!reg || !ok(date) || !byReg(reg)) return;
  const k = `${reg}|${date}`;
  if (!plan.has(k)) plan.set(k, { reg, date, why: [], overlapDirs: new Set() });
  const e = plan.get(k);
  if (!e.why.includes(why)) e.why.push(why);
  if (overlapKey) e.overlapDirs.add(overlapKey);
}

for (const f of flights) {
  const reg = f.plane_tail_number, s = f.start_date, e = f.end_date;
  const site = `${f.city || "?"}${f.airport_code ? ` (${f.airport_code})` : ""}`;
  if (ok(s)) { want(reg, shift(s, -1), `day before claimed arrival at ${site}`); want(reg, s, `claimed arrival at ${site} - flights.csv`); }
  if (ok(e) && e !== s) { want(reg, e, `claimed departure from ${site} - flights.csv`); want(reg, shift(e, 1), `day after claimed departure from ${site}`); }
}
for (const o of overlaps) {
  const key = (o.overlap_page || "").split("/").pop()?.replace(/\/?overview\.mdx$/, "").replace(/\.mdx$/, "");
  const dirKey = (o.overlap_page || "").replace(/^.*overlap\//, "").replace(/\/?overview\.mdx$/, "").replace(/\.mdx$/, "");
  for (const t of (o.foreign_tail || "").split(";")) {
    const reg = t.trim();
    if (!reg || reg === "UNKNOWN") continue;
    const why = `overlap ${o.overlap_id} - ${o.city || "?"} ${o.state || ""} (${o.confidence || "?"}, audit: ${o.audit_verdict || "untested"})`;
    for (const d of [shift(o.date, -1), o.date, shift(o.date, 1)]) want(reg, d, why, dirKey || key);
  }
}

// The Kirk / TPUSA and N1098L-thread aircraft are NOT in flights.csv - that file is
// deliberately scoped to the FOLLOWING fleet only. But the question "where was
// Charlie's aircraft, where was Erika's aircraft" needs primary data too, so we pull
// a bounded window around the assassination for every one of them. Bounded on
// purpose: 1-15 September 2025. Widening it is a decision a human makes, not a
// default this script takes.
const WINDOW = ["2025-09-01", "2025-09-15"];
for (const ac of FLEET.filter((a) => a.side === "kirk" || a.side === "n1098l")) {
  for (let d = WINDOW[0]; d <= WINDOW[1]; d = shift(d, 1)) {
    want(ac.reg, d, `September 2025 window sweep (${ac.side} side) - not a claimed date, a systematic look`);
  }
}

const entries = [...plan.values()].sort((a, b) => a.reg.localeCompare(b.reg) || a.date.localeCompare(b.date));
console.log(`${entries.length} (tail, date) pulls planned across ${new Set(entries.map(e => e.reg)).size} aircraft`);
if (!APPLY) { for (const e of entries.slice(0, 12)) console.log(`  ${e.reg} ${e.date}  ${e.why[0]}`); console.log("  ...  (--apply to run)"); process.exit(0); }

// ------------------------------------------------------------------------ run it
const results = [];
for (const e of entries) {
  const ac = byReg(e.reg);
  let r;
  try { r = await fetchTrace(ac, e.date); }
  catch (err) { r = { status: 0, points: 0, error: String(err) }; }
  results.push({ ...e, status: r.status, points: r.points, summary: r.summary });
  console.log(`${e.reg.padEnd(8)} ${e.date}  HTTP ${String(r.status).padStart(3)}  ${String(r.points).padStart(5)} pts`);

  const dirs = [`${PLANES}/${pageDir(e.reg)}/data/adsb`, ...[...e.overlapDirs].map((k) => `${FOLLOW}/overlap/${k}/data`)];
  for (const dir of dirs) {
    await mkdir(dir, { recursive: true });
    if (r.points > 0) {
      await writeFile(`${dir}/${e.reg}_${e.date}_summary.json`, JSON.stringify(r.summary, null, 2) + "\n");
    }
  }
  await new Promise((s) => setTimeout(s, 350));
}

// ------------------------------------------------- MISSING_DATA.md for every gap
const misses = results.filter((r) => r.points === 0);
const byDir = new Map();
for (const m of misses) {
  const dirs = [`${PLANES}/${pageDir(m.reg)}/data/adsb`, ...[...m.overlapDirs].map((k) => `${FOLLOW}/overlap/${k}/data`)];
  for (const d of dirs) { if (!byDir.has(d)) byDir.set(d, []); byDir.get(d).push(m); }
}
for (const [dir, ms] of byDir) {
  await mkdir(dir, { recursive: true });
  const lines = [
    "# Claimed flights we could NOT retrieve a primary ADS-B trace for",
    "",
    `Generated ${new Date().toISOString()} by`,
    "`site/docs/Planes/following/apis/public_open_source/code/pull_all.js`.",
    "",
    "**Source tried:** adsb.lol globe history —",
    "`https://adsb.lol/globe_history/YYYY/MM/DD/traces/<hh>/trace_full_<hex>.json`",
    "",
    "This is the only free, no-account source of historical ADS-B tracks we have found.",
    "It serves only what its volunteer feeder network actually received.",
    "",
    "**WHAT AN EMPTY RESULT DOES AND DOES NOT MEAN.** A 404 here means adsb.lol holds no",
    "trace for that airframe on that UTC day. It does **not** establish that the aircraft",
    "did not fly, and it does **not** establish that a transponder was switched off. The",
    "ordinary explanations come first: the aircraft was parked and silent, it flew outside",
    "volunteer receiver coverage (most of the Atlantic, most of North Africa, much of the",
    "rural US at low altitude), or the claimed date is simply wrong. Several of the rows",
    "below are already recorded in `overlaps.csv` as audited inaccurate.",
    "",
    "**The claim is what is listed. The absence is what we found. Neither is proof.**",
    "",
    "| Tail | UTC date | HTTP | Why we looked |",
    "|---|---|---|---|",
    ...ms.map((m) => `| ${m.reg} | ${m.date} | ${m.status} | ${m.why.join("; ").replace(/\|/g, "/")} |`),
    "",
  ];
  await writeFile(`${dir}/MISSING_DATA.md`, lines.join("\n"));
}

const hit = results.filter((r) => r.points > 0);
console.log(`\n${hit.length} traces retrieved, ${misses.length} claimed dates with no trace`);
console.log(`MISSING_DATA.md written into ${byDir.size} directories`);
await writeFile(`${new URL("../data/", import.meta.url).pathname}pull_all_index.json`,
  JSON.stringify(results.map(({ summary, ...r }) => ({ ...r, overlapDirs: [...r.overlapDirs] })), null, 2) + "\n");
