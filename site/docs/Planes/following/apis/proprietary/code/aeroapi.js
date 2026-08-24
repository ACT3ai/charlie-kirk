#!/usr/bin/env node
// FlightAware AeroAPI v4. Pay-per-query, from about $0.002 a query. History runs
// back to 1 January 2011, which is far deeper than anything free reaches - it
// covers the whole 2022-2025 window the trackers counted across.
//
//   GET /aircraft/{registration}/flights?start=&end=      the one we want
//   GET /flights/{ident}
//   GET /airports/{id}/flights
//
//   export AEROAPI_KEY=...
//   node aeroapi.js SU-BTT 2025-09-01 2025-09-15
//
// The header is x-apikey, not Authorization. Results are cursor-paginated via
// links.next. Every page is a separate billed query - watch the count.
import { savePull, getJSON } from "../../public_open_source/code/lib/save.js";
const OUT = new URL("../data/flightaware/", import.meta.url).pathname;
const BASE = "https://aeroapi.flightaware.com/aeroapi";
const key = process.env.AEROAPI_KEY;

export async function aircraftFlights(reg, start, end) {
  let url = `${BASE}/aircraft/${encodeURIComponent(reg)}/flights?start=${start}&end=${end}`;
  const pages = []; let n = 0;
  while (url && n < 10) {
    const { status, text, json } = await getJSON(url, { headers: { "x-apikey": key } });
    await savePull({ dir: `${OUT}${reg}`, name: `${start}_to_${end}_flights_p${n}.json`, url, status, body: text,
      note: "COMMERCIAL RESPONSE - audit trail only, not for republication. Each page is a billed query." });
    pages.push({ status, n });
    url = json?.links?.next ? `${BASE}${json.links.next}` : null;
    n++;
  }
  return pages;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [reg, start, end] = process.argv.slice(2);
  if (!key) {
    console.error("AEROAPI_KEY is not set. BLOCKED on credential - record it in knowledge.mdx.");
    console.error("This is the deepest history available to us (2011 onward) and the one most");
    console.error("likely to settle the 2022-2023 rows the free archive cannot reach.");
    process.exit(3);
  }
  if (!reg || !start || !end) { console.error("usage: aeroapi.js <REG> <YYYY-MM-DD> <YYYY-MM-DD>"); process.exit(2); }
  const pages = await aircraftFlights(reg, start, end);
  console.log(`${reg} ${start}..${end}  ${pages.length} page(s), statuses ${pages.map((p) => p.status).join(",")}`);
}
