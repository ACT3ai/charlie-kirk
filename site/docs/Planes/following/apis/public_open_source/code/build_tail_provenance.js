#!/usr/bin/env node
// WHAT WE ACTUALLY HOLD, PER AIRCRAFT — the provenance ledger behind every
// aircraft page.
//
// Every trace file this investigation has pulled carries a .meta.json sidecar
// naming the source, the URL, the HTTP status and the byte count. This walks all
// of them and answers, for one tail at a time:
//
//   * which archives hold this airframe, and over what span
//   * which days only ONE archive has  (the recovery finding)
//   * which days BOTH have             (the corroboration finding)
//   * where the aircraft actually was, resolved to named airports
//   * which tracking-site pages were archived, and what they show today
//
// THE HONEST FRAME. A day present in one archive and absent from the other is
// ORDINARY. Volunteer receiver networks differ by geography and by who is
// feeding them; Egypt and the mid-Atlantic are thin for both. It becomes a
// finding only when the missing side is missing for EVERY aircraft including
// controls -- which is an archive-wide condition -- or when a page that was
// public stops being public. Both of those are computed here and labelled.
import { readdir, readFile, writeFile, mkdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import { FLEET } from "./lib/fleet.js";
import { label, nearest } from "./lib/airports.js";

const PLANES = new URL("../../../../", import.meta.url).pathname;
const OUT = new URL("../data/provenance/", import.meta.url).pathname;
const NOW = new Date().toISOString();

// Control-verified coverage of the two free archives, as measured on 2026-08-24
// by asking each date of a basket of unrelated aircraft. These are properties of
// the ARCHIVES, not of any airframe, and no page may report them otherwise.
const ARCHIVE_CONDITIONS = [
  { network: "adsb.lol", from: "2025-10-12", to: "2025-12-30", http: 403,
    finding: "SITE-WIDE. Every aircraft asked returns 403, including controls with no connection to this case." },
  { network: "adsb.lol", from: "2025-12-31", to: "2026-08-01", http: 404,
    finding: "SITE-WIDE. The archive holds nothing at all for this stretch, for any aircraft." },
];

async function metas(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const f of await readdir(dir)) {
    if (!f.endsWith(".meta.json")) continue;
    try { out.push({ file: f, ...JSON.parse(await readFile(`${dir}/${f}`, "utf8")) }); } catch { /* */ }
  }
  return out;
}

const all = {};
for (const ac of FLEET) {
  const dir = `${PLANES}${ac.reg}/data`;
  const rows = [...await metas(`${dir}/recovered`), ...await metas(`${dir}/adsb`)];
  const byDate = new Map(), pages = [], legs = [];
  let redactions = 0;

  for (const m of rows) {
    redactions += m.vendor_credentials_redacted || 0;
    if (m.source?.startsWith("wayback/")) {
      pages.push({ site: m.source.split("/")[1], snapshot_utc: m.snapshot_utc,
        original_url: m.original_url, archived_http: m.http_status,
        live_http_today: m.live_http_today, bytes: m.bytes,
        flight_rows_recovered: m.flight_rows_recovered ?? null, table_state: m.table_state ?? null });
      continue;
    }
    const d = m.utc_date; if (!d || m.http_status !== 200) continue;
    if (!byDate.has(d)) byDate.set(d, { date: d, sources: {}, where: null });
    const e = byDate.get(d);
    e.sources[m.source] = { bytes: m.bytes, points: m.summary?.points ?? null };
    const s = m.summary;
    if (s && !e.where && s.first_pos && s.last_pos) {
      e.where = { first_utc: s.first_seen_utc, first: label(...s.first_pos),
                  last_utc: s.last_seen_utc, last: label(...s.last_pos),
                  wheels_up_utc: s.wheels_up_utc ?? null, wheels_down_utc: s.wheels_down_utc ?? null,
                  points: s.points };
      const a = nearest(...s.last_pos), b = nearest(...s.first_pos);
      e.from_icao = b?.icao ?? null; e.to_icao = a?.icao ?? null;
      e.from_km = b?.km ?? null; e.to_km = a?.km ?? null;
      e.on_ground_at_end = s.last_on_ground ?? null;
    }
  }

  const days = [...byDate.values()].sort((a, b) => a.date.localeCompare(b.date));
  const has = (e, k) => k in e.sources;
  const both  = days.filter((e) => has(e, "adsb-lol") && has(e, "airplanes-live"));
  const onlyA = days.filter((e) => has(e, "airplanes-live") && !has(e, "adsb-lol") && !has(e, "adsb-lol-daily"));
  const samplesOnly = days.filter((e) => Object.keys(e.sources).length === 1 && has(e, "adsbexchange-samples"));
  const pre2023 = days.filter((e) => e.date < "2023-01-01");
  const bySource = {};
  for (const e of days) for (const s of Object.keys(e.sources)) bySource[s] = (bySource[s] || 0) + 1;

  const airports = {};
  for (const e of days) for (const k of [e.from_icao, e.to_icao]) if (k) airports[k] = (airports[k] || 0) + 1;

  all[ac.reg] = {
    reg: ac.reg, hex: ac.hex, side: ac.side, type: ac.type, registry: ac.registry, note: ac.note,
    days_held: days.length,
    span: days.length ? { earliest: days[0].date, latest: days.at(-1).date } : null,
    earliest_primary_trace: days.length ? days[0].date : null,
    days_by_source: bySource,
    corroborated_both_archives: both.length,
    recovered_only_on_backup: onlyA.length,
    recovered_only_from_monthly_samples: samplesOnly.length,
    days_before_2023: pre2023.length,
    pre_2023_dates: pre2023.map((e) => e.date),
    airports_touched: Object.entries(airports).sort((a, b) => b[1] - a[1]).map(([k, v]) => ({ icao: k, days: v })),
    archived_pages: pages.sort((a, b) => (a.snapshot_utc || "").localeCompare(b.snapshot_utc || "")),
    page_rows_recovered: pages.reduce((n, p) => n + (p.flight_rows_recovered || 0), 0),
    pages_public_then_not_now: pages.filter((p) => p.archived_http === 200 && p.live_http_today !== 200).length,
    vendor_credentials_redacted_in_captures: redactions,
    days: days,
  };
  console.log(`${ac.reg.padEnd(8)} days=${String(days.length).padStart(3)}  ` +
    `both=${String(both.length).padStart(3)} backup_only=${String(onlyA.length).padStart(3)} ` +
    `samples_only=${String(samplesOnly.length).padStart(3)} pre2023=${String(pre2023.length).padStart(2)}  ` +
    `pages=${pages.length} rows=${all[ac.reg].page_rows_recovered}  ` +
    `span=${all[ac.reg].span ? all[ac.reg].span.earliest + ".." + all[ac.reg].span.latest : "-"}`);
}

await mkdir(OUT, { recursive: true });
await writeFile(`${OUT}tail_provenance.json`,
  JSON.stringify({ generated_utc: NOW, archive_conditions: ARCHIVE_CONDITIONS, tails: all }, null, 2) + "\n");
console.log(`\nwrote ${OUT}tail_provenance.json`);
