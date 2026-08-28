---
unlisted: true
title: "Week 36 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W36"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-09-02 to 2024-09-08."
status: completed
hide_table_of_contents: true
---

# Week 36, 2024

- Date range: 2024-09-02 to 2024-09-08
- Queried at (UTC): 2026-08-24T19:14:54Z
- Model: grok-4.3
- API status: completed
- Response id: f7b85678-8b67-96df-8430-a4cd5c1f2b03

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-09-02 to the end of the week 2024-09-08.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR campus OR \"will be\" OR speaking OR speech) since:2024-09-02 until:2024-09-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR \"speaking event\" OR \"will speak\" OR appearance) since:2024-09-02 until:2024-09-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between September 2-8 2024",
      "limit": "10",
      "from_date": "2024-09-02",
      "to_date": "2024-09-08"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"Courage Tour\" OR AmFest) (event OR speaking OR speak OR tour OR appearance OR \"town hall\" OR campus OR speech OR \"will be speaking\" OR \"will speak\") since:2024-09-02 until:2024-09-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"town hall\" OR campus OR speech OR Arizona OR Wisconsin OR Tucson) since:2024-09-02 until:2024-09-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"town hall\" OR campus OR speech OR AmFest) since:2024-09-02 until:2024-09-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA speaking events, campus events, tours, town halls, or appearances in early September 2024, especially Arizona, Wisconsin, or December",
      "limit": "10",
      "from_date": "2024-09-02",
      "to_date": "2024-09-08"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 20779,
  "input_tokens_details": {
    "cached_tokens": 10368
  },
  "output_tokens": 6100,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 26879,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 653373500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 7,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 11893,
    "output_tokens": 5633
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831547984410300593",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831547984410300593"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831746525367824891",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831746525367824891"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832546678672417083",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832546678672417083"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832385969636434355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832385969636434355"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832542023804416335",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832542023804416335"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831540375145914531",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831540375145914531"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831749755388445000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831749755388445000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832306998701941199",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832306998701941199"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1830813987325485147",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1830813987325485147"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831754671419224165",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831754671419224165"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831867352365093060",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831867352365093060"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832497221708759373",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832497221708759373"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832559038636192057",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832559038636192057"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832426333416108375",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832426333416108375"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832539341563764864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832539341563764864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832114547307770290",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832114547307770290"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832526519912296461",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832526519912296461"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832363642601234604",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832363642601234604"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832184322222371045",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832184322222371045"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832529137535508970",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832529137535508970"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832124016871780396",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832124016871780396"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831062670285394140",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831062670285394140"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832433381155770813",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832433381155770813"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831391838064013766",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831391838064013766"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1831805323168162040",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1831805323168162040"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1832433701826806143",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1832433701826806143"
  }
]
```

## Grok response

```text
**Here is a complete, unsummarized compilation of all relevant X posts from the specified date range (2024-09-02 to 2024-09-08, using searches up to 2024-09-09 to capture the full week).** I used keyword searches for terms like "Charlie Kirk", TPUSA, "Turning Point", "Courage Tour", AmFest, combined with event/speaking/tour/appearance/town hall/campus/speech indicators, plus targeted searches from @charliekirk11 and @TPUSA accounts. A semantic search was also performed for broader relevance to speaking events, tours, town halls, or appearances in early September 2024 (especially Arizona, Wisconsin, or December). No posts were excluded; all matching or contextually relevant results are listed in full below, including post ID, author, timestamp (GMT), engagement metrics, media (if any), and exact content. Duplicates across searches are preserved for completeness where they appeared.

Posts are ordered by approximate recency within the tool results (newest first where available). Note that @TPUSA-specific keyword search returned no results in the range.

### Key relevant posts mentioning events, speaking, tours, appearances, or locations (Sept 2-8, 2024):

