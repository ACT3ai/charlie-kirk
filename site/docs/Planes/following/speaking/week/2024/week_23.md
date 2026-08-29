---
unlisted: true
title: "Week 23 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W23"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-06-03 to 2024-06-09."
status: completed
hide_table_of_contents: true
---

# Week 23, 2024

- Date range: 2024-06-03 to 2024-06-09
- Queried at (UTC): 2026-08-24T19:13:37Z
- Model: grok-4.3
- API status: completed
- Response id: 0f275be8-5c1c-93cc-9cb4-8b9951263f95

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-06-03 to the end of the week 2024-06-09.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"will be\" OR appearing OR appearance) since:2024-06-03 until:2024-06-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR tour) (June OR \"June 3\" OR \"June 4\" OR \"June 5\" OR \"June 6\" OR \"June 7\" OR \"June 8\" OR \"June 9\" OR \"this week\") since:2024-06-03 until:2024-06-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between June 3 and June 9 2024",
      "limit": "10",
      "from_date": "2024-06-03",
      "to_date": "2024-06-10"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearing OR \"will be\" OR appearance) since:2024-06-03 until:2024-06-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR \"Charlie Kirk\") since:2024-06-03 until:2024-06-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1799572498167599260"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1798029988152963212"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1797654915525079129"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1799209962016780354"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1799084540113097088"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Young Women’s Leadership Summit\" OR YWLS OR \"People’s Convention\" OR \"Peoples Convention\") (TPUSA OR \"Turning Point\" OR Kirk) since:2024-06-03 until:2024-06-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Freedom Night\" OR \"Freedom Night in America\") (Dream City OR TPUSA OR Kirk) since:2024-06-03 until:2024-06-10",
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
  "input_tokens": 28346,
  "input_tokens_details": {
    "cached_tokens": 13312
  },
  "output_tokens": 7039,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 35385,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 990524000,
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
    "input_tokens": 16454,
    "output_tokens": 6501
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799200393450172637",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799200393450172637"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799588591858827636",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799588591858827636"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799221746001719637",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799221746001719637"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799143975820959893",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799143975820959893"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798731019237110193",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798731019237110193"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798851685055672655",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798851685055672655"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798223634798092589",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798223634798092589"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799232192104812553",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799232192104812553"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799249223223013719",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799249223223013719"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799564894397739513",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799564894397739513"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799532970564517906",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799532970564517906"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1797607260371529800",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1797607260371529800"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799579194378371168",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799579194378371168"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799545150114312533",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799545150114312533"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798924693233385832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798924693233385832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799538734754619771",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799538734754619771"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799205777606951021",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799205777606951021"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798827539676463120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798827539676463120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799587070848926129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799587070848926129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799572498167599260",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799572498167599260"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798520789488349663",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798520789488349663"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799540758619341044",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799540758619341044"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799494340462707106",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799494340462707106"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798805206018466111",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798805206018466111"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798029988152963212",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798029988152963212"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799533155424039234",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799533155424039234"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799209962016780354",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799209962016780354"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799500990930137347",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799500990930137347"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799573922838655044",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799573922838655044"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799198564674920786",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799198564674920786"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799516585800921576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799516585800921576"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1797667855258837230",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1797667855258837230"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798353713137918161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798353713137918161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799578761614311601",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799578761614311601"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799530063505088724",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799530063505088724"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1797851655859564649",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1797851655859564649"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799515492639453184",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799515492639453184"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799084540113097088",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799084540113097088"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1797654915525079129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1797654915525079129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799576456298639787",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799576456298639787"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799534758105641167",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799534758105641167"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1798770747122520319",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1798770747122520319"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1799208513639748013",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1799208513639748013"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1797736921864778033",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1797736921864778033"
  }
]
```

## Grok response

```text
**Here is all relevant X (Twitter) data from posts between June 3, 2024, and June 9, 2024 (inclusive of the date range up to 2024-06-09, with some posts referencing events through June 10 for context).** I have included full post details, content, authors, timestamps, engagement, media where present, and threads/replies where fetched. No summarization—raw data only.

