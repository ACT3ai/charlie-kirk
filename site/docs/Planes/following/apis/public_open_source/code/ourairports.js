#!/usr/bin/env node
// OurAirports - public-domain airport reference data, ~80,000 fields worldwide.
// CC0, downloadable as plain CSV, no key.
//
// This is how a page gets to say "a single strip with a windsock" with a number
// behind it instead of an adjective: runway length, elevation, whether the field is
// classed small/medium/large, and the scheduled-service flag. The whole
// how-unusual-is-a-foreign-state-jet-here argument rests on those facts, so they
// should come from a public dataset a reader can download, not from us.
//
//   node ourairports.js            refresh and index every airport in airports.csv
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { savePull } from "./lib/save.js";
const OUT = new URL("../data/ourairports/", import.meta.url).pathname;
const FOLLOW = "/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk/site/docs/Planes/following";
const FILES = {
  airports: "https://davidmegginson.github.io/ourairports-data/airports.csv",
  runways: "https://davidmegginson.github.io/ourairports-data/runways.csv",
};

if (import.meta.url === `file://${process.argv[1]}`) {
  await mkdir(OUT, { recursive: true });
  const got = {};
  for (const [name, url] of Object.entries(FILES)) {
    const res = await fetch(url);
    const text = await res.text();
    await savePull({ dir: OUT, name: `${name}.csv`, url, status: res.status, body: text });
    got[name] = text;
    console.log(`${name}.csv  HTTP ${res.status}  ${text.length.toLocaleString()} bytes`);
  }
  // Index just the fields this investigation names, so the join is small and readable.
  const ours = (await readFile(`${FOLLOW}/airports.csv`, "utf8")).split("\n").slice(1)
    .map((l) => l.split(",")[0]).filter((c) => /^[A-Z]{4}$/.test(c));
  const lines = got.airports.split("\n");
  const head = lines[0].split(",").map((h) => h.replace(/"/g, ""));
  const iIdent = head.indexOf("ident");
  const picked = lines.filter((l, i) => i === 0 || ours.includes((l.split(",")[iIdent] ?? "").replace(/"/g, "")));
  await writeFile(`${OUT}airports_in_this_case.csv`, picked.join("\n"));
  console.log(`indexed ${picked.length - 1} of ${ours.length} case airports into airports_in_this_case.csv`);
}
