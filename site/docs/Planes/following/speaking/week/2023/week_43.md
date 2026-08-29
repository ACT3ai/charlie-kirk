---
unlisted: true
title: "Week 43 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W43"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-10-22 to 2023-10-28."
status: completed
hide_table_of_contents: true
---

# Week 43, 2023

- Date range: 2023-10-22 to 2023-10-28
- Queried at (UTC): 2026-08-24T19:09:39Z
- Model: grok-4.3
- API status: completed
- Response id: d8432daa-d672-9c1b-9839-7e931c267b09

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-10-22 to the end of the week 2023-10-28.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR speaking OR appears OR appearance) since:2023-10-22 until:2023-10-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR speaking OR appears OR appearance) since:2023-10-22 until:2023-10-29 filter:has_engagement",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between October 22-28 2023",
      "limit": "10",
      "from_date": "2023-10-22",
      "to_date": "2023-10-28"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 9516,
  "input_tokens_details": {
    "cached_tokens": 3008
  },
  "output_tokens": 4348,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 13864,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 346066000,
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
    "input_tokens": 7926,
    "output_tokens": 4147
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718021086569287786",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718021086569287786"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1716911161336078394",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1716911161336078394"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718012900764193266",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718012900764193266"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717996481297137779",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717996481297137779"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717981987527692493",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717981987527692493"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718039631000723584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718039631000723584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717975185016467617",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717975185016467617"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717697290037788703",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717697290037788703"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1716506405132468378",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1716506405132468378"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718015391140594021",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718015391140594021"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717580073434255522",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717580073434255522"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717969786825523209",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717969786825523209"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718001766187319454",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718001766187319454"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718051326939025575",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718051326939025575"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717903979210826177",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717903979210826177"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1718003901406851387",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1718003901406851387"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717931747873055182",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717931747873055182"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1716921899144331374",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1716921899144331374"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717041883019641098",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717041883019641098"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717995000892432514",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717995000892432514"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1717947107175170279",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1717947107175170279"
  }
]
```

## Grok response

```text
**Here is the complete, un-summarized data from the X (Twitter) searches for posts mentioning Charlie Kirk or TPUSA/ Turning Point USA in connection with public speaking events, appearances, tours, campuses, or speaking opportunities, limited to the exact date range 2023-10-22 to 2023-10-28 (posts with timestamps within that week). All results from the keyword and semantic searches are included below with full post content, metadata, and any media descriptions. No posts were excluded.**

### Keyword Search Results (Latest mode, including has_engagement filter where applicable):

- **Post [post:0]**  
  ID: 1718051326939025575  
  Author: @Eleniphu  
  Timestamp: Fri, 27 Oct 2023 23:45:30 GMT  
  Content: There would have 10 times the people attending   Owens appearance if the fascist racists at UB hadn’t used devious assault tactics on her.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=9  
  (Mentions Owens appearance; context ties to TPUSA-related events.)

- **Post [post:1]**  
  ID: 1718039631000723584  
  Author: @MagnificentGodX  
  Timestamp: Fri, 27 Oct 2023 22:59:02 GMT  
  Content: “Therefore I tell you that the kingdom of God will be taken away from you and given to a people who will produce its fruit. Anyone who falls on this stone will be broken to pieces; anyone on whom it falls will be crushed.”  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=26  
  (No direct event mention; included per search match.)

- **Post [post:2] / [post:9]** (duplicate across searches)  
  ID: 1718021086569287786  
  Author: @ana_parks02  
  Timestamp: Fri, 27 Oct 2023 21:45:20 GMT  
  Content: Tarheel dream team!🔥 So blessed to be working for this amazing organization and alongside Abby here in NC! This state is changing for the better with every student, chapter, and event! Full steam ahead🚂🇺🇸! @TPUSA @tpusastudents #americafirst #tpusa #chapterschangetheworld  
  Engagement: Likes=6, Reposts=4, Quotes=0, Replies=2, Bookmarks=0, Views=306  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9ejEdgXoAACM47.jpg  
  (Mentions TPUSA events and chapters in NC.)

- **Post [post:3]**  
  ID: 1718015391140594021  
  Author: @Philosorap1694  
  Timestamp: Fri, 27 Oct 2023 21:22:43 GMT  
  Content: Charlie Kirk has 2.6 million followers because the far -right represents a large segment of the US population, and they are clearly not serious human beings.  Just read this loony post. This does not speak well for the future of our democracy.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=7  
  (Mentions Charlie Kirk.)

