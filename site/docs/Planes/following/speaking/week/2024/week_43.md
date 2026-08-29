---
unlisted: true
title: "Week 43 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W43"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-10-21 to 2024-10-27."
status: completed
hide_table_of_contents: true
---

# Week 43, 2024

- Date range: 2024-10-21 to 2024-10-27
- Queried at (UTC): 2026-08-24T19:15:20Z
- Model: grok-4.3
- API status: completed
- Response id: c35772e8-a138-903b-9400-2d3336b63561

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-10-21 to the end of the week 2024-10-27.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2024-10-21 until:2024-10-28",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2024-10-21 until:2024-10-28",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2024-10-21 until:2024-10-28",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between October 21-27 2024",
      "limit": "10",
      "from_date": "2024-10-21",
      "to_date": "2024-10-28",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 10992,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 2394,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 13386,
  "num_sources_used": 0,
  "num_server_side_tools_used": 4,
  "cost_in_usd_ticks": 364994000,
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
    "input_tokens": 9402,
    "output_tokens": 2145
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848751316446634161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848751316446634161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850319865640333816",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850319865640333816"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850304284723954068",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850304284723954068"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850295133998387576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850295133998387576"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848766526997889139",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848766526997889139"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850314577554342347",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850314577554342347"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850310262454362525",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850310262454362525"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848795541527810396",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848795541527810396"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850304477020201180",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850304477020201180"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849541084277506206",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849541084277506206"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850289301596283126",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850289301596283126"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849220852287500763",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849220852287500763"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849630624685908104",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849630624685908104"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848504708303859749",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848504708303859749"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849201351537901962",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849201351537901962"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850281900860182855",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850281900860182855"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848842953411748002",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848842953411748002"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849571576678842685",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849571576678842685"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850252804709101949",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850252804709101949"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850232846012837934",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850232846012837934"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849128531151720745",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849128531151720745"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1848843803383447938",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1848843803383447938"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850306180674965946",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850306180674965946"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1849168462263792016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1849168462263792016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1850296388695019836",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1850296388695019836"
  }
]
```

## Grok response

```text
**All relevant X posts from the search (Oct 21–27, 2024 date range) mentioning Charlie Kirk or TPUSA public speaking events, appearances, or speaking locations are included below in full (no summarization).** These cover campus events, tours, rallies, and related activity. Irrelevant or non-event posts from the results are excluded. All data is pulled directly from the tool results.

### From @charliekirk11 (official account):
- **Post ID: 1848795541527810396** (Oct 22, 2024, ~18:36 GMT)  
  Content: "University of Georgia showed up today!! The Gen Z campus energy is insane. Just look at that sea of red. My message: VOTE NOW Go Dawgs!! 🐶"  
  (Media: Multiple photos/videos of the large crowd at the event.)

- **Post ID: 1848766526997889139** (Oct 22, 2024, ~16:41 GMT)  
  Content: "Realtime poll at our Prove Me Wrong event at the University of Georgia. Harris Walz vs Team Sanity. Team blue down hard. Let’s go Georgia!! 🇺🇸🇺🇸"  
  (Media: Video of the event/poll.)

- **Post ID: 1849630624685908104** (Oct 25, 2024, ~01:54 GMT)  
  Content: "Mel Gibson is voting for Trump: 'I know what it will be like with her, and it ain’t good.' 'Miserable track record, no policies to speak of, and she’s got the IQ of a fence post.' No lies detected."  
  (Media: Video; this is a clip from a speaking appearance, but no new event location specified.)

- **Post ID: 1849201351537901962** (Oct 23, 2024, ~21:28 GMT)  
  Content: "🚨ATTENTION LAS VEGAS 🚨 We have put together a historic team to rally support for President Trump in the Silver State!! TOMORROW, Thursday Oct. 24th Confirmed Speakers: @realDonaldTrump @TulsiGabbard @VivekGRamaswamy @marcorubio @DanicaPatrick @GamebredFighter @ginacarano @JackPosobiec @sambrownusa @delbigtree @BobGOYA1 @MichaelMcD_Real @Chattah4Nevada @SetemaGali Tickets 👉"  
  (Mentions upcoming rally with Charlie Kirk implied via context; no direct link in post.)

