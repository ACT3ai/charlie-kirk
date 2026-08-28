---
unlisted: true
title: "Week 31 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W31"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-07-30 to 2023-08-05."
status: completed
hide_table_of_contents: true
---

# Week 31, 2023

- Date range: 2023-07-30 to 2023-08-05
- Queried at (UTC): 2026-08-24T19:08:16Z
- Model: grok-4.3
- API status: completed
- Response id: 7cb01b5d-afee-9a7e-b330-5d754e6e1d6f

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-07-30 to the end of the week 2023-08-05.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR events OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR appearing OR schedule OR \"speaking event\") since:2023-07-30 until:2023-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR events OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR appearing OR schedule OR \"speaking event\") since:2023-07-30 until:2023-08-06 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR events OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR appearing OR schedule OR \"speaking event\") since:2023-07-30 until:2023-08-06 min_faves:1",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie Kirk will speak between July 30 and August 5 2023",
      "limit": "10",
      "from_date": "2023-07-30",
      "to_date": "2023-08-06",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\" OR @TPUSA) (event OR events OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR appearing OR schedule OR \"speaking event\" OR \"field organizer\" OR training OR \"at TPUSA\" OR HQ) since:2023-07-30 until:2023-08-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR events OR speaking OR speak OR speech OR tour OR appearance OR schedule OR \"will be\" OR training OR organizer) since:2023-07-30 until:2023-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR events OR speaking OR speak OR speech OR tour OR appearance OR schedule OR \"will be\" OR training OR organizer) since:2023-07-30 until:2023-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Arizona OR \"Austin Smith\" OR \"Ken Blackwell\" OR \"Kingdom to The Capitol\" OR \"See You at the Library\" OR \"Summer Farm Fest\") since:2023-07-30 until:2023-08-06",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA events, speeches, appearances, tours, trainings, or where Charlie Kirk is speaking or appearing July 30 to August 5 2023",
      "limit": "10",
      "from_date": "2023-07-30",
      "to_date": "2023-08-06",
      "min_score_threshold": "0.05"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 28272,
  "input_tokens_details": {
    "cached_tokens": 12992
  },
  "output_tokens": 2353,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 30625,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 725809000,
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
    "input_tokens": 16699,
    "output_tokens": 1666
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687578165726572545",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687578165726572545"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1685725722000687104",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1685725722000687104"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686514929145348098",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686514929145348098"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687367177131978752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687367177131978752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687609219913052161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687609219913052161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687366995778715648",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687366995778715648"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686889467729305600",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686889467729305600"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687586692876607488",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687586692876607488"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687561206104735746",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687561206104735746"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687545847175614464",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687545847175614464"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686779571964895232",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686779571964895232"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686095950341640192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686095950341640192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686449402716504065",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686449402716504065"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686183434874691584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686183434874691584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686771033414443009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686771033414443009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687296347173724160",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687296347173724160"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687291962695507968",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687291962695507968"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687557592325754880",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687557592325754880"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687614249739173889",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687614249739173889"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687609762479849472",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687609762479849472"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686838117658132481",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686838117658132481"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687104714004148224",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687104714004148224"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686049575407427584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686049575407427584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687610364412997638",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687610364412997638"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687601636154245120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687601636154245120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686590730700206080",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686590730700206080"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687565579710832642",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687565579710832642"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1685747241829728256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1685747241829728256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1685470835341971456",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1685470835341971456"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687608770409660416",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687608770409660416"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687614311861035008",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687614311861035008"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687470389159727104",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687470389159727104"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686868450906386433",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686868450906386433"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687579487142383616",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687579487142383616"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687609980688482304",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687609980688482304"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687612291045371904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687612291045371904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687547945238065152",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687547945238065152"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687454084612128768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687454084612128768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1687537703871512598",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1687537703871512598"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1686779349188669440",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1686779349188669440"
  }
]
```

## Grok response

```text
**Here is all raw data from X (Twitter) posts matching the specified date range (2023-07-30 to 2023-08-05, using until:2023-08-06 for full week coverage) related to Charlie Kirk or TPUSA public speaking events, appearances, tours, trainings, or where Charlie Kirk/TPUSA will speak or appear. No summarization—full post content, metadata, and context preserved from tool results. Only relevant posts included; irrelevant or off-topic results (e.g., general mentions without event details) filtered out in presentation.**

### Posts from searches (exact matches to keywords like event/speaking/tour/training/appearance/schedule/"will be"/"at TPUSA HQ", etc.):

- **Post ID: 1686049575407427584**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 31 Jul 2023 16:21:58 GMT  
  Engagement: Likes=431, Reposts=55, Quotes=5, Replies=22, Bookmarks=1, Views=39245  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F2YM3KYa4AASEJt.jpg  
  Content: "50 new college and high school field organizers from around the country getting trained at @TPUSA HQ today! GROWTH"

