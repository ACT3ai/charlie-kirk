---
unlisted: true
title: "Week 24 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W24"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-06-10 to 2024-06-16."
status: completed
hide_table_of_contents: true
---

# Week 24, 2024

- Date range: 2024-06-10 to 2024-06-16
- Queried at (UTC): 2026-08-24T19:13:01Z
- Model: grok-4.3
- API status: completed
- Response id: ebc3ac39-d22f-96dc-9790-de69d5f69eca

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-06-10 to the end of the week 2024-06-16.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearance OR campus) since:2024-06-10 until:2024-06-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearance OR campus) since:2024-06-10 until:2024-06-17 filter:has_engagement",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between June 10-16 2024",
      "limit": "10",
      "from_date": "2024-06-10",
      "to_date": "2024-06-17"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"People's Convention\" OR #PEOPLES2024) (Detroit OR Michigan OR Huntington) since:2024-06-10 until:2024-06-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speak OR speaking OR event OR appearance OR tour OR \"will speak\" OR campus) since:2024-06-10 until:2024-06-17 -Detroit -Michigan -Huntington",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk TPUSA events or speaking appearances in June 2024 excluding Detroit Michigan People's Convention",
      "limit": "5",
      "from_date": "2024-06-10",
      "to_date": "2024-06-17"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 19522,
  "input_tokens_details": {
    "cached_tokens": 10048
  },
  "output_tokens": 3417,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 22939,
  "num_sources_used": 0,
  "num_server_side_tools_used": 6,
  "cost_in_usd_ticks": 523946000,
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
    "input_tokens": 10844,
    "output_tokens": 3033
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802124551272157630",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802124551272157630"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802128805080740037",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802128805080740037"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802093112396808637",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802093112396808637"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802126744888946757",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802126744888946757"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802128190564933933",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802128190564933933"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800160158708080931",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800160158708080931"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802124750690611443",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802124750690611443"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1801717872659456166",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1801717872659456166"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800493768237580435",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800493768237580435"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802124602912690304",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802124602912690304"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802124096643510768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802124096643510768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800361463732945124",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800361463732945124"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800324900512780304",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800324900512780304"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802127608546824328",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802127608546824328"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800591978306109649",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800591978306109649"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800267347997176090",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800267347997176090"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802084712283779570",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802084712283779570"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802126542337614032",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802126542337614032"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802127389884850340",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802127389884850340"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802066845081440529",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802066845081440529"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802128816308957692",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802128816308957692"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802127566616027235",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802127566616027235"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1802127030445543855",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1802127030445543855"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1800155830089846825",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1800155830089846825"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (June 10–16, 2024) mentioning Charlie Kirk or TPUSA/TP Action public speaking events, appearances, or locations where Charlie Kirk/TPUSA is scheduled to speak or host events.** (Note: The search window was extended to until:2024-06-17 to fully capture posts referencing the end of the week of June 16. No other events, tours, campus appearances, or speaking engagements for Charlie Kirk or TPUSA were found outside the main Detroit/Michigan event in this timeframe.)

- **Post [post:0]** (and duplicate [post:3], [post:21]):  
  Author: @censoreddottv  
  Timestamp: Sat, 15 Jun 2024 23:56:57 GMT  
  Content: HAPPENING NOW: Groypers waiting to hear Nick Fuentes speak outside the Huntington Place building where TPUSA is holding their annual convention  
  @AsianPatDixon @AngryPatriotX  
  (Media: Video of the scene outside the venue.)

- **Post [post:1]** (and duplicate [post:4], [post:26]):  
  Author: @ArkansasGroyper  
  Timestamp: Sat, 15 Jun 2024 23:51:12 GMT  
  Content: Is it possible that Charlie Kirk/TPUSA could be behind what’s going on with AFPAC? Nick did humiliate Charlie’s event yesterday. Maybe this is his revenge? 🧐  
  Of course this is just speculation, but you never know. 🤷🏻‍♂️

- **Post [post:2]** (and duplicate [post:5]):  
  Author: @JerryXhandle  
  Timestamp: Sat, 15 Jun 2024 23:50:24 GMT  
  Content: This is a photo from 180 Church today, the Detroit church Trump is visiting.  
  A lot of Trump’s support at the event is from out of town people in Detroit for Charlie Kirk’s TPUSA event.  
  (Quotes a post with photo from @patriottakes: “This is a photo from 180 Church today, the Detroit church Trump is visiting. A lot of Trump’s support at the event is from out of town people in Detroit for Charlie Kirk’s TPUSA event.”)

- **Post [post:6]:**  
  Author: @NahBabyNahNah  
  Timestamp: Sat, 15 Jun 2024 23:43:17 GMT  
  Content: President Trump Delivers Remarks at TPUSA Event in Michigan, 6:00pm ET Livestream: Tonight, President Donald Trump is speaking at Turning Point USA’s “The People’s Convention” in Detroit, Michigan. The anticipated start time for President Trump’s remarks…  
  (Media: Photo.)

