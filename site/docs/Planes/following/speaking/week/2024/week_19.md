---
unlisted: true
title: "Week 19 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W19"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-05-06 to 2024-05-12."
status: completed
hide_table_of_contents: true
---

# Week 19, 2024

- Date range: 2024-05-06 to 2024-05-12
- Queried at (UTC): 2026-08-24T19:12:35Z
- Model: grok-4.3
- API status: completed
- Response id: 187857fe-008e-9cb5-8c43-b47235130b0c

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-05-06 to the end of the week 2024-05-12.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR \"public speaking\" OR tour OR campus OR speech OR appearing OR appearance OR \"will be\" OR schedule OR tour OR \"speaking at\" OR \"speaking in\") since:2024-05-06 until:2024-05-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR \"public speaking\" OR tour OR campus OR speech OR appearing OR appearance OR \"will be\" OR schedule OR tour OR \"speaking at\" OR \"speaking in\") since:2024-05-06 until:2024-05-13 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR \"public speaking\" OR tour OR campus OR speech OR appearing OR appearance OR \"will be\" OR schedule OR tour OR \"speaking at\" OR \"speaking in\" OR rally OR debate) since:2024-05-06 until:2024-05-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR \"public speaking\" OR tour OR campus OR speech OR appearing OR appearance OR \"will be\" OR schedule OR tour OR \"speaking at\" OR \"speaking in\" OR rally OR debate) since:2024-05-06 until:2024-05-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, speeches, campus tours, or where Charlie will speak between May 6-12 2024",
      "limit": "10",
      "from_date": "2024-05-06",
      "to_date": "2024-05-13"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 16103,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 2960,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 19063,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 493031500,
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
    "input_tokens": 14513,
    "output_tokens": 2547
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789339242222789049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789339242222789049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788055154065080375",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788055154065080375"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787965085161505042",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787965085161505042"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788023068348252539",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788023068348252539"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787550036945162362",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787550036945162362"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787965907727434131",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787965907727434131"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789358905740468411",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789358905740468411"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789305997044904048",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789305997044904048"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788075611132715060",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788075611132715060"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787945444905283900",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787945444905283900"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789380085872578675",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789380085872578675"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789373990345003064",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789373990345003064"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789296251252420770",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789296251252420770"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788946442398453773",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788946442398453773"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789379373889392907",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789379373889392907"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788009913593287120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788009913593287120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788023993158783464",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788023993158783464"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788024171714502712",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788024171714502712"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788306509363126289",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788306509363126289"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789267599244632182",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789267599244632182"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789306035368304743",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789306035368304743"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787972822318596127",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787972822318596127"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788057022153556050",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788057022153556050"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788243725401121253",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788243725401121253"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788034713049075817",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788034713049075817"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789409306556747959",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789409306556747959"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788227679046750497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788227679046750497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1789422324346687559",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1789422324346687559"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1787935542447063167",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1787935542447063167"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788639224566325357",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788639224566325357"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788017247224799436",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788017247224799436"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1788050649885909099",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1788050649885909099"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range May 6–12, 2024 (searched via keyword and semantic queries for events, speaking appearances, tours, or locations involving Charlie Kirk or TPUSA), are listed below in full without summarization.** Only posts matching the criteria are included; irrelevant or off-topic results were filtered out during retrieval.

### Posts from @charliekirk11 (Charlie Kirk's account):
- **Post ID: 1788946442398453773** (May 10, 2024, 14:57 GMT)  
  Content: "I just finished a record-setting campus tour with @TPUSA. The most students ever attending our events, and the most views ever online.  
  I got asked at almost every visit why Biden is banning TikTok. The ban is deeply unpopular with Gen Z. They think it shows Biden’s totalitarian impulse.  
  I decided to actively start posting there again about 6 weeks ago. My account now has 10 million views a day and I can tell you the impact is very real. Pro-American students are hungry for like-minded creators on TikTok.  
  Trump is growing in popularity with Gen Z, and this is another reason why."

- **Post ID: 1788227679046750497** (May 8, 2024, 15:21 GMT)  
  Content: "Last night at UW was a MASSIVE win for @TPUSA and for conservatives in the PNW! There were a few altercations with ANTIFA but they were proven to be a bunch of cowards. Our Prove Me Wrong tabling event was packed and our Live Free Tour event was standing room only.  
  Onward!! 🇺🇸"  
  Media: Two photos (event scenes at University of Washington).

