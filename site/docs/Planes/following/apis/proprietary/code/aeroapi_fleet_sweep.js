#!/usr/bin/env node
// THE WHOLE-AIRCRAFT SWEEP. Every flight FlightAware holds for the Egyptian tails across
// the years the following-planes claim is counted over - not just the windows somebody
// already claimed an overlap in.
//
// WHY THIS EXISTS. Every earlier pull asked a per-claim question: "was this tail at this
// field on this date?" That can only ever confirm or refute somebody else's list. It can
// never produce the DENOMINATOR - how often these aircraft came to the United States at
// all - and without a denominator "73 overlaps" cannot be judged. This walks the calendar
// instead of the claim list.
//
// HOW. AeroAPI history allows at most 7 days per call, so the range is cut into 7-day
// windows and each is one billed call ($0.020 per result set of 15 flights). A window
// already held on disk is skipped, so a stopped run resumes for free. Pagination is
// followed up to --max-pages; a window with more pages than that says so in the log and
// in the summary, and is never silently truncated.
//
// COST. 209 windows per tail per four years. Five tails, minus what is already held,
// is about 1,025 calls - roughly $20.50. The client's guard reads the month's spend
// before every call and refuses at --budget for this run or --month-cap for the month,
// so the worst case is a stopped batch, not a surprise bill.
//
//   node aeroapi_fleet_sweep.js                                  dry run: the plan and the cost
//   node aeroapi_fleet_sweep.js --run --budget 22
//   node aeroapi_fleet_sweep.js --tails SU-BTV,SU-BGM --run --budget 5
//   node aeroapi_fleet_sweep.js --from 2022-01-01 --to 2026-01-01 --max-pages 3 --run --budget 22
//
// WHAT IT WRITES. Raw responses go to the PRIVATE store (see private_store.js), one file
// per window per page, each with its .meta.json. A ledger row lands in _fleet_sweep_log.csv
// beside them: tail, window, status, flights, whether more pages exist. Nothing here is
// published - analyse_fleet_us.py turns it into the public tables.
import { readFile, writeFile, appendFile, access, mkdir } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import { historyFlights, BudgetError } from "./aeroapi.js";
import { report } from "../../public_open_source/code/lib/credentials.js";
import { privateVendorDir } from "./private_store.js";

const DATA = privateVendorDir("flightaware");
const LOG = `${DATA}_fleet_sweep_log.csv`;
const PRICE_HISTORY = 0.020;
const DEFAULT_TAILS = ["SU-BTT", "SU-BND", "SU-BTU", "SU-BTV", "SU-BGM"];

const exists = async (p) => { try { await access(p); return true; } catch { return false; } };
const iso = (d) => d.toISOString().slice(0, 10);
const addDays = (d, n) => new Date(d.getTime() + n * 86400000);

/** Every UTC day a window file on disk already covers, so we never buy the same week twice. */
export async function coveredDays(tail) {
  const days = new Set();
  const { readdir } = await import("node:fs/promises");
  let names = [];
  try { names = await readdir(`${DATA}${tail}`); } catch { return days; }
  for (const n of names) {
    const m = n.match(/^(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_history_p0\.json$/);
    if (!m) continue;
    for (let d = new Date(`${m[1]}T00:00:00Z`); iso(d) < m[2]; d = addDays(d, 1)) days.add(iso(d));
  }
  return days;
}

export function windows(from, to) {
  const out = [];
  for (let d = new Date(`${from}T00:00:00Z`); iso(d) < to; d = addDays(d, 7)) {
    const end = addDays(d, 7);
    out.push({ start: iso(d), end: iso(end) > to ? to : iso(end) });
  }
  return out;
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const val = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : fallback; };
  const num = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? Number(args[i + 1]) : fallback; };
  const run = args.includes("--run");
  const from = val("--from", "2022-01-01");
  const to = val("--to", "2026-01-01");
  const maxPages = num("--max-pages", 2);
  const runBudget = num("--budget", 22);
  const monthCap = num("--month-cap", 90);
  const tails = val("--tails", DEFAULT_TAILS.join(",")).split(",").map((t) => t.trim()).filter(Boolean);

  const plan = [];
  for (const tail of tails) {
    const covered = await coveredDays(tail);
    for (const w of windows(from, to)) {
      const days = [];
      for (let d = new Date(`${w.start}T00:00:00Z`); iso(d) < w.end; d = addDays(d, 1)) days.push(iso(d));
      if (days.every((d) => covered.has(d))) continue;
      plan.push({ tail, ...w });
    }
  }
  const byTail = Object.fromEntries(tails.map((t) => [t, plan.filter((p) => p.tail === t).length]));
  console.log(`${from} to ${to}, tails ${tails.join(", ")}`);
  for (const [t, n] of Object.entries(byTail)) console.log(`  ${t}: ${n} window(s) to pull`);
  console.log(`total ${plan.length} call(s), est $${(plan.length * PRICE_HISTORY).toFixed(2)} at one page each; run budget $${runBudget}, month cap $${monthCap}`);

  if (!run) {
    console.log("DRY RUN - nothing billed. Add --run to pull.");
    process.exit(0);
  }
  if (!report("AEROAPI_KEY")) process.exit(3);
  await mkdir(DATA, { recursive: true });
  if (!(await exists(LOG))) await writeFile(LOG, "utc,tail,window_start,window_end,http_status,flights,pages_fetched,more_pages_unfetched\n");

  const ctx = { monthCap, runBudget, run: { spent: 0 } };
  let flights = 0, more = 0, failed = 0, done = 0;
  try {
    for (const w of plan) {
      const pages = await historyFlights(w.tail, w.start, w.end, { maxPages, ...ctx });
      const last = pages[pages.length - 1] ?? { status: 0, records: 0 };
      const body = JSON.parse(await readFile(`${DATA}${w.tail}/${w.start}_to_${w.end}_history_p${pages.length - 1}.json`, "utf8").catch(() => "{}") || "{}");
      const hasMore = Boolean(body?.links?.next);
      const n = pages.reduce((s, p) => s + p.records, 0);
      flights += n; done++;
      if (hasMore) more++;
      if (last.status !== 200) failed++;
      await appendFile(LOG, `${new Date().toISOString()},${w.tail},${w.start},${w.end},${last.status},${n},${pages.length},${hasMore}\n`);
      if (n || hasMore || last.status !== 200) {
        console.log(`  ${last.status}  ${w.tail} ${w.start}..${w.end}  ${n} flight(s)${hasMore ? "  MORE PAGES NOT FETCHED" : ""}`);
      } else if (done % 25 === 0) {
        console.log(`  ... ${done}/${plan.length} windows, ${flights} flights so far, $${ctx.run.spent.toFixed(2)} spent`);
      }
    }
  } catch (e) {
    if (!(e instanceof BudgetError)) throw e;
    console.error(`REFUSED - sweep stopped, nothing billed for the refused call. ${e.message}`);
    console.log(`partial: ${done}/${plan.length} windows, ${flights} flights, $${ctx.run.spent.toFixed(3)} billed. Re-run to resume.`);
    process.exit(4);
  }
  console.log(`done. ${done} windows, ${flights} flights, ${failed} non-200, ${more} window(s) with unfetched pages; $${ctx.run.spent.toFixed(3)} billed this run`);
}
