#!/usr/bin/env node
// TEST ALL 85 CLAIMED OVERLAPS AGAINST PRIMARY ADS-B DATA.
//
// Every one of the 85 rows in overlaps.csv is somebody's READING of a
// flight-tracking website. This script goes to the underlying position data and
// asks one narrow question per row: ON THE CLAIMED DATE, WHERE WAS THE CLAIMED
// AIRCRAFT, according to an archive we pulled ourselves?
//
// TWO INDEPENDENT ARCHIVES, on purpose:
//   adsb.lol          history seen 2023-02-24 .. 2025-10-11, then a site-wide
//                     403 band from 2025-10-12, then a site-wide 404 stretch,
//                     then normal again from about 2026-08-02.
//   airplanes.live    a DIFFERENT volunteer network. History starts in 2024.
// Where both hold a day and agree, that is the strongest thing we can produce.
// Where only one holds it, we say which. Where neither does, WE SAY WE DO NOT
// KNOW -- and that is not a refutation of the claim.
//
// THE VERDICTS, AND WHAT EACH IS WORTH
//   AT_CLAIMED_AIRPORT   a position within RADIUS_KM of the claimed field. The
//                        claim is corroborated by primary data.
//   ELSEWHERE            the aircraft was tracked that day, nowhere near it.
//                        This REFUTES the row, and it is the finding with teeth.
//   NO_ARCHIVE_COVERAGE  neither archive holds the day. NOT a refutation. The
//                        2022-2023 rows land here almost entirely, because no
//                        free archive reaches back that far.
//   NOT_HEARD            an archive holds the day but has no trace for this
//                        airframe. Weak: the fleet does not fly every day, and
//                        Egypt and the mid-Atlantic have thin receiver coverage.
//
// ABSENCE IS NOT PROOF. A tail with no trace on a date was not necessarily
// hidden -- it was, far more often, simply not heard. Only ELSEWHERE refutes.
//
//   node verify_overlaps.js               all 85 rows, +/-1 day
//   node verify_overlaps.js --id OWENS-041
//   node verify_overlaps.js --limit 5
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { FLEET, byReg, following } from "./lib/fleet.js";
import { nearest, label } from "./lib/airports.js";

const FOLLOWING_DIR = new URL("../../../", import.meta.url).pathname;   // following/
const OVERLAPS_CSV  = `${FOLLOWING_DIR}overlaps.csv`;
const OVERLAP_DIR   = `${FOLLOWING_DIR}overlap/`;
const OUT_DIR       = new URL("../data/overlap_verification/", import.meta.url).pathname;
const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const NOW = new Date().toISOString();
const RADIUS_KM = 15;              // generous: covers a big field's whole property
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const NETWORKS = [
  { key: "adsb-lol",       host: "adsb.lol" },
  { key: "airplanes-live", host: "globe.airplanes.live" },
];
const traceURL = (host, hex, d) => {
  const [y, m, dd] = d.split("-");
  return `https://${host}/globe_history/${y}/${m}/${dd}/traces/${hex.slice(-2)}/trace_full_${hex}.json`;
};

