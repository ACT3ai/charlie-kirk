---
unlisted: true
title: "Week 27 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W27"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-07-02 to 2023-07-08."
status: completed
hide_table_of_contents: true
---

# Week 27, 2023

- Date range: 2023-07-02 to 2023-07-08
- Queried at (UTC): 2026-08-24T19:07:48Z
- Model: grok-4.3
- API status: completed
- Response id: 35979b72-6bbd-9221-8167-9c3bb1472c4e

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-07-02 to the end of the week 2023-07-08.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR speaking OR speaks) since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speak OR speech OR tour OR appearance) since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between July 2 and July 8 2023",
      "limit": "10",
      "from_date": "2023-07-02",
      "to_date": "2023-07-08"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"Turning Point USA\" OR \"Turning Point Action\" OR TPAction OR \"ActCon\" OR ACTCON) (event OR speaking OR speak OR speech OR tour OR appearance OR \"will be\" OR speaks OR speaking OR conference OR \"book signing\") since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR speech OR tour OR appearance OR conference OR \"book signing\" OR TPUSA OR TPAction OR ACTCON) since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR speech OR tour OR appearance OR conference OR \"book signing\" OR Charlie OR Kirk) since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPAction (event OR speaking OR speak OR speech OR tour OR appearance OR conference OR \"book signing\" OR Charlie OR Kirk) since:2023-07-02 until:2023-07-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR charliekirk11 OR TPUSA OR TPAction OR \"Turning Point Action\" OR ACTCON OR \"ActCon2023\") (West Palm Beach OR Florida OR Palm Beach OR \"book signing\" OR Kari Lake) since:2023-07-02 until:2023-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Kari Lake\" OR \"book signing\") (Charlie Kirk OR charliekirk11 OR TPUSA OR TPAction) since:2023-07-02 until:2023-07-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPAction since:2023-07-02 until:2023-07-09",
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
  "input_tokens": 36640,
  "input_tokens_details": {
    "cached_tokens": 24064
  },
  "output_tokens": 2159,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 38799,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 759303000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 10,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 14016,
    "output_tokens": 1509
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677418683239636992",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677418683239636992"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677397527291899904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677397527291899904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677432409753784321",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677432409753784321"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677433333167321088",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677433333167321088"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677005670686806016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677005670686806016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676069436783230978",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676069436783230978"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1675591980745920513",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1675591980745920513"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676764710623141888",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676764710623141888"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677432323153997824",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677432323153997824"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677106338168713218",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677106338168713218"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677450796617846785",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677450796617846785"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677006648936914944",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677006648936914944"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676874080161771520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676874080161771520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677450720440725506",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677450720440725506"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676637289957687296",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676637289957687296"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677416245023371264",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677416245023371264"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677448246426206210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677448246426206210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677134592116129793",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677134592116129793"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676713348468035584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676713348468035584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676720109132603393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676720109132603393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677445160186138624",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677445160186138624"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677443088955084801",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677443088955084801"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677446392602669058",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677446392602669058"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1675695075651907584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1675695075651907584"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677045376099000320",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677045376099000320"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677006317645606917",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677006317645606917"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677416426238537728",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677416426238537728"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1677335403861295109",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1677335403861295109"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1675922284991619084",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1675922284991619084"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1676647761255747584",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1676647761255747584"
  }
]
```

## Grok response

```text
**All relevant X posts from July 2–8, 2023 (searched via keyword and semantic queries for "Charlie Kirk", TPUSA, TPAction, Turning Point USA/Action, ACTCON/ActCon2023, events, speaking, speeches, conferences, appearances, book signings, etc., within the exact date range):**

- **[post:14]** (Charlie Kirk @charliekirk11, Wed Jul 5, 2023):  
  "TURNING POINT ACTION CONFERENCE #ACTCON2023 IS ONLY 10 DAYS AWAY  
  WE WILL RUN OUT OF TICKETS. GET YOURS TODAY   
  Trump  
  Tucker  
  Megyn Kelly  
  Vivek  
  Bongino  
  Bannon   
  Gaetz   
  MTG  
  Donalds   
  Boebert   
  Cruz  
  Hawley   
  Vance   
  Paulina Luna   
  Benny  
  Poso   
  Presler   
  AND MORE  
  https://t.co/kn40D7KruX"

