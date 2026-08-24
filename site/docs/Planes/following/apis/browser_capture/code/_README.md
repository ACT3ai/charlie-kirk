# `browser_capture/code` — driving a real browser at the tracking sites

`targets.json` is the work list: one entry per (site, aircraft), with the URL, the
ICAO hex, which investigation thread the aircraft belongs to, and a note on what
that site is good for and where it will fight you.

There is no fetcher here on purpose. **This pass is driven by Claude Code's browser
tools**, following `../p_get_data.mdx`, because the whole point is to capture what a
human visitor actually sees — rendered, with its JavaScript run — rather than what a
scraper can pull out of the HTML.

The one command-line tool this pass does use:

    brew install monolith
    monolith -o captures/<site>/<tail>/<utc>.html "<url>"

`monolith` inlines every asset into a single self-contained file, so a captured page
still renders years later after the site has been redesigned. Use it alongside the
screenshot, not instead of it — a screenshot proves what was displayed, monolith
preserves what was underneath.

## Every capture needs four things or it does not count

1. The screenshot.
2. The page text.
3. The URL and the **UTC** time of capture.
4. The HTTP status.

## The comparison is the finding

A capture on its own says "this is what the page shows today". Paired with the
Internet Archive snapshot nearest the claim date — `wayback.js` in the open-source
pass — it can say "this is what the page showed then, and this is what it shows now."
That pairing is the only way this repo can honestly say data was removed.

**And it still cannot say why.** A redesign, a URL change, a retention window
rolling over, and a deliberate removal all look the same from outside. Every page
built from these captures says so.
