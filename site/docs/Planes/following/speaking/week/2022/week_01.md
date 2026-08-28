---
unlisted: true
title: "Week 01 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W01"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-01-01 to 2022-01-07."
status: completed
hide_table_of_contents: true
---

# Week 01, 2022

- Date range: 2022-01-01 to 2022-01-07
- Queried at (UTC): 2026-08-24T18:58:24Z
- Model: grok-4.3
- API status: completed
- Response id: 07cc7753-8999-9b5d-bcb5-36e5d35f6c86

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-01-01 to the end of the week 2022-01-07.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR events OR \"will be\" OR speaking OR tour OR \"public speaking\" OR appearance OR appearances) since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR events OR \"will be\" OR speaking OR tour OR \"public speaking\" OR appearance OR appearances) since:2022-01-01 until:2022-01-08 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR TPUSA OR \"Turning Point\") since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR \"Charlie Kirk\") since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, where Charlie will speak in early January 2022",
      "limit": "5",
      "from_date": "2022-01-01",
      "to_date": "2022-01-08"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (speaking OR \"will speak\" OR \"speaks at\" OR \"speaking at\" OR \"speaking engagement\" OR \"will be speaking\" OR \"speaking tour\" OR \"public speaking\" OR appearance OR appearances OR rally OR rallies OR event OR events OR \"at the\" OR campus OR college OR university) since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR speaking OR speak OR tour OR TPUSA) since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"ReAwaken America Tour\" (Charlie OR Kirk OR TPUSA) since:2022-01-01 until:2022-01-08",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2022-01-01 until:2022-01-08",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk speaking events, TPUSA events, rallies, campus speeches, or where Charlie Kirk will appear or speak in January 2022",
      "limit": "10",
      "from_date": "2022-01-01",
      "to_date": "2022-01-08",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 28106,
  "input_tokens_details": {
    "cached_tokens": 11200
  },
  "output_tokens": 8044,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 36150,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 984825000,
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
    "input_tokens": 18278,
    "output_tokens": 7364
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479144148947333120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479144148947333120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477690381781377025",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477690381781377025"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478845440988573699",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478845440988573699"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477088218323562504",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477088218323562504"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478814105234411520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478814105234411520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479109051950583823",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479109051950583823"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479192219454160896",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479192219454160896"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478803490361073668",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478803490361073668"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478513303953489923",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478513303953489923"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477849982472388610",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477849982472388610"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479185206020030466",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479185206020030466"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477850673958039556",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477850673958039556"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479090383611068419",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479090383611068419"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479175435552497666",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479175435552497666"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479215473757728768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479215473757728768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478893969832435712",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478893969832435712"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479172595979227136",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479172595979227136"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479114047928692740",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479114047928692740"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479163291108732928",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479163291108732928"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478889714144841729",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478889714144841729"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478881781063421952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478881781063421952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477421393025245189",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477421393025245189"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479235666076741636",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479235666076741636"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479185630932389891",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479185630932389891"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479145153877225486",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479145153877225486"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479156499028926467",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479156499028926467"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478848578789330945",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478848578789330945"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477694652665024514",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477694652665024514"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477406092195938306",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477406092195938306"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478824457372413964",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478824457372413964"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477345578384334848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477345578384334848"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478753552646422533",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478753552646422533"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479189293453266946",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479189293453266946"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478578977044377605",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478578977044377605"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479216340481318917",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479216340481318917"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478808723225133056",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478808723225133056"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478527330876215298",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478527330876215298"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478782806297698306",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478782806297698306"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478857166253559809",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478857166253559809"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478850310416207877",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478850310416207877"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479188769622343680",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479188769622343680"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479214840371630087",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479214840371630087"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478839837624918016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478839837624918016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479211160436023296",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479211160436023296"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1477625488692719616",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1477625488692719616"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479218856199606281",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479218856199606281"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479168963766472710",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479168963766472710"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1478910787611598851",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1478910787611598851"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479184295004721161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479184295004721161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479174937692688387",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479174937692688387"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1479175964831723522",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1479175964831723522"
  }
]
```

## Grok response

```text
**Here is the complete, unfiltered collection of all relevant X (Twitter) posts found from searches covering January 1–7, 2022 (using date range since:2022-01-01 until:2022-01-08).** No posts were found that announce, promote, or detail any specific public speaking events, campus appearances, rallies, tours, or confirmed locations where Charlie Kirk or TPUSA would be speaking during this exact week. 

