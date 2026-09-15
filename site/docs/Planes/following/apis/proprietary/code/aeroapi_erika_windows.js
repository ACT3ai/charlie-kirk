#!/usr/bin/env node
// Run the AeroAPI history pulls planned by plan_erika_windows.py - one call per packed
// 7-day block, for the Erika-claimed rows the free ADS-B archives could not decide.
//
// Every call goes through aeroapi.js, so the budget guard applies to each one: it reads
// this month's spend (free) and refuses before any call that would pass --budget for
// this run or --month-cap for the month. A refusal stops the batch; blocks already
// pulled stay on disk and are skipped on the next run, so a stopped batch resumes.
//
// ONE PAGE PER BLOCK. A block with more flights than one result set (15) says so in the
// output and is NOT paged automatically - more pages are more money, and that is a
// decision, not a default.
//
//   python3 plan_erika_windows.py
//   node aeroapi_erika_windows.js                     dry run: calls and cost, nothing billed
//   node aeroapi_erika_windows.js --run --budget 3
//   node aeroapi_erika_windows.js --plan _erika_plan_kirk.json --run --budget 3
import { readFile, access } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import { historyFlights, BudgetError } from "./aeroapi.js";
import { report } from "../../public_open_source/code/lib/credentials.js";
import { privateVendorDir } from "./private_store.js";

// Plans and raw pulls live in the private `all` repo - see private_store.js.
const DATA = privateVendorDir("flightaware");
const PRICE_HISTORY = 0.020;

const exists = async (p) => { try { await access(p); return true; } catch { return false; } };

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const num = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? Number(args[i + 1]) : fallback; };
  const run = args.includes("--run");
  const runBudget = num("--budget", 3);
  const monthCap = num("--month-cap", 90);
  const pi = args.indexOf("--plan");
  const planName = pi >= 0 ? args[pi + 1] : "_erika_plan.json";

  const plan = JSON.parse(await readFile(`${DATA}${planName}`, "utf8"));
  const todo = [];
  for (const b of plan.blocks) {
    const done = await exists(`${DATA}${b.tail}/${b.start}_to_${b.end}_history_p0.json`);
    todo.push({ ...b, done });
  }
  const pending = todo.filter((b) => !b.done);
  console.log(`${planName}: ${plan.rows.length} rows, ${todo.length} blocks, ${todo.length - pending.length} already on disk, ${pending.length} to pull, est $${(pending.length * PRICE_HISTORY).toFixed(2)}`);

  if (!run) {
    for (const b of pending) console.log(`  DRY RUN  ${b.tail} ${b.start}..${b.end}`);
    console.log("DRY RUN - nothing billed. Add --run to pull.");
    process.exit(0);
  }
  if (!report("AEROAPI_KEY")) process.exit(3);

  const ctx = { monthCap, runBudget, run: { spent: 0 } };
  let more = 0, failed = 0;
  try {
    for (const b of pending) {
      const [page] = await historyFlights(b.tail, b.start, b.end, { maxPages: 1, ...ctx });
      const body = JSON.parse(await readFile(`${DATA}${b.tail}/${b.start}_to_${b.end}_history_p0.json`, "utf8").catch(() => "{}") || "{}");
      const hasMore = Boolean(body?.links?.next);
      if (hasMore) more++;
      if (page.status !== 200) failed++;
      console.log(`  ${page.status}  ${b.tail} ${b.start}..${b.end}  ${page.records} flight(s)${hasMore ? "  MORE PAGES NOT FETCHED" : ""}`);
    }
  } catch (e) {
    if (!(e instanceof BudgetError)) throw e;
    console.error(`REFUSED - batch stopped, nothing billed for the refused call. ${e.message}`);
    console.log(`this run: estimated $${ctx.run.spent.toFixed(3)} billed`);
    process.exit(4);
  }
  console.log(`done. this run: estimated $${ctx.run.spent.toFixed(3)} billed; ${failed} non-200; ${more} block(s) with unfetched pages`);
}
