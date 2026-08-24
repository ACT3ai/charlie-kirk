#!/usr/bin/env node
// THE RECOVERY HARNESS.
//
// Premise, stated as an assumption and not as a finding: SOME OF THIS FLIGHT DATA
// HAS BEEN REMOVED FROM THE PLACES THE PUBLIC READS IT. This script goes looking
// for it somewhere else. It does four things, in the order that matters:
//
//   A  BACKUP ARCHIVE      globe.airplanes.live/globe_history — a SECOND free,
//                          no-account historical ADS-B archive, independent of
//                          adsb.lol, fed by a different volunteer network.
//   B  THE ARCHIVE WE HAD  adsb.lol/globe_history — pulled again beside A so the
//                          two can be DIFFED. Where A has a day and B does not,
//                          that day was recoverable and we had been missing it.
//   C  THE PAGE ARCHIVE    Internet Archive CDX + snapshot capture of the
//                          tracking-site aircraft pages themselves. A tracking
//                          site can drop an aircraft from its history table; the
//                          Wayback copy of that table is the record of what it
//                          used to say. FR24 history tables are parsed to rows.
//   D  LIVE PROBE          What the same URL returns to the public TODAY. The
//                          gap between C and D is the documented removal.
//
// WHAT A RECOVERY DOES AND DOES NOT MEAN. Finding a day on airplanes.live that
// adsb.lol does not have means one volunteer network heard the aircraft and the
// other did not. It is NOT evidence that anybody deleted anything from adsb.lol.
// Coverage differs between networks for entirely ordinary reasons — different
// feeders, different antennas, different geography. THE PAGE MUST SAY SO.
//
// The one thing that IS a removal finding is C-versus-D: a page the Internet
// Archive holds a populated copy of, which returns nothing to the public now.
// Even that has an innocent reading — owners may lawfully request blocking, and
// sites reorganise URLs. Say which. Never assert intent.
//
//   node recover_erased.js                    every tail, the case date windows
//   node recover_erased.js --tail N102DZ      one tail
//   node recover_erased.js --pages-only       skip ADS-B, do Wayback + live only
//   node recover_erased.js --adsb-only        skip Wayback
import { mkdir, writeFile } from "node:fs/promises";
import { FLEET } from "./lib/fleet.js";
import { scrubVendorCredentials } from "./lib/scrub.js";

const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
           "(KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const PLANES = new URL("../../../../", import.meta.url).pathname;      // site/docs/Planes/
const RECDIR = new URL("../data/recovery/", import.meta.url).pathname;
const NOW    = new Date().toISOString();
const sleep  = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------------------------------------------------------------- date windows
// The days this case actually turns on. Kept narrow on purpose: a recovery run
// that sweeps four years of dates buries the days that matter under noise.
function windows() {
  const w = [];
  const add = (a, b, why) => w.push({ from: a, to: b, why });
  add("2025-09-01", "2025-09-16", "the September 2025 window — the fortnight the case turns on");
  add("2025-10-08", "2025-10-16", "the adsb.lol 403 BAND — dates the primary archive refuses, incl. the 13 Oct Sharm el-Sheikh tarmac claim");
  add("2026-04-25", "2026-06-05", "around the reported MAY 2026 FlightRadar24 removal of N102DZ");
  return w;
}
const days = ({ from, to }) => {
  const out = []; const d = new Date(from + "T00:00:00Z"); const end = new Date(to + "T00:00:00Z");
  while (d <= end) { out.push(d.toISOString().slice(0, 10)); d.setUTCDate(d.getUTCDate() + 1); }
  return out;
};

// ------------------------------------------------------------------- fetch/save
async function grab(url, { text = true } = {}) {
  try {
    const res = await fetch(url, { headers: { "User-Agent": UA }, redirect: "follow" });
    const body = text ? await res.text() : Buffer.from(await res.arrayBuffer());
    return { status: res.status, body, bytes: Buffer.byteLength(body) };
  } catch (e) { return { status: 0, body: "", bytes: 0, err: String(e) }; }
}
async function save(dir, name, body, meta) {
  await mkdir(dir, { recursive: true });
  // The archived page carries the VENDOR'S own client-side keys. Redact them on
  // the way to disk -- see lib/scrub.js for why, and for what survives. The
  // redaction count is recorded in the sidecar so the capture states plainly
  // that it was altered, and in exactly one respect.
  let redacted = 0;
  if (typeof body === "string") {
    const scrubbed = scrubVendorCredentials(body);
    body = scrubbed.text;
    redacted = scrubbed.count;
  }
  if (body != null && body !== "") await writeFile(`${dir}/${name}`, body);
  await writeFile(`${dir}/${name}.meta.json`,
    JSON.stringify({ retrieved_utc: NOW, vendor_credentials_redacted: redacted, ...meta }, null, 2) + "\n");
}

