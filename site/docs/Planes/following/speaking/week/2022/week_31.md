---
unlisted: true
title: "Week 31 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W31"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-07-30 to 2022-08-05."
status: completed
hide_table_of_contents: true
---

# Week 31, 2022

- Date range: 2022-07-30 to 2022-08-05
- Queried at (UTC): 2026-08-24T19:02:06Z
- Model: grok-4.3
- API status: completed
- Response id: 77a9b900-f871-92ae-96f7-e0ed30473765

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-07-30 to the end of the week 2022-08-05.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (tour OR events OR \"speaking tour\" OR \"campus tour\") since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR \"will be\" OR appearing) since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR \"will be\" OR appearing) since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR tour OR campus) since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between July 30 and August 5 2022",
      "limit": "10",
      "from_date": "2022-07-30",
      "to_date": "2022-08-06"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearing OR appearance OR \"speaking tour\" OR \"campus tour\") since:2022-07-30 until:2022-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"TPUSA\" OR \"Turning Point USA\") (Florida OR Tampa OR \"Anna Paulina Luna\") since:2022-07-30 until:2022-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"TPUSA Pastors Summit\" OR \"Pastors Summit\" since:2022-07-30 until:2022-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR Ft. Worth OR \"GoVictoryTV\" OR SWBC22 OR Flashpoint) since:2022-07-30 until:2022-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Kari Lake\" OR \"Don Jr\" OR \"Kimberly Guilfoyle\" OR \"JP Sears\") (event OR speaking OR TPUSA) since:2022-07-30 until:2022-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"activism events on campus\" OR \"College Representatives\" TPUSA since:2022-07-30 until:2022-08-06",
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
  "input_tokens": 22210,
  "input_tokens_details": {
    "cached_tokens": 11584
  },
  "output_tokens": 2342,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 24552,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 814543000,
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
    "input_tokens": 12073,
    "output_tokens": 1658
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554872997210599424",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554872997210599424"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554990580794531841",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554990580794531841"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555304690681782281",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555304690681782281"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555290993666101248",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555290993666101248"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554831657579847680",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554831657579847680"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1553967645170339840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1553967645170339840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555250193922154497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555250193922154497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555085430520918016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555085430520918016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554942372718452739",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554942372718452739"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554844514623270913",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554844514623270913"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554538508286566402",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554538508286566402"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555186387527548929",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555186387527548929"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555064287026024448",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555064287026024448"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555266759388790784",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555266759388790784"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554806399506464768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554806399506464768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555302774211940352",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555302774211940352"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555314233469984772",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555314233469984772"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554882270812639236",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554882270812639236"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554921227860549632",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554921227860549632"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554247152834052101",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554247152834052101"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555299965911457792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555299965911457792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555280372082040832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555280372082040832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554877701189644288",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554877701189644288"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555257244706414592",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555257244706414592"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1553433474572251136",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1553433474572251136"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554101100516712454",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554101100516712454"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555266690941952006",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555266690941952006"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554717248417173505",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554717248417173505"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555287040056516618",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555287040056516618"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555306922567274496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555306922567274496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555279874989985803",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555279874989985803"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555307497573027840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555307497573027840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1555320645269049344",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1555320645269049344"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1554624328112541696",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1554624328112541696"
  }
]
```

## Grok response

```text
**Here is every relevant X/Twitter post** from the search results matching the exact date range (posts from 2022-07-30 through 2022-08-05, captured via searches up to 2022-08-06), focused on public speaking events, appearances, tours, campus events, or locations where Charlie Kirk or TPUSA were speaking or scheduled to appear. All data is included verbatim without summarization. Only posts with direct or contextual ties to events in the window are listed; unrelated posts were excluded.

### Posts referencing TPUSA events in Florida/Tampa (contextually around late July/early August 2022, described as "last week" or recent):

- **Post ID: 1555287040056516618**  
  Author: Eric Lynn (@EricLynnFL)  
  Timestamp: Thu, 04 Aug 2022 20:18:20 GMT  
  Content: Last week, Anna Paulina Luna attended Turning Point USA's event in Florida, where Nazis rallied in support.  
  Shamefully, Luna still hasn’t condemned them, and does not belong anywhere near Congress.  
  Engagement: Likes=79, Reposts=21, Quotes=1, Replies=2, Bookmarks=0, Views=N/A

- **Post ID: 1555266690941952006**  
  Author: Kyle Reese (@NightAgent99)  
  Timestamp: Thu, 04 Aug 2022 18:57:29 GMT  
  Content: Who wants to play "Catch the fake Nazi's" from the Turning Point USA event in Tampa?

