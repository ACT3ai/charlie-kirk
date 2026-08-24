---
unlisted: true
title: "Week 09 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W09"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-02-26 to 2023-03-04."
status: completed
hide_table_of_contents: true
---

# Week 09, 2023

- Date range: 2023-02-26 to 2023-03-04
- Queried at (UTC): 2026-08-24T19:06:03Z
- Model: grok-4.3
- API status: completed
- Response id: 6f76b200-fff5-9abd-9302-79675b46e0a4

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-02-26 to the end of the week 2023-03-04.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR campus) since:2023-02-26 until:2023-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus OR TPUSA) since:2023-02-26 until:2023-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR campus) since:2023-02-26 until:2023-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between Feb 26 and March 4 2023",
      "limit": "10",
      "from_date": "2023-02-26",
      "to_date": "2023-03-05"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Charlie Kirk",
      "count": "3"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Turning Point USA",
      "count": "3"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 10157,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 3311,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 13468,
  "num_sources_used": 0,
  "num_server_side_tools_used": 6,
  "cost_in_usd_ticks": 477481500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 6,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 8567,
    "output_tokens": 3048
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1965983581798555648",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1965983581798555648"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631000002746273792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631000002746273792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630190183206514693",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630190183206514693"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630574611875221504",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630574611875221504"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/491719838",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/491719838"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631767747851071491",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631767747851071491"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631740950660743168",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631740950660743168"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631795582967611395",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631795582967611395"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631765974331572224",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631765974331572224"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630272948664664071",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630272948664664071"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630699414024069120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630699414024069120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631740081219473408",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631740081219473408"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1629667369810264065",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1629667369810264065"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631133473049300993",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631133473049300993"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630226057935634434",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630226057935634434"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630634475913637889",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630634475913637889"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630199630053998601",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630199630053998601"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631765975388553216",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631765975388553216"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631448260446650369",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631448260446650369"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631126897659899909",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631126897659899909"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1966575521493643265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1966575521493643265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631399784673341445",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631399784673341445"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631136839192154114",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631136839192154114"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630241780913573888",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630241780913573888"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631777146728484865",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631777146728484865"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/292929271",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/292929271"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631772577445330944",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631772577445330944"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1630699516369469440",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1630699516369469440"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/125695079",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/125695079"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1249078342718033923",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1249078342718033923"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1631763409984208897",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1631763409984208897"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (2023-02-26 to 2023-03-04, inclusive, based on the tool results using until:2023-03-05 for coverage) mentioning Charlie Kirk, TPUSA/Turning Point USA, or related public speaking events/appearances are included below in full (no summarization).** 

Posts were retrieved via keyword searches (general + from specific accounts) and semantic search. Only posts with direct relevance to events, speaking, tours, or appearances are highlighted in the results; irrelevant or tangential posts (e.g., general mentions without event context) are still listed if returned but noted as such. No posts from the exact range explicitly detail events strictly between Feb 26–Mar 4 beyond the UCSB event and references to prior/upcoming ones. The Live Free Tour is repeatedly referenced.

### From @charliekirk11 (Charlie Kirk's account):
- **Post ID: 1631448260446650369**  
  Timestamp: Fri, 03 Mar 2023 00:15:50 GMT  
  Content: TPUSA hosted an incredible event last night at UC Santa Barbara. Packed house, a free exchange of ideas, and the protesters remained mostly peaceful!  
  Next up is the @universityofky on March 8th!  
  Register at https://t.co/zsOBKIPxt6 🇺🇸🔥  
  (Media: 4 photos)  
  Engagement: Likes=492, Reposts=99, Quotes=4, Replies=44, Bookmarks=3, Views=57555  
  **Relevance**: Directly references a TPUSA/Charlie Kirk speaking event at UC Santa Barbara (held the night before, i.e., March 2, 2023) and announces an upcoming one at University of Kentucky on March 8.

### From @TPUSA (Turning Point USA official account):
- **Post ID: 1631399784673341445**  
  Timestamp: Thu, 02 Mar 2023 21:03:13 GMT  
  Content: Catch @charliekirk11 on The Live Free Tour at a stop near you ⬇️ @tpusastudents  
  http://tpusa.com/livefree  
  Engagement: Likes=15, Reposts=2, Quotes=0, Replies=1, Bookmarks=1, Views=6302  
  **Relevance**: Promotes The Live Free Tour featuring Charlie Kirk speaking at various stops.

- **Post ID: 1631136839192154114**  
  Timestamp: Thu, 02 Mar 2023 03:38:22 GMT  
  Content: "FASCISTS OFF CAMPUS," protestors chant as they demand the removal of opposing points of view from their campus.  
  (Media: 1 video)  
  Engagement: Likes=82, Reposts=21, Quotes=4, Replies=37, Bookmarks=1, Views=11890  
  **Relevance**: Context is protest at the UC Santa Barbara Live Free Tour event.

