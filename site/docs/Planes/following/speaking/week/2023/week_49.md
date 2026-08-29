---
unlisted: true
title: "Week 49 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W49"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-12-03 to 2023-12-09."
status: completed
hide_table_of_contents: true
---

# Week 49, 2023

- Date range: 2023-12-03 to 2023-12-09
- Queried at (UTC): 2026-08-24T19:10:27Z
- Model: grok-4.3
- API status: completed
- Response id: 821fb251-9d74-9c46-be62-5edb358cb932

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-12-03 to the end of the week 2023-12-09.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR \"at\" OR campus OR university) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:RealCharlieKirk (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, where Charlie will speak or be speaking this week December 2023",
      "limit": "10",
      "from_date": "2023-12-03",
      "to_date": "2023-12-09"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR AmFest OR AMFEST OR #AmFest2023 OR #AMFEST2023) (event OR speaking OR speak OR tour OR appearance OR campus OR university OR \"will speak\" OR \"will be speaking\" OR \"speaking at\" OR \"at\" OR Phoenix OR Arizona) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"AmFest\" OR AMFEST OR #AmFest2023) (Phoenix OR Arizona OR \"next week\" OR \"Dec\" OR December) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (AmFest OR AMFEST OR #AmFest2023 OR Phoenix OR Arizona OR event) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (AmFest OR AMFEST OR #AmFest2023 OR Phoenix OR Arizona OR event) since:2023-12-03 until:2023-12-10",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSAEvents since:2023-12-03 until:2023-12-10",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "locations and dates for Charlie Kirk speaking events or TPUSA events in December 2023 especially AmFest or campus events",
      "limit": "10",
      "from_date": "2023-12-03",
      "to_date": "2023-12-09"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 27700,
  "input_tokens_details": {
    "cached_tokens": 11072
  },
  "output_tokens": 5557,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 33257,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 918919000,
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
    "input_tokens": 18041,
    "output_tokens": 4872
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733170503492268314",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733170503492268314"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732817355988935137",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732817355988935137"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733164535627022611",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733164535627022611"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733250773188805118",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733250773188805118"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731704106517926355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731704106517926355"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732173445637775674",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732173445637775674"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731710332060766345",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731710332060766345"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733181763923689971",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733181763923689971"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732875537360777466",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732875537360777466"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733178344462778864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733178344462778864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733252012073238573",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733252012073238573"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732259228235055149",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732259228235055149"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733271253467984019",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733271253467984019"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731841637297586292",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731841637297586292"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732881782213669367",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732881782213669367"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732824168620826919",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732824168620826919"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733255191661617219",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733255191661617219"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733174345659531273",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733174345659531273"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732810820424507583",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732810820424507583"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732531970138309025",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732531970138309025"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733118715003129957",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733118715003129957"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732224563210064175",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732224563210064175"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732138804247408674",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732138804247408674"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731734958195044459",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731734958195044459"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732454705161531840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732454705161531840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732582580325941508",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732582580325941508"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731679930235134226",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731679930235134226"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731282958877704665",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731282958877704665"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732459059196858711",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732459059196858711"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731430182022517242",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731430182022517242"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732034592918352235",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732034592918352235"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1731787268937994574",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1731787268937994574"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733260432713118171",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733260432713118171"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733128430659457084",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733128430659457084"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733269591437267186",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733269591437267186"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733266633047892080",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733266633047892080"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733274303741743586",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733274303741743586"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1732498435033776275",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1732498435033776275"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733109042925670419",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733109042925670419"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1733273158537383943",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1733273158537383943"
  }
]
```

## Grok response

```text
**Here is all the raw data from the X/Twitter searches for posts dated December 3–9, 2023 (using the date range 2023-12-03 to 2023-12-10 for the "end of the week").** No summarization or filtering has been applied beyond the tool results. Posts are presented with their full content, author, timestamp, engagement metrics, and any media/links as returned by the tools. Only relevant posts mentioning Charlie Kirk, TPUSA, or related events/appearances were returned; irrelevant or non-matching results are omitted.

