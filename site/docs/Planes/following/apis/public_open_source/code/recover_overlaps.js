#!/usr/bin/env node
// EVERY ALLEGED OVERLAP, TESTED AGAINST EVERY FREE ARCHIVE WE HAVE.
//
// recover_erased.js sweeps the three date windows the case turns on. This one
// sweeps the OTHER list: the 85 rows of overlaps.csv -- every date on which a
// foreign-registered aircraft is ALLEGED to have been where Charlie or Erika
// Kirk was. Those dates run from October 2022 to September 2025 and most of
// them have never been pulled at all.
//
// For each alleged (tail, date) it asks the same question of two independent
// volunteer archives, on the day itself and on the day either side of it,
// because an evening US event lands on the NEXT UTC date and a morning one on
// the previous:
//
//   airplanes.live/globe_history   independent network, the BACKUP
//   adsb.lol/globe_history         the archive this investigation already used
//
// WHAT A 404 MEANS HERE. Both free daily archives BEGIN IN 2023. Every 2022
// row will 404 on both, and that is a property of the archives, not of the
// aircraft -- 2022 is reachable only through the ADSBX monthly sample
// (recover_adsbx_samples.js), and only on the 1st of a month. Do not read a
// 2022 404 as a removal. Within 2023-2025, a day one network has and the other
// does not means the two volunteer networks heard differently. That is normal.
// The finding worth having is the opposite one: a date the sheet alleges an
// aircraft was in America where BOTH archives hold a track putting it
// somewhere else. That is testable, and it is what this pull is for.
//
//   node recover_overlaps.js
//   node recover_overlaps.js --tail SU-BND
//   node recover_overlaps.js --no-neighbours     the alleged date only
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { FLEET } from "./lib/fleet.js";
import { scrubVendorCredentials } from "./lib/scrub.js";

const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
           "(KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const PLANES  = new URL("../../../../", import.meta.url).pathname;      // site/docs/Planes/
const FOLLOW  = new URL("../../../", import.meta.url).pathname;         // site/docs/Planes/following/
const OUT     = new URL("../data/recovery/", import.meta.url).pathname;
const NOW     = new Date().toISOString();
const sleep   = (ms) => new Promise((r) => setTimeout(r, ms));

const argv = process.argv.slice(2);
const only = argv.includes("--tail") ? argv[argv.indexOf("--tail") + 1] : null;
const NEIGHBOURS = !argv.includes("--no-neighbours");

const NETWORKS = [
  { key: "airplanes-live", host: "globe.airplanes.live", role: "BACKUP ARCHIVE — independent volunteer network" },
  { key: "adsb-lol",       host: "adsb.lol",             role: "the archive this investigation already used" },
];
const traceURL = (host, hex, date) => {
  const [y, m, d] = date.split("-");
  return `https://${host}/globe_history/${y}/${m}/${d}/traces/${hex.slice(-2)}/trace_full_${hex}.json`;
};

// -------------------------------------------------------------- overlaps.csv
// Minimal CSV reader: the file is quoted and contains commas inside quotes.
function parseCSV(text) {
  const rows = []; let row = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) {
      if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; }
      else if (c === '"') q = false;
      else cell += c;
    } else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n") { row.push(cell); rows.push(row); row = []; cell = ""; }
    else if (c !== "\r") cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const head = rows.shift();
  return rows.filter((r) => r.length > 1).map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] ?? ""])));
}
// "SU-BTT; SU-BND" and "SU-BTT or SU-BND" both mean: test BOTH.
const splitTails = (s) => (s || "").split(/;|\bor\b|\/|,/).map((x) => x.trim().toUpperCase())
  .filter((x) => /^[A-Z0-9]{1,2}-?[A-Z0-9]{2,6}$/.test(x) && x !== "UNKNOWN");
const shift = (date, n) => {
  const d = new Date(date + "T00:00:00Z"); d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
};

async function grab(url) {
  try {
    const res = await fetch(url, { headers: { "User-Agent": UA }, redirect: "follow" });
    const body = await res.text();
    return { status: res.status, body, bytes: Buffer.byteLength(body) };
  } catch (e) { return { status: 0, body: "", bytes: 0, err: String(e) }; }
}
async function save(dir, name, body, meta) {
  await mkdir(dir, { recursive: true });
  let redacted = 0;
  if (typeof body === "string") { const s = scrubVendorCredentials(body); body = s.text; redacted = s.count; }
  if (body) await writeFile(`${dir}/${name}`, body);
  await writeFile(`${dir}/${name}.meta.json`,
    JSON.stringify({ retrieved_utc: NOW, vendor_credentials_redacted: redacted, ...meta }, null, 2) + "\n");
}
function summarise(json) {
  if (!json || !Array.isArray(json.trace) || !json.trace.length) return null;
  const tr = json.trace, t0 = json.timestamp;
  const iso = (s) => new Date((t0 + s) * 1000).toISOString();
  const gnd = (p) => p[3] === "ground";
  const f = tr[0], l = tr[tr.length - 1];
  let up = null, dn = null;
  for (let i = 1; i < tr.length; i++) {
    if (gnd(tr[i - 1]) && !gnd(tr[i]) && !up) up = iso(tr[i][0]);
    if (!gnd(tr[i - 1]) && gnd(tr[i])) dn = iso(tr[i][0]);
  }
  return { registration: json.r ?? null, type: json.t ?? null, points: tr.length,
    first_seen_utc: iso(f[0]), first_pos: [f[1], f[2]],
    last_seen_utc: iso(l[0]),  last_pos: [l[1], l[2]],
    wheels_up_utc: up, wheels_down_utc: dn };
}

