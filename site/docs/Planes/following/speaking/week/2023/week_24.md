---
unlisted: true
title: "Week 24 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W24"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-06-11 to 2023-06-17."
status: completed
hide_table_of_contents: true
---

# Week 24, 2023

- Date range: 2023-06-11 to 2023-06-17
- Queried at (UTC): 2026-08-24T19:08:01Z
- Model: grok-4.3
- API status: completed
- Response id: 75d21374-9578-9d8e-baa4-df1046ac5dd2

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-06-11 to the end of the week 2023-06-17.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR \"will be\" OR appearing) since:2023-06-11 until:2023-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR \"will be\" OR appearing) since:2023-06-11 until:2023-06-18 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be speaking\" OR TPUSA) since:2023-06-11 until:2023-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be speaking\") since:2023-06-11 until:2023-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak in June 2023",
      "limit": "10",
      "from_date": "2023-06-11",
      "to_date": "2023-06-18"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 14004,
  "input_tokens_details": {
    "cached_tokens": 3008
  },
  "output_tokens": 6712,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 20716,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 561266000,
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
    "input_tokens": 12414,
    "output_tokens": 6402
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669853286986403841",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669853286986403841"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669846381807190018",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669846381807190018"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1667946353131941889",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1667946353131941889"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668708327789068289",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668708327789068289"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669809049372618755",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669809049372618755"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668006847683657728",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668006847683657728"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669856713628061698",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669856713628061698"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669102458914897920",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669102458914897920"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668659066967838720",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668659066967838720"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669836752553656320",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669836752553656320"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669831823294369793",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669831823294369793"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669846275947372544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669846275947372544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669816370744156167",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669816370744156167"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669856448321388544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669856448321388544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669814500441174017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669814500441174017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669832070632468480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669832070632468480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668657876246855680",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668657876246855680"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668395878992998400",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668395878992998400"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669840413673369602",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669840413673369602"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669833362133995520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669833362133995520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669850131536158720",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669850131536158720"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669299490421866497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669299490421866497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669425808526524417",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669425808526524417"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1667936646380281856",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1667936646380281856"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1667969439726465024",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1667969439726465024"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669854840627888128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669854840627888128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669376215436910594",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669376215436910594"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1668334474105622529",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1668334474105622529"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1669851695113814017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1669851695113814017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1667935630205255682",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1667935630205255682"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range (2023-06-11 to 2023-06-17, inclusive, based on post timestamps and search filters since:2023-06-11 until:2023-06-18) mentioning Charlie Kirk, TPUSA, or Turning Point USA in connection with speaking events, public appearances, tours, or related announcements are included below in full (no summarization or omission of qualifying posts). Posts are presented chronologically by timestamp (oldest to newest) with full metadata.**

- **Post ID: 1668006847683657728**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Sun, 11 Jun 2023 21:26:37 GMT  
  **Content:** Speaking to nearly 3,000 students at Turning Point USA's Young Women's Leadership Summit, Riley Gaines tells the story of what really happened when Lia Thomas, formerly Will, cheated his way to a "national championship" and the disgraceful trophy ceremony where she decided to fight back.  
  **Engagement:** Likes=13298, Reposts=2410, Quotes=111, Replies=415, Bookmarks=253, Views=1185207  
  **Media:** Video (1 item) – URL: https://video.twimg.com/amplify_video/1668006555000934400/vid/640x360/i5wJ7gHZPbhHW4jR.mp4?tag=14 (duration: 413738 ms)  
  **Conversation ID:** 1668006847683657728  
  **Quoted Post:** None

- **Post ID: 1667946353131941889**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Sun, 11 Jun 2023 17:26:14 GMT  
  **Content:** BREAKING: Libs of TikTok creator, Chaya Raichik, joins TPUSA as contributor  
  https://humanevents.com/2023/06/11/breaking-libs-of-tiktok-creator-chaya-raichik-joins-tpusa-as-contributor?utm_campaign=64501  
  **Engagement:** Likes=1755, Reposts=204, Quotes=6, Replies=125, Bookmarks=3, Views=104830  
  **Media:** None  
  **Conversation ID:** 1667946353131941889  
  **Quoted Post:** None

