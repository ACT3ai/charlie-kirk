---
unlisted: true
title: "Week 08 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W08"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-02-19 to 2025-02-25."
status: completed
hide_table_of_contents: true
---

# Week 08, 2025

- Date range: 2025-02-19 to 2025-02-25
- Queried at (UTC): 2026-08-24T19:17:26Z
- Model: grok-4.3
- API status: completed
- Response id: e3fa958d-cc77-9656-b9c8-e94d20c0e32e

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-02-19 to the end of the week 2025-02-25.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR tour OR appearance OR \"will be\" OR speaking OR campus OR university OR college) since:2025-02-19 until:2025-02-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR tour OR appearance OR campus OR university) since:2025-02-19 until:2025-02-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR tour OR appearance OR campus OR university) since:2025-02-19 until:2025-02-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, appearances, or where Charlie will speak between February 19-25 2025",
      "limit": "10",
      "from_date": "2025-02-19",
      "to_date": "2025-02-26"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"American Comeback Tour\" OR \"theturningpointtour\") (event OR tour OR speaking OR speak OR appearance OR campus OR \"will speak\" OR \"speaking at\" OR university OR college) since:2025-02-19 until:2025-02-26 -from:charliekirk11 -from:TPUSA",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"American Comeback Tour\" OR \"Turning Point Tour\" OR \"TPUSA tour\") since:2025-02-19 until:2025-02-26",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Hillsdale OR \"South Florida\" OR USF OR \"University of South Florida\") since:2025-02-19 until:2025-02-26",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1892627408064544781"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 21365,
  "input_tokens_details": {
    "cached_tokens": 10496
  },
  "output_tokens": 3646,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 25011,
  "num_sources_used": 0,
  "num_server_side_tools_used": 8,
  "cost_in_usd_ticks": 648004500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 8,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 12334,
    "output_tokens": 3184
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894169452326891577",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894169452326891577"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894158063625802084",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894158063625802084"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894161396599763251",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894161396599763251"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894132033770631237",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894132033770631237"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893055294105591979",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893055294105591979"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894134414646345773",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894134414646345773"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892627408064544781",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892627408064544781"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892645369609388460",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892645369609388460"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892620132146676161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892620132146676161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894144433345409200",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894144433345409200"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894137918492393672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894137918492393672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892985212897796582",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892985212897796582"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893044494397784546",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893044494397784546"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894142802553876503",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894142802553876503"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893181426578665792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893181426578665792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892670449894531242",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892670449894531242"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894152247572901968",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894152247572901968"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894133551953494366",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894133551953494366"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894170257050247561",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894170257050247561"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892627590785228963",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892627590785228963"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893435207220343285",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893435207220343285"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893088491560468990",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893088491560468990"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892647539884838937",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892647539884838937"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1893703531548319948",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1893703531548319948"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894173512115339764",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894173512115339764"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892675363727188456",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892675363727188456"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894144287119405350",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894144287119405350"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1894132797876363697",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1894132797876363697"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1892606394286698698",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1892606394286698698"
  }
]
```

## Grok response

```text
**Here is all the relevant X/Twitter data** from the specified date range (posts from 2025-02-19 to 2025-02-25, with searches extending slightly into 02-26 for complete coverage) matching queries about Charlie Kirk, TPUSA, or Turning Point USA public speaking events, tours, appearances, or locations where Charlie will speak. I included **every matching post** without summarization, using the exact content, timestamps, authors, engagement, and context from the tool results. No posts were omitted.

### Direct posts from Charlie Kirk (@charliekirk11) mentioning events/tours/speaking:
- **[post:9]** ID: 1892645369609388460  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 20 Feb 2025 18:39:54 GMT  
  **Engagement:** Likes=1187, Reposts=138, Quotes=5, Replies=50, Bookmarks=35, Views=205929  
  **Content:** It’s one of my great honors to learn from, support, and speak at the invitation of @DrLarryArnn and Hillsdale College, the best college in the country. May God continue to bless their mission and multiply their efforts. We need more students educated in the mode of Hillsdale.  
  *(Quoted post context: Praise from Larry Arnn about attacks on government involving Trump, Musk, Kirk.)*

- **[post:10 / post:14 / post:38]** ID: 1892627408064544781  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 20 Feb 2025 17:28:32 GMT  
  **Engagement:** Likes=3327, Reposts=397, Quotes=23, Replies=151, Bookmarks=46, Views=140082  
  **Content:** FIRST TOUR STOP OF THE YEAR AT THE UNIVERSITY OF SOUTH FLORIDA 🇺🇸  
  The energy is already INCREDIBLE. These kids are excited and ready for the next 4 years!!  
  Come to our next tour stop: https://theturningpointtour.com/  
  *(Includes 4 video attachments of the event/crowd.)*  
  **Thread replies (included for full context):**  
  - @akafaceUS (Thu, 20 Feb 2025 17:30:11 GMT): Keep up the good work Charlie! (Likes=36)  
  - @Bubblebathgirl (Thu, 20 Feb 2025 17:35:11 GMT): Enjoy these tours. I can’t imagine how great the energy is now following Trump’s victory. (Likes=17)  
  - @SmashingReality (Thu, 20 Feb 2025 17:31:24 GMT): Charlie, I hope you take pride in the fact that you have educated more college students than all the US college professors combined. It’s a beautiful thing to see! (Likes=12)