- **Post [post:4]**  
  ID: 1718012900764193266  
  Author: @MrReediculous1  
  Timestamp: Fri, 27 Oct 2023 21:12:49 GMT  
  Content: JOHN WAS NOT ALLOWED TO SPEAK! ft. John Amanchukwu | TPUSA Faith https://t.co/ekOm8Nma6f via @YouTube  
  Engagement: Likes=0, Reposts=0, Replies=0, Bookmarks=0, Views=5  
  (Mentions TPUSA Faith event/speaking.)

- **Post [post:5]**  
  ID: 1718003901406851387  
  Author: @Robbie347  
  Timestamp: Fri, 27 Oct 2023 20:37:03 GMT  
  Content: This has given me a new podcast idea: drunk me is going to break down Charlie Kirk and Ben Shapiro's points. It will be hilarious, but it will also be NC-17.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=19  
  (Mentions Charlie Kirk.)

- **Post [post:6]**  
  ID: 1718001766187319454  
  Author: @marshalotis  
  Timestamp: Fri, 27 Oct 2023 20:28:34 GMT  
  Content: Speaking of 'hideous abominations'; Charlie Kirk!😅  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=1  
  (Mentions Charlie Kirk.)

- **Post [post:7] / [post:12]** (duplicate)  
  ID: 1717996481297137779  
  Author: @peterchristos  
  Timestamp: Fri, 27 Oct 2023 20:07:34 GMT  
  Content: Thank you for having me @IngrahamAngle to talk about the violent Anti-Zionist attack my co-worker and I from @TPUSA faced, while attending a Solidarity for Israel event in Skokie, IL. Now more than ever, it’s important to get organized & speak up for what is right.  
  Engagement: Likes=69, Reposts=28, Quotes=0, Replies=5, Bookmarks=1, Views=4077  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9eMsX4WQAAST9n.jpg  
  (Mentions TPUSA event in Skokie, IL.)

- **Post [post:8]**  
  ID: 1717995000892432514  
  Author: @RemyVTR15  
  Timestamp: Fri, 27 Oct 2023 20:01:41 GMT  
  Content: just like always, you'll have 3-5 that u can depend on out of 12... then there will be 5 that improve to competent, then 2-5 that will be replaced.  
  (Quoted post about speed reloads; no direct event.)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=22

- **Post [post:10]**  
  ID: 1718003901406851387 (same as post:5)  
  Author: @Robbie347  
  Timestamp: Fri, 27 Oct 2023 20:37:03 GMT  
  Content: This has given me a new podcast idea: drunk me is going to break down Charlie Kirk and Ben Shapiro's points. It will be hilarious, but it will also be NC-17.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=19

- **Post [post:11]**  
  ID: 1718001766187319454 (same as post:6)  
  Author: @marshalotis  
  Timestamp: Fri, 27 Oct 2023 20:28:34 GMT  
  Content: Speaking of 'hideous abominations'; Charlie Kirk!😅  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=1

- **Post [post:13]**  
  ID: 1717981987527692493  
  Author: @basednblessed  
  Timestamp: Fri, 27 Oct 2023 19:09:59 GMT  
  Content: ‼️POV: TPUSA x Dream City Christian School : High School Fearless Leaders edition‼️ 📣Championing faith and freedom on campus every day📣 Special thanks to Mr. Alvarado for supporting our efforts and securing tabling time and morning announcements 🫡  
  Engagement: Likes=9, Reposts=3, Quotes=0, Replies=1, Bookmarks=0, Views=453  
  Media: Yes (4 items) – photos URLs: https://pbs.twimg.com/media/F9d_gi0bYAAODFL.jpg, https://pbs.twimg.com/media/F9d_gi0bkAA0IC7.jpg, https://pbs.twimg.com/media/F9d_gizbkAEyJiz.jpg, https://pbs.twimg.com/media/F9d_gi2bgAAymqu.jpg  
  (Mentions TPUSA campus event at Dream City Christian School.)

