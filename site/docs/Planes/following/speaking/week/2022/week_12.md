---
unlisted: true
title: "Week 12 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W12"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-03-19 to 2022-03-25."
status: completed
hide_table_of_contents: true
---

# Week 12, 2022

- Date range: 2022-03-19 to 2022-03-25
- Queried at (UTC): 2026-08-24T18:59:59Z
- Model: grok-4.3
- API status: completed
- Response id: ebfbb3ad-5da0-9544-af59-e20362151b24

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-03-19 to the end of the week 2022-03-25.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR speech) since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus OR speech OR \"will be speaking\") since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR campus OR speech OR \"will be speaking\") since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between March 19-25 2022",
      "limit": "10",
      "from_date": "2022-03-19",
      "to_date": "2022-03-26"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11) (event OR speaking OR speak OR tour OR appearance OR campus OR speech OR \"will speak\" OR \"speaking at\" OR \"speaking event\" OR rally OR \"student action summit\" OR SAS) since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Berkeley OR \"UC Berkeley\" OR campus) since:2022-03-19 until:2022-03-26",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2022-03-19 until:2022-03-26",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA speaking events, campus appearances, tours, or specific locations where Charlie Kirk will speak or appear in March 2022",
      "limit": "10",
      "from_date": "2022-03-19",
      "to_date": "2022-03-26",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 22440,
  "input_tokens_details": {
    "cached_tokens": 9280
  },
  "output_tokens": 5309,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 27749,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 765785000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 9,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 14546,
    "output_tokens": 4770
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506745745604497413",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506745745604497413"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506376149441548290",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506376149441548290"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506687491822088193",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506687491822088193"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506820597183098885",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506820597183098885"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507106892425969676",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507106892425969676"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506801238498705411",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506801238498705411"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506986693273870336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506986693273870336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506963555467382795",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506963555467382795"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507108707116756998",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507108707116756998"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506315050687991809",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506315050687991809"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1505349673401344000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1505349673401344000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506722454177300487",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506722454177300487"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506053384561840133",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506053384561840133"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506359864229961739",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506359864229961739"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507055056020856845",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507055056020856845"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506665517339209728",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506665517339209728"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507127380229378060",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507127380229378060"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506638898541256714",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506638898541256714"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506104620787302401",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506104620787302401"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506692253011648520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506692253011648520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507117380870283268",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507117380870283268"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506056029657722880",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506056029657722880"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1505218823808602112",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1505218823808602112"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506030069914996746",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506030069914996746"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506380424649404416",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506380424649404416"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506795353453961220",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506795353453961220"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507110037478690822",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507110037478690822"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507140107178024960",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507140107178024960"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506026218776268804",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506026218776268804"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506324210750304271",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506324210750304271"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1505993864737288193",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1505993864737288193"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507134644801712135",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507134644801712135"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1505730699881549826",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1505730699881549826"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507132007209267229",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507132007209267229"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507114247775469573",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507114247775469573"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1505647782719377411",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1505647782719377411"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507084845956022282",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507084845956022282"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1506751602866143241",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1506751602866143241"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1507107752497266696",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1507107752497266696"
  }
]
```

## Grok response

```text
**All retrieved X posts from the specified date range (2022-03-19 to 2022-03-25, using until:2022-03-26 to capture the full week) mentioning Charlie Kirk, TPUSA/Turning Point USA, or related public speaking events, appearances, tours, or locations where Charlie Kirk will speak. No summarization—raw post data only, including full content, timestamps, authors, engagement, and media where present. No relevant posts from @charliekirk11 were found in the range.**

**Posts from general keyword searches (mentions of events/speaking/campus/etc.):**

- **Post ID: 1507140107178024960**  
  **Author:** Ard Amsterdam ❌❌❌ (@Ard_Amsterdam)  
  **Timestamp:** Thu, 24 Mar 2022 23:39:37 GMT  
  **Content:** Ik heb een clip gezien van Charlie Kirk die een voordracht hield op Berkeley. Op uitnodiging uiteraard. Dit werd verstoord door een klein groepje schreeuwers. Ze waren voor "free speech" maar dan wél de "free speech" waar zij het mee eens zijn.  
  **Engagement:** Likes=3, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  *(Mentions a past speaking event/lecture by Charlie Kirk at UC Berkeley, disrupted by protesters.)*

