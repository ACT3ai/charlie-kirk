---
unlisted: true
title: "Week 05 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W05"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-01-29 to 2023-02-04."
status: completed
hide_table_of_contents: true
---

# Week 05, 2023

- Date range: 2023-01-29 to 2023-02-04
- Queried at (UTC): 2026-08-24T19:05:34Z
- Model: grok-4.3
- API status: completed
- Response id: 7d6644b8-1b17-976f-b0a4-fdb3fb26cfcc

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-01-29 to the end of the week 2023-02-04.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR appearance OR tour OR \"speaking event\" OR \"will be\" OR \"speaking at\" OR campus OR university OR college) since:2023-01-29 until:2023-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR speaking) since:2023-01-29 until:2023-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be speaking\" OR \"speaking at\") since:2023-01-29 until:2023-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance) since:2023-01-29 until:2023-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between Jan 29 and Feb 4 2023",
      "limit": "10",
      "from_date": "2023-01-29",
      "to_date": "2023-02-05"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Turning Point\") (Miami OR \"Power of the People\" OR Bolsonaro OR \"Power Of The People\") since:2023-01-29 until:2023-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (Miami OR Bolsonaro OR \"Power of the People\" OR TPUSA) since:2023-01-29 until:2023-02-05",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (Miami OR Bolsonaro OR \"Power of the People\") since:2023-01-29 until:2023-02-05",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (campus OR university OR college OR speaking OR event) since:2023-01-29 until:2023-02-05 -Bolsonaro -Miami",
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
  "input_tokens": 16816,
  "input_tokens_details": {
    "cached_tokens": 4416
  },
  "output_tokens": 1926,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 18742,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 661982000,
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
    "input_tokens": 9101,
    "output_tokens": 1401
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621655398351572992",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621655398351572992"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621639611700350978",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621639611700350978"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621656644286382080",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621656644286382080"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621658541130907650",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621658541130907650"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620828682582622210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620828682582622210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620592167046762496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620592167046762496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1619799223846989824",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1619799223846989824"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620828685153734656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620828685153734656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621641702791598080",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621641702791598080"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621601938939973635",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621601938939973635"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1619510911735300096",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1619510911735300096"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620477522113855488",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620477522113855488"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621629958186729472",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621629958186729472"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620484486285905921",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620484486285905921"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1619901840426151936",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1619901840426151936"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1620467068930859009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1620467068930859009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621659723224256512",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621659723224256512"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621659370521088000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621659370521088000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1621161883805044737",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1621161883805044737"
  }
]
```

## Grok response

```text
**All relevant X/Twitter posts from the specified date range (2023-01-29 to 2023-02-04, with searches extending to 2023-02-05 to capture the full week) mentioning public speaking events, appearances, tours, or locations where Charlie Kirk or TPUSA would speak or host events are included below. No other events (e.g., unrelated campus tours or additional TPUSA/Charlie Kirk speaking appearances) were found in the results.**

**Posts from @charliekirk11 (Charlie Kirk):**
- [post:5] / [post:20] ID: 1621639611700350978 (Fri, 03 Feb 2023 22:39:46 GMT)  
  Content: "Happening now! Tune in live for President Bolsonaro's first public event since the elections in Brazil"  
  (Quoted post links to a YouTube live stream; context from surrounding posts ties it to the TPUSA Miami event.)

- [post:4] / [post:18] ID: 1621641702791598080 (Fri, 03 Feb 2023 22:48:05 GMT)  
  Content: "I had the honor of sitting down for an exclusive interview with Brazilian President Jair Bolsonaro just minutes ago. We made some news! Will post the interview to The Charlie Kirk Show podcast feed ASAP. Stay tuned... https://podcasts.apple.com/us/podcast/the-charlie-kirk-show/id1460600818"

- [post:12] / [post:20] ID: 1620477522113855488 (Tue, 31 Jan 2023 17:42:02 GMT)  
  Content: "Brazil has become a key battleground in the global clash between the power of the people and the tyranny of a corrupt globalist machine. TPUSA is honored to host President Jair Bolsonaro in Miami THIS FRIDAY for his first public event following the recent Brazilian elections."  
  (Media: Photo attached.)