- **Post ID: 1631133473049300993**  
  Timestamp: Thu, 02 Mar 2023 03:24:59 GMT  
  Content: WATCH LIVE: TPUSA Presents The LIVE FREE Tour LIVE with @charliekirk11 at UC Santa Barbara  
  https://www.youtube.com/live/VJJzDzZwQXs?feature=share  
  Engagement: Likes=83, Reposts=25, Quotes=0, Replies=7, Bookmarks=1, Views=41345  
  **Relevance**: Live stream of Charlie Kirk/TPUSA speaking event at UC Santa Barbara (March 2, 2023).

- **Post ID: 1631126897659899909**  
  Timestamp: Thu, 02 Mar 2023 02:58:51 GMT  
  Content: HAPPENING NOW: UC Santa Barbara students protest @CharlieKirk11 before tonight's Live Free Tour event kicks off  
  (Media: 1 video)  
  Engagement: Likes=229, Reposts=55, Quotes=7, Replies=87, Bookmarks=4, Views=81791  
  **Relevance**: Describes protests ahead of Charlie Kirk's Live Free Tour speaking event at UC Santa Barbara (March 2, 2023).

- **Post ID: 1631000002746273792**  
  Timestamp: Wed, 01 Mar 2023 18:34:37 GMT  
  Content: Spotted near the @ucsantabarbara campus today ahead of @Charliekirk11's visit  
  (Media: 1 photo)  
  Engagement: Likes=90, Reposts=18, Quotes=13, Replies=80, Bookmarks=1, Views=134604  
  **Relevance**: Pre-event promotion for Charlie Kirk's visit/speaking at UC Santa Barbara.

- **Post ID: 1630699516369469440**  
  Timestamp: Tue, 28 Feb 2023 22:40:36 GMT  
  Content: Don't forget: The LIVE FREE TOUR kicks off tomorrow NIGHT at 7PM at UCSB @charliekirk11  
  Get tickets👇  
  http://tpusa.com/livefree  
  Engagement: Likes=25, Reposts=6, Quotes=0, Replies=1, Bookmarks=0, Views=6709  
  **Relevance**: Announces the start of The Live Free Tour with Charlie Kirk speaking at UCSB (UC Santa Barbara) on March 1, 2023 (7 PM).

### Other relevant posts from general keyword/semantic searches (mentions of events/appearances):
- **Post ID: 1631795582967611395** (Author: @semperfidem2004)  
  Timestamp: Fri, 03 Mar 2023 23:15:58 GMT  
  Content: I said from the first time I heard him speak "this man is an imbecile"  
  (Quoted post context unrelated to TPUSA/Charlie Kirk events)  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=182  
  **Relevance**: General mention of hearing "him" (likely Charlie Kirk) speak; no specific event details in range.

- **Post ID: 1631777146728484865** (Author: @KennaThordarson, @TPUSA College Strategic Specialist)  
  Timestamp: Fri, 03 Mar 2023 22:02:43 GMT  
  Content: Our @TPUSA Chapter at Grand Canyon University asked students on campus what the craziest thing is that they’ve been taught in school.  
  Start or join a Turning Point USA Chapter near you TODAY to combat leftist propaganda on campus!🔥  
  https://t.co/qTzHZso3gk  
  (Media: 1 video)  
  Engagement: Likes=12, Reposts=7, Quotes=0, Replies=0, Bookmarks=0, Views=702  
  **Relevance**: TPUSA campus chapter activity; no specific Charlie Kirk speaking event.

- **Post ID: 1631765975388553216** and **Post ID: 1631765974331572224** (Author: @Stanford_GOP, Stanford Turning Point USA)  
  Timestamp: Fri, 03 Mar 2023 21:18:19 GMT  
  Content (combined thread context): Were it not for SCR and @yaf, students could go their full four years without hearing conservative ideas. SCR is the undisputed Standard bearer of conservative ideas at @Stanford, and we will continue to fulfill our mandate to bring conservative ideas to campus. 3/  
  Leading up the event, leftists destroyed our flyers, but last night outside the auditorium, not a soul of resistance materialized. Yesterday, we achieved complete and total victory, the culmination of over six years of unflinching conservative advocacy. 2/  
  Engagement: Likes=12 each, Reposts=0, Quotes=0, Replies=1 (on second), Bookmarks=0, Views=257/305  
  **Relevance**: References a recent conservative event at Stanford (not directly Charlie Kirk/TPUSA national tour).

- **Post ID: 1629667369810264065** (Author: @SeeingRedNE)  
  Timestamp: Sun, 26 Feb 2023 02:19:13 GMT  
  Content: Community members making it clear that Nebraskans are firmly on the side of trans people outside the @LCRPNE fundraiser featuring Charlie Kirk. Why was he invited to speak in Nebraska on the National Day of Hate, created by white nationalist antisemites to intimidate Jews?  
  (Media: 1 photo)  
  Engagement: Likes=217, Reposts=25, Quotes=7, Replies=11, Bookmarks=0, Views=24346  
  **Relevance**: References a Charlie Kirk speaking appearance/fundraiser in Nebraska (prior to or around Feb 26, 2023; outside the exact week but in semantic results).