// THE CONTROL BASKET. Nine busy airframes with NOTHING to do with this case.
// Before any absence is reported, the same date is asked of these. If one of
// them has a track, the archive HOLDS that date and a missing case aircraft is
// a genuine absence from the record. If none of them does, the archive simply
// does not cover the date, and the case aircraft's absence says nothing at all.
// Every "not heard" verdict below is backed by this probe. It is the difference
// between "the record does not show it" and "we cannot see the record".
const CONTROLS = [
  ["N628TS", "a8ae5f"], ["N509AY", "a66f6b"], ["VH-OQA", "7c6b5b"], ["G-EUUU", "4009a2"],
  ["D-AIBA", "3c4ad1"], ["N582MM", "a7a2b8"], ["N872RA", "ac2f97"], ["N102DZ", "a00c85"],
  ["N1098L", "a0299e"],
];
const archiveCache = new Map();
// Run a list of thunks N-at-a-time. The archives are static files on a CDN and
// tolerate this comfortably; the control calendar is ~1,500 requests and would
// take an hour one at a time.
async function pool(items, n, fn) {
  const out = new Array(items.length); let i = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (i < items.length) { const k = i++; out[k] = await fn(items[k], k); }
  }));
  return out;
}
async function probeCoverage(host, date) {
  let verdict = "NOT_COVERED", codes = [];
  for (const [, hex] of CONTROLS) {
    const r = await grab(traceURL(host, hex, date));
    codes.push(r.status);
    if (r.status === 200) { verdict = "COVERED"; break; }
    if (r.status === 403) { verdict = "FORBIDDEN"; break; }
  }
  return { verdict, codes };
}
async function archiveHolds(host, date) {
  const k = `${host}|${date}`;
  if (archiveCache.has(k)) return archiveCache.get(k);
  const out = await probeCoverage(host, date);
  archiveCache.set(k, out);
  return out;
}

function parseCSV(text) {
  const rows = []; let row = [], cur = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(cur); cur = ""; }
    else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; }
    else if (c !== "\r") cur += c;
  }
  if (cur || row.length) { row.push(cur); rows.push(row); }
  return rows;
}
const shift = (d, n) => { const x = new Date(d + "T00:00:00Z"); x.setUTCDate(x.getUTCDate() + n); return x.toISOString().slice(0, 10); };

// Reduce a trace to the places the aircraft actually WAS, not every fix.
function places(json) {
  if (!json?.trace?.length) return null;
  const t0 = json.timestamp, tr = json.trace;
  const iso = (s) => new Date((t0 + s) * 1000).toISOString().replace(".000Z", "Z");
  const ground = (p) => p[3] === "ground";
  const out = { registration: json.r ?? null, type: json.t ?? null, icao: json.icao ?? null,
                points: tr.length, first_utc: iso(tr[0][0]), last_utc: iso(tr.at(-1)[0]),
                ground_positions: [], airports_touched: [], low_positions: [] };
  const seen = new Set();
  const note = (p, why) => {
    const a = nearest(p[1], p[2]); if (!a) return;
    const key = a.icao;
    if (!seen.has(key)) { seen.add(key); out.airports_touched.push({ icao: a.icao, iata: a.iata, name: a.name,
      city: a.city, region: a.region, country: a.country, km: a.km, first_utc: iso(p[0]), how: why }); }
  };
  for (const p of tr) {
    if (ground(p)) { note(p, "on_ground"); if (out.ground_positions.length < 4) out.ground_positions.push({ utc: iso(p[0]), where: label(p[1], p[2]) }); }
    else if (typeof p[3] === "number" && p[3] < 4000) note(p, "below_4000ft");
  }
  note(tr[0], "first_fix"); note(tr.at(-1), "last_fix");
  out.first_where = label(tr[0][1], tr[0][2]);
  out.last_where  = label(tr.at(-1)[1], tr.at(-1)[2]);
  return out;
}

async function grab(url) {
  try { const r = await fetch(url, { headers: { "User-Agent": UA } });
        return { status: r.status, body: r.status === 200 ? await r.text() : "" }; }
  catch (e) { return { status: 0, body: "", err: String(e) }; }
}

const argv = process.argv.slice(2);
const onlyId = argv.includes("--id") ? argv[argv.indexOf("--id") + 1] : null;
const limit  = argv.includes("--limit") ? +argv[argv.indexOf("--limit") + 1] : Infinity;

