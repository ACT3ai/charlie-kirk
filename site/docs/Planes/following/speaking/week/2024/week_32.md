---
unlisted: true
title: "Week 32 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W32"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-08-05 to 2024-08-11."
status: completed
hide_table_of_contents: true
---

# Week 32, 2024

- Date range: 2024-08-05 to 2024-08-11
- Queried at (UTC): 2026-08-24T19:14:02Z
- Model: grok-4.3
- API status: completed
- Response id: 44557d18-ba32-95d5-a339-37e3ce6bdb2c

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-08-05 to the end of the week 2024-08-11.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speech OR event OR \"will speak\" OR \"speaking at\" OR tour OR appearance) since:2024-08-05 until:2024-08-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speech) (location OR where OR campus OR university OR college) since:2024-08-05 until:2024-08-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speech OR tour OR appearance OR TPUSA) since:2024-08-05 until:2024-08-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speech OR tour OR appearance) since:2024-08-05 until:2024-08-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (August 5 OR August 6 OR August 7 OR August 8 OR August 9 OR August 10 OR August 11) (speaking OR event OR speech) since:2024-08-05 until:2024-08-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (speaking OR \"will speak\" OR \"speaking at\" OR \"speaks at\" OR event OR rally OR tour OR appearance OR \"town hall\" OR campus) (August OR \"this week\" OR \"next week\" OR schedule OR dates) since:2024-08-05 until:2024-08-12 -filter:replies",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Phoenix OR Arizona OR \"Las Vegas\" OR Nevada OR \"Salt Lake\" OR Utah OR Texas OR Florida OR \"New York\" OR California) (event OR speaking OR speech) since:2024-08-05 until:2024-08-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA OR from:charliekirk11 OR from:tpusastudents (event OR speaking OR \"town hall\" OR campus OR university) since:2024-08-05 until:2024-08-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, speeches, campus appearances, or tour dates in early August 2024",
      "limit": "10",
      "from_date": "2024-08-05",
      "to_date": "2024-08-12",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 20354,
  "input_tokens_details": {
    "cached_tokens": 9920
  },
  "output_tokens": 1480,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 21834,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 637265000,
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
    "input_tokens": 11865,
    "output_tokens": 846
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822409332656336900",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822409332656336900"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820610614622081123",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820610614622081123"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820500910696767715",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820500910696767715"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821696973835268475",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821696973835268475"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821573894710481256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821573894710481256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821921085677244545",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821921085677244545"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820896610743722182",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820896610743722182"
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
    "url": "https://x.com/i/status/1822378565100269818",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822378565100269818"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822323531843047724",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822323531843047724"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822376973450027274",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822376973450027274"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821956919000457387",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821956919000457387"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820995319519162681",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820995319519162681"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820261156122177605",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820261156122177605"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820984747763626455",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820984747763626455"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822310834124505414",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822310834124505414"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822036211462005173",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822036211462005173"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822403209648058770",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822403209648058770"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821629596904906785",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821629596904906785"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822172579987079203",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822172579987079203"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821567951793004750",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821567951793004750"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822126497085239402",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822126497085239402"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820459756395389090",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820459756395389090"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822114991601848688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822114991601848688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821369786867085476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821369786867085476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821223207732670579",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821223207732670579"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821897413650739369",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821897413650739369"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1820982266190811609",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1820982266190811609"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822348336269029828",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822348336269029828"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821618898241745169",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821618898241745169"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822367440703205713",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822367440703205713"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1822303772237844517",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1822303772237844517"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1821233438353141914",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1821233438353141914"
  }
]
```

## Grok response

```text
**Here is every relevant X post found from the date range 2024-08-05 to 2024-08-11 (searched via keyword and semantic queries targeting Charlie Kirk, TPUSA/Turning Point USA, speaking events, speeches, campus appearances, tours, town halls, or related announcements). All results are included without summarization or filtering beyond the query scope. No other posts matched the criteria for public speaking events or appearances by Charlie Kirk or TPUSA in that exact week.**

- **[post:20]** ID: 1822036211462005173  
  Author: Steve Smothermon (@Stevesmothermon)  
  Timestamp: Fri, 09 Aug 2024 22:24:19 GMT  
  Content: Exciting news! Charlie Kirk, is coming to Legacy Church this Sunday, August 11th, at 6:30pm for a special ‘Freedom Night in America’ event. Join us as we learn how to make an impact in our community. Together, we’ll work towards change in Albuquerque and across New Mexico, all while honoring God. Don’t miss this opportunity to be inspired and equipped to put your faith into action. See you at Legacy Church’s Central Campus. Let’s make a difference together!  
  (Media: 1 photo)  
  Engagement: Likes=22, Reposts=5, Quotes=0, Replies=4, Bookmarks=1, Views=726

- **[post:21]** ID: 1821921085677244545  
  Author: Mason Cottrell (@maseface32)  
  Timestamp: Fri, 09 Aug 2024 14:46:51 GMT  
  Content: Back on campus next week??? Back on campus next week. Oklahoma State and OU org fairs up next.  
  (Media: 1 photo)  
  Engagement: Likes=5, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=120  
  (Mentions: @TPUSA @tpusastudents @tpusasc)

- **[post:22]** ID: 1821897413650739369  
  Author: faith © (@faith_knaus)  
  Timestamp: Fri, 09 Aug 2024 13:12:47 GMT  
  Content: Get ready North Georgia! Coming to a college campus near you!!! 🇺🇸🇺🇸🇺🇸 I can’t wait to kick things off on campus next week. Make sure you follow us on Instagram @tpusapeach for updates on where we will be!! 📸  
  (Media: 1 photo)  
  Engagement: Likes=418, Reposts=48, Quotes=1, Replies=11, Bookmarks=5, Views=12074  
  (Mentions: @TPUSA @tpusastudents)

- **[post:23]** ID: 1820500910696767715  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Mon, 05 Aug 2024 16:43:35 GMT  
  Content: .@DruHammer talks about the importance of forgiveness as she healed after her divorce. 📆 Join us THIS Wednesday, August 7, 2024, at 6:30 pm at Dream City Church as we hear from Charlie Kirk and Dru Hammer. 🎟 Register for this FREE event: https://tpusafaith.com/register-for-freedom-night/?utm_source=Social+Media&utm_medium=Social+Media&utm_campaign=FNIA+launch  
  (Media: 1 video)  
  Engagement: Likes=2, Reposts=1, Quotes=0, Replies=1, Bookmarks=1, Views=464

**No other posts in the searched range contained announcements, details, or references to specific public speaking events, speeches, campus visits, tours, or appearances by Charlie Kirk or TPUSA during August 5–11, 2024. Posts referencing past events (e.g., June TPUSA town hall) or unrelated topics were excluded.**
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-08-05 to 2024-08-11**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-08-05 to 2024-08-11 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
