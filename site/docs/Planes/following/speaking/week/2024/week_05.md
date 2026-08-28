---
unlisted: true
title: "Week 05 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W05"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-01-29 to 2024-02-04."
status: completed
hide_table_of_contents: true
---

# Week 05, 2024

- Date range: 2024-01-29 to 2024-02-04
- Queried at (UTC): 2026-08-24T19:11:15Z
- Model: grok-4.3
- API status: completed
- Response id: 530ac365-572e-99b7-bcb6-a2d8e6ce68e4

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-01-29 to the end of the week 2024-02-04.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR campus OR \"public speaking\" OR rally) since:2024-01-29 until:2024-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus) since:2024-01-29 until:2024-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR campus) since:2024-01-29 until:2024-02-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus visits, or appearances where Charlie will speak between Jan 29 and Feb 4 2024",
      "limit": "10",
      "from_date": "2024-01-29",
      "to_date": "2024-02-05"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 8063,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 2658,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 10721,
  "num_sources_used": 0,
  "num_server_side_tools_used": 4,
  "cost_in_usd_ticks": 334981500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 4,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 6473,
    "output_tokens": 2427
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753875177111261471",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753875177111261471"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753438495333667251",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753438495333667251"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752756744542158865",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752756744542158865"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753897117985177766",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753897117985177766"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753872009488982351",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753872009488982351"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753858778078888218",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753858778078888218"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753884031572451401",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753884031572451401"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752458761447317613",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752458761447317613"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752589171460653297",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752589171460653297"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752781962752790898",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752781962752790898"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753859718513295585",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753859718513295585"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753536432789225957",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753536432789225957"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752043992210870652",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752043992210870652"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753858674655961468",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753858674655961468"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1752372306662551826",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1752372306662551826"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1753871272965009597",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1753871272965009597"
  }
]
```

## Grok response

```text
**All posts from the X searches (keyword and semantic) matching the date range 2024-01-29 to 2024-02-04 (extended to until:2024-02-05 for end-of-week coverage) are included below in full, without summarization.** No direct announcements of Charlie Kirk or TPUSA public speaking events, campus visits, or appearances by Charlie Kirk himself appear in the results for this exact week. The posts primarily reference past/recent TPUSA-related events (e.g., the Restoring National Confidence Summit in Las Vegas), criticisms, or unrelated topics.

### From @charliekirk11 account (keyword search):
- **Post ID: 1753438495333667251** (Feb 2, 2024, 15:21:29 GMT)  
  Content: "I admire Bret Weinstein. He loves truth and is willing to speak out. We need more people like him."  
  (Quoted post about Bret Weinstein on migration; no event details.)

- **Post ID: 1753536432789225957** (Feb 2, 2024, 21:50:39 GMT)  
  Content: "The Restoring National Confidence Summit was a massive success. We hosted over 400 grassroots warriors in Vegas including:  
  - 75 of the top GOP County Chairs representing 15 million voters in key battleground districts.  
  - 130 RNC members total including state GOP chairs and RNC committeemen and women  
  - Dozens of RNC candidates running to become RNC committeemen  
  - Dozens of precinct captains in battleground districts  
  - Dozens of partner orgs including Tea Party Patriots, Moms for Liberty, College Republicans, America First Works, and more.  
  We shared Turning Point data, technology, and GOTV relational strategies.  
  We drilled down to the precinct level, educating each attendee how to target LOW PROPENSITY conservative leaning voters who stayed home in 2020.  
  We also announced that @tpaction is hiring 300 full-time staff in Wisconsin, Arizona, and Georgia to embed themselves into the community and CHASE BALLOTS.  
  We can't do it alone. We need the grassroots to rise up and get in the arena.  
  Visit [link] and join the mission."  
  (Media: 4 photos of the event/summit.)

- **Post ID: 1752756744542158865** (Jan 31, 2024, 18:12:27 GMT)  
  Content: "BIG WIN IN VEGAS 🚨  
  While the RNC fumbles over itself and doesn’t care about winning in November, TURNING POINT ACTION hosted the FIRST ever alternative RNC summit training for state chairs and county chairs.  
  PLEASE WATCH THIS —>  
  We can't do it alone. We need the grassroots, multiple orgs, and local GOP leaders to pick up the slack.  
  This is how we WIN!  
  Onward  
  🇺🇸"  
  (Media: 1 video of the summit.)

- **Post ID: 1752372306662551826** (Jan 30, 2024, 16:44:50 GMT)  
  Content: "One of our GOP County Chairs just now at The Restoring National Confidence Summit:  
  “Thank you to Turning Point, I’ve learned more in one day than I did in two years with the RNC.”"  
  (Media: 1 video from the summit.)

### From @TPUSA account (keyword search):
- No results found.

### Other accounts (keyword search for "Charlie Kirk" OR TPUSA OR "Turning Point USA" + event/speaking terms):
- **Post ID: 1753897117985177766** (Feb 3, 2024, 21:43:53 GMT, @FutureHOF3)  
  Content: "What Charlie Kirk is saying, is what j said before. DEI and AA is a net negative for black people. But Charlie isn’t speaking as from the perspective of it being net negative for black people. He’s making it a negative for himself. DEI doesn’t only apply to blacks people. It applies to Evryone the left considers a minority. But because Charlie is not speaking for himself, he outs himself as only having an issue with black people. Just because it creates a negative thought pattern doesn’t mean you have it submit to it. But it seems like this has give Charlie an opportunity to speak how he really feels about black people. @charliekirk11 are you that weak willed that the left can just change the way yon think, to the point where you question every black person? You can’t check yourself before doing that?"  
  (Quotes a video clip of Charlie Kirk commenting on affirmative action/DEI.)

