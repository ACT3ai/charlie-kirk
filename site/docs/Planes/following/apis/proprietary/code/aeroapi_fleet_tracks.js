#!/usr/bin/env node
// THE PATHS. One flown track per flight - the positions FlightAware recorded between
// take-off and landing - for the flights the whole-aircraft sweep found.
//
// WHY A SECOND PASS. /history/flights answers WHERE a flight went, not HOW it got there.
// The route between the two airports is a separate purchase, one flight at a time, at
// $0.012 each. That is the difference between "SU-BTT flew Paris to Wichita" and being
// able to draw the line it actually flew across the United States.
//
// CHECKED 2026-09-16. The live /flights/{id}/track refuses any flight more than 10 days
// old and says to use the historical endpoint; the historical one answered for a
// November 2022 flight with 666 positions. Paths are therefore buyable for the whole
// claim window, not just the last week.
//
//   node aeroapi_fleet_tracks.js                          dry run: how many, what it costs
//   node aeroapi_fleet_tracks.js --run --budget 3
//   node aeroapi_fleet_tracks.js --all --run --budget 8   every flight, not only US legs
//   node aeroapi_fleet_tracks.js --tails SU-BTT --run --budget 2
//
// A track already on disk is skipped, so a stopped run resumes for free. Tracks are the
// vendor's data: they stay in the private store and are never republished. What goes
// public is the restated summary - where the path entered and left the country, how high,
// how long - written by the restatement prompt, not the positions themselves.
import { readdir, readFile, appendFile, access, writeFile, mkdir } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import { historyTrack, BudgetError } from "./aeroapi.js";
import { report } from "../../public_open_source/code/lib/credentials.js";
import { privateVendorDir } from "./private_store.js";

const DATA = privateVendorDir("flightaware");
const LOG = `${DATA}_fleet_track_log.csv`;
const PRICE_TRACK = 0.012;
const DEFAULT_TAILS = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM"];
const US = (c) => !!c && (c.startsWith("TJ") || c.startsWith("TI") || (c.length === 4 && (c[0] === "K" || c[0] === "P")));

const exists = async (p) => { try { await access(p); return true; } catch { return false; } };

/** Every flight on disk for a tail, de-duplicated by fa_flight_id. */
export async function flightsOnDisk(tail) {
  let names = [];
  try { names = await readdir(`${DATA}${tail}`); } catch { return []; }
  const out = new Map();
  for (const n of names.filter((n) => /_history_p\d+\.json$/.test(n))) {
    let body;
    try { body = JSON.parse(await readFile(`${DATA}${tail}/${n}`, "utf8")); } catch { continue; }
    for (const f of body?.flights ?? []) {
      if (!f.fa_flight_id) continue;
      const o = f.origin?.code_icao || f.origin?.code || "";
      const d = f.destination?.code_icao || f.destination?.code || "";
      out.set(f.fa_flight_id, {
        tail, id: f.fa_flight_id, date: (f.actual_off || f.scheduled_out || "").slice(0, 10),
        origin: o, destination: d, us: US(o) || US(d),
      });
    }
  }
  return [...out.values()];
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const val = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : fallback; };
  const num = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? Number(args[i + 1]) : fallback; };
  const run = args.includes("--run");
  const all = args.includes("--all");
  const runBudget = num("--budget", 3);
  const monthCap = num("--month-cap", 90);
  const tails = val("--tails", DEFAULT_TAILS.join(",")).split(",").map((t) => t.trim()).filter(Boolean);

  const todo = [];
  for (const tail of tails) {
    for (const f of await flightsOnDisk(tail)) {
      if (!all && !f.us) continue;
      if (await exists(`${DATA}${tail}/tracks/${f.id}_track.json`)) continue;
      todo.push(f);
    }
  }
  todo.sort((a, b) => (a.date + a.tail).localeCompare(b.date + b.tail));
  const byTail = {};
  for (const f of todo) byTail[f.tail] = (byTail[f.tail] ?? 0) + 1;
  console.log(`${all ? "every flight" : "United States legs only"}; ${todo.length} track(s) to pull, est $${(todo.length * PRICE_TRACK).toFixed(2)}`);
  for (const [t, n] of Object.entries(byTail)) console.log(`  ${t}: ${n}`);
  if (!run) { console.log("DRY RUN - nothing billed. Add --run to pull."); process.exit(0); }
  if (!report("AEROAPI_KEY")) process.exit(3);
  await mkdir(DATA, { recursive: true });
  if (!(await exists(LOG))) await writeFile(LOG, "utc,tail,fa_flight_id,date_utc,origin,destination,us_leg,http_status,positions\n");

  const ctx = { monthCap, runBudget, run: { spent: 0 } };
  let ok = 0, failed = 0, positions = 0;
  try {
    for (const f of todo) {
      const res = await historyTrack(f.id, { tail: f.tail, ...ctx });
      if (res.status === 200) { ok++; positions += res.positions; } else failed++;
      await appendFile(LOG, `${new Date().toISOString()},${f.tail},${f.id},${f.date},${f.origin},${f.destination},${f.us},${res.status},${res.positions}\n`);
      console.log(`  ${res.status}  ${f.tail} ${f.date} ${f.origin || "?"}->${f.destination || "?"}  ${res.positions} position(s)`);
    }
  } catch (e) {
    if (!(e instanceof BudgetError)) throw e;
    console.error(`REFUSED - stopped, nothing billed for the refused call. ${e.message}`);
    console.log(`partial: ${ok} track(s), $${ctx.run.spent.toFixed(3)} billed. Re-run to resume.`);
    process.exit(4);
  }
  console.log(`done. ${ok} track(s), ${positions} positions, ${failed} non-200; $${ctx.run.spent.toFixed(3)} billed this run`);
}
