---
unlisted: true
title: "Week 11 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W11"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-03-12 to 2025-03-18."
status: completed
hide_table_of_contents: true
---

# Week 11, 2025

- Date range: 2025-03-12 to 2025-03-18
- Queried at (UTC): 2026-08-24T19:17:18Z
- Model: grok-4.3
- API status: completed
- Response id: 74540b6d-9423-99ac-9789-51023c2714be

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-03-12 to the end of the week 2025-03-18.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR speech OR event OR tour OR \"will be\" OR \"appearing\" OR \"on stage\" OR campus OR university OR college) since:2025-03-12 until:2025-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (tour OR events OR schedule OR \"speaking tour\" OR \"campus tour\") since:2025-03-12 until:2025-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, speeches, campus visits, or tour dates between March 12-18 2025",
      "limit": "10",
      "from_date": "2025-03-12",
      "to_date": "2025-03-18"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR speech OR tour OR TPUSA OR campus) since:2025-03-12 until:2025-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR speech OR tour OR campus OR \"Charlie Kirk\") since:2025-03-12 until:2025-03-19",
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
  "input_tokens": 13213,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 1939,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 15152,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 431381500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 5,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 11623,
    "output_tokens": 1626
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901785089778106866",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901785089778106866"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901777764539404731",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901777764539404731"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900230025712197903",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900230025712197903"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901777442056053077",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901777442056053077"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900224455982670149",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900224455982670149"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901778042789458235",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901778042789458235"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901625893849555379",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901625893849555379"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900245917737115675",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900245917737115675"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901778354468274554",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901778354468274554"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901592968902877371",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901592968902877371"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900342979249783226",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900342979249783226"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901715833505644824",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901715833505644824"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901673212406051256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901673212406051256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900217936339492869",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900217936339492869"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901772854930075724",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901772854930075724"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901772341660594383",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901772341660594383"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901771944971673994",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901771944971673994"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901770339081769357",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901770339081769357"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901574932716273721",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901574932716273721"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901517751782416832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901517751782416832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901758381435572324",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901758381435572324"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900505960826769630",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900505960826769630"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900366501359870020",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900366501359870020"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900341822377123958",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900341822377123958"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900649384557375767",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900649384557375767"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901649143975621055",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901649143975621055"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899852752697938270",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899852752697938270"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900587709095440663",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900587709095440663"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900324593531056264",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900324593531056264"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901498023731233142",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901498023731233142"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901526458922668475",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901526458922668475"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900768117271220706",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900768117271220706"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1900651265224507802",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1900651265224507802"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901772839977709869",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901772839977709869"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901673350276989030",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901673350276989030"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1901782826762043432",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1901782826762043432"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899834232807268823",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899834232807268823"
  }
]
```

## Grok response

```text
**Here is every relevant X post from the search results matching the query criteria (posts between 2025-03-12 and 2025-03-18 inclusive, focused on Charlie Kirk or TPUSA public speaking events, appearances, speeches, campus visits, or tour dates). No summarization—full posts are included exactly as retrieved, with context from the tool outputs. Only posts with direct or indirect references to events/speaking in that window are listed; irrelevant posts (e.g., unrelated replies or off-topic) have been excluded.**

### Posts explicitly referencing the University of Tennessee, Knoxville event (part of Charlie Kirk’s “American Comeback Tour”):
- **Post [post:10]** (Mon, 17 Mar 2025 19:22:41 GMT, @UTKDailyBeacon):  
  "Thursday, March 13, hundreds of UT students gathered in the HSS Amphitheatre to support conservative activist Charlie Kirk, who was invited by UT’s TPUSA chapter. As part of his “American Comeback Tour,” Kirk debated students over political issues.  
  https://utdailybeacon.com/campus_news/campus_life/recapping-charlie-kirk-s-presence-at-ut-an-opportunity-for-students-to-engage-in-debate/article_50aabe6a-0364-11f0-89ba-7364b430fa13.html"

- **Post [post:18]** (Fri, 14 Mar 2025 11:15:05 GMT, @knoxnews):  
  "MAGA leader Charlie Kirk stopped at the University of Tennessee at Knoxville on his American Comeback tour. https://www.knoxnews.com/story/news/politics/2025/03/14/charlie-kirk-turned-out-thousands-of-conservative-ut-students/82363421007/?taid=67d40fb9c43a4e0001af92b5&utm_campaign=trueanthem&utm_medium=social&utm_source=twitter"

- **Post [post:19]** (Fri, 14 Mar 2025 00:27:27 GMT, @Bellamari8mazz):  
  "Charlie Kirk brought out a HUGE CROWD at the University of Tennessee, Knoxville!  
  This movement isn’t slowing down🔥🔥🔥🔥"  
  (Includes video media of the crowd.)

