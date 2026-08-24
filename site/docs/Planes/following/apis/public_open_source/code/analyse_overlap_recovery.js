#!/usr/bin/env node
// WHAT THE RECOVERED TRACKS ACTUALLY SAY ABOUT EACH ALLEGED OVERLAP.
//
// recover_overlaps.js pulled a track for every alleged (tail, date) in
// overlaps.csv that any free archive still holds. This turns those tracks into
// the only question that matters: ON THE DAY THE SHEET ALLEGES THIS AIRCRAFT WAS
// IN THAT AMERICAN CITY, WHERE DOES THE ADS-B RECORD PUT IT?
//
// The answer is a nearest-airport label with its distance attached, because that
// is all a position is. A track that starts and ends at Cairo does not "refute"
// anything on its own -- but a claim that the aircraft was in Chicago that day is
// testable against it, and this is the test.
//
//   node analyse_overlap_recovery.js
import { readFile, writeFile } from "node:fs/promises";
import { label, nearest } from "./lib/airports.js";

const REC = new URL("../data/recovery/", import.meta.url).pathname;
const FOLLOW = new URL("../../../", import.meta.url).pathname;
const idx = JSON.parse(await readFile(`${REC}overlap_recovery_index.json`, "utf8"));

// Alleged place, from overlaps.csv, per overlap_id.
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
const csv = parseCSV(await readFile(`${FOLLOW}overlaps.csv`, "utf8"));
const byId = new Map(csv.map((r) => [r.overlap_id, r]));

const out = [];
for (const r of idx.results) {
  const row = byId.get(r.overlap_ids[0]) || {};
  const alleged = [row.city, row.state || row.country].filter(Boolean).join(", ") || "unstated";
  const allegedAirport = row.airport_code || null;
  const day = r.days.find((d) => d.is_alleged_date);
  const sum = day?.sources["airplanes-live"]?.summary || day?.sources["adsb-lol"]?.summary || null;

  const rec = {
    overlap_ids: r.overlap_ids, tail: r.tail, date: r.date,
    alleged_place: alleged, alleged_airport: allegedAirport,
    verdict: r.alleged_date_verdict, points: sum?.points ?? null,
    track_starts: null, track_ends: null, same_country_as_alleged: null, test: null,
  };
  if (sum) {
    rec.track_starts = label(sum.first_pos[0], sum.first_pos[1]);
    rec.track_ends   = label(sum.last_pos[0],  sum.last_pos[1]);
    const a = nearest(sum.first_pos[0], sum.first_pos[1]);
    const b = nearest(sum.last_pos[0],  sum.last_pos[1]);
    const usClaim = !!(row.state && row.state.trim());       // an alleged US state
    const inUS = (x) => x?.country === "US";
    rec.same_country_as_alleged = usClaim ? (inUS(a) || inUS(b)) : null;
    // The alleged airport, when the sheet names one, and how far the track is from it.
    if (usClaim) {
      rec.test = (inUS(a) || inUS(b))
        ? "CONSISTENT — the recovered track puts the aircraft in the United States on the alleged day"
        : "INCONSISTENT — the recovered track puts the aircraft outside the United States on the alleged day";
    } else {
      rec.test = "NO US LOCATION ALLEGED — nothing to test against";
    }
  } else {
    rec.test = r.any_track_in_window
      ? "UNTESTED — no track on the alleged day; the archives hold one on a neighbouring day"
      : "UNTESTED — no free archive holds a track for this aircraft on or around this day";
  }
  out.push(rec);
}

const tested = out.filter((r) => r.test.startsWith("CONSISTENT") || r.test.startsWith("INCONSISTENT"));
const consistent = tested.filter((r) => r.test.startsWith("CONSISTENT"));
const summary = {
  generated_utc: new Date().toISOString(),
  alleged_overlaps: out.length,
  with_a_recovered_track_on_the_alleged_day: out.filter((r) => r.points).length,
  testable_against_a_us_claim: tested.length,
  consistent_with_the_claim: consistent.length,
  inconsistent_with_the_claim: tested.length - consistent.length,
  caution: "A nearest-airport label is geometry, not a landing record, and an absent track is an "
         + "absent track -- both free daily archives begin in 2023, so every 2022 row is untestable "
         + "by construction and no 404 here should be read as a removal.",
  rows: out,
};
await writeFile(`${REC}overlap_recovery_analysis.json`, JSON.stringify(summary, null, 2) + "\n");

console.log(`${summary.alleged_overlaps} alleged overlaps | ${summary.with_a_recovered_track_on_the_alleged_day} with a track on the alleged day`);
console.log(`${tested.length} testable against a US claim -> ${consistent.length} consistent, ${tested.length - consistent.length} INCONSISTENT\n`);
for (const r of out.filter((x) => x.points)) {
  console.log(`${r.tail.padEnd(7)} ${r.date}  ${r.overlap_ids.join(",").padEnd(20)} alleged ${r.alleged_place.padEnd(24)}`);
  console.log(`         track ${r.track_starts}  ->  ${r.track_ends}`);
  console.log(`         ${r.test}\n`);
}
console.log(`wrote ${REC}overlap_recovery_analysis.json`);
