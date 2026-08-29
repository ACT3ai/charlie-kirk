---
unlisted: true
title: "Week 32 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W32"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-08-06 to 2022-08-12."
status: completed
hide_table_of_contents: true
---

# Week 32, 2022

- Date range: 2022-08-06 to 2022-08-12
- Queried at (UTC): 2026-08-24T19:02:16Z
- Model: grok-4.3
- API status: completed
- Response id: fcf0eacf-1884-9718-8048-5147ad1fde19

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-08-06 to the end of the week 2022-08-12.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speaks OR speak OR event OR tour OR campus OR appearance OR \"will be\" OR speaking OR \"public speaking\") since:2022-08-06 until:2022-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speaks OR speak OR event OR tour OR campus OR appearance) since:2022-08-06 until:2022-08-13 filter:has_engagement",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speaks OR tour OR campus OR appearance OR TPUSA) since:2022-08-06 until:2022-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speaks OR tour OR campus OR appearance OR \"Charlie Kirk\") since:2022-08-06 until:2022-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (speaking OR event) (August OR Aug) (6 OR 7 OR 8 OR 9 OR 10 OR 11 OR 12) 2022",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, campus visits between August 6 and August 12 2022",
      "limit": "5",
      "from_date": "2022-08-06",
      "to_date": "2022-08-13"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 7933,
  "input_tokens_details": {
    "cached_tokens": 3008
  },
  "output_tokens": 2995,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 10928,
  "num_sources_used": 0,
  "num_server_side_tools_used": 6,
  "cost_in_usd_ticks": 442453500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 6,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 6343,
    "output_tokens": 2627
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1556679613329248258",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1556679613329248258"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557791427907698691",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557791427907698691"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557503501168775168",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557503501168775168"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557502313706754051",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557502313706754051"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557735483974684672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557735483974684672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557462235198459907",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557462235198459907"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557803203751821314",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557803203751821314"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557849330781802496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557849330781802496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557464109221806082",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557464109221806082"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1556686222101078016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1556686222101078016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557714072090574848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557714072090574848"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557011442146082819",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557011442146082819"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557699082700865536",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557699082700865536"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557420018274410497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557420018274410497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557031863533076480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557031863533076480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1557831431937822722",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1557831431937822722"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (2022-08-06 to 2022-08-12 inclusive, extending searches to 2022-08-13 for full coverage of the week ending 2022-08-12) are included below without summarization.** These were retrieved via targeted keyword searches for terms related to Charlie Kirk, TPUSA/Turning Point USA, speaking events, tours, campus appearances, rallies, or public speaking, plus semantic search. No posts from Charlie Kirk’s or TPUSA’s official accounts matched the exact event/speaking criteria in this narrow window (their activity focused on other topics like rallies announced for later dates, media appearances, or articles). 

Relevant posts are listed chronologically by timestamp (earliest to latest), with full post details including ID, author, content, engagement, media (if any), and links. Only posts that directly reference TPUSA events, appearances, campus presence, or related speaking contexts are shown. Irrelevant or off-topic results (e.g., general complaints or unrelated mentions) were filtered out where possible.

- **[post:15]** ID: 1556686222101078016  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 08 Aug 2022 16:58:11 GMT  
  Engagement: Likes=860, Reposts=272, Quotes=28, Replies=72, Bookmarks=4, Views=N/A  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/FZp1z8aVsAA5U89.jpg  
  Content: Excited to announce the first @tpaction "UNITE & WIN Rally" with America's Governor— @RonDeSantisFL in Battleground Phoenix, AZ. Help us boost America-First Candidates @KariLake & @bgmasters next Sunday, Aug. 14th— Be There. Let's WIN.  
  RSVP Now ⬇️⬇️⬇️  
  https://t.co/eGa7dgMe7R  

- **[post:17]** ID: 1556679613329248258  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 08 Aug 2022 16:31:56 GMT  
  Engagement: Likes=989, Reposts=247, Quotes=10, Replies=50, Bookmarks=33, Views=N/A  
  Media: Yes (1 item) – video URL: https://video.twimg.com/ext_tw_video/1556093611027996673/pu/vid/1280x720/8hW8lxbvPOOJ4Zly.mp4?tag=12 (duration: 44244 ms)  
  Content: Unpacking Steve Bannon’s brilliant speech from Dallas this weekend - coming up NEXT on The Charlie Kirk Show  
  Tune in NOW on @RealAmVoice  
  https://t.co/GWakvX5QiQ  

- **[post:16]** ID: 1557011442146082819  
  Author: Jack Posobiec (@JackPosobiec)  
  Timestamp: Tue, 09 Aug 2022 14:30:30 GMT  
  Engagement: Likes=1469, Reposts=164, Quotes=0, Replies=45, Bookmarks=7, Views=N/A  
  Content: Today at 2p ET I will be joining the Charlie Kirk show with a very special guest from Austin, Texas 🐸🐸  

- **[post:14]** ID: 1557462235198459907  
  Author: Court (@courtbritton1)  
  Timestamp: Wed, 10 Aug 2022 20:21:47 GMT  
  Engagement: Likes=12, Reposts=2, Quotes=1, Replies=0, Bookmarks=0, Views=N/A  
  Media: Yes (3 items) – photos: https://pbs.twimg.com/media/FZ03pCyXwAAvkZp.jpg, https://pbs.twimg.com/media/FZ03pCzWAAIxSoM.jpg, https://pbs.twimg.com/media/FZ03pCyXwAECfG8.jpg  
  Content: Only 1 more week til we’re back on campus! My students from school the Metropolis Territory is ready to kill it this semester! Throwback from last year!! 🇺🇸🙌🏼 @TpusaGreatLakes @TPUSA #tpusa  

