#!/usr/bin/env node
// THE SCRUBBING DETECTOR.
//
// This is the script that answers "the data is not there any more". The Internet
// Archive CDX API lists every snapshot it holds of a URL, with a timestamp, an HTTP
// status and a content digest. Three things fall out of that list:
//
//   1. A URL that WAS archived and now 404s live  ->  the page was taken down.
//   2. A URL whose digest CHANGES between snapshots -> the content was altered.
//   3. A URL with snapshots that STOP on a date  ->  something changed then.
//
// None of those on its own proves intent. A tracking site reorganising its URLs
// looks identical to a tracking site removing an aircraft. THE PAGE MUST SAY SO.
// What this tool gives you is a dated, checkable record that the public view was
// one thing and is now another - which is worth far more than a memory of it.
//
// No install and no key: this is the plain CDX HTTP API. The `waybackpy` and
// `waybackpack` CLIs wrap the same endpoints if you prefer a command line, but
// nothing here needs them.
//
//   node wayback.js                      the standard target list
//   node wayback.js https://some/url
import { FLEET } from "./lib/fleet.js";
import { savePull, getJSON, sleep } from "./lib/save.js";
const OUT = new URL("../data/wayback/", import.meta.url).pathname;

// The public pages the claim was originally read off. If any of these have moved,
// changed or gone, that is a finding about the evidence base of this whole topic.
export function targets() {
  const t = [];
  for (const ac of FLEET.filter((a) => a.side === "following")) {
    t.push(`https://globe.adsbexchange.com/?icao=${ac.hex}`);
    t.push(`https://www.flightradar24.com/data/aircraft/${ac.reg.toLowerCase()}`);
    t.push(`https://www.flightaware.com/live/flight/${ac.reg}`);
    t.push(`https://www.radarbox.com/data/registration/${ac.reg}`);
    t.push(`https://www.planespotters.net/search?q=${ac.reg}`);
  }
  return t;
}

export async function cdx(url) {
  const q = `https://web.archive.org/cdx/search/cdx?url=${encodeURIComponent(url)}` +
            `&output=json&limit=200&fl=timestamp,original,statuscode,digest,mimetype&collapse=digest`;
  const { status, text, json } = await getJSON(q);
  const rows = Array.isArray(json) && json.length > 1 ? json.slice(1) : [];
  const safe = url.replace(/[^A-Za-z0-9]+/g, "_").slice(0, 120);
  await savePull({ dir: OUT, name: `${safe}_cdx.json`, url: q, status, body: text,
    note: `${rows.length} distinct-content snapshots of ${url}` });
  return { status, rows };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const list = process.argv[2] ? [process.argv[2]] : targets();
  const report = [];
  for (const url of list) {
    const { status, rows } = await cdx(url).catch((e) => ({ status: 0, rows: [], err: e }));
    const first = rows[0]?.[0], last = rows.at(-1)?.[0];
    const fmt = (t) => (t ? `${t.slice(0, 4)}-${t.slice(4, 6)}-${t.slice(6, 8)}` : "—");
    console.log(`${String(rows.length).padStart(4)} snapshots  ${fmt(first)} .. ${fmt(last)}  ${url}`);
    report.push({ url, snapshots: rows.length, first: fmt(first), last: fmt(last),
      statuses: [...new Set(rows.map((r) => r[2]))] });
    await sleep(900);   // the CDX API throttles hard; do not hammer it
  }
  await savePull({ dir: OUT, name: "cdx_report.json", url: "(local summary)", status: 200,
    body: JSON.stringify(report, null, 2) + "\n",
    note: "A URL with zero snapshots was never archived - that is not evidence of removal." });
}