- **Post ID: 1753884031572451401** (Feb 3, 2024, 20:51:53 GMT, @RogerTheweeg)  
  Content: "It’s not church policy and you know it."  
  (Reply in a thread; no event details.)

- **Post ID: 1753875177111261471** (Feb 3, 2024, 20:16:42 GMT, @patriottakes)  
  Content: "Former GOP candidate Tudor Dixon says it’s “fishy” that Charlie Kirk owns millions of dollars in property and rakes in all these speaking fees while TPUSA brings in million of dollars."  
  (Media: 1 video.)

- **Post ID: 1753872009488982351** (Feb 3, 2024, 20:04:07 GMT, @zzag0939)  
  Content: "I think they would want people who can carry their own platform. Unless you want to do things in the background (research, producer, makeup, event planner <IDK> etc..)  
  here's 2 women (who agree w/ u) working for TpUSA on Charlies show last week:"  
  (Mentions TPUSA but no new events.)

- **Post ID: 1753859718513295585** (Feb 3, 2024, 19:15:16 GMT, @skiptheviolence)  
  Content: "Enough with this Charlie Kirk"

- **Post ID: 1753858778078888218** (Feb 3, 2024, 19:11:32 GMT, @CLK1341104)  
  Content: "Before you call them vulgar…. Why don’t you actually show up to a rally and talk to people for yourself… You’ll see people just wanting jobs and sanity"

- **Post ID: 1753858674655961468** (Feb 3, 2024, 19:11:07 GMT, @Taz8888888)  
  Content: "Charlie Kirk doesn't speak for us, assuming that is what he said. I will check it out in context."

### Semantic search results (relevant posts mentioning events/appearances in or near the date range):
- **Post ID: 1752589171460653297** (Jan 31, 2024, 07:06:34 GMT, @realTuckFrumper)  
  Content: "Kyle Rittenhouse to Speak at Tennessee University and Things Aren’t Looking Very Good for Him [link]"

- **Post ID: 1753536432789225957** (Feb 2, 2024, 21:50:39 GMT, @charliekirk11) — *Duplicate of above; full content on Restoring National Confidence Summit in Vegas.*

- **Post ID: 1752756744542158865** (Jan 31, 2024, 18:12:27 GMT, @charliekirk11) — *Duplicate of above; TPUSA/TPAction Vegas summit.*

- **Post ID: 1753871272965009597** (Feb 3, 2024, 20:01:11 GMT, @patriottakes)  
  Content: "Trump advisor Pastor Darrell Scott revealed that Charlie Kirk pays for the travel of students to attend his Turning Point USA events which he then uses to ask for more money from his donors."  
  (Media: 1 video.)

- **Post ID: 1752372306662551826** (Jan 30, 2024, 16:44:50 GMT, @charliekirk11) — *Duplicate of above; summit quote.*

- **Post ID: 1752458761447317613** (Jan 30, 2024, 22:28:22 GMT, @HornSports)  
  Content: "Texas AD Chris Del Conte announces in his weekly newsletter that the annual town hall will be held on February 13th. CDC also mentioned his staff is reviewing and identifying season ticket accounts exhibiting broker behavior to help give fans more tickets to access. #HookEm"  
  (Unrelated to Charlie Kirk/TPUSA.)

- **Post ID: 1752781962752790898** (Jan 31, 2024, 19:52:39 GMT, @laralogan)  
  Content: "Here are the details for the rally in Dripping Springs. Texas. This is direct from those in charge - no one to lie/deceive you. Go to the source - get it right. Most of what it being said is untrue.  
  PRESS RELEASE  
  WARNO for TAKE OUR BORDER BACK CONVOY RALLY at One Shot Distillery and Brewery, 1 Feb 24, 1700-2000  
  This is a peaceful first amendment gathering to express concerns about border security, its impact on local communities, and to hear from experts with first-hand experience. Citizens that are concerned about border security are invited to a Private Event at One Shot Distillery and Brewery, 31610 Ranch Road 12, Dripping Springs, TX on 1 Feb 2024. Gates will open at 1600 (4 pm) and the program will run from approximately 1700-2000 hrs (5-8 pm). There will be entertainment, border experts, convoy participants and several other speakers who share concern for Texas’ and our Nation’s security.  
  Coordinating Instructions:  
  Parking will be at Moxie Gymnastics at 31430 Ranch Road 12, Dripping Springs – one block south of One Shot.  
  There will be seating for approximately 500 people, so please bring a folding chair if possible. Gates will close when max capacity is reached.  
  Please do not come to the rally armed, with any type of tactical gear, backpacks or coolers. There will be ample security provided by local and state law enforcement, as well as private security.  
  This is a community and family event, behavior that is not consistent will result in rapid ejection from the gathering.  
  Premises will close promptly at 2100 hrs (9 pm)."  
  (Border rally; unrelated to Charlie Kirk/TPUSA.)

- **Post ID: 1752043992210870652** (Jan 29, 2024, 19:00:13 GMT, @CPAC)  
  Content: "Confirmed Speaker: @EVerastegui for CPAC in DC 2024  
  Join us February 21 - 24 for CPAC in DC!  
  Sign-up at [link]"  
  (CPAC event in Feb 2024; no mention of Charlie Kirk or TPUSA.)

No additional posts were returned beyond these in the tool results. All content is presented exactly as retrieved.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-01-29 to 2024-02-04**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-01-29 to 2024-02-04 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
