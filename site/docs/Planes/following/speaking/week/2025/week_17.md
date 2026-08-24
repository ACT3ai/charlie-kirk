---
unlisted: true
title: "Week 17 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W17"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-04-23 to 2025-04-29."
status: completed
hide_table_of_contents: true
---

# Week 17, 2025

- Date range: 2025-04-23 to 2025-04-29
- Queried at (UTC): 2026-08-24T19:18:14Z
- Model: grok-4.3
- API status: completed
- Response id: cc09739f-7b6d-913d-8da0-edd399340ed5

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-04-23 to the end of the week 2025-04-29.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR campus OR \"public speaking\" OR rally) since:2025-04-23 until:2025-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR \"will speak\" OR \"speaking at\" OR appearance) since:2025-04-23 until:2025-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak in late April 2025",
      "limit": "10",
      "from_date": "2025-04-23",
      "to_date": "2025-04-30"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA) (event OR speaking OR \"will speak\" OR \"speaking at\" OR appearance OR campus OR \"on campus\" OR tour OR \"will be\") (since:2025-04-23 until:2025-04-30)",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Wyoming OR \"Texas A&M\" OR \"Texas AM\" OR Akron OR \"Slippery Rock\" OR \"University of\" OR LSU OR \"Baton Rouge\" OR \"Tiger Stadium\") since:2025-04-23 until:2025-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR campus OR tour OR appearance OR Wyoming OR \"Texas A&M\") since:2025-04-23 until:2025-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR campus OR tour OR \"Charlie Kirk\") since:2025-04-23 until:2025-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 25610,
  "input_tokens_details": {
    "cached_tokens": 11264
  },
  "output_tokens": 4245,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 29855,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 657978000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 7,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 15785,
    "output_tokens": 3784
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917003166329278962",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917003166329278962"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915584426932879402",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915584426932879402"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915567434364579913",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915567434364579913"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916995693597598015",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916995693597598015"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916993896787173493",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916993896787173493"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915237239321485798",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915237239321485798"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916888412168097811",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916888412168097811"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916934621746303404",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916934621746303404"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915925790300246085",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915925790300246085"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916930790119866813",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916930790119866813"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915460227778175154",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915460227778175154"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916996382956618067",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916996382956618067"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915562874606674310",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915562874606674310"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916968728081666431",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916968728081666431"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915559711925231644",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915559711925231644"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1914836961619018119",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1914836961619018119"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915976561565602137",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915976561565602137"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916911124680761752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916911124680761752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915077026425270771",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915077026425270771"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915959886057296336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915959886057296336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916979019251134945",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916979019251134945"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917003328732729431",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917003328732729431"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916603407122747431",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916603407122747431"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916985675678724513",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916985675678724513"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915932196348535051",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915932196348535051"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916899336501268906",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916899336501268906"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915501499565670601",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915501499565670601"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915973010781311112",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915973010781311112"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915628369192116691",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915628369192116691"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915418576074293664",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915418576074293664"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917004166800527442",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917004166800527442"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917002760156741861",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917002760156741861"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916969502069428439",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916969502069428439"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916987388041035880",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916987388041035880"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916990098580648185",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916990098580648185"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915799080564932867",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915799080564932867"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916977148327563343",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916977148327563343"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916996038885331116",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916996038885331116"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916920071068205541",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916920071068205541"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915153451807629719",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915153451807629719"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915040658668015893",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915040658668015893"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916333553622700404",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916333553622700404"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915452280230514720",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915452280230514720"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1916938857783919020",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1916938857783919020"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1915136082443984966",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1915136082443984966"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917004498305769549",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917004498305769549"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range April 23–29, 2025 (posts dated up to April 29, covering events in that week), mentioning Charlie Kirk or TPUSA public speaking events, appearances, campus visits, or where Charlie will speak. No summarization—raw post content, metadata, and media descriptions included where available. Only posts with direct relevance to events/appearances were retained from searches; irrelevant or off-topic posts (e.g., general commentary without event details) were excluded.**

### Posts about Texas A&M (American Comeback Tour event with Charlie Kirk, featuring Lara Trump; occurred ~April 23, 2025)
- **[post:20]** ID: 1915077026425270771  
  Author: @jnottah (Hatton, America is back)  
  Timestamp: Wed, 23 Apr 2025 16:15:18 GMT  
  Content: Charlie Kirk speaks to huge crowd at Texas A&M , the brainwashed leftist paid TROLLS were out in force, trashing this, they only want COMMIES speaking at universities 👎  
  Media: Video (duration: 19829 ms)  
  Engagement: Likes=268, Reposts=151, Quotes=2, Replies=11, Bookmarks=2, Views=8453

- **[post:21]** ID: 1915136082443984966  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Wed, 23 Apr 2025 20:09:58 GMT  
  Content: HUMAN EVENTS: Charlie Kirk's Texas A&M campus visit draws massive crowd as American youth veers right  
  https://humanevents.com/2025/04/23/charlie-kirks-texas-a-m-campus-visit-draws-massive-crowd-as-american-youth-veers-right?utm_campaign=64501  
  Engagement: Likes=2377, Reposts=196, Quotes=5, Replies=93, Bookmarks=15, Views=105009

- **[post:23]** ID: 1915418576074293664  
  Author: @iAnonPatriot (American AF 🇺🇸)  
  Timestamp: Thu, 24 Apr 2025 14:52:29 GMT  
  Content: Charlie Kirk and Lara Trump TOOK OVER College Station, Texas.. 🔥🔥🔥  
  Media: Video (duration: 28900 ms)  
  Engagement: Likes=28894, Reposts=3821, Quotes=58, Replies=244, Bookmarks=375, Views=246528

- **[post:24]** ID: 1915153451807629719  
  Author: @ImMeme0 (I Meme Therefore I Am 🇺🇸)  
  Timestamp: Wed, 23 Apr 2025 21:18:59 GMT  
  Content: Spot the difference… These two gatherings happened at the Texas A&M campus at the same time. Charlie Kirk "American Comeback Tour" vs. Dean Whither "Unfvck America Tour"  
  Media: Two videos (durations: 6833 ms and 9900 ms)  
  Engagement: Likes=1606, Reposts=280, Quotes=20, Replies=62, Bookmarks=61, Views=157914

- **[post:25]** ID: 1915040658668015893  
  Author: @patriottakes (PatriotTakes 🇺🇸)  
  Timestamp: Wed, 23 Apr 2025 13:50:47 GMT  
  Content: A packed auditorium at Texas A&M to see anti-MLK MAGA activist Charlie Kirk.  
  Media: Photo  
  Engagement: Likes=586, Reposts=83, Quotes=43, Replies=379, Bookmarks=33, Views=62733

- **[post:38]** ID: 1916603407122747431  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Sun, 27 Apr 2025 21:20:35 GMT  
  Content: When I started visiting college campuses, it was: universities very liberal, students very liberal. Now it's: universities very liberal, students not so much. Young people are waking up 🇺🇸🇺🇸 Thank you to @LaraLeaTrump for coming to Texas A&M and experiencing the American Comeback Tour for yourself.  
  Media: Video (duration: 647513 ms)  
  Engagement: Likes=19483, Reposts=2397, Quotes=57, Replies=544, Bookmarks=363, Views=1338505

- **[post:48]** ID: 1915973010781311112  
  Author: @RickyDoggin (A Man Of Memes)  
  Timestamp: Sat, 26 Apr 2025 03:35:37 GMT  
  Content: Charlie Kirk at Texas A&M!  
  Media: Video (duration: 34039 ms)  
  Engagement: Likes=468, Reposts=87, Quotes=1, Replies=14, Bookmarks=15, Views=6900

- **[post:49]** ID: 1915959886057296336  
  Author: @wirebendr (wirebendr6996)  
  Timestamp: Sat, 26 Apr 2025 02:43:28 GMT  
  Content: Crowds Of Students That Are Now MAGA ! Charlie Kirk Is Assuring Our Next Generation Is On The Right Track To Make America Great Again ! THIS RECENT CAMPUS EVENT WAS LARA TRUMP AND CHARLIE KIRK DRAWING 3000 STUDENTS AT I BELIEVE TEXAS A&M  
  Media: None listed  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=477

- **[post:55]** ID: 1914836961619018119  
  Author: @TPUSA (Turning Point USA)  
  Timestamp: Wed, 23 Apr 2025 00:21:22 GMT  
  Content: A full house and incredible energy tonight at Texas A&M for the American Comeback Tour with @charliekirk11  
  Media: Video (duration: 10460 ms)  
  Engagement: Likes=7618, Reposts=1149, Quotes=89, Replies=278, Bookmarks=239, Views=1016775

### Posts about University of Wyoming (Charlie Kirk event on ~April 25, 2025; first visit to Laramie; part of American Comeback Tour)
- **[post:19]** ID: 1915584426932879402  
  Author: @MAGAVoice (MAGA Voice)  
  Timestamp: Fri, 25 Apr 2025 01:51:31 GMT  
  Content: BREAKING 🚨 THOUSANDS Lined up for Charlie Kirk’s event tonight at the University of Wyoming Keep in mind. THIS IS NOT AN ELECTION YEAR Charlie is waking up GEN Z 🔥  
  Media: Video (duration: 7976 ms)  
  Engagement: Likes=7989, Reposts=1460, Quotes=32, Replies=239, Bookmarks=62, Views=178942

- **[post:27]** ID: 1915562874606674310  
  Author: @TPUSA (Turning Point USA)  
  Timestamp: Fri, 25 Apr 2025 00:25:53 GMT  
  Content: THOUSANDS lined up for tonight’s event with @charliekirk11 at the University of Wyoming 🔥 @tpusastudents  
  Media: Video (duration: 15233 ms)  
  Engagement: Likes=523, Reposts=50, Quotes=3, Replies=12, Bookmarks=0, Views=21125

- **[post:39]** ID: 1915567434364579913  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Fri, 25 Apr 2025 00:44:00 GMT  
  Content: UPDATE: Full house at the University of Wyoming!! 1,900 in this room. More in the overflow. 🇺🇸🇺🇸  
  Media: Photo  
  Engagement: Likes=16308, Reposts=1731, Quotes=16, Replies=308, Bookmarks=61, Views=411410  
  (Quotes an earlier post by same author)

- **[post:40]** ID: 1915559711925231644  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Fri, 25 Apr 2025 00:13:19 GMT  
  Content: Thousands of students lined up for hours ahead of our event tonight at the University of Wyoming, my first ever visit to Laramie 🔥🔥 Let's go, Wyoming!!  
  Media: Video (duration: 15233 ms)  
  Engagement: Likes=28650, Reposts=2461, Quotes=28, Replies=380, Bookmarks=110, Views=694345

- **[post:44]** ID: 1916899336501268906  
  Author: @WyoPulse (Wyoming Pulse)  
  Timestamp: Mon, 28 Apr 2025 16:56:30 GMT  
  Content: 🌤️ Good morning, Wyoming! Today’s headlines: Wild weather swings, backwards-driving truck, Charlie Kirk draws crowd at UW + giant orca food truck ⏰ Wyoming’s 60-secondish news roundup: https://t.co/HixQAofJEG Photo by: Gintare K. #Wyoming #Wyo #WY #ThatWy #ThatsWyo  
  Media: Photo  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=37

- **[post:47]** ID: 1915976561565602137  
  Author: @iglesias_gabby (Gabriela Iglesias🇺🇲)  
  Timestamp: Sat, 26 Apr 2025 03:49:44 GMT  
  Content: 🔥BREAKING - THOUSANDS Lined up for Charlie Kirk’s event tonight at the University of Wyoming Keep in mind. THIS IS NOT AN ELECTION YEAR Charlie is waking up GEN Z  
  Media: Video (duration: 8034 ms)  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=60

- **[post:50]** ID: 1915932196348535051  
  Author: @jfkawakeninQ (Jfk Awakening Q17)  
  Timestamp: Sat, 26 Apr 2025 00:53:26 GMT  
  Content: BREAKING 🚨 THOUSANDS Lined up for Charlie Kirk’s event tonight at the University of Wyoming Keep in mind. THIS IS NOT AN ELECTION YEAR Charlie is waking up GEN Z 🔥  
  Media: Video (duration: 7976 ms)  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=40

- **[post:52]** ID: 1915628369192116691  
  Author: @TPUSA (Turning Point USA)  
  Timestamp: Fri, 25 Apr 2025 04:46:08 GMT  
  Content: The University of Wyoming PACKED the house at tonight’s event 🔥  
  Media: Video (duration: 9800 ms)  
  Engagement: Likes=153, Reposts=7, Quotes=0, Replies=1, Bookmarks=3, Views=9493

### Posts about other TPUSA-related events/appearances (April 23–29, 2025 range)
- **[post:0]** ID: 1917004166800527442  
  Author: @ACI1776 (American Cornerstone Institute)  
  Timestamp: Mon, 28 Apr 2025 23:53:04 GMT  
  Content: 🚨 Baton Rouge! @RealBenCarson will be on campus with @TPUSA TOMORROW, April 25th at Tiger Stadium - South Stadium Club! Come see us at 7PM! Register for tickets here: https://t.co/VhmCyoSd1h  
  Media: Photo  
  Engagement: Likes=132, Reposts=18, Quotes=0, Replies=4, Bookmarks=2, Views=13759  
  *(Note: Refers to April 25 event with Ben Carson + TPUSA at LSU/Tiger Stadium; posted on April 28 referencing the prior week's event.)*

- **[post:2]** ID: 1916996038885331116  
  Author: @tpusa_sru (TPUSA_SRU)  
  Timestamp: Mon, 28 Apr 2025 23:20:46 GMT  
  Content: T-Minus 2 days until the panel!! Please remember there was a‼️ROOM CHANGE‼️ Our panel event is now in the Campus Success Center- Second Floor MPR Room!! Tickets still available!! Link in bio!!  
  Media: Photo  
  Engagement: Likes=7, Reposts=2, Quotes=0, Replies=1, Bookmarks=0, Views=382  
  *(Slippery Rock University TPUSA chapter panel event; room change noted, ~April 30 timing implied by post date.)*

- **[post:4]** ID: 1916990098580648185  
  Author: @FrankLaRose (Frank LaRose)  
  Timestamp: Mon, 28 Apr 2025 22:57:10 GMT  
  Content: Grateful for the opportunity to speak with the @TPUSA University of Akron chapter today about Ohio’s secure and accessible elections—And how they can get involved! 🇺🇸  
  Media: Two photos  
  Engagement: Likes=10, Reposts=2, Quotes=1, Replies=5, Bookmarks=0, Views=812  
  *(University of Akron TPUSA chapter event/speaking appearance on ~April 28.)*

- **[post:14]** ID: 1916934621746303404  
  Author: @WyoRINORocket (Wyo RINO Rocket)  
  Timestamp: Mon, 28 Apr 2025 19:16:43 GMT  
  Content: Can’t wait for the episode about your @tpusa_uwyo1776 event. Maybe you could convince them to allow Jackalopes in the building? We don’t have fleas. We promise!  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=43  
  *(References @tpusa_uwyo1776 event at University of Wyoming chapter.)*

- **[post:17]** ID: 1916911124680761752  
  Author: @madi_smith1 (Madi Smith)  
  Timestamp: Mon, 28 Apr 2025 17:43:21 GMT  
  Content: ‼️TONIGHT ‼️ Charlie Kirk is hosting the Secretary of the Treasury Scott Bessent in this @tpusastudents exclusive virtual event!! 🇺🇸 You won’t want to miss this 🫵 Sign up now: https://t.co/Xhth2ccXcp  
  Media: Photo  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=107  
  *(Virtual TPUSA Students event with Charlie Kirk hosting Scott Bessent on ~April 28.)*

- **[post:41]** ID: 1915460227778175154  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Thu, 24 Apr 2025 17:38:00 GMT  
  Content: 🚨BREAKING: One of our chapter leaders at West Chester University was just assaulted on campus in advance of an event featuring Chloe Cole. The individual ran up to him, spit on him, and then punched him multiple times in the face. He is alright, thank God. He is pressing charges. The assault was not caught on camera but campus PD running after him and then arresting him was. This is becoming a weekly occurrence. Pray for our TPUSA students. Reach out to them and encourage them. They are the frontlines and have so much courage.  
  Media: Three videos (durations: 4600 ms each) + one photo  
  Engagement: Likes=12457, Reposts=3233, Quotes=124, Replies=750, Bookmarks=208, Views=468433  
  *(Mentions upcoming TPUSA event with Chloe Cole at West Chester University; assault in advance.)*

- **[post:54]** ID: 1915452280230514720  
  Author: @TPUSA (Turning Point USA)  
  Timestamp: Thu, 24 Apr 2025 17:06:25 GMT  
  Content: A TPUSA chapter member at West Chester University—volunteering ahead of today’s @tpusastudents event with @chloecole—was assaulted on campus. The attacker ran up, spat in his face, and punched him repeatedly. He’s okay and is pressing charges. Though the assault itself wasn’t captured, the attacker is visible in the videos below. Credit: @huriataj  
  Media: Two videos (durations: 4600 ms each)  
  Engagement: Likes=1040, Reposts=285, Quotes=39, Replies=132, Bookmarks=25, Views=208223  
  *(Confirms TPUSA event with Chloe Cole at West Chester University on ~April 24.)*

**No other posts in the searched results directly announced or detailed additional Charlie Kirk or TPUSA public speaking events/appearances within the exact April 23–29, 2025 window beyond those listed. Virtual events and chapter-specific panels are included as they reference speaking/appearances.**
```

