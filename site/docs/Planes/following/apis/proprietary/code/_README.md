# `proprietary/code` — the paid vendors

Nothing here runs without a credential, and **that is deliberate**. Every script
fails loudly with the reason, and the reason is meant to be copied into
`../knowledge.mdx` as a blocked-on-credential entry.

| script | vendor | credential | what it would settle |
|---|---|---|---|
| `fr24api.js` | Flightradar24 official API | `FR24_API_TOKEN` | The flight-summary endpoint is the machine-readable form of the aircraft-history table the original claims were screenshotted from. |
| `aeroapi.js` | FlightAware AeroAPI v4 | `AEROAPI_KEY` | History to 2011 — deep enough to cover the whole 2022–2025 window the trackers counted across. Pay per query. |
| `adsbexchange_rapidapi.js` | ADS-B Exchange via RapidAPI | `ADSBX_RAPIDAPI_KEY` | The feed several original claims were read off, now behind a paywall. |

## Rules

* **Credentials come from the environment.** Never a file in this repo, never a
  page, never a commit, never printed.
* **Run Pass 1 first.** adsb.lol serves a free historical archive at the same URL
  shape ADS-B Exchange charges for. Do not buy an answer that is already free.
* **Publish the finding, not the payload.** Commercial terms generally permit
  using the data and stating a conclusion; they do not permit mirroring the feed.
  The raw response stays in `../data/` as our audit trail, and the page says the
  response is held but not published, with the vendor and the query date.
* **Never work around a paywall.** No scraping the vendor's site, no undocumented
  endpoints, no shared keys. A blocked question recorded honestly is worth more
  than an answer obtained badly.
