#!/usr/bin/env node
// FlightAware AeroAPI v4. History runs back to 1 January 2011, which is far deeper
// than anything free reaches - it covers the whole 2022-2025 window the trackers
// counted across.
//
//   GET /history/flights/{ident}?ident_type=registration&start=&end=   the one we want
//       max 7-day span per call; billed per result set (15 records), and every
//       page is its own result set                                      $0.020
//   GET /aircraft/{ident}/blocked      run FIRST - a blocked tail returns no
//                                      history, and that is an FAA privacy
//                                      filing, never a removal              $0.020
//   GET /aircraft/{ident}/owner        US / AU / NZ registrations only      $0.002
//   GET /history/aircraft/{reg}/last_flight   NOT in the default probe      $0.200
//   GET /history/flights/{id}/track    the flown path of ONE past flight        $0.012
//       CHECKED 2026-09-16: the live /flights/{id}/track refuses anything older
//       than 10 days ("please use the historical version of this endpoint"), and
//       the historical one answers for 2022 flights - 666 positions for SU-BTT's
//       13 Nov 2022 Paris-Wichita leg. Paths across the whole claim window are
//       therefore buyable, one flight at a time.
//   GET /account/usage                 this month's spend, used by the guard $0.000
//
// Prices are FlightAware's published Standard-tier rates, checked 2026-09-14.
//
// CORRECTED 2026-09-14. This client used to call /aircraft/{registration}/flights.
// That is not an AeroAPI v4 resource - the only /aircraft/ resources are blocked,
// owner and types - so every call would have been billed for a 404, up to ten
// pages deep. apis/CLAUDE.md carried the same wrong path in its source register.
//
// THE BUDGET GUARD. The account is on the $100/month Standard tier, and FlightAware's
// pricing page does not say whether usage above that is refused or billed. So this
// client refuses first. Before EVERY billed call it asks /account/usage (free) what
// this month has cost, takes the larger of that and our own spend ledger (usage
// reporting can lag), and stops if the next call would pass either cap:
//   --month-cap  default $90   the whole month, all runs, all machines using this key
//   --budget     default $5    this one run
// A refusal exits 4 and bills nothing. If /account/usage cannot be read, nothing is
// billed either - spending blind is exactly what the guard exists to prevent.
//
// CREDENTIAL: AEROAPI_KEY. It comes from ~/.credentials/charlie_kirk.json
// (charlie_kirk.flight_apis.AEROAPI_KEY) or from the environment. Never from a
// file in this repo. See ../../public_open_source/code/lib/credentials.js.
//
// DRY RUN IS THE DEFAULT. Nothing is billed without --run.
//   node aeroapi.js --usage                                       month so far (free)
//   node aeroapi.js SU-BTT 2025-09-04 2025-09-11                  print the call only
//   node aeroapi.js SU-BTT 2025-09-04 2025-09-11 --run            one page, billed
//   node aeroapi.js SU-BTT 2025-09-04 2025-09-11 --run --max-pages 3 --budget 1
//   node aeroapi.js --probe N102DZ [--run] [--with-last-flight]   blocked (+ owner for US tails)
//
// Node 22 needs no flag for this file; it is plain JavaScript.
import { pathToFileURL } from "node:url";
import { readFile, appendFile, mkdir, access } from "node:fs/promises";
import { savePull, getJSON } from "../../public_open_source/code/lib/save.js";
import { cred, report } from "../../public_open_source/code/lib/credentials.js";
import { privateVendorDir } from "./private_store.js";
// MOVED 2026-09-14. Raw responses are written to the PRIVATE `all` repo, not to
// ../data/flightaware/ - this repo is public and the vendor's terms forbid republishing
// a response. See private_store.js. The published form is ../data/flightaware_restated/.
// (fileURLToPath, not URL.pathname, inside private_store.js: pathname keeps "%20" for
// a space in a directory name, and the first live run wrote into a path containing "%20".)
const OUT = privateVendorDir("flightaware");
const BASE = "https://aeroapi.flightaware.com/aeroapi";
const MAX_SPAN_DAYS = 7;
const PRICE = { history: 0.020, blocked: 0.020, owner: 0.002, last_flight: 0.200, track: 0.012 };
const MONTH_CAP_DEFAULT = 90;
const RUN_BUDGET_DEFAULT = 5;
const SPEND_LEDGER = `${OUT}_spend.csv`;
const NOTE = "COMMERCIAL RESPONSE - audit trail only, not for republication. Each page is a billed query.";
const key = () => cred("AEROAPI_KEY");

export class BudgetError extends Error {}

export function spanDays(start, end) {
  return (Date.parse(`${end}T00:00:00Z`) - Date.parse(`${start}T00:00:00Z`)) / 86400000;
}