- **Post ID: 1667969439726465024**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Sun, 11 Jun 2023 18:57:58 GMT  
  **Content:** THAT'S A WRAP on #YWLS2023!✨🪩  
  Thank you to everyone for making this the best event of the year for conservative women! 💖  
  **Engagement:** Likes=99, Reposts=23, Quotes=2, Replies=11, Bookmarks=0, Views=18829  
  **Media:** Yes (4 items) – Photos: https://pbs.twimg.com/media/FyXRWpEakAAU6Kq.jpg, https://pbs.twimg.com/media/FyXRWpHaIAAGJ4A.jpg, https://pbs.twimg.com/media/FyXRWpIakAIaSec.jpg, https://pbs.twimg.com/media/FyXRWpEagAE2Idq.jpg  
  **Conversation ID:** 1667969439726465024  
  **Quoted Post:** None

- **Post ID: 1667936646380281856**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Sun, 11 Jun 2023 16:47:39 GMT  
  **Content:** “I don’t care what people call me, and you shouldn’t either. It’s a way for them to take away our right to speak our mind.” @ChayaRaichik10 aka @libsoftiktok #YWLS2023  
  **Engagement:** Likes=202, Reposts=29, Quotes=1, Replies=10, Bookmarks=3, Views=26582  
  **Media:** None  
  **Conversation ID:** 1667936646380281856  
  **Quoted Post:** None

- **Post ID: 1667935630205255682**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Sun, 11 Jun 2023 16:43:37 GMT  
  **Content:** We are excited that Chaya Raichik (also known as @libsoftiktok) will be joining the team as our newest TPUSA Contributor! We look forward to working with Chaya in the fight to expose leftist corruption, while inspiring generations of young conservatives to speak freely. 🇺🇸  
  Join us in welcoming @ChayaRaichik10 to the TPUSA family! ⬇️  
  **Engagement:** Likes=2023, Reposts=333, Quotes=22, Replies=86, Bookmarks=18, Views=733021  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/ext_tw_video/1667935486734925825/pu/vid/1080x1920/_82f86RwhgJYdgPW.mp4?tag=14 (duration: 20954 ms)  
  **Conversation ID:** 1667935630205255682  
  **Quoted Post:** None

- **Post ID: 1668395878992998400**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Mon, 12 Jun 2023 23:12:29 GMT  
  **Content:** Charlie Kirk on his temperament towards the LGBT community and why he thinks “live and let live” is dead.  
  @charliekirk11 #YWLS2023  
  **Engagement:** Likes=616, Reposts=141, Quotes=12, Replies=69, Bookmarks=12, Views=78834  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/ext_tw_video/1668395181920653312/pu/vid/1280x720/vpPpJ8sZqnth_aKV.mp4?tag=14 (duration: 92607 ms)  
  **Conversation ID:** 1668395878992998400  
  **Quoted Post:** None

- **Post ID: 1668657876246855680**  
  **Author:** Charlie Wilson (@CharlieWilson)  
  **Timestamp:** Tue, 13 Jun 2023 16:33:34 GMT  
  **Content:** Excited to perform at the Juneteenth: A Global Celebration for Freedom concert next Monday 6/19 at the @Greek_Theatre!🕺🏾Tickets on sale now! Catch it live on @CNN at 8PM ET/ 5PM PT. #Juneteenth https://lnk.to/CharlieWilson  
  **Engagement:** Likes=248, Reposts=27, Quotes=5, Replies=11, Bookmarks=1, Views=8591  
  **Media:** Yes (1 item) – Photo: https://pbs.twimg.com/media/FyhDfhoaQAAsM_o.jpg  
  **Conversation ID:** 1668657876246855680  
  **Quoted Post:** None  
  *(Note: This post references a performance event but was returned in results; included for completeness as it appeared in semantic/keyword matches involving events around the date range.)*

- **Post ID: 1668659066967838720**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Tue, 13 Jun 2023 16:38:18 GMT  
  **Content:** UPDATE: Trans TikToker Rose Montoya reacts to the backlash over his topless video at Biden's White House Pride event, saying that outrage over the video just affirms his "female body".  
  No you're not a woman, you're wearing a surgical costume, dude.  
  **Engagement:** Likes=11471, Reposts=1577, Quotes=354, Replies=3488, Bookmarks=332, Views=4110254  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/ext_tw_video/1668657400134639617/pu/vid/576x1024/exAkCA9M1tgUkJip.mp4?tag=12 (duration: 96454 ms)  
  **Conversation ID:** 1668659066967838720  
  **Quoted Post:** Post ID 1668410936259125248 (Charlie Kirk, Tue, 13 Jun 2023 00:12:19 GMT – GRAPHIC: Trans TikTok "influencer" Rose Montoya...)