### Posts from general keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA" + event/speaking/tour/etc. terms):
- **[post:0]** Author: Matthew Boedy (@MatthewBoedy)  
  Timestamp: Fri, 08 Dec 2023 23:51:38 GMT  
  Likes=3, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=515  
  Content: You may not recognize the name but Turning Point USA is bringing a leading young Dutch anti-vax, anti-globalist, anti-immigrant provocateur to its event next week in Arizona. (She often appears on Fox News of UK. Don’t forget Charlie Kirk’s Turning Point UK remains alive)  
  (Quoted a post about Eva Vlaardingerbroek attending #AMFEST2023 next week.)

- **[post:1]** Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Fri, 08 Dec 2023 23:44:04 GMT  
  Likes=5, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=398  
  Content: ✝️ A friendly reminder from Brandon Tatum! 💯  
  Brandon will be joining us at AMFEST. Use promo code “FAITH13” for $13 General Admissions 🔗 [link]  
  (Media: 2 photos)

- **[post:2]** Author: TPUSA Events (@TPUSAEvents)  
  Timestamp: Fri, 08 Dec 2023 23:25:42 GMT  
  Likes=8, Reposts=6, Quotes=0, Replies=0, Bookmarks=0, Views=639  
  Content: Get ready to boot-scoot and boogie all night at the AmFest concert series! 🤠  
  What song are you most excited to hear live? ⬇️ 🎸  
  #AmFest2023 #tpusaevents #tpusa #eventsinphx #conservative #biggovsucks #myphx #Bigandrich #locash #raelynn  
  (Media: 1 photo)

- **[post:4]** Author: TPUSA Students (@tpusastudents)  
  Timestamp: Fri, 08 Dec 2023 22:27:36 GMT  
  Likes=15, Reposts=5, Quotes=1, Replies=0, Bookmarks=0, Views=721  
  Content: We want to hear what YOU think about the cultural issues America is facing today! 🇺🇸  
  Enter to win a chance to sit at one of four roundtables with: Dr. Ben Carson, Stephen Davis and Anthony Watson, Jonathan Issac, Alex Clark.  
  To qualify for the roundtable experience, you must be a High School or College Chapter Leader with an AmericaFest student pass!  
  (Media: 1 photo)

### Posts from @charliekirk11 account search:
- **[post:11]** Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 04 Dec 2023 21:27:14 GMT  
  Likes=394, Reposts=99, Quotes=19, Replies=112, Bookmarks=4, Views=78841  
  Content: AmFest 2023 starts in 12 days!!  
  Our BIGGEST lineup ever  
  Our BIGGEST multi-day event ever.  
  2024 begins at AmFest 2023  
  [link]  
  (Media: 1 photo)

### Posts from @TPUSA account search:
- **[post:12]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 07 Dec 2023 18:07:30 GMT  
  Likes=352, Reposts=120, Quotes=6, Replies=48, Bookmarks=2, Views=98721  
  Content: Exciting news! @SenTedCruz will be joining us at #AMFEST2023!  
  Come together with 10,000+ patriots next week for the nation’s largest multi-day conservative gathering: https://www.amfest.com/  
  (Media: 1 photo)

- **[post:13]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 06 Dec 2023 20:33:09 GMT  
  Likes=107, Reposts=20, Quotes=6, Replies=33, Bookmarks=6, Views=35701  
  Content: Last night at @CalPoly, @tpusastudents hosted an event with detransitioner @chloecole and @BillboardChris on the dangers of gender-affirming care for minors.  
  Here’s what the protesters were up to outside...  
  🎥: @FrontlinesTPUSA  
  (Media: 1 video)

### Posts from semantic search (Charlie Kirk or TPUSA public speaking events/appearances/tours December 2023):
- **[post:14]** Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 04 Dec 2023 21:27:14 GMT  
  Likes=394, Reposts=99, Quotes=19, Replies=112, Bookmarks=4, Views=78841  
  Content: AmFest 2023 starts in 12 days!!  
  Our BIGGEST lineup ever  
  Our BIGGEST multi-day event ever.  
  2024 begins at AmFest 2023  
  [link]  
  (Media: 1 photo)  
  *(Duplicate of post:11)*

- **[post:17]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 07 Dec 2023 18:07:30 GMT  
  Likes=352, Reposts=120, Quotes=6, Replies=48, Bookmarks=2, Views=98721  
  Content: Exciting news! @SenTedCruz will be joining us at #AMFEST2023!  
  Come together with 10,000+ patriots next week for the nation’s largest multi-day conservative gathering: https://www.amfest.com/  
  (Media: 1 photo)  
  *(Duplicate of post:12)*

### Expanded keyword searches (AmFest/AMFEST + Phoenix/Arizona/event terms, and account-specific):
- **[post:24]** Author: Matthew Boedy (@MatthewBoedy)  
  Timestamp: Fri, 08 Dec 2023 23:51:38 GMT  
  Likes=3, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=515  
  Content: You may not recognize the name but Turning Point USA is bringing a leading young Dutch anti-vax, anti-globalist, anti-immigrant provocateur to its event next week in Arizona. (She often appears on Fox News of UK. Don’t forget Charlie Kirk’s Turning Point UK remains alive)  
  *(Duplicate of post:0; references Eva Vlaardingerbroek at #AMFEST2023)*

- **[post:25]** Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Fri, 08 Dec 2023 23:44:04 GMT  
  Likes=5, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=398  
  Content: ✝️ A friendly reminder from Brandon Tatum! 💯  
  Brandon will be joining us at AMFEST. Use promo code “FAITH13” for $13 General Admissions 🔗 [link]  
  *(Duplicate of post:1)*

- **[post:26]** Author: TPUSA Events (@TPUSAEvents)  
  Timestamp: Fri, 08 Dec 2023 23:25:42 GMT  
  Likes=8, Reposts=6, Quotes=0, Replies=0, Bookmarks=0, Views=639  
  Content: Get ready to boot-scoot and boogie all night at the AmFest concert series! 🤠  
  What song are you most excited to hear live? ⬇️ 🎸  
  #AmFest2023 #tpusaevents #tpusa #eventsinphx #conservative #biggovsucks #myphx #Bigandrich #locash #raelynn  
  *(Duplicate of post:2)*

- **[post:27]** Author: Peyton Kelly (@peytonk131)  
  Timestamp: Fri, 08 Dec 2023 23:01:04 GMT  
  Likes=6, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=152  
  Content: I’m ready to bring the free speech ball back out to campus, anyone else?! 🤩🇺🇸  
  But first… AMFEST!!! 1 week, let’s go!!!! 🥳  
  (Media: 2 photos)

- **[post:28]** Author: TPUSA Students (@tpusastudents)  
  Timestamp: Fri, 08 Dec 2023 22:27:36 GMT  
  Likes=15, Reposts=5, Quotes=1, Replies=0, Bookmarks=0, Views=721  
  Content: We want to hear what YOU think about the cultural issues America is facing today! 🇺🇸  
  Enter to win a chance to sit at one of four roundtables with: Dr. Ben Carson, Stephen Davis and Anthony Watson, Jonathan Issac, Alex Clark.  
  To qualify for the roundtable experience, you must be a High School or College Chapter Leader with an AmericaFest student pass!  
  *(Duplicate of post:4)*

- **[post:30]** Author: Amber Kleinke (@realamber_k96)  
  Timestamp: Fri, 08 Dec 2023 17:48:28 GMT  
  Likes=16, Reposts=4, Quotes=0, Replies=0, Bookmarks=0, Views=1514  
  Content: Let’s save AZ! See y’all at Amfest next week! 😎🇺🇸🌵 #Amfest2023  
  @tpusastudents @TPUSA @TPUSAEvents  
  (Media: 1 photo)

- **[post:31]** Author: Turning Point Education (@tpusaeducation)  
  Timestamp: Fri, 08 Dec 2023 17:34:52 GMT  
  Likes=2, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=179  
  Content: Don’t miss “Standing Courageously Against the Indoctrination of Our Children” breakout session with @charliekirk11 at #AmFest2023!  
  📌 This breakout session will be on Sunday, December 17th, 10:30 am  
  Use promo code code "ACADEMY" for 25% off on general admissions 🔗  
  (Media: 1 video)

- **[post:32]** Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Fri, 08 Dec 2023 17:18:59 GMT  
  Likes=5, Reposts=3, Quotes=0, Replies=2, Bookmarks=0, Views=809  
  Content: Don’t miss “The Gospel and The Government” breakout session with Pastor Rob McCoy, Rick Green, Bob McEwen & Rylee Meek at #AmFest2023!  
  📌 This breakout session will be on Monday morning December 18, 2023  
  It’s not too late to register! Use promo code “FAITH13” for $13 General Admission 🔗 [link] @TPUSAEvents @TPUSA  
  (Media: 1 video)

- **[post:33]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 08 Dec 2023 17:03:43 GMT  
  Likes=494, Reposts=90, Quotes=2, Replies=39, Bookmarks=2, Views=59807  
  Content: JOIN TUCKER NEXT WEEK AT #AMFEST2023 🇺🇸  
  Be there: https://www.amfest.com/  
  (Media: 1 photo)

- **[post:34]** Author: Eva Vlaardingerbroek (@EvaVlaar)  
  Timestamp: Fri, 08 Dec 2023 13:37:56 GMT  
  Likes=2704, Reposts=283, Quotes=13, Replies=75, Bookmarks=29, Views=144812  
  Content: Let’s gooo! 🇳🇱❤️🇺🇸  
  See you all next week at #AMFEST2023!  
  (Media: 1 photo)

- **[post:35]** Author: Page 38 News (@Page38News)  
  Timestamp: Fri, 08 Dec 2023 12:59:30 GMT  
  Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=154  
  Content: @Page38News will be covering the AmericaFest 2023 event as Press in Phoenix, Arizona on December 16th - 19th.  
  @TPUSA #AmFest2023 #Phoenix #Arizona #December

- **[post:36]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 07 Dec 2023 18:07:30 GMT  
  Likes=352, Reposts=120, Quotes=6, Replies=48, Bookmarks=2, Views=98721  
  Content: Exciting news! @SenTedCruz will be joining us at #AMFEST2023!  
  Come together with 10,000+ patriots next week for the nation’s largest multi-day conservative gathering: https://www.amfest.com/  
  *(Duplicate of post:12)*

- **[post:37]** Author: Turning Point Education (@tpusaeducation)  
  Timestamp: Thu, 07 Dec 2023 17:40:26 GMT  
  Likes=1, Reposts=0, Quotes=1, Replies=0, Bookmarks=0, Views=793  
  Content: "Students today are being conditioned to 'don't ask, don't try, and don't think.'" 😱 - Hutz  
  *Join us at #AMFEST2023 this December 16-19, code "ACADEMY" for 25% off on general admissions 🇺🇸 [link]

- **[post:38]** Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Thu, 07 Dec 2023 17:14:28 GMT  
  Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=239  
  Content: 🇺🇸 Erika Kirk will be speaking at #AMFEST2023 on December 16-19th in Phoenix, Arizona.  
  🚩Use promo code “FAITH13” for $13 General Admission 🔗 [link] @TPUSAEvents

- **[post:41]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 08 Dec 2023 17:03:43 GMT  
  Likes=494, Reposts=90, Quotes=2, Replies=39, Bookmarks=2, Views=59807  
  Content: JOIN TUCKER NEXT WEEK AT #AMFEST2023 🇺🇸  
  Be there: https://www.amfest.com/  
  *(Duplicate of post:33)*

- **[post:42]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 07 Dec 2023 18:07:30 GMT  
  Likes=352, Reposts=120, Quotes=6, Replies=48, Bookmarks=2, Views=98721  
  Content: Exciting news! @SenTedCruz will be joining us at #AMFEST2023!  
  Come together with 10,000+ patriots next week for the nation’s largest multi-day conservative gathering: https://www.amfest.com/  
  *(Duplicate of post:12)*

- **[post:43]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 06 Dec 2023 20:33:09 GMT  
  Likes=107, Reposts=20, Quotes=6, Replies=33, Bookmarks=6, Views=35701  
  Content: Last night at @CalPoly, @tpusastudents hosted an event with detransitioner @chloecole and @BillboardChris on the dangers of gender-affirming care for minors.  
  Here’s what the protesters were up to outside...  
  🎥: @FrontlinesTPUSA  
  *(Duplicate of post:13)*

- **[post:44]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 06 Dec 2023 17:56:41 GMT  
  Likes=185, Reposts=42, Quotes=1, Replies=20, Bookmarks=2, Views=31074  
  Content: Catch @TulsiGabbard THIS MONTH at the nation’s largest multi-day conservative gathering, #AmFest2023! 🇺🇸 🦅  
  Register TODAY at https://www.amfest.com/  
  (Media: 1 photo)

- **[post:45]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 05 Dec 2023 23:01:46 GMT  
  Likes=17, Reposts=9, Quotes=1, Replies=0, Bookmarks=0, Views=6138  
  Content: Join us for an unforgettable night with all your country music favorites at #AMFEST2023!  
  BE THERE: https://www.amfest.com/  
  (Media: 1 photo)

- **[post:46]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 05 Dec 2023 20:44:07 GMT  
  Likes=58, Reposts=13, Quotes=0, Replies=23, Bookmarks=0, Views=6068  
  Content: Stop. Playing. Their. Game.  
  Join @Riley_Gaines_ and 10,000+ patriots in the fight for our nation’s future at #AMFEST2023 🇺🇸  
  Register today at https://www.amfest.com/  
  (Media: 1 photo)

- **[post:47]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 04 Dec 2023 17:59:22 GMT  
  Likes=30, Reposts=12, Quotes=2, Replies=1, Bookmarks=0, Views=5618  
  Content: .@patrickbetdavid is coming to #AMFEST2023, and so should you!  
  Head to https://www.amfest.com/ to register for the nation's LARGEST multi-day conservative gathering 🇺🇸  
  (Media: 1 photo)

- **[post:48]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 04 Dec 2023 15:56:47 GMT  
  Likes=41, Reposts=9, Quotes=0, Replies=3, Bookmarks=0, Views=6097  
  Content: "I want you to acknowledge this" says it all...  
  Come celebrate the greatest country in the history of the world at #AMFEST2023! Register NOW at https://www.amfest.com/ 🇺🇸  
  (Media: 1 video)

- **[post:49]** Author: TPUSA Events (@TPUSAEvents)  
  Timestamp: Fri, 08 Dec 2023 23:25:42 GMT  
  Likes=8, Reposts=6, Quotes=0, Replies=0, Bookmarks=0, Views=639  
  Content: Get ready to boot-scoot and boogie all night at the AmFest concert series! 🤠  
  What song are you most excited to hear live? ⬇️ 🎸  
  #AmFest2023 #tpusaevents #tpusa #eventsinphx #conservative #biggovsucks #myphx #Bigandrich #locash #raelynn  
  *(Duplicate of post:2)*

- **[post:51]** Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 04 Dec 2023 21:27:14 GMT  
  Likes=394, Reposts=99, Quotes=19, Replies=112, Bookmarks=4, Views=78841  
  Content: AmFest 2023 starts in 12 days!!  
  Our BIGGEST lineup ever  
  Our BIGGEST multi-day event ever.  
  2024 begins at AmFest 2023  
  [link]  
  *(Duplicate of post:11)*

- **[post:52]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 07 Dec 2023 18:07:30 GMT  
  Likes=352, Reposts=120, Quotes=6, Replies=48, Bookmarks=2, Views=98721  
  Content: Exciting news! @SenTedCruz will be joining us at #AMFEST2023!  
  Come together with 10,000+ patriots next week for the nation’s largest multi-day conservative gathering: https://www.amfest.com/  
  *(Duplicate of post:12)*

- **[post:53]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 08 Dec 2023 17:03:43 GMT  
  Likes=494, Reposts=90, Quotes=2, Replies=39, Bookmarks=2, Views=59807  
  Content: JOIN TUCKER NEXT WEEK AT #AMFEST2023 🇺🇸  
  Be there: https://www.amfest.com/  
  *(Duplicate of post:33)*

No posts were returned from @RealCharlieKirk or additional @TPUSAEvents searches within the date range. No other specific campus/university speaking events for Charlie Kirk or TPUSA outside the AmFest mentions and the Cal Poly event (Dec 6) were found in the results. All AmFest references point to the multi-day event in Phoenix, Arizona (December 16–19, 2023), with Charlie Kirk scheduled for at least one breakout session on Sunday, December 17th.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-12-03 to 2023-12-09**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-12-03 to 2023-12-09 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
