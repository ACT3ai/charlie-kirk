---
unlisted: true
title: "Week 27 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W27"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-07-01 to 2024-07-07."
status: completed
hide_table_of_contents: true
---

# Week 27, 2024

- Date range: 2024-07-01 to 2024-07-07
- Queried at (UTC): 2026-08-24T19:13:26Z
- Model: grok-4.3
- API status: completed
- Response id: 9071bd1e-ec2c-96dc-b605-8e96f2f49b2b

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-07-01 to the end of the week 2024-07-07.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR \"speaking event\" OR tour OR appearance OR \"will be speaking\" OR \"speaking at\" OR event OR campus) since:2024-07-01 until:2024-07-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour) since:2024-07-01 until:2024-07-08 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie Kirk will speak between July 1-7 2024",
      "limit": "10",
      "from_date": "2024-07-01",
      "to_date": "2024-07-07"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 8318,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 513,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 8831,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 234544000,
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
    "input_tokens": 6728,
    "output_tokens": 316
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809691058391130523",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809691058391130523"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809633654932455583",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809633654932455583"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1807912594860290315",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1807912594860290315"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809625591873704049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809625591873704049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1808216725579878851",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1808216725579878851"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1808877309681938626",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1808877309681938626"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1808848147549974613",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1808848147549974613"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809348771177984027",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809348771177984027"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809576472547332226",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809576472547332226"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1807899938279592256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1807899938279592256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1808653697750347917",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1808653697750347917"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809738307275801003",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809738307275801003"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809477502949073169",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809477502949073169"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809735027539755508",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809735027539755508"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1808202774049612194",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1808202774049612194"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809285052888453128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809285052888453128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1807943291884728573",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1807943291884728573"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809263246249222192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809263246249222192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1809622905707209202",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1809622905707209202"
  }
]
```

## Grok response

```text
**Here is the complete, unfiltered data from the X/Twitter searches** (all posts returned across the three tool calls for the exact date range 2024-07-01 to 2024-07-07, inclusive of posts up to 2024-07-08 in the keyword searches to capture the full week). No summarization or filtering applied—every post is included verbatim with its metadata. Note that the searches returned limited relevant results on Charlie Kirk or TPUSA speaking events specifically within that narrow 7-day window; most mentions are tangential or reference future events outside the range.

### From first x_keyword_search (basic keyword query, Latest mode, 10 results):
- **[post:0]** ID: 1809738307275801003  
  Conversation ID: 1809718210654081166  
  Author: Jonathan Pakianathan - @JonPakianathan  
  Timestamp: Sat, 06 Jul 2024 23:56:50 GMT  
  Content: This reminds me if that time leftists protesting outside a TPUSA event left for an hour, suspiciously replaced by neo Nazis for an hour before returning later all timed for cameras. Just like the fake Nazis outside the Youngkin rally that turned out to be anti gop activists.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16

- **[post:1]** ID: 1809735027539755508  
  Conversation ID: 180
```