// -------------------------------------------------------- A + B: the two archives
// Both networks serve tar1090's globe_history layout, so one URL shape does both.
const traceURL = (host, hex, date) => {
  const [y, m, d] = date.split("-");
  return `https://${host}/globe_history/${y}/${m}/${d}/traces/${hex.slice(-2)}/trace_full_${hex}.json`;
};
const NETWORKS = [
  { key: "airplanes-live", host: "globe.airplanes.live", role: "BACKUP ARCHIVE — independent volunteer network" },
  { key: "adsb-lol",       host: "adsb.lol",             role: "the archive this investigation already used" },
];

function summarise(json) {
  if (!json || !Array.isArray(json.trace) || !json.trace.length) return null;
  const tr = json.trace, t0 = json.timestamp;
  const iso = (s) => new Date((t0 + s) * 1000).toISOString();
  const onGround = (p) => p[3] === "ground";
  const first = tr[0], last = tr[tr.length - 1];
  let dep = null, arr = null;
  for (let i = 1; i < tr.length; i++) {
    if (onGround(tr[i - 1]) && !onGround(tr[i]) && !dep) dep = iso(tr[i][0]);
    if (!onGround(tr[i - 1]) && onGround(tr[i])) arr = iso(tr[i][0]);
  }
  return {
    registration: json.r ?? null, type: json.t ?? null, icao: json.icao ?? null,
    points: tr.length,
    first_seen_utc: iso(first[0]), first_pos: [first[1], first[2]], first_on_ground: onGround(first),
    last_seen_utc: iso(last[0]),  last_pos: [last[1], last[2]],   last_on_ground: onGround(last),
    wheels_up_utc: dep, wheels_down_utc: arr,
  };
}

async function pullArchives(ac, dateList) {
  const dir = `${PLANES}${ac.reg}/data/recovered`;
  const rows = [];
  for (const date of dateList) {
    const per = { tail: ac.reg, hex: ac.hex, date, sources: {} };
    for (const n of NETWORKS) {
      const url = traceURL(n.host, ac.hex, date);
      const r = await grab(url);
      let sum = null;
      if (r.status === 200) {
        try { sum = summarise(JSON.parse(r.body)); } catch { /* not json */ }
        // Source-tagged filename. The SOURCE IS PART OF THE NAME, on purpose.
        await save(dir, `${ac.reg}_${date}_${n.key}_trace_full.json`, r.body,
          { source: n.key, source_role: n.role, url, http_status: r.status, bytes: r.bytes,
            tail: ac.reg, hex: ac.hex, utc_date: date, summary: sum });
      }
      per.sources[n.key] = { http: r.status, bytes: r.bytes, summary: sum };
      await sleep(120);
    }
    const a = per.sources["airplanes-live"], b = per.sources["adsb-lol"];
    per.verdict =
      a?.http === 200 && b?.http !== 200 ? "RECOVERED_ONLY_ON_BACKUP" :
      a?.http !== 200 && b?.http === 200 ? "ONLY_ON_ADSB_LOL" :
      a?.http === 200 && b?.http === 200 ? "BOTH_HAVE_IT" : "NEITHER_HAS_IT";
    per.richer = a?.bytes && b?.bytes ? +(a.bytes / b.bytes).toFixed(1) : null;
    rows.push(per);
    const tag = per.verdict === "RECOVERED_ONLY_ON_BACKUP" ? "  <== RECOVERED" : "";
    console.log(`  ${ac.reg} ${date}  alive=${String(a?.http).padEnd(3)}/${String(a?.bytes).padStart(7)}  ` +
                `lol=${String(b?.http).padEnd(3)}/${String(b?.bytes).padStart(7)}  ${per.verdict}${tag}`);
  }
  return rows;
}

// ------------------------------------------------ C: the page archive (Wayback)
const PAGE_TARGETS = (reg) => {
  const lo = reg.toLowerCase();
  return [
    { site: "flightradar24", url: `https://www.flightradar24.com/data/aircraft/${lo}`, parse: "fr24" },
    { site: "flightaware",   url: `https://www.flightaware.com/live/flight/${reg}` },
    { site: "radarbox",      url: `https://www.radarbox.com/data/registration/${reg}` },
    { site: "adsbexchange",  url: `https://globe.adsbexchange.com/?icao=${reg}` },
    { site: "planespotters", url: `https://www.planespotters.net/search?q=${reg}` },
  ];
};