- **Post ID: 1668708327789068289**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Tue, 13 Jun 2023 19:54:03 GMT  
  **Content:** LIVE REACTION FROM MIAMI: Just moments ago we heard from grassroots conservatives—including a surprise cameo from Turning Point Action's @DrienaSixto—who is signing up Precinct Committeemen and women on the ground.  
  Where is the RNC? Where are the other leading presidential candidates besides Vivek?  
  **Engagement:** Likes=740, Reposts=177, Quotes=5, Replies=63, Bookmarks=5, Views=85422  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/ext_tw_video/1668705094307807232/pu/vid/1280x720/qqf4ixa6lzsKeCdl.mp4?tag=12 (duration: 333966 ms)  
  **Conversation ID:** 1668708327789068289  
  **Quoted Post:** None

- **Post ID: 1669102458914897920**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Wed, 14 Jun 2023 22:00:11 GMT  
  **Content:** After speaking in front of thousands of women at this year's Young Women's Leadership Summit, Riley Gaines sat down with us to discuss the reality of transgenders participating in women's sports.  
  She delves into the horror felt in the locker room when Lia Thomas exposed his penis, in addition to the behind-the-scenes support she received from athletes too scared to speak out. Read more here:  
  **Engagement:** Likes=48, Reposts=12, Quotes=0, Replies=3, Bookmarks=1, Views=7149  
  **Media:** None  
  **Conversation ID:** 1669102458914897920  
  **Quoted Post:** None

- **Post ID: 1669299490421866497**  
  **Author:** Belinda Carlisle (@belindacarlisle)  
  **Timestamp:** Thu, 15 Jun 2023 11:03:07 GMT  
  **Content:** Tour time again!! 🚌  
  The tour kicks off in Peachtree City, Georgia on July 1, which is a SOLD-OUT show. 🎉  
  Then, it's off to Washington, DC for PBS live taping for a 4th of July 🎇 celebration to be aired live.   
  Next stop will be Sheboygan, Wisconsin.  
  https://t.co/cmUyASIm69  
  **Engagement:** Likes=206, Reposts=20, Quotes=0, Replies=5, Bookmarks=1, Views=6073  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/ext_tw_video/1669299480049471488/pu/vid/720x1280/JQeoXwr-81vGOTnQ.mp4?tag=12 (duration: 15000 ms)  
  **Conversation ID:** 1669299490421866497  
  **Quoted Post:** None  
  *(Note: This post references a tour/performance event but was returned in results; included for completeness.)*

- **Post ID: 1669376215436910594**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 15 Jun 2023 16:07:59 GMT  
  **Content:** 🚨🚨BREAKING 🚨🚨  
  MEGYN KELLY is confirmed for our Turning Point Action Conference, July 15-16 in West Palm Beach, FL.  
  This has been the FASTEST selling event in Turning Point history. Get your tickets today while there's still time. https://t.co/kn40D7KruX  
  #ACTCON2023  
  **Engagement:** Likes=1769, Reposts=274, Quotes=12, Replies=98, Bookmarks=4, Views=103835  
  **Media:** Yes (1 item) – Photo: https://pbs.twimg.com/media/FyrQVoGakAAW-d7.jpg  
  **Conversation ID:** 1669376215436910594  
  **Quoted Post:** None

- **Post ID: 1669425808526524417**  
  **Author:** The Gateway Pundit (@gatewaypundit)  
  **Timestamp:** Thu, 15 Jun 2023 19:25:03 GMT  
  **Content:** Rally: Trump to Speak at Main Street Fourth of July Celebration in Small City of Pickens, South Carolina on July 1st https://www.thegatewaypundit.com/2023/06/rally-trump-speak-main-street-fourth-july-celebration/?utm_source=rss&utm_medium=rss&utm_campaign=rally-trump-speak-main-street-fourth-july-celebration  
  **Engagement:** Likes=401, Reposts=116, Quotes=2, Replies=12, Bookmarks=1, Views=13555  
  **Media:** None  
  **Conversation ID:** 1669425808526524417  
  **Quoted Post:** None  
  *(Note: This post references a speaking event but was returned in results; included for completeness.)*

