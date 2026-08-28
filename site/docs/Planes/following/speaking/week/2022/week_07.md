---
unlisted: true
title: "Week 07 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W07"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-02-12 to 2022-02-18."
status: completed
hide_table_of_contents: true
---

# Week 07, 2022

- Date range: 2022-02-12 to 2022-02-18
- Queried at (UTC): 2026-08-24T18:59:16Z
- Model: grok-4.3
- API status: completed
- Response id: 58b7f920-82e3-9a86-a79c-b2a8ee3c5a5e

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-02-12 to the end of the week 2022-02-18.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speak OR speaking OR event OR tour OR appearance OR \"will be\" OR speaking OR campus OR rally) since:2022-02-12 until:2022-02-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speak OR speaking OR event OR tour OR appearance OR \"will be\" OR speaking OR campus OR rally) since:2022-02-12 until:2022-02-19 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, appearances, where he will speak or be between February 12 and 18 2022",
      "limit": "10",
      "from_date": "2022-02-12",
      "to_date": "2022-02-19"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (Chicago OR \"No Forced Masks\" OR rally OR speaking OR speak OR event) since:2022-02-12 until:2022-02-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR rally OR speak OR speaking OR Chicago OR tour OR appearance OR campus) since:2022-02-12 until:2022-02-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR rally OR speak OR speaking OR Chicago OR tour OR appearance OR campus) since:2022-02-12 until:2022-02-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk TPUSA events rallies speaking in Chicago or anywhere February 12-18 2022",
      "limit": "10",
      "from_date": "2022-02-12",
      "to_date": "2022-02-19"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"St. Charles\" (rally OR TPUSA OR \"No Forced Masks\" OR \"Charlie Kirk\") since:2022-02-12 until:2022-02-19",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"St. Charles\" (rally OR TPUSA OR \"No Forced Masks\" OR \"Charlie Kirk\") since:2022-02-12 until:2022-02-19 filter:links",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1492823365240836103"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 27353,
  "input_tokens_details": {
    "cached_tokens": 13376
  },
  "output_tokens": 2560,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 29913,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 765464500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 10,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 11875,
    "output_tokens": 1989
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493670747373330435",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493670747373330435"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494372605125664769",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494372605125664769"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494335967716524039",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494335967716524039"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493993666884501508",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493993666884501508"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493688012718411778",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493688012718411778"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492557797380149248",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492557797380149248"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492537193881030656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492537193881030656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493689594440732678",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493689594440732678"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494128204008722435",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494128204008722435"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492823365240836103",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492823365240836103"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494351319959756802",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494351319959756802"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493609329139802125",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493609329139802125"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494277968318849026",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494277968318849026"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494449137521152001",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494449137521152001"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494107451741782017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494107451741782017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494424252073734160",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494424252073734160"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494450174587912201",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494450174587912201"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494367554248314890",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494367554248314890"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493646791459311617",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493646791459311617"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494425684495720448",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494425684495720448"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492299993331363840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492299993331363840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1493475265757995011",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1493475265757995011"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494360096851251210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494360096851251210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494314694865260544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494314694865260544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492591440882548740",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492591440882548740"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494427598897696775",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494427598897696775"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1492634650673561607",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1492634650673561607"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494443765213372421",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494443765213372421"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494103257504907265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494103257504907265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1494352069486170124",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1494352069486170124"
  }
]
```

## Grok response

```text
**All relevant X posts found for Charlie Kirk / TPUSA public speaking events or appearances between February 12–18, 2022 (inclusive), are listed below in full, without summarization.** These are drawn from keyword and semantic searches targeting mentions of events, rallies, speaking, Chicago, St. Charles (IL), masks, TPUSA, etc., within the exact date range. No other posts matching the criteria were identified.

**Posts directly announcing or promoting the events:**

- **Post ID: 1492823365240836103**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Sun, 13 Feb 2022 11:30:00 GMT  
  Content: RALLY TO FREE THE KIDS! 🇺🇸🇺🇸🇺🇸  
  Join TPUSA and @CharlieKirk11 at the No Forced Masks Rally in St. Charles, Illinois, and make your voice heard in America's fight for freedom!  
  DON'T MISS IT!  
  SIGN UP 👉 https://t.co/uUUslpiSY2  
  (Media: Photo of promotional graphic)  
  Engagement: Likes=65, Reposts=26, Quotes=2, Replies=14, Bookmarks=1

- **Post ID: 1494107451741782017**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 17 Feb 2022 00:32:30 GMT  
  Content: The child abuse taking place in our schools has to end.  
  The @TPUSA ‘No Forced Masks Rally’ is happening in Chicago in half an hour.  
  Americans are sick of medical tyranny and the energy here is unparalleled. It’s time to make our voices heard.  
  https://t.co/GelwrcaEQi  
  (Media: Photo)  
  Engagement: Likes=537, Reposts=135, Quotes=3, Replies=111, Bookmarks=5

**Posts reporting the events (post-occurrence, referencing speaking/rallies by Charlie Kirk / TPUSA):**

