---
unlisted: true
title: "Week 20 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W20"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-05-14 to 2025-05-20."
status: completed
hide_table_of_contents: true
---

# Week 20, 2025

- Date range: 2025-05-14 to 2025-05-20
- Queried at (UTC): 2026-08-24T19:18:18Z
- Model: grok-4.3
- API status: completed
- Response id: 1be5db6f-097f-942b-a7cc-cc0ebe3d09ca

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-05-14 to the end of the week 2025-05-20.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR appearance OR \"will be\" OR visiting OR \"public speaking\" OR campus OR rally OR conference) since:2025-05-14 until:2025-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will speak\" OR appearance) since:2025-05-14 until:2025-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus OR \"will be\") since:2025-05-14 until:2025-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR campus OR \"will be\") since:2025-05-14 until:2025-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between May 14 and May 20 2025",
      "limit": "10",
      "from_date": "2025-05-14",
      "to_date": "2025-05-21"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (event OR speaking OR speak OR \"will speak\" OR appearance OR \"will be speaking\" OR tour OR campus OR rally OR conference OR \"speaking event\") since:2025-05-14 until:2025-05-21 -from:charliekirk11 -from:TPUSA",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (Arizona OR AZ OR \"Andy Biggs\" OR tpaction) since:2025-05-14 until:2025-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk TPUSA Turning Point USA speaking events campus tours rallies conferences appearances May 14 to May 20 2025",
      "limit": "10",
      "from_date": "2025-05-14",
      "to_date": "2025-05-21",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (speaking OR event OR tour OR \"will be\" OR appearance) since:2025-05-14 until:2025-05-21",
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
  "input_tokens": 27406,
  "input_tokens_details": {
    "cached_tokens": 12096
  },
  "output_tokens": 1321,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 28727,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 698592000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 9,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 16792,
    "output_tokens": 716
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/KPruett1776/status/1924609325160702329",
    "start_index": 269,
    "end_index": 328,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/grok/status/1924598112074793312",
    "start_index": 710,
    "end_index": 762,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/KPruett1776/status/1924609325160702329",
    "start_index": 1602,
    "end_index": 1661,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/KPruett1776/status/1924609325160702329",
    "start_index": 2271,
    "end_index": 2330,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/christomlin/status/1923423365815030156",
    "start_index": 2620,
    "end_index": 2679,
    "title": "3"
  }
]
```

## Grok response

```text
**No direct announcements or detailed posts about specific Charlie Kirk or TPUSA public speaking events, tours, campus appearances, rallies, or speaking schedules were found in the searched X posts from May 14–20, 2025 (date range: since:2025-05-14 until:2025-05-21).**[[1]](https://x.com/KPruett1776/status/1924609325160702329)

The keyword and semantic searches across multiple queries (including variations with @charliekirk11, @TPUSA, "Turning Point USA", "speaking event", "will be speaking", campus, rally, conference, tour, Arizona/AZ, Andy Biggs, tpaction, etc.) returned mostly unrelated or tangential content. No posts from official accounts (@charliekirk11 or @TPUSA) in the period mentioned events.[[2]](https://x.com/grok/status/1924598112074793312)

### Relevant posts mentioning events (all included verbatim below, with full available metadata):

- **Post by Kristen Pruett (@KPruett1776)**, May 19, 2025, 23:33:15 GMT (ID: 1924609325160702329)  
  **Content:** "Just got reservations to go to the @tpaction @andybiggs4az event happening in 2 weeks!! I’m so excited! No one throws events like TPAction and TPUSA and there is no better candidate for AZ than Andy Biggs!"  
  **Media:** Two photos (URLs: https://pbs.twimg.com/media/GrWV9sXbAAEI3DD.jpg and https://pbs.twimg.com/media/GrWV9t5a4AAEbG4.jpg)  
  **Engagement:** 1 like, 0 reposts, 0 quotes, 0 replies, 0 bookmarks, 43 views  
  **Note:** This references a TPAction/TPUSA-linked event in Arizona with Andy Biggs, scheduled ~2 weeks later (around early June 2025). No mention of Charlie Kirk speaking or specific date/details.[[1]](https://x.com/KPruett1776/status/1924609325160702329)

- **Post by anarchotahdigism (@anarchotadigism)**, May 19, 2025, 21:22:50 GMT (ID: 1924574087344472488)  
  **Content:** "still thinking about the (mostly yt) gays in black bloc who spent so fuckin long gathering to advance on TPUSA event booth to take their shelter & throw one punch while blasting that fucking Zionist Lady Gaga & the so-called left called it a massive win it's all a LARP to y'all"  
  **Media:** None listed  
  **Engagement:** 0 likes, 0 reposts, 0 quotes, 0 replies, 0 bookmarks, 140 views  
  **Note:** References a past TPUSA event booth (no date, location, or Charlie Kirk details).[[1]](https://x.com/KPruett1776/status/1924609325160702329)

All other results from the date range were unrelated (e.g., general commentary on Charlie Kirk, tours by unrelated artists like Chris Tomlin or Jimmy Dore, old events, or non-event topics). No posts detailed upcoming or current speaking schedules for Charlie Kirk/TPUSA in the exact week.[[3]](https://x.com/christomlin/status/1923423365815030156)

This exhausts all results from the tool calls. No additional event data (locations, dates, or Charlie Kirk appearances) appears in the posts.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-05-14 to 2025-05-20**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2025-05-14 to 2025-05-20 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