### 1. TPUSA Young Women’s Leadership Summit (YWLS 2024) – San Antonio (ongoing June 7–9, 2024)
- **Post [post:32]** (from thread fetch of @TPUSAEvents post):  
  ID: 1799572498167599260  
  Author: TPUSA Events (@TPUSAEvents)  
  Timestamp: Sat, 08 Jun 2024 22:41:32 GMT  
  Content: “It makes no sense to prioritize career over marriage.” @SuzanneVenker  
  #TPUSAEVENTS #YWLS2024  
  Engagement: Likes=1, Reposts=0, Quotes=1, Replies=1, Bookmarks=0, Views=1533  
  (Referenced in [post:3] by @MatthewBoedy on Sat, 08 Jun 2024 22:57:16 GMT, noting messages at the event including hiring and homemaking themes.)

- **Post [post:3]** (mentions YWLS):  
  ID: 1799576456298639787  
  Author: Matthew Boedy (@MatthewBoedy)  
  Timestamp: Sat, 08 Jun 2024 22:57:16 GMT  
  Content: Let me sum up the messages women are getting at the Turning Point USA event this weekend: 1) Candace Owens, podcast host, formerly of Daily Wire: Homemaking is great 2) TPUSA: We are hiring. Expedited interviews today! 3) This radio host (and Phyllis Schlafly’s niece) 👇🏽  
  (Quotes [post:32])

- **Post [post:5]** (mentions YWLS Day 2 speakers):  
  ID: 1799564894397739513  
  Author: OrlandoMike911 (@OrlandoMike911)  
  Timestamp: Sat, 08 Jun 2024 22:11:19 GMT  
  Content: Watch Live: Riley Gaines, Alina Habba, More Speak at TPUSA Young Women‘s Leadership Summit Day 2 https://t.co/z0hjaGUJqb via @BreitbartNews  
  This was great today!  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=13

- **Post [post:37]** (YWLS Day 2):  
  ID: 1799564894397739513 (same as above)

- **Post [post:38]** (YWLS speakers):  
  ID: 1799545150114312533  
  Author: Tegan🇺🇸 (@HoldTheLine24)  
  Timestamp: Sat, 08 Jun 2024 20:52:52 GMT  
  Content: "It's heartbreaking to see what's happening" @sav_says reminds Americans that Biden is LYING to you about the state of our country as children are being exploited  
  Watch TPUSA's Young Women's Leadership Summit here! https://t.co/u5x3sATxLV

- **Post [post:39]** (YWLS speakers):  
  ID: 1799538734754619771  
  Author: UnfilteredAmerica (@NahBabyNahNah)  
  Timestamp: Sat, 08 Jun 2024 20:27:22 GMT  
  Content: Watch Live: Charlie Kirk, Lara Trump, and Megyn Kelly Speak at TPUSA Young Women‘s Leadership Summit: Charlie Kirk, Alex Clark, Lara Trump, and Megyn Kelly will speak on the first day of the 2024 TPUSA Young Women's Leadership… https://t.co/nzcPaRiKLz #Trump2024 #NahBabyNah  
  Media: 1 photo

- **Post [post:40]** (YWLS Day 2 update):  
  ID: 1799532970564517906  
  Author: Patriot Mobile 🇺🇸 (@PatriotMobile)  
  Timestamp: Sat, 08 Jun 2024 20:05:12 GMT  
  Content: Day 2 of the @TPUSA Young Women’s Leadership Summit is halfway over and the energy is electric! We've already heard from incredible speakers @AlinaHabba, @Riley_Gaines_, and so many inspiring conservative women encouraging attendees to stand up for themselves, be informed when it comes to their health, and take an active role in shaping the future of our nation.  
  Don't forget to visit Patriot Mobile's booth for a chance to win free AirPods. Let's make this a YWLS to remember!  
  #YWLS2024 | #TakeBackFemininity  
  Media: 4 photos

- **Post [post:41]** (YWLS link):  
  ID: 1799530063505088724  
  Author: monire nadjafli (@monirenadjafli5)  
  Timestamp: Sat, 08 Jun 2024 20:04:28 GMT  
  Content: WOMAN S RIGHTS= CHILDREN S RIGHTS= GOOD NEWS GOOD LUCK LADIES  
  Watch Live: Charlie Kirk, Lara Trump, and Megyn Kelly Speak at TPUSA Young Women‘s Leadership Summit https://www.breitbart.com/politics/2024/06/07/watch-live-charlie-kirk-lara-trump-and-megyn-kelly-speak-at-tpusa-young-womens-leadership-summit/ via @BreitbartNews