- **Post ID: 1788057022153556050** (May 8, 2024, 04:03 GMT)  
  Content: "JUST IN—After a successful evening event and day of tabling, ANTIFA is attempting to intimidate our attendees as the event ends. They are mostly non-students the university should immediately deal with but for some reason allow to roam free and bully the student body."  
  Media: Video.

- **Post ID: 1788055154065080375** (May 8, 2024, 03:55 GMT)  
  Content: "Turning Point USA Reporter, Protesters Clash in Bloody Campus Melee  
  https://www.newsweek.com/turning-point-usa-reporter-protesters-clash-bloody-campus-melee-1898179"

- **Post ID: 1788034713049075817** (May 8, 2024, 02:34 GMT)  
  Content: "TPUSA Frontlines Reporter Violently Attacked by Antifa Militants at Charlie Kirk Event at University of Washington in Seattle (VIDEO)  
  https://www.thegatewaypundit.com/2024/05/tpusa-frontlines-reporter-violently-attacked-antifa-militants-charlie/"

- **Post ID: 1788024171714502712** (May 8, 2024, 01:52 GMT)  
  Content: "BREAKING: Violence erupts outside of Charlie Kirk University of Washington event as Antifa militants attack journalist  
  https://thepostmillennial.com/breaking-violence-erupts-outside-of-charlie-kirk-u-washington-event-as-antifa-militants-attack-journalist?utm_campaign=64501"

- **Post ID: 1788017247224799436** (May 8, 2024, 01:25 GMT)  
  Content: "Attendees are lined up at the University of Washington on the last stop of the Live Free Tour. Tonight is going to be packed and standing room only. Our movement is growing and thriving even in the PNW!  
  Let's go!  
  🇺🇸🇺🇸🇺🇸"  
  Media: Video.

### Posts from @TPUSA (Turning Point USA's account):
- **Post ID: 1788050649885909099** (May 8, 2024, 03:37 GMT)  
  Content: "At the University of Washington campus, the liberated zone has created a human barricade at the east entrance as they await the conclusion of our event, the Live Free Tour with @charliekirk11"  
  Media: Video.

- **Post ID: 1788023068348252539** (May 8, 2024, 01:48 GMT)  
  Content: "A FULL HOUSE for the Live Free Tour event tonight with @charliekirk11 at the University of Washington"  
  Media: Photo.

- **Post ID: 1788009913593287120** (May 8, 2024, 00:55 GMT)  
  Content: "Attendees are lined up and ready to hear from @charliekirk11 at the University of Washington on the last stop of the Live Free Tour 🇺🇸"  
  Media: Video.

- **Post ID: 1787972822318596127** (May 7, 2024, 22:28 GMT)  
  Content: "THE FRAT BOYS HAVE ARRIVED to chat with protesters at our Prove Me Wrong Tabling event w/ @charliekirk11"  
  Media: Video.

- **Post ID: 1787935542447063167** (May 7, 2024, 20:00 GMT)  
  Content: "Our PROVE ME WRONG tabling event with Charlie Kirk at @UW is underway!"  
  Media: Photo.

### Posts from other accounts referencing events:
- **Post ID: 1789422324346687559** (May 11, 2024, 22:28 GMT, @TerriGreenUSA)  
  Content: "If David French has no business speaking in front of the GA of the PCA, then riddle me this one. What business do Christians have in partnering with Charlie Kirk?  
  Dave Rubin with Charlie Kirk on the drug war and gay rights. Kirk calls it conservative libertarianism. Kirk platformed Rubin. Kirk says it’s all about freedom. Then they applaud Peter Thiel who spoke at the RNC in 2016 about being a gay republican."  
  Media: Video (multiple clips) and one photo.

- **Post ID: 1789339242222789049** (May 11, 2024, 16:58 GMT, @anatoliafergus)  
  Content: "The Antifa Army @UW during the @charliekirk11 event hosted by @TPUSA @KVIseattle @thehoffather @TPostMillennial .  
  The full image shows around 10 of them up against 1 student with a cell phone. Here they are showing their talent at making garbage can shields. It look to me like they have tied themselves onto it with rope. What happens if someone grabs the shield? 🧐"  
  Media: Photo.