- **Post [post:7]:**  
  Author: @switchnbait  
  Timestamp: Sat, 15 Jun 2024 23:42:41 GMT  
  Content: The event is always near tpusa or cpac. We prefer the concrete wall to the online circle jerk you want the gentile to remain in. Sorry jew, no brakes.

- **Post [post:8]:**  
  Author: @CanadianNjgga  
  Timestamp: Sat, 15 Jun 2024 23:42:29 GMT  
  Content: That is the turning point USA event…

- **Post [post:9]** (and duplicate [post:29]):  
  Author: @EvanAKilgore  
  Timestamp: Sat, 15 Jun 2024 23:40:41 GMT  
  Content: BREAKING:  
  The America First movement has taken over outside the streets of the convention center where TPUSA just hosted President Donald Trump.  
  They are demanding @NickJFuentes come and speak.  
  They are also chanting "America First, "Groyper" and "Christ is King."  
  (Media: Video.)

- **Post [post:10]:**  
  Author: @TPostMillennial  
  Timestamp: Mon, 10 Jun 2024 13:19:29 GMT  
  Content: Tucker Carlson announces Live Nationwide Tour this fall  
  (Media: Video. No direct Charlie Kirk/TPUSA tie-in beyond later mentions.)

- **Post [post:11]:**  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Fri, 14 Jun 2024 20:46:29 GMT  
  Content: “At Turning Point Action, we wanted to put on an event, a training that is for you, the citizen, that is for We the People, that is for a restoration of this Republic. In the next couple of days, you will be challenged. You will be encouraged...  
  This is going to be the end of spectator politics... Instead, we are going to make a commitment that this year, this calendar year, will be the hardest year we have ever worked.”  
  @tpaction #PEOPLES2024  
  (Media: Video. Refers to the upcoming People’s Convention.)

- **Post [post:12]** (and duplicate [post:30]):  
  Author: @MarioNawfal  
  Timestamp: Sat, 15 Jun 2024 19:53:11 GMT  
  Content: 🇺🇸TRUMP HEADS TO DETROIT  
  He is scheduled to speak at a local church and at Turning Point USA's People's Convention at Huntington Place this weekend.  
  Source: donaldjtrumpjr on TikTok  
  (Media: Video.)

- **Post [post:13]:**  
  Author: @yashar  
  Timestamp: Mon, 10 Jun 2024 20:42:37 GMT  
  Content: Tucker Carlson is doing an arena tour around the USA starting in September.  
  In each city he will have a special guest join him, here are the guests announced so far:  
  Russell Brand  
  Vivek Ramaswamy  
  Tulsi Gabbard  
  Glenn Beck  
  Dan Bongino  
  Megyn Kelly  
  Charlie Kirk  
  Alex Jones  
  Kid Rock  
  Roseanne Barr  
  Marjorie Taylor Greene and Dr. Kevin Roberts  
  Donald Trump Jr.

- **Post [post:14]:**  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Tue, 11 Jun 2024 02:56:36 GMT  
  Content: Thank you Mr. President!!  
  "Right Wing Revolution: How to Beat the Woke and Save the West" comes out June 18th. It takes my 12 years of activism and distills them into one, how-to guide that YOU can put into action.  
  America is worth saving. This is how.  
  (Media: Photo. Book promotion tied to TPUSA activism.)

- **Post [post:15]:**  
  Author: @senatorbabet  
  Timestamp: Tue, 11 Jun 2024 11:42:20 GMT  
  Content: Legendary Australian businessman Clive Palmer has organised the 'Australian Freedom Conference' which will begin in less than 2 weeks!  
  It will feature:  
  -Global phenomenon and media titan Tucker Carlson.  
  -Political commentator, author and filmmaker, Dinesh D'Souza, whose recent films include 2000 Mules, Police State, Trump Card and Death of a Nation  
  -Queensland GP Dr Melissa McCann who has been instrumental in the struggle for compensation for people affected by Covid-19 injections  
  Grab your tickets here - https://t.co/2fJAhoeXLN  
  Fri 21 Jun 2024  
  Cairns Convention Centre, QLD  
  Sat 22 Jun 2024  
  Brisbane Entertainment Centre, QLD  
  Sun 23 Jun 2024  
  Adelaide Entertainment Centre Arena, SA  
  Mon 24 Jun 2024  
  PCEC Riverside Theatre, WA  
  Fri 28 Jun 2024  
  ICC Sydney Theatre, NSW  
  Mon 1 Jul 2024  
  Melbourne Convention and Exhibition Centre, VIC  
  See you there!  
  @TuckerCarlson @TCNetwork @DineshDSouza @drmelissamccann @CliveFPalmer @UnitedAusParty  
  (Media: Video. No TPUSA/Charlie Kirk mention.)

- **Post [post:16]:**  
  Author: @RealAlexJones  
  Timestamp: Tue, 11 Jun 2024 00:31:19 GMT  
  Content: Tucker Carlson's National Tour Can Save America  
  I'll be special guest September 16th in Milwaukee Wisconsin  
  For Tickets Go To https://drjonesnaturals.com/  
  Support Free Speech https://t.co/c7Lo59BhOD  
  (Media: Video.)