- **[post:9]** ID: 1832433381155770813  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sat, 07 Sep 2024 14:58:57 GMT  
  Engagement: Likes=4568, Reposts=743, Quotes=11, Replies=179, Bookmarks=15, Views=109347  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW4ccnca8AIzXUL.jpg  
  Content: Amazing event in TUCSON last night to wrap up a huge week.  
  We had 2,500 people in the MUST WIN state of Arizona.  
  We are chasing ballots and creating the army to WIN!  
  🇺🇸🇺🇸

- **[post:14]** ID: 1832124016871780396  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 06 Sep 2024 18:29:39 GMT  
  Engagement: Likes=3410, Reposts=851, Quotes=54, Replies=291, Bookmarks=67, Views=793888  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW0COMObsAAZnAx.jpg  
  Content: 🚨HUGE ANNOUNCEMENT🚨  
  Turning Point Action and TPPAC are honored to host a MAKE AMERICA HEALTHY AGAIN TOWN HALL featuring the great @RobertKennedyJr and @calleymeans.  
  Sept. 17th at 6:30pm MST in Old Town Scottsdale, AZ  
  Register for tickets 👉 https://t.co/CkaTihATZb  
  🇺🇸🇺🇸

- **[post:15]** ID: 1831547984410300593  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 05 Sep 2024 04:20:42 GMT  
  Engagement: Likes=39484, Reposts=7684, Quotes=160, Replies=887, Bookmarks=349, Views=838045  
  Media: Yes (3 items) - video URLs: https://video.twimg.com/amplify_video/1831547262792822785/vid/avc1/360x640/eGFMTkxPQEJk2h7O.mp4?tag=16 (duration: 14776 ms), https://video.twimg.com/amplify_video/1831547262947782656/vid/avc1/640x344/Bxw1T_KlFwA2BK45.mp4?tag=16 (duration: 79551 ms), https://video.twimg.com/amplify_video/1831547262792822784/vid/avc1/352x640/JVR6wubHcixDr9DU.mp4?tag=16 (duration: 11733 ms)  
  Content: Hero’s welcome for Trump on Fox.  
  Massive sellout crowd for Tucker in Phoenix.  
  Packed house, max-capacity for JD Vance in Mesa, AZ.  
  ALL IN ONE NIGHT!!  
  Can you feel the momentum surging?

- **[post:16]** ID: 1831746525367824891  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 05 Sep 2024 17:29:38 GMT  
  Engagement: Likes=27916, Reposts=5568, Quotes=150, Replies=818, Bookmarks=225, Views=577324  
  Media: Yes (1 item) - video URL: https://video.twimg.com/amplify_video/1831746470581612544/vid/avc1/720x1280/tgte4_lIFlbO4Wqf.mp4?tag=14 (duration: 7300 ms)  
  Content: MASSIVE crowd already at the University of Wisconsin, Madison.  
  @tpaction is on the ground registering new voters, doing the work it takes to win.  
  🔥🔥🔥

- **[post:20]** ID: 1831391838064013766  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 04 Sep 2024 18:00:14 GMT  
  Engagement: Likes=707, Reposts=206, Quotes=41, Replies=85, Bookmarks=9, Views=172464  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GWpgI9tWgAA_nBT.jpg  
  Content: Our first speaker drop for #AmFest2024 is HERE! Who are you most excited to hear from?  
  Head to https://www.amfest.com/ to register NOW & get 50% off all GA passes with our Early Bird deal until Sep. 6, 2024, at 11:59 PM PST

- **[post:28]** ID: 1831867352365093060  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 06 Sep 2024 01:29:45 GMT  
  Engagement: Likes=3764, Reposts=871, Quotes=27, Replies=150, Bookmarks=51, Views=128997  
  Media: Yes (2 items) - photo URLs: https://pbs.twimg.com/media/GWwZpOAXYAAP6Xl.jpg, https://pbs.twimg.com/media/GWwZoqwWoAAjHRQ.jpg  
  Content: According to local media reports, "a few dozen" students turned out to our Prove Me Wrong tabling event at UW Madison.  
  The few dozen:

- **[post:29]** ID: 1831754671419224165  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 05 Sep 2024 18:02:00 GMT  
  Engagement: Likes=33596, Reposts=6034, Quotes=128, Replies=823, Bookmarks=118, Views=434608  
  Media: Yes (3 items) - photo URLs: https://pbs.twimg.com/media/GWuzKawa8AMBoTP.jpg, https://pbs.twimg.com/media/GWuzKbSWoAAZ3A3.jpg, https://pbs.twimg.com/media/GWuzKava8AEg-ZF.jpg  
  Content: 120 new voters in just 2 hours at the University of Wisconsin Madison, and we’re just getting started!  
  This is how we win. This is how we take back the country. 🇺🇸  
  @tpaction

- **[post:34]** ID: 1831749755388445000  
  Author: Morgonn McMichael Brown (@Morgonn)  
  Timestamp: Thu, 05 Sep 2024 17:42:28 GMT  
  Engagement: Likes=218, Reposts=37, Quotes=1, Replies=12, Bookmarks=3, Views=11568  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GWuusIKWcAERpmd.jpg  
  Content: The You’re Being Brainwashed Tour by @TPUSA is here!!! Kicking off @UWBadgers in Madison WI! Students gathered to debate and hear from @charliekirk11 in the rain🇺🇸

- **[post:35]** ID: 1831540375145914531  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 05 Sep 2024 03:50:28 GMT  
  Engagement: Likes=9196, Reposts=1594, Quotes=23, Replies=200, Bookmarks=63, Views=137063  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GWrwJguXIAERRWd.jpg  
  Content: Absolutely packed house for JD Vance in Arizona tonight!!  
  2,000+ at Generation Church in Mesa all while Trump held a town hall on Fox and Tucker and Russell Brand packed out another arena in Phoenix. So much in depth policy discussed between both Trump and JD, addressing dozens of issues versus Harris and Walz who have given a grand total of 1 joint interview, 0 solo interviews, and 0 press conferences in the last 45 days.  
  Those with something to hide should not be trusted to run the country.

- **[post:3]** ID: 1832539341563764864  
  Author: PatriotTakes 🇺🇸 (@patriottakes)  
  Timestamp: Sat, 07 Sep 2024 22:00:00 GMT  
  Engagement: Likes=200, Reposts=66, Quotes=5, Replies=33, Bookmarks=5, Views=47291  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW05ZiQWcAAIGeL.jpg  
  Content: Tucker Carlson hosted a Nazi apologist and is now a confirmed speaker for Charlie Kirk’s December event.

- **[post:8]** ID: 1832497221708759373  
  Author: avis prede 🌻🕊️ (@iheartospreys)  
  Timestamp: Sat, 07 Sep 2024 19:12:38 GMT  
  Engagement: Likes=0, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=28  
  Content: Tell the Monroeville (PA) Convention Center: White Christian nationalism is bad for business - don't host "prophet" Lance Wallnau and TPUSA's Charlie Kirk's "Courage Tour"   👎🏼  
  https://act.faithfulamerica.org/sign/courage-tour-monroeville?akid=s642507..sPCs-x

- **[post:11]** ID: 1832385969636434355  
  Author: Madeline Brame (@brame_madeline)  
  Timestamp: Sat, 07 Sep 2024 11:50:33 GMT  
  Engagement: Likes=13, Reposts=3, Quotes=0, Replies=1, Bookmarks=0, Views=446  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW3xU8UXcAAmkbh.jpg  
  Content: ALL NYC @BlexitNY members are invited and encouraged to attend this event. Scan the QR Code to register. @TPUSA

