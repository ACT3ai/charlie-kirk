# Erika Kirk appearances, Jan 2023 – Sep 9 2025: second pass (her own channels)

Output: `erika_events_more.csv` has **0 data rows** (header only).

This pass found **no new in-person appearance** in the window that has both a date and a city and is not already in `erika_events_raw.csv`. Every in-person hit was a duplicate (Bloom 2025, YWLS 2023/2025, AmFest 2024, the Biggs rally, Signal Hill), fell outside the window, or had no city. Scratch files are in `/tmp/erika_events/work2/`. No Candace Owens material and no overlaps spreadsheet were used.

## Useful by-product: BIBLEin365 live Q&A streams (online, city NOT stated, not in person)
The YouTube channel PROCLAIM x BIBLEin365 (UCiysyKqal8Lhd7PlY_tXDeg) held monthly livestreamed Q&As. The descriptions name "the leader of BIBLEin365, Erika Kirk" and Pastor James Kaddis. Each description gives the date. The livestream start time below (UTC) comes from YouTube's liveBroadcastDetails.

These are **not** in-person appearances and do **not** give a location. At most they suggest she was online, not in the air, at about that time. Treat that as a weak signal: a description saying she hosted does not prove she was on the stream.

| date (per description) | stream start UTC | URL |
|---|---|---|
| 2023-02-17 | 2023-02-17T22:02Z | https://www.youtube.com/watch?v=zQV6Z2lbvdw |
| 2023-04-28 | 2023-04-28T20:50Z | https://www.youtube.com/watch?v=qfmgepavKWo |
| 2023-05-19 | 2023-05-19T21:03Z | https://www.youtube.com/watch?v=Ks6-paGgcdU |
| 2023-06-02 | 2023-06-02T21:02Z | https://www.youtube.com/watch?v=bS1BxG6fTH0 |
| 2023-07-14 | 2023-07-14T21:03Z | https://www.youtube.com/watch?v=ElXYC3eRd6Y |
| "August 11, 2023" (stream metadata says 08-18) | 2023-08-18T21:06Z | https://www.youtube.com/watch?v=0Dj7YmpTbkU |
| 2023-09-22 | 2023-09-22T21:02Z | https://www.youtube.com/watch?v=UER2Sy7PSrA |
| 2023-10-20 | 2023-10-20T21:06Z | https://www.youtube.com/watch?v=wM5gioTB56g |
| 2023-11-17 | 2023-11-17T21:04Z | https://www.youtube.com/watch?v=Di-TQ80RSTY |
| 2023-12-08 | 2023-12-08T21:10Z | https://www.youtube.com/watch?v=Xhl5nDIPmMo |
| 2024-02-23 | 2024-02-23T22:06Z | https://www.youtube.com/watch?v=EnfKii4oa2o |
| 2024-03-22 | 2024-03-22T21:08Z | https://www.youtube.com/watch?v=ZtAM4ekhJVc |
| 2024-04-26 | 2024-04-26T21:08Z | https://www.youtube.com/watch?v=PnC4bYe-w00 |
| 2024-08-30 | 2024-08-30T21:10Z | https://www.youtube.com/watch?v=MvJ501CAxCQ |
| 2024-10-11 | 2024-10-11T21:10Z | https://www.youtube.com/watch?v=kcDkqtrvFIs |
| 2024-11-15 | 2024-11-15T22:05Z | https://www.youtube.com/watch?v=57xbmjtRIEg |
| 2024-12-20 (during AmFest 2024) | not given | https://www.youtube.com/watch?v=KHz0pO0COUw |
| 2025-01-24 | 2025-01-24T22:04Z | https://www.youtube.com/watch?v=EaUTRcvHnmo |
| 2025-02-21 | 2025-02-21T22:06Z | https://www.youtube.com/watch?v=zGjx0-Zfzeg |
| 2025-04-04 | 2025-04-04T21:09Z | https://www.youtube.com/watch?v=d2hjvRwzN0s |
| 2025-04-25 | 2025-04-25T21:19Z | https://www.youtube.com/watch?v=xAcaYbfIcnM |
| 2025-05-30 | 2025-05-30T21:27Z | https://www.youtube.com/watch?v=1ssROkAorh0 |
| 2025-06-20 | 2025-06-20T21:14Z | https://www.youtube.com/watch?v=6UgLDY-dpQU |
| 2025-07-14 ("Lifestyle Q&A", recorded, not live) | not given | https://www.youtube.com/watch?v=5-eezW5IQco |
| 2025-08-22 | 2025-08-22T21:08Z | https://www.youtube.com/watch?v=DGE46Qc8Oxs |

