---
unlisted: true
title: "Week 25 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W25"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-06-18 to 2025-06-24."
status: completed
hide_table_of_contents: true
---

# Week 25, 2025

- Date range: 2025-06-18 to 2025-06-24
- Queried at (UTC): 2026-08-24T19:18:59Z
- Model: grok-4.3
- API status: completed
- Response id: 134ef4a5-70c1-95d2-a4ce-f0af5978bd36

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-06-18 to the end of the week 2025-06-24.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR \"speaking event\" OR rally) since:2025-06-18 until:2025-06-25",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR \"speaking event\" OR rally) since:2025-06-18 until:2025-06-25 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between June 18-24 2025",
      "limit": "10",
      "from_date": "2025-06-18",
      "to_date": "2025-06-25"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 10671,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 4276,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 14947,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 358031500,
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
    "input_tokens": 9081,
    "output_tokens": 4068
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937188866085277800",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937188866085277800"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937299350520013100",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937299350520013100"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937290500991541758",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937290500991541758"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937269604352455027",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937269604352455027"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937258614898516311",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937258614898516311"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937242273647067538",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937242273647067538"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937218316571148414",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937218316571148414"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1936483321393123473",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1936483321393123473"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937274456432341263",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937274456432341263"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937289792963977265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937289792963977265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1935354503584432490",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1935354503584432490"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1936488459960525138",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1936488459960525138"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1936157105083629910",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1936157105083629910"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937213199100879303",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937213199100879303"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937257579643879837",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937257579643879837"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1935804319854739497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1935804319854739497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937295565735313734",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937295565735313734"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937160510975390047",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937160510975390047"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937114586056142970",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937114586056142970"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1937042941190500805",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1937042941190500805"
  }
]
```

## Grok response

```text
**No direct announcements or posts about Charlie Kirk or TPUSA public speaking events, appearances, campus tours, rallies, or scheduled speaking engagements were found in X posts from June 18–24, 2025 (using the date range since:2025-06-18 until:2025-06-25).**

The searches (keyword-based for terms like "Charlie Kirk", TPUSA, "Turning Point USA" combined with event/speaking/speak/tour/appearance/"will be"/campus/"speaking event"/rally, plus a semantic search for relevant events/appearances/tours/speaking) returned posts in that window, but none contain specific details on upcoming or ongoing events during June 18–24, 2025. 

Here is the complete raw data from all returned posts (including full content, author, timestamp, engagement, media, and context where available). Posts are listed in the order returned by the tools, with no summarization or filtering beyond the tool results:

- **Post ID: 1937299350520013100**  
  Author: Debrich_X (@CatmomFlorida)  
  Timestamp: Mon, 23 Jun 2025 23:58:53 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=66  
  Content: Just wondering if you guys will be on Rumble tonight, I see Charlie Kirk is on RAV.

- **Post ID: 1937295565735313734**  
  Author: sherrie (@sherrie07834047)  
  Timestamp: Mon, 23 Jun 2025 23:43:50 GMT  
  Engagement: Likes=5, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=135  
  Content: These demons need an asylum so the world’s children will be safe.

- **Post ID: 1937290500991541758**  
  Author: ; 🇺🇸❤️‍🩹🤍💙🦅🐺🥀 (@B7789Quotes)  
  Timestamp: Mon, 23 Jun 2025 23:23:43 GMT  
  Engagement: Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=137  
  Content: *pedo friendly event. kids dont belong at such cult groupings

