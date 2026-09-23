# Erika Kirk public appearances 2022-2025: research notes

Output: `/tmp/erika_events/erika_events_raw.csv` (41 rows: 2022=0, 2023=5, 2024=6, 2025=30).
No row uses overlaps.csv or Candace Owens material. Scratch files (YouTube/Flickr/Getty dumps, podcast RSS) are in `/tmp/erika_events/work/`.

## Sources that worked best
- **Gage Skidmore Flickr** (photographs almost every TPUSA event). Queried the Flickr API (`flickr.photos.search`, text "Erika Kirk" / "Erika Frantzve" / user gageskidmore + "Erika", 2022-01-01..2025-12-31). The date comes from the photo's "date taken" field, and the caption names the venue and city. This is the strongest source type for dates.
- **White House Flickr** (whitehouse): 2025-09-21 and 2025-10-14.
- **Getty Images editorial captions** (scraped with curl): the Inaugural-Eve Ball, Air Force Two on 9/11, TPUSA HQ on 9/12, Patriot Awards, Oval Office, DealBook, Hannity, AmFest 2025.
- **Midweek Rise Up podcast RSS** (`https://anchor.fm/s/d2a6450/podcast/rss`, 110 episodes). Episodes "recorded live" at YWLS 2023, Bloom 2025, Calvary OC Q&A, YWLS 2025, Calvary Chapel Signal Hill, the AmFest 2024 sit-down, and the TPUSA Faith "RISE UP" tea in Nov 2023.
- **YouTube metadata** (publishDate + description via curl; yt-dlp searches): about 350 candidate videos checked.

## Searches run (web search unless noted)
- "Erika Kirk" + Young Women's Leadership Summit 2022 / 2023 / 2024 / 2025; YWLS 2022/2023/2024 dates and venue
- "Erika Kirk" + AmericaFest / AmFest 2022, 2023, 2024, 2025; "Charlie and Erika Kirk" 2024 event; AmFest 2024 closing remarks
- "Erika Kirk" + Student Action Summit (2023, 2024, 2025 Tampa); RNC 2024 Milwaukee; election night 2024 / Mar-a-Lago
- "Erika Kirk" + Pastors Summit / Faith Forward / Turning Point Faith; church conference 2022; Calvary Chapel (OC, Signal Hill, Chino Hills)
- Bloom Conference 2025; Calvary OC Q&A; "Summer in the Psalms" Signal Hill; TPUSA Faith "Rise Up" tea 2023; Nights of Unity 2023
- Inaugural-Eve Ball 2025; Oval Office / White House / Mar-a-Lago 2025; Medal of Freedom 10/14/25
- Air Force Two 9/11/25; first address 9/12/25; Hannity / Watters / Megyn Kelly / CBS town hall / DealBook / Fox book-tour week (Dec 8-11)
- Patriot Awards 11/6/25; Ole Miss 10/29/25; Mar-a-Lago gala Dec 2025 (archived gala.tpusa.com)
- "Erika Kirk" Israel / Jerusalem; "private jet" / "plane" / "flew"; how she traveled to Utah on 9/10
- site:tpusa.com "Erika Kirk"; mrserikakirk.com (ministry/home pages); Wikipedia Erika Kirk / AmericaFest; Wikimedia Commons category
- YouTube: channel @mrserikakirk (13 videos), TPUSA Faith channel search "Erika", James Kaddis channel, RSBN, many keyword searches
- Wayback CDX: ywls2022-2025.com, sas20xx.com, amfest*.com, gala.tpusa.com (the archive was intermittently offline)

## Dead ends / negative findings (absence is not proof)
- **2022: no public appearance found.** Her daughter was born 2022-08-23, and she said the pregnancy was kept "extremely private" (podcast episode 2022-08-31). Gage Skidmore has no 2022 photos of her. AmFest 2022 (Dec 17-20, Phoenix) produced no Erika source.
- **YWLS 2024** (San Antonio, June 7-9, 2024): the archived speaker list (ywls2024.com, 2024-06-08 snapshot) does **not** include Erika. Her son was born 2024-05-14.
- **SAS 2022-2025, AmFest 2023:** no source places her there. Gage Skidmore's Erika photos exist only for YWLS 2023, AmFest 2024, the Biggs rally, YWLS 2025, the 9/21 memorial, Ole Miss, and AmFest 2025.
- **RNC 2024, election night 2024:** nothing found.
- **Christian Media Summit, Jerusalem (Nov 2-6, 2025):** Times of Israel said she would accept an award. KFOX/TPUSA (Andrew Kolvet): "Erika will not be attending". Not a row.
- **Faith Forward Pastors' Summit at Fellowship Church, Grapevine, TX** is 2026-04-22 (Christian Post). The Santa Barbara Pastors Summit is Aug 2026. Both are out of range.
- **Charlie Kirk Show 9/26/25:** the studio city is not stated (row kept, city blank).
- **Mar-a-Lago gala:** the exact date is unconfirmed. Press says "this past weekend" (articles dated Dec 12-13). The archived TPUSA gala page (2025-12-09 snapshot) says "RSVP for December 7th". Row marked MONTH, Dec 6-7.
- **Calvary Chapel Signal Hill "Summer in the Psalms":** the event date was never found. The row uses the podcast publish date (PUBLISH_PROXY 2025-07-16).
- **Nights of Unity 3 Mar 2023:** the ministry is based in Eagle, ID, but the video description does not give a venue or city, or whether she appeared in person.
- **TPUSA Faith "RISE UP" tea (Nov 2023):** the city is unknown.
- **"Charlie & Erika Kirk: Family, Faith..." (YouTube 2025-04-13) and "Advice From The Kirk Family" (2025-02-28):** no location or date in the descriptions, so no row.
- **Blocked or unavailable pages:** Rolling Stone, Variety, Deadline, Hollywood Reporter (tollbit redirects); Snopes (402); factually.co (403); primetimer (403); Mississippi Today (403); theparisnews (429). The **Fox & Friends 12/9 NYC** row relies on a search-engine summary of an AP photo caption and should be re-checked.
- **Wikipedia (as summarized by the fetch tool)** said she was "present during" the assassination on 9/10. This contradicts her own NYT account and was not used.