- **[post:16]** ID: 1892620132146676161  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 20 Feb 2025 16:59:37 GMT  
  **Engagement:** Likes=1415, Reposts=239, Quotes=4, Replies=99, Bookmarks=36, Views=434651  
  **Content:** Principles Last + Defy, Defund + Restoring Real Justice | Hutchins, Libby, Mehan | 2.20.2025 https://twitter.com/i/broadcasts/1OdJrDrBmjnKX  
  *(Broadcast link, tied to the tour/event day context.)*

- **[post:21]** ID: 1893703531548319948  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Sun, 23 Feb 2025 16:44:39 GMT  
  **Engagement:** Likes=1140, Reposts=101, Quotes=8, Replies=109, Bookmarks=17, Views=158357  
  **Content:** I’ll be joining @kilmeade tonight at 10pm ET on @OneNationFNC  
  Don’t miss it.  
  *(Media: 1 photo attachment.)*

### Direct posts from TPUSA (@TPUSA) mentioning events/tours/speaking:
- **[post:12]** ID: 1892647539884838937  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 20 Feb 2025 18:48:31 GMT  
  **Engagement:** Likes=187, Reposts=16, Quotes=1, Replies=7, Bookmarks=3, Views=9712  
  **Content:** The University of South Florida SHOWED UP for @charliekirk11  
  *(Media: 1 video attachment of the crowd.)*

- **[post:13]** ID: 1892627590785228963  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 20 Feb 2025 17:29:15 GMT  
  **Engagement:** Likes=544, Reposts=100, Quotes=9, Replies=39, Bookmarks=6, Views=49858  
  **Content:** CURRENT SCENE at the first stop of The American Comeback Tour with @charliekirk11 at the University of South Florida! 🇺🇸🔥@tpusastudents  
  🎥: @morgonn  
  *(Media: 1 video attachment.)*

### Other relevant posts mentioning Charlie Kirk/TPUSA events, tours, or speaking in the date range:
- **[post:0]** ID: 1894173512115339764  
  **Author:** We Are Charlie Kirk - @Viscalvish  
  **Timestamp:** Mon, 24 Feb 2025 23:52:11 GMT  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=164  
  **Content:** Elon, I really love Grok and I will be using it a lot, but I think the price of 50 bucks at month will hurt a lot of people, it should be 25 or 30  
  *(Conversation context unrelated to events.)*

- **[post:1]** ID: 1894170257050247561  
  **Author:** Ruchi🇨🇦 - @Ruchi68459542  
  **Timestamp:** Mon, 24 Feb 2025 23:39:15 GMT  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=6  
  **Content:** Now, we have the target audience group. Wish we could call them at a place n ask them questions. I think 200 conservatives would be enough to handle them all n atlest convert 50% of them. Just like Charlie kirk did campus QnAs!!

- **[post:2]** ID: 1894169452326891577  
  **Author:** We Are Charlie 🇺🇸 - @CharlieKirkUS  
  **Timestamp:** Mon, 24 Feb 2025 23:36:04 GMT  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=694  
  **Content:** Great announcement event!  
  Vivek for Ohio and 🇺🇸

- **[post:3]** ID: 1894161396599763251  
  **Author:** KoNo - @realoHNoKoNo  
  **Timestamp:** Mon, 24 Feb 2025 23:04:03 GMT  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=94  
  **Content:** these tiktok people are literally retarded, there is a good reason why this fat fk got his ass beat outside tpusa event  
  *(Quoted: Jay Dyer debate video.)*

- **[post:4]** ID: 1894152247572901968  
  **Author:** Randy Farnsworth - @randy77866  
  **Timestamp:** Mon, 24 Feb 2025 22:27:42 GMT  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=20  
  **Content:** I remember when the crowds were all hating on Kirk.. Of all Conservatives, Charlie Kirk has done it the hard way on college, one debate at a time. Huge respect 👍💪

- **[post:6]** ID: 1894144287119405350  
  **Author:** Momma Chandy - @MommaChandy  
  **Timestamp:** Mon, 24 Feb 2025 21:56:04 GMT  
  **Engagement:** Likes=22, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=7759  
  **Content:** “You are the reason we should eliminate the Department of Education!” Can’t wait to see Charlie Kirk on campus this week. Already have my ticket!  
  *(Quoted context about disclosure committee.)*

- **[post:7]** ID: 1894142802553876503  
  **Author:** AirCondaTv (I am Charlie Kirk) 🇺🇸 - @AircondaTvT  
  **Timestamp:** Mon, 24 Feb 2025 21:50:10 GMT  
  **Engagement:** Likes=6, Reposts=2, Quotes=0, Replies=1, Bookmarks=0, Views=172  
  **Content:** Time for some edit & chill on @rumblevideo where I will be editing a new music video that will announce the date of my Fishing Tournament as well as Ep. 4 of Project Orion.  
  *(Media: 1 photo; stream link mentioned.)*