export function historyUrl(ident, start, end, identType = "registration") {
  return `${BASE}/history/flights/${encodeURIComponent(ident)}?ident_type=${identType}&start=${start}&end=${end}`;
}

export function probeUrls(ident, { withLastFlight = false } = {}) {
  const id = encodeURIComponent(ident);
  const urls = { blocked: `${BASE}/aircraft/${id}/blocked` };
  // /owner only answers for US, Australian and New Zealand registrations.
  if (/^(N|VH-|ZK-)/i.test(ident)) urls.owner = `${BASE}/aircraft/${id}/owner`;
  if (withLastFlight) urls.last_flight = `${BASE}/history/aircraft/${id}/last_flight`;
  return urls;
}

const monthStart = () => `${new Date().toISOString().slice(0, 7)}-01`;

/** This month's billed total according to FlightAware. Free. Throws if unreadable. */
export async function accountUsage() {
  const { status, json } = await getJSON(`${BASE}/account/usage?start=${monthStart()}`, { headers: { "x-apikey": key() } });
  if (status !== 200 || typeof json?.total_cost !== "number") {
    throw new BudgetError(`account/usage returned HTTP ${status}; refusing to spend without knowing this month's total`);
  }
  return json.total_cost;
}

/** This month's spend according to our own ledger - catches usage that FlightAware has not reported yet. */
export async function ledgerMonthCost() {
  let text;
  try { text = await readFile(SPEND_LEDGER, "utf8"); } catch { return 0; }
  const month = new Date().toISOString().slice(0, 7);
  return text.trim().split("\n").slice(1)
    .filter((r) => r.startsWith(month))
    .reduce((sum, r) => sum + (Number(r.split(",")[3]) || 0), 0);
}

async function logSpend(endpoint, status, cost, url) {
  await mkdir(OUT, { recursive: true });
  let exists = true;
  try { await access(SPEND_LEDGER); } catch { exists = false; }
  const head = exists ? "" : "utc,endpoint,http_status,est_cost_usd,url\n";
  await appendFile(SPEND_LEDGER, `${head}${new Date().toISOString()},${endpoint},${status},${cost.toFixed(3)},${url}\n`);
}

/** Refuse, before spending, if the next call would pass the run budget or the month cap. */
export async function guard(next, { monthCap = MONTH_CAP_DEFAULT, runBudget = RUN_BUDGET_DEFAULT, run = { spent: 0 } } = {}) {
  if (run.spent + next > runBudget) {
    throw new BudgetError(`run budget $${runBudget} would be passed: this run $${run.spent.toFixed(3)} + next call $${next.toFixed(3)}`);
  }
  const account = await accountUsage();
  const local = await ledgerMonthCost();
  const month = Math.max(account, local);
  if (month + next > monthCap) {
    throw new BudgetError(`month cap $${monthCap} would be passed: month so far $${month.toFixed(3)} (FlightAware $${account.toFixed(3)}, local ledger $${local.toFixed(3)}) + next call $${next.toFixed(3)}`);
  }
  return month;
}

async function billed(endpoint, url, opts) {
  const cost = PRICE[endpoint];
  await guard(cost, opts);
  const res = await getJSON(url, { headers: { "x-apikey": key() } });
  // Logged for every HTTP answer, success or not: assume FlightAware bills it.
  await logSpend(endpoint, res.status, cost, url);
  opts.run.spent += cost;
  return res;
}

export async function historyFlights(ident, start, end, { maxPages = 1, identType = "registration", monthCap, runBudget, run = { spent: 0 } } = {}) {
  const days = spanDays(start, end);
  if (!(days > 0) || days > MAX_SPAN_DAYS) {
    throw new Error(`span ${start}..${end} is ${days} days; AeroAPI history allows 1-${MAX_SPAN_DAYS}`);
  }
  const opts = { monthCap, runBudget, run };
  let url = historyUrl(ident, start, end, identType);
  const pages = []; let n = 0;
  while (url && n < maxPages) {
    const { status, text, json } = await billed("history", url, opts);
    await savePull({ dir: `${OUT}${ident}`, name: `${start}_to_${end}_history_p${n}.json`, url, status, body: text, note: NOTE });
    pages.push({ status, n, records: json?.flights?.length ?? 0 });
    // Stop on any non-200. A quota or auth failure must end the window, not be
    // re-probed and billed again, and must never be read as "no flights".
    if (status !== 200) break;
    url = json?.links?.next ? `${BASE}${json.links.next}` : null;
    n++;
  }
  return pages;
}

/** The flown path of one PAST flight. Positions are the vendor's data: they stay in the
 *  private store and are never republished - what goes public is a restated summary. */