- **Post [post:43]** (YWLS link):  
  ID: 1799516585800921576  
  Author: conservativegallt (@NervousCook)  
  Timestamp: Sat, 08 Jun 2024 18:59:22 GMT  
  Content: Watch Live: Charlie Kirk, Lara Trump, and Megyn Kelly Speak at TPUSA Young Women’s Leadership Summit https://www.breitbart.com/politics/2024/06/07/watch-live-charlie-kirk-lara-trump-and-megyn-kelly-speak-at-tpusa-young-womens-leadership-summit/

- **Post [post:44]** (YWLS speakers):  
  ID: 1799515492639453184  
  Author: Real America's Voice (RAV) (@RealAmVoice)  
  Timestamp: Sat, 08 Jun 2024 18:55:01 GMT  
  Content: "It's heartbreaking to see what's happening" @savsays reminds Americans that Biden is LYING to you about the state of our country as children are being exploited  
  Watch TPUSA's Young Women's Leadership Summit here! https://rumble.com/v50dcjw-young-womens-leadership-summit-ywls-2024.html  
  Media: 1 video

- **Post [post:28]** (TPUSA account on YWLS):  
  ID: 1799249223223013719  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Sat, 08 Jun 2024 01:16:57 GMT  
  Content: Charlie Kirk on breaking the stigma around people who want to have large families: "Big families are never lacking in purpose, they are never lacking in direction, and they are never bored." @charliekirk11 #YWLS2024  
  Media: 1 video

- **Post [post:29]** (TPUSA account on YWLS):  
  ID: 1799232192104812553  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Sat, 08 Jun 2024 00:09:17 GMT  
  Content: Candace Owens on Harrison Butker: "I was blessed to hear him speak a couple of weeks ago... and Harrison said, 'the more masculine I became, the more feminine my wife became.' And I thought that was such a beautiful way to say things." @RealCandaceO #YWLS2024  
  Media: 1 video

- **Post [post:30]** (TPUSA account on YWLS):  
  ID: 1799205777606951021  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 07 Jun 2024 22:24:19 GMT  
  Content: "Once this (event) wraps up, you and I will both be slandered by the left-wing media as radical extremists." @realalexclark #YWLS2024  
  Media: 1 video

- **Post [post:31]** (TPUSA account on YWLS live):  
  ID: 1799198564674920786  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 07 Jun 2024 21:55:39 GMT  
  Content: YWLS IS LIVE: Watch Charlie Kirk, Alex Clark, Candace Owens, Megyn Kelly + MORE! #YWLS2024  
  https://rumble.com/v50936f-ywls-is-live-charlie-kirk-alex-clark-candace-owens-and-lara-trump-ywls2024.html

- **Post [post:36]** (YWLS attendee post):  
  ID: 1799587070848926129  
  Author: Lacey Nagao (@lacenagao)  
  Timestamp: Sat, 08 Jun 2024 23:39:27 GMT  
  Content: Seeing all the little babies and daughters here with their moms at YWLS is the absolute best thing ever. I’m so grateful to live the best of both worlds. Thank you @tpaction and @TPUSA for always allowing us to put family first and being a huge advocate of mothers. Being here again with my own daughter is extra special.  
  Media: 3 photos

### 2. Chase the Vote Town Hall with President Trump – Phoenix, AZ (Dream City Church, June 6, 2024)
- **Post [post:45]** (Charlie Kirk announcement):  
  ID: 1797654915525079129  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 03 Jun 2024 15:41:45 GMT  
  Content: I am honored to announce that Turning Point PAC with @tpaction will be hosting “Chase the Vote: A TOWN HALL with Special Guest President Donald J. Trump” this Thursday, June 6, in Phoenix, AZ. President Trump will be taking questions directly from AZ voters in the heart of Maricopa County, one of the most critical in the entire country. Join us at  
  Media: 1 photo  
  Engagement: Likes=3667, Reposts=1105, Quotes=68, Replies=264, Bookmarks=77, Views=425862  
  Replies include: @MAHA_TANK ("Phoenix. Show up and support Charlie..."), @FFT1776 ("HUGE!!! Can’t wait!!!"), @npagnotta1776 ("I STAND WITH TRUMP! 🇺🇸")

