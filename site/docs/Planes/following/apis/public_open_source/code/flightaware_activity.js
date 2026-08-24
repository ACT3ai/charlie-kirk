#!/usr/bin/env node
// FLIGHTAWARE'S SERVER-RENDERED ACTIVITY LOG. A fifth free route, found while
// running the recovery sweep.
//
// FlightAware's per-aircraft page ships a JSON blob in the HTML --
// `var trackpollBootstrap = {...}` -- carrying `activityLog.flights`: origin,
// destination, actual takeoff and landing times, aircraft type. No key, no
// account, and unlike FlightRadar24 the site serves a plain script (HTTP 200).
//
// WHAT IT IS NOT. It is NOT a recovery route. The free log reaches back roughly a
// week, the same as everyone else's free tier -- SU-BTT returned 11 legs spanning
// 2026-08-11 to 2026-08-19. It cannot reach 2022, or 2025, or the September window.
// What it IS: a current, NAMED-AIRPORT record of where these aircraft are flying
// now, from a source independent of the ADS-B archives, without our having to
// resolve coordinates to fields ourselves.
//
//   node flightaware_activity.js
//   node flightaware_activity.js --tail N1098L
import { mkdir, writeFile } from "node:fs/promises";
import { FLEET } from "./lib/fleet.js";
import { scrubVendorCredentials } from "./lib/scrub.js";

const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
           "(KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const PLANES = new URL("../../../../", import.meta.url).pathname;
const OUT    = new URL("../data/recovery/", import.meta.url).pathname;
const NOW    = new Date().toISOString();
const sleep  = (ms) => new Promise((r) => setTimeout(r, ms));
const argv = process.argv.slice(2);
const only = argv.includes("--tail") ? argv[argv.indexOf("--tail") + 1] : null;

const iso = (s) => (s ? new Date(s * 1000).toISOString() : null);
const report = { generated_utc: NOW, source: "flightaware.com activity log (server-rendered)",
  reach: "the free log runs roughly one week back; this is CURRENT activity, not a historical recovery",
  tails: {} };

for (const ac of FLEET.filter((a) => (only ? a.reg === only : true))) {
  // FlightAware wants the ident with no dash for foreign registrations.
  const idents = [...new Set([ac.reg, ac.reg.replace(/-/g, "")])];
  let got = null, usedURL = null, status = 0;
  for (const id of idents) {
    const url = `https://www.flightaware.com/live/flight/${id}`;
    const res = await fetch(url, { headers: { "User-Agent": UA } }).catch(() => null);
    if (!res) { await sleep(800); continue; }
    status = res.status;
    const html = await res.text();
    const m = html.match(/var trackpollBootstrap = (\{[\s\S]*?\});/);
    if (m) {
      try {
        const j = JSON.parse(m[1]);
        const key = Object.keys(j.flights || {})[0];
        const log = j.flights?.[key]?.activityLog?.flights || [];
        if (log.length || !got) { got = log; usedURL = url; }
        if (log.length) break;
      } catch { /* not parseable */ }
    }
    await sleep(800);
  }
  const legs = (got || []).map((f) => ({
    ident: f.ident || null,
    from: f.origin?.friendlyName ?? null, from_icao: f.origin?.icao ?? null,
    to: f.destination?.friendlyName ?? null, to_icao: f.destination?.icao ?? null,
    takeoff_utc: iso(f.takeoffTimes?.actual), landing_utc: iso(f.landingTimes?.actual),
    scheduled_out_utc: iso(f.gateDepartureTimes?.scheduled),
    aircraft_type: f.aircraftTypeFriendly || f.aircraftType || null,
  })).filter((l) => l.from || l.to);

  const dates = legs.map((l) => (l.takeoff_utc || l.scheduled_out_utc || "").slice(0, 10)).filter(Boolean).sort();
  report.tails[ac.reg] = { hex: ac.hex, side: ac.side, http: status, url: usedURL,
    legs: legs.length, earliest: dates[0] ?? null, latest: dates.at(-1) ?? null, flights: legs };

  const dir = `${PLANES}${ac.reg}/data/recovered`;
  await mkdir(dir, { recursive: true });
  const name = `${ac.reg}_${NOW.slice(0, 10)}_flightaware_activity_log.json`;
  const body = scrubVendorCredentials(JSON.stringify(report.tails[ac.reg], null, 2) + "\n");
  await writeFile(`${dir}/${name}`, body.text);
  await writeFile(`${dir}/${name}.meta.json`, JSON.stringify({
    retrieved_utc: NOW, source: "flightaware-activity-log",
    source_role: "FlightAware's server-rendered activity log — free, no account, reaches about a week back",
    url: usedURL, http_status: status, tail: ac.reg, hex: ac.hex,
    legs: legs.length, covers: [report.tails[ac.reg].earliest, report.tails[ac.reg].latest],
    vendor_credentials_redacted: body.count,
  }, null, 2) + "\n");

  console.log(`  ${ac.reg.padEnd(7)} http=${status} legs=${String(legs.length).padStart(3)}  ` +
              `${report.tails[ac.reg].earliest ?? "—"} .. ${report.tails[ac.reg].latest ?? "—"}`);
  await sleep(900);
}
await mkdir(OUT, { recursive: true });
await writeFile(`${OUT}flightaware_activity_index.json`, JSON.stringify(report, null, 2) + "\n");
console.log(`\nwrote ${OUT}flightaware_activity_index.json`);
