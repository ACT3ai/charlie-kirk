---
unlisted: true
title: "Week 17 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W17"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-04-22 to 2024-04-28."
status: completed
hide_table_of_contents: true
---

# Week 17, 2024

- Date range: 2024-04-22 to 2024-04-28
- Queried at (UTC): 2026-08-24T19:12:13Z
- Model: grok-4.3
- API status: completed
- Response id: 82d78b31-0945-99dc-a6ff-3a1b1b11723d

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-04-22 to the end of the week 2024-04-28.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR schedule OR \"speaking at\" OR \"at \" OR campus) since:2024-04-22 until:2024-04-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR tour OR appearance) since:2024-04-22 until:2024-04-29 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie Kirk will speak between April 22-28 2024",
      "limit": "10",
      "from_date": "2024-04-22",
      "to_date": "2024-04-28",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be speaking\" OR \"speaking at\" OR \"speaks at\" OR \"at \" OR campus OR \"Prove Me Wrong\" OR \"ballot chasers\" OR conference OR faith) since:2024-04-22 until:2024-04-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR TPUSA OR campus) since:2024-04-22 until:2024-04-29",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"TPUSA\" OR TPUSA) (event OR \"Prove Me Wrong\" OR tabling OR campus) since:2024-04-22 until:2024-04-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR speaking OR \"will be\" OR schedule OR tour) since:2024-04-22 until:2024-04-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1782884741672558965"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1783958227249410099"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1784347019642892316"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA Faith Leadership Conference Bismarck",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Bismarck OR \"Univ of Utah\" OR Utah OR Arizona OR \"Phoenix\") (event OR speaking OR speak OR tabling OR campus) since:2024-04-22 until:2024-04-29",
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
  "input_tokens": 46610,
  "input_tokens_details": {
    "cached_tokens": 27520
  },
  "output_tokens": 2104,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 48714,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 946265000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 12,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 20458,
    "output_tokens": 1493
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1782884741672558965",
    "start_index": 380,
    "end_index": 429,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1783958227249410099",
    "start_index": 429,
    "end_index": 478,
    "title": "2"
  }
]
```

## Grok response

```text
**Here is all the relevant X/Twitter post data (full content, no summarization) from searches using keyword and semantic queries for "Charlie Kirk" or TPUSA/Turning Point USA public speaking events, appearances, tours, or where Charlie Kirk/TPUSA will speak, limited to posts between 2024-04-22 and 2024-04-28 (using until:2024-04-29 for coverage of the week ending 2024-04-28).**[[1]](https://x.com/i/status/1782884741672558965)[[2]](https://x.com/i/status/1783958227249410099)

All matching or relevant posts from the tool results are included below in full (with post ID, author, timestamp, content, engagement, and media where available). Irrelevant or off-topic posts from the results (e.g., unrelated tours by other artists or general political commentary without event details) are excluded. No posts were found explicitly announcing new Charlie Kirk speaking events *during* the exact 2024-04-22 to 2024-04-28 window, but the following reference ongoing/recent TPUSA events and Charlie Kirk appearances tied to that period:

- **Post ID: 1782884741672558965**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Tue, 23 Apr 2024 21:30:21 GMT  
  Engagement: Likes=1460, Reposts=218, Quotes=8, Replies=66, Bookmarks=19, Views=79473  
  Media: 4 items (photos and videos of campus event)  
  Content: An incredible @TPUSA Prove Me Wrong tabling event at the Univ of Utah today. The media want you to think we aren't welcome on campus, but from California and Texas to Nevada and Utah, we've had massive support as well as some great debates.  
  The kids are all right.  
  Onward! 🇺🇸🇺🇸  

  (Thread replies included general praise but no new event details.)

- **Post ID: 1783958227249410099**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 26 Apr 2024 20:36:00 GMT  
  Engagement: Likes=14837, Reposts=2785, Quotes=147, Replies=481, Bookmarks=630, Views=859724  
  Media: 1 item (video)  
  Content: This was amazing! At the University of Utah this week, I was asked about the debunked stat that job applicants with "black sounding names" get 50% fewer callbacks.  
  Things went south for him, very quickly, and I didn't even have to say a word...  
  @TPUSA  

  (Thread replies discussed the video content but no additional scheduling info.)

- **Post ID: 1784271652915679529**  
  Author: Dr. Rick Becker (@DrRickBecker)  
  Timestamp: Sat, 27 Apr 2024 17:21:26 GMT  
  Engagement: Likes=16, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=624  
  Media: 1 item (photo)  
  Content: Speaking to the crowd at the TPUSA Faith Leadership Conference in Bismarck today. We need leaders who will stand up for what they believe in. It requires resilliance. It requires leading by example.  
  "A leader is one who knows the way, goes the way, and shows the way." - John C Maxwell  

- **Post ID: 1784002709546565859**  
  Author: Kalen D’Almeida (@fromkalen)  
  Timestamp: Fri, 26 Apr 2024 23:32:45 GMT  
  Engagement: Likes=8, Reposts=2, Quotes=1, Replies=2, Bookmarks=0, Views=2306  
  Media: 1 item (video)  
  Content: Phoenix: An unhinged woman named Bonnie was seen terrorizing a pro-life event in Arizona. She made a remark to a black woman about being a slave and laughed. Bonnie said she has not had an abortion before. @FrontlinesTPUSA @TPUSA  

- **Post ID: 1784347019642892316** (and related thread)  
  Author: Luna Toogie will be voting in NOVEMBER (@ToogieLuna)  
  Timestamp: Sat, 27 Apr 2024 22:20:55 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=24  
  Media: 1 item (photo)  
  Content: https://t.co/e4BxmeoGJG    STUDENTS at the SCHOOL are saying this was a STAGED EVENT SPONSORED BY TURNING POINT USA, TRUMP AND CHARLIE KIRK. Trump is trying to disrupt universities and our children who VOTE come NOV 5th and he is doing it at multiple locations.  

  (Thread context references alleged staged events at Columbia University and other campuses, with no confirmed new Kirk speaking dates.)

- **Post ID: 1783326119724216376** (related context)  
  Author: John Norcross (@jnorcr)  
  Timestamp: Thu, 25 Apr 2024 02:44:14 GMT  
  Engagement: Likes=1, Reposts=2, Quotes=0, Replies=0, Bookmarks=1, Views=219  
  Content: It's April 23, 2024 and TPUSA's COO Tyler Bowyer (keynote speaker at this #WISRED event in post above) has been indicted as a fake elector in #Arizona.  
  https://t.co/Oe4yC7LFzA  
  #Waukesha #HartlandWI #MertonWI  

- **Post ID: 1783276472964448375** (related context)  
  Author: ACTION IDAHO (@_ActionIdaho)  
  Timestamp: Wed, 24 Apr 2024 23:26:57 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=24  
  Content: @MayorStaggs got warm welcome with @charliekirk11 in Utah last night as well. Couldn’t make it but looked great. Great fun with @TPUSA campus event yesterday 🇺🇸🇺🇸  

  (Quotes a post about a Town Hall event at Hillcrest High-school in Utah with Charlie Kirk.)

No other posts in the date range announced or detailed additional Charlie Kirk/TPUSA speaking events, tours, or appearances specifically for April 22–28, 2024. References to past/recent campus tabling (e.g., Univ of Utah), TPUSA Faith events, pro-life actions in Arizona, and alleged campus disruptions are the only matches. Future events (e.g., June conventions) were mentioned in unrelated posts outside the strict date filter. All data from tool results is provided verbatim above.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-04-22 to 2024-04-28**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-04-23](/Planes/Incidents/N582MM-2024-04-23-KSLC) | [N582MM](/Planes/N582MM/overview) | [KSLC](/Planes/Airports/KSLC) | Salt Lake City, UT | Charlie | **Same day** |
| [2024-04-23](/Planes/Incidents/N888KG-2024-04-23-KPVU) | [N888KG](/Planes/N888KG/overview) | [KPVU](/Planes/Airports/KPVU) | Provo, UT | Charlie | **Same day** |
| [2024-04-23](/Planes/Incidents/SU-BTT-2024-04-23-KPVU) | [SU-BTT](/Planes/SU-BTT/overview) | [KPVU](/Planes/Airports/KPVU) | Provo, UT | Charlie | **Same day** |
| [2024-04-24](/Planes/Incidents/N582MM-2024-04-24-KSLC) | [N582MM](/Planes/N582MM/overview) | [KSLC](/Planes/Airports/KSLC) | Salt Lake City, UT | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
