---
unlisted: true
title: "Week 53 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W53"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-12-31 to 2022-12-31."
status: completed
hide_table_of_contents: true
---

# Week 53, 2022

- Date range: 2022-12-31 to 2022-12-31
- Queried at (UTC): 2026-08-24T19:04:42Z
- Model: grok-4.3
- API status: completed
- Response id: 48035ae4-9c39-9fec-9069-ecf1087eb2c5

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-12-31 to the end of the week 2022-12-31.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR event OR tour OR campus OR speech OR \"will be\" OR speaking OR \"public speaking\" OR \"speaking event\") since:2022-12-31 until:2023-01-01",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR tour OR \"campus tour\" OR \"speaking tour\") since:2022-12-31 until:2023-01-01",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR tour OR speak OR campus) since:2022-12-31 until:2023-01-01",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR tour OR speak OR campus) since:2022-12-31 until:2023-01-01",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, campus events where Charlie Kirk will speak or appear",
      "limit": "10",
      "from_date": "2022-12-31",
      "to_date": "2023-01-01",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 3515,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 509,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 4024,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 274406500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 5,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 1925,
    "output_tokens": 210
  }
}
```

## Grok response

```text
**No relevant X (Twitter) posts were found** for the specified date range (posts from 2022-12-31 to the end of that week, i.e., until 2023-01-01).

I ran multiple targeted searches using both keyword-based advanced search operators and semantic search, including:
- Broad queries combining "Charlie Kirk", TPUSA, or "Turning Point USA" with terms like "speaking", "event", "tour", "campus", "speech", "will be", etc.
- Specific searches from the accounts @charliekirk11 and @TPUSA.
- Semantic search for announcements about public speaking events, tours, or appearances.

All searches returned **zero results**. This likely indicates there were no public posts on X matching the criteria during that exact narrow window (a single day at the end of 2022 / very start of 2023).

If you'd like me to expand the date range, adjust the search terms, or search for a different period, let me know!
```

