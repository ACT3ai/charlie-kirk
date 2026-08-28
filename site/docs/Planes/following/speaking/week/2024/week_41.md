---
unlisted: true
title: "Week 41 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W41"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-10-07 to 2024-10-13."
status: completed
hide_table_of_contents: true
---

# Week 41, 2024

- Date range: 2024-10-07 to 2024-10-13
- Queried at (UTC): 2026-08-24T19:15:16Z
- Model: grok-4.3
- API status: completed
- Response id: a39e8d65-f02b-9bf9-bba4-d0c661f6d3ed

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-10-07 to the end of the week 2024-10-13.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR tour OR campus OR \"public speaking\" OR appearance OR \"will be\" OR visiting OR visit) since:2024-10-07 until:2024-10-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR tour OR campus OR \"public speaking\" OR appearance OR \"will be\" OR visiting OR visit) since:2024-10-07 until:2024-10-14 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speak OR speaking) (October OR Oct) since:2024-10-07 until:2024-10-14",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus visits, or appearances where he will speak, between October 7 and October 13 2024",
      "limit": "10",
      "from_date": "2024-10-07",
      "to_date": "2024-10-14"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA OR @tpusastudents) (tour OR \"brainwashed\" OR \"you’re being brainwashed\" OR event OR speak OR speaking OR campus OR ASU OR \"Arizona State\" OR \"U of A\" OR \"University of Arizona\" OR NAU OR \"Northern Arizona\" OR \"Oregon State\") since:2024-10-07 until:2024-10-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR tour OR speak OR ASU OR Arizona OR Tucson OR Tempe) since:2024-10-07 until:2024-10-14",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:tpusastudents (tour OR event OR Charlie OR Kirk) since:2024-10-07 until:2024-10-14",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk's You're Being Brainwashed Tour or TPUSA events in October 2024 including specific dates and locations like Oregon State, NAU, U of A, ASU",
      "limit": "10",
      "from_date": "2024-10-07",
      "to_date": "2024-10-14"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 28883,
  "input_tokens_details": {
    "cached_tokens": 13504
  },
  "output_tokens": 2726,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 31609,
  "num_sources_used": 0,
  "num_server_side_tools_used": 8,
  "cost_in_usd_ticks": 687395500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 8,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 16835,
    "output_tokens": 2168
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1843087001303822474",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1843087001303822474"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844590814451626440",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844590814451626440"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844824676998037877",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844824676998037877"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845122612118290791",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845122612118290791"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1843746663971860530",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1843746663971860530"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844228148621357437",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844228148621357437"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844497167656063425",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844497167656063425"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845248493385928746",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845248493385928746"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844910618895319329",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844910618895319329"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844740546977206463",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844740546977206463"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845241877341274236",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845241877341274236"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845219615917605374",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845219615917605374"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845116423921614908",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845116423921614908"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844787085653524906",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844787085653524906"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844438706054365627",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844438706054365627"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845220923017920746",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845220923017920746"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845245677816672527",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845245677816672527"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845040958188269711",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845040958188269711"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844182748971557099",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844182748971557099"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845215466081415184",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845215466081415184"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1843728033578135622",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1843728033578135622"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845248984002056626",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845248984002056626"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845221716945141814",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845221716945141814"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1843718055324725331",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1843718055324725331"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844222377049325731",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844222377049325731"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845234295901913222",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845234295901913222"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844105524297756908",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844105524297756908"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844582352393289819",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844582352393289819"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844102475089101027",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844102475089101027"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845243920047112368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845243920047112368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844409925381824770",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844409925381824770"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1844077068885336306",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1844077068885336306"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845225671670288527",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845225671670288527"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1843335608598704498",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1843335608598704498"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1845114454603956544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1845114454603956544"
  }
]
```

## Grok response

```text
**Here is every relevant X post from the search results (October 7–13, 2024 date range) mentioning Charlie Kirk or TPUSA/TPUSA Students events, speaking appearances, tours, or campus visits. No summarization—full post content, metadata, and context preserved exactly as returned.**

### Key posts directly announcing or discussing Charlie Kirk / TPUSA events in the specified week:

