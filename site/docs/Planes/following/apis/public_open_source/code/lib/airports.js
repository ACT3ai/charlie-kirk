// Turn a latitude/longitude out of an ADS-B trace into a named field.
//
// THIS IS GEOMETRY, NOT A LANDING RECORD. The nearest airport to a position is
// the nearest airport to a position. A point 1.2 km from a runway with the
// on-ground flag set is as good as this method gets; a point 14 km away names
// the closest field and nothing more. EVERY resolved airport carries its
// distance for exactly that reason, and no page here states an arrival without
// it. The Provo-versus-Dugway mislabel that this investigation already had to
// correct is what happens when a nearest-field label is read as a destination.
import { readFileSync } from "node:fs";

const CSV = new URL("../../data/ourairports/airports.csv", import.meta.url).pathname;
const SKIP = new Set(["closed", "heliport", "seaplane_base", "balloonport"]);

function parseCSV(text) {
  const rows = []; let row = [], cur = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(cur); cur = ""; }
    else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; }
    else if (c !== "\r") cur += c;
  }
  if (cur || row.length) { row.push(cur); rows.push(row); }
  return rows;
}

let APTS = null;
function load() {
  if (APTS) return APTS;
  const rows = parseCSV(readFileSync(CSV, "utf8"));
  const h = rows[0]; const ix = (n) => h.indexOf(n);
  const [I, T, N, LA, LO, MU, RE, CO, IA] =
    ["ident", "type", "name", "latitude_deg", "longitude_deg", "municipality", "iso_region", "iso_country", "iata_code"].map(ix);
  APTS = [];
  for (let i = 1; i < rows.length; i++) {
    const r = rows[i]; if (!r || r.length < 10) continue;
    if (SKIP.has(r[T])) continue;
    const la = +r[LA], lo = +r[LO];
    if (!isFinite(la) || !isFinite(lo)) continue;
    APTS.push({ icao: r[I], iata: r[IA], name: r[N], lat: la, lon: lo,
                city: r[MU], region: r[RE], country: r[CO], type: r[T] });
  }
  APTS.sort((a, b) => a.lat - b.lat);
  return APTS;
}

const R = Math.PI / 180;
export function nearest(lat, lon, { maxDeg = 1.0 } = {}) {
  const a = load();
  let lo = 0, hi = a.length;
  while (lo < hi) { const m = (lo + hi) >> 1; if (a[m].lat < lat - maxDeg) lo = m + 1; else hi = m; }
  let best = null, bd = Infinity;
  for (let i = lo; i < a.length && a[i].lat <= lat + maxDeg; i++) {
    const dy = (a[i].lat - lat) * 111.32;
    const dx = (a[i].lon - lon) * 111.32 * Math.cos(lat * R);
    const d = Math.hypot(dx, dy);
    if (d < bd) { bd = d; best = a[i]; }
  }
  return best ? { ...best, km: +bd.toFixed(2) } : null;
}

// A LABEL, not a claim. "KPVU (Provo Municipal, Provo US-UT) 1.1km" reads as
// what it is; "Provo" on its own does not.
export function label(lat, lon) {
  const a = nearest(lat, lon);
  if (!a) return `unresolved ${lat.toFixed(3)},${lon.toFixed(3)}`;
  const where = [a.city, a.country === "US" ? a.region.split("-").pop() : a.country].filter(Boolean).join(" ");
  return `${a.icao}${a.iata ? "/" + a.iata : ""} (${a.name}, ${where}) ${a.km}km`;
}