- **Post ID: 1850281900860182855** (Oct 26, 2024, ~21:02 GMT)  
  Content: "At the beginning of this year, I committed to all of you I would do more and worker harder than ever before to help us win. Below is the pace we set last week alone including: - 2 Trump rallies (Georgia and Nevada) - 3 pastor events with 500+ pastors in GA, MI, and CT - 9 campus events and Prove Me Wrong tabling events in GA, NV, WA, TN, NC, WV - 61 “super chase” door knocking and ballot chasing events in swing states - 500 volunteer ballot chasers trained in AZ and WI - 80,000+ low propensity ballots were successfully chased by our army of ballot chasers in AZ alone. See our day-by-day schedule👇. 🇺🇸🇺🇸 MONDAY, OCTOBER 21st * Morning: Charlie Kirk and Vivek Ramaswamy at Georgia State University in downtown Atlanta with 1,000+ students. * Afternoon: Charlie Kirk and Vivek Ramaswamy at UNC-Chapel Hill with 2,000+ students. * Afternoon: TPUSA brought Leigh Allyn Baker to West Virginia University for 400+ students. * TP Action trained ~100 'Commit 100' volunteers who will chase ballots in swing states through Election Day. * TP Action hosted 9 'Super Chase' door-knocking & ballot-chasing events in swing states. * 3,544 ballot returns by low-propensity voters targeted by TP Action ballot chasers in just Arizona. TUESDAY, OCTOBER 22nd * Morning: Charlie Kirk at University of Georgia with 4,000+ students. * Evening: Charlie Kirk spoke in Omaha, mobilizing 1,000 patriots for victory. * Evening: TPUSA brought Rob Schneider to Grand Canyon University for 500+ students. * Evening: TPUSA brought Riley Gaines to University of Tennessee-Knoxville for 400+ students. * TP Action trained ~100 'Commit 100' volunteers who will chase ballots in swing states through Election Day. * TP Action hosted 9 'Super Chase' door-knocking & ballot-chasing events in swing states. * 8,398 ballot returns by low-propensity voters targeted by TP Action ballot chasers in just Arizona. WEDNESDAY, OCTOBER 23rd * Morning: TPUSA hosted our 'Southeast Pastor Summit' for 500+ pastors and faith leaders. * Afternoon: TP Action hosted President Trump at our 'Georgia for Trump' rally in metro Atlanta with 12,000+ attendees (and 5,000 more outside). * Evening: TPUSA brought Vivek Ramaswamy to Oakland University for 1,000+ students. * TPUSA Faith hosted a pastor roundtable in Connecticut with former Congressman Bob McEwen. * TP Action trained ~100 'Commit 100' volunteers who will chase ballots in swing states through Election Day. * TP Action hosted 14 'Super Chase' door-knocking & ballot-chasing events in swing states. * 18,635 ballot returns by low-propensity voters targeted by TP Action ballot chasers in just Arizona. THURSDAY, OCTOBER 24th * Morning: Charlie Kirk at University of NV-Las Vegas campus with 1,500+ students. * Morning: TPUSA brought Brandon Tatum to the University of Washington for 500 students. * Afternoon: TP Action hosted President Trump at our 'United for Change' rally in Las Vegas with 12,500+ attendees. * TP Action trained ~100 'Commit 100' volunteers who will chase ballots in swing states through Election Day. * TP Action hosted 16 'Super Chase' door-knocking & ballot-chasing events in swing states. * 19,244 ballot returns by low-propensity voters targeted by TP Action ballot chasers in just Arizona. FRIDAY, OCTOBER 25th * TPUSA Faith hosted 100+ Indiana/Michigan pastors for our final 'Clear Truth' gathering. * TP Action hosted 13 'Super Chase' door-knocking & ballot-chasing events in swing states. * TP Action trained ~100 'Commit 100' volunteers who will chase ballots in swing states through Election Day."  
  (Full detailed schedule of events for the week, including Charlie Kirk speaking appearances.)