- **[post:0]** ID: 1832559038636192057  
  Author: Rob😎 (@CannabisandCafe)  
  Timestamp: Sat, 07 Sep 2024 23:18:16 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=183  
  Media: Yes (2 items) - photo URLs: https://pbs.twimg.com/media/GW6OuT2XsAAeEnr.jpg, https://pbs.twimg.com/media/GW6OuTzWMAA03QZ.jpg  
  Content: Yeah but she’s never faced any consequences for her biggest lie  
  Remember that is what got her “popular” with the anti-trans crowd.  
  That’s a picture from the event…  
  She waited for everyone else to show up and protest her vile disgusting bigotry.   
  She & TPUSA planned it…imo🤨

- **[post:17]** ID: 1832539341563764864 (duplicate of post:3)  
  Author: PatriotTakes 🇺🇸 (@patriottakes)  
  Timestamp: Sat, 07 Sep 2024 22:00:00 GMT  
  Engagement: Likes=200, Reposts=66, Quotes=5, Replies=33, Bookmarks=5, Views=47291  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW05ZiQWcAAIGeL.jpg  
  Content: Tucker Carlson hosted a Nazi apologist and is now a confirmed speaker for Charlie Kirk’s December event.

- **[post:18]** ID: 1832184322222371045  
  Author: Chuck Callesto (@ChuckCallesto)  
  Timestamp: Fri, 06 Sep 2024 22:29:17 GMT  
  Engagement: Likes=607, Reposts=103, Quotes=3, Replies=17, Bookmarks=3, Views=18762  
  Content: BREAKING REPORT: Turning Point Action and TPPAC to host a MAKE AMERICA HEALTHY AGAIN town hall with RFK Jr.    
  DEVELOPING..

- **[post:19]** ID: 1832433701826806143  
  Author: Bryce M. Lipscomb (@BryceMLipscomb)  
  Timestamp: Sat, 07 Sep 2024 15:00:14 GMT  
  Engagement: Likes=496, Reposts=177, Quotes=4, Replies=15, Bookmarks=8, Views=7489  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW4cvTbXkAAEzwJ.jpg  
  Content: BIG NEWS🚨🚨:  
  The amazing @charliekirk11 will be promoting #MAHA & #MAGA UNITY by hosting a town hall with @RobertKennedyJr & @calleymeans.  
  I WILL NOT BE MISSING THIS, & I hope you won’t. Let’s Make America Great & Healthy Again.

- **[post:21]** ID: 1831805323168162040  
  Author: Ashley Nicole🌺 (@antiwarmisfit)  
  Timestamp: Thu, 05 Sep 2024 21:23:16 GMT  
  Engagement: Likes=192, Reposts=38, Quotes=1, Replies=8, Bookmarks=4, Views=3507  
  Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1831804998558044160/pu/vid/avc1/720x1600/-yQ6Qak6WkeGlaca.mp4?tag=12 (duration: 37268 ms)  
  Content: Tucker Carlson Live featuring Tulsi Gabbard on September 6 in Colorado Springs, CO  
  A few tickets are still available!   
  https://t.co/D9psiQJd7Q

- **[post:36]** ID: 1831062670285394140  
  Author: Eric Daugherty (@EricLDaugh)  
  Timestamp: Tue, 03 Sep 2024 20:12:14 GMT  
  Engagement: Likes=528, Reposts=116, Quotes=9, Replies=14, Bookmarks=22, Views=20492  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GWk7LPIWgAA8W7v.jpg  
  Content: 🚨 Trump campaign's swing state blitz this week  
  TONIGHT, 6PM ET: Braselton, Ga. - policy tour  
  TONIGHT, 6PM PT: Mesa, Ariz. - policy tour  
  TOMORROW, 9PM ET: Harrisburg, Pa. - Trump town hall  
  THURSDAY, 3PM MT: Phoenix, Ariz. - @JDVance  
  THURSDAY, 7PM CT: Milwaukee, Wis. - policy tour  
  SATURDAY, 1PM CT: Mosinee, Wis. - Trump rally.

