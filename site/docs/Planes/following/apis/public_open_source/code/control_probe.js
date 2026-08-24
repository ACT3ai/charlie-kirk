#!/usr/bin/env node
// THE CONTROL TEST. Run this BEFORE reporting that anything was removed.
//
// This investigation keeps meeting the same shape of evidence: a record that used
// to be reachable and is not now. That shape has two completely different causes
// and they look identical from the outside:
//
//   A  SOMETHING HAPPENED TO THIS AIRCRAFT'S RECORD.
//   B  SOMETHING HAPPENED TO THE WHOLE SOURCE, and this aircraft is incidental.
//
// The only way to tell them apart is to ask the same question about aircraft that
// have NOTHING to do with the case. If the unrelated controls fail the same way,
// it is B, and reporting it as A would be false. Every "removal" finding on this
// site has to survive this script first.
//
// Three probes, and what each has already settled:
//
//   --archives   Walks the two free ADS-B history archives across a date range.
//                SETTLED: adsb.lol answers 403 for EVERY aircraft from exactly
//                2025-10-12 to about 2025-12-30, and 404 for EVERY aircraft from
//                about 2025-12-31 to about 2026-08-01. Both are site-wide. Neither
//                is suppression, and neither may ever be reported as scrubbing.
//
//   --fr24       Asks Flightradar24 for case tails, control tails, and FR24's own
//                home page. SETTLED: FR24 answers 403 to scripted requests for its
//                ENTIRE SITE, same ~5,877-byte body every time. An FR24 403 is bot
//                protection. It cannot distinguish a removed record from a present
//                one, and nothing on this site may read it as evidence about any
//                particular aircraft.
//
//   --depth      Finds where each archive's history actually begins.
//                SETTLED: adsb.lol from about 2023-02; globe.airplanes.live from
//                about 2023-11; the ADSBX monthly sample back to 2016 but only the
//                1st of each month.
//
//   node control_probe.js --fr24
//   node control_probe.js --archives --from 2025-10-08 --to 2025-10-20
//   node control_probe.js --depth
import { FLEET } from "./lib/fleet.js";

const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
           "(KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Nine busy airframes with no connection whatever to this case. They are the whole
// point: a result that is identical for these and for SU-BTT is a result about the
// source, not about SU-BTT.
const CONTROLS = [
  { reg: "N628TS", hex: "a8ae5f" }, { reg: "N509AY", hex: "a66f6b" },
  { reg: "VH-OQA", hex: "7c6b5b" }, { reg: "G-EUUU", hex: "4009a2" },
  { reg: "D-AIBA", hex: "3c4ad1" }, { reg: "EI-DYY", hex: "4ca7b3" },
  { reg: "N800XX", hex: "ab1644" }, { reg: "N1",     hex: "a00001" },
  { reg: "N509MD", hex: "a66d21" },
];

const NETWORKS = [
  { key: "adsb.lol",              host: "adsb.lol" },
  { key: "globe.airplanes.live",  host: "globe.airplanes.live" },
  { key: "samples.adsbexchange",  host: "samples.adsbexchange.com", path: "traces" },
];
const url = (n, hex, d) => {
  const [y, m, dd] = d.split("-");
  const base = n.path ? `https://${n.host}/${n.path}` : `https://${n.host}/globe_history`;
  return `${base}/${y}/${m}/${dd}/${n.path ? "" : "traces/"}${hex.slice(-2)}/trace_full_${hex}.json`;
};

async function head(u) {
  try { const r = await fetch(u, { headers: { "User-Agent": UA } }); return r.status; }
  catch { return 0; }
}

