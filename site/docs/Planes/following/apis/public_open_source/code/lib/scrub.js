// Redact THIRD-PARTY vendor credentials out of a capture BEFORE it hits disk.
//
// Flightradar24 and FlightAware ship their own client-side keys inside the HTML
// they serve — a Mapbox token, a Stadia Maps key, a Vicinity token, a Firebase
// web key. Archiving their page verbatim archives those keys too, and GitHub
// push protection rejects a push that carries one. On 2026-08-24 exactly that
// blocked this investigation from publishing, over FlightAware's Mapbox token
// in a captured N102DZ page.
//
// So the value is replaced, in place, with
//
//     __REDACTED_VENDOR_CREDENTIAL_sha256_<first 16 hex of sha256(value)>
//
// The key name, the markup and every byte of flight data are untouched. The
// fingerprint is one-way but stable, so two captures that carried the same
// vendor key still fingerprint identically — the "this page served the same key
// as that page" chain survives. We lose the secret, not the proof.
//
// This is the write-time twin of security/scrub_vendor_tokens.py, which sweeps
// captures already on disk. Keep the two in step: same patterns, same marker.
import { createHash } from "node:crypto";

const MARK = "__REDACTED_VENDOR_CREDENTIAL_sha256_";
const fingerprint = (v) => MARK + createHash("sha256").update(v).digest("hex").slice(0, 16) + "__";

// Unmistakable credential shapes, redacted wherever they appear — including
// inside a URL query such as ?access_token=pk.eyJ...
const SHAPES = [
  /\b(?:pk|sk)\.eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}/g,   // Mapbox
  /\bAIza[0-9A-Za-z_-]{35}\b/g,                                 // Google / Firebase
  /\bAKIA[0-9A-Z]{16}\b/g,                                      // AWS
  /\bgh[pousr]_[A-Za-z0-9]{36,}\b/g,                            // GitHub
  /\bxox[abposr]-[A-Za-z0-9-]{10,}/g,                           // Slack
  /\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}/g, // JWT
];

// Named assignments where the NAME is what marks it as a credential — the value
// alone (a UUID, a hex blob) would not be conclusive. Curated on purpose:
// over-redaction would damage the capture, which is the thing being preserved.
const NAMED =
  /(["']?)(MAPBOX_(?:API|ACCESS)_TOKEN|STADIA_MAPS_API_KEY|VICINITY_TOKEN|GOOGLE_MAPS_API_KEY|MAPTILER_KEY|api[_-]?key|apikey|access[_-]?token|auth[_-]?token|bearer[_-]?token|client[_-]?secret)\1(\s*[:=]\s*)(["'])([^"'\s]{16,})\4/gi;

const PLACEHOLDER = /^(?:your|my|the|test|demo|sample|example|placeholder|dummy|fake|none|null|undefined|changeme|x{3,}|\.\.\.|<|\{|\$)/i;

function isCredentialValue(v) {
  if (v.length < 16 || PLACEHOLDER.test(v) || v.startsWith(MARK)) return false;
  if (v.includes("/") || v.startsWith("http")) return false;
  const hasDigit = /[0-9]/.test(v);
  const hasAlpha = /[A-Za-z]/.test(v);
  // "us-anything-254-charlie-and-aliens" reads as words; a key does not.
  const wordy = v.split(/[-_.]/).filter((w) => /^[A-Za-z]{3,}$/.test(w)).length >= 3;
  return hasDigit && hasAlpha && !wordy;
}

/** Redact vendor credentials in `text`. Returns { text, count }. */
export function scrubVendorCredentials(text) {
  if (typeof text !== "string" || text === "") return { text, count: 0 };
  let count = 0;
  let out = text;
  for (const shape of SHAPES) {
    out = out.replace(shape, (m) => { count++; return fingerprint(m); });
  }
  out = out.replace(NAMED, (whole, q, name, sep, vq, value) => {
    if (!isCredentialValue(value)) return whole;
    count++;
    return `${q}${name}${q}${sep}${vq}${fingerprint(value)}${vq}`;
  });
  return { text: out, count };
}
