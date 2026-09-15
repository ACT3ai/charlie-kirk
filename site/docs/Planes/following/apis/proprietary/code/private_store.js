// Where the RAW commercial responses live. Not in this repo.
//
// This repo is public, and FlightAware's terms do not allow republishing an AeroAPI
// response. So the raw pulls, the spend ledger, the plans and the verdicts built from
// them are checked in to the PRIVATE `all` repo instead (Bryan, 14 Sep 2026):
//
//   ~/BGit/all/politics/charlie_kirk/flights/<vendor>/
//
// What IS published is the restated version - every fact, laid out in our own
// structure - written by p_restate_flight_data.md into ../data/<vendor>_restated/.
//
// Resolution order, first directory that exists wins:
//   1. $CK_PRIVATE_FLIGHTS_DIR
//   2. ~/BGit/all/politics/charlie_kirk/flights
//   3. <checkout>/../all/politics/charlie_kirk/flights   (the two repos side by side)
// If none exists this THROWS. It never falls back to a directory inside this repo:
// a raw response written into the public tree is one `git add .` from being published.
import { existsSync } from "node:fs";
import { homedir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const CHECKOUT = resolve(fileURLToPath(new URL(".", import.meta.url)), "../../../../../../..");

export function privateFlightsDir() {
  const candidates = [
    process.env.CK_PRIVATE_FLIGHTS_DIR,
    join(homedir(), "BGit/all/politics/charlie_kirk/flights"),
    resolve(CHECKOUT, "../all/politics/charlie_kirk/flights"),
  ].filter(Boolean);
  const hit = candidates.find((d) => existsSync(d));
  if (!hit) {
    throw new Error(`private flights directory not found - clone the private "all" repo or set CK_PRIVATE_FLIGHTS_DIR. Looked in: ${candidates.join(" | ")}`);
  }
  return hit;
}

/** <private>/<vendor>/ with a trailing slash, e.g. privateVendorDir("flightaware"). */
export const privateVendorDir = (vendor) => `${join(privateFlightsDir(), vendor)}/`;