- **Post ID: 1937289792963977265**  
  Author: FRONTLINES TPUSA (@FrontlinesTPUSA)  
  Timestamp: Mon, 23 Jun 2025 23:20:54 GMT  
  Engagement: Likes=124, Reposts=39, Quotes=4, Replies=16, Bookmarks=20, Views=45797  
  Media: 1 video (URL: https://video.twimg.com/amplify_video/1937284027683340292/vid/avc1/848x464/I1fqG-Acpva7xKbt.mp4, duration: 98300 ms)  
  Content: WATCH: Members of the LGBTQ+ community tell @bodittle why they believe the DC Pride Parade, officially known as the WorldPride Parade, is considered a family-friendly event.  
  @TPUSA

- **Post ID: 1937274456432341263**  
  Author: Rob Bluey (@RobertBluey)  
  Timestamp: Mon, 23 Jun 2025 22:19:57 GMT  
  Engagement: Likes=5, Reposts=2, Quotes=0, Replies=3, Bookmarks=1, Views=632  
  Media: 1 photo (URL: https://pbs.twimg.com/media/GuKUtSMXEAAqrcR.jpg)  
  Content: ‘FASCISM IS NOT A SIDE’: JOURNALISTS STRATEGIZE TO EXPOSE THE ‘EXTREMISM’ ON THE RIGHT  
  NEW ORLEANS—When Turning Point USA founder Charlie Kirk goes to speak on campus and attracts a large following, that’s not the story—the story is how the Right conspired to open the door to his “extremism,” according to journalists presenting at an investigative reporting conference.  
  Link to full article in first reply.  
  @Tyler2ONeil @DailySignal

- **Post ID: 1937269604352455027**  
  Author: Ray Charles Istre (@Ray_Istre)  
  Timestamp: Mon, 23 Jun 2025 22:00:41 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=27  
  Content: It's will be over when they stop paying the rah rah cheerleaders like Mark Levin, Charlie Kirk, Jack Posobiec, Steve Bannon... etc. Take away their pom poms... even though they look soooo cute. @marklevinshow @charliekirk11 @JackPosobiec @Stevebannon_sk

- **Post ID: 1937258614898516311**  
  Author: Lisa 🇺🇸 We Are Charlie Kirk🇺🇸🇫🇮 (@elkay101)  
  Timestamp: Mon, 23 Jun 2025 21:17:00 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=118  
  Content: The event that most formed my opinion on #iran was when they took our embassy hostage. Hence I hate Iran and everything they stand for. As long as they chant death to America and Israel, they can go to hell. IDGAF about Iran. At all.

- **Post ID: 1937257579643879837** (thread continuation)  
  Author: Tyler O'Neil (@Tyler2ONeil)  
  Timestamp: Mon, 23 Jun 2025 21:12:54 GMT  
  Engagement: Likes=16, Reposts=3, Quotes=0, Replies=1, Bookmarks=0, Views=1712  
  Quoted Post: [Post ID 1926367734075470287 from May 24, 2025 – SPLC hate map thread on TPUSA]  
  Content: When Kirk speaks at a campus & attracts a huge crowd, that's not the story, she said. The real story is how conservatives enabled his "extremism" to get there.😲  
  She didn't cite the SPLC, but one suspects she shares its antipathy to @TPUSA.  
  🧵3/9

- **Post ID: 1937242273647067538**  
  Author: Jesús Franco (@francojesuus)  
  Timestamp: Mon, 23 Jun 2025 20:12:04 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=1, Replies=1, Bookmarks=0, Views=41  
  Media: 1 photo (URL: https://pbs.twimg.com/media/GuJ3lQUbcAA3x_l.jpg)  
  Content: Charlie Kirk is happy because there will be no more war.

- **Post ID: 1937218316571148414**  
  Author: JZ Murdock-Writer/Filmmaker (@jzmurdock)  
  Timestamp: Mon, 23 Jun 2025 18:36:53 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=1, Replies=0, Bookmarks=0, Views=40  
  Content: Right-wing grifters like Charlie Kirk tour colleges, poisoning minds while baiting the left—only to swoop in as the “savior” exposing the chaos they helped provoke.  
  Sounds like Trump.  
  Debunking the Charlie Kirk Origin Story by Matthew Boedy:

- **Post ID: 1937213199100879303**  
  Author: We are ALL Charlie Kirk! (@bobs_626)  
  Timestamp: Mon, 23 Jun 2025 18:16:33 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=7  
  Media: 1 photo (URL: https://pbs.twimg.com/media/GuJdIkhWAAAwY-p.jpg)  
  Content: Have some tea, go touch some grass and relax a bit. Come back when it's over and work on getting Massie that new Mayoral job he will be moving to! 🤣👍🇺🇸🥰

- **Post ID: 1937188866085277800**  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Mon, 23 Jun 2025 16:39:51 GMT  
  Engagement: Likes=16, Reposts=5, Quotes=0, Replies=2, Bookmarks=1, Views=635  
  Media: 1 video (URL: https://video.twimg.com/amplify_video/1937188694332751872/vid/avc1/2160x3840/Uu3nFFlIoLcPvXCD.mp4, duration: 19133 ms)  
  Content: When your mind is renewed by the Word of God, your entire life starts to shift. That’s the power of walking by faith—not by sight.  
  👊 Let your faith transform how you think, speak, and lead. (Romans 12:2)  
  ft. @AWatsonOLY

- **Post ID: 1937160510975390047**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 23 Jun 2025 14:47:11 GMT  
  Engagement: Likes=8536, Reposts=1658, Quotes=46, Replies=263, Bookmarks=281, Views=463910  
  Quoted Post: [Post ID 1936685778077168091 from Jun 22, 2025 – Danish newspaper remigration editorial]  
  Content: A large, centrist newspaper in Denmark just published this editorial about immigration: "They should not be integrated. They should go home."  
  It's in response to a recent forecast which predicts that by the end of the century, non-Danish immigrants and their descendants will be a majority of the country.  
  The editorial says "It is simply not acceptable if we end up in a situation where Danes are a minority in their own country," then declares there should be "a complete stop to immigration from the Middle East and full speed ahead in sending people from the Middle East without Danish citizenship out of Denmark."  
  The shift in America over the past few years is reverberating across the West. Replacement migration is a choice — and we can choose not to let it happen.

- **Post ID: 1937114586056142970**  
  Author: Ben Gazeer (@BGazeer)  
  Timestamp: Mon, 23 Jun 2025 11:44:41 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=88  
  Media: 1 photo (URL: https://pbs.twimg.com/media/GuIDZVlXUAArR83.jpg)  
  Content: Illegals work construction, agriculture, landscape services, hospitality and dining industries. They contribute immensely to the American economy and well-being. Creepy Charlie Kirk produces nothing of value to anyone, and his TPUSA Event Planner is in prison for baby-rape porn.

- **Post ID: 1935354503584432490**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 18 Jun 2025 15:10:45 GMT  
  Engagement: Likes=787, Reposts=82, Quotes=3, Replies=95, Bookmarks=7, Views=265850  
  Content: Whoa! Massive ticket surge yesterday after our first speaker drop for SAS 2025.  
  Get your tickets ASAP 👉 https://www.sas2025.com/  
  See you in Tampa July 11-13 🇺🇸

- **Post ID: 1935804319854739497**  
  Author: Ryan Conner (@RyanConner69)  
  Timestamp: Thu, 19 Jun 2025 20:58:10 GMT  
  Engagement: Likes=2020, Reposts=66, Quotes=0, Replies=50, Bookmarks=232, Views=256550  
  Media: 1 photo (URL: https://pbs.twimg.com/media/Gt1bxKUWIAAqCst.jpg)  
  Content: TEXAS you asked and yes I am coming!!!!   San Antonio July 24, Austin July 25, Dallas July 26-27 and Houston July 28-29.   Email only for all the details.   Email me at ryan@ryanconner.com to get all the info to cross that bucket lust item off your list …😘

- **Post ID: 1936157105083629910**  
  Author: Jordan Clark (@itsjordanclark)  
  Timestamp: Fri, 20 Jun 2025 20:20:00 GMT  
  Engagement: Likes=306, Reposts=81, Quotes=0, Replies=8, Bookmarks=30, Views=6369  
  Media: 1 video (URL: https://video.twimg.com/ext_tw_video/1936156850669408256/pu/vid/avc1/720x1280/zbd0tCJhuxEpv9fw.mp4?tag=12, duration: 58839 ms)  
  Content: Perfect timing to have a show with the KILTED CHRISTIAN! 7pm ET! This Patriot and follower of Christ is truly a blessing In this movement!  
  We're going to discuss all the rabbit holes, Q OPERATION/COMMS and of course the Israel/Iran situation!  
  ..  
  Join us in the chat on X, FB, and Rumble! Links on website below! Q&A at the end! Love y'all!🫡✝️  
  👉 https://t.co/7GRcMMHVCt 👈

- **Post ID: 1936483321393123473**  
  Author: The Offspring (@offspring)  
  Timestamp: Sat, 21 Jun 2025 17:56:16 GMT  
  Engagement: Likes=227, Reposts=26, Quotes=4, Replies=6, Bookmarks=5, Views=14511  
  Media: 1 video (URL: https://video.twimg.com/amplify_video/1936482236473192448/vid/avc1/1080x1920/1GuszdZEUttvMft4.mp4, duration: 46171 ms)  
  Content: SUPERCHARGED WORLDWIDE IN ‘25 with The Offspring, @jimmyeatworld & @newfoundglory ⚡  
  See you this summer? ☀️🤘  
  [Full tour list: Jul 11 West Palm Beach FL, Jul 12 Tampa FL, Jul 15 Alpharetta GA, Jul 16 Raleigh NC, Jul 18 Virginia Beach VA, Jul 19 Bristow VA, Jul 20 Scranton PA, Jul 22 Syracuse NY, Jul 23 Toronto ON, Jul 25 Cincinnati OH, Jul 26 Noblesville IN, Jul 27 Clarkston MI, Jul 29 Camden NJ, Jul 30 Mansfield MA, Aug 01 Bethel NY, Aug 02 Holmdel NJ, Aug 03 Wantagh NY, Aug 13 Cuyahoga Falls OH, Aug 15 Minneapolis MN, Aug 16 Tinley Park IL, Aug 17 St. Louis MO, Aug 20 Ridgedale MO, Aug 22 Dallas TX, Aug 23 The Woodlands TX, Aug 24 Austin TX, Aug 26 Albuquerque NM, Aug 27 Phoenix AZ, Aug 29 Inglewood CA, Aug 30 Mountain View CA, Aug 31 Wheatland CA, Sep 03 Auburn WA, Sep 04 Ridgefield WA, Sep 06 West Valley City UT, Sep 07 Denver CO]

- **Post ID: 1937042941190500805**  
  Author: LiSA_STAFF (@LiSA_STAFF)  
  Timestamp: Mon, 23 Jun 2025 07:00:00 GMT  
  Engagement: Likes=684, Reposts=96, Quotes=2, Replies=4, Bookmarks=6, Views=45538  
  Media: 2 items (video URL: https://video.twimg.com/amplify_video/1936985173695840256/vid/avc1/1080x1920/TcbzGmx_OcC7xzy0.mp4 duration 46800 ms; photo URL: https://pbs.twimg.com/media/GuGNygjWoAAdhS1.jpg)  
  Content: 【NEW】  
  #LiSA "ANOTHER GREAT DAY North America Headline Shows 2025” in New York, June 18&19, VLOG is now out on YouTube☆  
  ▽"ANOTHER GREAT DAY North America Headline Shows 2025" in New York  
  https://www.youtube.com/watch?v=iQgPEdkIykE&feature=youtu.be  
  ＊＊＊＊＊＊＊＊＊＊  
  LiSA – ANOTHER GREAT DAY  
  North America Headline Shows 2025  
  ▽Schedule  
  June 18: Terminal 5 - New York  
  June 19: Terminal 5 – New York   
  June 23: The Roxy Theatre– Los Angeles  
  June 24: YouTube Theater – Los Angeles　  
  June 28: Pepsi Center - Mexico City  
  ▽Ticket  
  https://t.co/Berckz7pHQ  
  #LiSA_NATOUR

- **Post ID: 1936488459960525138**  
  Author: Ndegwa Njiru Adv. (@NjiruAdv)  
  Timestamp: Sat, 21 Jun 2025 18:16:41 GMT  
  Engagement: Likes=502, Reposts=189, Quotes=3, Replies=31, Bookmarks=2, Views=13619  
  Media: 1 photo (URL: https://pbs.twimg.com/media/Gt_J_AkWYAMQczs.jpg)  
  Content: Two most important programs to note.   
  22rd June, 2025 at 3:00 PM and the venue is at All Saint Cathedral.  
  25th June, 2025 at 2:00PM and the venue is known to all as per the program.  
  The event is know to all Kenyans.  
  No retreat no surrender.

All other tool results (including additional keyword variations with links filter) returned only duplicates of the above posts. No posts reference specific Charlie Kirk/TPUSA speaking locations, dates, or events within the June 18–24, 2025 window. One post mentions a future SAS 2025 event in Tampa (July 11-13), but it falls outside the requested date range.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-06-18 to 2025-06-24**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2025-06-18 to 2025-06-24 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
