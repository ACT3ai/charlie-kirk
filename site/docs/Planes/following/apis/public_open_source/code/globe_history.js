#!/usr/bin/env node
// adsb.lol GLOBE HISTORY - the single most valuable free source we have found.
//
// It is the ONLY free, no-account, no-key source of HISTORICAL ADS-B tracks we
// have located. Every other free network (adsb.lol /v2, adsb.fi, airplanes.live,
// OpenSky anonymous) serves LIVE positions only and returns an empty array for an
// aircraft that is not airborne right now.
//
//   https://adsb.lol/globe_history/YYYY/MM/DD/traces/<last2 of hex>/trace_full_<hex>.json
//
// The payload is gzip. It self-identifies the aircraft in "r" (registration) and
// "t" (ICAO type) straight from the feeder database, which is how we settle hex
// disagreements between community registries.
//
// trace[] rows are: [seconds_after_timestamp, lat, lon, alt, gs, track, flags, ...]
// alt is the string "ground" when the aircraft is on the surface.
//
// COUNTERARGUMENT, and it belongs on any page built from this: adsb.lol only sees
// what its volunteer feeders saw. A gap in a trace is a coverage gap first and a
// transponder-off event second, and nothing here can tell the two apart.
//
//   node globe_history.js SU-BTT 2025-09-10
//   node globe_history.js --all 2025-09-10
//   node globe_history.js SU-BTT 2025-09-04 2025-09-11     (inclusive range)

import { gunzipSync } from "node:zlib";
import { FLEET, byReg } from "./lib/fleet.js";
import { savePull, sleep } from "./lib/save.js";

const OUT = new URL("../data/adsb_lol_globe_history/", import.meta.url).pathname;
const url = (hex, d) =>
  `https://adsb.lol/globe_history/${d.replace(/-/g, "/")}/traces/${hex.slice(-2)}/trace_full_${hex}.json`;

function decode(buf) {
  let txt;
  try { txt = gunzipSync(buf).toString("utf8"); } catch { txt = buf.toString("utf8"); }
  return JSON.parse(txt);
}

export async function fetchTrace(ac, day) {
  const u = url(ac.hex, day);
  const res = await fetch(u, { redirect: "follow" });
  const buf = Buffer.from(await res.arrayBuffer());
  if (res.status !== 200) {
    await savePull({ dir: `${OUT}${ac.reg}`, name: `${day}_trace_full.miss.json`, url: u,
      status: res.status, body: null,
      note: "NO TRACE FOR THIS AIRCRAFT ON THIS DATE. Absence of a track is not proof of a covert leg." });
    return { ac, day, status: res.status, points: 0 };
  }
  let d;
  try { d = decode(buf); } catch { return { ac, day, status: res.status, points: 0, error: "undecodable" }; }
  const t0 = d.timestamp;
  const pts = d.trace ?? [];
  const at = (p) => new Date((t0 + p[0]) * 1000).toISOString().replace(".000Z", "Z");
  const summary = {
    icao: d.icao, registration: d.r, type: d.t, description: d.desc,
    db_flags: d.dbFlags, day, points: pts.length,
    first_seen_utc: pts.length ? at(pts[0]) : null,
    last_seen_utc: pts.length ? at(pts[pts.length - 1]) : null,
    first_position: pts.length ? { lat: pts[0][1], lon: pts[0][2], alt: pts[0][3] } : null,
    last_position: pts.length ? { lat: pts.at(-1)[1], lon: pts.at(-1)[2], alt: pts.at(-1)[3] } : null,
    ground_segments: groundSegments(pts, at),
    source_url: u, retrieved_utc: new Date().toISOString(),
  };
  await savePull({ dir: `${OUT}${ac.reg}`, name: `${day}_trace_full.json`, url: u,
    status: res.status, body: JSON.stringify(d), note: `${pts.length} trace points` });
  await savePull({ dir: `${OUT}${ac.reg}`, name: `${day}_summary.json`, url: u,
    status: res.status, body: JSON.stringify(summary, null, 2) + "\n",
    note: "derived summary - the raw trace beside it is the record" });
  return { ac, day, status: 200, points: pts.length, summary };
}

// Contiguous runs where alt === "ground": takeoff and landing bracket the flight.
function groundSegments(pts, at) {
  const segs = []; let start = null;
  for (const p of pts) {
    const onGround = p[3] === "ground";
    if (onGround && start === null) start = p;
    if (!onGround && start !== null) { segs.push({ from: at(start), to: at(p), lat: start[1], lon: start[2] }); start = null; }
  }
  if (start !== null) segs.push({ from: at(start), to: null, lat: start[1], lon: start[2] });
  return segs;
}

function days(a, b) {
  if (!b) return [a];
  const out = []; const d = new Date(a + "T00:00:00Z"); const end = new Date(b + "T00:00:00Z");
  while (d <= end) { out.push(d.toISOString().slice(0, 10)); d.setUTCDate(d.getUTCDate() + 1); }
  return out;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [who, from, to] = process.argv.slice(2);
  if (!who || !from) { console.error("usage: globe_history.js <REG|--all|--following> <YYYY-MM-DD> [YYYY-MM-DD]"); process.exit(2); }
  const list = who === "--all" ? FLEET
    : who === "--following" ? FLEET.filter((a) => a.side === "following")
    : [byReg(who)].filter(Boolean);
  if (!list.length) { console.error(`unknown tail ${who}`); process.exit(2); }
  for (const ac of list) {
    for (const day of days(from, to)) {
      const r = await fetchTrace(ac, day);
      const s = r.summary;
      console.log(`${ac.reg.padEnd(8)} ${day}  HTTP ${r.status}  ${String(r.points).padStart(5)} pts` +
        (s ? `  ${s.first_seen_utc} -> ${s.last_seen_utc}  reg-in-file=${s.registration}` : "  (no trace)"));
      await sleep(400);   // be a good citizen on a volunteer-funded service
    }
  }
}
