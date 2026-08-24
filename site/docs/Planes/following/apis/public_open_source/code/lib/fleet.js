// The aircraft this investigation tracks, and the identifiers every API needs.
//
// hex        = ICAO 24-bit address, lowercase. THE join key for every ADS-B source.
// reg        = civil registration / tail number as painted.
// side       = following | kirk | military | unknown  — NEVER merge the threads.
// hexSource  = where the hex came from, so a wrong one is traceable.
//
// CONFLICT ON RECORD: api.adsbdb.com returns 0101F0 for SU-BTT. The adsb.lol
// historical trace for 0101D3 self-identifies as `"r":"SU-BTT","t":"FA7X"` and
// carries a real 2025-09-10 Provo->Wilmington track, while 0101F0 has no trace
// on that date. We use 0101D3 and record the disagreement rather than hiding it.

export const FLEET = [
  // --- the "following" fleet: foreign-registered, the subject of the claim ---
  { reg: "SU-BTT", hex: "0101d3", side: "following", type: "FA7X", registry: "Egypt",
    note: "yellow plane. Lead tail of the 73-overlap claim.", hexSource: "adsb.lol trace self-ID" },
  { reg: "SU-BND", hex: "01003e", side: "following", type: "GLF4", registry: "Egypt",
    note: "blue plane. Second lead tail.", hexSource: "planes.csv + adsbdb agree" },
  { reg: "SU-BTU", hex: "0101d0", side: "following", type: "FA7X", registry: "Egypt",
    note: "Armada tail. Claimed el-Sisi personal jet.", hexSource: "planes.csv + adsbdb agree" },
  { reg: "SU-BTV", hex: "0101d1", side: "following", type: "FA7X", registry: "Egypt",
    note: "Armada tail.", hexSource: "planes.csv + adsbdb agree" },
  { reg: "SU-BGM", hex: "010070", side: "following", type: "GLF4", registry: "Egypt",
    note: "Armada tail. Two April 2025 Provo legs only.", hexSource: "planes.csv + adsbdb agree" },
  { reg: "T7-ELL", hex: "50018a", side: "following", type: "GLEX", registry: "San Marino",
    note: "T7- is SAN MARINO, not Egypt. adsbdb operator: Solairus Aviation.", hexSource: "adsbdb" },

  // --- the Kirk / TPUSA side: where the Kirks and the organisation actually were ---
  { reg: "N102DZ",  hex: "a00c85", side: "kirk", type: "GLF5", registry: "United States",
    note: "Owner per adsbdb: Aviation Enterprises Inc.", hexSource: "adsbdb" },
  { reg: "N888KG",  hex: "ac3c75", side: "kirk", type: "CL30", registry: "United States",
    note: "Wendover departure thread. SEPARATE CLAIM - do not merge.", hexSource: "adsbdb" },
  { reg: "N560TW",  hex: "a728a8", side: "kirk", type: "C56X", registry: "United States",
    note: "Scottsdale-Provo-Santa Barbara-Scottsdale, 10 Sep 2025.", hexSource: "adsbdb" },
  { reg: "N582MM",  hex: "a77e75", side: "kirk", type: "LJ60", registry: "United States",
    note: "TPUSA-associated aircraft.", hexSource: "adsbdb" },
  { reg: "N872RA",  hex: "abff3c", side: "kirk", type: "BE40", registry: "United States",
    note: "Provo arrival.", hexSource: "adsbdb" },
  { reg: "N40JD",   hex: "a4ab14", side: "kirk", type: "PRM1", registry: "United States",
    note: "Provo arrival.", hexSource: "adsbdb" },

  // --- the N1098L / survey thread: DIFFERENT AIRCRAFT, DIFFERENT CLAIM ---
  { reg: "N1098L",  hex: "a0299e", side: "n1098l", type: "GLEX", registry: "United States",
    note: "LASAI Aviation II LLC. Fort Huachuca / HADES thread.", hexSource: "adsbdb" },
  { reg: "N2100L",  hex: "a1bbe5", side: "n1098l", type: "GLEX", registry: "United States",
    note: "LASAI Aviation II LLC - same registered owner as N1098L.", hexSource: "adsbdb" },
  { reg: "N59906",  hex: "a7c14d", side: "n1098l", type: "PA31", registry: "United States",
    note: "MARC Inc survey aircraft.", hexSource: "adsbdb" },
  { reg: "N55906",  hex: "a72351", side: "n1098l", type: "P28R", registry: "United States",
    note: "Piper Arrow. Named in a Cullen claim; a light single, not a survey platform.",
    hexSource: "adsbdb" },
];

// Callsign-only entries. These have NO fixed hex - a SAM callsign is assigned to
// whichever USAF airframe flies the mission, so they are queried by callsign.
export const CALLSIGNS = [
  { call: "SAM000", side: "military" }, { call: "SAM112", side: "military" },
  { call: "SAM650", side: "military" }, { call: "SAM702", side: "military" },
  { call: "EJM36",  side: "unknown",
    note: "EJM = Executive Jet Management ICAO operator designator. A CALLSIGN, not a registration." },
];

export const byReg = (r) => FLEET.find((a) => a.reg.toUpperCase() === r.toUpperCase());
export const following = () => FLEET.filter((a) => a.side === "following");
