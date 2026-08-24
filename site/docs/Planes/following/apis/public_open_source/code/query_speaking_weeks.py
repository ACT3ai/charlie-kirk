#!/usr/bin/env python3
"""Query Grok (xAI Responses API + x_search) once per week, Jan 2022–Oct 2025.

Writes:
  site/docs/Planes/following/speaking/week/{year}/week_{NN}.md

Auth: ~/.grok/auth.json (Grok CLI OIDC session). Never prints the token.

Resume: skips a week whose markdown already has status: completed.
Retry: files with status: error are retried.

Usage:
  python3 query_speaking_weeks.py
  python3 query_speaking_weeks.py --limit 2
  python3 query_speaking_weeks.py --workers 3
  python3 query_speaking_weeks.py --model grok-4.6
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
import traceback
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

API_URL = "https://api.x.ai/v1/responses"
AUTH_PATH = Path.home() / ".grok" / "auth.json"
ROOT = Path("/Users/bryanstarbuck/BGit/Bryan_git/charlie-kirk")
OUT_DIR = ROOT / "site/docs/Planes/following/speaking/week"
PROGRESS = OUT_DIR / "_progress.log"

QUERY_TEMPLATE = (
    "Search twitter and x.com posts for where Charlie Kirk or TPUSA has "
    "public speaking events or where Charlie will be and speak.  Look at "
    "posts between the week date range {start} to the end of the week {end}.  "
    "Include all data. Don't summarize"
)

RANGE_START = date(2022, 1, 1)
RANGE_END = date(2025, 10, 31)

_token_lock = threading.Lock()
_print_lock = threading.Lock()


def log(msg: str) -> None:
    line = f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {msg}"
    with _print_lock:
        print(line, flush=True)
        PROGRESS.parent.mkdir(parents=True, exist_ok=True)
        with PROGRESS.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def load_token() -> str:
    data = json.loads(AUTH_PATH.read_text())
    entry = next(iter(data.values()))
    token = entry.get("key") or entry.get("access_token")
    if not token:
        raise SystemExit("no token in ~/.grok/auth.json")
    return token


def token_expires_at() -> datetime | None:
    data = json.loads(AUTH_PATH.read_text())
    entry = next(iter(data.values()))
    raw = entry.get("expires_at")
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def refresh_token() -> None:
    """Ask the Grok CLI to mint a fresh session token, then re-read auth.json."""
    log("refreshing Grok CLI session token")
    env = os.environ.copy()
    env.pop("GROK_AGENT", None)
    try:
        subprocess.run(
            [
                str(Path.home() / ".grok/bin/grok"),
                "-p",
                "ok",
                "--max-turns",
                "1",
                "--output-format",
                "plain",
                "--disallowed-tools",
                "Agent,run_terminal_cmd,search_replace,write,read_file",
            ],
            cwd=str(ROOT),
            env=env,
            timeout=90,
            check=False,
            capture_output=True,
        )
    except Exception as e:
        log(f"token refresh spawn failed: {type(e).__name__}: {e}")


def ensure_token() -> str:
    with _token_lock:
        exp = token_expires_at()
        now = datetime.now(timezone.utc)
        if exp is not None and exp - now < timedelta(minutes=8):
            refresh_token()
        return load_token()


def iter_weeks():
    """Calendar 7-day blocks from Jan 1 of each year, clipped to RANGE_*."""
    for year in range(RANGE_START.year, RANGE_END.year + 1):
        d = date(year, 1, 1)
        n = 1
        year_end = date(year, 12, 31)
        while d.year == year:
            end = min(d + timedelta(days=6), year_end)
            if end >= RANGE_START and d <= RANGE_END:
                yield {
                    "year": year,
                    "week": n,
                    "start": max(d, RANGE_START),
                    "end": min(end, RANGE_END),
                }
            d = d + timedelta(days=7)
            n += 1
            if d > RANGE_END:
                return


def week_path(item: dict) -> Path:
    return OUT_DIR / str(item["year"]) / f"week_{item['week']:02d}.md"


def already_done(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:400]
    except OSError:
        return False
    return "status: completed" in head


def extract_text(data: dict) -> str:
    chunks = []
    for item in data.get("output") or []:
        if item.get("type") != "message":
            continue
        content = item.get("content")
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and part.get("text"):
                    chunks.append(part["text"])
        elif isinstance(content, str):
            chunks.append(content)
    return "\n\n".join(chunks).strip()


def extract_tool_calls(data: dict) -> list[dict]:
    out = []
    for item in data.get("output") or []:
        if item.get("type") in ("custom_tool_call", "function_call", "tool_call"):
            inp = item.get("input") or item.get("arguments") or item.get("function", {}).get("arguments")
            if isinstance(inp, str):
                try:
                    inp = json.loads(inp)
                except json.JSONDecodeError:
                    pass
            out.append(
                {
                    "name": item.get("name") or item.get("function", {}).get("name"),
                    "input": inp,
                    "status": item.get("status"),
                }
            )
    return out


def extract_annotations(data: dict) -> list:
    anns = []
    for item in data.get("output") or []:
        if item.get("type") != "message":
            continue
        content = item.get("content")
        if not isinstance(content, list):
            continue
        for part in content:
            if isinstance(part, dict) and part.get("annotations"):
                anns.extend(part["annotations"])
    return anns


def fence(text: str) -> str:
    body = text or ""
    ticks = "```"
    while ticks in body:
        ticks += "`"
    return f"{ticks}text\n{body}\n{ticks}"


def render_md(item: dict, query: str, data: dict | None, error: str | None) -> str:
    start = item["start"].isoformat()
    end = item["end"].isoformat()
    year = item["year"]
    week = item["week"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    status = "error" if error else "completed"
    model = (data or {}).get("model") or ""
    usage = (data or {}).get("usage") or {}
    title = f"Week {week:02d} {year} Charlie Kirk / TPUSA speaking search"
    lines = [
        "---",
        "unlisted: true",
        f'title: "{title}"',
        f"sidebar_label: \"{year}-W{week:02d}\"",
        f"description: \"Grok X-search dump for Charlie Kirk / TPUSA speaking posts {start} to {end}.\"",
        f"status: {status}",
        "hide_table_of_contents: true",
        "---",
        "",
        f"# Week {week:02d}, {year}",
        "",
        f"- Date range: {start} to {end}",
        f"- Queried at (UTC): {now}",
        f"- Model: {model}",
        f"- API status: {(data or {}).get('status') or 'n/a'}",
        f"- Response id: {(data or {}).get('id') or 'n/a'}",
        "",
        "## Query sent to Grok",
        "",
        fence(query),
        "",
    ]
    if error:
        lines += ["## Error", "", fence(error), ""]
        if data:
            lines += ["## Raw API body (truncated)", "", fence(json.dumps(data, default=str)[:20000]), ""]
        return "\n".join(lines) + "\n"

    tools = extract_tool_calls(data or {})
    lines += [
        "## Grok X-search tool calls",
        "",
        fence(json.dumps(tools, indent=2, ensure_ascii=False)),
        "",
        "## Usage",
        "",
        fence(json.dumps(usage, indent=2, default=str)),
        "",
    ]
    anns = extract_annotations(data or {})
    if anns:
        lines += [
            "## Annotations / citations",
            "",
            fence(json.dumps(anns, indent=2, ensure_ascii=False, default=str)),
            "",
        ]
    text = extract_text(data or {})
    lines += [
        "## Grok response",
        "",
        fence(text if text else "(empty response text)"),
        "",
    ]
    return "\n".join(lines) + "\n"


def call_grok(query: str, start: str, end: str, model: str, timeout: int) -> dict:
    payload = {
        "model": model,
        "input": [{"role": "user", "content": query}],
        "tools": [
            {
                "type": "x_search",
                "from_date": start,
                "to_date": end,
            }
        ],
    }
    body = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(4):
        token = ensure_token()
        req = urllib.request.Request(
            API_URL,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")
            last_err = f"HTTP {e.code}: {raw[:2000]}"
            if e.code in (401, 403) and attempt < 3:
                log(f"auth error HTTP {e.code}, refreshing token")
                with _token_lock:
                    refresh_token()
                time.sleep(2)
                continue
            if e.code == 429:
                wait = 15 * (attempt + 1)
                log(f"rate limited, sleeping {wait}s")
                time.sleep(wait)
                continue
            if e.code >= 500:
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(last_err) from e
        except (TimeoutError, urllib.error.URLError) as e:
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(5 * (attempt + 1))
            continue
    raise RuntimeError(last_err or "unknown Grok API failure")


def process_week(item: dict, model: str, timeout: int) -> str:
    path = week_path(item)
    if already_done(path):
        return "skip"
    query = QUERY_TEMPLATE.format(
        start=item["start"].isoformat(),
        end=item["end"].isoformat(),
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = call_grok(
            query,
            item["start"].isoformat(),
            item["end"].isoformat(),
            model,
            timeout,
        )
        if data.get("status") not in (None, "completed"):
            md = render_md(item, query, data, error=f"API status={data.get('status')}")
            path.write_text(md, encoding="utf-8")
            return "error"
        path.write_text(render_md(item, query, data, error=None), encoding="utf-8")
        return "ok"
    except Exception as e:
        err = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        path.write_text(render_md(item, query, None, error=err), encoding="utf-8")
        return "error"


def write_category() -> None:
    cat = {
        "label": "Weekly X searches",
        "position": 99,
        "collapsed": True,
        "link": {"type": "generated-index", "title": "Weekly Grok X searches for Charlie Kirk / TPUSA speaking events"},
    }
    (OUT_DIR / "_category_.json").write_text(json.dumps(cat, indent=2) + "\n", encoding="utf-8")
    for year in range(RANGE_START.year, RANGE_END.year + 1):
        ydir = OUT_DIR / str(year)
        ydir.mkdir(parents=True, exist_ok=True)
        (ydir / "_category_.json").write_text(
            json.dumps(
                {
                    "label": str(year),
                    "collapsed": True,
                    "link": {"type": "generated-index", "title": f"{year} weekly Grok X searches"},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="grok-4-fast-non-reasoning")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--force", action="store_true", help="re-query weeks already completed")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_category()
    weeks = list(iter_weeks())
    if args.limit:
        weeks = weeks[: args.limit]
    if not args.force:
        pending = [w for w in weeks if not already_done(week_path(w))]
    else:
        pending = weeks
    log(
        f"weeks total={len(list(iter_weeks()))} selected={len(weeks)} "
        f"pending={len(pending)} model={args.model} workers={args.workers}"
    )
    if not pending:
        log("nothing to do")
        return 0

    ok = skip = err = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        futs = {
            ex.submit(process_week, w, args.model, args.timeout): w for w in pending
        }
        for fut in as_completed(futs):
            w = futs[fut]
            label = f"{w['year']}-W{w['week']:02d} {w['start']}..{w['end']}"
            try:
                result = fut.result()
            except Exception as e:
                result = "error"
                log(f"FAIL {label} {type(e).__name__}: {e}")
            if result == "ok":
                ok += 1
            elif result == "skip":
                skip += 1
            else:
                err += 1
            log(f"{result:4} {label}  running_ok={ok} err={err} skip={skip} left~={len(pending)-ok-err-skip}")
    log(f"DONE ok={ok} err={err} skip={skip}")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
