---
unlisted: true
title: "Week 20 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W20"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-05-14 to 2022-05-20."
status: completed
hide_table_of_contents: true
---

# Week 20, 2022

- Date range: 2022-05-14 to 2022-05-20
- Queried at (UTC): 2026-08-24T19:00:57Z
- Model: grok-4.3
- API status: completed
- Response id: 89664ee7-cfdb-9d73-93f1-9c1f1dc99236

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-05-14 to the end of the week 2022-05-20.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR tour OR speak OR speaking OR \"will be\" OR speaking OR campus OR rally OR \"public speaking\" OR \"speaking event\") since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR tour OR speak OR speaking OR campus OR rally) since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR tour OR speak OR speaking OR campus OR rally) since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking) (May 14 OR May 15 OR May 16 OR May 17 OR May 18 OR May 19 OR May 20) since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Turning Point\") (speak OR speaking OR event OR tour OR campus OR rally OR \"will speak\" OR \"speaking at\" OR \"speaking event\") since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, campus appearances, or where Charlie will speak in May 2022",
      "limit": "10",
      "from_date": "2022-05-14",
      "to_date": "2022-05-21"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (event OR tour OR speaking) since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (event OR tour OR speaking) since:2022-05-14 until:2022-05-21",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Arizona OR AZ) (May 22 OR \"May 22nd\" OR \"this Sunday\") since:2022-05-14 until:2022-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"2000 Mules\" (Kirk OR TPUSA OR \"Turning Point\") (Arizona OR AZ OR Scottsdale) since:2022-05-14 until:2022-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"high school\" OR \"HS\") (disrupt OR disruption) TPUSA since:2022-05-14 until:2022-05-21",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (event OR speaking) (high school OR HS OR campus) since:2022-05-14 until:2022-05-21",
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
  "input_tokens": 27799,
  "input_tokens_details": {
    "cached_tokens": 16576
  },
  "output_tokens": 3708,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 31507,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 866139500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 12,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 12585,
    "output_tokens": 3018
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1526311635945566208",
    "start_index": 264,
    "end_index": 325,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1526311635945566208",
    "start_index": 325,
    "end_index": 386,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TrumpStudents/status/1526622521109250048",
    "start_index": 858,
    "end_index": 919,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TrumpStudents/status/1526705568198451200",
    "start_index": 919,
    "end_index": 980,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/issashowgirl/status/1526639970953244672",
    "start_index": 9846,
    "end_index": 9906,
    "title": "4"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (2022-05-14 to 2022-05-20, with `until:2022-05-21` to capture the full week) mentioning Charlie Kirk, TPUSA (Turning Point USA), or related events/speaking appearances are included below without summarization.**[[1]](https://x.com/charliekirk11/status/1526311635945566208)[[1]](https://x.com/charliekirk11/status/1526311635945566208)

No other direct announcements of additional Charlie Kirk or TPUSA public speaking events, tours, or campus appearances appear in the searched posts for this exact week. The primary relevant content centers on a planned Arizona event tied to the film *2000 Mules* (noted as occurring the following Sunday, May 22, which falls just outside the range) and a reported disruption at a TPUSA high school event (location unspecified in posts but referenced as Missouri in one).[[2]](https://x.com/TrumpStudents/status/1526622521109250048)[[3]](https://x.com/TrumpStudents/status/1526705568198451200)

### Relevant Posts (Latest Mode Results, in reverse chronological order where available):

- **Post ID: 1527408784435466249** (Thu, 19 May 2022 22:00:06 GMT)  
  Author: @semperfidem2004  
  Content: "Literally" - as opposed to what? Figuratively gives money in taxes? Anyway, that means the government's stake will be worth some £s, which it can use to cut taxes or spend, which most people would prefer to owning shares in a TV station

- **Post ID: 1527390426864537603** (Thu, 19 May 2022 20:47:09 GMT)  
  Author: @legaldawn  
  Content: I could NOT believe this as Bush was a patriot; or so I thought. The black community was the first to mention that Bush was in on 9/11 and I said 'no'. Now I say yes as Bush is NOT a patriot and is in on Great Reset! He will be one of the elite who you obey if we don't stop G.R.

- **Post ID: 1527369284598394880** (Thu, 19 May 2022 19:23:09 GMT)  
  Author: @WapiroBen  
  Content: Wonder what Charlie Kirk did that was so great if there were so few women at said event.  
  (Includes video media)

- **Post ID: 1527357159637663744** (Thu, 19 May 2022 18:34:58 GMT)  
  Author: @AircondaTvT  
  Content: They say the national average will be $6 by August

- **Post ID: 1527355455701495808** (Thu, 19 May 2022 18:28:12 GMT)  
  Author: @TomEDewey1948  
  Content: Absolutely. It's nice to see other conservatives in an atmosphere where meeting people with a similar ideology is limited. Also, you go beyond College Republicans and join YAF and TPUSA if your campus has it.

- **Post ID: 1527354968277078021** (Thu, 19 May 2022 18:26:15 GMT)  
  Author: @JohnstonShow  
  Content: Turning Point USA | LGBTQ Groomer Event at Sex Shop for Kids

- **Post ID: 1527345486943768576** (Thu, 19 May 2022 17:48:35 GMT)  
  Author: @PostaDiFalcone  
  Content: Turning Point USA: The Left Continues to Sexualize and Groom Elementary School Children | Drew Hernandez Time and time again, the Left continues to sexualize children. It's so evident- they want to groom your kids. STAND UP and SPEAK OUT!!🇺🇸  
  (Includes subscription link)

- **Post ID: 1527327011185668096** (Thu, 19 May 2022 16:35:10 GMT)  
  Author: @Grama641  
  Content: Democrats are the creepy shadow ppl who mama warned you to never speak to  
  #Grooming

- **Post ID: 1527181168063430659** (Thu, 19 May 2022 06:55:38 GMT)  
  Author: @pjkate  
  Content: High School Students Disrupt TPUSA Event With Jeers, Taunts; Smash Glass Table

- **Post ID: 1527140425311604737** (Thu, 19 May 2022 04:13:44 GMT)  
  Author: @bluesky804  
  Content: But were the @TPUSA students prevented from speaking by shouting and talking over them when they tried to speak? Wasn’t the purpose of the meeting to provide students with information about @TPUSA ‘s principles and objectives? Did protestors wait for a question/answer session?

- **Post ID: 1527109676697018374** (Thu, 19 May 2022 02:11:33 GMT)  
  Author: @YorkTonga  
  Content: High School Students Disrupt TPUSA Event With Jeers, Taunts; Smash Glass Table

- **Post ID: 1527064679184404480** (Wed, 18 May 2022 23:12:45 GMT)  
  Author: @TPAction  
  Content: @DanODonnellShow hit it right on the head‼️ People are very passionate about election integrity & @DineshDSouza’s 2000 Mules proves that. Thank you again for speaking in WI!  
  Join us for our next showings👇🏼  
  Arizona 🎟: [link]  
  Georgia 🎟: [link]  
  (Includes video media)

- **Post ID: 1527050389308248068** (Wed, 18 May 2022 22:15:58 GMT)  
  Author: @LHCBMatt  
  Content: He was also one of the early IDW guys, convinced the biggest threat to God & Country was college students who didn't want to pay speaking fees to guys like Charlie Kirk or people who criticized NYT opinion writers for being irrelevant fluff.

- **Post ID: 1527033347246944256** (Wed, 18 May 2022 21:08:15 GMT)  
  Author: @Kingdavethe1st2  
  Content: Leftist students violently disrupt TPUSA high school meeting in Missouri, destroy school property  
  [link]

- **Post ID: 1526972260283727873** (Wed, 18 May 2022 17:05:31 GMT)  
  Author: @jakony_com  
  Content: High School Students Disrupt TPUSA Event With Jeers, Taunts; Smash Glass Table

- **Post ID: 1526949141338726406** (Wed, 18 May 2022 15:33:39 GMT)  
  Author: @KBittermanGross  
  Content: High School Students Disrupt TPUSA Event With Jeers, Taunts; Smash Glass Table | The Daily Wire

- **Post ID: 1526938244591538177** (Wed, 18 May 2022 14:50:21 GMT)  
  Author: @GeorgiPapadopo3  
  Content: The ReAwaken America Tour | Charlie Kirk | Why We Must Fight Against Vaccine Mandates

- **Post ID: 1526769735991545856** (Wed, 18 May 2022 03:40:45 GMT)  
  Author: @JessxRaine  
  Content: LMAO EMMA REALLY WENT DOWN THERE TO SUCK JAY’S DICK 😂😂😂😂😂😂 Talking about a Mf tour. GIRRLLLLLL

- **Post ID: 1526753368181313537** (Wed, 18 May 2022 02:35:43 GMT)  
  Author: @BrandonStraka  
  Content: #WalkAway is teaming up with @KariLake to give American Patriots a night to remember! Join us for drinks, hors d’oeuvres, an onstage conversation, Q&A, pictures, handshakes, and more!  
  June 11th in Scottsdale, AZ  
  Tickets are selling FAST!  
  [link]  
  (Includes photo media)

- **Post ID: 1526705568198451200** (Tue, 17 May 2022 23:25:46 GMT)  
  Author: @TrumpStudents  
  Content: Don’t miss the EXCLUSIVE AZ showing of '2000 Mules' THIS SUNDAY featuring Congressman Andy Biggs!🔥  
  Join Turning Point Action w/special guests @DineshDSouza, @charliekirk11, @RepAndyBiggsAZ & AZ Rep Jake Hoffman for this EXCLUSIVE event! 🇺🇸  
  TICKETS?  
  👉 [link]  
  (Includes photo media)

- **Post ID: 1526684543838724097** (Tue, 17 May 2022 22:02:14 GMT)  
  Author: @CatoTheElder71  
  Content: BREAKING! A SERIOUS EVENT IS COMING!  
  [YouTube link]

- **Post ID: 1526639970953244672** (Tue, 17 May 2022 19:05:07 GMT)  
  Author: @issashowgirl  
  Content: SWIFTIE REMINDER: tomorrow taylor is set to speak at NYU for the their class of 2022. this isn’t for promotion, there will be no performances, and not easter eggs. She is there to give the graduating students advice to help them prepare for life after college.

- **Post ID: 1526622521109250048** (Tue, 17 May 2022 17:55:46 GMT)  
  Author: @TrumpStudents  
  Content: EXCLUSIVE ARIZONA SHOWING OF '2000 MULES' 🔥🔥🔥  
  Join Turning Point Action w/special guests @DineshDSouza, @charliekirk11, @RepAndyBiggsAZ & State Rep Jake Hoffman for an EXCLUSIVE showing of '2000 Mules' THIS SUNDAY! 🇺🇸  
  NEED TICKETS?  
  👉 [link]  
  (Includes 2 photo media items)

- **Post ID: 1526599665503727617** (Tue, 17 May 2022 16:24:57 GMT)  
  Author: @OANN  
  Content: 45th President Donald J. Trump is set to host a 'Save America' rally on May 28th in Casper, Wyo. Be sure to tune in to One America News for LIVE, uninterrupted coverage! #OANN  
  (Includes photo media)

- **Post ID: 1526339467409297409** (Mon, 16 May 2022 23:11:01 GMT)  
  Author: @gaywonk  
  Content: “The Rise of ‘Head Empty’ Fascism” is premiering in an hour.  
  It’s a video about Charlie Kirk, spectacles, and the power of ‘vibes’ in politics.  
  It’s also a video about propaganda, and if you watch till the end you’ll get to see shit like this:  
  [link]  
  (Includes video media)

- **Post ID: 1526311635945566208** (Mon, 16 May 2022 21:20:26 GMT)  
  Author: @charliekirk11  
  Content: Breaking down all the data behind the bombshell film from @DineshDSouza — '2,000 Mules'  
  Join me May 22 in Arizona for an in-depth analysis of the 2020 Election. Get your tickets NOW!  
  ➡️➡️➡️ [link]  
  (Includes photo media)

- **Post ID: 1526218540692512773** (Mon, 16 May 2022 15:10:30 GMT)  
  Author: @realDailyWire  
  Content: We've announced another Backstage LIVE at the Ryman in Nashville!  
  On June 29th, join the Daily Wire hosts for their roundtable discussion and a celebration of the incredible victories we've had over the past year!  
  Get your tickets here: [link]  
  (Includes photo media)

- **Post ID: 1525963852180905985** (Sun, 15 May 2022 22:18:28 GMT)  
  Author: @BrandonStraka  
  Content: ARIZONA! #WalkAway is inviting you to get “KARI’D AWAY” June 11th in Scottsdale, AZ!  
  Join @KariLake, @BrandonStraka, and the #WalkAway Team for a magical night of inspirational conversation, Q&A, and food and drinks 🍹 🍷 🍱  
  Get tickets now:  
  [link]  
  (Includes photo media)

- **Post ID: 1525481758736752640** (Sat, 14 May 2022 14:22:48 GMT)  
  Author: @ScottPresler  
  Content: When: Saturday, May 14th  
  Time: @ 1 pm - 3 pm  
  Where:  
  Memorial Park Bandshell  
  (Next to The Monument)  
  (Includes photo media)

**Semantic search results** for queries about Charlie Kirk/TPUSA events in the date range primarily overlapped with the above keyword results and did not yield additional unique posts about events *within* May 14–20. Other posts referenced unrelated events (e.g., Taylor Swift at NYU, Daily Wire Backstage Live, Trump rally on May 28).[[4]](https://x.com/issashowgirl/status/1526639970953244672)

**No posts** were returned from official accounts @charliekirk11 or @TPUSA in the initial targeted searches for this exact window beyond the *2000 Mules* announcement on May 16. All other results are user-generated mentions or reactions. No further posts matched additional refinements for specific dates or locations within the week.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-05-14 to 2022-05-20**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-05-14 to 2022-05-20 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
