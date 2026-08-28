---
unlisted: true
title: "Week 13 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W13"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-03-26 to 2025-04-01."
status: completed
hide_table_of_contents: true
---

# Week 13, 2025

- Date range: 2025-03-26 to 2025-04-01
- Queried at (UTC): 2026-08-24T19:17:46Z
- Model: grok-4.3
- API status: completed
- Response id: 17f6d5dd-9859-97cc-aae3-a253af147c40

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-03-26 to the end of the week 2025-04-01.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (speaking OR speaks OR \"public speaking\" OR event OR tour OR campus OR \"will be\" OR appearing OR appearance OR speak) since:2025-03-26 until:2025-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (event OR tour OR campus OR speaking) since:2025-03-26 until:2025-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus visits, or appearances where he will speak between March 26 and April 1 2025",
      "limit": "10",
      "from_date": "2025-03-26",
      "to_date": "2025-04-02"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point\") (Purdue OR \"April 10\" OR \"April 10th\") since:2025-03-26 until:2025-04-02",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR appearance) (Purdue OR campus) since:2025-03-26 until:2025-04-02",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (Riley Gaines OR \"Riley_Gaines_\") (event OR speaking) since:2025-03-26 until:2025-04-02",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR tour OR speaking OR speak OR campus OR Purdue) since:2025-03-26 until:2025-04-02",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 23526,
  "input_tokens_details": {
    "cached_tokens": 11968
  },
  "output_tokens": 2754,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 26280,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 587261000,
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
    "input_tokens": 12960,
    "output_tokens": 2313
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906850168990781544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906850168990781544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906848519324848528",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906848519324848528"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906846324840091673",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906846324840091673"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1904966689512452448",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1904966689512452448"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905443090170577210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905443090170577210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906857258438258938",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906857258438258938"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906849214312636500",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906849214312636500"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906854816954875952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906854816954875952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906858829092180476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906858829092180476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906774225832263683",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906774225832263683"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905360868944081047",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905360868944081047"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905237193485934757",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905237193485934757"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906783431348130229",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906783431348130229"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906780385071223145",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906780385071223145"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906759779621503152",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906759779621503152"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905368613705703928",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905368613705703928"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906737349268025584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906737349268025584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906848020303614389",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906848020303614389"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906852739101196603",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906852739101196603"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906834507438649709",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906834507438649709"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905316338245271706",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905316338245271706"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905308184144642415",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905308184144642415"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906853694039028022",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906853694039028022"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906738219439321181",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906738219439321181"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906855518993518692",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906855518993518692"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906820840517480456",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906820840517480456"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905350329626992837",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905350329626992837"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905356185102156183",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905356185102156183"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906719401534951629",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906719401534951629"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906858596270321775",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906858596270321775"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906823999390364050",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906823999390364050"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1904981443719422161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1904981443719422161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905651054576107859",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905651054576107859"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906756747722993982",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906756747722993982"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906853298503553414",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906853298503553414"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906145401607954549",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906145401607954549"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905640003557851202",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905640003557851202"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1905020502621769900",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1905020502621769900"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906857830885319010",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906857830885319010"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906771509839868039",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906771509839868039"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1906059050241941617",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1906059050241941617"
  }
]
```

## Grok response

```text
**Here is all the raw data from X/Twitter posts matching your query criteria (posts between 2025-03-26 and 2025-04-01, inclusive of the date range, focused on public speaking events, campus appearances, or locations where Charlie Kirk or TPUSA would speak).** I performed multiple keyword and semantic searches using exact date filters (`since:2025-03-26 until:2025-04-02` where needed) and included every relevant post without summarization. No posts directly announced new Charlie Kirk speaking events strictly within March 26–April 1, 2025; the results primarily reference upcoming or recent events, past activities, or unrelated discussions. All matching posts are listed below with full content, metadata, and context.

### Relevant Posts Referencing Charlie Kirk or TPUSA Speaking Events/Appearances:
- **[post:19]** (Purdue Exponent @purdueexponent, Thu, 27 Mar 2025 20:04:52 GMT)  
  Content: "Conservative commentator and online personality Charlie Kirk is set to speak at Purdue on April 10. The founder of Turning Point USA has railed against abortion, gay marriage and DEI, among other issues.  
  https://www.purdueexponent.org/campus/events/charlie-kirk-purdue-tpusa/article_01333c9e-b76e-49a6-bee2-e045b3ba27ea.html"  
  Engagement: Likes=234, Reposts=24, Quotes=7, Replies=33, Bookmarks=19, Views=33625  
  (Direct announcement of Charlie Kirk speaking at Purdue University on April 10, 2025.)

- **[post:32]** (Same as post:19 above – duplicate from additional search.)

- **[post:23]** (Mason Cottrell @maseface32, Thu, 27 Mar 2025 20:28:08 GMT)  
  Content: "🚨THIS WEEK @ UNIVERSITY OF OKLAHOMA🚨  
  OU leftists vandalize banners ahead of TPUSA’s event w/ @Riley_Gaines_   
  TPUSA at OU will host Riley Gaines on Wed, April 3rd - 6:30PM  
  The fun is just getting started! Join us for this lifechanging event  
  Tix in bio  
  @tpusastudents @TPUSA"  
  (Includes media: video + 2 photos)  
  Engagement: Likes=397, Reposts=113, Quotes=19, Replies=57, Bookmarks=9, Views=134868  
  (TPUSA event at University of Oklahoma featuring Riley Gaines on April 3, 2025 – related to TPUSA campus speaking.)

- **[post:39]** (Same as post:23 above – duplicate from additional search.)

