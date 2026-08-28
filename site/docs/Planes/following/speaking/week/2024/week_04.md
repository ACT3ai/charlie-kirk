---
unlisted: true
title: "Week 04 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W04"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-01-22 to 2024-01-28."
status: completed
hide_table_of_contents: true
---

# Week 04, 2024

- Date range: 2024-01-22 to 2024-01-28
- Queried at (UTC): 2026-08-24T19:11:03Z
- Model: grok-4.3
- API status: completed
- Response id: fc4345ca-ac5b-9434-869c-8998c66464d1

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-01-22 to the end of the week 2024-01-28.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR \"public speaking\" OR tour OR appearance OR \"will be\" OR speaking OR \"on stage\" OR campus OR university) since:2024-01-22 until:2024-01-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR speaking) (2024 OR January) since:2024-01-22 until:2024-01-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak in late January 2024",
      "limit": "10",
      "from_date": "2024-01-22",
      "to_date": "2024-01-28",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 7583,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 3192,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 10775,
  "num_sources_used": 0,
  "num_server_side_tools_used": 3,
  "cost_in_usd_ticks": 292331500,
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
    "input_tokens": 5993,
    "output_tokens": 2995
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751387205191270735",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751387205191270735"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750905869838279059",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750905869838279059"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751372149133344938",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751372149133344938"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1749969311526179085",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1749969311526179085"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751312658563821812",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751312658563821812"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751346594010509351",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751346594010509351"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750423566502498556",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750423566502498556"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751311296883020226",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751311296883020226"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751330037670777049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751330037670777049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751382323776340003",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751382323776340003"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750153914974888016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750153914974888016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751349316273270864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751349316273270864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750345004017504430",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750345004017504430"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750687200701002046",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750687200701002046"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1751297937991184452",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1751297937991184452"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1750283597167153477",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1750283597167153477"
  }
]
```

## Grok response

```text
**Here is every relevant post** from the X (Twitter) search results for the exact date range **2024-01-22 to 2024-01-28** (posts dated up to 2024-01-28, with the search extending to 2024-01-29 per the query operators) mentioning Charlie Kirk, TPUSA, or Turning Point USA in connection with public speaking events, appearances, tours, campus events, or where Charlie will speak. I used the exact keyword and semantic searches requested and included **all matching data without summarization**.

### Posts from keyword search (mode: Latest):

- **Post ID: 1751387205191270735**  
  **Author:** Sue Nutt (@SueNutt2)  
  **Timestamp:** Sat, 27 Jan 2024 23:30:23 GMT  
  **Content:** Charlie Kirk speaking to a guy that said whites should pay reparations!  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16  
  **Media:** None

- **Post ID: 1751382323776340003**  
  **Author:** We Are Charlie Kirk R.I.P ☦️🙏 (@RogerR54116409)  
  **Timestamp:** Sat, 27 Jan 2024 23:10:59 GMT  
  **Content:** Biased court with direct ties to white house and its administration. The ruling will be overturned and EJC will held liable to DJT’s legal fees just as his last accuser.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=11  
  **Media:** None  
  *(Note: This post is in a conversation thread referencing a Charlie Kirk quote but does not mention events.)*

- **Post ID: 1751349316273270864**  
  **Author:** I AM CHARLIE KIRK (@jallinen2003)  
  **Timestamp:** Sat, 27 Jan 2024 20:59:50 GMT  
  **Content:** @newscentermaine https://t.co/a9INLIb4M6 this is blatent election interference and a violation of maine's residents rights all votes count no matter for who my civil rights office will be filing a lawsuit against this for your state openly violating citizens rights to have a vote  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=8  
  **Media:** None