All matching or near-matching posts (from keyword searches for terms like "Charlie Kirk", TPUSA, "Turning Point USA", speaking/event/rally/tour/appearance combined with the date range, plus semantic searches for speaking events/appearances) are listed below in full, including post ID, author, timestamp (GMT), full content, and any quoted/replied media or context. Irrelevant or off-topic posts were filtered out where possible, but all retrieved results matching the broad search criteria are included for completeness. No from:charliekirk11 or from:TPUSA posts in the window referenced any upcoming personal speaking appearances by Kirk.

- **[post:0]** ID: 1479235666076741636  
  Author: Hogs & Horsepower (@SuperHeroTo5)  
  Timestamp: Thu, 06 Jan 2022 23:37:20 GMT  
  Content: Has anyone thought about the name reveal being on #GroundhogDay (yes I know you have) well maybe they will be true to the movie and repeat, what I mean is the name....MAYBE it stays the same as now, the #WashingtonFootball Team....just saying

- **[post:1]** ID: 1479218856199606281  
  Author: Hogs & Horsepower (@SuperHeroTo5)  
  Timestamp: Thu, 06 Jan 2022 22:30:32 GMT  
  Content: Oh God he is at it again #DramaQueen @KingJames, running his mouth over the @WashWizards announcer.  Man #STFU by the way you ain't no 👑 and never will be deflate that head of yours

