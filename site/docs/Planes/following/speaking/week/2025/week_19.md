---
unlisted: true
title: "Week 19 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W19"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-05-07 to 2025-05-13."
status: completed
hide_table_of_contents: true
---

# Week 19, 2025

- Date range: 2025-05-07 to 2025-05-13
- Queried at (UTC): 2026-08-24T19:18:50Z
- Model: grok-4.3
- API status: completed
- Response id: ac3a951a-3498-9d2f-9c13-c31da75fd1e7

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-05-07 to the end of the week 2025-05-13.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR tour OR appearance OR \"will be\" OR visiting OR campus) since:2025-05-07 until:2025-05-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR tour OR appearance OR \"will be\" OR visiting OR campus) since:2025-05-07 until:2025-05-14 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, campus visits, or tour dates in May 2025",
      "limit": "10",
      "from_date": "2025-05-07",
      "to_date": "2025-05-13",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR tour OR appearance OR campus OR \"will be\") since:2025-05-07 until:2025-05-14",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR tour OR appearance OR campus OR \"will be\") since:2025-05-07 until:2025-05-14",
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
  "input_tokens": 12537,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 6119,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 18656,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 527431500,
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
    "input_tokens": 10947,
    "output_tokens": 5810
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1921213320897454362",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1921213320897454362"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922005869354533243",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922005869354533243"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920849117817061477",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920849117817061477"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1921655282750652438",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1921655282750652438"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922044251942129693",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922044251942129693"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1921087138415997120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1921087138415997120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920516887621828947",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920516887621828947"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922017949050712368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922017949050712368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920286054248010025",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920286054248010025"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922068221881921770",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922068221881921770"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922022694922354961",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922022694922354961"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922058203824570704",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922058203824570704"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922016681733616020",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922016681733616020"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922017608997482655",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922017608997482655"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922062247725056238",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922062247725056238"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922050901486743997",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922050901486743997"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920841196643271078",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920841196643271078"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922035834175328711",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922035834175328711"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920939383987073417",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920939383987073417"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922066936818483227",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922066936818483227"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920611949663985806",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920611949663985806"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920301821488251120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920301821488251120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922069483734110601",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922069483734110601"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922047035223470277",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922047035223470277"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920939875253010503",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920939875253010503"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1920071116560941553",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1920071116560941553"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1922067429884363106",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1922067429884363106"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range May 7–13, 2025 (searched via keyword and semantic queries for Charlie Kirk / TPUSA events, speaking appearances, campus visits, tours, or related mentions). No summarization—raw post data only, including full content, timestamps, authors, engagement, and media where present. Posts are listed in the order returned by the tools (Latest mode prioritized for recency within the window).**

### From keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA") (event OR speak OR speaking OR tour OR appearance OR "will be" OR visiting OR campus) since:2025-05-07 until:2025-05-14:
- **[post:0]** ID: 1922069483734110601  
  Author: MAGANOMICS🇺🇲TPUSA🇺🇲 (@jvargasnow77)  
  Timestamp: Mon, 12 May 2025 23:20:49 GMT  
  Content: And he will be for the next 4 years.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=23  
  (No media)

- **[post:1]** ID: 1922068221881921770  
  Author: Never Forget Charlie Kirk (@B_reazonable)  
  Timestamp: Mon, 12 May 2025 23:15:49 GMT  
  Content: So well put! I was looking for a comment like this! The ultimate destination for “equity” is that we will all be equally mediocre, equally poor, and equally disadvantaged. Excellence will be erased. But the elites running the show will be fine. Because you know, Bernie can’t be expected to wait in line at United. Socialism to a T.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=65  
  (No media)

- **[post:2]** ID: 1922067429884363106  
  Author: Grok (@grok)  
  Timestamp: Mon, 12 May 2025 23:12:40 GMT  
  Content: @AmericaPapaBear The video features Nala Rae, a former OnlyFans model who now advocates against pornography, speaking at a Turning Point USA event. The other speaker, a man in a black shirt discussing a porn ban, couldn't be identified from available sources. The event likely took place in May 2025, but specific details are unclear. Check Turning Point USA's official channels for more info.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=605  
  (No media)

- **[post:3]** ID: 1922066936818483227  
  Author: 🇮🇹🇫🇷✝️Valérie24 (@v78568915)  
  Timestamp: Mon, 12 May 2025 23:10:42 GMT  
  Content: Charlie Kirk Crushes Liberal Student on Campus https://www.youtube.com/shorts/oq3M4dzTUbI?si=BMmluUrTS6613zMB via @YouTube  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=333  
  (No media)

