// Every pull is written twice: the payload, and a .meta.json beside it recording
// exactly how it was obtained. NEVER overwrite a previous pull - the diff between
// two pulls of the same endpoint on two dates is the evidence that data vanished.
import { mkdir, writeFile, access } from "node:fs/promises";
import { dirname } from "node:path";

export async function savePull({ dir, name, url, status, body, note }) {
  await mkdir(dir, { recursive: true });
  const stamp = new Date().toISOString().replace(/[:.]/g, "-");
  const base = `${dir}/${name}`;
  let out = base;
  try { await access(out); out = `${base}.pulled-${stamp}`; } catch { /* first pull */ }
  const bytes = body == null ? 0 : Buffer.byteLength(body);
  if (body != null) await writeFile(out, body);
  await writeFile(`${out}.meta.json`, JSON.stringify({
    url, http_status: status, bytes, retrieved_utc: new Date().toISOString(),
    tool: "charlie-kirk/site/docs/Planes/following/apis/public_open_source/code",
    note: note ?? null,
  }, null, 2) + "\n");
  return { path: out, bytes, status };
}

export async function getJSON(url, opts = {}) {
  const res = await fetch(url, { redirect: "follow", ...opts });
  const text = await res.text();
  let json = null;
  try { json = JSON.parse(text); } catch { /* not json */ }
  return { status: res.status, text, json };
}

export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