- **[post:32]** ID: 1893088491560468990  
  **Author:** Tallahassee Democrat - @TDOnline  
  **Timestamp:** Sat, 22 Feb 2025 00:00:42 GMT  
  **Engagement:** Likes=4, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=1304  
  **Content:** MAGA star Charlie Kirk is bringing his "American Comeback Tour" to the campus of Florida State University on Friday, Feb. 28. https://www.tallahassee.com/story/news/local/2025/02/21/conservative-icon-charlie-kirk-of-turning-point-usa-coming-to-fsu/79330709007/?taid=67b913aad9c4900001f16967&utm_campaign=trueanthem&utm_medium=social&utm_source=twitter

- **[post:33]** ID: 1893055294105591979  
  **Author:** Emily Bird McCutchan - @embirdmccutchan  
  **Timestamp:** Fri, 21 Feb 2025 21:48:48 GMT  
  **Engagement:** Likes=20, Reposts=12, Quotes=0, Replies=1, Bookmarks=0, Views=753  
  **Content:** HUGE Kickoff for The American Comeback Tour at the University of South Florida!! I am incredibly proud of our students and staff who work diligently to make every event a success. Let’s do it again next week!😉🇺🇸  
  *(Media: 4 photos of the event.)*

- **[post:34]** ID: 1893044494397784546  
  **Author:** Lutz Activism Hub - @TPUSAatLutz  
  **Timestamp:** Fri, 21 Feb 2025 21:05:53 GMT  
  **Engagement:** Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=32  
  **Content:** America is back!📈The American Comeback Tour with @charliekirk11 at USF was amazing! 🇺🇸  
  *(Media: 1 photo.)*

- **[post:35]** ID: 1892985212897796582  
  **Author:** Craig Anderson - @craigandersonj  
  **Timestamp:** Fri, 21 Feb 2025 17:10:19 GMT  
  **Engagement:** Likes=1, Reposts=1, Quotes=0, Replies=1, Bookmarks=1, Views=180  
  **Content:** Criminal Mischief? This individual was filmed allegedly tearing down TPUSA posters for the @charliekirk11 American Comeback Tour at the University of Florida in Gainesville, FL. The club is offering $10 & a MAGA hat to the first person to come forward with the woman's name.  
  *(Media: 1 video.)*

- **[post:36]** ID: 1892675363727188456  
  **Author:** Terrence O’Sullivan - @TerrenceOSulli4  
  **Timestamp:** Thu, 20 Feb 2025 20:39:05 GMT  
  **Engagement:** Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=612  
  **Content:** American Comeback Tour. 🇺🇸  
  ****Sooo I just rtn’d from the University of South Florida (USF) campus….Charlie Kirk tour…despite the leftist and out-of-touch faculty, an awesome gathering of gen-z students…..what a spirited atmosphere ….I am hopeful 🙏🇺🇸  
  *(Media: 4 photos + 1 video.)*

- **[post:37]** ID: 1892670449894531242  
  **Author:** Valerie Mecklenburg🇺🇸❤🇺🇸 - @valiej79  
  **Timestamp:** Thu, 20 Feb 2025 20:19:34 GMT  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=214  
  **Content:** Charlie kirk & Kaitlin Bennett at USF today.. Cool listen up libiots

### Additional context from searches:
- Multiple mentions tie the USF event (Feb 20, 2025) explicitly to the **"American Comeback Tour"** / **"The Turning Point Tour"** (first stop of the year), with a link to https://theturningpointtour.com/ for future stops.
- One post references a planned **FSU (Florida State University) stop on Friday, Feb 28** (outside the exact week but announced in-range).
- No other specific upcoming dates/locations for Charlie Kirk speaking events were posted in the exact 02-19 to 02-25 window beyond the USF event, the tour promotion, and the Hillsdale speaking reference (past/general).
- Semantic search yielded overlapping results with the above (e.g., USF tour posts).

All data extracted directly from tool results. No external assumptions added.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-02-19 to 2025-02-25**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event** — the **5** most significant of **7** this page touches, foreign-fleet and same-day first, then most recent. The full set is on [the contacts index](/Planes/Incidents/overview) and on each aircraft's own page.

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2025-02-19](/Planes/Incidents/N560TW-2025-02-19-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2025-02-19](/Planes/Incidents/N582MM-2025-02-19-KPHX) | [N582MM](/Planes/N582MM/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day after |
| [2025-02-20](/Planes/Incidents/N582MM-2025-02-20-KTPA) | [N582MM](/Planes/N582MM/overview) | [KTPA](/Planes/Airports/KTPA) | Tampa, FL | Charlie | **Same day** |
| [2025-02-20](/Planes/Incidents/N582MM-2025-02-20-KSDL) | [N582MM](/Planes/N582MM/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2025-02-21](/Planes/Incidents/N582MM-2025-02-21-KLAL) | [N582MM](/Planes/N582MM/overview) | [KLAL](/Planes/Airports/KLAL) | Lakeland, FL | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