- **Post ID: 1555306922567274496** (reply context to above events)  
  Author: We all should be Charlie Kirk (@ManOnDaNet)  
  Timestamp: Thu, 04 Aug 2022 21:37:21 GMT  
  Content: So I imagine @SecGranholm will be “moving on to spend more time with her family” any moment now. #TrushIsHeresy #NuclearEnergy  
  (No direct event mention but in thread referencing TPUSA Florida events.)

- **Post ID: 1555250193922154497** (contextual reference)  
  Author: Roberto Herrera (@Rherrera42R)  
  Timestamp: Thu, 04 Aug 2022 17:51:56 GMT  
  Content: You're talking about the same women that had to apologize on TV about lying on a TPUSA event? They are nothing more than propaganda at this point.

- **Post ID: 1555290993666101248** (contextual reference)  
  Author: CRAIG (@IamaGrip)  
  Timestamp: Thu, 04 Aug 2022 20:34:03 GMT  
  Content: Did he denounce the Tampa Nazis from the @TPUSA rally?

- **Post ID: 1554806399506464768** (contextual reference)  
  Author: malcolm (@MalcomapMalcolm)  
  Timestamp: Wed, 03 Aug 2022 12:28:27 GMT  
  Content: I honestly think these are the feds bro. Because its strange they come to only right-wing events but never come to these left-wing events here in Florida. Plus, at the last TPUSA event those Nazi's were there in protest against the event, they weren't for it.

- **Post ID: 1554624328112541696** (contextual reference)  
  Author: William Hall (@William43285469)  
  Timestamp: Wed, 03 Aug 2022 00:24:58 GMT  
  Content: Exactly, they hate tpusa, been protesting them for few years due to tpusa jewish links. Videos f multiple tpusa events where they yelled at kids entering & leaving event

### Post about TPUSA training/activism events on campus:

- **Post ID: 1555299965911457792** (and duplicate in other searches)  
  Author: Chris Gaffrey (@ChrisGaffrey) – Turning Point USA Director of College Operations  
  Timestamp: Thu, 04 Aug 2022 21:09:42 GMT  
  Content: Teaching the next generation of @TPUSA College Representatives the importance of activism events on campus! Such a bright group of leaders!  
  Media: 2 photos (showing training/session)  
  Engagement: Likes=11, Reposts=5, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

### Post by Charlie Kirk referencing a past event in the period:

- **Post ID: 1553967645170339840**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 01 Aug 2022 04:55:32 GMT  
  Content: Great event with @GoVictoryTV tonight in Ft. Worth—WOW! 4,000+ on a Sunday evening. Remarkable energy. The media is very scared of Christians rising up to reclaim America—and the left should be terrified!  
  #SWBC22 #Flashpoint  
  Media: 1 video  
  Engagement: Likes=862, Reposts=170, Quotes=10, Replies=59, Bookmarks=5, Views=N/A  
  (Event occurred on or around Sunday, July 31, 2022, within the week.)

### Post referencing future TPUSA Pastors Summit (outside the exact week but announced in-range):

- **Post ID: 1554942372718452739**  
  Author: Michael O'Fallon (@SovMichael)  
  Timestamp: Wed, 03 Aug 2022 21:28:45 GMT  
  Content: I would love to meet you in the next month!  
  My live event schedule for August is as follows:  
  August 10-12, 2022: TPUSA Pastors Summit, San Diego, CA:  
  August 25-27, 2022: Non-Conformist Conf, NY, NY  
  We are finalizing events in Virginia, London (UK) and Phoenix for the fall.  
  Media: 1 photo  
  Engagement: Likes=11, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

### Other contextual mentions (no specific new events announced for the week):

- **Post ID: 1554872997210599424** (general reference)  
  Author: LoL (@THElolercopter)  
  Timestamp: Wed, 03 Aug 2022 16:53:05 GMT  
  Content: CNN and MSNBC have opinion shows but they also report the news. Charlie Kirk enters TPUSA events like he’s on the WWE. They all continuously lie to you because they know they’ll face no backlash for it and even when you do get proven that they lie you don’t care.

- **Post ID: 1554717248417173505** (general reference)  
  Author: AZindependents (@zindependents)  
  Timestamp: Wed, 03 Aug 2022 06:34:11 GMT  
  Content: Ruben V was the tenth trump associate convicted of child sex crimes And was Ronnas friend and was at tpusa events for trump

No additional posts from official @charliekirk11, @TPUSA accounts, or others in the exact window announced new events, tours, or appearances for Charlie Kirk/TPUSA specifically between July 30–August 5, 2022 (searches for "tour", "speaking tour", "campus tour", "will be", "appearing", etc., returned zero direct matches beyond the above). The Tampa/Florida event appears to have occurred in the prior week relative to August 4 posts. The Ft. Worth event is explicitly dated to the start of the week. No other locations, dates, or speaker schedules were detailed in posts from this range.
```

