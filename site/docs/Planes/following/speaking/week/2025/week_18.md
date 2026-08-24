---
unlisted: true
title: "Week 18 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W18"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-04-30 to 2025-05-06."
status: completed
hide_table_of_contents: true
---

# Week 18, 2025

- Date range: 2025-04-30 to 2025-05-06
- Queried at (UTC): 2026-08-24T19:18:15Z
- Model: grok-4.3
- API status: completed
- Response id: f2449d2e-f4bf-9eb2-a5d1-0b833fae17ec

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-04-30 to the end of the week 2025-05-06.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speak OR speaking OR event OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2025-04-30 until:2025-05-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speak OR speaking OR event OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2025-04-30 until:2025-05-07 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus tours, or where Charlie Kirk will speak between April 30 and May 6 2025",
      "limit": "10",
      "from_date": "2025-04-30",
      "to_date": "2025-05-07"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 9212,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 3417,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 12629,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 318319000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 3,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 7622,
    "output_tokens": 3219
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919518865811181957",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919518865811181957"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1918054049657790928",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1918054049657790928"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919521683657892183",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919521683657892183"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919527817898865000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919527817898865000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1918065438661243079",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1918065438661243079"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919478100473040987",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919478100473040987"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919527073208520794",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919527073208520794"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919530588861612278",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919530588861612278"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919495828495888511",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919495828495888511"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1918033127815168417",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1918033127815168417"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917574442307445255",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917574442307445255"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919529451768906171",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919529451768906171"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919521365293465895",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919521365293465895"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919057727906558189",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919057727906558189"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919472234927948162",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919472234927948162"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917523046614851624",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917523046614851624"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919521306506375169",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919521306506375169"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1918301707274011035",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1918301707274011035"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1917696055447085504",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1917696055447085504"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1919536523172614155",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1919536523172614155"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1918090541578817908",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1918090541578817908"
  }
]
```

## Grok response

```text
**Here is every relevant post from the X searches (keyword and semantic) matching the criteria for posts between 2025-04-30 and 2025-05-06 (inclusive of the until:2025-05-07 cutoff), without any summarization or filtering beyond the tool results. All posts are presented in full with their metadata.**

### Posts from the first keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA" + event/speaking terms, Latest mode):
- **[post:0]** ID: 1919536523172614155  
  Author: Olivia Weston (@pakdesen)  
  Timestamp: Mon, 05 May 2025 23:35:45 GMT  
  Content: The reason why Charlie Kirk has such "appeal" in public universities like CSU is that he makes good use of the "social media rhetoric + on-site confrontation" model that the current Z generation likes, instantly breaking the daily tranquility of the campus and making more young people start to think about "what do I believe in?"  
  Engagement: Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=300

- **[post:1]** ID: 1919530588861612278  
  Author: 🌐 BehindTheHeadlines (@BTHLines)  
  Timestamp: Mon, 05 May 2025 23:12:10 GMT  
  Content: Charlie Kirk is red-pilling California one campus at a time.  
  Engagement: Likes=42, Reposts=5, Quotes=0, Replies=1, Bookmarks=0, Views=1786

- **[post:2]** ID: 1919529451768906171  
  Author: We miss Charlie Kirk (@legaldawn)  
  Timestamp: Mon, 05 May 2025 23:07:39 GMT  
  Content: @HouseGOP better get their act together or they will be in the food line come election time  
  (Quoted post from Laura Loomer about impeachment and midterms; not directly about events)

- **[post:3]** ID: 1919527817898865000  
  Author: Donna Faulkner (@DonnaRev1111)  
  Timestamp: Mon, 05 May 2025 23:01:09 GMT  
  Content: You are the perfect person to be California governor! Great spirit. Transparent. Speak truth to power. Excellent communicator!

- **[post:4]** ID: 1919527073208520794  
  Author: Red haired lass ☘️ Fight the trump criminal mafia (@Smapsley)  
  Timestamp: Mon, 05 May 2025 22:58:11 GMT  
  Content: I think you might have doxxed me today. I will be reporting you.

- **[post:5]** ID: 1919521683657892183  
  Author: Joann Sands (@JoannSands1)  
  Timestamp: Mon, 05 May 2025 22:36:47 GMT  
  Content: Thank you, Charlie Kirk, for all your hard work reaching out to the younger generations speaking the truth.  
  Engagement: Likes=26, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=596

- **[post:6]** ID: 1919521365293465895  
  Author: B. W (@Bwildes)  
  Timestamp: Mon, 05 May 2025 22:35:31 GMT  
  Content: Scott Starboard Show Ep46 Karen Read Day 9 Recap! Alex Stein TPUSA Event! https://www.youtube.com/live/qmjcEHOOTzE?si=v-mX_yyzryYbO1_I via @YouTube  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=237