- **Post ID: 1669809049372618755**  
  **Author:** Queens DSA (@QueensDSA)  
  **Timestamp:** Fri, 16 Jun 2023 20:47:55 GMT  
  **Content:** NO TRANSPHOBES OR WHITE SUPREMACISTS IN QUEENS!  
  🚨CANCEL TPUSA/BLEXIT!🚨  
  1) Contact Uri Zucker at Motif Studios 212.633.1111 uri@motifstudios.com  
  2) Contact Tammany House 718.873.6881 tammanyhousenyc@gmail.com  
  Demand they cancel the event!  
  **Engagement:** Likes=15, Reposts=7, Quotes=0, Replies=3, Bookmarks=0, Views=2730  
  **Media:** Yes (2 items) – Photos: https://pbs.twimg.com/media/FyxaekpWYAAjuzH.jpg, https://pbs.twimg.com/media/FyxaekqWAAIUlC8.jpg  
  **Conversation ID:** 1669809049372618755  
  **Quoted Post:** None

- **Post ID: 1669814500441174017**  
  **Author:** Talia Jane (@taliaotg)  
  **Timestamp:** Fri, 16 Jun 2023 21:09:35 GMT  
  **Content:** EXCLU: TPUSA is paying at least $25,000 for a free event featuring conspiracy theorists, transphobes, and christofascists that will be attended by and is “partnered” with extremist groups who harass queer people/spaces.  
  The intent is to build extremist power in NYC.  
  **Engagement:** Likes=21, Reposts=3, Quotes=0, Replies=1, Bookmarks=0, Views=4301  
  **Media:** None  
  **Conversation ID:** 1669814500441174017  
  **Quoted Post:** Post ID 1669728767370035201 (United Against Racism and Fascism NYC, Fri, 16 Jun 2023 15:28:54 GMT – 🚨The TPUSA/BLEXIT event has moved to a new venue in Queens...)

- **Post ID: 1669816370744156167**  
  **Author:** Michael Gianaris (@SenGianaris)  
  **Timestamp:** Fri, 16 Jun 2023 21:17:01 GMT  
  **Content:** Shame on Motif Studios for agreeing to host an event with alt-right extremist hate groups Turning Point USA and Blexit in Long Island City. I join my colleagues in city and state government in denouncing this event and calling on Motif Studios to do the right thing and cancel it  
  **Engagement:** Likes=70, Reposts=22, Quotes=11, Replies=82, Bookmarks=1, Views=15487  
  **Media:** Yes (1 item) – Photo: https://pbs.twimg.com/media/FyxhI3uX0AM1GYU.png  
  **Conversation ID:** 1669816370744156167  
  **Quoted Post:** None

- **Post ID: 1669831823294369793**  
  **Author:** Naked Mole Rat (@downunder045)  
  **Timestamp:** Fri, 16 Jun 2023 22:18:25 GMT  
  **Content:** @bowerypresents Thank you for cancelling the TPUSA event.  
  Nobody should be give hatred and racism a platform.  
  Well done !!!!!!  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16  
  **Media:** Yes (1 item) – Photo: https://pbs.twimg.com/media/Fyxu6w2aMAQTCnl.jpg  
  **Conversation ID:** 1669831823294369793  
  **Quoted Post:** None

- **Post ID: 1669832070632468480**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Fri, 16 Jun 2023 22:19:24 GMT  
  **Content:** Outrageous!!  
  A bunch of white liberal New Yorkers just cancelled a BLEXIT/TPUSA venue for an event featuring Brandon Tatum, Candace Owens, Anthony, Davis, and Yoenmi Park—3 black Americans and 1 North Korean defector—with less than three days notice.   
  Our event will go on AS PLANNED at a new venue. We will not let the radical left terrorize us and win. We'll see you in NYC tomorrow.  
  Please let The Music Hall of Williamsburg @bowerypresents know you don't appreciate their intolerance toward black and brown Americans.  
  **Engagement:** Likes=14460, Reposts=3255, Quotes=145, Replies=949, Bookmarks=72, Views=1608584  
  **Media:** None  
  **Conversation ID:** 1669832070632468480  
  **Quoted Post:** None

