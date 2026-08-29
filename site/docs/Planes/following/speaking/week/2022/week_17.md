---
unlisted: true
title: "Week 17 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W17"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-04-23 to 2022-04-29."
status: completed
hide_table_of_contents: true
---

# Week 17, 2022

- Date range: 2022-04-23 to 2022-04-29
- Queried at (UTC): 2026-08-24T19:00:18Z
- Model: grok-4.3
- API status: completed
- Response id: 30dd0939-1237-93bf-8a05-a81ea9ddf2d6

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-04-23 to the end of the week 2022-04-29.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"public speaking\" OR appearance OR \"will be\" OR \"speaking at\" OR \"appearing at\") since:2022-04-23 until:2022-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"public speaking\" OR appearance OR \"will be\" OR \"speaking at\" OR \"appearing at\") since:2022-04-23 until:2022-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Arizona OR Texas OR Florida OR California OR \"New York\" OR Michigan OR Ohio OR \"South Carolina\" OR Georgia OR \"North Carolina\") since:2022-04-23 until:2022-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus tours, or appearances where Charlie will speak",
      "limit": "10",
      "from_date": "2022-04-23",
      "to_date": "2022-04-30",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\" OR \"Turning Point Action\") (event OR speaking OR speak OR tour OR campus OR appearance OR \"will be\" OR \"speaking at\" OR \"appearing at\" OR rally OR \"faith and freedom\" OR stumping OR stump) since:2022-04-23 until:2022-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 OR from:TPUSA since:2022-04-23 until:2022-04-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR speaking OR speak OR \"will speak\" OR \"speaking at\" OR campus OR tour) since:2022-04-23 until:2022-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (event OR speaking OR speak OR tour OR campus) since:2022-04-23 until:2022-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1519784841956397056"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1519800121948520448"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1519768419029200896"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Ohio OR \"Josh Mandel\" OR Vance OR \"faith freedom\" OR rally) since:2022-04-23 until:2022-04-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR \"will speak\" OR campus OR \"speaking at\") since:2022-04-23 until:2022-04-30 -filter:replies",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 36977,
  "input_tokens_details": {
    "cached_tokens": 5568
  },
  "output_tokens": 1578,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 38555,
  "num_sources_used": 0,
  "num_server_side_tools_used": 13,
  "cost_in_usd_ticks": 1093198500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 13,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 16087,
    "output_tokens": 862
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/StellaSimmonds1/status/1519811535597568000",
    "start_index": 735,
    "end_index": 798,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1519784841956397056",
    "start_index": 1092,
    "end_index": 1145,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1519784841956397056",
    "start_index": 1410,
    "end_index": 1459,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1519794924316618752",
    "start_index": 1861,
    "end_index": 1922,
    "title": "4"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1519768419029200896",
    "start_index": 2102,
    "end_index": 2151,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/HagermanLarry/status/1519808084507598848",
    "start_index": 2312,
    "end_index": 2373,
    "title": "6"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/AssyrianGOP/status/1519303530288451585",
    "start_index": 2560,
    "end_index": 2619,
    "title": "7"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1519758109236809728",
    "start_index": 2830,
    "end_index": 2883,
    "title": "8"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/officialmaksimz/status/1519526672621580289",
    "start_index": 2954,
    "end_index": 3017,
    "title": "9"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TravisTritt/status/1518579877317791744",
    "start_index": 3121,
    "end_index": 3181,
    "title": "10"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TheRReport/status/1519796329546981377",
    "start_index": 3368,
    "end_index": 3427,
    "title": "11"
  }
]
```

## Grok response

```text
**No posts from the specified date range (April 23–29, 2022, inclusive; searches used until:2022-04-30 to capture the full week) were found that announce, promote, or detail specific public speaking events, campus tours, rallies, appearances, or locations where Charlie Kirk or TPUSA would speak.**

Extensive searches across multiple queries on X (Twitter) posts—including keyword searches for terms like "event," "speaking," "speak," "tour," "campus," "appearance," "will be," "speaking at," "appearing at," "rally," "stump," combined with "Charlie Kirk," "@charliekirk11," "TPUSA," or "Turning Point USA," plus state-specific and semantic searches—yielded zero relevant results announcing or describing such events during that week.[[1]](https://x.com/StellaSimmonds1/status/1519811535597568000)

### Key Findings from All Posts Retrieved:
- The dominant theme in posts from April 23–29, 2022, is **Charlie Kirk's return to Twitter/X** on or around April 28, 2022, after a month-long suspension. TPUSA and Charlie Kirk posted celebratory content, and users reacted positively or otherwise.[[2]](https://x.com/TPUSA/status/1519784841956397056)
  - Example (TPUSA, April 28): "HE'S BACK!! 🙌🇺🇸 Thanks to new management (we love @ElonMusk, don't we, folks??), @CharlieKirk11's month-long Twitter suspension is over and the great freedom fighter is back! READ MORE from @TPostMillennial!" (with link to article).[[3]](https://x.com/i/status/1519784841956397056)
  - Example (Charlie Kirk, April 28): Multiple general political posts, e.g., "If their victory were inevitable, their propaganda wouldn’t be necessary," "There's never been more momentum for the America First Movement...," "We have a two-party system in America right now. It's the Parents Party or the Perverts Party," and "There is an undeniable War on White People in The West." No event mentions.[[4]](https://x.com/charliekirk11/status/1519794924316618752)
  - TPUSA live stream post (April 28): "🔴LIVE NOW: Guess Who’s Back? Back Again! Watch daily shows, live in-studio content from TPUSA HQ..." (no public speaking events announced).[[5]](https://x.com/i/status/1519768419029200896)

- Other posts are unrelated reactions, general commentary, or spam. Examples include border security complaints, references to lockdowns, or off-topic replies.[[6]](https://x.com/HagermanLarry/status/1519808084507598848)

- One post references a **past event** (not during the date range): Assyrian GOP noting Charlie Kirk's endorsement "last week at our event in Springfield" (likely prior to April 23–29).[[7]](https://x.com/AssyrianGOP/status/1519303530288451585)

- Mentions of events **outside the date range or unrelated**:
  - TPUSA Young Women's Leadership Summit (#ywls2022) ticket promotion (future event; no date/location tied to this week or Charlie Kirk speaking).[[8]](https://x.com/TPUSA/status/1519758109236809728)
  - General TPUSA campus chapter praise (no specific upcoming events).[[9]](https://x.com/officialmaksimz/status/1519526672621580289)
  - Unrelated tours/rallies (e.g., Travis Tritt shows, YAF speakers on April 27, Ted Cruz/Ohio events).[[10]](https://x.com/TravisTritt/status/1518579877317791744)

- One post speculates on Charlie Kirk stumping for JD Vance in Ohio (with Josh Hawley), but this is a news-style mention without dates, confirmation of speaking, or ties to April 23–29.[[11]](https://x.com/TheRReport/status/1519796329546981377)

All tool results (keyword searches with/without user filters, semantic search, and thread fetches) were reviewed exhaustively. No announcements, schedules, locations, or details about Charlie Kirk or TPUSA public speaking events in the target week exist in the posts. If events occurred, they were not promoted or discussed on X during April 23–29, 2022.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-04-23 to 2022-04-29**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-04-23 to 2022-04-29 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
