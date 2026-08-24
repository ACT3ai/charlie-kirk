#!/usr/bin/env node
// FAA RELEASABLE AIRCRAFT DATABASE - a United States government primary record,
// public domain, no key, no request, refreshed daily.
//
//   https://registry.faa.gov/database/ReleasableAircraft.zip
//
// This is the highest-ranking thing Pass 3 can get without writing a letter. It is
// a facility_record, not an ADS-B reading: it says who the FAA says owns an
// airframe, what it is, when it was registered, and when that registration expires.
//
// WHAT IT CANNOT DO, and this is the whole shape of this case: it covers
// N-REGISTERED AIRCRAFT ONLY. Every SU- tail in this investigation is Egyptian and
// appears nowhere in it. There is no equivalent public Egyptian registry download.
// So the aircraft at the centre of the claim are precisely the ones the best free
// government record cannot describe - and that asymmetry belongs on the page.
//
// MASTER.txt is one row per registered aircraft, keyed by N-NUMBER (no leading N).
// ACFTREF.txt is the type reference, joined on MFR MDL CODE.
//
//   node faa_registry.js            download and extract our tails
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { execFileSync } from "node:child_process";
import { FLEET } from "../../public_open_source/code/lib/fleet.js";

const OUT = new URL("../data/faa_registry/", import.meta.url).pathname;
const URL_ZIP = "https://registry.faa.gov/database/ReleasableAircraft.zip";

await mkdir(OUT, { recursive: true });
const res = await fetch(URL_ZIP, { redirect: "follow" });
console.log(`GET ${URL_ZIP}  ->  HTTP ${res.status}`);
if (res.status !== 200) {
  await writeFile(`${OUT}FETCH_FAILED.md`, [
    "# FAA releasable aircraft database — download failed",
    "", `Attempted ${new Date().toISOString()}`, `URL: ${URL_ZIP}`, `HTTP status: ${res.status}`, "",
    "This is a US government public-domain dataset and should be freely downloadable.",
    "A failure here is a temporary outage or a changed URL, not a records refusal —",
    "check the FAA aircraft registry page before concluding anything else.", "",
  ].join("\n"));
  process.exit(1);
}
const buf = Buffer.from(await res.arrayBuffer());
await writeFile(`${OUT}ReleasableAircraft.zip`, buf);
await writeFile(`${OUT}ReleasableAircraft.zip.meta.json`, JSON.stringify({
  url: URL_ZIP, http_status: res.status, bytes: buf.length,
  retrieved_utc: new Date().toISOString(),
  note: "US government public domain. May be republished in full.",
}, null, 2) + "\n");
console.log(`saved ${(buf.length / 1e6).toFixed(1)} MB`);

execFileSync("unzip", ["-o", "-q", `${OUT}ReleasableAircraft.zip`, "MASTER.txt", "ACFTREF.txt", "-d", OUT]);

const master = (await readFile(`${OUT}MASTER.txt`, "latin1")).split("\n");
const head = master[0].split(",").map((h) => h.trim());
const col = (r, name) => (r[head.indexOf(name)] ?? "").trim();
const wanted = new Map(FLEET.filter((a) => /^N/.test(a.reg)).map((a) => [a.reg.slice(1), a]));

const found = [];
for (const line of master.slice(1)) {
  const r = line.split(",");
  const n = (r[0] ?? "").trim();
  if (!wanted.has(n)) continue;
  const ac = wanted.get(n);
  found.push({
    registration: ac.reg, hex_from_faa: col(r, "MODE S CODE HEX"), hex_we_use: ac.hex.toUpperCase(),
    serial: col(r, "SERIAL NUMBER"), year_mfr: col(r, "YEAR MFR"),
    registrant_name: col(r, "NAME"), registrant_type: col(r, "TYPE REGISTRANT"),
    street: col(r, "STREET"), city: col(r, "CITY"), state: col(r, "STATE"), zip: col(r, "ZIP CODE"),
    country: col(r, "COUNTRY"), last_action_date: col(r, "LAST ACTION DATE"),
    cert_issue_date: col(r, "CERT ISSUE DATE"), expiration_date: col(r, "EXPIRATION DATE"),
    airworthiness_date: col(r, "AIR WORTH DATE"), status_code: col(r, "STATUS CODE"),
    kirk_case_side: ac.side, note: ac.note,
  });
}
await writeFile(`${OUT}tracked_tails_faa_master.json`, JSON.stringify({
  source: URL_ZIP, retrieved_utc: new Date().toISOString(),
  licence: "US government work — public domain",
  n_registered_tails_we_track: wanted.size, found: found.length,
  not_found: [...wanted.keys()].filter((n) => !found.some((f) => f.registration === "N" + n)).map((n) => "N" + n),
  caveat: "FAA registry covers N-registered aircraft only. The SU- Egyptian tails at the centre of this case are not in it and have no public equivalent.",
  records: found,
}, null, 2) + "\n");

for (const f of found) {
  const flag = f.hex_from_faa && f.hex_from_faa.toUpperCase() !== f.hex_we_use ? "  <-- HEX DISAGREES" : "";
  console.log(`${f.registration.padEnd(8)} hex=${f.hex_from_faa.padEnd(7)} ${f.registrant_name.slice(0, 34).padEnd(34)} ${f.city}, ${f.state}${flag}`);
}
console.log(`\n${found.length}/${wanted.size} tracked N-tails found in the FAA master file`);
console.log("SU-BTT SU-BND SU-BTU SU-BTV SU-BGM: Egyptian registry — NOT COVERED by any free government download.");