- **Post ID: 1687565579710832642**  
  Author: Ken Blackwell (@kenblackwell)  
  Timestamp: Fri, 04 Aug 2023 20:46:02 GMT  
  Engagement: Likes=4, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=526  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F2tv8xkXUAAJklp.jpg  
  Content: "Arizona State Representative Austin Smith of @TPUSA speaking to the crowd. Proud to have TPUSA as one of our co-hosts for this great event!"

- **Post ID: 1687547945238065152**  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Fri, 04 Aug 2023 19:35:57 GMT  
  Engagement: Likes=15, Reposts=1, Quotes=0, Replies=1, Bookmarks=1, Views=754  
  Quoted Post: Sean Feucht (@seanfeucht) – "It’s was comical to watch these pathetic protestors in the Pacific Northwest squirm while witnessing a church that would not be bullied, silenced or backed into a corner. Thousands upon thousands showed up to worship God with boldness and passion! A new season in America⚡️🔥🙏🏽" (with 3 photos)  
  Content: "Comment below if you have attended any of our Kingdom to The Capitol tour stops & what state it was. 🙌🏼"

- **Post ID: 1687104714004148224** (mentions Kirk Cameron event on 2023-08-05, overlapping TPUSA-adjacent conservative circles)  
  Author: Kirk Cameron (@KirkCameron)  
  Timestamp: Thu, 03 Aug 2023 14:14:43 GMT  
  Engagement: Likes=1105, Reposts=225, Quotes=21, Replies=74, Bookmarks=3, Views=85730  
  Media: Yes (3 items) – photos of event materials  
  Content: "Join me this Saturday, August 5th, for the first National 'See You at the Library’ day with thousands of faithful Americans for a day of singing, praying, and reading. I will be visiting 3 libraries with @BraveBooksUS and @Riley_Gaines_: 1. TENNESSEE: We will be at the Hendersonville Public Library in Hendersonville, TN, for a reading that starts at 8 am CT. 2. ALABAMA: Next, we will be at Madison Public Library in Huntsville, AL starting at 10 am. 3. TEXAS: Finally, we will be at the Taylor Public Library in Taylor, TX, right outside Austin in the afternoon. Join tens of thousands of Americans at over 300 libraries across the country in this mission to bring faith and good moral values back into our public institutions. Invite your friends and family this Saturday for a sweet time of singing, praying, and reading! I can't wait to see you at the library! Locate your nearest library for the event by clicking the link below:"

- **Post ID: 1687601636154245120** (related to above Kirk Cameron event)  
  Author: Jack Posobiec (@JackPosobiec)  
  Timestamp: Fri, 04 Aug 2023 23:09:18 GMT  
  Engagement: Likes=658, Reposts=139, Quotes=4, Replies=5, Bookmarks=0, Views=48157  
  Content: "EXCLUSIVE: Kirk Cameron gears up for nationwide 'See You at the Library' day, goes after the ALA, and is confident 'good will triumph over evil' https://thepostmillennial.com/exclusive-kirk-cameron-gears-up-for-nationwide-see-you-at-the-library-day-goes-after-the-ala-and-is-confident-good-will-triumph-over-evil?utm_campaign=64483"

### Additional related posts from broader keyword/semantic searches (still within date range, referencing events/appearances/speaking):

- **Post ID: 1687454084612128768**  
  Author: Human Events (@HumanEvents)  
  Timestamp: Fri, 04 Aug 2023 13:22:59 GMT  
  Engagement: Likes=101, Reposts=25, Quotes=1, Replies=6, Bookmarks=2, Views=25472  
  Media: Yes (1 item) – video URL: https://video.twimg.com/ext_tw_video/1687453503969533953/pu/vid/640x352/dxQMqgY1FzS4ieLn.mp4?tag=12 (duration: 480566 ms)  
  Content: ".@charliekirk11 talks about the time Mike Pence attended Turning Point USA conference: 'He created his own political grave'"

- **Post ID: 1686868450906386433**  
  Author: Alex Nicoll (@realalexnicoll)  
  Timestamp: Wed, 02 Aug 2023 22:35:53 GMT  
  Engagement: Likes=208, Reposts=46, Quotes=1, Replies=9, Bookmarks=0, Views=31472  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F2jwtojXMAAq7B3.jpg  
  Content: "📥INBOX: @KariLake to Deliver Speech at Summer Farm Fest in Ohio FREE TICKETS: https://t.co/FKoHsKntVT MEDIA CREDENTIALS: https://t.co/7SOvR38hM4"

- **Post ID: 1686779571964895232** (Charlie Kirk live broadcast context)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 02 Aug 2023 16:42:43 GMT  
  Engagement: Likes=654, Reposts=217, Quotes=1, Replies=54, Bookmarks=30, Views=174508  
  Content: "LIVE now with John Eastman, 'Co-Conspirator 2' https://rumble.com/v344jnx-the-january-6-indictment-eastman-rep.-bishop-donald-trump-jr.-driscoll-live.html"

No direct posts from @TPUSA official account in the results for this exact range. No other specific dates/locations for Charlie Kirk personal speaking appearances found in the searched posts. All data extracted directly from tool outputs without alteration.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-07-30 to 2023-08-05**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-07-30 to 2023-08-05 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