- **Post [post:17]** (and duplicate [post:31]):  
  Author: @charliekirk11 (Charlie Kirk)  
  Timestamp: Tue, 11 Jun 2024 18:12:35 GMT  
  Content: Huge!! Finally official. @JDVance1 will be LIVE from The People's Convention in Detroit this weekend.  
  Join us👇

- **Post [post:18]:**  
  Author: @TCNetwork  
  Timestamp: Mon, 10 Jun 2024 13:36:41 GMT  
  Content: Pre-sale tickets are live now. Get yours at https://tuckercarlson.com/events  
  (Media: None listed.)

- **Post [post:19]:**  
  Author: @Matt_of_MI  
  Timestamp: Sat, 15 Jun 2024 23:59:26 GMT  
  Content: I love @NickJFuentes but America is not ready for him. Still an operation underway 😉😘. It has to happen this way. Can’t wait to see what nick does about this tho haha.

- **Post [post:20]:**  
  Author: @MichiganWave  
  Timestamp: Sat, 15 Jun 2024 23:59:23 GMT  
  Content: Still encounter so many SoCons who don't know what time it is. If you conceal your power level, you Might be able to assemble in/rent out major venues. But even then, you have to be as cunning as possible.

- **Post [post:22]:**  
  Author: @mindys4biden  
  Timestamp: Sat, 15 Jun 2024 23:54:38 GMT  
  Content: Random shooting in Michigan. Isn’t that where a lot of MAGA are gathered for their Turning Point meeting and party convention?

- **Post [post:23]:**  
  Author: @MichiganWave  
  Timestamp: Sat, 15 Jun 2024 23:54:28 GMT  
  Content: In retrospect, the cypto-Commie state of affairs after 2005 was inevitable after immigration control was pathologized/made taboo 1998-2000. Doing that was a Uniparty project w/ the SPLC infomally allied w/ CON Inc, the WSJ etc.  
  They intended 2end freedom of assembly for Whites  
  (Quotes a post about AFPAC IV cancellation.)

- **Post [post:24]:**  
  Author: @Matt_of_MI  
  Timestamp: Sat, 15 Jun 2024 23:53:46 GMT  
  Content: Fuck ya. Any word on why their venue backed out and cops showed up?

- **Post [post:25]:**  
  Author: @mindys4biden  
  Timestamp: Sat, 15 Jun 2024 23:52:20 GMT  
  Content: I just watched Trump's speech at the Turning Point convention in Detroit so that you wouldn't have to. You're welcome. Tonight he never veered off the teleprompter. It was largely all the same bullshit he always spews. But one part caught my attention and seemed somewhat alarming

- **Post [post:27]:**  
  Author: @switchnbait  
  Timestamp: Sat, 15 Jun 2024 23:42:41 GMT  
  Content: The event is always near tpusa or cpac. We prefer the concrete wall to the online circle jerk you want the gentile to remain in. Sorry jew, no brakes.

- **Post [post:28]:**  
  Author: @CanadianNjgga  
  Timestamp: Sat, 15 Jun 2024 23:42:29 GMT  
  Content: That is the turning point USA event…

- **Post [post:32]:**  
  Author: @NEWSMAX  
  Timestamp: Sat, 15 Jun 2024 21:37:33 GMT  
  Content: COMING UP: Former President Donald Trump speaks at Turning Point Action's "People's Convention" in Detroit, Michigan. Watch it LIVE on NEWSMAX or NEWSMAX2! @tpaction #PEOPLES2024  
  (Link to broadcast.)

- **Post [post:33]:**  
  Author: @RSBNetwork  
  Timestamp: Sat, 15 Jun 2024 21:04:11 GMT  
  Content: LIVE COVERAGE: President Trump set to headline The People’s Convention hosted by TP Action in Detroit, Michigan at 6:00pm ET  
  (Media: Video.)

**Key details across posts (all raw data, no summarization):**  
- Primary event: TPUSA / Turning Point Action’s “The People’s Convention” (also called annual convention or #PEOPLES2024) at Huntington Place, Detroit, Michigan.  
- Dates referenced: Weekend of June 15–16, 2024 (posts from June 14–15 confirm “this weekend”).  
- Speakers/appearances mentioned: President Donald Trump (main headline speaker at 6:00pm ET on June 15), JD Vance (LIVE from the convention), Charlie Kirk (host/organizer via TPUSA/TP Action).  
- Additional context: Out-of-town attendees also at a Detroit church (180 Church) for Trump visit; protests/counter-events by Groypers/Nick Fuentes supporters outside the venue.  
- No other Charlie Kirk or TPUSA speaking events, campus stops, tours, or locations identified in the date range. Tucker Carlson-related posts mention Charlie Kirk only as a future tour guest (September 2024 onward, not in this week).
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-06-10 to 2024-06-16**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-06-15](/Planes/Incidents/N582MM-2024-06-15-KDTW) | [N582MM](/Planes/N582MM/overview) | [KDTW](/Planes/Airports/KDTW) | Romulus, MI | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