- **Post ID: 1751346594010509351**  
  **Author:** House of Life University (@mcwright349026)  
  **Timestamp:** Sat, 27 Jan 2024 20:49:01 GMT  
  **Content:** Now you know Candace Owens and Charlie Kirk on NWO puppets with their latest stupid rant on aboriginal (black) pilots. Remember Tuskegee Airmen, greatest fighter pilots ever!  
  **Engagement:** Likes=2, Reposts=0, Quotes=1, Replies=0, Bookmarks=0, Views=262  
  **Media:** Yes (2 photos: https://pbs.twimg.com/media/GE4HxLTWgAA7c_X.jpg and https://pbs.twimg.com/media/GE4HzRFXsAADPl_.jpg)

- **Post ID: 1751330037670777049**  
  **Author:** Frederick Leathers (@FrederickLeath5)  
  **Timestamp:** Sat, 27 Jan 2024 19:43:13 GMT  
  **Content:** @SenatorLankford, if you support this, Charlie Kirk, TPUSA, will be coming down for your next election to remind people you supported Biden a invasion of the country and amnesty. I too will do what I can to remind people. You’re only doing this because you’re not up yet but wait.  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=3  
  **Media:** None  
  *(Mentions future TPUSA/Charlie Kirk election-related activity but no specific dates or events in the range.)*

- **Post ID: 1751312658563821812**  
  **Author:** Craig Silverman (@craigscolorado)  
  **Timestamp:** Sat, 27 Jan 2024 18:34:10 GMT  
  **Content:** Charlie Kirk is proud graduate of Trump University School of Law featuring Professor Alina Habba.  
  **Engagement:** Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=423  
  **Media:** None  
  *(Quotes a Charlie Kirk post about a court verdict; no event details.)*

- **Post ID: 1751311296883020226**  
  **Author:** The All-American Book Club (@allamericanbook)  
  **Timestamp:** Sat, 27 Jan 2024 18:28:45 GMT  
  **Content:** The All-America Book Club is honored to feature these authors and patriots with @TPUSA Georgetown University Chapter on Tuesday, Feb. 13. #NationalSecurity topics, with @WashTimes & emcee @ckchumley. #AFSpouseoftheYear @kristenchristy & former #WH physician Dr. Mark Richard’s.  
  **Engagement:** Likes=6, Reposts=3, Quotes=1, Replies=1, Bookmarks=1, Views=995  
  **Media:** Yes (3 photos: https://pbs.twimg.com/media/GE3oUXUXcAA74_V.jpg, https://pbs.twimg.com/media/GE3oUXXWMAAIRTL.jpg, https://pbs.twimg.com/media/GE3oUXZXYAADwFL.jpg)  
  *(Mentions TPUSA Georgetown University Chapter event on Feb 13, 2024 — outside the date range but directly references TPUSA campus activity.)*

- **Post ID: 1751297937991184452**  
  **Author:** Je Suis Charlie Kirk (@semperfidem2004)  
  **Timestamp:** Sat, 27 Jan 2024 17:35:40 GMT  
  **Content:** Truth. Am I naīve for hoping it will be different second time around?  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=104  
  **Media:** None  
  *(Quotes another post; no event mentions.)*

### Posts from semantic search (relevant to events/appearances/speaking):

- **Post ID: 1750423566502498556**  
  **Author:** #TuckFrump (@realTuckFrumper)  
  **Timestamp:** Thu, 25 Jan 2024 07:41:14 GMT  
  **Content:** Motivational Speaker Kyle Rittenhouse to Speak at Tennessee University and People Are NOT Happy About It https://www.politicalflare.com/2024/01/motivational-speaker-kyle-rittenhouse-to-speak-at-tennessee-university-and-people-are-not-happy-about-it/  
  **Engagement:** Likes=344, Reposts=69, Quotes=25, Replies=196, Bookmarks=3, Views=25801  
  **Media:** None  
  *(Mentions a different speaker; no direct Charlie Kirk/TPUSA link.)*

- **Post ID: 1750687200701002046**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Fri, 26 Jan 2024 01:08:49 GMT  
  **Content:** THOUGHTCRIME IS LIVE 🚨  
  -Is the Biden Administration's border invasion sending America into a constitutional crisis?  
  -What is a "hicklib," and why did they come so unglued over last weeks discussion of DEI for pilots?  
  -Are we going to destroy the value of antibiotics for the sake of orgies?  
  @JackPosobiec  
  **Engagement:** Likes=503, Reposts=61, Quotes=3, Replies=78, Bookmarks=9, Views=131012  
  **Media:** None  
  *(Live show/podcast, not a public speaking event.)*

- **Post ID: 1750345004017504430**  
  **Author:** Jon Herold (@patel_patriot)  
  **Timestamp:** Thu, 25 Jan 2024 02:29:03 GMT  
  **Content:** Tonight's show should be 🔥🔥🔥  
  - Trump v Haley  
  - Kari Lake situation  
  - New NSPM Devo nugget  
  - Texas border situation and what it means for Devo  
  - Regular shenanigans  
  Don't miss it!  
  10:30 PM ET  
  @BadlandsMedia_ @reBurningBright @realjusthuman  
  https://rumble.com/v48ynaw-devolution-power-hour-217-1030-pm-et-.html?mref=nmtun&mc=4m0ok  
  **Engagement:** Likes=214, Reposts=63, Quotes=4, Replies=10, Bookmarks=5, Views=32941  
  **Media:** None  
  *(Podcast show announcement.)*

- **Post ID: 1751372149133344938**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Sat, 27 Jan 2024 22:30:33 GMT  
  **Content:** President Trump in Las Vegas, Nevada:  
  “Within moments of my inauguration, we will begin the largest domestic deportation operation in American history. We have no choice.” 🔥🔥  
  **Engagement:** Likes=20339, Reposts=3263, Quotes=152, Replies=614, Bookmarks=83, Views=581389  
  **Media:** Yes (1 video: https://video.twimg.com/ext_tw_video/1751371893335326720/pu/vid/avc1/848x464/Y2iCKUoCTRqnLV61.mp4?tag=12)  
  *(Mentions Trump appearance; Charlie Kirk is quoting/posting about it.)*

- **Post ID: 1750283597167153477**  
  **Author:** CPAC (@CPAC)  
  **Timestamp:** Wed, 24 Jan 2024 22:25:02 GMT  
  **Content:** "Donald Trump is going to do it again. We are going to lock the border down, and we are going to protect Americans."  
  Confirmed CPAC in DC Speaker Tom Homan 🇺🇸  
  Hear more from him and other leaders in the conservative movement at CPAC in DC, February 21 - 24!  
  Get Your Tickets Now at  
  **Engagement:** Likes=653, Reposts=129, Quotes=2, Replies=24, Bookmarks=1, Views=9050  
  **Media:** Yes (1 video: https://video.twimg.com/ext_tw_video/1750283559309352963/pu/vid/avc1/1280x720/y8nwFGLNZyy_9WJT.mp4?tag=12)  
  *(CPAC event announcement for Feb 2024; no Charlie Kirk/TPUSA mention in the post.)*

- **Post ID: 1750905869838279059**  
  **Author:** ✞🎀TrumpGirlOnFire 🔥 (@TrumpGirlOnFire)  
  **Timestamp:** Fri, 26 Jan 2024 15:37:44 GMT  
  **Content:** President Donald J. Trump to Deliver Remarks at Commit to Caucus Rally in Las Vegas, Nevada  
  💃🕺LETS GO AMERICA 🗳️VOTE TRUMP!  
  📌Sat, January 27, 2024   
          1:00 pm (US/Pacific)  
  #TrumpGirlOnFire 🔥 #Nevadacaucuses  
  **Engagement:** Likes=192, Reposts=142, Quotes=1, Replies=14, Bookmarks=2, Views=8046  
  **Media:** Yes (1 photo: https://pbs.twimg.com/media/GEx2kUGa8AAh-hA.png)  
  *(Trump rally; no direct Charlie Kirk/TPUSA link.)*

- **Post ID: 1750153914974888016**  
  **Author:** PatriotTakes 🇺🇸 (@patriottakes)  
  **Timestamp:** Wed, 24 Jan 2024 13:49:44 GMT  
  **Content:** Charlie Kirk Instructs MAGA Audience Not to Go to the Hospital  
  Video and story— https://meidasnews.com/news/charlie-kirk-instructs-maga-audience-not-to-go-to-the-hospital  
  **Engagement:** Likes=288, Reposts=65, Quotes=18, Replies=119, Bookmarks=9, Views=73713  
  **Media:** None  
  *(Refers to a past audience address by Charlie Kirk; no future event details.)*

- **Post ID: 1749969311526179085**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Wed, 24 Jan 2024 01:36:11 GMT  
  **Content:** We are the number 1 stream in the country tonight.   
  LET'S GO 🔥🔥  
  https://rumble.com/v48v5uo-the-new-hampshire-primary-livestream.html?mref=4pvd7&mc=b2gay  
  **Engagement:** Likes=1289, Reposts=118, Quotes=7, Replies=63, Bookmarks=4, Views=131531  
  **Media:** None  
  *(Livestream announcement.)*

**No other posts** were returned by the searches in the specified date range that directly announce or detail public speaking events, tours, or appearances by Charlie Kirk or TPUSA. All data from the tool results is included above exactly as retrieved.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-01-22 to 2024-01-28**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-01-22 to 2024-01-28 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
