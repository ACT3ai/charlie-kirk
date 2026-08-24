#!/usr/bin/env node
// The free community ADS-B networks, probed side by side.
//
// THE FINDING THIS SCRIPT EXISTS TO RECORD: every one of these serves LIVE
// POSITIONS ONLY. Ask any of them about an aircraft that is not airborne at this
// second and you get an empty array with HTTP 200 - which reads like "no such
// aircraft" and means "not flying right now". A researcher who does not know that
// will conclude an aircraft was hidden when it was simply parked.
//
// Probed 24 August 2026 against SU-BTT:
//   adsb.lol        /v2/hex, /v2/reg      HTTP 200, 0 aircraft    live only, open
//   adsb.fi         /api/v2/hex           HTTP 200, 0 aircraft    live only, open
//   airplanes.live  /v2/reg               HTTP 403                NOW GATED - the
//     body asks you to email contact@airplanes.live with a description of your
//     project before it will serve you. It was open before. That is a real change
//     in what a member of the public can retrieve, and it is why we record dates.
//   adsbexchange    globe_history         HTTP 403                paid tier only
//
//   node live_networks.js SU-BTT
import { FLEET, byReg } from "./lib/fleet.js";
import { savePull, getJSON, sleep } from "./lib/save.js";
const OUT = new URL("../data/live_networks/", import.meta.url).pathname;

const SOURCES = [
  { id: "adsb.lol",       byHex: (h) => `https://api.adsb.lol/v2/hex/${h}`,        byReg: (r) => `https://api.adsb.lol/v2/reg/${r}` },
  { id: "adsb.fi",        byHex: (h) => `https://opendata.adsb.fi/api/v2/hex/${h}`, byReg: (r) => `https://opendata.adsb.fi/api/v2/registration/${r}` },
  { id: "airplanes.live", byHex: (h) => `https://api.airplanes.live/v2/hex/${h}`,   byReg: (r) => `https://api.airplanes.live/v2/reg/${r}` },
];

if (import.meta.url === `file://${process.argv[1]}`) {
  const list = process.argv[2] ? [byReg(process.argv[2])].filter(Boolean) : FLEET.filter((a) => a.side === "following");
  for (const ac of list) {
    for (const s of SOURCES) {
      for (const [kind, url] of [["hex", s.byHex(ac.hex)], ["reg", s.byReg(ac.reg)]]) {
        const { status, text, json } = await getJSON(url).catch((e) => ({ status: 0, text: String(e), json: null }));
        const n = json?.ac?.length ?? json?.aircraft?.length ?? 0;
        await savePull({ dir: `${OUT}${ac.reg}`, name: `${s.id}_${kind}.json`, url, status, body: text,
          note: `${n} live aircraft returned. Live-position endpoint - an empty result means NOT AIRBORNE NOW, not absent from history.` });
        console.log(`${ac.reg.padEnd(8)} ${s.id.padEnd(15)} ${kind}  HTTP ${String(status).padStart(3)}  ${n} aircraft live`);
        await sleep(300);
      }
    }
  }
}