- **Post [post:25]** (Fri, 14 Mar 2025 16:39:55 GMT, @charliekirk11):  
  "KNOXVILLE NEWS-SENTINEL: Charlie Kirk's visit shows the MAGA movement is loud and proud at the University of Tennessee  
  🔥🔥  
  https://www.yahoo.com/news/charlie-kirks-visit-proves-conservatism-092316321.html?fr=sycsrp_catchall&guccounter=1&guccounter=1"

- **Post [post:26]** (Thu, 13 Mar 2025 18:01:46 GMT, @charliekirk11):  
  "Just check out this crowd at University of Tennessee, Knoxville 🇺🇸🇺🇸  
  Everywhere we go, the crowds are growing. God bless the USA.  
  @TPUSA"  
  (Includes multiple photos and video media of the large crowd.)

- **Post [post:32]** (Thu, 13 Mar 2025 16:36:29 GMT, @charliekirk11):  
  "HUGE turnout at the University of Tennessee Knoxville! 🔥🔥🔥  
  These kids are fired up for the Trump years. It’s amazing to see.  
  @TPUSA"  
  (Includes multiple videos and one photo of the event.)

- **Post [post:37]** (Thu, 13 Mar 2025 16:58:37 GMT, @TPUSA):  
  "The American Comeback Tour with @charliekirk11 brought out a HUGE CROWD at the University of Tennessee, Knoxville!  
  This movement isn’t slowing down🔥 @tpusastudents"  
  (Includes video media.)

### Posts referencing Wisconsin event (Townhall with Charlie Kirk and Donald Trump Jr.):
- **Post [post:2]** (Mon, 17 Mar 2025 23:29:53 GMT, @BTHLines):  
  "A powerhouse event. Charlie Kirk and Don Jr. bringing the energy to Wisconsin."

- **Post [post:20]** (Mon, 17 Mar 2025 23:27:30 GMT, @TPAction):  
  "Turning Point Action Presents Townhall: Wisconsin LIVE with Charlie Kirk and Donald Trump Jr. https://twitter.com/i/broadcasts/1YqKDZaYBzNJV"

- **Post [post:24]** (Mon, 17 Mar 2025 23:28:47 GMT, @charliekirk11):  
  "Turning Point Action Presents Townhall: Wisconsin LIVE with Charlie Kirk and Donald Trump Jr. https://x.com/i/broadcasts/1DXxyqnPvVExM"

### Posts from @TPUSA linking to tour/event info:
- **Post [post:36]** (Fri, 14 Mar 2025 02:00:55 GMT, @TPUSA):  
  "See our upcoming stops on the American Comeback Tour ⬇️  
  https://theturningpointtour.com/"

- **Post [post:35]** (Fri, 14 Mar 2025 20:45:00 GMT, @TPUSA):  
  "Surround yourself with unapologetic women united in faith, family, and well-being at our WOMEN’S LEADERSHIP SUMMIT 2025!  
  Registration is NOW OPEN for the largest conservative event for women of all ages at https://wls2026.com/"  
  (Note: This promotes a 2025/2026 summit but falls within the date range; no specific March 12-18 dates mentioned.)

### Other mentions of Charlie Kirk/TPUSA events or appearances in the date range (general or indirect):
- **Post [post:4]** (Mon, 17 Mar 2025 23:09:12 GMT, @RedClifford22):  
  "Don't worry guys. Charlie Kirk was just at a college campus telling Christians they should be thankful to jews. He would never lie."

- **Post [post:28]** (Sat, 15 Mar 2025 04:36:48 GMT, @charliekirk11):  
  "I was asked on campus this week: “What has Trump actually accomplished?”  
  Well, he shut down the border in little more than a month. We didn’t need a “bipartisan” border bill, we just needed a new president.  
  I explain why this is such a historic accomplishment:"  
  (Includes video; references recent campus activity.)

- **Post [post:11]** (Mon, 17 Mar 2025 16:33:52 GMT, @Mort429):  
  "Hey TP, I registered to go to one of your events but never received anything and it is tonight, saying its reached capacity, could you assist?"

- **Post [post:13]** (Mon, 17 Mar 2025 11:14:28 GMT, @MonicaPaigeTV):  
  "TODAY’S SCHEDULE:  
  1PM - Press briefing  
  2:55PM - President Trump goes to the Kennedy Center for a Board Meeting and Tour  
  @FrontlinesTPUSA @TPUSA"

No other posts in the tool results directly announced or described additional public speaking events, speeches, or tour stops for Charlie Kirk or TPUSA strictly within March 12–18, 2025. All retrieved data is included above.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-03-12 to 2025-03-18**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2025-03-13](/Planes/Incidents/N582MM-2025-03-13-KTYS) | [N582MM](/Planes/N582MM/overview) | [KTYS](/Planes/Airports/KTYS) | Knoxville, TN | Charlie | **Same day** |
| [2025-03-18](/Planes/Incidents/N582MM-2025-03-18-KLZU) | [N582MM](/Planes/N582MM/overview) | [KLZU](/Planes/Airports/KLZU) | Lawrenceville, GA | Charlie | **Same day** |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