- **Post [post:10]** (event details):  
  ID: 1798353713137918161  
  Author: Stacy (@SickofBS_)  
  Timestamp: Wed, 05 Jun 2024 13:58:31 GMT  
  Content: Turning Point Action hosts "Chase the Vote - A Town Hall with President Donald J. Trump" with Charlie Kirk at Dream City Church in Phoenix, Arizona. RSBN will have full coverage of this special event on Thursday, June 6, 2024, starting at approximately 2:00 p.m. ET. The event will begin at 4:00 p.m. ET. https://t.co/6jPBsyi8CX  
  Thank you @harris_loving for continuing to fight💥👊 and supporting @MikeGil21446788  
  Media: 1 photo  
  (Quotes [post:10] from @harris_loving: "Look who’s coming to Arizona this Thursday!!!❤️❤️❤️🇺🇸 https://www.tpaction.com/townhall")

- **Post [post:8]** (Trump speaking at event):  
  ID: 1798851685055672655  
  Author: 'Merican Grit (@MericanGrit)  
  Timestamp: Thu, 06 Jun 2024 22:57:17 GMT  
  Content: Watch Live: Donald Trump Speaks at Turning Point Action Town Hall Event: Former President Donald Trump will participate in a town hall event held by Turning Point Action with Charlie Kirk in Phoenix, Arizona, on Thursday, June 6. The post… https://t.co/4zKm2bwYhg #Trump2024  
  Media: 1 photo

- **Post [post:9]** (event timing):  
  ID: 1798805206018466111  
  Author: Deborah Lloyd (@Deborah19937878)  
  Timestamp: Thu, 06 Jun 2024 19:52:35 GMT  
  Content: PRESIDENT TRUMP TO SPEAK 5 PM EST Turning Point Action hosts "Chase the Vote - A Town Hall with President Donald J. Trump" with Charlie Kirk at Dream City Church in Phoenix, Arizona. RSBN will have full coverage of this special event on Thursday, June 6, 2024, starting at approximately 3:00 p.m. ET. The event will begin at 5:00 p.m. ET.  
  Media: 1 photo

- **Post [post:18]** (event details):  
  ID: 1798223634798092589  
  Author: TheRealThelmaJohnson (@TheRealThelmaJ1)  
  Timestamp: Wed, 05 Jun 2024 05:21:38 GMT  
  Content: Dream City Church in Phoenix where Trump will be appearing Thursday has an auditorium that holds 3600 people. They're an Evangelical cult so I expect most of those seats to be filled with Church members. The MAGA politicians here fight to polish Trump's mushroom, I expect all will be there including every fake elector and Trump endorsed losers Kari Lake and Abe Hamadeh. Arizona only gets a few visits a year. This event is sponsored by Turning Point Action, so this is a Charlie Kirk event. It is billed as a 'town hall' but I assume Charlie will be writing the questions and teleprompting the answers to try to keep Crazy Uncle Rico on track. I'm sure he'll still say the same crazy stuff as always.  
  Media: 1 photo

- **Post [post:25]** (Trump at Dream City Church):  
  ID: 1797736921864778033  
  Author: TheRealThelmaJohnson (@TheRealThelmaJ1)  
  Timestamp: Mon, 03 Jun 2024 21:07:37 GMT  
  Content: Donald Trump is coming back to Phoenix June 6 at Dream City Church. That place is right down the road from me. It's a grifting cult and has a million ties to Charlie Kirk. How these people don't pay taxes I will never know. This will be the 4th time Trump has been scheduled to speak and the second time he appeared there I think.  
  Media: 1 photo

- **Post [post:24]** (Trump appearance):  
  ID: 1798731019237110193  
  Author: .. (@OperDJT)  
  Timestamp: Thu, 06 Jun 2024 14:57:48 GMT  
  Content: President Trump will be appearing at the Dream City Church in Phoenix, AZ for a Town Hall this afternoon. This is the first campaign event since verdict. Charlie Kirk @charliekirk11 decided not to promote this event that he’s hosting today.  
  Media: 1 photo