- **[post:7]** ID: 1919521306506375169  
  Author: Deano 🇺🇸 (@Notoriousdyc)  
  Timestamp: Mon, 05 May 2025 22:35:17 GMT  
  Content: As a CSULB alum, I can tell you Charlie has his work cut out for him on that campus.  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=156

- **[post:8]** ID: 1919518865811181957  
  Author: P.I-Thor (@stephens_county)  
  Timestamp: Mon, 05 May 2025 22:25:35 GMT  
  Content: Well, that’s NOT shocking.. the SWAMP CREATURES perceive him as “young & impressionable” and he will be if he gets compromised.. I hope he is “awake” and truly understands the game they are playing and what’s at stake! I’m thrilled to gave young engaging but with the swamp as “mentors” he’ll become like the indoctrinated TPUSA youth.. moderates.. OH BE CAREFUL of the MODERATES.. in the Bible “lukewarm” gets spewed from Yahuah mouth!

### Posts from the second keyword search (same query + filter:links, Latest mode):
- **[post:9]** ID: 1919529451768906171 (duplicate of post:2)  
  Author: We miss Charlie Kirk (@legaldawn)  
  Timestamp: Mon, 05 May 2025 23:07:39 GMT  
  Content: @HouseGOP better get their act together or they will be in the food line come election time

- **[post:10]** ID: 1919521365293465895 (duplicate of post:6)  
  Author: B. W (@Bwildes)  
  Timestamp: Mon, 05 May 2025 22:35:31 GMT  
  Content: Scott Starboard Show Ep46 Karen Read Day 9 Recap! Alex Stein TPUSA Event! https://www.youtube.com/live/qmjcEHOOTzE?si=v-mX_yyzryYbO1_I via @YouTube

- **[post:11]** ID: 1919478100473040987  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Mon, 05 May 2025 19:43:35 GMT  
  Content: The American Comeback Tour with @charliekirk11 drew a serious crowd at Cal State Long Beach 🔥  
  @tpusastudents  
  (Media: 1 photo)  
  Engagement: Likes=389, Reposts=62, Quotes=0, Replies=10, Bookmarks=4, Views=15569

- **[post:12]** ID: 1919472234927948162  
  Author: ethan (@erhod55)  
  Timestamp: Mon, 05 May 2025 19:20:17 GMT  
  Content: charlie kirk on my campus  
  (Media: 1 video)  
  Engagement: Likes=19, Reposts=1, Quotes=0, Replies=0, Bookmarks=1, Views=1253

### Posts from the semantic search (Charlie Kirk or TPUSA public speaking events... between April 30 and May 6 2025):
- **[post:13]** ID: 1919495828495888511  
  Author: American AF 🇺🇸 (@iAnonPatriot)  
  Timestamp: Mon, 05 May 2025 20:54:02 GMT  
  Content: Charlie Kirk is TAKING OVER college campuses all throughout California..  
  📍Cal State Long Beach  
  (Media: 1 video)  
  Engagement: Likes=401, Reposts=58, Quotes=3, Replies=26, Bookmarks=4, Views=13041

- **[post:14]** ID: 1917523046614851624  
  Author: Kathleen Winchell ❤️🤍💙🇺🇸🇺🇸 (@KathleenWinche3)  
  Timestamp: Wed, 30 Apr 2025 10:14:54 GMT  
  Content: Charlie is talking about his tour and they how they were rudely interrupted during this particular event at Texas A&M.  
  Dean and Parker were the instigators! Listen below for more details!  
  @charliekirk11 keep doing what you’re doing because you and TPUSA our making a HUGE difference. ♥️♥️♥️  
  (Media: 1 video)  
  Engagement: Likes=214, Reposts=64, Quotes=0, Replies=2, Bookmarks=8, Views=7057

- **[post:15]** ID: 1918301707274011035  
  Author: American AF 🇺🇸 (@iAnonPatriot)  
  Timestamp: Fri, 02 May 2025 13:49:01 GMT  
  Content: SHEEESH.. Charlie Kirk TOOK OVER UC San Diego yesterday.  
  🔥🔥🔥  
  (Media: 1 video)  
  Engagement: Likes=373, Reposts=40, Quotes=2, Replies=31, Bookmarks=8, Views=10061

- **[post:16]** ID: 1918033127815168417  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Thu, 01 May 2025 20:01:47 GMT  
  Content: The American Comeback Tour with @charliekirk11 made its mark at University of California San Diego 🇺🇸 🔥  
  @tpusastudents  
  (Media: 1 photo)  
  Engagement: Likes=242, Reposts=33, Quotes=2, Replies=5, Bookmarks=3, Views=11013