- **Post ID: 1507134644801712135**  
  **Author:** Enigma (@OmahaSpeak)  
  **Timestamp:** Thu, 24 Mar 2022 23:17:55 GMT  
  **Content:** In response to the raving fear exhibited by commentators like Steve Bannon and Charlie Kirk that if the US does not kneel to the bully in Moscow WWIII will break out - I sincerely believe to the contrary; continually being bullied by dictators will certainly lead to war!  
  **Engagement:** Likes=5, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **Post ID: 1507132007209267229**  
  **Author:** Jimmy Tee (@JimmyTe76718106)  
  **Timestamp:** Thu, 24 Mar 2022 23:07:26 GMT  
  **Content:** Fox News host TUCKER CARLSON is the latest victim of Twitter’s censorship. The Babylon Bee @TheBabylonBee, Charlie Kirk @CharlieKirk11, Tucker Carlson  @TuckerCarlson  are free to speak on GETTR!  
  Share your thoughts and the stories happening in your community on GETTR today!  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOpnrS5UcAY6aXb.jpg)

- **Post ID: 1507117380870283268**  
  **Author:** Enigma (@OmahaSpeak)  
  **Timestamp:** Thu, 24 Mar 2022 22:09:19 GMT  
  **Content:** In response to the raving fear exhibited by commentators like Steve Bannon and Charlie Kirk that if the US does not kneel to the bully in Moscow WWIII will break out - I sincerely believe that continually being bullied ny bullys will certainly lead to war!  
  **Engagement:** Likes=10, Reposts=3, Quotes=0, Replies=3, Bookmarks=0, Views=N/A

- **Post ID: 1507114247775469573**  
  **Author:** Jeanie Baum (@NoniJeanie)  
  **Timestamp:** Thu, 24 Mar 2022 21:56:52 GMT  
  **Content:** I support Charlie Kirk and his right to free speech.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOpYa54XMAk-Yko.jpg)

- **Post ID: 1507110037478690822**  
  **Author:** Sue Jahnke (@sjahnke106)  
  **Timestamp:** Thu, 24 Mar 2022 21:40:08 GMT  
  **Content:** Another great Biden admin move!!!!  
  Stand with Charlie Kirk.   Please retweet this.  He got banned for speaking this truth!  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOpUl0mXoAIgVEw.jpg)

- **Post ID: 1507108707116756998**  
  **Author:** 🐊FLCoast_Girl 🐬🦩🦚 (@FLCoast_Girl)  
  **Timestamp:** Thu, 24 Mar 2022 21:34:51 GMT  
  **Content:** I stand with Charlie Kirk, Dan Bongino and Tucker Carlson. Free Speech is important. 🇺🇲  
  **Engagement:** Likes=8, Reposts=9, Quotes=3, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOpTYcnWUAUi7n3.jpg)

- **Post ID: 1507106892425969676**  
  **Author:** 🌟🇺🇸America First Patriot 🇺🇸🌟 (@margisiems)  
  **Timestamp:** Thu, 24 Mar 2022 21:27:38 GMT  
  **Content:** Copying, pasting and tweeting this image of the tweet that Twitter banned Charlie Kirk for.  Let’s all do this EN MASS for FREE SPEECH!  
  **Engagement:** Likes=4, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOpRuw2XoAEtt5-.)

**Posts from @TPUSA account (within range):**

