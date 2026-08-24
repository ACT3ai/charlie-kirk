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

// NO `collapse=digest`. The earlier version of this function used it, and that
// was a mistake worth recording rather than quietly fixing: collapsing on digest
// returns only DISTINCT-CONTENT captures, so every count it produced was a floor
// and not a total -- and, worse, it made the "did this page stop changing?" test
// impossible by construction, because adjacent identical digests are exactly
// what it throws away. A page that freezes is a page that stopped being updated,
// and that is one of the three things this script exists to detect.
//
// The CDX endpoint also times out under load and answers 504 with an HTML error
// body. A 504 is NOT "zero snapshots" -- it is "we do not know" -- and three of
// the first run's apparent never-archived URLs turned out to be 504s, one of them
// SU-BTT's, the most load-bearing aircraft in the case. Retries and an explicit
// UNKNOWN status exist for that.
export async function cdx(url, { retries = 3 } = {}) {
  const q = `https://web.archive.org/cdx/search/cdx?url=${encodeURIComponent(url)}` +
            `&output=json&limit=2000&fl=timestamp,original,statuscode,digest,mimetype,length`;
  let status = 0, text = "", json = null;
  for (let i = 0; i < retries; i++) {
    ({ status, text, json } = await getJSON(q));
    if (status === 200) break;
    await sleep(4000 * (i + 1));
  }
  const ok = status === 200 && Array.isArray(json);
  const rows = ok && json.length > 1 ? json.slice(1) : [];
  const safe = url.replace(/[^A-Za-z0-9]+/g, "_").slice(0, 120);
  await savePull({ dir: OUT, name: `${safe}_cdx.json`, url: q, status, body: text,
    note: ok
      ? `${rows.length} snapshots of ${url} (TOTAL, not collapsed on digest)`
      : `QUERY FAILED with HTTP ${status}. Snapshot count is UNKNOWN, NOT zero. Re-run before citing this URL.` });
  return { status, rows, ok };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const list = process.argv[2] ? [process.argv[2]] : targets();
  const report = [];
  for (const url of list) {
    const { status, rows, ok } = await cdx(url).catch((e) => ({ status: 0, rows: [], ok: false, err: e }));
    const first = rows[0]?.[0], last = rows.at(-1)?.[0];
    const fmt = (t) => (t ? `${t.slice(0, 4)}-${t.slice(4, 6)}-${t.slice(6, 8)}` : "—");
    // Did the archived page ever stop changing? Adjacent identical digests mean
    // the Archive kept fetching and kept getting the same bytes.
    const digests = rows.map((r) => r[3]);
    let lastChange = null, frozenRuns = 0;
    for (let i = 1; i < rows.length; i++) {
      if (digests[i] !== digests[i - 1]) lastChange = rows[i][0]; else frozenRuns++;
    }
    const codes = [...new Set(rows.map((r) => r[2]))];
    // The one transition that IS a removal signal in this data.
    let firstNon200 = null;
    for (const r of rows) if (r[2] && r[2] !== "200" && r[2] !== "-") { firstNon200 = { ts: r[0], code: r[2] }; break; }
    console.log(`${ok ? String(rows.length).padStart(4) : " ???"} snapshots  ${fmt(first)} .. ${fmt(last)}  ` +
                `codes=${codes.join("/") || "-"}  ${url}${ok ? "" : `   <== QUERY FAILED HTTP ${status}, count UNKNOWN`}`);
    report.push({ url, query_ok: ok, query_http: status,
      snapshots: ok ? rows.length : null,
      snapshots_note: ok ? "total snapshots" : "UNKNOWN - the CDX query failed. This is NOT zero.",
      first: ok ? fmt(first) : null, last: ok ? fmt(last) : null,
      statuses: codes, first_non_200: firstNon200,
      distinct_digests: new Set(digests).size,
      last_digest_change: lastChange ? fmt(lastChange) : null,
      identical_consecutive_captures: frozenRuns,
      by_year: rows.reduce((a, r) => { const y = r[0].slice(0, 4); a[y] = (a[y] || 0) + 1; return a; }, {}) });
    await sleep(900);   // the CDX API throttles hard; do not hammer it
  }
  const failed = report.filter((r) => !r.query_ok).map((r) => r.url);
  await savePull({ dir: OUT, name: "cdx_report.json", url: "(local summary)", status: 200,
    body: JSON.stringify({ generated_utc: new Date().toISOString(), targets: report.length,
      failed_queries: failed, results: report }, null, 2) + "\n",
    note: "A URL with zero snapshots was NEVER ARCHIVED - that is not evidence of removal, it is " +
          "absence of archival interest. A URL whose query FAILED has an UNKNOWN count and must be " +
          "re-run before it is cited either way. Counts here are totals: this query does not " +
          "collapse on digest."});
  if (failed.length) console.log(`\n${failed.length} queries FAILED - counts UNKNOWN, not zero:\n  ` + failed.join("\n  "));
}
