#!/usr/bin/env node
// THE CONTROL TEST FOR THE *PAGE* SIDE. Run this before calling any tracking-site
// 403 a removal.
//
// recover_erased.js records what each tracking site returns TODAY for each
// aircraft in this case. On its own that number proves nothing, because these
// sites also return 403 to any scripted request regardless of which aircraft is
// asked for. Cloudflare does not know or care whose tail number is in the URL.
//
// So: ask the same five sites the same question about aircraft that have NOTHING
// to do with this case -- ordinary airliners and unrelated business jets. If the
// control aircraft come back 403 too, then 403 means "we block robots", and every
// 403 in the fleet table is meaningless. Only a site that serves the CONTROLS and
// refuses OUR aircraft is evidence of anything about our aircraft.
//
//   node control_page_probe.js
import { mkdir, writeFile } from "node:fs/promises";
const UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
           "(KHTML, like Gecko) Chrome/125.0 Safari/537.36";
const OUT = new URL("../data/recovery/", import.meta.url).pathname;
const NOW = new Date().toISOString();
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Chosen for irrelevance. Two mainline airliners, one regional, two business
// jets with no connection to this case, this investigation, or anyone in it.
const CONTROLS = [
  { reg: "N102UW", what: "American Airlines Airbus A320 — mainline airliner" },
  { reg: "EI-DCL", what: "Ryanair Boeing 737-800 — European mainline airliner" },
  { reg: "D-AIMA", what: "Lufthansa Airbus A380 — European mainline airliner" },
  { reg: "N904XJ", what: "Endeavor Air CRJ-900 — US regional airliner" },
  { reg: "N1KE",   what: "Nike corporate Gulfstream — unrelated business jet" },
];
// And the aircraft this case turns on, asked the identical way in the same run,
// from the same address, seconds apart. Same question, same conditions.
const SUBJECTS = ["N102DZ", "N1098L", "SU-BTT", "SU-BND", "N888KG"];

const TARGETS = (reg) => {
  const lo = reg.toLowerCase();
  return [
    { site: "flightradar24", url: `https://www.flightradar24.com/data/aircraft/${lo}` },
    { site: "flightaware",   url: `https://www.flightaware.com/live/flight/${reg}` },
    { site: "radarbox",      url: `https://www.radarbox.com/data/registration/${reg}` },
    { site: "adsbexchange",  url: `https://globe.adsbexchange.com/?icao=${reg}` },
    { site: "planespotters", url: `https://www.planespotters.net/search?q=${reg}` },
  ];
};

async function probe(url) {
  try {
    const res = await fetch(url, { headers: { "User-Agent": UA }, redirect: "follow" });
    const body = await res.text();
    return { status: res.status, bytes: Buffer.byteLength(body) };
  } catch (e) { return { status: 0, bytes: 0, err: String(e) }; }
}

const rows = [];
for (const group of [{ kind: "CONTROL", list: CONTROLS.map((c) => c.reg), meta: CONTROLS },
                     { kind: "SUBJECT", list: SUBJECTS, meta: [] }]) {
  for (const reg of group.list) {
    for (const t of TARGETS(reg)) {
      const r = await probe(t.url);
      rows.push({ kind: group.kind, reg, site: t.site, url: t.url, http: r.status, bytes: r.bytes,
        note: group.meta.find((m) => m.reg === reg)?.what ?? null });
      console.log(`  ${group.kind.padEnd(7)} ${reg.padEnd(7)} ${t.site.padEnd(14)} ${String(r.status).padStart(3)}  ${String(r.bytes).padStart(7)}b`);
      await sleep(400);
    }
  }
}

// The verdict is per SITE, not per aircraft.
const sites = [...new Set(rows.map((r) => r.site))];
const verdicts = {};
for (const s of sites) {
  const ctrl = rows.filter((r) => r.site === s && r.kind === "CONTROL");
  const subj = rows.filter((r) => r.site === s && r.kind === "SUBJECT");
  const ctrlOK = ctrl.filter((r) => r.http === 200).length;
  const subjOK = subj.filter((r) => r.http === 200).length;
  verdicts[s] = {
    controls_served: `${ctrlOK}/${ctrl.length}`, subjects_served: `${subjOK}/${subj.length}`,
    verdict:
      ctrlOK === 0
        ? "SITE_BLOCKS_ALL_SCRIPTED_REQUESTS — a non-200 here says nothing about any aircraft"
        : subjOK === 0
        ? "SERVES_CONTROLS_REFUSES_SUBJECTS — this difference is about the aircraft, not the robot"
        : "MIXED — read per aircraft",
  };
  console.log(`\n${s}: controls ${verdicts[s].controls_served} served, subjects ${verdicts[s].subjects_served} served -> ${verdicts[s].verdict}`);
}

await mkdir(OUT, { recursive: true });
await writeFile(`${OUT}page_control_probe.json`,
  JSON.stringify({ generated_utc: NOW,
    why: "A tracking-site 403 is only evidence about an aircraft if the same site serves aircraft that have nothing to do with this case.",
    controls: CONTROLS, subjects: SUBJECTS, rows, verdicts }, null, 2) + "\n");
console.log(`\nwrote ${OUT}page_control_probe.json`);