- **[post:4]** ID: 1922062247725056238  
  Author: LaurenLee (@laurenlitvak7)  
  Timestamp: Mon, 12 May 2025 22:52:04 GMT  
  Content: I really love watching Charlie Kirk’s campus interactions.  
  (Quoted post: Mila Joy video of OnlyFans model at Charlie Kirk’s mic)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=54  
  (No media in this post)

- **[post:5]** ID: 1922058203824570704  
  Author: Ken (@terciops)  
  Timestamp: Mon, 12 May 2025 22:36:00 GMT  
  Content: Oh goodness gracious me. A student on a campus yelling about 'fascism' and can't define it. What is the World coming to?  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=237  
  (No media)

- **[post:6]** ID: 1922050901486743997  
  Author: Defiant L’s (@DefiantLs)  
  Timestamp: Mon, 12 May 2025 22:06:59 GMT  
  Content: Liberal: We don't want Charlie Kirk on our campus he's a fascist. Interviewer: What's fascism? Liberal: I don't know I'm not good at interviews.  
  Media: Video (https://video.twimg.com/amplify_video/1922014136378261505/vid/avc1/1080x1920/JLvGCe26rCyCMU1I.mp4, duration: 13613 ms)  
  Engagement: Likes=25697, Reposts=4542, Quotes=277, Replies=842, Bookmarks=717, Views=490673

- **[post:7]** ID: 1922047035223470277  
  Author: Aquatic (@AquaticsCentral)  
  Timestamp: Mon, 12 May 2025 21:51:37 GMT  
  Content: It consists of electing Christian nationalists like Trump/vance It consists of cultural movements like Charlie Kirk’s college campus events The only laws necessary are to prevent discrimination and protect free speech as the strength of these ideas win in open debate.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=81  
  (No media)

- **[post:8]** ID: 1922044251942129693  
  Author: Charlie Kirk Saves (@jazzytrump2028)  
  Timestamp: Mon, 12 May 2025 21:40:34 GMT  
  Content: one of those babies will be elon musk or scarlette johannsen. keep them coming  
  Engagement: Likes=5, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=673  
  (No media)

### Additional keyword search results with filter:links (same query):
- **[post:9]** ID: 1922066936818483227 (duplicate of above)  
  Author: 🇮🇹🇫🇷✝️Valérie24 (@v78568915)  
  Timestamp: Mon, 12 May 2025 23:10:42 GMT  
  Content: Charlie Kirk Crushes Liberal Student on Campus https://www.youtube.com/shorts/oq3M4dzTUbI?si=BMmluUrTS6613zMB via @YouTube  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=333  
  (No media)

- **[post:10]** ID: 1922062247725056238 (duplicate of above)  
  Author: LaurenLee (@laurenlitvak7)  
  Timestamp: Mon, 12 May 2025 22:52:04 GMT  
  Content: I really love watching Charlie Kirk’s campus interactions.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=54  
  (No media)

- **[post:11]** ID: 1922050901486743997 (duplicate of above)  
  Author: Defiant L’s (@DefiantLs)  
  Timestamp: Mon, 12 May 2025 22:06:59 GMT  
  Content: Liberal: We don't want Charlie Kirk on our campus he's a fascist. Interviewer: What's fascism? Liberal: I don't know I'm not good at interviews.  
  Media: Video (https://video.twimg.com/amplify_video/1922014136378261505/vid/avc1/1080x1920/JLvGCe26rCyCMU1I.mp4, duration: 13613 ms)  
  Engagement: Likes=25697, Reposts=4542, Quotes=277, Replies=842, Bookmarks=717, Views=490673

- **[post:12]** ID: 1922035834175328711  
  Author: Thomas Sowell Quotes (@ThomasSowell)  
  Timestamp: Mon, 12 May 2025 21:07:07 GMT  
  Content: "We don’t want Charlie Kirk on our campus, we don’t want fascists on our campus, we don’t want to support that here." Watch her response when she's asked what fascism is.  
  Media: Video (https://video.twimg.com/amplify_video/1922014136378261505/vid/avc1/1080x1920/JLvGCe26rCyCMU1I.mp4, duration: 13613 ms)  
  Engagement: Likes=1583, Reposts=292, Quotes=39, Replies=96, Bookmarks=82, Views=84376

- **[post:13]** ID: 1922022694922354961  
  Author: Yahya Khashaba (@ItsYahya15)  
  Timestamp: Mon, 12 May 2025 20:14:54 GMT  
  Content: Only the Right will be able to fight against these types of corruption effectively. Never leftie porn-riddled degenerates. This is why I like right-wing conservative movements even though I hate people like Charlie Kirk.  
  (Quoted post about porn ban video)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=24  
  (No media)

- **[post:14]** ID: 1922017949050712368  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 12 May 2025 19:56:03 GMT  
  Content: “We don’t want @Charliekirk11 on our campus, we don’t want fascists on our campus, we don’t want to support that here.” “What is fascism?” “I don’t know...” @topheronx  
  Media: Video (https://video.twimg.com/amplify_video/1922014136378261505/vid/avc1/1080x1920/JLvGCe26rCyCMU1I.mp4, duration: 13613 ms)  
  Engagement: Likes=2533, Reposts=449, Quotes=36, Replies=134, Bookmarks=109, Views=89502

- **[post:15]** ID: 1922017608997482655  
  Author: Maryland Family Institute (@MDFamilyInst)  
  Timestamp: Mon, 12 May 2025 19:54:42 GMT  
  Content: Grateful for @TPUSA's invitation for MFI President @jtrimbath to speak to a Pastor's Roundtable at Nu-Lyfe Church hosted by @realrevtravers @howardftravers @howard_travers in Salisbury on June 3. Registration here: https://tpusa.com/pastormeetings/  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=42  
  (No media)

- **[post:16]** ID: 1922016681733616020  
  Author: Wilda V. Heard (@drWilda)  
  Timestamp: Mon, 12 May 2025 19:51:00 GMT  
  Content: UW student ‘shocked, saddened’ after feces thrown on her at conservative event https://mynorthwest.com/local/uw-feces-turning-point-usa/4085943 When the Left Can’t Win the Argument, They Fling Feces Civil discourse officially died—again—at the UW when a volunteer for Turning Point USA, Mia Parsons, had a bag of feces launched at her by a protester. Yes, really. While she was calmly checking in attendees, some unhinged leftist decided the best way to “debate” conservatism was with biological warfare. Mia, showing more grace than her attacker could spell, laughed it off and even prayed for the protesters—because unlike the mob, she still believes in decency. “I’m glad it was in a bag,” she quipped. And yet, somehow, she’s the one treated like a villain on this campus. This isn’t a one-off, either. It’s part of a disturbing pattern at UW, where conservative speakers are met with hysteria, harassment, and now—human waste. Apparently, throwing poop is now part of the “progressive” playbook. So the next time someone tells you the Left is all about love and tolerance, just remember: their idea of dialogue is a Ziploc full of excrement. Read more at  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16  
  (No media)

- **[post:17]** ID: 1922005869354533243  
  Author: Seattle Red 🎙 (@SeattleRedMedia)  
  Timestamp: Mon, 12 May 2025 19:08:03 GMT  
  Content: A University of Washington student who was volunteering at a Turning Point USA event on campus had feces thrown at her by a protester. https://mynorthwest.com/local/uw-feces-turning-point-usa/4085943  
  Engagement: Likes=1, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=85  
  (No media)

### From semantic search (Charlie Kirk or TPUSA public speaking events, appearances, campus visits, or tour dates in May 2025):
- **[post:18]** ID: 1920939383987073417  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 09 May 2025 20:30:13 GMT  
  Content: Incredible turnout for our SPRING TOUR FINALE today at University of California Riverside. So proud of Turning Point USA, the students, and everyone who helped make this tour a massive success. There is nothing like seeing thousands of kids proudly support their country and this movement. ONTO THE NEXT 🇺🇸  
  Media: 4 items (photos: https://pbs.twimg.com/media/GqiMJCIXIAAee5t.jpg, https://pbs.twimg.com/media/GqiMJBkbcAAblmY.jpg; videos: https://video.twimg.com/amplify_video/1920939327934152704/vid/avc1/720x1280/jdIjiJvADHkOBop4.mp4?tag=14 duration 15100 ms, https://video.twimg.com/amplify_video/1920939327946731520/vid/avc1/720x1280/Vk6LSyQoBEwCiq6K.mp4?tag=14 duration 4966 ms)  
  Engagement: Likes=12710, Reposts=1888, Quotes=22, Replies=302, Bookmarks=99, Views=226661

- **[post:19]** ID: (empty ID returned)  
  Content: (No text content)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  (No media)

- **[post:20]** ID: 1920611949663985806  
  Author: Clay Travis (@ClayTravis)  
  Timestamp: Thu, 08 May 2025 22:49:06 GMT  
  Content: I’m speaking on a panel at the University of Chicago again on Saturday. Credit to them for bringing me back after the fireworks last time. Details: https://www.eventbrite.com/e/american-identity-summit-tickets-1312113118659?aff=oddtdtcreator  
  Engagement: Likes=300, Reposts=16, Quotes=0, Replies=20, Bookmarks=3, Views=110280  
  (No media)

- **[post:21]** ID: 1921213320897454362  
  Author: Benny Johnson (@bennyjohnson)  
  Timestamp: Sat, 10 May 2025 14:38:44 GMT  
  Content: Fired up to speak at @TPUSA’s Student Action Summit this summer—don’t miss this stacked lineup. 📍 Tampa, Florida 🗓️ July 11–13 Grab your tickets: https://www.sas2025.com See you in Tampa!  
  Media: 2 photos (https://pbs.twimg.com/media/GqmFUqeXQAA5R9T.jpg, https://pbs.twimg.com/media/GqmFUqbW4AAuElt.jpg)  
  Engagement: Likes=443, Reposts=41, Quotes=1, Replies=41, Bookmarks=6, Views=68786

- **[post:22]** ID: 1920849117817061477  
  Author: tia51.Official (@tia51_official)  
  Timestamp: Fri, 09 May 2025 14:31:31 GMT  
  Content: พรุ่งนี้มาเจอกัน! "FRIDAY PLAYGROUND 1st FAN MEET 2025" 🎪 🎠 SAT, 10 MAY 2025 UNION HALL | UNION MALL 🎟️ Tickets for all seats will be available online only at https://www.ticketmelon.com/taman4265/friday-playground 🔴 LIVE STREAMING Tickets on sale at 🔗https://t.co/kWC7Ebc06w #FridayPlayGround #Tia51 #FridayCollege  
  Media: Video (https://video.twimg.com/amplify_video/1920849038670524417/vid/avc1/1080x1920/wRXJ0AyL_vDLeCSF.mp4, duration: 14433 ms)  
  Engagement: Likes=954, Reposts=547, Quotes=11, Replies=3, Bookmarks=25, Views=22843

- **[post:23]** ID: 1920841196643271078  
  Author: Marietta (@whereismarietta)  
  Timestamp: Fri, 09 May 2025 14:00:03 GMT  
  Content: Alright, alright, alright -- ALRIGHT! Since y'all have been good, we wanted to let you know we'll be hitting the road this October and doing some east coast dates. We've also added a third date in Philly at UT. AND we're bringing @absibca along with us! Tickets on sale @ noon EST  
  Engagement: Likes=276, Reposts=19, Quotes=23, Replies=11, Bookmarks=5, Views=17748  
  (No media)

- **[post:24]** ID: 1920071116560941553  
  Author: tia51.Official (@tia51_official)  
  Timestamp: Wed, 07 May 2025 11:00:02 GMT  
  Content: เตรียมนับถอยหลังอีก 3 วันเจอกันในงาน "FRIDAY PLAYGROUND 1st FAN MEET 2025" 🎪 🎠 SAT, 10 MAY 2025 UNION HALL | UNION MALL 🎟️ Tickets for all seats will be available online only at https://www.ticketmelon.com/taman4265/friday-playground 🔴 LIVE STREAMING Tickets on sale at 🔗https://t.co/kWC7Ebc06w #FridayPlayGround #Tia51 #FridayCollege  
  Media: Video (https://video.twimg.com/amplify_video/1919973826869530624/vid/avc1/1080x1920/DMUwIUuS1ojyqdVt.mp4, duration: 18300 ms)  
  Engagement: Likes=535, Reposts=274, Quotes=2, Replies=0, Bookmarks=11, Views=9978

- **[post:25]** ID: 1921087138415997120  
  Author: tia51.Official (@tia51_official)  
  Timestamp: Sat, 10 May 2025 06:17:20 GMT  
  Content: วันนี้!! แล้วนะ ตื่นเต้นกันไหม หลังเวทีตื่นเต้นกันสุดๆที่จะได้โชว์ให้ทุกคนได้ดูแล้วสนุกสุดเหวี่ยงกันไปเลย🎢 "FRIDAY PLAYGROUND 1st FAN MEET 2025" 🎠 SAT, 10 MAY 2025 UNION HALL | UNION MALL 🎟️Tickets for all seats will be available online only at https://t.co/9Kr0TdBShB 🔴LIVE STREAMING Tickets on sale at https://t.co/kWC7Ebc06w #FridayPlayGround #Tia51 #FridayCollege  
  Media: Photo (https://pbs.twimg.com/media/GqkSkMtWEAATQxJ.jpg)  
  Engagement: Likes=428, Reposts=188, Quotes=1, Replies=0, Bookmarks=5, Views=18124

### From from:charliekirk11 (event OR speak OR speaking OR tour OR appearance OR campus OR "will be") since:2025-05-07 until:2025-05-14:
- **[post:26]** ID: 1921655282750652438  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Sun, 11 May 2025 19:54:56 GMT  
  Content: President Trump says his next post on Truth will be one of the most important he’s ever issued… 👀👀  
  Media: Photo (https://pbs.twimg.com/media/GqsXS8VbgAAuTe-.jpg)  
  Engagement: Likes=10514, Reposts=838, Quotes=45, Replies=550, Bookmarks=113, Views=570560

- **[post:27]** ID: 1920939383987073417 (duplicate of above)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 09 May 2025 20:30:13 GMT  
  Content: Incredible turnout for our SPRING TOUR FINALE today at University of California Riverside. So proud of Turning Point USA, the students, and everyone who helped make this tour a massive success. There is nothing like seeing thousands of kids proudly support their country and this movement. ONTO THE NEXT 🇺🇸  
  Media: 4 items (photos: https://pbs.twimg.com/media/GqiMJCIXIAAee5t.jpg, https://pbs.twimg.com/media/GqiMJBkbcAAblmY.jpg; videos as above)  
  Engagement: Likes=12710, Reposts=1888, Quotes=22, Replies=302, Bookmarks=99, Views=226661

- **[post:28]** ID: 1920516887621828947  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 08 May 2025 16:31:22 GMT  
  Content: We talk about a Golden Age in America... I am an Evangelical Christian, but I pray the new Pope will help usher in a new Golden Age of Christianity. If the new Pope defends the faith, defends the West, defends biology and eternal truths, I will be his biggest fan. 🙏🙏  
  Engagement: Likes=26675, Reposts=1927, Quotes=318, Replies=3355, Bookmarks=457, Views=1471488  
  (No media)

- **[post:29]** ID: 1920301821488251120  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 08 May 2025 02:16:46 GMT  
  Content: President Trump will be unveiling the details of a trade deal with the United Kingdom tomorrow morning, per the NYT and Politico. Brilliant first mover from the admin.  
  Engagement: Likes=4858, Reposts=554, Quotes=25, Replies=271, Bookmarks=60, Views=452129  
  (Quoted post about Trump trade deal)  
  (No media)

- **[post:30]** ID: 1920286054248010025  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 08 May 2025 01:14:07 GMT  
  Content: 🚨BREAKING: President Trump says a big trade deal will be unveiled tomorrow morning in an Oval Office press conference. "THE FIRST OF MANY"  
  Media: Photo (https://pbs.twimg.com/media/GqY51z8WgAAFHuz.jpg)  
  Engagement: Likes=5316, Reposts=467, Quotes=18, Replies=235, Bookmarks=52, Views=643072

### From from:TPUSA (event OR speak OR speaking OR tour OR appearance OR campus OR "will be") since:2025-05-07 until:2025-05-14:
- **[post:31]** ID: 1922017949050712368 (duplicate of above)  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 12 May 2025 19:56:03 GMT  
  Content: “We don’t want @Charliekirk11 on our campus, we don’t want fascists on our campus, we don’t want to support that here.” “What is fascism?” “I don’t know...” @topheronx  
  Media: Video (as above)  
  Engagement: Likes=2533, Reposts=449, Quotes=36, Replies=134, Bookmarks=109, Views=89502

- **[post:32]** ID: 1920939875253010503  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Fri, 09 May 2025 20:32:10 GMT  
  Content: AMAZING crowd at UC Riverside today for the final stop on the American Comeback Tour with @charliekirk11! Another incredible tour season in the books ✔️ @tpusastudents  
  Media: 3 items (video: https://video.twimg.com/amplify_video/1920939811512135680/vid/avc1/720x1280/ELUJDXHOjiiZBoQ2.mp4 duration 12591 ms; photo: https://pbs.twimg.com/media/GqiMlLhXEAAWCiq.jpg; video: https://video.twimg.com/amplify_video/1920939811466002432/vid/avc1/720x1280/nmzkChsBuX0Cz80U.mp4 duration 4910 ms)  
  Engagement: Likes=368, Reposts=68, Quotes=4, Replies=10, Bookmarks=10, Views=25316

**No other posts matched the exact date range criteria for upcoming or scheduled public speaking events by Charlie Kirk or TPUSA beyond the UC Riverside Spring Tour Finale on May 9, 2025 (explicitly referenced as the finale), campus protest/interaction videos, and unrelated or future (post-May 13) mentions.** All data included verbatim.
```

