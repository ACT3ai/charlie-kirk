# The corrected tally, and where it was applied

Run 26 August 2026. Not a published page (leading underscore).

`code/corrected_tally.py` re-tallies all 85 rows of `overlaps.csv` using the per-row verdict the
claims audit reached by reading every position fix in every recovered trace, and prints the
before/after. Re-run it any time: `python3 code/corrected_tally.py`.

## The numbers

| | 24 Aug pass | **Corrected 26 Aug** |
|---|---:|---:|
| Supported at the claimed field | 24 | **27** |
| Contradicted | 12 | **2** |
| Not heard (asked, archive empty) | 22 | 30 |
| No archive coverage | 20 | 17 |
| No tail named | 2 | 4 |
| No date named | 5 | 5 |
| **Decidable** | 36 | **29** |
| **Contradicted share of decidable** | 33% | **7%** |

**10 of the 12 published refutations were retracted.** Why, by count:

* 6 — refuted on a **different day** than the one claimed (OWENS-016, 028, 029, 030, 052, 055)
* 2 — aircraft was **at** the claimed field; refutation reversed (OWENS-024, SITE-003)
* 1 — closest approach read off the **shorter archive trace** (OWENS-012)
* 1 — **half** the row confirmed, half untested (OWENS-015)

The 2 that hold: **OWENS-050** (hard — Paris-Le Bourget to Inshas AB Cairo, 7,034 km from
St. Louis) and **OWENS-036** (weak — the whole day's holding is 5 minutes at FL320 over Egypt).

One confirmation was **downgraded**: OWENS-010's 0.48 km from KSTL was at 3,357 ft AGL, an
overflight; the aircraft landed 24 km away at KSUS. SITE-001 borrowed that day and is now untested.

## Against the X/Twitter accuracy audit (22/43/39 of 65)

| The audit said | primary data supports | contradicts | cannot test |
|---|---:|---:|---:|
| accurate | 17 | 0 | 4 |
| partially accurate | 7 | 0 | 1 |
| **inaccurate** | **3** | **2** | **39** |

**Of the 44 rows the audit marks inaccurate, primary ADS-B reaches 5, and the audit is wrong on 3
of those 5.** The three it gets wrong are OWENS-021 (SU-BTT on the surface at Wilmington, 0.82 km),
OWENS-025 (SU-BND on the ground at Provo, **0.02 km**) and OWENS-041 (SU-BTT on the ground at Provo
on **10 September 2025**, 0.03 km — the marquee row).

**Of its 29 accurate/partial rows, 24 are confirmed by primary position data and none contradicted.**

**The honest limit, which must travel with every quote of the above.** The other 39 negative
verdicts are **untested, not refuted**. The auditor used FlightRadar24 Business and a $950
FlightAware tier, which reach dates no free volunteer archive does. "Wrong where it can be checked"
is the claim this data supports. "Wrong overall" is not.

## Recovery volume behind these numbers

| | |
|---|---:|
| Case aircraft-days of primary position data recovered | **1,831** |
| Case aircraft | 15 |
| Trace payload files | 3,619 |
| Raw position data on disk | 308 MB |
| Days asked about and empty (`.miss.json.meta.json`) | 15,721 |
| Control aircraft-days pulled alongside | 404 |

By source: airplanes-live 1,906 · adsb-lol 1,504 · adsbexchange-samples 207 · adsblol-github-backup 2.
By year: 2022 34 · 2023 807 · 2024 1,211 · 2025 1,351 · 2026 216.

**Flight records shown to be removed from anywhere: zero.** The 15,721 empty days are a coverage
fact, not a deletion count — see `site/docs/Planes/Deleted-Flight-Records.mdx`, where every
suppression hypothesis was tested against control airframes and none survived.

## Pages updated (43 .mdx)

Headline: `Planes/overview`, `Following-Charlie-Erika`, `Deleted-Flight-Records`,
`Charlie-Erika-Aircraft/overview`, `SU-BTT/overview`, `SU-BND/overview`,
`Flight-Data-Recovery/overview`, `Flight-Data-Recovery/Overlap-Recovery`,
`following/73_overlaps`, `following/overlap/overview`, `following/apis/overview`,
`following/apis/government/knowledge`, `following/apis/public_open_source/knowledge`.

Row-level retractions/corrections: OWENS-010, 012, 015, 016, 024, 028, 029, 030, 036, 052, 055,
SITE-001, SITE-003.

Boilerplate tally line: 18 overlap pages.

`site/` builds clean; `pages.csv` line counts refreshed.
