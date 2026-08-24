#!/usr/bin/env node
// ADS-B Exchange, via RapidAPI. Once the "unfiltered" community feed, now a
// commercial product - and the change matters to this investigation, because the
// globe.adsbexchange.com history pages that several of the original claims were
// read off now return HTTP 403 to the public (verified 24 August 2026).
//
//   /v2/registration/{reg}/       live
//   /v2/icao/{hex}/               live
//   globe_history/...             historical traces, subscriber only
//
// CREDENTIAL: ADSBX_RAPIDAPI_KEY. It comes from ~/.credentials/charlie_kirk.json
// (charlie_kirk.flight_apis.ADSBX_RAPIDAPI_KEY) or from the environment. Never
// from a file in this repo. See ../../public_open_source/code/lib/credentials.js.
//   export ADSBX_RAPIDAPI_KEY=... # optional, overrides the store
//   node adsbexchange_rapidapi.js SU-BTT
import { savePull, getJSON } from "../../public_open_source/code/lib/save.js";
import { byReg, FLEET } from "../../public_open_source/code/lib/fleet.js";
import { cred, report } from "../../public_open_source/code/lib/credentials.js";
const OUT = new URL("../data/adsbexchange/", import.meta.url).pathname;
const HOST = "adsbexchange-com1.p.rapidapi.com";

if (import.meta.url === `file://${process.argv[1]}`) {
  if (!report("ADSBX_RAPIDAPI_KEY")) {
    console.error("Note for knowledge.mdx: adsb.lol serves a free historical archive at the same");
    console.error("URL shape adsbexchange charges for. Try Pass 1 before paying for this.");
    process.exit(3);
  }
  const list = process.argv[2] ? [byReg(process.argv[2])].filter(Boolean) : FLEET.filter((a) => a.side === "following");
  for (const ac of list) {
    const url = `https://${HOST}/v2/registration/${ac.reg}/`;
    const { status, text } = await getJSON(url, { headers: { "X-RapidAPI-Key": cred("ADSBX_RAPIDAPI_KEY"), "X-RapidAPI-Host": HOST } });
    await savePull({ dir: `${OUT}${ac.reg}`, name: "live_registration.json", url, status, body: text,
      note: "COMMERCIAL RESPONSE - audit trail only. Live endpoint: empty means not airborne now." });
    console.log(`${ac.reg.padEnd(8)} HTTP ${status}`);
  }
}