// FR24 renders its history table server-side. Pull the rows back out of the
// archived HTML — this is the actual erased content, recovered.
function parseFR24(htmlText) {
  const strip = (s) => s.replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/g, " ")
    .replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&")
    .replace(/&#0?39;|&apos;/g, "'").replace(/&quot;/g, '"').replace(/[ \t]+/g, " ");
  const t = strip(htmlText);
  const info = {};
  const g = (label, re) => { const m = t.match(re); if (m) info[label] = m[1].trim(); };
  g("aircraft", /AIRCRAFT\s+(.+?)\s+AIRLINE/);
  g("operator", /AIRLINE\s+(.+?)\s+OPERATOR/);
  g("type_code", /TYPE CODE\s+([A-Z0-9]+)/);
  g("mode_s", /MODE S\s+([A-F0-9]{6})/i);
  const title = htmlText.match(/<title>(.*?)<\/title>/s);
  if (title) info.page_title = title[1].trim();
  const i = t.indexOf("FLIGHTS HISTORY");
  const flights = [];
  if (i >= 0) {
    for (const chunk of t.slice(i).split(/\s—\s/).slice(1)) {
      const c = chunk.replace(/\s+/g, " ").trim();
      // "10 Sep 2025 1:11 Landed 01:32 STD 23:30 ATD 00:21 STA 01:01 FROM X (AAA) TO Y (BBB)"
      const m = c.match(/^(\d{2} \w{3} \d{4})\s+(\S+)\s+(.*?)\s*STD\s+(\S+)\s+ATD\s*(\S*)\s*STA\s+(\S+)\s+FROM\s+(.+?)\s+TO\s+(.+?)\s+\d{2} \w{3}/);
      if (m) flights.push({ date: m[1], flight_time: m[2], status: m[3].trim(),
        std_utc: m[4], atd_utc: m[5] || null, sta_utc: m[6], from: m[7].trim(), to: m[8].trim() });
    }
  }
  return { info, flights, flight_rows: flights.length };
}

async function pullPages(ac) {
  const dir = `${PLANES}${ac.reg}/data/recovered`;
  const out = [];
  for (const tgt of PAGE_TARGETS(ac.reg)) {
    const cdxURL = `https://web.archive.org/cdx/search/cdx?url=${encodeURIComponent(tgt.url)}` +
                   `&output=json&limit=300&fl=timestamp,original,statuscode,digest,length&collapse=digest`;
    const cdx = await grab(cdxURL);
    let snaps = [];
    try { const j = JSON.parse(cdx.body); snaps = j.length > 1 ? j.slice(1) : []; } catch { /* */ }
    // D: what does the public get from this URL right now?
    const live = await grab(tgt.url);
    const rec = { site: tgt.site, url: tgt.url, snapshots: snaps.length,
      first: snaps[0]?.[0] ?? null, last: snaps.at(-1)?.[0] ?? null,
      live_http_today: live.status, live_bytes: live.bytes, captured: [] };

    for (const s of snaps) {
      const ts = s[0];
      const snapURL = `https://web.archive.org/web/${ts}id_/${tgt.url}`;
      const r = await grab(snapURL);
      if (r.status !== 200 || r.bytes < 500) { await sleep(250); continue; }
      const name = `${ac.reg}_${ts}_wayback_${tgt.site}.html`;
      let parsed = null;
      if (tgt.parse === "fr24") {
        parsed = parseFR24(r.body);
        if (parsed.flight_rows) {
          await save(dir, `${ac.reg}_${ts}_wayback_${tgt.site}_flights.json`,
            JSON.stringify({ tail: ac.reg, snapshot_utc: ts, source_url: tgt.url,
              wayback_url: snapURL, ...parsed }, null, 2) + "\n",
            { source: "wayback/flightradar24", url: snapURL, http_status: 200,
              note: `${parsed.flight_rows} flight-history rows recovered from an archived copy of a page that today returns HTTP ${live.status} to the public` });
        }
      }
      await save(dir, name, r.body,
        { source: `wayback/${tgt.site}`, url: snapURL, snapshot_utc: ts,
          http_status: r.status, bytes: r.bytes, original_url: tgt.url,
          live_http_today: live.status,
          flight_rows_recovered: parsed?.flight_rows ?? null });
      rec.captured.push({ ts, bytes: r.bytes, flight_rows: parsed?.flight_rows ?? null,
        info: parsed?.info ?? null, flights: parsed?.flights ?? null });
      await sleep(250);
    }
    const flag = rec.snapshots && rec.live_http_today !== 200 ? "  <== ARCHIVED THEN, NOT PUBLIC NOW" : "";
    console.log(`  ${ac.reg} ${tgt.site.padEnd(14)} snapshots=${String(rec.snapshots).padStart(3)}  ` +
                `live_today=${rec.live_http_today}${flag}`);
    out.push(rec);
  }
  return out;
}

// ------------------------------------------------------------------------ main
const argv = process.argv.slice(2);
const only = argv.includes("--tail") ? argv[argv.indexOf("--tail") + 1] : null;
const pagesOnly = argv.includes("--pages-only");
const adsbOnly  = argv.includes("--adsb-only");
const fleet = FLEET.filter((a) => (only ? a.reg === only : true));
const dateList = [...new Set(windows().flatMap(days))];

const report = { generated_utc: NOW, windows: windows(), tails: {} };
for (const ac of fleet) {
  console.log(`\n=== ${ac.reg} (${ac.hex}) — ${ac.side} ===`);
  report.tails[ac.reg] = { hex: ac.hex, side: ac.side };
  if (!pagesOnly) report.tails[ac.reg].archives = await pullArchives(ac, dateList);
  if (!adsbOnly)  report.tails[ac.reg].pages    = await pullPages(ac);
}
await mkdir(RECDIR, { recursive: true });
await writeFile(`${RECDIR}recovery_index.json`, JSON.stringify(report, null, 2) + "\n");
console.log(`\nwrote ${RECDIR}recovery_index.json`);
