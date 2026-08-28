---
unlisted: true
title: "Week 13 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W13"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-03-26 to 2022-04-01."
status: completed
hide_table_of_contents: true
---

# Week 13, 2022

- Date range: 2022-03-26 to 2022-04-01
- Queried at (UTC): 2026-08-24T18:59:54Z
- Model: grok-4.3
- API status: completed
- Response id: 44e1a7ef-050f-99e4-85f5-0dc2cd0b65d5

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-03-26 to the end of the week 2022-04-01.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR visiting OR campus) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR visiting OR campus) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR visiting OR campus) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak",
      "limit": "10",
      "from_date": "2022-03-26",
      "to_date": "2022-04-02",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"charliekirk11\") (event OR speaking OR speak OR tour OR appearance OR rally OR campus OR \"will be speaking\" OR \"speaking at\" OR visiting) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR speaking OR speak OR tour OR appearance) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (event OR speaking OR speak OR tour OR appearance OR \"Saving America Tour\") since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA events, tours, speaking engagements, or appearances in late March early April 2022",
      "limit": "10",
      "from_date": "2022-03-26",
      "to_date": "2022-04-02",
      "min_score_threshold": "0.05"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Educate Don't Mandate\" OR \"Educate Don’t Mandate\" (tour OR event OR Charlie OR Kirk OR TPUSA) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Saving America Tour\" (Charlie OR Kirk OR TPUSA OR Fervent) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Arkansas OR Berkeley OR Rutgers OR Michigan OR Ann Arbor OR UArkansas) since:2022-03-26 until:2022-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1509328827712950276"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 36175,
  "input_tokens_details": {
    "cached_tokens": 21376
  },
  "output_tokens": 3747,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 39922,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 921414500,
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
    "input_tokens": 16180,
    "output_tokens": 3077
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509667878743777287",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509667878743777287"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508516485135839236",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508516485135839236"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508187214198542339",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508187214198542339"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509335418164101126",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509335418164101126"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509376714765443072",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509376714765443072"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508258823382831104",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508258823382831104"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509328827712950276",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509328827712950276"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509615997568917508",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509615997568917508"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509236852011634691",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509236852011634691"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509390147741274115",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509390147741274115"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509619519546875904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509619519546875904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509585271469260805",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509585271469260805"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509312640581095435",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509312640581095435"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509597771065696265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509597771065696265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508886732124606476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508886732124606476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509346309962190848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509346309962190848"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509008465141764101",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509008465141764101"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509659043295543296",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509659043295543296"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509383339475714048",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509383339475714048"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509199354103480328",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509199354103480328"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509347359813259269",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509347359813259269"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508289099861479428",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508289099861479428"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509662333684969510",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509662333684969510"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507840625420521476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507840625420521476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507905643318968321",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507905643318968321"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508920918566916099",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508920918566916099"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507809964127051778",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507809964127051778"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509680414260039681",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509680414260039681"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509577133525508108",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509577133525508108"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509257814912479234",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509257814912479234"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509105935402541059",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509105935402541059"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509295648646045696",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509295648646045696"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509663103411056697",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509663103411056697"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509521211847553024",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509521211847553024"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1508981969115361284",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1508981969115361284"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509295916737388548",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509295916737388548"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509338276578181122",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509338276578181122"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509323290019606533",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509323290019606533"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509128553421492225",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509128553421492225"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509583300645380097",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509583300645380097"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509318228539068416",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509318228539068416"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509355567860568064",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509355567860568064"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1509135563076558848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1509135563076558848"
  }
]
```

## Grok response

```text
**All relevant X/Twitter posts** (from searches across keyword and semantic queries for "Charlie Kirk", TPUSA/Turning Point USA, events/speaking/tours/appearances, specific tour names like "Educate Don't Mandate" or "Saving America Tour", and locations) **from March 26, 2022, through April 1, 2022** (using `since:2022-03-26 until:2022-04-02` where applicable) are included below in full. No summarization—every matching post is listed with its full content, author, timestamp, engagement metrics, and media details where present. Irrelevant or non-matching posts from the results (e.g., unrelated mentions of "Kirk" or general TPUSA without events) have been excluded.

