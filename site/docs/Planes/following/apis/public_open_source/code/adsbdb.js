#!/usr/bin/env node
// adsbdb.com - free, no key, no rate limit published. Aircraft metadata and
// callsign->route lookup, built from open registry data.
//
// WHAT IT IS GOOD FOR: turning a tail number into an ICAO hex, a type, and a
// registered owner. That is how the FLEET table in lib/fleet.js was built and how
// the "Government of Egypt" registered-owner string was confirmed for all five SU-
// tails without relying on a single X post.
//
// WHAT IT IS NOT: a flight history. It holds no positions and no dates.
//
// KNOWN CONFLICT, recorded not hidden: adsbdb returns mode_s 0101F0 for SU-BTT.
// The adsb.lol historical trace for 0101D3 self-identifies as SU-BTT and carries
// a real track; 0101F0 has none. Both are community databases. We use 0101D3
// because the trace is a primary observation and the registry entry is a lookup.
//
//   node adsbdb.js              every tail in the fleet
//   node adsbdb.js SU-BTT
import { FLEET, byReg } from "./lib/fleet.js";
import { savePull, getJSON, sleep } from "./lib/save.js";
const OUT = new URL("../data/adsbdb/", import.meta.url).pathname;

export async function aircraft(reg) {
  const url = `https://api.adsbdb.com/v0/aircraft/${encodeURIComponent(reg)}`;
  const { status, text, json } = await getJSON(url);
  await savePull({ dir: OUT, name: `${reg}_aircraft.json`, url, status, body: text });
  return { status, ac: json?.response?.aircraft ?? null };
}
export async function callsign(cs) {
  const url = `https://api.adsbdb.com/v0/callsign/${encodeURIComponent(cs)}`;
  const { status, text, json } = await getJSON(url);
  await savePull({ dir: OUT, name: `${cs}_callsign.json`, url, status, body: text });
  return { status, route: json?.response?.flightroute ?? null };
}
if (import.meta.url === `file://${process.argv[1]}`) {
  const arg = process.argv[2];
  const list = arg ? [byReg(arg) ?? { reg: arg }] : FLEET;
  for (const a of list) {
    const { status, ac } = await aircraft(a.reg);
    console.log(`${a.reg.padEnd(9)} HTTP ${status}  ` + (ac
      ? `hex=${ac.mode_s} type=${ac.icao_type} owner=${ac.registered_owner} (${ac.registered_owner_country_name})`
      : "NO REGISTRY RECORD"));
    await sleep(250);
  }
}
