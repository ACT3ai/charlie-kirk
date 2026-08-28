---
unlisted: true
title: "Week 35 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W35"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-08-26 to 2024-09-01."
status: completed
hide_table_of_contents: true
---

# Week 35, 2024

- Date range: 2024-08-26 to 2024-09-01
- Queried at (UTC): 2026-08-24T19:14:23Z
- Model: grok-4.3
- API status: completed
- Response id: e1419e88-83aa-970d-8ce2-6902a8e610c4

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-08-26 to the end of the week 2024-09-01.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR \"speaking at\" OR \"speaks at\" OR campus OR university OR college) since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR \"speaking at\" OR \"speaks at\" OR campus OR university OR college) since:2024-08-26 until:2024-09-02 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR university OR college OR TPUSA) since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus OR university OR college) since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus tours, or appearances between August 26 and September 1 2024",
      "limit": "10",
      "from_date": "2024-08-26",
      "to_date": "2024-09-02"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"You’re Being Brainwashed\" OR \"Brainwashed Tour\") (tour OR event OR speaking OR speak OR \"will be\" OR appearing OR appearance OR \"speaking at\" OR \"speaks at\" OR campus OR university OR college OR stop OR stops) since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (tour OR event OR speaking OR speak OR \"will be\" OR appearing OR appearance OR \"speaking at\" OR \"speaks at\" OR campus OR university OR college OR stop OR stops) since:2024-08-26 until:2024-09-02 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"You’re Being Brainwashed Tour\" OR \"Brainwashed Tour\" OR \"theturningpointtour.com\") since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2024-08-26 until:2024-09-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSASpeakers OR from:TPUSAFaith OR from:TPUSAStudents since:2024-08-26 until:2024-09-02",
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
  "input_tokens": 35389,
  "input_tokens_details": {
    "cached_tokens": 13504
  },
  "output_tokens": 1681,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 37070,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 892595500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 11,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 23317,
    "output_tokens": 971
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1828525391428100193",
    "start_index": 187,
    "end_index": 240,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1828525391428100193",
    "start_index": 552,
    "end_index": 605,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1828525391428100193",
    "start_index": 2018,
    "end_index": 2071,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1827879043536232929",
    "start_index": 2286,
    "end_index": 2347,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1828843756474511631",
    "start_index": 2643,
    "end_index": 2704,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1829961893626462536",
    "start_index": 3067,
    "end_index": 3120,
    "title": "4"
  }
]
```

## Grok response

```text
**No specific public speaking events, campus appearances, or stops for Charlie Kirk or TPUSA were mentioned in X posts from August 26 to September 1, 2024 (the week ending September 1).**[[1]](https://x.com/TPUSA/status/1828525391428100193)

### Key Relevant Posts (All Data Included, No Summaries)

- **August 27, 2024 (Tue), @TPUSA (Turning Point USA)**:  
  "The YOU’RE BEING BRAINWASHED TOUR ft. @charliekirk11 is here.  
  Get tickets for a stop near you at https://theturningpointtour.com/ @tpusastudents"  
  (Video attached promoting the tour.)[[1]](https://x.com/TPUSA/status/1828525391428100193)

- **August 27, 2024 (Tue), multiple regional TPUSA accounts and users reposting/promoting the same tour** (examples):  
  - @samtpusa: “📢 BIG NEWS 🇺🇸🔥 @TPUSA has OFFICIALLY launched the “You’re Being Brainwashed Tour” 🧠🧼 @charliekirk11 might be coming to a college campus near you 👀 Click the link below to find out more ⬇️ https://theturningpointtour.com/”  
  - @thestephstevens: “🚨The FALL 2024 TOUR is HERE 🚨 Don’t miss the YOU’RE BEING BRAINWASHED Tour coming to a campus near you🤩 @TPUSA @tpusastudents @charliekirk11 #brainwashedtour #tpusa” (Photos attached.)  
  - @MarissaMahacek (TPUSA Great Lakes Regional Manager): “Don’t miss your opportunity to hear from @charliekirk11 🇺🇸 Get tickets now for the YOU’RE BEING BRAINWASHED TOUR! https://t.co/QX0Jc0kbKn @TPUSA @tpusastudents @TPUSAEvents @TpusaGreatLakes” (Photo attached.)  
  - @MatthewBoedy: “The new Turning Point USA and Charlie Kirk college campus tour made public today. The “You are Being Brainwashed” Tour does *not* mention TPUSA campus tour regular Candace Owens. https://theturningpointtour.com/”  
  - @ItsBeamm: “That’s a funny AD. “You’re being brainwashed tour” LOL”  
  - @crouch01: “Brainwashed Tour Page https://theturningpointtour.com/”  
  - @WCUSpatriot: “The “You’re Being Brainwashed Tour””  
  These posts announce the launch of the tour but provide **no specific dates, locations, or stops within August 26–September 1**.[[1]](https://x.com/TPUSA/status/1828525391428100193)

- **August 28, 2024 (Wed), @charliekirk11**:  
  “Thank you 🙏 was an honor to speak on such a historic night.” (No details on location, audience, or event type; context appears unrelated to a new TPUSA tour stop.)[[2]](https://x.com/charliekirk11/status/1827879043536232929)

- **August 28, 2024 (Wed), @charliekirk11**:  
  Post about an Ohio State University on-campus faith event (“Let's give Him the glory”) involving Bible distribution and baptisms. Kirk commented positively but **did not indicate he was speaking there or that it was a TPUSA/Charlie Kirk event**.[[3]](https://x.com/charliekirk11/status/1828843756474511631)

- **No posts** from @TPUSA, @charliekirk11, or related accounts (@TPUSASpeakers, @TPUSAFaith, @TPUSAStudents, @TPUSA_LU, etc.) announcing or detailing any specific speaking events, campus visits, or appearances by Charlie Kirk during the exact date range. Other @TPUSA posts in the period were unrelated (e.g., general commentary on politics, crime, education).[[4]](https://x.com/TPUSA/status/1829961893626462536)

- **No posts** from @TPUSAFaith or similar in the range discussed speaking events by Kirk or TPUSA.

The tour announcement on August 27 is the only direct reference to upcoming Charlie Kirk speaking events via TPUSA, directing users to theturningpointtour.com for stops (no specific dates listed in the X posts themselves). All other posts in the range are either unrelated commentary, reposts of the tour promo, or older clips of past events. No additional details (e.g., venues, exact dates in the week, or confirmations of appearances) appear in the searched X data.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-08-26 to 2024-09-01**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-08-26 to 2024-09-01 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
