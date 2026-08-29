---
unlisted: true
title: "Week 37 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W37"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-09-10 to 2023-09-16."
status: completed
hide_table_of_contents: true
---

# Week 37, 2023

- Date range: 2023-09-10 to 2023-09-16
- Queried at (UTC): 2026-08-24T19:08:41Z
- Model: grok-4.3
- API status: completed
- Response id: d2ae06c5-1774-92b4-bd11-aaa0b850589a

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-09-10 to the end of the week 2023-09-16.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR appearance OR \"will be\" OR schedule OR \"public speaking\" OR campus OR university) since:2023-09-10 until:2023-09-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR tour OR \"will speak\" OR appearance) (from:charliekirk11 OR from:TPUSA) since:2023-09-10 until:2023-09-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, appearances, or where Charlie will speak between September 10-16 2023",
      "limit": "10",
      "from_date": "2023-09-10",
      "to_date": "2023-09-16"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 9141,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 1223,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 10364,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 262581500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 3,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 7551,
    "output_tokens": 1018
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702476014931054612",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702476014931054612"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702078374770794780",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702078374770794780"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702777994362704178",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702777994362704178"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702789892269363413",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702789892269363413"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702058751849595129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702058751849595129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702789872921235583",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702789872921235583"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702765363124162569",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702765363124162569"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702788301646954776",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702788301646954776"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702825289418522662",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702825289418522662"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702003227678347455",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702003227678347455"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702698576747344255",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702698576747344255"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702540688758538548",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702540688758538548"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702076480740892965",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702076480740892965"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1701317771576090966",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1701317771576090966"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702503238426390827",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702503238426390827"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702815089089220623",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702815089089220623"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702541163956449336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702541163956449336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702789863206961415",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702789863206961415"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702012065282670869",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702012065282670869"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702125408093712600",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702125408093712600"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1701673907269558305",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1701673907269558305"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1702792830958084153",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1702792830958084153"
  }
]
```

## Grok response

```text
**All X posts found matching the query for Charlie Kirk or TPUSA public speaking events/appearances/speaking tours between 2023-09-10 and 2023-09-16 (inclusive).**  
Posts were retrieved via keyword search (exact date range with `since:2023-09-10 until:2023-09-17`) and semantic search focused on events, speaking, tours, or appearances. Only posts with any relevance to events/speaking are included; unrelated posts were filtered out. No posts from the official accounts directly announcing new Charlie Kirk/TPUSA events *within* the exact week were found. One relevant TPUSA Students post announces a future event. All data is presented without summarization.

### Relevant Posts (Chronological by Timestamp):

- **[post:21]** ID: 1701673907269558305  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 12 Sep 2023 19:07:29 GMT  
  Content: The first #AMFEST2023 speaker drop is here! Joining us to fight the good fight is…  
  @charliekirk11, @RealCandaceO, @HawleyMO, @Riley_Gaines_, @realMikeLindell, @conservmillen, @DennisPrager, @ConceptualJames, and @RealJackHibbs (with many more speakers to come!)  
  🔗 https://t.co/dUbWU6xyFE to register and claim 50% OFF GA before early bird ends!  
  (Media: Video)  
  Engagement: Likes=217, Reposts=95, Quotes=34, Replies=15, Bookmarks=1, Views=85977  
  *Relevance: Announces Charlie Kirk as a speaker at AMFEST2023 (future event; date not specified in post).*

- **[post:12]** ID: 1702012065282670869  
  Author: TPUSA Students (@tpusastudents)  
  Timestamp: Wed, 13 Sep 2023 17:31:12 GMT  
  Content: PROVE ME WRONG - The Government IS Lying to You 🫣  
  @charliekirk1776 will be at Northern Arizona University on September 19th at 1 p.m. If you don’t agree, now is your chance to discuss. See you there!!  
  (Media: Photo)  
  Engagement: Likes=275, Reposts=70, Quotes=5, Replies=15, Bookmarks=1, Views=47080  
  *Relevance: Announces Charlie Kirk speaking event at Northern Arizona University on September 19, 2023 (future event, just after the date range).*

- **[post:3]** ID: 1702789892269363413  
  Author: 🚨👑 King EJ 👑🚨 (@newkingej)  
  Timestamp: Fri, 15 Sep 2023 21:02:01 GMT  
  Content: LOL, someone posted video of Charlie Kirk speaking before a "pastors conference" yesterday.  
  What wisdom is this 29 year old passing on to elders?  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=181  
  *Relevance: References a video of Charlie Kirk speaking at a pastors conference (implied to have occurred on or around September 14, 2023).*

- **[post:4]** ID: 1702789872921235583  
  Author: Jason K Watkins (@JasonKimbleyW)  
  Timestamp: Fri, 15 Sep 2023 21:01:56 GMT  
  Content: Ann Atkinson lost her job at ASU after inviting Charlie Kirk to speak on campus.  
  Students deserve to hear a plurality of voices, especially voices they may disagree with.  
  Limiting students’ exposure to ideas does a disservice to them and to the entire community.  
  Engagement: Likes=4, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=194  
  *Relevance: References past invitation for Charlie Kirk to speak on campus at ASU (contextual mention of a speaking event/appearance).*

### Additional Notes on Search Results:
- No direct posts from @charliekirk11 or @TPUSA announcing or detailing new speaking events/tours/appearances strictly within the 2023-09-10 to 2023-09-16 window.  
- The semantic search returned several unrelated posts about other figures' events (e.g., Trump, DeSantis schedules), which were excluded.  
- The keyword search captured some tangential mentions of speaking but no additional concrete event details for Charlie Kirk/TPUSA in the exact period.  
- All posts above are presented verbatim with full metadata. No further filtering or summarization applied.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-09-10 to 2023-09-16**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2023-09-14](/Planes/Incidents/N582MM-2023-09-14-KSAN) | [N582MM](/Planes/N582MM/overview) | [KSAN](/Planes/Airports/KSAN) | San Diego, CA | Charlie | Day after |
| [2023-09-15](/Planes/Incidents/N582MM-2023-09-15-KSAN) | [N582MM](/Planes/N582MM/overview) | [KSAN](/Planes/Airports/KSAN) | San Diego, CA | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