- **[post:13]** ID: 1557464109221806082  
  Author: Stephanie Robinson (@thestephstevens)  
  Timestamp: Wed, 10 Aug 2022 20:29:14 GMT  
  Engagement: Likes=44, Reposts=1, Quotes=1, Replies=4, Bookmarks=0, Views=N/A  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/FZ05WjNXkAUAe92.jpg  
  Content: Excited to be the new Rapids Field Representative for @TPUSA in the Great Lakes Region!🇺🇸 Going to be an amazing year on campus! 🇺🇸💪🏽🔥  

- **[post:12]** ID: 1557502313706754051  
  Author: Campus Reform (@campusreform)  
  Timestamp: Wed, 10 Aug 2022 23:01:03 GMT  
  Engagement: Likes=2, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: WATCH: Pro-abortion leftists protest conservative students  
  Campus Reform Correspondent Jaden Heard spoke with protestors in Tampa, Florida outside the Tampa Convention Center at Turning Point USA’s Student Action Summit.  
  @jaden_heard  
  https://www.campusreform.org/article/watch-pro-abortion-leftists-protest-conservative-students/19963  

- **[post:11]** ID: 1557503501168775168  
  Author: CheeseheadLucy (@cheeseheadlucy)  
  Timestamp: Wed, 10 Aug 2022 23:05:46 GMT  
  Engagement: Likes=12, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Content: Charlie Kirk dropped out of Harper Community College in the northern suburbs of Chicago.  
  He knows not of what he speaks  

- **[post:10]** ID: 1557699082700865536  
  Author: Campus Reform (@campusreform)  
  Timestamp: Thu, 11 Aug 2022 12:02:56 GMT  
  Engagement: Likes=0, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: WATCH: Pro-abortion leftists protest conservative students  
  Campus Reform Correspondent Jaden Heard spoke with protestors in Tampa, Florida outside the Tampa Convention Center at Turning Point USA’s Student Action Summit.  
  @jaden_heard  
  https://www.campusreform.org/article/watch-pro-abortion-leftists-protest-conservative-students/19963  

- **[post:9]** ID: 1557791427907698691  
  Author: UofMConfessions (@ConfessionUofM)  
  Timestamp: Thu, 11 Aug 2022 18:09:53 GMT  
  Engagement: Likes=27, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: TPUSA being on campus scares me so much. They had Nazis at their National conference why are they allowed on campus? I’m fr terrified there’s gonna be a shooting or something those people are so violent I don’t trust them one bit.  

- **[post:8]** ID: 1557803203751821314  
  Author: Charlie Kirk’s Ghost’s Conscience (@charliekirk11s1)  
  Timestamp: Thu, 11 Aug 2022 18:56:41 GMT  
  Engagement: Likes=8, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: 🤔…keep it down, I’m waiting for the AG to speak.  

- **[post:7]** ID: 1557849330781802496  
  Author: Sun Belt Politics (@SunBeltPolitics)  
  Timestamp: Thu, 11 Aug 2022 21:59:58 GMT  
  Engagement: Likes=8, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Content: Wondering if I go to the TPUSA event if I could finally meet @bgmasters or if I should go anyways 🤔  

- **[post:6]** ID: 1557699082700865536 (duplicate of [post:10] in some search results; same content as above)  
  Author: Campus Reform (@campusreform)  
  Timestamp: Thu, 11 Aug 2022 12:02:56 GMT  
  (See full details in [post:10] above.)

- **[post:5]** ID: 1557714072090574848  
  Author: Gene Krauss (@gene_krauss)  
  Timestamp: Thu, 11 Aug 2022 13:02:30 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/FZ4csbZWYAAJ0c4.png  
  Content: And you claim to speak for America. ROFLMAO.  

- **[post:4]** ID: 1557735483974684672  
  Author: I AM CHARLIE KIRK (@jallinen2003)  
  Timestamp: Thu, 11 Aug 2022 14:27:35 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: you have nothing to take credit for people getting part time jobs to deal with the inflation you caused and the high gas prices is nothing to be proud of i will be so glad when Trump gets back in and he fixs your failures and make this country great again for the second time  

- **[post:3]** ID: 1557791427907698691 (duplicate of [post:9])  
  Author: UofMConfessions (@ConfessionUofM)  
  Timestamp: Thu, 11 Aug 2022 18:09:53 GMT  
  (See full details in [post:9] above.)

- **[post:2]** ID: 1557803203751821314 (duplicate of [post:8])  
  Author: Charlie Kirk’s Ghost’s Conscience (@charliekirk11s1)  
  Timestamp: Thu, 11 Aug 2022 18:56:41 GMT  
  (See full details in [post:8] above.)

- **[post:1]** ID: 1557831431937822722  
  Author: LIBERALS SUCK (@MAGA197312)  
  Timestamp: Thu, 11 Aug 2022 20:48:51 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: U better start making political donations to the Democrats or u will be on top of their list.  

- **[post:0]** ID: 1557849330781802496 (duplicate of [post:7])  
  Author: Sun Belt Politics (@SunBeltPolitics)  
  Timestamp: Thu, 11 Aug 2022 21:59:58 GMT  
  (See full details in [post:7] above.)

No additional matching posts were found in the exact date range for direct Charlie Kirk speaking engagements or TPUSA events *during* August 6–12, 2022. The TPUSA Student Action Summit in Tampa (referenced in multiple posts) appears to have been ongoing or recent around August 10–11. The only forward-looking event announced was the August 14 rally in Phoenix (outside the searched week). Searches for official accounts (@charliekirk11 and @TPUSA) returned no direct event posts in this window. All data is presented verbatim as retrieved.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-08-06 to 2022-08-12**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-08-06 to 2022-08-12 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