### Posts about the **Educate Don't Mandate Tour** (featuring Charlie Kirk / TPUSA campus events):
- **[post:38]** Author: Andrew Sypher (@AndrewSypher)  
  Timestamp: Thu, 31 Mar 2022 00:36:49 GMT  
  Likes: 69 | Reposts: 8 | Quotes: 4 | Replies: 3 | Bookmarks: 0  
  Content: @charliekirk11's first campus tour stop of 2022 is an absolute success! Nearly 500 students came to hear about #EducateDontMandate at @UArkansas. So proud of our @TPUSA chapter there and personnel: @RickeyAdamJr & @JohnGaltForever!  
  Media: Video (https://video.twimg.com/ext_tw_video/1509327553277964290/pu/vid/1280x720/hfI5LZnqmV53DC-9.mp4?tag=12, duration: 8433 ms)  
  **Replies included in thread fetch:**  
  - @Wreckem1996 (Thu, 31 Mar 2022 17:48:31 GMT): @charliekirk11 - next stop Texas Tech University!  
  - @PapaSmurfSexy (Thu, 31 Mar 2022 17:39:24 GMT): Lots of secret abortions in they audience

- **[post:56]** Author: America First - tyrannide resistere (@Therealbp65)  
  Timestamp: Wed, 30 Mar 2022 23:54:42 GMT  
  Likes: 3 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: At @charliekirk11 “Educate don’t Mandate” tour in Fayetteville Arkansas. About to get things goin! #NoMandates  
  Media: Photo (https://pbs.twimg.com/media/FPIs7YQXoAAJwhF.jpg)

- **[post:57] / [post:39] / [post:31]** Author: Amber Kleinke (@realamber_k96)  
  Timestamp: Wed, 30 Mar 2022 22:26:02 GMT  
  Likes: 105 | Reposts: 50 | Quotes: 8 | Replies: 23 | Bookmarks: 1  
  Content: UC BERKELEY: Leftist rips down Turning Point USA at UC Berkeley’s event flyers for the Educate Don’t Mandate Tour featuring Charlie Kirk. @charliekirk11 @TPUSA  
  Media: Video (https://video.twimg.com/ext_tw_video/1509295852157763585/pu/vid/720x1280/IpTJf9C65SKq7OSo.mp4?tag=12, duration: 20441 ms)

- **[post:35]** Author: Condork (@conndorr)  
  Timestamp: Thu, 31 Mar 2022 17:03:29 GMT  
  Likes: 1 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: @hasanthehun Look at this racist ass poster from the TPUSA event at Rutgers  
  Media: Photo (https://pbs.twimg.com/media/FPMYZtsXMAE600f.jpg)

- **[post:40]** Author: Chris Gaffrey (@ChrisGaffrey)  
  Timestamp: Wed, 30 Mar 2022 19:54:38 GMT  
  Likes: 19 | Reposts: 9 | Quotes: 1 | Replies: 2 | Bookmarks: 0  
  Content: Promoting our #EducateDontMandate Tour at the Michigan Capital!! Make sure to get your tickets and come out to Ann Arbor to see Allie Stuckey, April 11th https://t.co/c1VOZ7TlzG @TPUSA  
  Media: Video (https://video.twimg.com/ext_tw_video/1509257771493036037/pu/vid/588x334/IEiPWVNSmQXi0rFu.mp4?tag=12, duration: 43436 ms)

- **[post:30]** Author: creature (@saintmotherfukr)  
  Timestamp: Thu, 31 Mar 2022 01:03:00 GMT  
  Likes: 1 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: the revolutionaries are here w us at the charlie kirk event ,,,, asking questions doing debates lets goo

- **[post:50]** Author: Shelly Ann titchenel (@shelly35160)  
  Timestamp: Thu, 31 Mar 2022 04:40:28 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Educate Don't Mandate Tour live from the University of Arkansas https://t.co/cfRSE592DJ via @YouTube

- **[post:51]** Author: Minutemen (@m1nu73m3n)  
  Timestamp: Thu, 31 Mar 2022 02:23:04 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Turning Point USA: Educate Don't Mandate Tour live from the University of Arkansas

- **[post:52]** Author: £Ʌ ƿɵ§ꝉɅ ↁᵻ ꟻɅ£¢ɵ₪€ (@PostaDiFalcone)  
  Timestamp: Thu, 31 Mar 2022 01:50:27 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Turning Point USA: Educate Don't Mandate Tour live from the University of Arkansas Turning Point USA proudly presents the Educate Don't Mandate Tour live from the University of Arkansas featuring Charlie Kirk -Special Thanks to Dr Bob-

- **[post:53]** Author: Texans For Israel Mike Isley (@texansforisrael)  
  Timestamp: Thu, 31 Mar 2022 01:46:17 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Educate Don't Mandate Tour live from the University of Arkansas https://t.co/dndYY8gYDQ via @YouTube

- **[post:54]** Author: Nancy Jimenez (@NancyJi08833634)  
  Timestamp: Thu, 31 Mar 2022 01:14:21 GMT  
  Likes: 0 | Reposts: 1 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Watch "Educate Don't Mandate Tour live from the University of Arkansas" on YouTube

- **[post:55]** Author: Willem Hilton (@WillemHilton8)  
  Timestamp: Thu, 31 Mar 2022 00:14:48 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Educate Don't Mandate Tour live from the University of Arkansas https://t.co/5qy1OgFVO9 via @YouTube

### Posts about the **Saving America Tour** (TPUSA Faith with Charlie Kirk):
- **[post:1] / [post:19] / [post:25] / [post:32]** Author: TruTube (@TruTubeTV)  
  Timestamp: Thu, 31 Mar 2022 22:45:06 GMT  
  Likes: 5 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: TPUSA Faith presents the Saving America Tour with Charlie Kirk | Fervent Church #VideoOfTheDay #Bitcast #FreeSpeech✨

- **[post:2] / [post:20] / [post:26] / [post:33]** Author: TruTube (@TruTubeTV)  
  Timestamp: Thu, 31 Mar 2022 22:42:03 GMT  
  Likes: 5 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: TPUSA Faith presents the Saving America Tour with Charlie Kirk | Fervent Church #VideoOfTheDay #Bitcast #FreeSpeech✨

- **[post:60]** Author: Bitcast (@bitcastvideo)  
  Timestamp: Wed, 30 Mar 2022 16:02:20 GMT  
  Likes: 2 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: TPUSA Faith presents the Saving America Tour with Charlie Kirk | Fervent Church #VideoOfTheDay #Bitcast #FreeSpeech✨

- **[post:61]** Author: £Ʌ ƿɵ§ꝉɅ ↁᵻ ꟻɅ£¢ɵ₪€ (@PostaDiFalcone)  
  Timestamp: Wed, 30 Mar 2022 11:48:51 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Turning Point USA: TPUSA Faith presents the Saving America Tour with Charlie Kirk | Fervent Church

- **[post:62]** Author: Minutemen (@m1nu73m3n)  
  Timestamp: Wed, 30 Mar 2022 11:21:00 GMT  
  Likes: 1 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: Turning Point USA: TPUSA Faith presents the Saving America Tour with Charlie Kirk | Fervent Church

- **[post:63]** Author: Matt Hay (@MattHayOriginal)  
  Timestamp: Wed, 30 Mar 2022 03:23:48 GMT  
  Likes: 17 | Reposts: 5 | Quotes: 3 | Replies: 0 | Bookmarks: 0  
  Content: Saving America Tour at Fervent Church tonight!!! Well done!!! #TPUSAFAITH @charliekirk11  
  Media: Photo (https://pbs.twimg.com/media/FPETMtPVsAEi8Lx.jpg)

### Other TPUSA-related posts mentioning events or speaking (general):
- **[post:7]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 28 Mar 2022 01:45:00 GMT  
  Likes: 40 | Reposts: 18 | Quotes: 1 | Replies: 6 | Bookmarks: 1  
  Content: “If you are questioning what government can do… Just look at the past two years” @JonnyRoot_ Was there a specific event or moment that made you stop trusting big gov? Tell us below 👇  
  Media: Video (https://video.twimg.com/amplify_video/1506318508925222913/vid/720x720/Fd62iKx40ytfRumi.mp4?tag=14, duration: 40807 ms)

- **[post:8]** Author: Turning Point USA (@TPUSA)  
  Timestamp: Sun, 27 Mar 2022 02:21:35 GMT  
  Likes: 61 | Reposts: 17 | Quotes: 2 | Replies: 12 | Bookmarks: 0  
  Content: Should conservatives leave a platform that doesn’t support free speech?🤔 @TheIsabelB doesn’t think so.👇 “Culture lives on those big tech platforms, & if we don’t speak the truth… They will never be exposed to that way of thinking.” What do you think?  
  Media: Video (https://video.twimg.com/amplify_video/1507867475542564866/vid/720x720/Bk1iMLvhT1fze9T9.mp4?tag=14, duration: 64531 ms)

- **[post:34]** Author: Isabel Brown (@theisabelb)  
  Timestamp: Thu, 31 Mar 2022 17:28:00 GMT  
  Likes: 7 | Reposts: 1 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: LADIES LADIES LADIES -- I hope you will join me this summer in Dallas for @TPUSA's Young Women's Leadership Summit! It's my fave event every year!! You can use code "ISABEL" for a discount on your ticket price here 👉 https://t.co/Ys0KifdTfR  
  Media: Photo (https://pbs.twimg.com/media/FOtfsX7VUAAuvpa.jpg)

- **[post:37]** Author: Wonder TRUMP2024 (@wonderworld2016)  
  Timestamp: Thu, 31 Mar 2022 03:47:06 GMT  
  Likes: 12 | Reposts: 22 | Quotes: 0 | Replies: 0 | Bookmarks: 0  
  Content: This is Amazing! GREAT event by #TPUSA!! https://t.co/STbSfwJO8i  
  Media: Photo (https://pbs.twimg.com/media/FPJiH3AX0AYSjtP.jpg)

No posts were found from @charliekirk11 in the date range matching the search criteria. No additional direct announcements of future speaking locations or schedules appeared in the results beyond the tour stops and events noted above. All data from the tool results has been exhaustively included.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-03-26 to 2022-04-01**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-03-26 to 2022-04-01 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
