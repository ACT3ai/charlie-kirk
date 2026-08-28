---
unlisted: true
title: "Week 10 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W10"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-03-05 to 2023-03-11."
status: completed
hide_table_of_contents: true
---

# Week 10, 2023

- Date range: 2023-03-05 to 2023-03-11
- Queried at (UTC): 2026-08-24T19:06:00Z
- Model: grok-4.3
- API status: completed
- Response id: 13deddae-6be7-9ed8-a5ce-2c218bab2f7e

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-03-05 to the end of the week 2023-03-11.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR \"public speaking\" OR tour OR campus OR \"will be\" OR speaking OR appearance) since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR tour OR campus OR appearance OR \"will be\") since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR tour OR campus OR appearance OR \"will be\") since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events or where Charlie will speak between March 5 and March 11 2023",
      "limit": "10",
      "from_date": "2023-03-05",
      "to_date": "2023-03-12"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Live Free Tour\") (event OR speak OR speaking OR tour OR campus OR appearance OR \"will be\" OR \"at the\" OR chicago OR kentucky OR illinois) since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2023-03-05 until:2023-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk TPUSA Live Free Tour events locations dates March 2023",
      "limit": "10",
      "from_date": "2023-03-05",
      "to_date": "2023-03-12"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 22065,
  "input_tokens_details": {
    "cached_tokens": 9408
  },
  "output_tokens": 2176,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 24241,
  "num_sources_used": 0,
  "num_server_side_tools_used": 8,
  "cost_in_usd_ticks": 631428500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 8,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 14019,
    "output_tokens": 1728
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634341031822131200",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634341031822131200"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633524017406566403",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633524017406566403"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633317807801679879",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633317807801679879"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634338270367690754",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634338270367690754"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634317245693435904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634317245693435904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1632803141224738817",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1632803141224738817"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250338034413568",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250338034413568"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634324863317082119",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634324863317082119"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633615028355223553",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633615028355223553"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634247900615286784",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634247900615286784"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634226716662018049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634226716662018049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634318082259689472",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634318082259689472"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633512722066284567",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633512722066284567"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250015169183745",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250015169183745"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634243529458462720",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634243529458462720"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633151973695586304",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633151973695586304"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250017757356032",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250017757356032"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634227346491465730",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634227346491465730"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633995057899638784",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633995057899638784"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250014011846656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250014011846656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633958341012774913",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633958341012774913"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634238710425239559",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634238710425239559"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250016671039489",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250016671039489"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634341917994385410",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634341917994385410"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633204987991056386",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633204987991056386"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634250858362994688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634250858362994688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633994105993965568",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633994105993965568"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634274577252749312",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634274577252749312"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633987262022299648",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633987262022299648"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633620704930430977",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633620704930430977"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634309058873409538",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634309058873409538"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634295128008581125",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634295128008581125"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1632803397949882369",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1632803397949882369"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634337735698784258",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634337735698784258"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634295603818647553",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634295603818647553"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634306043957362688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634306043957362688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1634324866165018624",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1634324866165018624"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1633635718856691713",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1633635718856691713"
  }
]
```

## Grok response

```text
**Here is every relevant post** from the searched X/Twitter results (using keyword and semantic searches for terms like "Charlie Kirk", TPUSA, "Turning Point USA", "Live Free Tour", event/speak/speaking/tour/campus/appearance/"will be", combined with the exact date range March 5–11, 2023, or March 5–12 inclusive to capture the full week) mentioning public speaking events, locations where Charlie Kirk or TPUSA would speak, or related tour stops. No summarization—full post content, metadata, and context are included exactly as retrieved. Irrelevant posts (e.g., unrelated "speaking" or other tours) were filtered out during tool use.

### Posts from @TPUSA (Turning Point USA):
- **Post ID: 1633995057899638784**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 10 Mar 2023 00:55:54 GMT  
  Content: 🔴LIVE NOW: TPUSA Presents The LIVE FREE Tour with Charlie Kirk at the University of Illinois Chicago  
  https://www.youtube.com/live/JPGJE08wBW8?feature=share  
  Engagement: Likes=34, Reposts=4, Quotes=0, Replies=2, Bookmarks=0, Views=7994

- **Post ID: 1633987262022299648**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 10 Mar 2023 00:24:55 GMT  
  Content: Happening now at the University of Illinois Chicago outside of TPUSA's Live Free Tour:  
  (Includes video media)  
  Engagement: Likes=149, Reposts=30, Quotes=3, Replies=40, Bookmarks=0, Views=81001