- **Post ID: 1669833362133995520**  
  **Author:** Civics and Civility are essential!😎 (@BeaReno)  
  **Timestamp:** Fri, 16 Jun 2023 22:24:32 GMT  
  **Content:** Charlie Kirk’s all bent out of shape because his hate event got cancelled.😃🔥⬇️  
  **Engagement:** Likes=1, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=49  
  **Media:** None  
  **Conversation ID:** 1669833362133995520  
  **Quoted Post:** Post ID 1668978348700184583 (Music Hall of Williamsburg, Wed, 14 Jun 2023 13:47:01 GMT – June 17th Blexit event no longer taking place at Music Hall of Williamsburg...)

- **Post ID: 1669836752553656320**  
  **Author:** Blue Shirt Project (@blueshirtday1)  
  **Timestamp:** Fri, 16 Jun 2023 22:38:00 GMT  
  **Content:** Remember when you claimed that TPUSA was a "non-partisan" organization on your IRS Form 990, Chuck?  
  That's pretty damn funny. It will be even funnier when you lose your non-profit status.  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=9  
  **Media:** Yes (1 item) – Photo: https://pbs.twimg.com/media/FyxzorkagAIMjz2.png  
  **Conversation ID:** 1669836752553656320  
  **Quoted Post:** None

- **Post ID: 1669840413673369602**  
  **Author:** MissRosie (@MissRosie45)  
  **Timestamp:** Fri, 16 Jun 2023 22:52:33 GMT  
  **Content:** Showing @bowerypresents as true racists by canceling @TPUSA event which was headlining BLEXIT LIVE black and brown Americans. @bowerypresents shutting down free speech. DISGRACEFUL  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=7  
  **Media:** Yes (1 item) – Video: https://video.twimg.com/tweet_video/Fyx3ANaXgAIIwZ-.mp4 (duration: 0 ms)  
  **Conversation ID:** 1669840413673369602  
  **Quoted Post:** None

- **Post ID: 1669846275947372544**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Fri, 16 Jun 2023 23:15:51 GMT  
  **Content:** Cowards and liars. The Music Hall of Williamsburg knew exactly who we were when we booked this event. They said they "lean left" but believed "everyone has a right to speak". Later, they claimed they had to back out because they feared for staff safety. Fair enough, we understood. But to then go on social media to virtue signal that this is some stand against "hate" is disgraceful and a lie, and even fans of the @MusicHallofWB should know.   
  Dear white liberals, last time I checked, canceling a venue for black and brown people was the very definition of hate.  
  **Engagement:** Likes=3182, Reposts=763, Quotes=24, Replies=131, Bookmarks=12, Views=340446  
  **Media:** None  
  **Conversation ID:** 1669846275947372544  
  **Quoted Post:** Post ID 1668978348700184583 (Music Hall of Williamsburg, Wed, 14 Jun 2023 13:47:01 GMT – June 17th Blexit event no longer taking place at Music Hall of Williamsburg...)