- **[post:15]** (Charlie Kirk @charliekirk11, Thu Jul 6, 2023):  
  "We are 9 days out from the largest grassroots and "super activist" event of the year - we expect over 6,000 people from all 50 states in Palm Beach. Many people are asking me, "Where are the other presidential candidates?" So I figured I would share where we stand currently:  
  Trump - CONFIRMED  
  @VivekGRamaswamy - CONFIRMED  
  @FrancisSuarez - CONFIRMED  
  @Mike_Pence - declined  
  @SenatorTimScott - declined  
  @NikkiHaley - declined  
  @GovChristie - TBD / no response  
  @RonDeSantis - TBD  
  @AsaHutchinson - TBD / no response  
  @DougBurgum - TBD / no response  
  @larryelder - TBD / no response  
  All these candidates are welcome to make their case to the base of the party and millions more watching online. We will treat every candidate with the utmost respect and honor them for their time. The people attending are engaged in state and local politics. These are the people you must convince to win a GOP primary.  
  The event is just days away, will be curious to see who ends up showing up!  
  https://t.co/mtpiEQq9wP #ActCon2023"

- **[post:16]** (Charlie Kirk @charliekirk11, Tue Jul 4, 2023):  
  "Trump  
  Tucker  
  Megyn Kelly  
  Bongino  
  Bannon  
  Hawley  
  Vance  
  Scott   
  Ramaswamy   
  Suarez  
  Gaetz   
  Boebert   
  Benny  
  Poso  
  And More  
  #ACTCON2023 only weeks away from the premiere summer event in the conservative movement.   
  Get your tickets today at https://t.co/EtHw8Ga7E6"

- **[post:17]** (Charlie Kirk @charliekirk11, Fri Jul 7, 2023):  
  "Okay we just wrapped the show but watch it from the top if you missed it. Ep. 4 was the BEST THOUGHTCRIME THURSDAY YET!   
  (p.s. Next Thursday we’ll be live from ACTCON in Florida)  
  Must Watch:  
   https://rumble.com/v2yk2aw-thoughtcrime-ep.-4-disney-flops-and-desantis-deflates-incel-armageddon-liza.html"

- **[post:21]** (Jack Posobiec @JackPosobiec, Fri Jul 7, 2023):  
  "BREAKING: Sound of Freedom WILL be screened at Turning Point Action   
  AND   
  Tim Ballard will be speaking   
  Tickets are almost SOLD OUT ->   
  https://t.co/nOie9RLReU, Promocode Poso  
  July 15-16, West Palm Beach"

- **[post:1]** (Natalia Marie Carissimi @NanLee1124, Fri Jul 7, 2023; quoting Scott Presler):  
  "LOOK who’s speaking at the Turning Point Action Conference in West Palm Beach, FL!📢  
  “If you will it - & work for it - you can win it.” @ScottPresler   
  @TurningPointACT   
  @TPUSA   
  SEE THIS🇺🇸🇺🇸🇺🇸‼️⬇️"  
  (Quotes Scott Presler’s post about speaking at the event next weekend.)

- **[post:2]** (No Longer @MESourceOfTruth, Fri Jul 7, 2023):  
  "I’ll be headed to the @TPUSA @tpusafaith Action Conference a week from today to cover the event for @MESourceOfTruth!  If you know anyone who can chip in to help my travel expenses, please go to https://t.co/TvipIjyQBj   
  Please watch the video. ✝️🇺🇸"

- **[post:6]** (Shawn McBreairty @ShawnMcBreairty, Fri Jul 7, 2023):  
  "I’ll be headed to the @TPUSA @tpusafaith Action Conference a week from today to cover the event for @MESourceOfTruth!  If you know anyone who can chip in to help my travel expenses, please go to https://t.co/42papV4dDk   
  @realDonaldTrump @TuckerCarlson @dbongino @charliekirk11 @VivekGRamaswamy @mtgreenee @pnjaban @laurenboebert @JackPosobiec @mattgaetz @tedcruz @ByronDonalds and more!   
  Please watch the video. ✝️🇺🇸"

- **[post:22]** (Kari Lake @KariLake, Fri Jul 7, 2023):  
  "TODAY!   
  There’s still time to register for today’s exclusive book signing with @KariLake, hosted by @charliekirk11 & @tpaction!   
  RSVP: https://t.co/hoHb6c2eU1"

- **[post:40]** (Mona Burrell @lovebignalu, Thu Jul 6, 2023):  
  "I look forward to joining Turning Point Action and Charlie Kirk THIS FRIDAY in Tempe for a book signing!    
  REGISTER at https://t.co/fgfkQmpi4n"

- **[post:41]** (Randy Whitten @RandyWhitten9, Wed Jul 5, 2023):  
  "I look forward to joining Turning Point Action and Charlie Kirk THIS FRIDAY in Tempe for a book signing!    
  REGISTER at https://t.co/V8Vb8gGBAG"

No other posts in the searched date range (July 2–8, 2023) directly referenced additional Charlie Kirk/TPUSA public speaking events, appearances, or locations beyond the above. All data included without summarization.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-07-02 to 2023-07-08**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-07-02 to 2023-07-08 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