- [post:21] ID: 1619510911735300096 (Sun, 29 Jan 2023 01:41:05 GMT)  
  Content: "TPUSA 'Teens Against Gender Mutilation' rally crashed by radical trans activists https://thepostmillennial.com/breaking-tpusa-teens-against-gender-mutilation-rally-crashed-by-radical-trans-activists?utm_campaign=64501"

**Posts from @TPUSA (Turning Point USA):**
- [post:6] / [post:26] ID: 1621629958186729472 (Fri, 03 Feb 2023 22:01:25 GMT)  
  Content: "🚨RIGHT NOW: Charlie Kirk & Brazilian President Jair Bolsonaro speak LIVE from Miami TUNE IN⬇️ https://www.youtube.com/watch?v=jgS6ydhGALw"

- [post:7] / [post:11] / [post:27] ID: 1621601938939973635 (Fri, 03 Feb 2023 20:10:04 GMT)  
  Content: "TONIGHT👀: @jairbolsonaro addresses the people for the FIRST TIME in 2023. He will be speaking with @charliekirk11 LIVE from Miami🌴 at 5ET / 2PT Tickets Available: https://t.co/9uv7f4AB6d"  
  (Media: Photo attached.)

- [post:8] / [post:29] ID: 1620828682582622210 (Wed, 01 Feb 2023 16:57:26 GMT)  
  Content: "“Former Brazil President Jair Messias Bolsonaro is set to appear at a Turning Point USA event on Friday, which will be his first public event since the Brazilian presidential election in October.” https://thepostmillennial.com/breaking-tpusa-to-host-power-to-the-people-rally-in-miami-with-president-bolsonaro"

- [post:28] ID: 1620828685153734656 (Wed, 01 Feb 2023 16:57:26 GMT)  
  Content: "Join TPUSA for “Power of the People” ft. Brazilian President Jair Bolsonaro on February 3rd in Miami, Florida:"

**Other relevant posts (mentions of TPUSA/Charlie Kirk events):**
- [post:0] / [post:2] / [post:24] ID: 1621658541130907650 (Fri, 03 Feb 2023 23:54:59 GMT, @JayneZirkle)  
  Content: "Brazilian President Bolsonaro gets swarmed by supporters and media as he exits the “Power Of The People” @TPUSA event"  
  (Media: Video attached.)

- [post:1] / [post:3] ID: 1621655398351572992 (Fri, 03 Feb 2023 23:42:30 GMT, @MarceloMarcosA8)  
  Content: "Assista a "TPUSA presents The Power of The People Event LIVE Featuring Charlie Kirk & Jair Bolsonaro" no YouTube https://www.youtube.com/live/jgS6ydhGALw?feature=share"

- [post:22] ID: 1621659723224256512 (Fri, 03 Feb 2023 23:59:41 GMT, @Pri_22_brasil)  
  Content: "Adorei a legenda abaixo do nome do presidente. Presidente Bolsonaro está falando agora no Turning Point USA na Florida. Saudade chega a doer, o melhor presidente do mundo. 💚🇧🇷🙏🏻"  
  (Media: Photo attached.)

- [post:23] ID: 1621659370521088000 (Fri, 03 Feb 2023 23:58:17 GMT, @fazendaimperial)  
  Content: "LIVE: Brazil's former President Jair Bolsonaro speaks at a Turning Point... https://t.co/JQG7PZL3LD via @YouTube"

- [post:25] ID: 1621656644286382080 (Fri, 03 Feb 2023 23:47:27 GMT, @ConceioLage3)  
  Content: "Meu presidente Bolsonaro"

**No other posts** in the date range referenced additional Charlie Kirk or TPUSA public speaking events, campus appearances, tours, or speaking locations outside of the Miami "Power of the People" event with Jair Bolsonaro on February 3, 2023 (with live streams, interviews, and related commentary occurring that day). Searches excluding the Bolsonaro/Miami terms returned no results for other events.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-01-29 to 2023-02-04**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-01-29 to 2023-02-04 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