- **Post [post:23]** (invitation to event):  
  ID: 1797851655859564649  
  Author: @DAVIDXRPLION (@DavidXRPLion)  
  Timestamp: Tue, 04 Jun 2024 04:43:31 GMT  
  Content: Dave XRPLion Got The "SPECIAL INVITATION" To Be In The House w/ CHARLIE KIRK ON WEDNESDAY NIGHT (6/5/24) & THURSDAY NIGHT (6/6/24) WITH OUR CIC - PRESIDENT DONALD TRUMP. HALLELUJAH!  
  Media: 1 photo

- **Post [post:26]** (Kari Lake on Charlie Kirk Show at event):  
  ID: 1798770747122520319  
  Author: Kari Lake (@KariLake)  
  Timestamp: Thu, 06 Jun 2024 17:35:40 GMT  
  Content: 🚨 LIVE NOW: @KariLake joins The Charlie Kirk Show! TUNE IN: https://rumble.com/v4zyo0c-live-at-donald-trump-swamp-the-vote-rally-in-az-lake-rep.-biggs-live-6.6.24.html  
  Media: 1 photo

- **Post [post:21]** (Charlie Kirk post-event):  
  ID: 1798827539676463120  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 06 Jun 2024 21:21:20 GMT  
  Content: Absolutely PACKED house at the Turning Point PAC “Chase the Vote Town Hall with special guest President Donald J. Trump.” Thousands more outside. The energy is insane!! WATCH LIVE 👇 https://t.co/likVheBjY3  
  Media: 1 photo  
  Engagement: Likes=3683, Reposts=841, Quotes=13, Replies=150, Bookmarks=29, Views=184449

- **Post [post:20]** (Charlie Kirk recap):  
  ID: 1799084540113097088  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 07 Jun 2024 14:22:34 GMT  
  Content: Just wrapped up our successful Chase the Vote Trump Town Hall in Phoenix with 4,000 people… Heading to San Antonio this morning for our Young Women’s Leadership summit with 2,500 young leaders and Megyn Kelly, Lara Trump, Riley Gaines, Candace Owens and more… And then onto Detroit for The People’s Convention with thousands of patriots, President Trump, Vivek Ramaswamy, Dr. Ben Carson, Tulsi Gabbard, and many more. We have a country to save!! Onward 🇺🇸  
  Media: 1 photo  
  Engagement: Likes=3210, Reposts=509, Quotes=13, Replies=131, Bookmarks=26, Views=115644  
  Replies include: @DefenderZionist, @FFT1776, @paulkeres155

- **Post [post:6]** (Trump event in Phoenix):  
  ID: 1799540758619341044  
  Author: Feisty is proud to be a Democrat! (@FeistyLibLady)  
  Timestamp: Sat, 08 Jun 2024 20:35:25 GMT  
  Content: On June 6 Donald Trump was an event in Phoenix hosted right-wing extremist, Charlie Kirk. Yes, the very same Charlie Kirk who said, “we made a huge mistake when we passed the Civil Rights Act.” Trump who brags about his Latino support called former Maricopa County sheriff Joe Arpaio to the stage. Trump gave him a hug and a kiss. Arpaio called Trump “the only hero I ever had in his life.” Trump pardoned Arpaio for contempt of court relating to Arpaio's racial profiling and abusive treatment of migrants in Arizona. Yes, a few Latino's may support Trump but once they found out he still is hugging and kissing Joe Arpaio, they should be running far away from him. Trump is a liar, a fake and a felon. #BidenHarris4More #DemsUnited  
  Media: 1 photo  
  Engagement: Likes=247, Reposts=130, Quotes=6, Replies=11, Bookmarks=3, Views=4639