Also: on 2023-01-20 a Q&A description says Charlie Kirk "share[d] ... some encouraging words", but it does not name Erika as on the stream (https://www.youtube.com/watch?v=sQm3jLVzbtY).

## Refinement of an existing row (not repeated in the CSV)
- **BLOOM 2025:** the event page at https://www.calvarywomen.net/events/2025/3/21/bloom-spring-conference gives the times: "Friday, March 21, 2025 6:30 PM – Saturday, March 22, 2025 4:30 PM, Calvary South OC 1311 Calle Batido San Clemente, CA ... featuring Erika Kirk!"
- **Signal Hill "Summer in the Psalms":** the event date is still not found. The YouTube copy on her channel (LnZm7DbcDoI) was uploaded 2025-07-21, later than the 2025-07-16 podcast date, so it does not narrow the date. "Summer in the Psalms" is also the name of Kaddis's recurring women's summer Bible series (2021/2022 streams), so the talk may have been one session of that series.

## Searches run
- **Midweek Rise Up RSS** (re-scanned all 2023-2025 descriptions for place words): no new location beyond the known episodes (YWLS 2023, Nov 2023 RISE UP tea, AmFest 2024, Calvary OC, YWLS 2025, Signal Hill).
- **Charlie Kirk Show RSS** (Omny, 4,415 episodes; grep Erika / "my wife", 2023 – Sep 2025):
  - 2023-09-24 "Tough Love": no location.
  - 2024-12-25 AmFest speech: already known.
  - 2025-04-14 "Ask Charlie Anything 219": no location.
  - 2025-06-29 "Charlie and Erika share the stage at YWLS": already known (YWLS 2025).
- **Instagram:**
  - Her handle is @mrserikakirk, not @erikakirk.
  - Wayback CDX for instagram.com/mrserikakirk/ (2023-2025): every capture is a 302 to the login page, so there are no captions.
  - Wayback has nothing for the picuki, imginn, pixwox, dumpor, greatfon or gramhir mirrors, or for the @proclaimstreetwear / @biblein365 profiles.
  - site:instagram.com web searches only returned fan reels from after Sep 2025.
  - A search summary claimed "Erika posted an Instagram photo ... White House in February 2025". No source could be found, so it was not used.
- **mrserikakirk.com** (Wayback, 2023-2025): the /events-page is empty. The homepage only has "BOOK ERIKA FOR SPEAKING", with no events listed.
- **PROCLAIM x BIBLEin365 YouTube channel:** full list of about 300 videos and 29 streams. The Q&As above are the only dated items.
- **YouTube keyword searches** (about 25 queries: women's conference, keynote, chapel, gala, Rise Up tea, AmFest 2023, SAS 2024, Chase the Vote, Signal Hill, Nights of Unity, Kaddis): results are swamped by post-Sep-2025 commentary, and nothing new came up for 2023 – Sep 2025.
- **Calvary Chapel Signal Hill:**
  - YouTube channel search: only Sunday sermons and prayer streams.
  - Wayback site pages (women's ministry, announcements, calendar): no conference or Erika mention.
  - ccsignalhill.churchcenter.com needs JavaScript.
- **calvarywomen.net:**
  - Sitemap and event pages for 2023-2025 (Set Free 2024, Refresh 2024/2025, Christmas dinners, Thrive): Erika appears only at Bloom 2025.
- **TPUSA event sites on Wayback:**
  - believerssummit.com 2024 (West Palm Beach, July 26-28): Erika is **not** on the speaker list.
  - believerssummit.com 2025: lists "Erika Kirk" among the speakers, but the event was "OKLAHOMA CITY, OK OCTOBER 15-17th", so it is **out of range**, and her attendance is not confirmed.
  - amfest2023.com, sas2025.com, ywls2023.com, ywls2025.com, pastorssummit.com, tpusafaith.com agenda: no Erika hits.
- **Getty** (captions for "erika kirk", "charlie kirk erika", "charlie kirk wife"; 15 pages each, oldest first): the only in-window hits are the Inaugural-Eve Ball on 2025-01-19, which is already known.
- **Wikimedia Commons** (Category:Erika Kirk in 2023/2024/2025): all Gage Skidmore photos, already covered. **Flickr re-check:** the prior API dumps have extra Feb 2025 and Jul 2025 hits, but these are false positives for "Erika Donalds" (CPAC 2025, SAS 2025 Tampa).
- **Web searches (WebSearch + DuckDuckGo HTML):**
  - Women's conference, pregnancy-center gala, Republican women dinner, university chapel, luncheon, pageant judge/alumni, Proclaim pop-up, Everyday Heroes Like You, TPUSA Faith RISE UP tea (Eileen Marx / Stephanie Denham / Rachel Jensen), Nights of Unity, Godspeak Calvary Chapel, Dream City Church Dream Conference 2024, Believers Summit, Student Action Summit 2025, Madison Square Garden / Butler / election night 2024, inauguration day, Japan/Korea Sept 2025 trip, White House / Mar-a-Lago 2025, "joined by his wife Erika", TBN / Fox Nation / guest podcasts, X (@MrsErikaKirk, @charliekirk11).
  - Nearly every result is from after Sep 2025 (WLS 2026, Make Heaven Crowded tour 2026, Hillsdale 2026), so all are out of range.

## Dead ends / out of range
- **Calvary Women "Good Things Conference"** with Erika Kirk (calvarywomen.net/titus-2-talk-erika-kirk): **Saturday, August 21, 2021**, Calvary Chapel, 31612 El Camino Real, San Juan Capistrano. This is before the window.
- **Believers Summit 2025**, Oklahoma City, Oct 15-17 2025: after the window, and her attendance is not verified.
- **Charlie Kirk's Asia trip** (South Korea Sep 5-6, Japan Sep 7 2025): no source says Erika went.
- **Nights of Unity 3 Mar 2023:** nightsofunity.org returns a Wix "ConnectYourDomain" error. The ministry's online-event page suggests the event was streamed, and the city is still unknown.
- **TPUSA Faith RISE UP tea (Nov 2023):** no event page or city found.
- **Blocked:**
  - religionnews.com (Cloudflare 403) and Rolling Stone (tollbit redirect). Both are profiles that might list earlier events.
  - Shutterstock editorial (403), Rumble search (Cloudflare challenge).
  - DuckDuckGo started rate-limiting after about 3 queries.
  - web.archive.org was intermittently "Temporarily Offline".
- **Not chased:** Alamy and Shutterstock pre-2025 editorial captions (blocked). Facebook event pages (need login).
