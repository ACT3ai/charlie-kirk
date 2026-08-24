---
unlisted: true
title: "Week 36 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W36"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-09-03 to 2022-09-09."
status: completed
hide_table_of_contents: true
---

# Week 36, 2022

- Date range: 2022-09-03 to 2022-09-09
- Queried at (UTC): 2026-08-24T19:02:45Z
- Model: grok-4.3
- API status: completed
- Response id: 4326f75a-c4dc-9a4e-9738-ddf6416e3697

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-09-03 to the end of the week 2022-09-09.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR rally OR campus) since:2022-09-03 until:2022-09-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR tour OR appearance) since:2022-09-03 until:2022-09-10 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak or be present",
      "limit": "10",
      "from_date": "2022-09-03",
      "to_date": "2022-09-10"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point\") (event OR tour OR speaking OR speak OR appearance OR rally OR \"will speak\" OR \"speaking at\" OR \"speaking in\" OR campus) since:2022-09-03 until:2022-09-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Iowa OR Tennessee OR Florida OR California OR \"Made in America\") since:2022-09-03 until:2022-09-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Free America Tour\" OR \"Made in America Tour\" (Charlie OR Kirk OR TPUSA) since:2022-09-03 until:2022-09-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-09-03 until:2022-09-10 (event OR tour OR speak OR speaking OR TPUSA)",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11) (tour OR event OR speaking OR speak OR \"will be\" OR appearance OR rally) since:2022-09-03 until:2022-09-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2022-09-03 until:2022-09-10 (tour OR event OR speaking OR \"Charlie Kirk\" OR free OR america)",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Free America Tour\" since:2022-09-03 until:2022-09-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Made in America Tour\" since:2022-09-03 until:2022-09-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-09-03 until:2022-09-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1568012268138528768"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1567558441476018178"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1567589791377620992"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1567248413376348167"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 58375,
  "input_tokens_details": {
    "cached_tokens": 40704
  },
  "output_tokens": 2420,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 60795,
  "num_sources_used": 0,
  "num_server_side_tools_used": 16,
  "cost_in_usd_ticks": 1162795500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 16,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 18991,
    "output_tokens": 1704
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/bennyjohnson/status/1568012268138528768",
    "start_index": 278,
    "end_index": 338,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1568012268138528768",
    "start_index": 1001,
    "end_index": 1050,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1567248413376348167",
    "start_index": 1458,
    "end_index": 1507,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1567558441476018178",
    "start_index": 1893,
    "end_index": 1942,
    "title": "4"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1567589791377620992",
    "start_index": 2249,
    "end_index": 2298,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/wku_tpusa/status/1567973787869630465",
    "start_index": 2760,
    "end_index": 2817,
    "title": "6"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/maggiefuchs9/status/1567972933418602496",
    "start_index": 3087,
    "end_index": 3147,
    "title": "7"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1567634350304542720",
    "start_index": 3537,
    "end_index": 3590,
    "title": "8"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/wku_tpusa/status/1567629075144900608",
    "start_index": 3955,
    "end_index": 4012,
    "title": "9"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/RickeyAdamJr/status/1567646187087331332",
    "start_index": 4444,
    "end_index": 4505,
    "title": "10"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/JordynAB716/status/1567920520955400194",
    "start_index": 4808,
    "end_index": 4868,
    "title": "11"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/WillardHixson/status/1567975574160941056",
    "start_index": 5334,
    "end_index": 5396,
    "title": "12"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/RonFilipkowski/status/1567921982288629760",
    "start_index": 5587,
    "end_index": 5650,
    "title": "13"
  }
]
```

## Grok response

```text
**All relevant X/Twitter posts from the specified date range (2022-09-03 to 2022-09-09, using searches up to 2022-09-10 to capture the full week) mentioning Charlie Kirk, TPUSA/Turning Point USA, or related events/speaking appearances are included below without summarization.**[[1]](https://x.com/bennyjohnson/status/1568012268138528768)

### Posts referencing TPUSA "Made in America Tour" (Benny Johnson on the tour; states mentioned: Iowa, Tennessee, Florida, California):
- **Post ID: 1568012268138528768** (2022-09-08 23:03:51 GMT, @bennyjohnson)  
  Content: "🚨 Come See Me on TOUR: Join me this month on the @TPUSA Made in America Tour in Iowa, Tennessee, Florida, and California — more dates and locations to be announced. I can’t wait to see you there 🇺🇸 TICKETS: https://t.co/l7maCF2bl6"  
  (Media: Photo of tour graphic.)  
  Thread reply (ID: 1568012665280159744, same author, 2022-09-08 23:05:26 GMT): "DATES 👇 See you there! https://t.co/l7maCF1Dvy"  
  (Media: Photo of dates graphic.)[[2]](https://x.com/i/status/1568012268138528768)

- **Post ID: 1567248413376348167** (2022-09-06 20:28:34 GMT, @ChrisOfWeavers)  
  Content: "Found it, they certainly have it listed, it was under Made in America Tour. https://events2022.tpusa.com/events/made-in-america-tour-at-nolensville-high-school"  
  (Media: Photo/screenshot of the event listing.)  
  (Context: Discussion of a TPUSA event at Nolensville High School under the Made in America Tour.)[[3]](https://x.com/i/status/1567248413376348167)

### Posts referencing TPUSA "Free America Tour" featuring Charlie Kirk (church events):
- **Post ID: 1567558441476018178** (2022-09-07 17:00:30 GMT, @TPUSA)  
  Content: "Turning Point USA is THRILLED to announce the Free America Tour featuring @charliekirk11, coming to a church near you! Get tickets now: https://t.co/wo0r22x0lP"  
  (Media: Photo graphic of the tour announcement.)[[4]](https://x.com/i/status/1567558441476018178)

- **Post ID: 1567589791377620992** (2022-09-07 19:05:05 GMT, @LifeChu28345609 / TPUSA Faith @ Life Church)  
  Content: "The Fall Launch of the Free America Tour with Charlie Kirk. Get your tickets now before they’re sold out! #freeamericatour #tpusa #tpusafaith @ Life Church-Noblesville"  
  (No media.)[[5]](https://x.com/i/status/1567589791377620992)

### Other TPUSA/chapter events mentioned (no direct Charlie Kirk speaking confirmed in these posts):
- **Post ID: 1567973787869630465** (2022-09-08 20:30:57 GMT, @wku_tpusa)  
  Content: "Our event will still be this Tuesday, September 13, at 6pm in DSU 2123! Show up and show Eventbrite they can’t censor conservative voices!"  
  (Context: WKU TPUSA chapter event, a watch party of "What is a Woman?"; references Eventbrite issues. Quoted a Daily Wire post.)[[6]](https://x.com/wku_tpusa/status/1567973787869630465)

- **Post ID: 1567972933418602496** (2022-09-08 20:27:33 GMT, @maggiefuchs9)  
  Content: "@eventbrite isn’t going to stop us from our watch party of #WhatIsAWoman . Follow @wku_tpusa for details about the event on Tuesday!"  
  (Context: Same WKU TPUSA chapter event.)[[7]](https://x.com/maggiefuchs9/status/1567972933418602496)

- **Post ID: 1567634350304542720** (2022-09-07 22:02:09 GMT, @TPUSA)  
  Content: "EXCLUSIVE: Eventbrite Removes TPUSA Chapter’s Listing for Event Watch Party of @MattWalshBlog’s “What is a Woman” Read more: https://tpusa.com/live/exclusive-eventbrite-removes-tpusa-chapters-listing-for-event-watch-party-of-matt-walshs-what-is-a-woman/"  
  (Context: General TPUSA chapter event issues.)[[8]](https://x.com/TPUSA/status/1567634350304542720)

- **Post ID: 1567629075144900608** (2022-09-07 21:41:11 GMT, @wku_tpusa)  
  Content: "We will not let EventBrite stop us from sharing and promoting our ideas. Our event will still be happening. https://tpusa.com/live/exclusive-eventbrite-removes-tpusa-chapters-listing-for-event-watch-party-of-matt-walshs-what-is-a-woman/"  
  (Context: Same WKU chapter event.)[[9]](https://x.com/wku_tpusa/status/1567629075144900608)

- **Post ID: 1567646187087331332** (2022-09-07 22:49:11 GMT, @RickeyAdamJr)  
  Content: "Back at it with *NEW* graphics complements of @TPUSA the University of Arkansas would like to invite anyone and everyone to attend their @conservmillen event! Apply for tickets at - https://t.co/3iUh7Txcsw @tpusastudents changing the world 🇺🇸"  
  (Media: Photo of event graphic; University of Arkansas TPUSA/conservative millennial event.)[[10]](https://x.com/RickeyAdamJr/status/1567646187087331332)

- **Post ID: 1567920520955400194** (2022-09-08 16:59:17 GMT, @JordynAB716)  
  Content: "IOWA!! Remember to get your FREE tickets this event!! 🤩🤩 https://t.co/W7eDNeY1xc @bennyjohnson @HayleySenne @tpusastudents @TPUSA"  
  (Media: Photo of event graphic; Iowa TPUSA-related event with Benny Johnson.)[[11]](https://x.com/JordynAB716/status/1567920520955400194)

### Posts mentioning Charlie Kirk or TPUSA events in passing (no specific new speaking dates/locations):
- **Post ID: 1567975574160941056** (2022-09-08 20:38:03 GMT, @WillardHixson)  
  Content: "Is Jack and Charlie Kirk still searching for the nazis that showed up at the TPUSA event? They talked a big game about it, but I hear an antifa group beat them to the punch and doxed those nazi losers. 🤣"  
  (Context: References a past TPUSA event with Charlie Kirk.)[[12]](https://x.com/WillardHixson/status/1567975574160941056)

- **Post ID: 1567921982288629760** (2022-09-08 17:05:05 GMT, @RonFilipkowski)  
  Content: [Video clip of Charlie Kirk speaking about Steve Bannon and related topics; no new event details.][[13]](https://x.com/RonFilipkowski/status/1567921982288629760)

No posts from @charliekirk11 in the date range directly announced or detailed his own speaking events/tours (his activity focused on other topics like politics, crime, and his book). No other specific dates, locations, or speaking appearances for Charlie Kirk or TPUSA were found in the searched posts matching the criteria. All available data from the tool results is listed above.
```