const rows = parseCSV(await readFile(OVERLAPS_CSV, "utf8"));
const head = rows[0]; const col = (r, n) => r[head.indexOf(n)] ?? "";
// The five UNPUB- rows carry date "UNKNOWN" on purpose: they are the gap between
// the 67 rows the Owens sheet published and the 72 it claims. There is nothing to
// query for a row with no date, and that is the finding, not a defect.
const DATED = (r) => /^\d{4}-\d{2}-\d{2}$/.test(col(r, "date"));
let claims = rows.slice(1).filter((r) => r.length > 5 && col(r, "date"));
const undated = claims.filter((r) => !DATED(r)).map((r) => col(r, "overlap_id"));
claims = claims.filter(DATED);
if (onlyId) claims = claims.filter((r) => col(r, "overlap_id") === onlyId);
claims = claims.slice(0, limit);

// one network fetch per (hex,date), cached — many rows share dates
const cache = new Map();
async function trace(hex, date) {
  const k = `${hex}|${date}`;
  if (cache.has(k)) return cache.get(k);
  const per = {};
  await Promise.all(NETWORKS.map(async (n) => {
    const r = await grab(traceURL(n.host, hex, date));
    let p = null;
    if (r.status === 200) { try { p = places(JSON.parse(r.body)); } catch { /* not json */ } }
    per[n.key] = { http: r.status, places: p };
  }));
  cache.set(k, per);
  return per;
}

// ---- PREPASS: build the archive-coverage calendar once, concurrently.
// Every "not heard" verdict below points at a row in this calendar, so the
// difference between "the record does not show it" and "we cannot see the
// record" is answerable for every single date without taking it on trust.
const allDates = [...new Set(claims.flatMap((r) => {
  const d = col(r, "date"); return [shift(d, -1), d, shift(d, 1)];
}))].sort();
console.log(`coverage prepass: ${allDates.length} dates x 2 archives ...`);
const pairs = allDates.flatMap((d) => NETWORKS.map((n) => [n.host, d]));
await pool(pairs, 12, async ([host, d]) => {
  archiveCache.set(`${host}|${d}`, await probeCoverage(host, d));
});
const cov0 = { "adsb.lol": {}, "globe.airplanes.live": {} };
for (const [k, v] of archiveCache) { const [h, d] = k.split("|"); cov0[h][v.verdict] = (cov0[h][v.verdict] || 0) + 1; }
console.log("coverage:", JSON.stringify(cov0), "\n");

// ---- PREPASS 2: fetch every (tail, date) trace once, concurrently.
const need = [];
for (const r of claims) {
  const d0 = col(r, "date");
  for (const t of (col(r, "foreign_tail") || "").split(/[;| ]+/).map(s => s.trim()).filter(Boolean)) {
    const ac = byReg(t); if (!ac) continue;
    for (const d of [shift(d0, -1), d0, shift(d0, 1)]) need.push([ac.hex, d]);
  }
}
const uniq = [...new Map(need.map((x) => [x.join("|"), x])).values()];
console.log(`trace prepass: ${uniq.length} (tail,date) pairs ...`);
await pool(uniq, 12, async ([hex, d]) => { await trace(hex, d); });
console.log("traces cached\n");

const report = { generated_utc: NOW, radius_km: RADIUS_KM,
  method: "For each claimed overlap, both free ADS-B history archives were queried for the claimed foreign tail on the claimed date and the day either side. Positions were resolved to the nearest airport in the OurAirports public-domain gazetteer. A verdict of ELSEWHERE refutes a row; NO_ARCHIVE_COVERAGE and NOT_HEARD do not.",
  results: [] };
const tally = {};

