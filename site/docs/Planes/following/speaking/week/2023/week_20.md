---
unlisted: true
title: "Week 20 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W20"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-05-14 to 2023-05-20."
status: completed
hide_table_of_contents: true
---

# Week 20, 2023

- Date range: 2023-05-14 to 2023-05-20
- Queried at (UTC): 2026-08-24T19:07:05Z
- Model: grok-4.3
- API status: completed
- Response id: 5a5b54cc-3e13-9bd3-a853-25c1467bdf87

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-05-14 to the end of the week 2023-05-20.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR appearance OR \"public speaking\" OR campus OR \"will be\" OR speaking OR \"speaks at\" OR \"speaking at\") since:2023-05-14 until:2023-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR tour OR speaking) (May 2023 OR \"this week\" OR \"next week\" OR schedule OR calendar) since:2023-05-14 until:2023-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between May 14-20 2023",
      "limit": "10",
      "from_date": "2023-05-14",
      "to_date": "2023-05-20"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA) (event OR events OR speaking OR speak OR tour OR appearance OR campus OR \"will speak\" OR \"speaking at\" OR schedule OR \"this week\" OR \"next week\" OR May) since:2023-05-14 until:2023-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR tour OR speaking OR speak OR campus OR TPUSA) since:2023-05-14 until:2023-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR events OR tour OR speaking OR campus OR YWLS OR summit) since:2023-05-14 until:2023-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA speaking events or tour schedule in May 2023",
      "limit": "10",
      "from_date": "2023-05-14",
      "to_date": "2023-05-20"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\") (event OR tour OR speaking OR \"will be speaking\" OR \"speaks at\" OR campus OR \"public speaking\" OR schedule) (May OR 2023) since:2023-05-14 until:2023-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"YWLS2023\" OR \"Educators Summit\" OR \"Turning Point Academy\" OR \"Pastor's Summit\") since:2023-05-14 until:2023-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2023-05-14 until:2023-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2023-05-14 until:2023-05-21",
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
  "input_tokens": 40165,
  "input_tokens_details": {
    "cached_tokens": 16384
  },
  "output_tokens": 2807,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 42972,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 950205500,
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
    "input_tokens": 20404,
    "output_tokens": 2128
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659657992365654016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659657992365654016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658650138196451328",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658650138196451328"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659315462289670145",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659315462289670145"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658110513136427012",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658110513136427012"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659676534460801024",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659676534460801024"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659201499694768133",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659201499694768133"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659708420528668674",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659708420528668674"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658664269469175809",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658664269469175809"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659277004540375041",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659277004540375041"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659707917812244480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659707917812244480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659567450386747393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659567450386747393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657809750443323393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657809750443323393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659661280448507904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659661280448507904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659690234328813569",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659690234328813569"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659693298766979073",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659693298766979073"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659656852601446400",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659656852601446400"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659672676187897856",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659672676187897856"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659259783361495046",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659259783361495046"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659675468109414401",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659675468109414401"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658850832455016452",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658850832455016452"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659710344116224003",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659710344116224003"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659657383310663682",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659657383310663682"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659655073142804480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659655073142804480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659204863081992196",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659204863081992196"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659703279948029952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659703279948029952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659690235754848256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659690235754848256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657926137530712065",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657926137530712065"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658243191248932864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658243191248932864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659697005139214336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659697005139214336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659659559156195339",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659659559156195339"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658285803783729153",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658285803783729153"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658154041044611088",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658154041044611088"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659621221338628105",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659621221338628105"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659666551010652160",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659666551010652160"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659623224811094016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659623224811094016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659649074042388480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659649074042388480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659314746871664641",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659314746871664641"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659301510440706048",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659301510440706048"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659277958324842497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659277958324842497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659631790322245632",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659631790322245632"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658880205325205518",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658880205325205518"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658827447016517632",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658827447016517632"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659621882914824192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659621882914824192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658285169785094145",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658285169785094145"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659107835286790145",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659107835286790145"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659685761241976832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659685761241976832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659581883074719746",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659581883074719746"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659710182434430978",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659710182434430978"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659707671195336706",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659707671195336706"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659211482943586305",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659211482943586305"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659630310269792256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659630310269792256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659246114342834176",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659246114342834176"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659384671984304128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659384671984304128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659620034329690112",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659620034329690112"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659670049316298752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659670049316298752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659685018103595011",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659685018103595011"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659706850600787974",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659706850600787974"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659709362712064001",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659709362712064001"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659276706853822464",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659276706853822464"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659658876755517450",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659658876755517450"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658646908947271680",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658646908947271680"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1659619988515241993",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1659619988515241993"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1658930657089802242",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1658930657089802242"
  }
]
```

## Grok response

```text
**Here is a complete compilation of all relevant X (Twitter) posts from the searched results matching the criteria (posts between 2023-05-14 and 2023-05-20 inclusive, focused on Charlie Kirk or TPUSA/ Turning Point USA public speaking events, appearances, tours, or where Charlie Kirk will speak). No summarization has been applied—full post content, metadata, and context are included as returned by the tools. Irrelevant or off-topic posts (e.g., unrelated tours or non-TPUSA events) have been filtered out based on the query.**