- **Post [post:27]** (Trump town hall announcement):  
  ID: 1797667855258837230  
  Author: Mario Nawfal (@MarioNawfal)  
  Timestamp: Mon, 03 Jun 2024 16:33:10 GMT  
  Content: 🚨🇺🇸 BREAKING: TRUMP TO HOLD TOWN HALL IN ARIZONA He will appear on June 6 at Dream City Church in Phoenix to take questions from voters. Source: @charliekirk11  
  Media: 1 photo  
  Engagement: Likes=199, Reposts=42, Quotes=3, Replies=28, Bookmarks=3, Views=36569

- **Post [post:12]** (DJT schedule mention):  
  ID: 1797607260371529800  
  Author: CJB 🇺🇲 (@thatguyCJB)  
  Timestamp: Mon, 03 Jun 2024 12:32:23 GMT  
  Content: DJT schedule for June as of 6/3/24. NOTE: He's giving one speech at the TPUSA event, the specific day is unclear as of rn.  
  Media: 1 photo

### 3. Freedom Night in America – Dream City Church, Phoenix (June 5, 2024)
- **Post [post:33]** (from thread fetch):  
  ID: 1798029988152963212  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Tue, 04 Jun 2024 16:32:09 GMT  
  Content: The world has ALWAYS been better because of Christians. 🔥 📆 Join us THIS Wednesday, June 5 at 6:30 pm at Dream City Church as we hear from @charliekirk11 & @conservmillen 🎟 Register for this FREE event. - https://tpusafaith.com/register-for-freedom-night/?utm_source=Social+Media&utm_medium=Social+Media&utm_campaign=FNIA+launch  
  Media: 1 video  
  Engagement: Likes=4, Reposts=1, Quotes=1, Replies=2, Bookmarks=0, Views=770  
  Replies: @CherylCWS1, @OCrabeyes

- **Post [post:46]** (post-event):  
  ID: 1799200393450172637  
  Author: Dream City Church (@dreamcitychurch)  
  Timestamp: Fri, 07 Jun 2024 22:02:55 GMT  
  Content: We had an amazing turnout at Freedom Night in America with @charliekirk1776 and @alliebstuckey 🇺🇸🦅 1/3  
  Media: 1 photo

- **Post [post:47]** (event reference):  
  ID: 1798924693233385832  
  Author: YancyFaith (@YancyFaith)  
  Timestamp: Fri, 07 Jun 2024 03:47:23 GMT  
  Content: Looks like the Trump - TPUSA rally was supposed to be held last night, not tonight. Freedom Night – Dream City Church https://www.dreamcitychurch.us/series/freedom-night-in-america/

### 4. The People’s Convention (upcoming, referenced in range; June 15+ but previewed)
- **Post [post:7]** / **[post:34]** (Tulsi Gabbard speaking):  
  ID: 1799209962016780354  
  Author: *Heidi*DivineJustice*MissionEarth⚡🙏🇺🇸👼🐺🦁🕊️☄ (@quantify88faith)  
  Timestamp: Fri, 07 Jun 2024 22:40:57 GMT  
  Content: 🙏🇺🇸🎖️~Yes, I am voting for Trump, no matter who his VP is... We Patriots should be learning from each other, not just fighting~😔 Tulsi will also be speaking at this @TPUSA Peoples Convention, on June 15th~ ☄️  
  Media: 1 photo  
  (In reply thread to another post)

- **Post [post:20]** (Charlie Kirk preview): Includes "And then onto Detroit for The People’s Convention with thousands of patriots, President Trump, Vivek Ramaswamy, Dr. Ben Carson, Tulsi Gabbard, and many more."

### 5. Other/General Mentions of Charlie Kirk/TPUSA Events or Speaking (within date range, no specific new events)
- **Post [post:0]** (general comment):  
  ID: 1799588591858827636  
  Author: Greg (@jackpotdreamer)  
  Timestamp: Sat, 08 Jun 2024 23:45:29 GMT  
  Content: People like Charlie Kirk have tunnel vision. They believe by supporting Convict Trump they will be able to force other Americans to live & believe as they do. They don’t think about the existential consequences of a Fascist Dictator or making him follow through on these promises.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=83

- **Post [post:1]** (general):  
  ID: 1799579194378371168  
  Author: George Nemeh (@GeorgeNemeh)  
  Timestamp: Sat, 08 Jun 2024 23:08:09 GMT  
  Content: I was very happy to hear President Trump & Charlie Kirk & Steve Bannon speaking exactly what I have been saying for the last 5 years!! Kudos. My rant’s did work. Thx 🙏George