export async function historyTrack(faFlightId, { tail, monthCap, runBudget, run = { spent: 0 } } = {}) {
  const opts = { monthCap, runBudget, run };
  const url = `${BASE}/history/flights/${encodeURIComponent(faFlightId)}/track`;
  const { status, text, json } = await billed("track", url, opts);
  await savePull({ dir: `${OUT}${tail || faFlightId.split("-")[0]}/tracks`, name: `${faFlightId}_track.json`, url, status, body: text, note: NOTE });
  return { status, positions: json?.positions?.length ?? 0 };
}

export async function probe(ident, { withLastFlight = false, monthCap, runBudget, run = { spent: 0 } } = {}) {
  const opts = { monthCap, runBudget, run };
  const out = {};
  for (const [name, url] of Object.entries(probeUrls(ident, { withLastFlight }))) {
    const { status, text } = await billed(name, url, opts);
    await savePull({ dir: `${OUT}${ident}`, name: `probe_${name}.json`, url, status, body: text, note: NOTE });
    out[name] = status;
  }
  return out;
}

// pathToFileURL, not `file://${argv[1]}`: the checkout path can contain a space
// (in a directory name), which import.meta.url percent-encodes and argv does not, so the naive
// comparison is silently false and the CLI never runs.
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const flag = (name) => args.includes(name);
  const value = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? Number(args[i + 1]) : fallback; };
  const valued = new Set(["--max-pages", "--month-cap", "--budget"]);
  const pos = args.filter((a, i) => !a.startsWith("--") && !valued.has(args[i - 1]));
  const run = flag("--run");
  const maxPages = value("--max-pages", 1);
  const monthCap = value("--month-cap", MONTH_CAP_DEFAULT);
  const runBudget = value("--budget", RUN_BUDGET_DEFAULT);
  const withLastFlight = flag("--with-last-flight");
  const ctx = { monthCap, runBudget, run: { spent: 0 } };
  const done = (code) => {
    if (ctx.run.spent) console.log(`this run: estimated $${ctx.run.spent.toFixed(3)} billed`);
    process.exit(code);
  };

  try {
    if (flag("--usage")) {
      if (!report("AEROAPI_KEY")) process.exit(3);
      const account = await accountUsage();
      const local = await ledgerMonthCost();
      console.log(`since ${monthStart()}: FlightAware $${account.toFixed(3)}, local ledger $${local.toFixed(3)}; month cap $${monthCap}`);
      process.exit(0);
    }

    if (flag("--probe")) {
      const [ident] = pos;
      if (!ident) { console.error("usage: aeroapi.js --probe <REG> [--run] [--with-last-flight]"); process.exit(2); }
      const urls = probeUrls(ident, { withLastFlight });
      const est = Object.keys(urls).reduce((s, k) => s + PRICE[k], 0);
      if (!run) {
        console.log(`DRY RUN - nothing billed. Would call (est $${est.toFixed(3)}):`);
        for (const u of Object.values(urls)) console.log(`  ${u}`);
        process.exit(0);
      }
      if (!report("AEROAPI_KEY")) process.exit(3);
      console.log(ident, await probe(ident, { withLastFlight, ...ctx }));
      done(0);
    }

    const [reg, start, end] = pos;
    if (!reg || !start || !end) {
      console.error("usage: aeroapi.js <REG> <YYYY-MM-DD> <YYYY-MM-DD> [--run] [--max-pages N] [--budget USD] [--month-cap USD]");
      process.exit(2);
    }
    const days = spanDays(start, end);
    if (!(days > 0) || days > MAX_SPAN_DAYS) {
      console.error(`span ${start}..${end} is ${days} days; AeroAPI history allows 1-${MAX_SPAN_DAYS}`);
      process.exit(2);
    }
    if (!run) {
      console.log(`DRY RUN - nothing billed. Would call, up to ${maxPages} page(s), est up to $${(maxPages * PRICE.history).toFixed(3)}:`);
      console.log(`  ${historyUrl(reg, start, end)}`);
      process.exit(0);
    }
    if (!report("AEROAPI_KEY")) {
      console.error("Record it in knowledge.mdx as blocked-on-credential.");
      process.exit(3);
    }
    const pages = await historyFlights(reg, start, end, { maxPages, ...ctx });
    console.log(`${reg} ${start}..${end}  ${pages.length} page(s), statuses ${pages.map((p) => p.status).join(",")}, records ${pages.map((p) => p.records).join(",")}`);
    done(0);
  } catch (e) {
    if (e instanceof BudgetError) { console.error(`REFUSED - nothing billed for this call. ${e.message}`); done(4); }
    throw e;
  }
}