- **Post ID: 1789306035368304743** (May 11, 2024, 14:46 GMT, @Tammy_K_Clark)  
  Content: "The People's Convention will be President Trump's signature rally-style event in MI this summer.  
  See discount codes TPUSA has generously created for MI grassroots organizations! You won’t want to miss this educational conference! Registration link: https://t.co/UOBbtVukgL"  
  Media: Photo.

- **Post ID: 1789296251252420770** (May 11, 2024, 14:07 GMT, @vaultus2250)  
  Content: "Antifa Gets Out of Control at Charlie Kirk UW Event, Find Out That Wasn't a Good Idea"

- **Post ID: 1788306509363126289** (May 8, 2024, 20:34 GMT, @charliekirk11 – included for completeness as it references the prior UW event)  
  Content: "Very fair article from last night.  
  The energy from the grassroots is palpable.  
  We must keep building.  
  Register voters.  
  Chase ballots.  
  Win."

- **Post ID: 1787965085161505042** (May 7, 2024, 21:57 GMT, @choeshow)  
  Content: "With tons of security, Antifa called in reinforcements. So far, none of the efforts have disrupted the TPUSA Charlie Kirk Q&A. The main event is this evening at 5:30pm. Tickets are already sold out. @FrontlinesTPUSA @TPUSA"  
  Media: Video.

- **Post ID: 1787945444905283900** (May 7, 2024, 20:39 GMT, @choeshow)  
  Content: "HAPPENING NOW: TPUSA’s Charlie Kirk is at the University of Washington campus in Seattle. Hundreds of students are outside the Husky Union Building. So far the Q&A has been respectful and lively. It’s early. @FrontlinesTPUSA @TPUSA"  
  Media: Video.

- **Post ID: 1788023993158783464** (May 8, 2024, 01:51 GMT, @choeshow)  
  Content: "HAPPENING NOW: Charlie Kirk TPUSA event is officially sold out at the University of Washington in Seattle. Unfortunately, people are being turned away. Thankfully these Antifa goons did not get inside. They are roaming on the outskirts of the HUB and are clearly here to intimidate the crowd. @TPUSA @FrontlinesTPUSA @charliekirk11"  
  Media: Video.

- **Post ID: 1787550036945162362** (May 6, 2024, 18:28 GMT, @choeshow)  
  Content: "Charlie is coming to UW on Tuesday. He does not capitulate to the woke mob. See you there. @TPUSA @charliekirk11 @FrontlinesTPUSA  
  https://thepostmillennial.com/gaza-camp-protesters-demand-charlie-kirk-event-be-canceled-at-university-of-washington"  
  (Note: This post is from May 6 and references the upcoming May 7 event.)

- **Post ID: 1788075611132715060** (May 8, 2024, 05:17 GMT, @choeshow)  
  Content: "The Charlie Kirk TPUSA event at UW was a smashing success Tuesday evening. But the crowd leaving is facing Antifa madness on the Quad."  
  Media: Video.

- **Post ID: 1787965907727434131** (May 7, 2024, 22:01 GMT, @TPostMillennial)  
  Content: "A heavy security presence has prevented Antifa thugs from disrupting Charlie Kirk’s Q&A session at the University of Washington."  
  Media: Video.

**Key observed event details across posts (for reference only; full text preserved above):**  
- **Live Free Tour / Prove Me Wrong events** at University of Washington (UW) in Seattle, WA: Tabling/Q&A during the day on May 7, 2024; main speaking event (sold out, standing room only) evening of May 7, 2024 (referred to as "last night" or "Tuesday evening" in May 8 posts). This was the final stop of the campus tour. Heavy security, Antifa protests/violence outside reported in multiple posts.  
- References to a broader "record-setting campus tour" completed by May 10, 2024.  
- Upcoming/future mention: TPUSA discount codes for "The People's Convention" (Trump rally-style event in Michigan, summer 2024) shared on May 11.  
- No other specific speaking locations or dates in the exact week range were detailed in the retrieved posts.

No additional matching posts were found in the searches. All content is reproduced verbatim from the tool results.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-05-06 to 2024-05-12**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-05-06 to 2024-05-12 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
