#!/usr/bin/env node
// OpenSky Network - the research-grade open network. Run by a university
// consortium, and the only free source with a documented HISTORICAL flight-list
// endpoint (/flights/aircraft).
//
// AUTHENTICATION CHANGED. Since 18 March 2026 basic auth with an OpenSky username
// and password is GONE. It is OAuth2 client-credentials now: create an API client
// in your OpenSky account, then exchange client_id + client_secret for a bearer
// token that expires after 30 minutes.
//
// CREDENTIALS: OPENSKY_CLIENT_ID and OPENSKY_CLIENT_SECRET. They come from
// ~/.credentials/charlie_kirk.json (charlie_kirk.flight_apis.*) or from the
// environment. Never from a file in this repo. See lib/credentials.js.
//   export OPENSKY_CLIENT_ID=...      # optional, overrides the store
//   export OPENSKY_CLIENT_SECRET=...
//
// WITHOUT CREDENTIALS: anonymous callers get HTTP 403 with the body
// "You cannot access historical flights" - verified 24 August 2026. Anonymous
// access is limited to the live /states/all endpoint.
//
// CREDITS: separate daily pools for states / tracks / flights. Anonymous 400,
// registered 4000, feeder accounts 8000. /flights/* is charged by the number of
// calendar-day partitions the time range crosses, so ask one day at a time.
// Over the limit returns 429 with X-Rate-Limit-Retry-After-Seconds.
//
//   node opensky.js SU-BTT 2025-09-10
import { FLEET, byReg } from "./lib/fleet.js";
import { savePull, getJSON, sleep } from "./lib/save.js";
import { cred } from "./lib/credentials.js";
const OUT = new URL("../data/opensky/", import.meta.url).pathname;
const TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token";

export async function token() {
  const id = cred("OPENSKY_CLIENT_ID"), secret = cred("OPENSKY_CLIENT_SECRET");
  if (!id || !secret) return null;
  const res = await fetch(TOKEN_URL, {
    method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "client_credentials", client_id: id, client_secret: secret }),
  });
  if (!res.ok) { console.error(`token exchange failed: HTTP ${res.status}`); return null; }
  return (await res.json()).access_token;
}

export async function flightsOnDay(ac, day, bearer) {
  const begin = Math.floor(Date.parse(day + "T00:00:00Z") / 1000);
  const url = `https://opensky-network.org/api/flights/aircraft?icao24=${ac.hex}&begin=${begin}&end=${begin + 86400}`;
  const { status, text, json } = await getJSON(url, bearer ? { headers: { Authorization: `Bearer ${bearer}` } } : {});
  await savePull({ dir: `${OUT}${ac.reg}`, name: `${day}_flights.json`, url, status, body: text,
    note: bearer ? null : "ANONYMOUS - historical flights are 403 without OAuth2 credentials" });
  return { status, flights: Array.isArray(json) ? json : [] };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const bearer = await token();
  console.log(bearer ? "authenticated via OAuth2 client credentials"
    : "NO CREDENTIALS - put OPENSKY_CLIENT_ID / OPENSKY_CLIENT_SECRET in\n"
    + "~/.credentials/charlie_kirk.json under charlie_kirk.flight_apis. Historical calls will 403.");
  const [who, day] = process.argv.slice(2);
  const list = who && who !== "--following" ? [byReg(who)].filter(Boolean) : FLEET.filter((a) => a.side === "following");
  for (const ac of list) {
    const r = await flightsOnDay(ac, day ?? "2025-09-10", bearer);
    console.log(`${ac.reg.padEnd(8)} ${day ?? "2025-09-10"}  HTTP ${r.status}  ${r.flights.length} flights`);
    for (const f of r.flights) console.log(`   ${f.estDepartureAirport ?? "????"} -> ${f.estArrivalAirport ?? "????"}  callsign=${(f.callsign ?? "").trim()}`);
    await sleep(1200);
  }
}