- **[post:37]** ID: 1831391838064013766 (duplicate of post:20)  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 04 Sep 2024 18:00:14 GMT  
  Engagement: Likes=707, Reposts=206, Quotes=41, Replies=85, Bookmarks=9, Views=172464  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GWpgI9tWgAA_nBT.jpg  
  Content: Our first speaker drop for #AmFest2024 is HERE! Who are you most excited to hear from?  
  Head to https://www.amfest.com/ to register NOW & get 50% off all GA passes with our Early Bird deal until Sep. 6, 2024, at 11:59 PM PST

### Other posts in the search results (contextual or less directly event-specific, but included for full data):

- **[post:1]** ID: 1832546678672417083  
  Author: We Are Charlie Kirk (@CLK1341104)  
  Timestamp: Sat, 07 Sep 2024 22:29:09 GMT  
  Engagement: Likes=12, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=621  
  Content: Please, Mr. Cleese Speak out against this free speech violations, happening in your home country.

- **[post:2]** ID: 1832542023804416335  
  Author: Modern Populist (@modern_populist)  
  Timestamp: Sat, 07 Sep 2024 22:10:40 GMT  
  Engagement: Likes=0, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=64  
  Content: She was at the Trump rally in Wisconsin today. Sang and then gave a nice speech.

- **[post:4]** ID: 1832529137535508970  
  Author: InfantryCop (@Infantry828)  
  Timestamp: Sat, 07 Sep 2024 21:19:27 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=16  
  Content: That struck me as an odd statement. We can't say free speech and civil discourse always, EXCEPT for WWII (or insert any other subject).

- **[post:5]** ID: 1832526519912296461  
  Author: CJ Az 🇺🇲🦅💙 (@jackman_christy)  
  Timestamp: Sat, 07 Sep 2024 21:09:03 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=12  
  Content: I'm saying the big payday will be TPUSA

- **[post:6]** ID: 1832559038636192057 (duplicate of post:0)  
  Author: Rob😎 (@CannabisandCafe)  
  Timestamp: Sat, 07 Sep 2024 23:18:16 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=183  
  Media: Yes (2 items) - photo URLs: https://pbs.twimg.com/media/GW6OuT2XsAAeEnr.jpg, https://pbs.twimg.com/media/GW6OuTzWMAA03QZ.jpg  
  Content: Yeah but she’s never faced any consequences for her biggest lie  
  Remember that is what got her “popular” with the anti-trans crowd.  
  That’s a picture from the event…  
  She waited for everyone else to show up and protest her vile disgusting bigotry.   
  She & TPUSA planned it…imo🤨

- **[post:7]** ID: 1832539341563764864 (duplicate of post:3)  
  Author: PatriotTakes 🇺🇸 (@patriottakes)  
  Timestamp: Sat, 07 Sep 2024 22:00:00 GMT  
  Engagement: Likes=200, Reposts=66, Quotes=5, Replies=33, Bookmarks=5, Views=47291  
  Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/GW05ZiQWcAAIGeL.jpg  
  Content: Tucker Carlson hosted a Nazi apologist and is now a confirmed speaker for Charlie Kirk’s December event.

- **[post:10]** ID: 1832426333416108375  
  Author: Jesse formerly known as Darth Crypto (@DefNotDarth)  
  Timestamp: Sat, 07 Sep 2024 14:30:57 GMT  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=42  
  Content: Or option 5, wishful thinking. I need everybody to suffer and the lowest of lower lows to come as I continue to save up capital for my epic comeback tour.

- **[post:12]** ID: 1832363642601234604  
  Author: ParentChain #AnnWiddecombe (@parentchain)  
  Timestamp: Sat, 07 Sep 2024 10:21:50 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=127  
  Content: Singing the national anthem before a sporting event is normal. BTW, many media supported Hitler just like Time Magazine in America had Hitler on its cover as "Man of the Year." Everyone thought Hitler was great at the beginning. The Guardian owned slaves, complain about that!  
  (Quoted post about another topic)