- **[post:13]** (TPUSA AT FIU @TPUSA_FIU, Mon, 31 Mar 2025 23:18:09 GMT)  
  Content: "We excited to host Valentina at our Event on April 15 ‼️DALE🔥  
  @ValentinaForUSA"  
  (Quotes a post by Valentina Gomez about speaking at FIU on April 15.)  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=51  
  (TPUSA campus event at FIU on April 15, 2025.)

- **[post:6]** (Conservative Dude @DeeConservedude, Mon, 31 Mar 2025 23:38:42 GMT)  
  Content: "Thank you @ScottPresler for being here in Milwaukee. Thank you @TPUSA for bringing this together. This was fun. Sorry I couldn't canvas with you. Hopefully 2026 will be "all gas, no brakes" campaign. Until next time Scott. Also thank you for spending a minute chatting with my mom"  
  (Includes 4 photos)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=5  
  (References a past TPUSA event in Milwaukee with Scott Presler.)

- **[post:11]** (Shawn Nelson @Shawn4Boston, Mon, 31 Mar 2025 23:24:42 GMT)  
  Content: "what would it take to get a @TPUSA event in #Massachusetts!? @charliekirk11"  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=88  
  (Request for a future TPUSA event in Massachusetts.)

### Posts Referencing Charlie Kirk's General Speaking/Campus Activities (Historical or Contextual):
- **[post:0]** and **[post:9]** (DodgyWal @DodgyWal, Mon, 31 Mar 2025 23:59:07 GMT)  
  Content: "Having watched from Australia well before the last election, I honestly believe @charliekirk11 was solely responsible for converting the majority of uni students around to country to conservatives with his campus sessions. The guy knows his stuff."  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=14

- **[post:3]** and **[post:10]** (Jordan @jordansavon, Mon, 31 Mar 2025 23:52:52 GMT)  
  Content: "I loved every moment that I had speaking with TPUSA members on campus, they gave me a new perspective on a few political points.   
  I think I have made a life long friend, and this friend is the reason I'm returning to church."  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=17

- **[post:15]** (FedUp @Bills613S, Mon, 31 Mar 2025 23:16:10 GMT)  
  Content: "It’s been proven that the woke Democrats always bring them.  They were caught standing outside Turning Point USA event dressed as Nazis."  
  (Includes 1 photo)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=17  
  (Mentions a past TPUSA event.)

- **[post:33]** (Real America's Voice (RAV) @RealAmVoice, Thu, 27 Mar 2025 17:49:48 GMT)  
  Content: "TPUSA MEMBER ATTACKED BY TRANS STUDENT  
  @TPUSAStudents Chapter President, Paige Neumann was assaulted on campus and is speaking out, "we are not scared." @CharlieKirk11 @TPUSA"  
  (Includes 1 video)  
  Engagement: Likes=2164, Reposts=737, Quotes=12, Replies=59, Bookmarks=52, Views=25654  
  (References a recent TPUSA campus incident.)

- **[post:34]** (DeniseRoars #IAmCharlieKirk @DeniseRoars, Wed, 26 Mar 2025 22:14:16 GMT)  
  Content: "Turns out it's an XY person, aka trans woman who just got arrested for attacking XX females at a @TPUSA event on campus!"  
  (Includes 1 video)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=68

### Other Posts in the Date Range (Mentioning Charlie Kirk/TPUSA but Not Specific Upcoming Events in the Window):
- **[post:5]** (Speckled Alabaster @SpeckledAlabas1, Mon, 31 Mar 2025 23:43:10 GMT)  
  Content: "This was intertesting. @charliekirk11 you like to let other voices speak.. have you ever had an interaction with these two?"  
  (Quotes a post by Montana Tucker; includes 1 video)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=38

- **[post:17]** (I_know_your_Passwords 🛡️🦅🔫 🇺🇸 @SunSunshine4u, Mon, 31 Mar 2025 21:40:43 GMT)  
  Content: "@realDonaldTrump @JDVance @SpeakerJohnson @charliekirk11 @benshapiro @marklevinshow @RepMTG  https://t.co/7n5avkhMW3  
  'This event was a resounding success and served as a powerful reminder of how the OBiden administration’s open-border policies were strategically designed to expand their voter base in the United States.'"  
  (Quotes a post by @america; includes 1 video)  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=10

- **[post:27]** (MAGA Posts @MAGAPosts, Sun, 30 Mar 2025 00:44:12 GMT)  
  Content: "🚨 Charlie Kirk chats with a college student who wants to get rid of all borders 🤣"  
  (Includes 1 video)  
  Engagement: Likes=1609, Reposts=242, Quotes=14, Replies=217, Bookmarks=98, Views=242064  
  (Video of Charlie Kirk speaking at a campus event.)

- **[post:35]** (ape attack survivor @pissvortex, Wed, 26 Mar 2025 18:40:26 GMT)  
  Content: "I believe he is trying to use the publicity from this to become a touring conservative campus speaker like Charlie Kirk (if it wasn’t obvious from naming the event “Triggered”) w/ ties to “Moms for Liberty.” As far as I can tell, this has been the only stop on his “national tour”"  
  Engagement: Likes=49, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=1447

All other posts from the searches (e.g., [post:1], [post:2], [post:4], [post:7], [post:8], [post:12], [post:14], [post:16], [post:18], [post:20]–[post:22], [post:24]–[post:26], [post:28], [post:29]–[post:31], [post:36]–[post:38], [post:40]–[post:45]) were unrelated to specific speaking events/locations for Charlie Kirk or TPUSA in the requested date range and were excluded from this compilation. No additional relevant posts were found in the targeted searches for Purdue, Riley Gaines/OU, or general event keywords within the exact week.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-03-26 to 2025-04-01**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2025-03-26 to 2025-04-01 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