- **[post:19]** (and duplicate **[post:40]**)  
  **Author:** TPUSA Students (@tpusastudents)  
  **Timestamp:** Tue, 08 Oct 2024 18:20:13 GMT  
  **Content:**  
  New Stops Added to the YOU’RE BEING BRAINWASHED TOUR… 👀📺🧠  

  10/11: Oregon State University   
  10/15: Northern Arizona University   
  10/16: University of Arizona  
  10/17: Arizona State University   

  Don’t miss the opportunity to see Charlie Kirk on your campus! Visit https://t.co/6au2GYxRvx & get your free ticket today 🎟️  

  (Media: Video + photo of tour graphic)

- **[post:20]** (and duplicate **[post:41]**)  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 10 Oct 2024 18:03:50 GMT  
  **Content:**  
  🚨 ATTENTION TUCSON, AZ 🚨  

  NEXT WEDNESDAY, October 16th, Join @TulsiGabbard and I at the Student Union on campus at U of A.  

  EVENT DETAILS 👇  

  Doors open at 5:30 pm MST  
  Event starts: 6:30 pm MST  

  TICKETS: https://t.co/0Epu3NOpO0  

  (Media: Photo)

- **[post:21]** (and duplicate **[post:42]**)  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Tue, 08 Oct 2024 20:13:54 GMT  
  **Content:**  
  🚨 ATTENTION TEMPE, AZ 🚨  

  THURSDAY, October 17th, Join @DonaldJTrumpJr and I at the Omni Tempe Hotel at ASU.  

  DETAILS👇  

  Doors open at 5:30 pm MST  
  Remarks at 6:30 pm MST  

  TICKETS: https://t.co/1KvUvSJRhu  

  (Media: Photo)

- **[post:46]**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Fri, 11 Oct 2024 19:37:32 GMT  
  **Content:**  
  HUGE turnout at Oregon State University today. Gen Z is awake!!  

  It may be a blue state, but it has a lot of red students… 👀  

  This is how we win!!  

  🇺🇸🇺🇸🇺🇸  

  (Media: 3 items – photo + video + photo)

### Other posts in the date range referencing events (past or future, including indirect mentions):

- **[post:11]**  
  **Author:** C.K. Bouferrache aka Honeybadgermom (@Honeybadgermom)  
  **Timestamp:** Sat, 12 Oct 2024 15:21:26 GMT  
  **Content:**  
  This young man asking questions showed up early (to the Charlie Kirk tour) to be the first in line. I talked to him after watching him consulting his notes for 20 minutes and asked him his story. He was very sincere, but outmatched.  

  (Media: Video of Q&A)

- **[post:12]**  
  **Author:** Conservative_Josh231 (@Rightwing_Josh)  
  **Timestamp:** Sat, 12 Oct 2024 14:49:01 GMT  
  **Content:**  
  I'm already having drawbacks to two days ago because that's how much I loved the speaker event that my TPUSA Chapter hosted yesterday! Hosting @Riley_Gaines_ on Real Women's Day was definitely an unforgettable experience, and getting her to sign my Title IX Certificate from @LeadershipInst was a huge highlight of my night as well!  

  I'm also thankful that she got to meet my District Attorney (who calls himself the polar opposite of George Gascón, lol) and that he had the time to come to my speaker event after inviting him! And for the first time, my elected official asked for a picture with me rather than the other way around, which definitely made my night even better!  

  Now for a little promo, if you want to learn more about the progress of Title IX and how you can help women reclaim that for women's sports, go to https://t.co/l2wNQN87Fv and take the Title IX course on the @RileyGCenter website for free! It's a lot of fun to take and you can learn a lot from it as well, so make sure to sign up for the free course online today! Other than that, good luck on the rest of your Title IX Tour @Riley_Gaines_, and enjoy your almost 2 week break!  

  (Media: 3 photos)