- **[post:13]** ID: 1832306998701941199  
  Author: Nathan Greene (@17NGreene76)  
  Timestamp: Sat, 07 Sep 2024 06:36:45 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=80  
  Content: Looking forward to the interview. I binge watched survivor interviews and documentaries during the last anniversary of the attack, so I think I have a strong idea of what this survivor may say  
  He'd probably smack Charlie Kirk across the room for dismissing it as a made up event

- **[post:22]** ID: 1830813987325485147  
  Author: Commentary Donald J. Trump Posts From Truth Social (@TrumpDailyPosts)  
  Timestamp: Tue, 03 Sep 2024 03:44:04 GMT  
  Engagement: Likes=2376, Reposts=759, Quotes=10, Replies=138, Bookmarks=16, Views=79635  
  Content: Join me in Harrisburg, Pennsylvania this Wednesday, September 4th—at 5:30PM Eastern, for a Town Hall. Get your tickets today at https://hannitytownhall.fox-newschannel.com/ Look forward to seeing you there—MAGA2024!!!  
  Donald Trump Truth Social 11:16 PM EST 09/02/24 @realDonaldTrump

- **[post:23]** ID: 1832559038636192057 (duplicate of post:0)  
  (Same as above)

- **[post:24]** ID: 1832546678672417083 (duplicate of post:1)  
  (Same as above)

- **[post:25]** ID: 1832433381155770813 (duplicate of post:9)  
  (Same as above)

- **[post:26]** ID: 1832124016871780396 (duplicate of post:14)  
  (Same as above)

- **[post:27]** ID: 1832114547307770290  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 06 Sep 2024 17:52:01 GMT  
  Engagement: Likes=20975, Reposts=4865, Quotes=243, Replies=1791, Bookmarks=472, Views=641920  
  Content: Donald Trump's sentencing was the last predictable "big event" Democrats could look forward to as a way to hurt Donald Trump. Now, it's gone.  
  So, what do they have left? One possibility we've never had to consider before: A fake October surprise. The technology now exists to produce an audio recording of Trump saying something offensive or criminal, which sounds entirely real to the untrained ear but is actually fake.  
  Four years ago, "intelligence experts" and the press nakedly lied about the Hunter Biden laptop, calling it a Russian fake when it was obviously real and censoring the story. If they feel desperate enough about this election, what are the odds they would do the opposite: Run interference for a deepfake, calling it real or, at the least, "impossible to disprove?"  
  I don't know what the left has planned. But we have to be ready for anything, because they are capable of anything.

- **[post:30]** ID: 1832124016871780396 (duplicate of post:14)  
  (Same as above)

- **[post:31]** ID: 1831746525367824891 (duplicate of post:16)  
  (Same as above)

- **[post:32]** ID: 1831547984410300593 (duplicate of post:15)  
  (Same as above)

- **[post:33]** ID: 1832433381155770813 (duplicate of post:9)  
  (Same as above)

- **[post:38]** ID: 1832539341563764864 (duplicate of post:3)  
  (Same as above)

This exhausts all results from the tool calls within the date range. No additional posts were found in the searches. All data is presented exactly as returned.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-09-02 to 2024-09-08**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-09-03](/Planes/Incidents/N560TW-2024-09-03-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | **Same day** |
| [2024-09-04](/Planes/Incidents/N2100L-2024-09-04-KMSN) | [N2100L](/Planes/N2100L/overview) | [KMSN](/Planes/Airports/KMSN) | Madison, WI | Charlie | Day before |
| [2024-09-04](/Planes/Incidents/N560TW-2024-09-04-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2024-09-04](/Planes/Incidents/N582MM-2024-09-04-KPHX) | [N582MM](/Planes/N582MM/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day after |
| [2024-09-05](/Planes/Incidents/N582MM-2024-09-05-KMSN) | [N582MM](/Planes/N582MM/overview) | [KMSN](/Planes/Airports/KMSN) | Madison, WI | Charlie | **Same day** |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