- **[post:2]** ID: 1479189293453266946  
  Author: We Are Charlie Kirk (@Saucy_Rossy75)  
  Timestamp: Thu, 06 Jan 2022 20:33:04 GMT  
  Content: Dick Cheney, the man who waged multiple failed wars in the Middle East, should not being preaching to us about the immorality of the January 6th event.  
  (Quoted post: Former VP Dick Cheney had strong words for how current GOP leaders have responded to the Capitol attack that took place one year ago: “It's not leadership that resembles any of the folks I knew when I was here for 10 years.” [with photo])

- **[post:3]** ID: 1479188769622343680  
  Author: Kirk Nienaber M.D. (@KirkNienaber)  
  Timestamp: Thu, 06 Jan 2022 20:30:59 GMT  
  Content: Head on up to Union University in Jackson… where you will be free to be your little quasi racist self while soothing your fragile ego…

- **[post:4]** ID: 1479185630932389891  
  Author: ❌ABBY’S DADDY❌(2009-19)❌ (@JohnGLovesLife)  
  Timestamp: Thu, 06 Jan 2022 20:18:31 GMT  
  Content: @MunchenerPost @charliekirk11  “Charlie Kirk bussed vacationers”? You’re accusing Charlie of a massive kissing event. I beg to differ! (He won’t understand, C.K. He’s a Democrat, a.k.a. DemonRat!)  
  (Quoted post: Remember when .@Charliekirk11 bussed vacationers in for an unscheduled tour of a secure government building? [with photo])

- **[post:5]** ID: 1479184295004721161  
  Author: James Taylor (@TammyJone63)  
  Timestamp: Thu, 06 Jan 2022 20:13:12 GMT  
  Content: @RealCandaceO as usual, spouting the talking points that have been spouted repeatedly at @TPUSA events and RNC conventions (with the exception of 2020 RNC where Owens was snubbed) Are you not tired of them, Candace? Because we all are!

- **[post:6]** ID: 1479175435552497666  
  Author: Gabe Kuhn (@G_Kuhn71)  
  Timestamp: Thu, 06 Jan 2022 19:38:00 GMT  
  Content: Also, I can’t lie…seeing those Turning Point USA kids from the U of Memphis speaking on race relations from one of their families million dollar houses definitely tickled me.

- **[post:7]** ID: 1479174937692688387  
  Author: Gil Noble (@GilGnoble)  
  Timestamp: Thu, 06 Jan 2022 19:36:01 GMT  
  Content: Kelly Ernby, GOP Super Star, 46 yrs old died of COVID She got sick after speaking AGAINST VACCINE mandates at a "Turning Point USA" Rally! “I don’t think the govt should be involved in mandating what vaccines people are taking”-Kelly Ernby "SHE'S NOT VAXXED", said her husband.

- **[post:8]** ID: 1479168963766472710  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 19:12:17 GMT  
  Content: Watch the EXCLUSIVE interview with NBA Superstar Enes Kanter Freedom on TPUSA's sports show, Breakaway! 🇺🇸 @EnesFreedom "Enes is courageous enough to speak out boldly in the name of freedom!" @JonnyRoot_ https://tpusa.com/live/exclusive-enes-kanter-freedom-talks-ccp-lebron-more-on-breakaway/

- **[post:9]** (duplicate of post:2) ID: 1479189293453266946  
  Author: We Are Charlie Kirk (@Saucy_Rossy75)  
  Timestamp: Thu, 06 Jan 2022 20:33:04 GMT  
  Content: Dick Cheney, the man who waged multiple failed wars in the Middle East, should not being preaching to us about the immorality of the January 6th event.  
  (Quoted post same as above)

- **[post:10]** (duplicate of post:4) ID: 1479185630932389891  
  Author: ❌ABBY’S DADDY❌(2009-19)❌ (@JohnGLovesLife)  
  Timestamp: Thu, 06 Jan 2022 20:18:31 GMT  
  Content: @MunchenerPost @charliekirk11  “Charlie Kirk bussed vacationers”? You’re accusing Charlie of a massive kissing event. I beg to differ! (He won’t understand, C.K. He’s a Democrat, a.k.a. DemonRat!)  
  (Quoted post same as above)

- **[post:11]** (duplicate of post:7) ID: 1479174937692688387  
  Author: Gil Noble (@GilGnoble)  
  Timestamp: Thu, 06 Jan 2022 19:36:01 GMT  
  Content: Kelly Ernby, GOP Super Star, 46 yrs old died of COVID She got sick after speaking AGAINST VACCINE mandates at a "Turning Point USA" Rally! “I don’t think the govt should be involved in mandating what vaccines people are taking”-Kelly Ernby "SHE'S NOT VAXXED", said her husband.

- **[post:12]** (duplicate of post:8) ID: 1479168963766472710  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 19:12:17 GMT  
  Content: Watch the EXCLUSIVE interview with NBA Superstar Enes Kanter Freedom on TPUSA's sports show, Breakaway! 🇺🇸 @EnesFreedom "Enes is courageous enough to speak out boldly in the name of freedom!" @JonnyRoot_ https://tpusa.com/live/exclusive-enes-kanter-freedom-talks-ccp-lebron-more-on-breakaway/

- **[post:13]** ID: 1478893969832435712  
  Author: Jon Root (@JonnyRoot_)  
  Timestamp: Thu, 06 Jan 2022 00:59:33 GMT  
  Content: The Washington Football Team's new name will be the Admirals. Here's why... PS: Hey NFL, we're still waiting for more information other than just Jon Gruden's emails from your investigation into their "toxic workplace environment" @TPUSA | #TPUSALIVE  
  (With video)

- **[post:14]** ID: 1478850310416207877  
  Author: Paulina🌻 (@TrefaultPaulina)  
  Timestamp: Wed, 05 Jan 2022 22:06:04 GMT  
  Content: “We are forgetting that January 6th was very much a religious event—white Christian nationalism on display. We must remember that fact. Bc evidence is mounting that white Christian nationalism could provide the theological cover for more events like it.” https://time.com/6132591/january-6th-christian-nationalism/

- **[post:15]** ID: 1478839837624918016  
  Author: Ann Albert (@Georgephyl1)  
  Timestamp: Wed, 05 Jan 2022 21:24:27 GMT  
  Content: Charlie Kirk, Eric Trump & Kim Clement's Daughter Join General Flynn's ReAwaken America Tour!!!

- **[post:16]** ID: 1478824457372413964  
  Author: Gordon Chamberlain (@GChamberlainAZ)  
  Timestamp: Wed, 05 Jan 2022 20:23:20 GMT  
  Content: Christian roots LOL Unlike Charlie Kirk Christians care about others are not colluding with climate criminals Look forward to your 06 Jan testimony @SpeakerPelosi @TPUSA helped bring people to event What was the purpose of that, stole election lies? #USpolitics  
  (Quoted post from @charliekirk11 about Chick-Fil-A vaccine policy)

- **[post:17]** (duplicate of post:8/12) ID: 1479168963766472710  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 19:12:17 GMT  
  Content: Watch the EXCLUSIVE interview with NBA Superstar Enes Kanter Freedom on TPUSA's sports show, Breakaway! 🇺🇸 @EnesFreedom "Enes is courageous enough to speak out boldly in the name of freedom!" @JonnyRoot_ https://tpusa.com/live/exclusive-enes-kanter-freedom-talks-ccp-lebron-more-on-breakaway/

- **[post:18]** ID: 1477406092195938306  
  Author: America Out Loud News (@OutLoudNews)  
  Timestamp: Sat, 01 Jan 2022 22:27:15 GMT  
  Content: Krikorian, Powell, McCullough & Shaffer What Just Happened 2021? What Lies Ahead 2022? Viewpoint This Sunday 10 AM ET, Encore 6 PM iHEART RADIO https://www.iheart.com/live/america-out-loud-talk-radio-7363/ LIVE https://streamdb7web.securenetsystems.net/ce/TALKLOUD& @MarkSKrikorian @CIS_org @P_McCulloughMD @tspooky  
  (With photo)

- **[post:19]** ID: 1477849982472388610  
  Author: Kari Lake (@KariLake)  
  Timestamp: Mon, 03 Jan 2022 03:51:07 GMT  
  Content: I’m honored to have President Trump’s endorsement. And I’m thrilled that he’s coming to Florence, Arizona January 15 for his first rally of 2022. Let’s make this his biggest rally yet. I will see you there! Sign up to attend.⤵️ https://t.co/ghob1knZKW  
  (With photo)

- **[post:20]** ID: 1478527330876215298  
  Author: Christine Pelosi (@sfpelosi)  
  Timestamp: Wed, 05 Jan 2022 00:42:40 GMT  
  Content: So Trump is going to rally in Arizona on January 15 - MLK’s actual birthday - no doubt with a couple of his Black MAGA candidates to co-opt the holiday. Senators Kelly and Sinema: do not let him denigrate your state: pass real #votingrights reforms now!

- **[post:21]** ID: 1477625488692719616  
  Author: 🇯🇲CocoaBreadFed🇯🇲(BusinessOnly) (@CocoaBreadFed)  
  Timestamp: Sun, 02 Jan 2022 12:59:04 GMT  
  Content: Just added NY 2 the list so DM me 4 any BOOKING INFO. ***FULLY BOOKED*** Jan 5th Houston,TX Jan 8th San Antonio,TX Jan 13th Dallas,TX Jan 18th Las Vegas,NV Jan 21st St Louis,MO Jan 27th Detroit,MI Feb 10th Los Angeles, CA Feb 11th San Francisco, CA *Feb 20th New York, NY  
  (With video)

- **[post:22]** ID: 1479114047928692740  
  Author: Dinesh D'Souza (@DineshDSouza)  
  Timestamp: Thu, 06 Jan 2022 15:34:04 GMT  
  Content: Hey Texas and Florida! We’re in Houston on Saturday, January 29. Fort Lauderdale on Saturday, February 19. For tickets to go https://t.co/S4eEjln2Eu  
  (With photo)

- **[post:23]** ID: 1479216340481318917  
  Author: Rhonda Harbison (@rhonda_harbison)  
  Timestamp: Thu, 06 Jan 2022 22:20:32 GMT  
  Content: https://t.co/BoeLHnoA25 Who Funds Conservative Campus Group Turning Point USA? Donors ...

- **[post:24]** ID: 1479215473757728768  
  Author: Charlie Kirk’s Ghost’s Conscience (@charliekirk11s1)  
  Timestamp: Thu, 06 Jan 2022 22:17:06 GMT  
  Content: 🤔…how about the people at the Capitol a year ago who didn’t give a damn about the Capitol Police or MPD who were telling them to leave?  Crappy framing @DailyCaller!

- **[post:25]** ID: 1479214840371630087  
  Author: lib claptrap (@hellcheez)  
  Timestamp: Thu, 06 Jan 2022 22:14:35 GMT  
  Content: They crow about how they’re the champions of election integrity but it’s republicans who seem to be the ones getting caught cheating at the ballot box. And they disdain the whole process anyway, resorting to violence and audit shams when things don’t go their way.

- **[post:26]** ID: 1479192219454160896  
  Author: Cole Younger (@oakengnome)  
  Timestamp: Thu, 06 Jan 2022 20:44:41 GMT  
  Content: I wouldn’t want tpusa on my campus at all. Didn’t Charlie Kirk send bus loads of them to the capitol for 1/6? Not mention I feel like these kinds of scholarships are pretty common. It just sounds like someone let the racist kids on Fox News.

- **[post:27]** (duplicate of post:2) ID: 1479189293453266946  
  Author: We Are Charlie Kirk (@Saucy_Rossy75)  
  Timestamp: Thu, 06 Jan 2022 20:33:04 GMT  
  Content: Dick Cheney, the man who waged multiple failed wars in the Middle East, should not being preaching to us about the immorality of the January 6th event.  
  (Quoted post same as above)

- **[post:28]** (duplicate of post:4) ID: 1479185630932389891  
  Author: ❌ABBY’S DADDY❌(2009-19)❌ (@JohnGLovesLife)  
  Timestamp: Thu, 06 Jan 2022 20:18:31 GMT  
  Content: @MunchenerPost @charliekirk11  “Charlie Kirk bussed vacationers”? You’re accusing Charlie of a massive kissing event. I beg to differ! (He won’t understand, C.K. He’s a Democrat, a.k.a. DemonRat!)  
  (Quoted post same as above)

- **[post:29]** ID: 1479185206020030466  
  Author: R.1014 (@Rrichmond14Data)  
  Timestamp: Thu, 06 Jan 2022 20:16:49 GMT  
  Content: Clearly leaning on her elementary charlie kirk/tpusa talking points. Lol.

- **[post:30]** ID: 1479175964831723522  
  Author: … ™ (@Stinkshovel)  
  Timestamp: Thu, 06 Jan 2022 19:40:06 GMT  
  Content: Now do TPUSA and Charlie Kirk.  
  (Quoted post with video about Republican Party as domestic terrorist organization)

- **[post:31]** ID: 1479145153877225486  
  Author: Je Suis Charlie Kirk (@semperfidem2004)  
  Timestamp: Thu, 06 Jan 2022 17:37:40 GMT  
  Content: I agree that the Remoaning needs to stop. I disagree with the caricature that Leavers didn't think their vote through. That may be true of some, but most I speak to give solid, sensible reasons which have since been proved to be well founded

- **[post:32]** ID: 1478839837624918016  
  Author: Ann Albert (@Georgephyl1)  
  Timestamp: Wed, 05 Jan 2022 21:24:27 GMT  
  Content: Charlie Kirk, Eric Trump & Kim Clement's Daughter Join General Flynn's ReAwaken America Tour!!!

- **[post:33]** ID: 1477421393025245189  
  Author: Cindy Bruni (@bruni_cindy)  
  Timestamp: Sat, 01 Jan 2022 23:28:03 GMT  
  Content: Charlie Kirk, Eric Trump & Kim Clement's Daughter Join General Flynn's ReAwaken America Tour!!!

- **[post:34]** ID: 1477345578384334848  
  Author: Ryan M Glassford (@OutLaw_76)  
  Timestamp: Sat, 01 Jan 2022 18:26:48 GMT  
  Content: Charlie Kirk, Eric Trump & Kim Clement's Daughter Join General Flynn's ReAwaken America Tour!!!

- **[post:35]** ID: 1479172595979227136  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 06 Jan 2022 19:26:43 GMT  
  Content: We should cease trade with the Australian Government given their treatment of Novak Djokovic. These are Human Rights Abuses—there must be a cost.

- **[post:36]** ID: 1479156499028926467  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 06 Jan 2022 18:22:45 GMT  
  Content: It's very telling that Democrats are choosing to use the January 6th Anniversary as a platform to promote their federal takeover of elections.

- **[post:37]** ID: 1478857166253559809  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 05 Jan 2022 22:33:18 GMT  
  Content: Weren't teachers given priority access to the vaccine so we could keep schools open? Why isn't that enough for them? 🤔

- **[post:38]** ID: 1478814105234411520  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 05 Jan 2022 19:42:12 GMT  
  Content: It's been 365 days since someone planted pipe bombs outside the DNC & RNC Headquarters. How is it possible that the DOJ & FBI had time to investigate parents at school board meetings but can't get to the bottom of this?

- **[post:39]** ID: 1478808723225133056  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 05 Jan 2022 19:20:49 GMT  
  Content: Hearing from Chick-Fil-A employees that they were required to be vaccinated by Feb 4th or face risk of termination We already know Chick-Fil-A is sympathetic to BLM and donated to groups that support abortion...why are they further betraying their alleged Christian roots?

- **[post:40]** ID: 1478782806297698306  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 05 Jan 2022 17:37:50 GMT  
  Content: 20% of kids in Chicago don't have internet at home Only 50% of kids in The South Side have internet at home In South & West Side schools in 2020, 1 in every 5 grades given out in math & english was an F So obviously sending Chicago schools back online is a great idea, right?

- **[post:41]** ID: 1478513303953489923  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Tue, 04 Jan 2022 23:46:55 GMT  
  Content: No serious nation would ever tolerate an illegal invasion of 2 million foreigners per year. Where are our leaders?

- **[post:42]** ID: 1477850673958039556  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 03 Jan 2022 03:53:52 GMT  
  Content: So the media blames players like Kirk Cousins and Aaron Rodgers for getting COVID, but the media is silent when entire teams of vaccinated players get the virus?

- **[post:43]** ID: 1477694652665024514  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sun, 02 Jan 2022 17:33:54 GMT  
  Content: You can find MTG uncensored and unfiltered on The Charlie Kirk Show Listen to what Twitter’s least favorite congresswoman has to say here ⬇️

- **[post:44]** ID: 1477690381781377025  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sun, 02 Jan 2022 17:16:55 GMT  
  Content: How many more Elected Republicans have to get banned from big tech platforms before our side decides to wake up and start doing something about it? Stop letting Big Tech subvert the will of the American people.

- **[post:45]** ID: 1479211160436023296  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 21:59:57 GMT  
  Content: 🔴 LIVE NOW: Professors Are Being Bribed To Go Woke?! Watch daily shows, live in-studio content from TPUSA HQ and watch today’s weekly show, Benny on the Block. @JackPosobiec @realalexclark @JonnyRoot_ @bennyjohnson @realmagahulk @JobobTaeleifi https://x.com/i/broadcasts/1yNGaYlQEXnGj

- **[post:46]** (duplicate of post:8/12/17) ID: 1479168963766472710  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 19:12:17 GMT  
  Content: Watch the EXCLUSIVE interview with NBA Superstar Enes Kanter Freedom on TPUSA's sports show, Breakaway! 🇺🇸 @EnesFreedom "Enes is courageous enough to speak out boldly in the name of freedom!" @JonnyRoot_ https://tpusa.com/live/exclusive-enes-kanter-freedom-talks-ccp-lebron-more-on-breakaway/

- **[post:47]** ID: 1479163291108732928  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 18:49:44 GMT  
  Content: Residents of San Francisco and their streets have one thing in common: they both have to deal with a lot of crap! #BigGovSucks @JonnyRoot_ @RealMAGAHulk @TheIsabelB @Jobob  
  (With video)

- **[post:48]** ID: 1479144148947333120  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 17:33:40 GMT  
  Content: Gun rights are women’s rights! #GunsSaveLives  
  (With photo)

- **[post:49]** ID: 1479090383611068419  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 14:00:02 GMT  
  Content: SPOT ON @BennyJohnson! Conforming to the mob is NOT the flex that the Left thinks it is. #BigGovSucks #AMFEST2021  
  (With video)

- **[post:50]** ID: 1478910787611598851  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 02:06:23 GMT  
  Content: Professors are being "BRIBED" to incorporate woke curriculum into their classes! @UofMemphis is literally paying professors to teach radical, woke ideology. The TPUSA chapter on campus is fighting back! WATCH!  
  (With video)

- **[post:51]** ID: 1478889714144841729  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 00:42:38 GMT  
  Content: TPUSA student chapter president at the University of Memphis EXPOSES the Left's WOKE incentives DESTROYING education: “Bribing teachers with taxpayer dollars is massively unethical, and should be illegal!” CATCH @theisabelb's reaction at TPUSA LIVE! https://tpusa.com/live/tpusa-students-from-the-university-of-memphis-blast-woke-curriculum-and-bribery-on-fox-news/  
  (With photo)

- **[post:52]** ID: 1478881781063421952  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 06 Jan 2022 00:11:07 GMT  
  Content: Yep @BennyJohnson... This is RIDICULOUS & UNACCEPTABLE. #GenFree  
  (With photo)

- **[post:53]** ID: 1478848578789330945  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 05 Jan 2022 21:59:11 GMT  
  Content: 🔴 LIVE NOW: 'What in the World' Are These Banished Words? Watch daily shows, live in-studio content from TPUSA HQ and watch today’s weekly show, SMASH. @JackPosobiec @realalexclark @JonnyRoot_ @realmagahulk @theisabelb @JobobTaeleifi

- **[post:54]** ID: 1478845440988573699  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 05 Jan 2022 21:46:43 GMT  
  Content: There’s a record number of Americans quitting their jobs during the pandemic – And there are more reasons as to why than you might think. Tune into TPUSA LIVE today at 5 PM ET / 2 PM PT for more unfiltered opinions. @JonnyRoot_ @TheIsabelB @RealMAGAHulk  
  (With video)

- **[post:55]** (duplicate of post:18) ID: 1477406092195938306  
  Author: America Out Loud News (@OutLoudNews)  
  Timestamp: Sat, 01 Jan 2022 22:27:15 GMT  
  Content: Krikorian, Powell, McCullough & Shaffer What Just Happened 2021? What Lies Ahead 2022? Viewpoint This Sunday 10 AM ET, Encore 6 PM iHEART RADIO https://www.iheart.com/live/america-out-loud-talk-radio-7363/ LIVE https://streamdb7web.securenetsystems.net/ce/TALKLOUD& @MarkSKrikorian @CIS_org @P_McCulloughMD @tspooky  
  (With photo)

- **[post:56]** (duplicate of post:19) ID: 1477849982472388610  
  Author: Kari Lake (@KariLake)  
  Timestamp: Mon, 03 Jan 2022 03:51:07 GMT  
  Content: I’m honored to have President Trump’s endorsement. And I’m thrilled that he’s coming to Florence, Arizona January 15 for his first rally of 2022. Let’s make this his biggest rally yet. I will see you there! Sign up to attend.⤵️ https://t.co/ghob1knZKW  
  (With photo)

- **[post:57]** (duplicate of post:20) ID: 1478527330876215298  
  Author: Christine Pelosi (@sfpelosi)  
  Timestamp: Wed, 05 Jan 2022 00:42:40 GMT  
  Content: So Trump is going to rally in Arizona on January 15 - MLK’s actual birthday - no doubt with a couple of his Black MAGA candidates to co-opt the holiday. Senators Kelly and Sinema: do not let him denigrate your state: pass real #votingrights reforms now!

- **[post:58]** ID: 1478753552646422533  
  Author: Dr. Kelli Ward 🇺🇸 (@kelliwardaz)  
  Timestamp: Wed, 05 Jan 2022 15:41:35 GMT  
  Content: President Trump is holding his first #SaveAmerica Rally of 2022 in ARIZONA in 1/15/22. Get your tickets today!

- **[post:59]** ID: 1478803490361073668  
  Author: Kyle Griffin (@kylegriffin1)  
  Timestamp: Wed, 05 Jan 2022 19:00:01 GMT  
  Content: Warning: At the Cobb County, Georgia GOP headquarters, a group of far-right activists will hold a two-hour long program on Jan. 6 to lionize the insurrectionists who stampeded into the Capitol to prevent Congress from certifying Joe Biden's victory.

- **[post:60]** (duplicate of post:21) ID: 1477625488692719616  
  Author: 🇯🇲CocoaBreadFed🇯🇲(BusinessOnly) (@CocoaBreadFed)  
  Timestamp: Sun, 02 Jan 2022 12:59:04 GMT  
  Content: Just added NY 2 the list so DM me 4 any BOOKING INFO. ***FULLY BOOKED*** Jan 5th Houston,TX Jan 8th San Antonio,TX Jan 13th Dallas,TX Jan 18th Las Vegas,NV Jan 21st St Louis,MO Jan 27th Detroit,MI Feb 10th Los Angeles, CA Feb 11th San Francisco, CA *Feb 20th New York, NY  
  (With video)

- **[post:61]** (duplicate of post:22) ID: 1479114047928692740  
  Author: Dinesh D'Souza (@DineshDSouza)  
  Timestamp: Thu, 06 Jan 2022 15:34:04 GMT  
  Content: Hey Texas and Florida! We’re in Houston on Saturday, January 29. Fort Lauderdale on Saturday, February 19. For tickets to go https://t.co/S4eEjln2Eu  
  (With photo)

- **[post:62]** ID: 1477088218323562504  
  Author: Kyle Cheney (@kyledcheney)  
  Timestamp: Sat, 01 Jan 2022 01:24:08 GMT  
  Content: And here is what it lists as events to organize as part of this effort: https://www.politico.com/news/2021/12/31/kerik-documents-jan-6-committee-526297  
  (With photo)

- **[post:63]** ID: 1478578977044377605  
  Author: RSBN 🇺🇸 (@RSBNetwork)  
  Timestamp: Wed, 05 Jan 2022 04:07:53 GMT  
  Content: We will be LIVE on Jan. 6 with two events 🚨 1PM ET - @RepMTG and @RepMattGaetz EXPOSE the truth about Jan. 6 🎥 4PM ET - 'Freedom Rally' in support of President Trump in West Palm Beach! 🇺🇸 MORE INFO ⬇️

- **[post:64]** ID: 1479109051950583823  
  Author: Governor Prof. Hillary Barchok (@BarchokHillary)  
  Timestamp: Thu, 06 Jan 2022 15:14:13 GMT  
  Content: The Bomet County leadership is delighted to announce that preparations towards our big day on Monday 10th January are on top gear and that we are set for a Mega Hustler Nation rally at the Bomet Green Stadium.  
  (With photo)

**No additional posts were returned from the searches.** The results primarily reference past or unrelated events (e.g., January 6, 2021 references, future Trump rallies in mid-January 2022, or general TPUSA campus activity), with no direct announcements of Charlie Kirk or TPUSA speaking engagements for January 1–7, 2022.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-01-01 to 2022-01-07**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-01-01 to 2022-01-07 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