// ------------------------------------------------------------------------ run
const csv = parseCSV(await readFile(`${FOLLOW}overlaps.csv`, "utf8"));
const byHex = new Map(FLEET.map((a) => [a.reg.toUpperCase(), a]));

// Build the work list: one entry per (tail, alleged date), carrying every
// overlap_id that alleges it so the recovered file can be traced back.
const work = new Map();
for (const r of csv) {
  const date = (r.date || "").trim();
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) continue;
  for (const t of [...splitTails(r.foreign_tail), ...splitTails(r.kirk_tail)]) {
    if (only && t !== only.toUpperCase()) continue;
    if (!byHex.has(t)) continue;                      // no hex = cannot query
    const k = `${t}|${date}`;
    if (!work.has(k)) work.set(k, { tail: t, date, ids: [], places: [] });
    work.get(k).ids.push(r.overlap_id);
    work.get(k).places.push(`${r.city || "?"}, ${r.state || r.country || "?"}`);
  }
}
const jobs = [...work.values()].sort((a, b) => a.tail.localeCompare(b.tail) || a.date.localeCompare(b.date));
console.log(`${jobs.length} alleged (tail, date) overlaps to test` +
            `${NEIGHBOURS ? ", each with the UTC day either side" : ""}\n`);

const report = { generated_utc: NOW, source: "site/docs/Planes/following/overlaps.csv",
  neighbours: NEIGHBOURS, jobs: jobs.length, results: [] };

for (const job of jobs) {
  const ac = byHex.get(job.tail);
  const dir = `${PLANES}${ac.reg}/data/recovered`;
  const dates = NEIGHBOURS ? [shift(job.date, -1), job.date, shift(job.date, 1)] : [job.date];
  const rec = { ...job, hex: ac.hex, overlap_ids: job.ids, alleged_place: job.places[0], days: [] };
  for (const date of dates) {
    const per = { date, is_alleged_date: date === job.date, sources: {} };
    for (const n of NETWORKS) {
      const url = traceURL(n.host, ac.hex, date);
      const r = await grab(url);
      let sum = null;
      if (r.status === 200) {
        try { sum = summarise(JSON.parse(r.body)); } catch { /* not json */ }
        await save(dir, `${ac.reg}_${date}_${n.key}_trace_full.json`, r.body,
          { source: n.key, source_role: n.role, url, http_status: r.status, bytes: r.bytes,
            tail: ac.reg, hex: ac.hex, utc_date: date, summary: sum,
            pulled_for: "alleged overlap", overlap_ids: job.ids,
            alleged_overlap_date: job.date, alleged_place: job.places[0] });
      }
      per.sources[n.key] = { http: r.status, bytes: r.bytes, summary: sum };
      await sleep(110);
    }
    const a = per.sources["airplanes-live"], b = per.sources["adsb-lol"];
    per.verdict =
      a?.http === 200 && b?.http !== 200 ? "RECOVERED_ONLY_ON_BACKUP" :
      a?.http !== 200 && b?.http === 200 ? "ONLY_ON_ADSB_LOL" :
      a?.http === 200 && b?.http === 200 ? "BOTH_HAVE_IT" : "NEITHER_HAS_IT";
    rec.days.push(per);
  }
  const hit = rec.days.find((d) => d.is_alleged_date);
  const any = rec.days.some((d) => d.verdict !== "NEITHER_HAS_IT");
  rec.alleged_date_verdict = hit.verdict;
  rec.any_track_in_window  = any;
  // Where does the recovered track actually put the aircraft on the alleged day?
  const s = hit.sources["airplanes-live"]?.summary || hit.sources["adsb-lol"]?.summary;
  rec.recovered_first_pos = s?.first_pos ?? null;
  rec.recovered_last_pos  = s?.last_pos  ?? null;
  rec.recovered_points    = s?.points    ?? null;
  report.results.push(rec);
  const tag = any ? (hit.verdict === "NEITHER_HAS_IT" ? "  (track on a NEIGHBOURING day only)" : "  <== TRACK RECOVERED") : "";
  console.log(`  ${rec.tail.padEnd(7)} ${rec.date}  ${rec.overlap_ids.join(",").padEnd(22)} ` +
              `${hit.verdict.padEnd(24)}${tag}`);
}

await mkdir(OUT, { recursive: true });
await writeFile(`${OUT}overlap_recovery_index.json`, JSON.stringify(report, null, 2) + "\n");
const got = report.results.filter((r) => r.alleged_date_verdict !== "NEITHER_HAS_IT").length;
console.log(`\n${got} of ${report.results.length} alleged overlap dates now have a recovered track.`);
console.log(`wrote ${OUT}overlap_recovery_index.json`);