### Posts from Keyword and Semantic Searches:

- **[post:5] ID: 1659623224811094016**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 19 May 2023 18:13:05 GMT  
  Content: CONFIRMED #YWLS2023 SPEAKER: @RaeLynn 💖🤠  
  Register for the country’s BIGGEST event for conservative women today: https://t.co/86vbXokIfn  
  (Media: photo of speaker announcement)  
  Engagement: Likes=46, Reposts=11, Quotes=0, Replies=0, Bookmarks=0, Views=7729

- **[post:7] ID: 1659621221338628105**  
  Author: Daniel G. Amen, M.D. (@DocAmen)  
  Timestamp: Fri, 19 May 2023 18:05:08 GMT  
  Content: Upcoming event with special guest Dr. Daniel Amen! Join Charlie Kirk and Dr. Amen on Wednesday, June 7th, 2023 at Dream City Church. @charliekirk11  
  Sign Up: https://t.co/FnyiFXsYFr  
  More Info: https://t.co/TVVvaMQjYC  
  (Media: photo of event promo)  
  Engagement: Likes=7, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=1948

- **[post:8] ID: 1659246114342834176**  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Thu, 18 May 2023 17:14:35 GMT  
  Content: PASTORS, if you are ready to hear more of this 🔥 fire truth, then register for The Pastor's Summit T.O.D.A.Y!  
  @REVWUTRUTH will be one of the amazing speakers during this event on May 24-26, 2023, in Nashville, TN & you DON'T want to miss out! Register today -https://t.co/ET9f6YUihD  
  .  
  #tpusafaithsummit #thepastorssummit2023 #christianpastor #johnamanchukwu  
  (Media: video of speaker)  
  Engagement: Likes=10, Reposts=4, Quotes=1, Replies=0, Bookmarks=0, Views=478

- **[post:12] ID: 1659567450386747393**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 19 May 2023 14:31:28 GMT  
  Content: At our big Turning Point summer event we will be inviting all the FBI whistleblowers to speak. We will use it a chance to pay them for their time so they can feed their families and also give you a chance to support these brave patriots.  
  Engagement: Likes=2829, Reposts=667, Quotes=25, Replies=158, Bookmarks=7, Views=137363

- **[post:25] ID: 1659567450386747393** (duplicate of above in results)  
  Same as [post:12].

- **[post:26] ID: 1659315462289670145**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 18 May 2023 21:50:09 GMT  
  Content: Kash Patel is a patriot who ensured FBI whistleblowers, who had their lives destroyed by their own government, were able to feed their families and keep a roof over their kids' heads. They weren't "bought and paid for" witnesses, many have lost everything to speak out.  
  Engagement: Likes=10921, Reposts=2489, Quotes=47, Replies=531, Bookmarks=40, Views=287014

- **[post:27] ID: 1659623224811094016** (duplicate of [post:5])  
  Same as above.

