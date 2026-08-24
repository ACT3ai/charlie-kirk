#!/usr/bin/env node
// Ingest traces extracted from an adsb.lol GitHub Release backup into the
// per-aircraft directories, with the source in the filename like every other pull.
//
// The GitHub releases are the OFF-SITE BACKUP of adsb.lol's own archive: one
// release per day, ~3 GB, Open Database Licence. They matter here because the
// live adsb.lol API returns HTTP 403 for a band of dates in late 2025 while the
// backup for those same days is published in full.
//
//   node ingest_github_backup.js <extract-dir> <YYYY-MM-DD>
//
// <extract-dir> is where `tar -xf` put `traces/<xx>/trace_full_<hex>.json`.
// Files inside the archive are gzip-compressed despite the .json name.
import { readdir, readFile, writeFile, mkdir } from "node:fs/promises";
import { gunzipSync } from "node:zlib";
import { FLEET } from "./lib/fleet.js";
const PLANES = new URL("../../../../", import.meta.url).pathname;
const [dir, date] = process.argv.slice(2);
if (!dir || !date) { console.error("usage: ingest_github_backup.js <extract-dir> <YYYY-MM-DD>"); process.exit(1); }
const TAG = `v${date.replace(/-/g, ".")}-planes-readsb-prod-0`;
const byHex = new Map(FLEET.map((a) => [a.hex.toLowerCase(), a]));

async function walk(d) {
  const out = [];
  for (const e of await readdir(d, { withFileTypes: true })) {
    const p = `${d}/${e.name}`;
    if (e.isDirectory()) out.push(...await walk(p));
    else if (/^trace_full_[0-9a-f]{6}\.json$/.test(e.name)) out.push(p);
  }
  return out;
}
function summarise(j) {
  if (!j?.trace?.length) return null;
  const tr = j.trace, t0 = j.timestamp, iso = (s) => new Date((t0 + s) * 1000).toISOString();
  const gnd = (p) => p[3] === "ground";
  const f = tr[0], l = tr[tr.length - 1];
  let up = null, dn = null;
  for (let i = 1; i < tr.length; i++) {
    if (gnd(tr[i - 1]) && !gnd(tr[i]) && !up) up = iso(tr[i][0]);
    if (!gnd(tr[i - 1]) && gnd(tr[i])) dn = iso(tr[i][0]);
  }
  return { registration: j.r ?? null, type: j.t ?? null, points: tr.length,
    first_seen_utc: iso(f[0]), first_pos: [f[1], f[2]], first_on_ground: gnd(f),
    last_seen_utc: iso(l[0]), last_pos: [l[1], l[2]], last_on_ground: gnd(l),
    wheels_up_utc: up, wheels_down_utc: dn };
}

let n = 0;
for (const p of await walk(dir)) {
  const hex = p.match(/trace_full_([0-9a-f]{6})\.json$/)[1];
  const ac = byHex.get(hex);
  if (!ac) continue;
  let raw = await readFile(p);
  if (raw[0] === 0x1f && raw[1] === 0x8b) raw = gunzipSync(raw);
  const body = raw.toString("utf8");
  let sum = null; try { sum = summarise(JSON.parse(body)); } catch { /* */ }
  const out = `${PLANES}${ac.reg}/data/recovered`;
  await mkdir(out, { recursive: true });
  const name = `${ac.reg}_${date}_adsblol-github-backup_trace_full.json`;
  await writeFile(`${out}/${name}`, body);
  await writeFile(`${out}/${name}.meta.json`, JSON.stringify({
    retrieved_utc: new Date().toISOString(),
    source: "adsblol-github-backup",
    source_role: "OFF-SITE BACKUP of the adsb.lol archive — one GitHub release per day, " +
                 "Open Database Licence. Recovers days the live adsb.lol API refuses.",
    url: `https://github.com/adsblol/globe_history_2025/releases/tag/${TAG}`,
    release_tag: TAG, http_status: 200, bytes: Buffer.byteLength(body),
    tail: ac.reg, hex: ac.hex, utc_date: date, summary: sum,
    note: "Extracted from the release tarball by streaming it and filtering to this airframe. " +
          "The live adsb.lol globe_history endpoint returns HTTP 403 for this date.",
  }, null, 2) + "\n");
  console.log(`  ${ac.reg.padEnd(8)} ${date}  ${String(Buffer.byteLength(body)).padStart(8)} B  ${sum?.points ?? "?"} pts -> ${name}`);
  n++;
}
console.log(`ingested ${n} trace(s) from GitHub backup ${TAG}`);