## Overlap with tpusa_events.csv (for charlie_present marking)
- Already present in tpusa_events.csv as Charlie events (Erika there per these new sources): YWLS 2023 Grapevine (06-09..11), AmFest 2024 Phoenix (12-19..22), Inaugural-Eve Ball DC (2025-01-19), YWLS 2025 Grapevine (06-13..15), 9/21 memorial, Ole Miss 10/29.
- **Not in tpusa_events.csv:** Andy Biggs for Governor rally, Arizona Biltmore, Phoenix, **2025-05-31**. Gage Skidmore photographed Erika and Charlie together (photo 54570846701). This is a joint appearance to add.
- Sources explicitly put Charlie on stage with her at: YWLS 2025 opening night (06-13), the AmFest 2024 Faith Night marriage talk, the AmFest 2024 podcast sit-down, the Biggs rally, and the Inaugural-Eve Ball.

## Aircraft / flight mentions found (quoted, not chased)
1. **Air Force Two, 2025-09-11, Salt Lake City -> Phoenix Sky Harbor, with Erika aboard.**
   - Global News: "Air Force Two arrived in Phoenix from Salt Lake City ... Vance's wife, Usha, stepped off the plane with Kirk's widow, Erika" (https://globalnews.ca/news/11416576/jd-vance-escorts-charlie-kirk-casket-phoenix-air-force-two/).
   - CBS: "landing shortly before 5 p.m. local time", with the caption "Phoenix Sky Harbor International Airport on Sept. 11, 2025" (https://www.cbsnews.com/news/charlie-kirk-flown-air-force-two-arizona/).
   - Getty (Eric Thayer): "Vice President JD Vance (R) second lady Usha Vance (C) and Erika Kirk deplane Air Force Two while escorting the body of Charlie Kirk on September 11, 2025 in Phoenix, Arizona."
2. **"Her husband's chartered plane", 2025-09-10, Phoenix -> Provo.**
   - Yahoo News 2025-09-21, citing her NYT interview: "The mother of two was on her husband's chartered plane, headed to Provo, Utah, when she was told he had been pronounced dead at a nearby hospital." (https://www.yahoo.com/news/articles/erika-kirk-describes-moment-she-160659195.html)
   - IBTimes 2025-09-29: "She later boarded a chartered flight to Utah." (https://www.ibtimes.com/separating-fact-fiction-where-was-charlie-kirks-wife-during-shooting-3784748)
   - No tail number is given. Note the tension: the same account says Charlie had already flown to Utah that morning. The original NYT article URL was not retrieved.
3. **Ole Miss, 2025-10-29: not on Air Force Two.** Snopes 2025-11-04: a TPUSA spokesperson called the claim "100% false" and said "Erika flew separately". The White House pool report listed Vance, Usha Vance and two senators (https://www.snopes.com/news/2025/11/04/erika-kirk-air-force-2-ole-miss/). Getty shows Air Force Two going Joint Base Andrews -> Tupelo Regional Airport that day. Her own aircraft is not identified.
4. **Social-media claims of very short private-jet hops, not substantiated:**
   - "Erika Kirk's 3 Mile Flight?! #erikakirk #nickiminaj #privatejet #aviation": TikTok @nikalas.vr video 7589680792968777015 and YouTube Short MSh6s-l8CLY (uploaded 2025-12-30; hashtags suggest the AmFest week).
   - "Erika Kirk's NEW 2 Mile Flight?! #jdvance #privatejet": NewsBreak (https://www.newsbreak.com/memorable-218280143/4436006730887-erika-kirk-s-new-2-mile-flight-erikakirk-jdvance-privatejet-aviation-repost).
   - Video text was not retrievable, so no tail number was captured. factually.co fact-checks (403) reportedly say reporting does not support the claim.
5. **Not Erika's aircraft, noted for context:**
   - Erika said Charlie left AmFest 2024 "to get on Air Force One" with Trump (Deseret 2025-12-18).
   - Baron Coleman YouTube "TPUSA Plane Spotted at Ft Huachuca?" (ozwVk2OWyZk) is a TPUSA-plane claim, not tied to Erika in its title.
   - Niko House YouTube "Why Has Erika Kirk Been Surveilled by Egyptian Military For Years?" (WZ5CBgBpcYk) is a conspiracy claim, not examined.
   - A GitHub PR in ACT3ai/charlie-kirk (#6) came up in search; it is this project's own work, so it was ignored as a source.