- **Post ID: 1633958341012774913**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 09 Mar 2023 22:30:00 GMT  
  Content: TONIGHT: @charliekirk11 & @RealCandaceO will be in Chicago @ the University of Illinois on the LIVE FREE TOUR  
  Tickets: https://t.co/yWJGPEdkWw  
  (Includes photo media)  
  Engagement: Likes=55, Reposts=12, Quotes=0, Replies=5, Bookmarks=2, Views=6915

- **Post ID: 1633620704930430977**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 09 Mar 2023 00:08:21 GMT  
  Content: 🔴LIVE NOW: TPUSA Presents The LIVE FREE Tour with @charliekirk11 at the University of Kentucky  
  Engagement: Likes=25, Reposts=7, Quotes=0, Replies=3, Bookmarks=0, Views=6901

- **Post ID: 1634324866165018624** (reply thread)  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 10 Mar 2023 22:46:27 GMT  
  Content: See you in Davis, next week!  
  Engagement: Likes=22, Reposts=5, Quotes=1, Replies=0, Bookmarks=0, Views=7611  
  (Context: In reply to a thread about a UC Davis professor criticizing a TPUSA event)

- **Post ID: 1634324863317082119**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 10 Mar 2023 22:46:26 GMT  
  Content: For people wondering how students get so radical, this is who they are learning from.  
  (Quotes a Charlie Kirk post about a UC Davis professor calling for cancellation of a TPUSA event)  
  Engagement: Likes=72, Reposts=20, Quotes=1, Replies=7, Bookmarks=0, Views=16837

- **Post ID: 1632803397949882369**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 06 Mar 2023 18:00:40 GMT  
  Content: Catch @charliekirk11 on The Live Free Tour at a stop near you ⬇️ @tpusastudents  
  Engagement: Likes=8, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=5677

### Posts from @charliekirk11 (Charlie Kirk):
- **Post ID: 1633994105993965568**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 10 Mar 2023 00:52:07 GMT  
  Content: My University of Illinois- Chicago welcoming committee. Should be a fun night!  
  Catch the live stream here starting at 7pm CT: https://t.co/mDYsOFF0zV  
  (Includes video media)  
  Engagement: Likes=723, Reposts=115, Quotes=6, Replies=105, Bookmarks=0, Views=107700  
  (Directly references the UIC Live Free Tour event on March 10, 2023)

- **Post ID: 1634247900615286784**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 10 Mar 2023 17:40:37 GMT  
  Content: This UC Davis professor, Joshua Clover, is calling for our TPUSA event to be cancelled. He is welcome to come to my event and challenge me to my face, but I bet he is too much of a coward, so instead he slanders me and our students online.  
  (Includes photo media)  
  Engagement: Likes=5409, Reposts=1336, Quotes=72, Replies=556, Bookmarks=18, Views=250507  
  (References an upcoming/planned TPUSA event at/near UC Davis)

### Other relevant posts mentioning the events (reposts, reports, or direct references):
- **Post ID: 1634295603818647553**  
  Author: Dinesh D'Souza (@DineshDSouza)  
  Timestamp: Fri, 10 Mar 2023 20:50:10 GMT  
  Content: Violent protestors assault man, try to stop Charlie Kirk, Candace Owens from speaking at TPUSA Live Free Tour event in Chicago  
  https://humanevents.com/2023/03/10/violent-protestors-assault-man-try-to-stop-charlie-kirk-candace-owens-from-speaking-at-tpusa-live-free-tour-event-in-chicago  
  Engagement: Likes=511, Reposts=159, Quotes=8, Replies=56, Bookmarks=3, Views=72381

- **Post ID: 1634238710425239559**  
  Author: Jack Posobiec (@JackPosobiec)  
  Timestamp: Fri, 10 Mar 2023 17:04:05 GMT  
  Content: Violent protestors assault man, try to stop Charlie Kirk, Candace Owens from speaking at TPUSA Live Free Tour event in Chicago  
  https://humanevents.com/2023/03/10/violent-protestors-assault-man-try-to-stop-charlie-kirk-candace-owens-from-speaking-at-tpusa-live-free-tour-event-in-chicago?utm_campaign=64483  
  Engagement: Likes=298, Reposts=91, Quotes=1, Replies=28, Bookmarks=1, Views=43957

No additional posts from the searches explicitly detailed events strictly between March 5–9, 2023 (beyond the University of Kentucky stop referenced on March 9). The primary confirmed events in the week are:
- University of Kentucky (Live Free Tour with Charlie Kirk) – referenced as live on March 9.
- University of Illinois Chicago (Live Free Tour with Charlie Kirk + Candace Owens) – March 10 (with live streams, protests, and welcoming committee posts).

All retrieved data is included above; no further relevant posts matched the strict criteria in the tool results.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-03-05 to 2023-03-11**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-03-05 to 2023-03-11 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