- **[post:28] ID: 1658243191248932864**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 15 May 2023 22:49:20 GMT  
  Content: CALLING ALL EDUCATORS: Turning Point Academy is proud to present EDUCATORS’ SUMMIT 2023 this June in Deerfield, IL! 📚📝  
  Educators of all subjects will walk away with renewed excitement for teaching students HOW TO THINK and the tools to do it.  
  Register today:  
  (Media: photo of event promo)  
  Engagement: Likes=62, Reposts=24, Quotes=4, Replies=6, Bookmarks=0, Views=10582

- **[post:39] ID: 1659621221338628105** (duplicate of [post:7])  
  Same as above.

- **[post:40] ID: 1659620034329690112**  
  Author: Amen Clinics (@Amen_Clinics)  
  Timestamp: Fri, 19 May 2023 18:00:25 GMT  
  Content: Upcoming event with special guest Dr. Daniel Amen! Join Charlie Kirk and Dr. Amen on Wednesday, June 7th, 2023 at Dream City Church. @charliekirk11  
  Registration Link: https://t.co/3LyRppOi7i  
  More Info: https://t.co/ZWZoNJWzhA  
  (Media: photo of event promo)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=1, Views=138

- **[post:43] ID: 1659246114342834176** (duplicate of [post:8])  
  Same as above.

- **[post:48] ID: 1659676534460801024**  
  Author: Cassidy Riley Smith (@cassidy_smith97)  
  Timestamp: Fri, 19 May 2023 21:44:55 GMT  
  Content: Such an inspiring lineup of women who were born “for such a time as this” 💕  
  There are still a few spots available to hear them speak at #YWLS2023 🪩  
  Register now ➡️ https://t.co/ukzmjDuffj  
  (Media: photo of lineup)  
  Engagement: Likes=8, Reposts=5, Quotes=0, Replies=0, Bookmarks=0, Views=536

- **[post:49] ID: 1659675468109414401**  
  Author: Morgonn McMichael Brown (@Morgonn)  
  Timestamp: Fri, 19 May 2023 21:40:41 GMT  
  Content: My FAVORITE event of the year is almost here #YWLS2023 be sure to register soon and use code ‘MORGONN’ for 50% off GA! I can’t wait to see all you ladies there 🪩💕 https://t.co/0ML5zuoaY2  
  (Media: photo of promo)  
  Engagement: Likes=7, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=1197

- **[post:50] ID: 1659659559156195339**  
  Author: Maggie Fuchs (@maggiefuchs9)  
  Timestamp: Fri, 19 May 2023 20:37:28 GMT  
  Content: Learn how to be a strong woman and look great while doing it at #YWLS2023 💅🏻💪🏼  
  Learn more ➡️ https://t.co/isrD1TOHCL  
  (Media: photo of promo)  
  Engagement: Likes=4, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=210

- **[post:51] ID: 1659623224811094016** (duplicate of [post:5]/[post:27])  
  Same as above.

- **[post:57] ID: 1659623224811094016** (duplicate)  
  Same as above.

- **[post:62] ID: 1659259783361495046**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 18 May 2023 18:08:54 GMT  
  Content: We're excited to hear from @RealDrGina at #YWLS2023 💖  
  Register today: https://t.co/86vbXokIfn  
  (Media: photo of promo)  
  Engagement: Likes=25, Reposts=5, Quotes=0, Replies=1, Bookmarks=1, Views=6177

**No direct posts from @charliekirk11 or @TPUSA in the date range explicitly announcing Charlie Kirk's personal speaking locations or campus events for May 14-20, 2023. Mentions of upcoming TPUSA events (YWLS2023, Educators’ Summit 2023, Pastor's Summit, and a June 2023 event with Charlie Kirk) reference future dates outside the immediate week but are included as they were posted in the range and relate to speaking events. No posts specified exact venues or dates for Charlie Kirk speaking in the queried week itself.**

All data from tool results is presented verbatim where relevant. No additional posts matched the exact criteria after filtering.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-05-14 to 2023-05-20**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-05-14 to 2023-05-20 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
