#!/usr/bin/env node
// THE THIRD BACKUP: samples.adsbexchange.com
//
// ADS-B Exchange sells its historical archive, and this investigation already
// recorded that `globe_history` there returns 403 to the public. But ADSBX also
// publishes a FREE SAMPLE ARCHIVE, and the sample is a WHOLE DAY — the first of
// each month — in the same per-ICAO trace format, going back to July 2016.
//
// That matters here for one specific reason. Both free daily archives
// (adsb.lol, airplanes.live) begin in 2023. The following-planes claim is dated
// from 2022, and this repo has published that those 2022 rows "cannot be tested
// for free at all." The ADSBX monthly sample is the one free source that reaches
// them — on twelve days a year.
//
// WHAT THIS IS AND IS NOT. It is one day in thirty. A 404 here overwhelmingly
// means "not the 1st of the month" or "not heard that day", NOT "removed".
// It cannot test a claim about the 13th of anything. It can establish that an
// airframe existed, flew, and was being received in a month the daily archives
// cannot reach at all.
//
//   node recover_adsbx_samples.js
//   node recover_adsbx_samples.js --tail N102DZ --from 2022-01 --to 2026-08
import { mkdir, writeFile } from "node:fs/promises";
import { scrubVendorCredentials } from "./lib/scrub.js";
import { FLEET } from "./lib/fleet.js";

const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/125.0 Safari/537.36";
const PLANES = new URL("../../../../", import.meta.url).pathname;
const OUT    = new URL("../data/recovery/", import.meta.url).pathname;
const NOW    = new Date().toISOString();
const sleep  = (ms) => new Promise((r) => setTimeout(r, ms));

const argv = process.argv.slice(2);
const arg  = (k, d) => (argv.includes(k) ? argv[argv.indexOf(k) + 1] : d);
const only = arg("--tail", null);
const FROM = arg("--from", "2022-01"), TO = arg("--to", "2026-08");

function months(from, to) {
  const out = []; let [y, m] = from.split("-").map(Number);
  const [ey, em] = to.split("-").map(Number);
  while (y < ey || (y === ey && m <= em)) {
    out.push(`${y}-${String(m).padStart(2, "0")}-01`);
    if (++m > 12) { m = 1; y++; }
  }
  return out;
}
function summarise(j) {
  if (!j || !Array.isArray(j.trace) || !j.trace.length) return null;
  const tr = j.trace, t0 = j.timestamp, iso = (s) => new Date((t0 + s) * 1000).toISOString();
  const grounded = (p) => p[3] === "ground";
  const f = tr[0], l = tr[tr.length - 1];
  return { registration: j.r ?? null, type: j.t ?? null, points: tr.length,
    first_seen_utc: iso(f[0]), first_pos: [f[1], f[2]], first_on_ground: grounded(f),
    last_seen_utc: iso(l[0]),  last_pos: [l[1], l[2]],  last_on_ground: grounded(l) };
}

const fleet = FLEET.filter((a) => (only ? a.reg === only : true));
const report = { generated_utc: NOW, source: "samples.adsbexchange.com/traces (free monthly sample)",
  window: { from: FROM, to: TO }, note:
  "One day per month (the 1st). A 404 means the sample does not hold that airframe that day — " +
  "almost always because it was not heard, not because anything was removed.", hits: [], tails: {} };

for (const ac of fleet) {
  const dir = `${PLANES}${ac.reg}/data/recovered`;
  let found = 0, tried = 0;
  for (const date of months(FROM, TO)) {
    const [y, m, d] = date.split("-");
    const url = `https://samples.adsbexchange.com/traces/${y}/${m}/${d}/${ac.hex.slice(-2)}/trace_full_${ac.hex}.json`;
    tried++;
    let res;
    try { res = await fetch(url, { headers: { "User-Agent": UA } }); } catch { await sleep(150); continue; }
    if (res.status !== 200) { await sleep(120); continue; }
    const body = await res.text();
    let sum = null; try { sum = summarise(JSON.parse(body)); } catch { /* */ }
    await mkdir(dir, { recursive: true });
    const name = `${ac.reg}_${date}_adsbexchange-samples_trace_full.json`;
    // Belt and braces. A raw trace carries no vendor key, so this is normally a
    // no-op recording 0 -- but every capture written by this investigation goes
    // through the same gate, so none can quietly ship one. See lib/scrub.js.
    const scrubbed = scrubVendorCredentials(body);
    await writeFile(`${dir}/${name}`, scrubbed.text);
    await writeFile(`${dir}/${name}.meta.json`, JSON.stringify({
      retrieved_utc: NOW, source: "adsbexchange-samples",
      vendor_credentials_redacted: scrubbed.count,
      source_role: "BACKUP ARCHIVE — ADSBX free monthly sample, reaches back to 2016; " +
                   "the only free source covering the 2022 dates the daily archives do not hold",
      url, http_status: 200, bytes: Buffer.byteLength(body),
      tail: ac.reg, hex: ac.hex, utc_date: date, summary: sum,
    }, null, 2) + "\n");
    found++;
    const pre2023 = date < "2023-03-01";
    console.log(`  ${ac.reg} ${date}  ${String(Buffer.byteLength(body)).padStart(7)} B  ` +
      `${sum?.points ?? "?"} pts${pre2023 ? "   <== PRE-2023: beyond the reach of both daily archives" : ""}`);
    report.hits.push({ tail: ac.reg, date, bytes: Buffer.byteLength(body), summary: sum, pre_2023: pre2023 });
    await sleep(120);
  }
  report.tails[ac.reg] = { hex: ac.hex, months_tried: tried, months_found: found };
  console.log(`${ac.reg}: ${found}/${tried} monthly samples held`);
}
await mkdir(OUT, { recursive: true });
await writeFile(`${OUT}adsbx_samples_index.json`, JSON.stringify(report, null, 2) + "\n");
console.log(`\nwrote ${OUT}adsbx_samples_index.json`);