- **Post ID: 1494128204008722435**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 17 Feb 2022 01:54:58 GMT  
  Content: LIVE! @CharlieKirk11 speaking at TPUSA's No Forced Masks rally!  
  👇👇👇  
  https://www.youtube.com/watch?v=VQ7C3f_E8qE  
  Engagement: Likes=175, Reposts=37, Quotes=0, Replies=9, Bookmarks=0

- **Post ID: 1494427598897696775**  
  Author: Terry Flatt (@TerryFlatt4)  
  Timestamp: Thu, 17 Feb 2022 21:44:39 GMT  
  Content: ‘Tyrants Be Warned:’ Charlie Kirk, Students Rally Against Chicago Mask Mandate  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1494425684495720448**  
  Author: P-E-Z (@pez1963)  
  Timestamp: Thu, 17 Feb 2022 21:37:02 GMT  
  Content: 'Tyrants Be Warned:' Charlie Kirk, Students Rally Against Forced Masks in Chicago  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1494424252073734160**  
  Author: New Right Network (@NewRightNetwork)  
  Timestamp: Thu, 17 Feb 2022 21:31:21 GMT  
  Content: ‘Tyrants Be Warned:’ Charlie Kirk, Students Rally Against Chicago Mask Mandate  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1494360096851251210**  
  Author: Trent (@tnertz)  
  Timestamp: Thu, 17 Feb 2022 17:16:25 GMT  
  Content: A lot of great people in attendance listening to many amazing leaders. If you missed @TPUSA’s #noforcedmask rally yesterday in St Charles, here’s the stream: https://t.co/be519L8g4m (@charliekirk11, @rlesliemendoza, @BlackAndRightAM, @Awake_IL, @WeAreFreedomIL, @AM560TheAnswer)  
  (Media: 3 photos)  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0

- **Post ID: 1494352069486170124**  
  Author: Trent (@tnertz)  
  Timestamp: Thu, 17 Feb 2022 16:44:31 GMT  
  Content: https://t.co/ch2WN5OHo1 huge applause for Devore in St Charles at yesterdays @TPUSA rally  
  (Media: Video)  
  Engagement: Likes=5, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1494372605125664769**  
  Author: Chris Hennessey (@chrishennessey)  
  Timestamp: Thu, 17 Feb 2022 18:06:07 GMT  
  Content: St. Charles, IL last night at a no forced masks event. It was scheduled quickly after a group refused to wear masks and leave a public library a few weeks back.  
  The leader of the group that argued with librarians is/was a youth pastor in the area. 😕  
  Engagement: Likes=1, Reposts=1, Quotes=0, Replies=1, Bookmarks=0

- **Post ID: 1494351319959756802**  
  Author: Colorado Conservative (@JawasDugg)  
  Timestamp: Thu, 17 Feb 2022 16:41:33 GMT  
  Content: He hinted at convening a grand jury against JB Pritzker last night at Charlie Kirk's event in St Charles. It'll be interesting to hear what the actual announcement is.  
  Engagement: Likes=9, Reposts=2, Quotes=0, Replies=1, Bookmarks=0

- **Post ID: 1494335967716524039**  
  Author: Mike Slodki (@mslodki645)  
  Timestamp: Thu, 17 Feb 2022 15:40:32 GMT  
  Content: The Charlie Kirk appearance at the Arcada Theater in St. Charles was an amazing night! The show started at 7, but Charlie’s forehead arrived at 6:30. He did a burlesque set by himself for a little bit and then drank his own urine for an hour! What a night.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1494277968318849026**  
  Author: Kane County Chronicle - Shaw Local (@kcchronicle)  
  Timestamp: Thu, 17 Feb 2022 11:50:04 GMT  
  Content: Conservative activist Charlie Kirk was at the Arcada Theatre in St. Charles Wednesday night for what he was promoting as a “no forced masks” rally.  
  Engagement: Likes=3, Reposts=1, Quotes=0, Replies=0, Bookmarks=0

**Thread/replies related to the St. Charles rally announcement (for completeness, as the parent post is included above):**

- **Post ID: 1492845941845598208** (reply to 1492823365240836103)  
  Author: CharliesSock (@KirksSock)  
  Timestamp: Sun, 13 Feb 2022 12:59:42 GMT  
  Content: How does Charlie and TP feel about girls high school coaches walking into locker rooms while they’re changing? Will that be a topic of discussion?  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1492824068294422528** (reply to 1492823365240836103)  
  Author: aGIFforEveryCharlie (@aGIFforCharlies)  
  Timestamp: Sun, 13 Feb 2022 11:32:47 GMT  
  Content: Gosh your graphics team  
  (Media: Video/GIF)  
  Engagement: Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0

- **Post ID: 1492893278886318084** (reply to 1492823365240836103)  
  Author: mormon school (@614_blu3)  
  Timestamp: Sun, 13 Feb 2022 16:07:48 GMT  
  Content: Boy this is a long 2 year temper tantrum you guys are throwing.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0

No additional posts from the searched date range (Feb 12–18, 2022) were found that reference other speaking events, tours, campus appearances, or future schedules for Charlie Kirk or TPUSA. All data is included verbatim.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-02-12 to 2022-02-18**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-02-12 to 2022-02-18 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