### From @TPUSA (official account):
- **Post ID: 1848504708303859749** (Oct 21, 2024, ~23:20 GMT)  
  Content: "A PACKED HOUSE for the You're Being Brainwashed Tour stop at The University of North Carolina at Chapel Hill with @charliekirk11 and @VivekGRamaswamy! @tpusastudents"  
  (Media: Photo of the packed event.)

- **Post ID: 1849220852287500763** (Oct 23, 2024, ~22:46 GMT)  
  Content: "Today at a @tpusastudents tabling event at UC Berkeley with Chloe Cole and Harrison Tinsley, this individual threw a full bottle of tomato juice all over the TPUSA chapter members, staff, and their table. @Harrisontinz @chloecole VC: @uhneti"  
  (Media: Video of the incident at the tabling/speaking-related event.)

- **Post ID: 1849541084277506206** (Oct 24, 2024, ~19:58 GMT)  
  Content: "CURRENT SCENE at the University of Nevada, Las Vegas You’re Being Brainwashed Tour Stop ft. @charliekirk11 & @TulsiGabbard 🇺🇸 @tpusastudents"  
  (Media: Photo of the current scene at the event.)

### Other user posts mentioning events:
- **Post ID: 1850319865640333816** (Oct 26, 2024, ~23:33 GMT, by @BuckDefi)  
  Content: "rah @koorah @nickmeta Charlie Kirk and Vivek are coming to my campus this Thursday. Imma have all the homies where POX written in them with signs and try to get on a TikTok clip😂"  
  (Mentions upcoming Charlie Kirk campus event on Thursday—likely referring to a future date beyond the range, but posted in-range.)

- **Post ID: 1850314577554342347** (Oct 26, 2024, ~23:12 GMT, by @GingerSnappiest)  
  Content: "I just received notification of a $47 payment from @theamericapac for forwarding the petition to my buddy who went to the Duluth, GA @TPUSA event with me. Didn't even realize they were doing that. @elonmusk That notification came 3 days after she signed upon the petition, and THANKS!"  
  (Mentions attendance at a recent Duluth, GA TPUSA event.)

- **Post ID: 1850304477020201180** (Oct 26, 2024, ~22:32 GMT, by @Politasports1)  
  Content: "The @charliekirk11 / @TPUSA campus talks are great. He is patient and gives opposing facts. Liberal kids have NEVER heard/had opposition. Conservative kids get it everywhere. But not libkids. All the BS is reenforced at home, school, and media. Its wrking Kirk. Keep it up. #MAGA"  
  (General praise for campus talks/events.)

This constitutes **all** matching data from the searches for the specified week. No additional relevant posts appeared in the results.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-10-21 to 2024-10-27**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-10-21](/Planes/Incidents/N582MM-2024-10-21-KATL) | [N582MM](/Planes/N582MM/overview) | [KATL](/Planes/Airports/KATL) | Atlanta, GA | Charlie | **Same day** |
| [2024-10-21](/Planes/Incidents/N582MM-2024-10-21-KRDU) | [N582MM](/Planes/N582MM/overview) | [KRDU](/Planes/Airports/KRDU) | Chapel Hill, NC | Charlie | **Same day** |
| [2024-10-22](/Planes/Incidents/N582MM-2024-10-22-KRDU) | [N582MM](/Planes/N582MM/overview) | [KRDU](/Planes/Airports/KRDU) | Chapel Hill, NC | Charlie | Day after |
| [2024-10-23](/Planes/Incidents/N582MM-2024-10-23-KLZU) | [N582MM](/Planes/N582MM/overview) | [KLZU](/Planes/Airports/KLZU) | Lawrenceville, GA | Charlie | **Same day** |
| [2024-10-24](/Planes/Incidents/N582MM-2024-10-24-KLAS) | [N582MM](/Planes/N582MM/overview) | [KLAS](/Planes/Airports/KLAS) | Las Vegas, NV | Charlie | **Same day** |
| [2024-10-24](/Planes/Incidents/N582MM-2024-10-24-KLZU) | [N582MM](/Planes/N582MM/overview) | [KLZU](/Planes/Airports/KLZU) | Lawrenceville, GA | Charlie | Day after |
| [2024-10-27](/Planes/Incidents/N582MM-2024-10-27-KSDL) | [N582MM](/Planes/N582MM/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day before |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
