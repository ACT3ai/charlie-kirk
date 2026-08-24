---
unlisted: true
title: "Week 42 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W42"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-10-15 to 2023-10-21."
status: completed
hide_table_of_contents: true
---

# Week 42, 2023

- Date range: 2023-10-15 to 2023-10-21
- Queried at (UTC): 2026-08-24T19:09:26Z
- Model: grok-4.3
- API status: completed
- Response id: 6c934ead-0aee-9a6c-a9cb-8590a33da285

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-10-15 to the end of the week 2023-10-21.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"will be\" OR appears OR appearance) since:2023-10-15 until:2023-10-22",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (campus OR college OR university) (tour OR speaking OR event) since:2023-10-15 until:2023-10-22",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, appearances, or where Charlie Kirk will speak between October 15-21 2023",
      "limit": "10",
      "from_date": "2023-10-15",
      "to_date": "2023-10-21"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR TPUSA) since:2023-10-15 until:2023-10-22",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Charlie Kirk",
      "count": "3"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 12822,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 2705,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 15527,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 445644000,
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
    "input_tokens": 11232,
    "output_tokens": 2455
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/wku_tpusa/status/1715499344458133780",
    "start_index": 320,
    "end_index": 377,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1715155218202313090",
    "start_index": 377,
    "end_index": 438,
    "title": "2"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range (2023-10-15 to 2023-10-21, using until:2023-10-22 to capture the full week) mentioning Charlie Kirk, TPUSA, or Turning Point USA in connection with public speaking events, appearances, tours, campus stops, or where Charlie will speak are included below without summarization.**[[1]](https://x.com/wku_tpusa/status/1715499344458133780)[[2]](https://x.com/charliekirk11/status/1715155218202313090)

These were found via keyword and semantic searches focused on the specified period. Only posts with direct relevance to events/speaking (not general commentary) are listed; unrelated or off-topic posts from the results (e.g., debates on guns, circumcision, or unrelated politics) are excluded. Posts are presented in the order returned by the tools, with full original content, author, timestamp (GMT), engagement, and media notes where applicable. No content was altered.

### Posts from TPUSA-affiliated or event-related accounts:
- **Post [post:0] / [post:8]** (ID: 1715499344458133780)  
  Author: TPUSA at Western Kentucky University (@wku_tpusa)  
  Timestamp: Fri, 20 Oct 2023 22:44:50 GMT  
  Content: Thank you to everyone who came to our event with @ighaworth last night! We had an amazing turnout and a great discussion about the pro-life movement!  

  Huge thank you to @ighaworth for coming to speak with us, be sure to give him a follow!  
  Engagement: Likes=264, Reposts=36, Quotes=3, Replies=15, Bookmarks=0, Views=81640  
  Media: 3 photos (URLs: https://pbs.twimg.com/media/F86tjvtXsAAedbf.jpg, https://pbs.twimg.com/media/F86tjvuXkAAaNdl.jpg, https://pbs.twimg.com/media/F86tjvtXoAAxKOz.jpg)

- **Post [post:5]** (ID: 1715437424199729296)  
  Author: Kelli (@AriesBorn1982)  
  Timestamp: Fri, 20 Oct 2023 18:38:47 GMT  
  Content: TPUSA presents the LIVE FREE TOUR with Charlie Kirk LIVE from Missouri S... https://t.co/9wOxV2xYNf via @YouTube  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=14

- **Post [post:7] / [post:11]** (ID: 1715422525277302959)  
  Author: Sam Johnson (@merican_mullet1)  
  Timestamp: Fri, 20 Oct 2023 17:39:35 GMT  
  Content: It was a boot scootin’ time up in Montana this week!  

  The @TPUSA chapter at the University of Montana hosted their annual “Camouflage and cowboy boots” line dancing event! With over 90+ students coming out to cut up a rug and learn about conservative values!  

  @tpusastudents  
  Engagement: Likes=5, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=409  
  Media: 1 photo (URL: https://pbs.twimg.com/media/F85npewaIAAIgUL.jpg), 1 video (URL: https://video.twimg.com/ext_tw_video/1715422470403174400/pu/vid/avc1/720x1280/NvBvnoaae7RzkUle.mp4?tag=12, duration: 7606 ms)

### Posts from Charlie Kirk (@charliekirk11) and @TPUSA:
- **Post [post:12] / [post:13] / [post:23]** (ID: 1715155218202313090)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 19 Oct 2023 23:57:24 GMT  
  Content: The @TPUSA LIVE FREE TOUR at Missouri State University is at MAX CAPACITY 🇺🇸  

  WATCH LIVE:  
  https://t.co/C2fSJBeXWH  
  Engagement: Likes=663, Reposts=117, Quotes=5, Replies=84, Bookmarks=3, Views=168339  
  Media: 1 video (URL: https://video.twimg.com/ext_tw_video/1715155041781530624/pu/vid/avc1/720x1280/fuGU3GwOUgJKLoOk.mp4?tag=12, duration: 21100 ms)  
  (Quoted post from @TPUSA: TPUSA presents the LIVE FREE TOUR with Charlie Kirk LIVE from Missouri State University https://twitter.com/i/broadcasts/1eaJbgElRQQxX – Likes=71, Reposts=22, Quotes=4, Replies=12, Bookmarks=6, Views=182951)

- **Post [post:14]** (ID: 1714808540207198718)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 19 Oct 2023 00:59:50 GMT  
  Content: PACKED HOUSE AT UNIVERSITY OF TEXAS SAN ANTONIO!!  

  Let’s go! 🔥🔥  

  @TPUSA’s Live Free Tour rolls on.  
  Engagement: Likes=1518, Reposts=193, Quotes=1, Replies=85, Bookmarks=5, Views=104195  
  Media: 1 video (URL: https://video.twimg.com/ext_tw_video/1714808500235476992/pu/vid/avc1/720x1280/7YUmrVR-4Nd148Yj.mp4?tag=12, duration: 14533 ms)

- **Post [post:15]** (ID: 1714818004788424742)  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 19 Oct 2023 01:37:26 GMT  
  Content: A PACKED HOUSE TONIGHT for @charliekirk11 at UT San Antonio 🇺🇸  

  Catch Charlie on the Live Free Tour at a stop near you: https://t.co/lXB1OxFoml  
  Engagement: Likes=205, Reposts=33, Quotes=1, Replies=18, Bookmarks=0, Views=16021  
  Media: 1 video (URL: https://video.twimg.com/amplify_video/1714817934521151488/vid/avc1/720x1280/ZH2_Nyd175qsQTWu.mp4?tag=14, duration: 13446 ms)

- **Post [post:16] / [post:28]** (ID: 1714283216075727051)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Tue, 17 Oct 2023 14:12:23 GMT  
  Content: Packed house for another @TPUSA high school chapter event. This one is a majority minority high school. We are reaching the next generation daily. Join us tomorrow in San Antonio, TX and on Thursday in Springfield, MO!  
  Engagement: Likes=1013, Reposts=147, Quotes=6, Replies=71, Bookmarks=3, Views=86878  
  Media: 1 photo (URL: https://pbs.twimg.com/media/F8pbf4rbQAA02iw.jpg)

- **Post [post:24]** (ID: 1714821176634306881)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 19 Oct 2023 01:50:03 GMT  
  Content: Our @TPUSA chapter at UT San Antonio is incredible. Very proud of this team. They represent the frontline on America’s college campuses and they’re stranding stronger than ever!  

  🇺🇸🇺🇸🇺🇸  
  Engagement: Likes=634, Reposts=93, Quotes=3, Replies=71, Bookmarks=1, Views=97763  
  Media: 4 photos (URLs: https://pbs.twimg.com/media/F8xExXda0AAPAE8.jpg, https://pbs.twimg.com/media/F8xExXbbMAA8RFT.jpg, https://pbs.twimg.com/media/F8xExXbbYAA0ePA.jpg, https://pbs.twimg.com/media/F8xExXabcAAUx91.jpg)

### Additional related posts (mentions of events, cancellations, or TPUSA speaking):
- **Post [post:3] / [post:9]** (ID: 1715454151193149535)  
  Author: AudioBoomer (@audio_boomer)  
  Timestamp: Fri, 20 Oct 2023 19:45:15 GMT  
  Content: Get your tickets to the next TPUSA event!  Watch Charlie Kirk debate a hapless college kid then drop an edited video in social media, making himself look like a badass! 

  Next up:  Charlie travels to grammar schools and debates 2nd and 3rd graders 

  Coming to a venue near you!  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=47

- **Post [post:6] / [post:10]** (ID: 1715430045785985187)  
  Author: Matt Fleming (@FlemingWords)  
  Timestamp: Fri, 20 Oct 2023 18:09:28 GMT  
  Content: It's quaint to think about how concerned students and Sac Bee were about Charlie Kirk speaking on campus.  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=96

- **Post [post:19]** (ID: 1714491507258908946)  
  Author: azcentral (@azcentral)  
  Timestamp: Wed, 18 Oct 2023 04:00:03 GMT  
  Content: Scottsdale high school cancels visit from Turning Point USA founder Charlie Kirk https://www.azcentral.com/story/news/local/scottsdale-education/2023/10/17/scottsdale-high-school-cancels-visit-from-turning-point-usa-founder/71210680007/?utm_campaign=snd-autopilot&cid=twitter_azcentral  
  Engagement: Likes=634, Reposts=74, Quotes=17, Replies=145, Bookmarks=5, Views=72801

- **Post [post:22]** (ID: 1715175740541686089)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 20 Oct 2023 01:18:57 GMT  
  Content: I hope you do  
  Engagement: Likes=11, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=472  
  (Reply in context of prior tour/event discussion)

**No other posts in the search results directly announced or referenced Charlie Kirk/TPUSA speaking events, tours, or appearances strictly within October 15–21, 2023.** Additional searches for @TPUSA account activity or broader campus tour keywords yielded overlapping results already listed (primarily the Live Free Tour stops at UT San Antonio on/around Oct 18–19 and Missouri State University on Oct 19). Charlie Kirk's own account (@charliekirk11) was the primary source for real-time event updates.
```