- **Post ID: 1630241780913573888** (Author: @CPAC)  
  Timestamp: Mon, 27 Feb 2023 16:21:43 GMT  
  Content: CONFIRMED SPEAKER: @realMikeLindell will be speaking at CPAC DC 2023. March 1st-4th more information at http://CPAC.org/DC  
  (Media: 1 video)  
  Engagement: Likes=226, Reposts=53, Quotes=203, Replies=869, Bookmarks=7, Views=378183  
  **Relevance**: CPAC event (March 1-4, 2023) with speakers; no direct Charlie Kirk/TPUSA mention here, but related conservative speaking circuit.

- **Post ID: 1630199630053998601** (Author: @RSBNetwork)  
  Timestamp: Mon, 27 Feb 2023 13:34:14 GMT  
  Content: DON'T MISS: CPAC in Washington, D.C. - March 1-4, 2023 🇺🇸  
  We will be LIVE in our nation's capital this week covering the top conservative leaders, including President Donald J. Trump ‼️  
  https://www.rsbnetwork.com/news/live-cpac-in-washington-d-c-march-1-4-2023/  
  Engagement: Likes=429, Reposts=196, Quotes=14, Replies=55, Bookmarks=4, Views=37316  
  **Relevance**: Coverage of CPAC speaking events (March 1-4, 2023).

- **Post ID: 1630226057935634434** (Author: @CPAC)  
  Timestamp: Mon, 27 Feb 2023 15:19:15 GMT  
  Content: Join CPAC’s all-star list of table hosts who will be at the Ronald Reagan Dinner and come hear @KariLake speak on Friday, March 3rd  
  https://t.co/VDtCzuXZ6i  
  Engagement: Likes=394, Reposts=89, Quotes=54, Replies=286, Bookmarks=3, Views=247473  
  **Relevance**: CPAC speaking event details.

- **Post ID: 1630272948664664071** (Author: @mschlapp)  
  Timestamp: Mon, 27 Feb 2023 18:25:34 GMT  
  Content: CONFIRMED SPEAKER: @SenJohnKennedy will be speaking at CPAC DC 2023. March 1st-4th more information at http://CPAC.org/DC  
  (Media: 1 video)  
  Engagement: Likes=549, Reposts=90, Quotes=90, Replies=1004, Bookmarks=1, Views=64472  
  **Relevance**: CPAC speaker confirmations.

- **Post ID: 1630634475913637889** (Author: @CPAC)  
  Timestamp: Tue, 28 Feb 2023 18:22:09 GMT  
  Content: WATCH as @KariLake calls out the Fake News:  
  “Why won’t you be honest with the people of this country?”  
  We’re wondering the same thing  
  Why did they cover up the Hunter laptop story or the origins of COVID?  
  Why are they so determined to continue to lie to the American people?  
  (Media: 1 video)  
  Engagement: Likes=2097, Reposts=514, Quotes=36, Replies=277, Bookmarks=9, Views=96591  
  **Relevance**: CPAC event footage/speaking.

- **Post ID: 1630574611875221504** (Author: @gatewaypundit)  
  Timestamp: Tue, 28 Feb 2023 14:24:16 GMT  
  Content: President Trump to Be Keynote Speaker at CPAC In DC This Week – Mike Pence and Ron DeSantis to Skip This Year’s Event https://www.thegatewaypundit.com/2023/02/mike-pence-and-ron-desantis-to-skip-cpac-president-trump-will-be-keynote-speaker/?utm_source=rss&utm_medium=rss&utm_campaign=mike-pence-and-ron-desantis-to-skip-cpac-president-trump-will-be-keynote-speaker  
  Engagement: Likes=421, Reposts=126, Quotes=20, Replies=78, Bookmarks=2, Views=20041  
  **Relevance**: CPAC keynote speaking details.

### Additional notes from results:
- No direct posts from the searched range about events strictly on Feb 26–Mar 1 (pre-UCSB) beyond the Nebraska mention and general tour promo.
- The dominant event in the week is the **Live Free Tour stop at UC Santa Barbara (UCSB)** on/around March 1–2, 2023, with heavy promotion, live streaming, and protest coverage by @TPUSA and @charliekirk11.
- Upcoming: University of Kentucky on March 8 (announced post-event).
- Semantic search also surfaced unrelated CPAC (March 1–4) speaker announcements, as it overlaps the conservative speaking calendar.
- All data included verbatim; no filtering beyond tool returns. No other @TPUSA or @charliekirk11 posts in the range detailed additional stops. For full context, the Live Free Tour link (tpusa.com/livefree) was promoted multiple times.
```