- **Post ID: 1669846381807190018**  
  **Author:** ParentChain #AnnWiddecombe (@parentchain)  
  **Timestamp:** Fri, 16 Jun 2023 23:16:16 GMT  
  **Content:** WRONG!!! Sunak with Boris - he was the one who took pics of Boris. It was Cummings who threatened, "There will be photos." Why? Cummings bitter his job came to an end. Even together, Boris got FPN, Sunak did not! He got free pass. Privileges Committee is flawed!  
  **Engagement:** Likes=3, Reposts=1, Quotes=0, Replies=3, Bookmarks=0, Views=727  
  **Media:** None  
  **Conversation ID:** 1669846381807190018  
  **Quoted Post:** Post ID 1669657807426056192 (Capman #FBPE, Fri, 16 Jun 2023 10:46:56 GMT – Johnson was "hauled" in front of the privileges committee...)

- **Post ID: 1669846381807190018** (duplicate reference in results)  
  *(Note: Duplicate entry in tool output; same as above.)*

- **Post ID: 1669850131536158720**  
  **Author:** Prayers for Charlie Kirk 🙏 (@GoHalos4Life)  
  **Timestamp:** Fri, 16 Jun 2023 23:31:10 GMT  
  **Content:** Dodgers do care. That’s why they didn’t go after Tre Turner because they didn’t want to pay the 100% repeater tax. Red Sox have no shot. That is a pipe dream. If he doesn’t stay with the Angels it will be the Dodgers, SF or Padres period. He isn’t leaving the West Coast  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=56  
  **Media:** None  
  **Conversation ID:** 1669850131536158720  
  **Quoted Post:** None  
  *(Note: This post references Charlie Kirk but in a non-event context; included as returned in results.)*

- **Post ID: 1669851695113814017**  
  **Author:** SloopJohnB 🇺🇸 (@realJohnBarryD)  
  **Timestamp:** Fri, 16 Jun 2023 23:37:23 GMT  
  **Content:** @bowerypresents why did you cancel the TPUSA event?   
  Are you pro censorship? Anti-black? Pro North Korea??  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=15  
  **Media:** None  
  **Conversation ID:** 1669851695113814017  
  **Quoted Post:** None

- **Post ID: 1669853286986403841**  
  **Author:** Believe Better (@believebetter1)  
  **Timestamp:** Fri, 16 Jun 2023 23:43:42 GMT  
  **Content:** It's silly that A man is giving this advice giving this advice and he's doing it in Charlie Kirk speak but there are real trade-offs that need to be considered that are never discussed in mainstream culture.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=48  
  **Media:** None  
  **Conversation ID:** 1669853286986403841  
  **Quoted Post:** None

- **Post ID: 1669854840627888128**  
  **Author:** RoCu (@RobertCub1)  
  **Timestamp:** Fri, 16 Jun 2023 23:49:53 GMT  
  **Content:** If the event was really 'a non-profit organization dedicated to the advancement of urban and minority communities', then why is Charlie Kirk so enraged about it's cancellation? He has no history of supporting this. They tell on themselves, it's obvious why he's enraged about it.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=13  
  **Media:** None  
  **Conversation ID:** 1669854840627888128  
  **Quoted Post:** None

- **Post ID: 1669856448321388544**  
  **Author:** Let The Idiot Speak .phd (@LGB_LGB_LGB)  
  **Timestamp:** Fri, 16 Jun 2023 23:56:16 GMT  
  **Content:** Future cannon fodder?  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=14  
  **Media:** None  
  **Conversation ID:** 1669856448321388544  
  **Quoted Post:** None

- **Post ID: 1669856713628061698**  
  **Author:** Suzee W 💙 (@Suzee42755)  
  **Timestamp:** Fri, 16 Jun 2023 23:57:19 GMT  
  **Content:** The real reason the event was canceled, is LACK OF INTEREST. Chucky is trying to blame his failure on them. Truth is TPUSA couldn't fill the space. They couldn't get 650 ppl for their event of hate, bigotry, racism and Nazi garbag. 🤣🤣  
  #NeverUnderestimateTheHelp 😏 Thx!  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=10  
  **Media:** None  
  **Conversation ID:** 1669856713628061698  
  **Quoted Post:** None

**Key event details extracted directly from posts (no summarization):**  
- **Young Women's Leadership Summit (#YWLS2023)**: Multiple posts confirm it occurred/ concluded around June 11, 2023 (e.g., wrap-up posts on June 11; Charlie Kirk speaking to ~3,000 students; Riley Gaines and Chaya Raichik appearances/speaking; Chaya Raichik announced as new TPUSA contributor).  
- **BLEXIT/TPUSA event (New York City area)**: Planned for June 17, 2023 (initially at Music Hall of Williamsburg, Brooklyn; featured speakers including Brandon Tatum, Candace Owens, Anthony Davis, Yeonmi Park; later moved to Motif Studios/Tammany House in Queens/Long Island City due to cancellation). Multiple posts from June 14–16 discuss the booking, cancellation by venue, relocation, and protests/calls to cancel. Charlie Kirk posted updates confirming the event would proceed at a new venue.  
- **Future announcements (outside strict range but posted in range)**: Turning Point Action Conference (July 15-16, West Palm Beach, FL – Megyn Kelly confirmed); other unrelated events mentioned in results.  

All data from tool results is reproduced verbatim above. No posts were omitted.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-06-11 to 2023-06-17**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-06-11 to 2023-06-17 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
