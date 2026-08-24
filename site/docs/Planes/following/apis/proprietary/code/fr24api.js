#!/usr/bin/env node
// Flightradar24 official API (fr24api.flightradar24.com). Subscription, bearer
// token, credit-metered. The vendor whose SCREENSHOTS the entire following-planes
// claim was originally read off - which makes its own API the most direct way to
// check whether the screenshots were read correctly.
//
// Endpoints that matter here:
//   /api/flight-summary/full      historic and near-real-time synopsis of flights,
//                                 queryable by registration and date range. THIS IS
//                                 THE ONE. It is the machine-readable form of the
//                                 aircraft-history table people screenshotted.
//   /api/historic/flight-positions/full   historic positional track
//   /api/flight-tracks             full track for a completed flight
//
// CREDENTIAL: FR24_API_TOKEN. It comes from ~/.credentials/charlie_kirk.json
// (charlie_kirk.flight_apis.FR24_API_TOKEN) or from the environment. Never from a
// file in this repo. See ../../public_open_source/code/lib/credentials.js.
//   export FR24_API_TOKEN=...     # optional, overrides the store
//   node fr24api.js SU-BTT 2025-09-01 2025-09-15
//
// TERMS: read them before publishing anything. The finding may be published; the
// payload generally may not be redistributed. Keep the response in ../data/ as our
// audit trail and publish the conclusion with the query date.
import { savePull, getJSON } from "../../public_open_source/code/lib/save.js";
import { byReg } from "../../public_open_source/code/lib/fleet.js";
import { cred, report } from "../../public_open_source/code/lib/credentials.js";
const OUT = new URL("../data/flightradar24/", import.meta.url).pathname;
const BASE = "https://fr24api.flightradar24.com/api";

const headers = () => ({ Authorization: `Bearer ${cred("FR24_API_TOKEN")}`, Accept: "application/json",
                         "Accept-Version": "v1" });

export async function flightSummary(reg, from, to) {
  const url = `${BASE}/flight-summary/full?registrations=${encodeURIComponent(reg)}` +
              `&flight_datetime_from=${from}T00:00:00Z&flight_datetime_to=${to}T23:59:59Z`;
  const { status, text } = await getJSON(url, { headers: headers() });
  await savePull({ dir: `${OUT}${reg}`, name: `${from}_to_${to}_flight_summary.json`, url, status, body: text,
    note: "COMMERCIAL RESPONSE - held as audit trail, NOT for republication. Publish the finding and the query date." });
  return { status, text };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [reg, from, to] = process.argv.slice(2);
  if (!report("FR24_API_TOKEN")) {
    console.error("BLOCKED, and that is the finding: this vendor's own record of the aircraft");
    console.error("its screenshots were read off cannot be checked without a paid subscription.");
    console.error("Record it in knowledge.mdx as blocked-on-credential, do not work around it.");
    process.exit(3);
  }
  if (!reg || !from || !to) { console.error("usage: fr24api.js <REG> <YYYY-MM-DD> <YYYY-MM-DD>"); process.exit(2); }
  if (!byReg(reg)) console.error(`note: ${reg} is not in lib/fleet.js`);
  const r = await flightSummary(reg, from, to);
  console.log(`${reg} ${from}..${to}  HTTP ${r.status}  ${r.text.length} bytes saved`);
}