- **Post [post:2]** (general):  
  ID: 1799578761614311601  
  Author: MAAP REAL TALK SHOW (@MaapReal)  
  Timestamp: Sat, 08 Jun 2024 23:06:25 GMT  
  Content: I was very happy to hear President Trump & Charlie Kirk & Steve Bannon speaking exactly what I have been saying for the last 5 years!! Kudos. George

- **Post [post:4]** (general):  
  ID: 1799573922838655044  
  Author: Larry (@Larry0033150515)  
  Timestamp: Sat, 08 Jun 2024 22:47:12 GMT  
  Content: Speak for yourself, Charlie!

- **Post [post:13]** (Charlie Kirk post, not event-specific):  
  ID: 1799534758105641167  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sat, 08 Jun 2024 20:11:34 GMT  
  Content: Hundreds of Trump supporters line the streets of Newport Beach as Donald Trump caps off his three-day California fundraiser tour. This last stop is at John and Kimberly Word’s Harbor Island home, hosted jointly hosted with tech entrepreneur Palmer Luckey. Tickets range from $3,300 to $100,000.  
  Media: 1 video

- **Post [post:14]** (Charlie Kirk post):  
  ID: 1799500990930137347  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sat, 08 Jun 2024 17:57:24 GMT  
  Content: Only compared to the French Laundry event no one will ever forget.

- **Post [post:15]** (Charlie Kirk post):  
  ID: 1799494340462707106  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sat, 08 Jun 2024 17:30:58 GMT  
  Content: November will be a referendum on: Endless war Open borders Inflation Crime Democrats want to distract you with phony trials, fear mongering about Christians and white rural rage, and the “death of democracy” which they themselves are advancing. Stay focused on the core four.

- **Post [post:16]** (Charlie Kirk post):  
  ID: 1799221746001719637  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 07 Jun 2024 23:27:46 GMT  
  Content: Lara Trump 🚨🚨🚨 “We are in a very, very bad place as a country and as the world right now. But because of what has happened, I believe this will be a landslide election for Donald Trump and Republicans” @LaraLeaTrump  
  Media: 1 video

- **Post [post:17]** (Charlie Kirk post):  
  ID: 1799143975820959893  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 07 Jun 2024 18:18:44 GMT  
  Content: According to the Live TikTok Follower Count of President Trump v Biden-Harris HQ, Trump has 5.5 million more followers. 2012 was the Facebook election. 2016 was the Twitter election. 2020 was the Instagram election. 2024 will be the 𝕏/TikTok election.  
  Media: 1 photo

- **Post [post:42]** (general YWLS-related discussion):  
  ID: 1799520789488349663 (in thread)  
  Author: TrashDiscourse (@TrashDiscourse)  
  Timestamp: Sat, 08 Jun 2024 19:52:55 GMT  
  Content: And apparently sent an intern to spy on her at the YWLS @TPUSA  
  (Quotes post about Candace Owens)

- **Post [post:22]** (unrelated Trump event):  
  ID: 1798520789488349663  
  Author: Laura H. (@LauraHa00527137)  
  Timestamp: Thu, 06 Jun 2024 01:02:25 GMT  
  Content: I'm going to see him on Sunday, June 9th for freeeeeee! He's having a rally at Sunset Park in Las Vegas. It's going to be hot, but we are providing misting stations, cooling tents and water. It's Vegas Baby!🇺🇸🇺🇸🇺🇸

All data pulled directly from tool results. No additional events or speaking appearances by Charlie Kirk or TPUSA were identified in the specified date range beyond those listed.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-06-03 to 2024-06-09**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-06-07](/Planes/Incidents/N582MM-2024-06-07-KSAT) | [N582MM](/Planes/N582MM/overview) | [KSAT](/Planes/Airports/KSAT) | San Antonio, TX | Charlie | **Same day** |
| [2024-06-08](/Planes/Incidents/N582MM-2024-06-08-KSAT) | [N582MM](/Planes/N582MM/overview) | [KSAT](/Planes/Airports/KSAT) | San Antonio, TX | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