- **Post [post:14]**  
  ID: 1717975185016467617  
  Author: @thestephstevens  
  Timestamp: Fri, 27 Oct 2023 18:42:57 GMT  
  Content: Another #LiveFree Tour Stop in the books! @tpusa_buffalo hosted @RealCandaceO this week and it was a phenomenal event! A packed room with 850+ students and community members 🤩🇺🇸 @TPUSA @tpusastudents @TpusaGreatLakes  
  Engagement: Likes=12, Reposts=3, Quotes=0, Replies=2, Bookmarks=2, Views=386  
  Media: Yes (3 items) – photos URLs: https://pbs.twimg.com/media/F9d5UyfX0AEniY9.jpg, https://pbs.twimg.com/media/F9d5UyaXcAAGdF7.jpg, https://pbs.twimg.com/media/F9d5UyaXQAAU8vh.jpg  
  (Mentions TPUSA #LiveFree Tour stop with Candace Owens in Buffalo.)

- **Post [post:15]**  
  ID: 1717969786825523209  
  Author: @3dom4domfreedom  
  Timestamp: Fri, 27 Oct 2023 18:21:30 GMT  
  Content: If we play the "knock-out game" with people who rip down "missing" posters, it will be the first time the game was played righteously.  
  Engagement: Likes=39, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=1588  
  (No direct event; included per search.)

- **Post [post:16]**  
  ID: 1717947107175170279  
  Author: @JakePoling  
  Timestamp: Fri, 27 Oct 2023 16:51:22 GMT  
  Content: Here in Ohio Students are buying into LOVING America Because of the work @TPUSA is doing! Centerville held a great event recently to promote AmericaFest! 🇺🇸  
  Engagement: Likes=7, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=487  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9dfyaZW0AAHxlS.jpg  
  (Mentions TPUSA event in Centerville, Ohio, promoting AmericaFest.)

- **Post [post:17]**  
  ID: 1717931747873055182  
  Author: @Amanda_Patriot1  
  Timestamp: Fri, 27 Oct 2023 15:50:20 GMT  
  Content: Turning Point USA at Christian Collegiate Academy made Halloween Goodie bags to be passed out to every single High Schooler on campus!! Talk about an impact, epic job guys! 🫡 @TPUSA @tpusastudents @charliekirk11 #socialismscares  
  Engagement: Likes=6, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=242  
  Media: Yes (3 items) – photos URLs: https://pbs.twimg.com/media/F9dR0WcXQAAw5aQ.jpg, https://pbs.twimg.com/media/F9dR0WfXwAAxL5u.jpg, https://pbs.twimg.com/media/F9dR0WfXoAAEDx3.jpg  
  (Mentions TPUSA campus activity at Christian Collegiate Academy.)

### Semantic Search Results (posts relevant to Charlie Kirk or TPUSA public speaking events/appearances/tours in the date range):

- **Post [post:18]**  
  ID: 1717697290037788703  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Fri, 27 Oct 2023 00:18:41 GMT  
  Content: 🚨 THOUGHTCRIME IS LIVE 🚨 -The UFC/Bud Light Deal: Based or cringe? -Are college sports being ruined by too much money? -Why countries that are richer than ever having fewer kids than ever? -No, really, what the heck is an "Ebony Alert"? Tune in now on Rumble ⬇️  
  Engagement: Likes=226, Reposts=48, Quotes=2, Replies=64, Bookmarks=0, Views=109252  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9Z8esYbEAActia.jpg  
  (Charlie Kirk live show; no in-person event specified.)

- **Post [post:19]**  
  ID: 1716921899144331374  
  Author: @hsjphil01  
  Timestamp: Tue, 24 Oct 2023 20:57:34 GMT  
  Content: DeSantis on Deck- October 24-29, 2023 Today •DeSantis will campaign in New Hampshire with Governor Chris Sununu. He will have multiple media availabilities throughout the day that we will flag. •DeSantis joined Governor Sununu for a joint in-studio interview with Jack Heath at 10am ET. Wednesday •DeSantis will speak with Iowa media. •DeSantis will appear on Jesse Watters Primetime on Fox News in the 8pm ET hour. Thursday •DeSantis will appear on The Source with Kaitlan Collins on CNN in the 9pm ET hour. Friday •DeSantis will join Fox & Friends on Fox News in the 8am ET hour. Saturday •DeSantis will speak at the Republican Jewish Coalition’s Leadership Summit in Las Vegas, NV. •DeSantis will join Life, Liberty, and Levin on Fox News in the 8pm ET hour.  
  Engagement: Likes=185, Reposts=45, Quotes=5, Replies=11, Bookmarks=1, Views=5794  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9O7XY-a8AEBXTV.jpg  
  (Lists DeSantis schedule; no direct Charlie Kirk/TPUSA mention but returned in semantic results.)

- **Post [post:20]**  
  ID: 1716506405132468378  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Mon, 23 Oct 2023 17:26:32 GMT  
  Content: We're going live with @GadSaad in about 5 min. Really looking forward to this https://rumble.com/v3r6wjz-why-the-youth-hate-israel-suicide-of-the-west-us-police-statekash-saad-dsou.html  
  Engagement: Likes=232, Reposts=30, Quotes=1, Replies=24, Bookmarks=4, Views=108835  
  (Charlie Kirk live show/podcast.)

- **Post [post:21]**  
  ID: 1717903979210826177  
  Author: @testament  
  Timestamp: Fri, 27 Oct 2023 14:00:00 GMT  
  Content: Just a reminder that starting today our own #ChuckBilly will be a guest at the 20th anniversary of @SpookyEmpire in Orlando Florida; October 27th - 29th! Check out https://t.co/T5rSiqDiZU for all the details! 🤘  
  Engagement: Likes=199, Reposts=14, Quotes=0, Replies=5, Bookmarks=1, Views=6882  
  Media: Yes (1 item) – photo URL: https://pbs.twimg.com/media/F9Y4aHtWUAAMI5S.jpg  
  (No TPUSA/Charlie Kirk connection; semantic match on “events.”)

- **Post [post:22]**  
  ID: 1717580073434255522  
  Author: @RSBNetwork  
  Timestamp: Thu, 26 Oct 2023 16:32:55 GMT  
  Content: GET READY for a big Trump weekend 🚨 ➡️ 10/28: President Trump headlines the Republican Jewish Coalition Summit in Las Vegas at 3 pm ET https://www.rsbnetwork.com/featured/live-trump-headlines-republican-jewish-coalition-summit-in-las-vegas-nevada-10-28-23/ ➡️ 10/28: Trump holds Nevada Commit to Caucus event in Las Vegas at 9 pm ET https://www.rsbnetwork.com/video/live-president-trump-holds-nevada-commit-to-caucus-event-in-las-vegas-10-28-23/ ➡️ 10/29: Trump to deliver remarks in Sioux City, Iowa, at 4 pm ET  
  Engagement: Likes=1041, Reposts=477, Quotes=29, Replies=102, Bookmarks=12, Views=98552  
  (Trump events; no direct TPUSA/Charlie Kirk.)

- **Post [post:23]**  
  ID: 1717041883019641098  
  Author: @JohnCleese  
  Timestamp: Wed, 25 Oct 2023 04:54:20 GMT  
  Content: Get SILLY in PHILLY on WEDNESDAY October 25th! 🧀 I’ll be performing in Philadelphia at the @KimmelCC at 7:30pm. Get tickets now on https://t.co/h7dqdTUD1u! #philadelphia #philly #cheese  
  Engagement: Likes=373, Reposts=35, Quotes=2, Replies=33, Bookmarks=2, Views=79447  
  Media: Yes (1 item) – video URL (embedded).  
  (No TPUSA/Charlie Kirk connection.)

- **Post [post:24]**  
  ID: 1716911161336078394  
  Author: @TerriClarkMusic  
  Timestamp: Tue, 24 Oct 2023 20:14:54 GMT  
  Content: The Homecoming Tour ‘23 with @paulbrandt starts next week! So much to do… like packing all of our Canadian jerseys! We kick it all off in Yorkton. Anyone have a Yorkton jersey we can borrow?!?!? Dates + Tickets: https://www.terriclark.com/tour/  
  Engagement: Likes=323, Reposts=41, Quotes=5, Replies=30, Bookmarks=4, Views=18545  
  Media: Yes (1 item) – video URL (embedded).  
  (No TPUSA/Charlie Kirk connection.)

**No additional posts matching the criteria were returned in the tool results. All available data from the searches is listed above verbatim.**
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-10-22 to 2023-10-28**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-10-22 to 2023-10-28 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