// --------------------------------------------------------------- --archives
async function archives(from, to) {
  const days = []; const d = new Date(from + "T00:00:00Z"); const end = new Date(to + "T00:00:00Z");
  while (d <= end) { days.push(d.toISOString().slice(0, 10)); d.setUTCDate(d.getUTCDate() + 1); }
  const cases = FLEET.slice(0, 4);
  console.log("date        network                  case(200/403/404)  CONTROL(200/403/404)  verdict");
  for (const day of days) {
    for (const n of NETWORKS.slice(0, 2)) {
      const tally = async (list) => {
        const s = { 200: 0, 403: 0, 404: 0, other: 0 };
        for (const a of list) { const c = await head(url(n, a.hex, day));
                                if (s[c] === undefined) s.other++; else s[c]++; await sleep(40); }
        return s;
      };
      const c = await tally(cases), k = await tally(CONTROLS);
      // The verdict is decided by the CONTROLS, never by the case aircraft.
      const v = k[200] > 0 ? "archive serving normally"
              : k[403] > 0 ? "SITE-WIDE 403 — NOT suppression"
              : "SITE-WIDE absence — NOT suppression";
      console.log(`${day}  ${n.key.padEnd(22)} ${c[200]}/${c[403]}/${c[404]}`.padEnd(58) +
                  `${k[200]}/${k[403]}/${k[404]}`.padEnd(22) + v);
    }
  }
  console.log("\nRead the CONTROL column first. If the controls fail, the case aircraft's");
  console.log("failure is the same failure and says nothing about the case aircraft.");
}

// ------------------------------------------------------------------- --fr24
async function fr24() {
  const H = { "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
              "Accept-Language": "en-US,en;q=0.9", "Sec-Fetch-Dest": "document",
              "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none" };
  const probe = async (u, tag) => {
    try { const r = await fetch(u, { headers: H, redirect: "manual" });
          const b = await r.text().catch(() => "");
          console.log(`${tag.padEnd(9)} ${String(r.status).padEnd(4)} ${String(b.length).padStart(6)} bytes  ${u}`);
          return { status: r.status, bytes: b.length }; }
    catch { console.log(`${tag.padEnd(9)} ERR   ${u}`); return { status: 0, bytes: 0 }; }
  };
  const out = [];
  console.log("--- CASE AIRCRAFT ---");
  for (const a of FLEET) { out.push(await probe(`https://www.flightradar24.com/data/aircraft/${a.reg.toLowerCase()}`, "case")); await sleep(350); }
  console.log("--- CONTROL AIRCRAFT (nothing to do with this case) ---");
  for (const a of CONTROLS) { out.push(await probe(`https://www.flightradar24.com/data/aircraft/${a.reg.toLowerCase()}`, "control")); await sleep(350); }
  console.log("--- FR24's OWN PAGES (does the whole site block us?) ---");
  const site = [];
  for (const u of ["https://www.flightradar24.com/", "https://www.flightradar24.com/data/aircraft"])
    { site.push(await probe(u, "site")); await sleep(350); }

  const all403 = [...out, ...site].every((r) => r.status === 403);
  console.log("\n" + (all403
    ? "EVERY request returned 403, INCLUDING FLIGHTRADAR24'S OWN HOME PAGE.\n" +
      "This is bot protection. It is NOT evidence that any aircraft's record was\n" +
      "removed, and it must never be published as if it were. Testing a removal\n" +
      "claim requires a real browser session — see browser_capture/."
    : "Mixed results. Read them carefully before concluding anything: a 403 that\n" +
      "applies to SOME aircraft and not others would be a very different finding."));
}

// ------------------------------------------------------------------ --depth
async function depth() {
  const probes = ["2016-01-01", "2018-01-01", "2020-01-01", "2022-01-01", "2022-06-01",
                  "2023-01-01", "2023-06-01", "2023-11-01", "2024-01-01", "2025-01-01",
                  "2025-09-10", "2026-01-01", "2026-08-01"];
  const basket = [...FLEET.slice(0, 3), ...CONTROLS.slice(0, 5)];
  for (const n of NETWORKS) {
    console.log(`\n--- ${n.key} ---`);
    for (const day of probes) {
      let hits = 0;
      for (const a of basket) { if (await head(url(n, a.hex, day)) === 200) hits++; await sleep(40); }
      console.log(`  ${day}  ${hits > 0 ? `PRESENT (${hits}/${basket.length} heard)` : "nothing"}`);
    }
  }
  console.log("\n`nothing` from a small basket is weak evidence on any single date --");
  console.log("these aircraft do not all fly every day. Read the pattern, not one row.");
}

const a = process.argv.slice(2);
const arg = (k, d) => (a.includes(k) ? a[a.indexOf(k) + 1] : d);
if (a.includes("--fr24")) await fr24();
else if (a.includes("--depth")) await depth();
else if (a.includes("--archives")) await archives(arg("--from", "2025-10-08"), arg("--to", "2025-10-20"));
else console.log("usage: node control_probe.js [--fr24 | --archives [--from D --to D] | --depth]");
