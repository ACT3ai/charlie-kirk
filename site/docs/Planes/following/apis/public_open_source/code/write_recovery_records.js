#!/usr/bin/env node
// Writes {tail}/data/recovered/_RECOVERED_DATA.md — the per-aircraft record of
// WHAT WAS NOT AVAILABLE, WHERE IT WAS NOT AVAILABLE FROM, AND WHAT WE GOT BACK.
//
// Leading underscore so Docusaurus does not publish it as a page (see the
// exclude list in site/docusaurus.config.ts). It is the audit trail that sits
// beside the recovered payloads, not a public page.
import { readdir, readFile, writeFile, stat } from "node:fs/promises";
import { FLEET } from "./lib/fleet.js";
const PLANES = new URL("../../../../", import.meta.url).pathname;
const NOW = new Date().toISOString();

const SOURCES = {
  "airplanes-live": {
    name: "globe.airplanes.live globe_history",
    what: "A second free, no-account historical ADS-B archive, fed by a volunteer network independent of adsb.lol.",
  },
  "adsb-lol": {
    name: "adsb.lol globe_history",
    what: "The free historical archive this investigation used first.",
  },
  "adsbexchange-samples": {
    name: "samples.adsbexchange.com free monthly sample",
    what: "ADS-B Exchange publishes one full day per month (the 1st) free, back to 2016. The only free source that reaches the 2022 dates.",
  },
  "adsblol-github-backup": {
    name: "adsb.lol GitHub Release backup (ODbL)",
    what: "adsb.lol mirrors its whole archive, one release per day, to github.com/adsblol/globe_history_YYYY. Days its live API refuses are still published there in full.",
  },
};

for (const ac of FLEET) {
  const dir = `${PLANES}${ac.reg}/data/recovered`;
  let files;
  try { files = await readdir(dir); } catch { continue; }
  const metas = files.filter((f) => f.endsWith(".meta.json"));
  if (!metas.length) continue;

  const byDate = new Map();     // date -> { source -> meta }
  const pages = [];
  for (const m of metas) {
    let j; try { j = JSON.parse(await readFile(`${dir}/${m}`, "utf8")); } catch { continue; }
    if (j.utc_date) {
      if (!byDate.has(j.utc_date)) byDate.set(j.utc_date, {});
      byDate.get(j.utc_date)[j.source] = j;
    } else if (j.snapshot_utc) pages.push(j);
  }

  const dates = [...byDate.keys()].sort();
  const rows = [];
  for (const d of dates) {
    const s = byDate.get(d);
    const has = (k) => (s[k] ? "yes" : "—");
    const recovered = !s["adsb-lol"] && (s["airplanes-live"] || s["adsbexchange-samples"] || s["adsblol-github-backup"]);
    const sum = (s["airplanes-live"] ?? s["adsbexchange-samples"] ?? s["adsblol-github-backup"] ?? s["adsb-lol"])?.summary;
    rows.push({ d, s, recovered, sum, has });
  }
  const recCount = rows.filter((r) => r.recovered).length;

  let md = `# ${ac.reg} — flight data we could not get, and what we got back\n\n`;
  md += `Generated ${NOW} by \`site/docs/Planes/following/apis/public_open_source/code/write_recovery_records.js\`.\n\n`;
  md += `Aircraft: **${ac.reg}**, ICAO hex \`${ac.hex}\`, type ${ac.type}, ${ac.registry}. Thread: \`${ac.side}\`.\n\n`;
  md += `## What this file is\n\n`;
  md += `This investigation works on the stated assumption that **some of this flight data has been removed from the places the public reads it.** This file records, for this one airframe: the UTC days we went looking for, which archives held them, which did not, and which of the days that one archive lacked were **recovered from a backup**.\n\n`;
  md += `**A gap in one archive is not evidence that anybody deleted anything.** Volunteer ADS-B networks hear different aircraft on different days because they have different feeders, different antennas and different geography. Retention windows also roll off on a schedule. Those ordinary explanations come first, every time. The only finding here that is genuinely about *removal* is a page the Internet Archive holds a populated copy of which returns nothing to the public today — and even that has the innocent reading that an owner lawfully requested blocking, or that the site reorganised its URLs.\n\n`;
  md += `## Sources used\n\n| Key | Source | What it is |\n|---|---|---|\n`;
  for (const [k, v] of Object.entries(SOURCES)) md += `| \`${k}\` | ${v.name} | ${v.what} |\n`;

  md += `\n## Day-by-day\n\n`;
  md += `**${rows.length} UTC days checked. ${recCount} recovered from a backup after the primary archive returned nothing.**\n\n`;
  md += `| UTC date | adsb.lol | airplanes.live | ADSBX sample | GitHub backup | Recovered | What the trace shows |\n|---|---|---|---|---|---|---|\n`;
  for (const r of rows) {
    const w = r.sum
      ? `${r.sum.points} pts, ${String(r.sum.first_seen_utc).slice(11, 19)}Z (${r.sum.first_pos?.[0]?.toFixed(3)}, ${r.sum.first_pos?.[1]?.toFixed(3)}) → ${String(r.sum.last_seen_utc).slice(11, 19)}Z (${r.sum.last_pos?.[0]?.toFixed(3)}, ${r.sum.last_pos?.[1]?.toFixed(3)})`
      : "no trace held by any source";
    md += `| ${r.d} | ${r.has("adsb-lol")} | ${r.has("airplanes-live")} | ${r.has("adsbexchange-samples")} | ${r.has("adsblol-github-backup")} | ${r.recovered ? "**YES**" : "—"} | ${w} |\n`;
  }

  if (pages.length) {
    md += `\n## Tracking-site pages: archived then, public now?\n\n`;
    md += `| Snapshot (UTC) | Site | Bytes | Flight rows recovered | That URL returns to the public today |\n|---|---|---|---|---|\n`;
    for (const p of pages.sort((a, b) => String(a.snapshot_utc).localeCompare(String(b.snapshot_utc)))) {
      const ts = String(p.snapshot_utc);
      const pretty = `${ts.slice(0, 4)}-${ts.slice(4, 6)}-${ts.slice(6, 8)} ${ts.slice(8, 10)}:${ts.slice(10, 12)}`;
      md += `| ${pretty} | ${String(p.source).replace("wayback/", "")} | ${p.bytes} | ${p.flight_rows_recovered ?? "—"} | HTTP ${p.live_http_today} |\n`;
    }
    md += `\nA page the Internet Archive holds and the live site no longer serves is the one thing on this page that is genuinely about removal. **It still does not establish intent.**\n`;
  }
  md += `\n## Reproducing this\n\n\`\`\`\nnode recover_erased.js --tail ${ac.reg}\nnode recover_adsbx_samples.js --tail ${ac.reg}\n\`\`\`\n\nEvery payload in this directory has a \`.meta.json\` beside it recording the exact URL, the HTTP status, the byte count and the UTC time of the request. **Nothing overwrites a previous pull** — a re-pull lands beside the first with a timestamp suffix, because the diff between two pulls is how a disappearance gets shown.\n`;

  await writeFile(`${dir}/_RECOVERED_DATA.md`, md);
  console.log(`${ac.reg.padEnd(8)} ${String(rows.length).padStart(3)} days, ${String(recCount).padStart(3)} recovered, ${pages.length} archived pages -> _RECOVERED_DATA.md`);
}