- **[post:15]**  
  **Author:** KLZ 560, Conservative Talk (@klz_radio)  
  **Timestamp:** Fri, 11 Oct 2024 14:03:14 GMT  
  **Content:**  
  October 18th at 7 p.m. is Freedom Night in America with Charlie Kirk at Charis Bible College in Woodland Park, Colorado. This is your chance to rise up and take action. For more information on the event: https://truthandliberty.ticketspice.com/freedom-night-in-america-with-charlie-kirk?utm_medium=email&_hsenc=p2ANqtz-_vL-0ro9oyLn4bt7te3eqfoLxMX_es4ZtPRhAlfXEoQiWoh0LYKs20oH6dzOnM9jLOXOWOxLLMJvMzEMulTsjfF_gj5EqzRJqYnhDpnrz3WgoMAa4&_hsmi=328401717&utm_content=328401717&utm_source=hs_email  

  (No media)

- **[post:16]**  
  **Author:** John Norcross 🌹 (@jnorcr)  
  **Timestamp:** Fri, 11 Oct 2024 04:08:15 GMT  
  **Content:**  
  This is who #Arrowhead's #TPUSA high school "club" has invited to speak to students on October 15th in #HartlandWI.   
  No other club at this school has invited a speaker who said "R*pe is hilarious".   
  The GOP-backed school board stands behind this club.  

  (Media: 3 photos)

- **[post:17]**  
  **Author:** Dan Dow (@dandow)  
  **Timestamp:** Fri, 11 Oct 2024 03:34:38 GMT  
  **Content:**  
  I am so thankful for @Riley_Gaines_ being a strong leader and role model for young women across our great country. Thank you to @TPUSA chapter at @CalPoly for bringing Riley to speak to our community today on XX (October 10) Real Women’s Day. #StandWithWomen  
  #objectivetruth  

  (Media: Video)

- **[post:5]** (and duplicate **[post:10]**)  
  **Author:** conserv58 (@conserv58)  
  **Timestamp:** Sat, 12 Oct 2024 21:52:05 GMT  
  **Content:**  
  🚨DONALD J. TRUMP IN GEORGIA - OCTOBER 23, 2024 🚨  

  At the Gas South Arena, 6400 Sugarloaf Parkway, Duluth, Georgia   

  Charlie Kirk says this will be MOATR - The Mother of All Trump Rallies!  

  Donald Trump says "I will be leading the JUSTICE LEAGUE OF AMERICA at this Trump Rally in Georgia. Don't you dare miss it!"  

  🇺🇸 @realDonaldTrump   
  🇺🇸 @CharlieKirk11   
  🇺🇸 @TuckerCarlson   
  🇺🇸 #RealBenCarson   
  🇺🇸 @RobertKennedyJr   
  🇺🇸 @Jason_Aldean   
  🇺🇸 @TulsiGabbard   

  Sponsored by Turning Point PAC:  

  (Media: Photo)

- **[post:14]**  
  **Author:** D (@DuderonoME)  
  **Timestamp:** Sat, 12 Oct 2024 01:19:02 GMT  
  **Content:**  
  Any people here going to the Georgia October 23rd event with TPUSA and Trump?  

  (No media)

- **[post:26]**  
  **Author:** Lauren Toncich🇺🇸 (@TPA_LT)  
  **Timestamp:** Fri, 11 Oct 2024 17:08:10 GMT  
  **Content:**  
  Thrilled to host @realDonaldTrump for a FIFTH time this year, October 23rd at Gas South Arena in Duluth, GA- back again in a arena along with this incredible lineup, and we are only getting started.  

  This is just one of the most recent events added onto the ambitious @tpaction agenda in the most critical month of our lives. From multiple rallies each week across the country, hundreds of super chase events, and thousands of full time staff and volunteers chasing hundreds of thousands low propensity ballots in key battle ground states- I can confidently say there is NO ONE doing more than the Turning Point team.  

  Less than one month left- lets win 🇺🇸  

  (Media: Photo)

- **[post:18]** (and duplicate **[post:34]**) – Already listed above as the Tucson event post.

All other results in the tool output were unrelated (e.g., past ASU incidents from 2023, Trump rally discussions without Charlie Kirk/TPUSA focus, or non-event content). No additional posts matched the exact date range and topic criteria beyond those listed.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-10-07 to 2024-10-13**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-10-12](/Planes/Incidents/N582MM-2024-10-12-KEUG) | [N582MM](/Planes/N582MM/overview) | [KEUG](/Planes/Airports/KEUG) | Eugene, OR | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