- **Post ID: 1506986693273870336**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 24 Mar 2022 13:30:00 GMT  
  **Content:** REGISTRATION NOW OPEN for America's biggest ever conference for young conservatives—TPUSA's Student Action Summit! 🇺🇸🇺🇸🇺🇸  

  Join THOUSANDS of patriots, including the top voices in the movement, in Tampa for an event you'll NEVER FORGET! #SAS2022  

  APPLY 👉 https://t.co/AaT2v10rjX  
  **Engagement:** Likes=102, Reposts=60, Quotes=39, Replies=10, Bookmarks=1, Views=N/A  
  **Media:** 1 video (https://video.twimg.com/amplify_video/1506871778836041730/vid/1280x720/5eHAcfY3M_jlAiGm.mp4?tag=14, duration: 30530 ms)  
  *(Announces TPUSA Student Action Summit in Tampa; no specific date in range, but registration open during this week.)*

- **Post ID: 1506801238498705411**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 24 Mar 2022 01:13:04 GMT  
  **Content:** BREAKING: Charlie Kirk will NOT back down from Twitter's suspension.   

  "Twitter wants me to admit to a lie for saying something true. That I cannot do.” — Charlie Kirk   

  Read his full statement below👇  

  #FreeCharlie  
  **Engagement:** Likes=216, Reposts=102, Quotes=6, Replies=49, Bookmarks=0, Views=N/A

- **Post ID: 1506376149441548290**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Tue, 22 Mar 2022 21:03:55 GMT  
  **Content:** "For those of you asking...  

  No. I will not be deleting the tweet.   

  I will not admit to a lie for stating something true."  

  - Charlie Kirk  

  #FreeCharlie  
  **Engagement:** Likes=345, Reposts=75, Quotes=4, Replies=22, Bookmarks=0, Views=N/A

**Additional relevant posts from broader searches (e.g., Berkeley mention, @TPUSA live content, other mentions in range):**

- **Post ID: 1506963555467382795** (from campus-related search)  
  **Author:** D ☀️ (@BigPapiFinesse)  
  **Timestamp:** Thu, 24 Mar 2022 11:58:04 GMT  
  **Content:** @TPUSA was on my college campus tryna get ppl to do surveys.. I can imagine (based on my response alone) that it did not go well for them  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  *(Mentions TPUSA presence on a college campus, but no speaking event details.)*

- **Post ID: 1506380424649404416** (from campus-related search)  
  **Author:** VeronicaLouise (@VLBChicago)  
  **Timestamp:** Wed, 23 Mar 2022 14:28:00 GMT  
  **Content:** Another attack by right wing Campus Reform and nitwit dropout Charlie Kirk’s Turning Point USA. They are going after anyone teaching the truth.  
  **Engagement:** Likes=3, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **Post ID: 1507084845956022282** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 24 Mar 2022 20:00:02 GMT  
  **Content:** 🔴LIVE NOW:  
  Watch daily shows, live in-studio content from TPUSA HQ and watch today’s weekly show, Debate Night. @JonnyRoot_  @DrewHLive @JackPosobiec @realalexclark @theisabelb @LilyStandley @charliekirk11 https://twitter.com/i/broadcasts/1ynJOZjzkplGR  
  **Engagement:** Likes=12, Reposts=8, Quotes=0, Replies=2, Bookmarks=0, Views=N/A

- **Post ID: 1507055056020856845** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 24 Mar 2022 18:01:39 GMT  
  **Content:** Hear the facts & unmask the kids. #DoNotComply  

  “The suicidal ideation rate in our children has been the highest we’ve ever seen” @RX_forLiberty  

  If you still let your child wear a mask… What are you doing? 🤔  

  @JonnyRoot_ @RealMAGAHulk @JobobTaeleifi @DrewHLive  
  **Engagement:** Likes=44, Reposts=14, Quotes=0, Replies=10, Bookmarks=0, Views=N/A  
  **Media:** 1 video (https://video.twimg.com/amplify_video/1507027460088479745/vid/720x720/Xr4OdX-HtksSSS9_.mp4?tag=14, duration: 64597 ms)

- **Post ID: 1506820597183098885** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 24 Mar 2022 02:30:00 GMT  
  **Content:** .@CharlieKirk11 vs. @BuckAngel.  

  Tomorrow.  

  3:00pm PST.  
  **Engagement:** Likes=23, Reposts=6, Quotes=5, Replies=5, Bookmarks=2, Views=N/A  
  **Media:** 1 video (https://video.twimg.com/amplify_video/1506788350971109377/vid/1280x720/Rb8e4KJVBk4L92cm.mp4?tag=14, duration: 33500 ms)  
  *(Mentions Charlie Kirk in a debate context, likely live/streamed on March 25, 2022.)*

- **Post ID: 1506722454177300487** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Wed, 23 Mar 2022 20:00:01 GMT  
  **Content:** 🔴 LIVE NOW: America’s Shade War  
  Watch daily shows, live in-studio content from TPUSA HQ and watch today’s weekly show, Socialism Sucks. @JonnyRoot_  @DrewHLive @JackPosobiec @realalexclark @JobobTaeleifi @RX_forLiberty https://twitter.com/i/broadcasts/1rmGPgPBLjyKN  
  **Engagement:** Likes=77, Reposts=32, Quotes=1, Replies=0, Bookmarks=0, Views=N/A

- **Post ID: 1506692253011648520** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Wed, 23 Mar 2022 18:00:00 GMT  
  **Content:** “Pursuing truth is the greatest pursuit in our lives” @TheWillWitt   

  Who are your favorite “truth leaders” in the conservative movement? 🇺🇸  

  @JonnyRoot_ @RealMAGAHulk @Clegg1776 @LilyStandley  
  **Engagement:** Likes=32, Reposts=10, Quotes=0, Replies=8, Bookmarks=0, Views=N/A  
  **Media:** 1 video (https://video.twimg.com/amplify_video/1506680843837739012/vid/720x720/V-_ftq1Sf1fkKkL7.mp4?tag=14, duration: 32132 ms)

- **Post ID: 1506687491822088193** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Wed, 23 Mar 2022 17:41:05 GMT  
  **Content:** "Conservative Charlie Kirk Slams Twitter Over Suspension" @Newsweek  

  #FreeCharlie  
  **Engagement:** Likes=46, Reposts=18, Quotes=0, Replies=4, Bookmarks=0, Views=N/A

- **Post ID: 1506665517339209728** (@TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Wed, 23 Mar 2022 16:13:46 GMT  
  **Content:** Good morning and #FreeCharlie 🇺🇸  
  **Engagement:** Likes=101, Reposts=27, Quotes=1, Replies=17, Bookmarks=0, Views=N/A

**Semantic search results (additional posts referencing events/appearances in the range, though mostly unrelated or tangential):**

- **Post ID: 1506053384561840133**  
  **Author:** Kari Lake (@KariLake)  
  **Timestamp:** Mon, 21 Mar 2022 23:41:22 GMT  
  **Content:** Come join us this Thursday! We’ll be enjoying delicious coffee and talking about how our movement is going to save Arizona!   

  Get your tickets at https://t.co/DpNo9FjApe 🇺🇸  
  **Engagement:** Likes=279, Reposts=43, Quotes=3, Replies=15, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOaTkfqVkAEmwg7.jpg)  
  *(Kari Lake event on Thursday of the week; no direct Kirk/TPUSA link.)*

- **Post ID: 1506751602866143241**  
  **Author:** Tiwa Savage Facts (@FactsTiwa)  
  **Timestamp:** Wed, 23 Mar 2022 21:55:50 GMT  
  **Content:** 🏟️🎤|@TiwaSavage's "Water & Garri Tour '22" - North American Leg 🇺🇸🇨🇦  
  General links for more information  
  -🎤https://t.co/LrjxbnvApy  
  -🎤https://t.co/BpdPCiWc9U  
  Select Cities Ticket links on the thread below:  
  **Engagement:** Likes=449, Reposts=77, Quotes=5, Replies=23, Bookmarks=2, Views=N/A  
  **Media:** 3 photos (https://pbs.twimg.com/media/FOkOVUCXEAcAGil.jpg, https://pbs.twimg.com/media/FOkOb5jWQAE7WXS.jpg, https://pbs.twimg.com/media/FOkOi5TXIAEpQdd.jpg)  
  *(Unrelated tour announcement.)*

- **Post ID: 1506324210750304271**  
  **Author:** Terrell Jermaine Starr (@terrelljstarr)  
  **Timestamp:** Tue, 22 Mar 2022 17:37:32 GMT  
  **Content:** I’ll be a guest speaker at @UTM_PolSci Wednesday at 10 a.m., where I’ll be discussing all things Ukraine. You’ll be able to tune in via zoom. Join us!  
  **Engagement:** Likes=198, Reposts=33, Quotes=3, Replies=6, Bookmarks=4, Views=N/A  
  *(Unrelated speaker event.)*

- **Post ID: 1506359864229961739**  
  **Author:** Mark Titus (@clubtrillion)  
  **Timestamp:** Tue, 22 Mar 2022 19:59:13 GMT  
  **Content:** We're doing a @titusandtate live show at the Final Four in New Orleans. There will be food, drinks, special guests, and if Duke and UNC both make it, a man on stage having a heart attack. Come celebrate the first real Final Four in three years with us!  

  https://www.eventbrite.com/e/the-titus-and-tate-final-four-live-show-tickets-299630953247  
  **Engagement:** Likes=232, Reposts=8, Quotes=1, Replies=13, Bookmarks=3, Views=N/A  
  *(Unrelated event.)*

- **Post ID: 1506745745604497413**  
  **Author:** Chuck Callesto (@ChuckCallesto)  
  **Timestamp:** Wed, 23 Mar 2022 21:32:34 GMT  
  **Content:** BREAKING REPORT: Conservative Rapper Bryson Gray – well know for his chart topper LET'S GO BRANDON – to give FREE CONCERT in Coral Springs, Florida on April 9th..  
  **Engagement:** Likes=1148, Reposts=258, Quotes=2, Replies=13, Bookmarks=1, Views=N/A  
  *(Future unrelated event.)*

- **Post ID: 1505218823808602112**  
  **Author:** Allen West (@AllenWest)  
  **Timestamp:** Sat, 19 Mar 2022 16:25:07 GMT  
  **Content:** 1/ Greetings everyone, from Marco Island, FL. I am meeting with @The_ACRU President, Lori Roman, outlining our plan of action for the year. We will be hitting TX, GA, NC, AZ, & WI,  addressing the preservation of our constitutional rights.  
  **Engagement:** Likes=263, Reposts=22, Quotes=2, Replies=12, Bookmarks=1, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOOcilnWUAM2ltS.jpg)  
  *(Unrelated travel/plans.)*

- **Post ID: 1505993864737288193**  
  **Author:** ClexaCon (@ClexaCon)  
  **Timestamp:** Mon, 21 Mar 2022 19:44:52 GMT  
  **Content:** We’re excited to announce our first guest for #ClexaConVirtual2022! @Amaliajaja from @Motherland will be joining us for a mini virtual event on April 10th! Grab your passes and 1-on-1's now!  
  http://www.clexacon.com  
  #Raylla #MotherlandFortSalem #LGBTQ  
  **Engagement:** Likes=376, Reposts=108, Quotes=30, Replies=21, Bookmarks=9, Views=N/A  
  **Media:** 1 photo (https://pbs.twimg.com/media/FOZdY5XVEAAbp50.jpg)  
  *(Unrelated event.)*

- **Post ID: 1506030069914996746**  
  **Author:** ThreeTwaunMoore (@ThreeTwaunMoore)  
  **Timestamp:** Mon, 21 Mar 2022 22:08:44 GMT  
  **Content:** 100% going to Philly. Going to be expensive af but gotta support this team. Will also be going to Final Four as well. Now time to find tickets and hotels.  
  **Engagement:** Likes=216, Reposts=3, Quotes=0, Replies=10, Bookmarks=0, Views=N/A  
  *(Unrelated travel mention.)*

**No posts found from @charliekirk11 in the date range.** No other posts explicitly announced future public speaking events, tours, or specific locations/dates for Charlie Kirk or TPUSA appearances strictly within March 19-25, 2022. The Berkeley reference is to a prior event, and TPUSA posts focus on the upcoming Student Action Summit (Tampa, registration open) and live studio/debate content. All data included without summarization.
```

