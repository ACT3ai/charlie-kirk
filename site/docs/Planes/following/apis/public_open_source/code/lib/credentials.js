// Credentials NEVER live in this repo. This module is the one place that knows
// where they do live, so no script has to hardcode a path and no key has to be
// exported by hand before every run.
//
// Lookup order for a name, first hit wins:
//
//   1. process.env[NAME]                       an explicit `export` still works
//   2. ~/.credentials/charlie_kirk.json        the house credential store,
//                                              charlie_kirk.flight_apis.NAME
//   3. $CK_CREDENTIALS_FILE                    override the store's path
//
// The store is the same shape every other app on this machine uses: one file per
// app under ~/.credentials/, top-level key named after the app. It is chmod 600
// and lives OUTSIDE every git repo. If it is readable by anyone else this module
// says so once and keeps going - a loud warning, not a silent risk.
//
// Nothing here ever prints, logs or returns a credential to a caller that did not
// ask for it by name. `have()` and `report()` exist so a script can say what it is
// missing without putting the value anywhere near stdout.
import { readFileSync, statSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";

const STORE = process.env.CK_CREDENTIALS_FILE || join(homedir(), ".credentials", "charlie_kirk.json");
const APP = "charlie_kirk";

let cache = null;

function load() {
  if (cache) return cache;
  cache = {};
  try {
    const st = statSync(STORE);
    if (st.mode & 0o077) {
      console.error(`WARNING: ${STORE} is readable by other users. Run: chmod 600 ${STORE}`);
    }
    const doc = JSON.parse(readFileSync(STORE, "utf8"));
    const app = doc?.[APP] ?? doc ?? {};
    for (const [group, entries] of Object.entries(app)) {
      if (group.startsWith("_") || entries === null || typeof entries !== "object") continue;
      for (const [k, v] of Object.entries(entries)) {
        if (typeof v === "string" && v !== "") cache[k] = v;
      }
    }
  } catch (e) {
    if (e.code !== "ENOENT") console.error(`note: could not read ${STORE}: ${e.message}`);
  }
  return cache;
}

/** The value for NAME, or undefined. Env wins over the store. */
export function cred(name) {
  const fromEnv = process.env[name];
  if (fromEnv) return fromEnv;
  return load()[name] || undefined;
}

/** True when every named credential is present. Never reveals the values. */
export function have(...names) {
  return names.every((n) => Boolean(cred(n)));
}

/** Print where a missing credential should go, and why we are blocked. */
export function report(...names) {
  const missing = names.filter((n) => !cred(n));
  if (!missing.length) return true;
  console.error(`BLOCKED on credential: ${missing.join(", ")} not set.`);
  console.error(`Put it in ${STORE} under ${APP}.flight_apis, or export it in the shell.`);
  console.error("Never commit it to this repo, never paste it onto a page.");
  return false;
}

export const CREDENTIALS_FILE = STORE;