- **[post:17]** ID: 1919057727906558189  
  Author: Ryan Hendrickson (@tipofthespear42)  
  Timestamp: Sun, 04 May 2025 15:53:11 GMT  
  Content: The trip home is never easy or smooth, but I made it with a few days to spare. May 6th in Atlanta is going to be amazing! I'll be speaking at the Atlanta History Center about my military career, my book, but more importantly, our mission in Ukraine. If you are in the Atlanta area, I'd love to see you there. Check out the link for more information. https://t.co/sEYo6XZgtY  
  Huge shoutout to ATLVets for making this happen! It's going to be epic.  
  (Media: 4 photos)  
  Engagement: Likes=206, Reposts=30, Quotes=1, Replies=3, Bookmarks=2, Views=15827  
  (Note: This post is about Ryan Hendrickson speaking on May 6, 2025, not Charlie Kirk or TPUSA.)

- **[post:18]** ID: 1918090541578817908  
  Author: ABC 33/40 News (@abc3340)  
  Timestamp: Thu, 01 May 2025 23:49:56 GMT  
  Content: President Trump arrives at the Tuscaloosa National Airport for the University of Alabama Spring 2025 Graduation Commencement Address.  
  The President is scheduled to speak at 7 p.m.  
  #trump #news #national  
  (Media: 1 video)  
  Engagement: Likes=239, Reposts=11, Quotes=2, Replies=6, Bookmarks=8, Views=9566  
  (Note: About President Trump speaking at University of Alabama, not Charlie Kirk or TPUSA.)

- **[post:19]** ID: 1917574442307445255  
  Author: Kyle Langford (@KyleLangfordCA)  
  Timestamp: Wed, 30 Apr 2025 13:39:08 GMT  
  Content: Good morning LangGang🕺🏼💜  
  1.) this SATURDAY; May 3rd join me @ Unite Inland Empire (feat. @Riley_Gaines_ )  
  https://www.eventbrite.com/e/unite-ie-conservative-summit-tickets-1256853395339  
  2.) Join for for CFPAC after the convention (also May 3rd but at 6pm)  
  https://t.co/V0cbuC52Oe  
  🐻✝️🇺🇸  
  (Media: 1 video)  
  Engagement: Likes=354, Reposts=31, Quotes=1, Replies=19, Bookmarks=9, Views=19749  
  (Note: About Kyle Langford and Riley Gaines events on May 3, 2025, not Charlie Kirk or TPUSA.)

- **[post:20]** ID: 1917696055447085504  
  Author: Doug Jones (@DougJones)  
  Timestamp: Wed, 30 Apr 2025 21:42:23 GMT  
  Content: Trump invited himself to the U of A – so now, I'm inviting you to show the world that Alabama and the rest of America have had enough.  
  My friend @Beto O’Rourke and I will be in Tuscaloosa tomorrow in Snow Hinton Park. If you’re anywhere around we’d love to see you there.  
  (Media: 1 photo)  
  Engagement: Likes=1360, Reposts=564, Quotes=8, Replies=69, Bookmarks=17, Views=26535  
  (Note: About Doug Jones and Beto O’Rourke counter-event, not Charlie Kirk or TPUSA.)

- **[post:21]** ID: 1918054049657790928  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 01 May 2025 21:24:55 GMT  
  Content: UC San Diego showed up HUGE🔥🔥  
  Young people are defying the poltical geography that’s divided America for generations, even in California.  
  This state is DESPERATE for a rebirth of freedom 🇺🇸🇺🇸  
  (Media: 4 photos + 1 video)  
  Engagement: Likes=20648, Reposts=3548, Quotes=137, Replies=681, Bookmarks=201, Views=678161

- **[post:22]** ID: 1918065438661243079  
  Author: MAGA Voice (@MAGAVoice)  
  Timestamp: Thu, 01 May 2025 22:10:11 GMT  
  Content: HOLY SH*T 🚨 THOUSANDS of students from UC San Diego showed up for Charlie Kirk in Deep Blue California. MSM will say this isn’t possible 🔥  
  Remarkable to see how energized Gen Z Voters are for the MAGA Party during a non Election Season  
  The Great Awakening is happening ❤️  
  (Media: 1 video)  
  Engagement: Likes=9224, Reposts=2330, Quotes=40, Replies=265, Bookmarks=104, Views=162079

**No other posts matched the exact date range and search criteria in the tool outputs.** All data above is included verbatim as returned.
```