for (const r of claims) {
  const id = col(r, "overlap_id"), date = col(r, "date"), apt = col(r, "airport_code");
  const tails = (col(r, "foreign_tail") || "").split(/[;| ]+/).map(s => s.trim()).filter(Boolean);
  const page = col(r, "site_page");
  const rec = { overlap_id: id, date, claimed_airport: apt, claimed_city: col(r, "city"),
                claimed_state: col(r, "state"), claimed_tails: tails, subject: col(r, "subject"),
                audit_verdict: col(r, "audit_verdict"), site_page: page, tails: {} };

  if (!tails.length) { rec.verdict = "NO_TAIL_CLAIMED"; }
  else {
    let best = "NO_ARCHIVE_COVERAGE";
    const rank = { AT_CLAIMED_AIRPORT: 3, ELSEWHERE: 2, NOT_HEARD: 1, NO_ARCHIVE_COVERAGE: 0 };
    for (const t of tails) {
      const ac = byReg(t);
      if (!ac) { rec.tails[t] = { error: "tail not in FLEET - no hex, cannot query" }; continue; }
      const per = {};
      for (const d of [shift(date, -1), date, shift(date, 1)]) {
        const q = await trace(ac.hex, d);
        const hit = q["adsb-lol"].places || q["airplanes-live"].places;
        // Only ask the control basket when the aircraft itself was NOT found --
        // a hit already proves the archive holds the date.
        let cov = null;
        if (!hit) {
          const [cl, ca] = [await archiveHolds("adsb.lol", d), await archiveHolds("globe.airplanes.live", d)];
          cov = { "adsb-lol": cl, "airplanes-live": ca };
        }
        const archiveUp = hit ? true
          : cov["adsb-lol"].verdict === "COVERED" || cov["airplanes-live"].verdict === "COVERED";
        let near = null;
        if (hit) {
          near = hit.airports_touched
            .filter((a) => a.icao === apt || a.iata === apt)
            .sort((a, b) => a.km - b.km)[0] ?? null;
        }
        per[d] = { adsb_lol_http: q["adsb-lol"].http, airplanes_live_http: q["airplanes-live"].http,
                   archive_control_probe: cov,
                   both_agree: !!(q["adsb-lol"].places && q["airplanes-live"].places),
                   heard: !!hit, at_claimed_airport: !!near,
                   airports_touched: hit ? hit.airports_touched.map((a) => `${a.icao} ${a.km}km ${a.how}`) : null,
                   first_where: hit?.first_where ?? null, last_where: hit?.last_where ?? null,
                   points: hit?.points ?? null };
        let v = hit ? (near ? "AT_CLAIMED_AIRPORT" : "ELSEWHERE")
              : archiveUp ? "NOT_HEARD"
              : "NO_ARCHIVE_COVERAGE";
        per[d].verdict = v;
        if (rank[v] > rank[best]) best = v;
      }
      rec.tails[t] = per;
    }
    rec.verdict = best;
  }
  tally[rec.verdict] = (tally[rec.verdict] || 0) + 1;
  report.results.push(rec);
  console.log(`${id.padEnd(11)} ${date} ${apt.padEnd(5)} ${(tails.join("+")||"-").padEnd(14)} ${rec.verdict}`);

  // The extract belongs in the overlap's own directory.
  if (page) {
    const dir = `${OVERLAP_DIR}${page.replace(/\/overview\.mdx$/, "").split("/").pop()}/data`;
    if (existsSync(dir.replace(/\/data$/, ""))) {
      await mkdir(dir, { recursive: true });
      await writeFile(`${dir}/adsb_verification.json`, JSON.stringify({ verified_utc: NOW, ...rec }, null, 2) + "\n");
    }
  }
}

for (const id of undated) {
  report.results.push({ overlap_id: id, date: "UNKNOWN", verdict: "NO_DATE_CLAIMED",
    note: "This row has no date. It is one of the five carried to mark the gap between the 67 rows the source sheet published and the 72 overlaps it claims. A claim with no date cannot be checked by anyone, including its author." });
  tally.NO_DATE_CLAIMED = (tally.NO_DATE_CLAIMED || 0) + 1;
  console.log(`${id.padEnd(11)} UNKNOWN    -     -              NO_DATE_CLAIMED`);
}
report.tally = tally;
await mkdir(OUT_DIR, { recursive: true });
await writeFile(`${OUT_DIR}overlap_verification.json`, JSON.stringify(report, null, 2) + "\n");
console.log("\nTALLY:", JSON.stringify(tally));
console.log(`wrote ${OUT_DIR}overlap_verification.json`);
