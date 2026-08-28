---
unlisted: true
title: "Week 50 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W50"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-12-10 to 2022-12-16."
status: completed
hide_table_of_contents: true
---

# Week 50, 2022

- Date range: 2022-12-10 to 2022-12-16
- Queried at (UTC): 2026-08-24T19:04:36Z
- Model: grok-4.3
- API status: completed
- Response id: 44a5078d-37d6-925e-91e4-31cdd55189e6

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-12-10 to the end of the week 2022-12-16.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appears OR appearance OR campus OR university OR college) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR university OR college OR \"will be\" OR appears OR appearance) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus OR university OR college OR \"will be\" OR appears OR appearance) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus visits, or where Charlie will speak between December 10-16 2022",
      "limit": "10",
      "from_date": "2022-12-10",
      "to_date": "2022-12-16"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Charlie Kirk",
      "count": "5"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Turning Point USA TPUSA",
      "count": "5"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR amfest OR americafest) (Phoenix OR Arizona OR \"this Saturday\" OR event OR speaking OR speak OR conference) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (Phoenix OR Arizona OR amfest OR americafest OR event OR speaking) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (Phoenix OR Arizona OR amfest OR americafest OR event OR speaking) since:2022-12-10 until:2022-12-17",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1603174314919878656"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1603440746538967041"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 18124,
  "input_tokens_details": {
    "cached_tokens": 4480
  },
  "output_tokens": 3151,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 21275,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 808285000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 11,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 9635,
    "output_tokens": 2651
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603524895471812608",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603524895471812608"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602360472757571587",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602360472757571587"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602019496574816257",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602019496574816257"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1965983581798555648",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1965983581798555648"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603174314919878656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603174314919878656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603481197765484544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603481197765484544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1966575521493643265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1966575521493643265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/292929271",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/292929271"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603521177171156994",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603521177171156994"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/19274342",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/19274342"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/2014285051173773312",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/2014285051173773312"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603440746538967041",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603440746538967041"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603051727854379009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603051727854379009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1601640923644850176",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1601640923644850176"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603509484105580544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603509484105580544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603497406007500809",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603497406007500809"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602452218556186624",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602452218556186624"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603493298634645521",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603493298634645521"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602425701080207360",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602425701080207360"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602064146391965697",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602064146391965697"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1601699751384453120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1601699751384453120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603516789509324801",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603516789509324801"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602706148968251393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602706148968251393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603538131806027777",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603538131806027777"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603486117721886721",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603486117721886721"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1603538432076259328",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1603538432076259328"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1602823035228016640",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1602823035228016640"
  }
]
```

## Grok response

```text
**All relevant X/Twitter posts from December 10–16, 2022 (searched via keyword and semantic tools across the specified date range, including from @charliekirk11, @TPUSA, and general mentions). No summarization—raw posts only, presented in chronological order where possible based on timestamps. No other events (e.g., campus visits or additional speaking dates) were found in the results for this exact week.**

### Posts from December 10, 2022 (Saturday):
- **@TPUSA** (ID: 1601640923644850176, Timestamp: Sat, 10 Dec 2022 18:12:07 GMT)  
  Content: 🚨New Speaker Drop Alert🚨  
  Wait... there's MORE?!  
  Let the anticipation begin.  
  Use code "AZLOCAL" for $20 GA & a free concert 🇺🇸  
  🔗https://t.co/6ToIQO74He  
  (Media: Photo)

- **@charliekirk11** (ID: 1601699751384453120, Timestamp: Sat, 10 Dec 2022 22:05:53 GMT)  
  Content: BREAKING: The State Republican Executive Committee of Texas joins the Arizona GOP in "unanimously expressing no confidence" in Ronna McDaniel as RNC Chair, calls for new leadership.

### Posts from December 11, 2022 (Sunday):
- **@IamBrookJackson** (ID: 1602019496574816257, Timestamp: Sun, 11 Dec 2022 19:16:26 GMT)  
  Content: 🚨  
  INAUGURAL MEDICAL FREEDOM LEGAL SYMPOSIUM: Strategies for Overcoming Tyranny  
  DATE: DEC. 12, 2022 6:00PM EST  
  SESSION 1:  
  Military Law•Disability Law•Domestic Relations Law•The Griner Case•Definition of a Vaccine  
  HOSTS: Dr. Vliet & Warner Mendenhall  
  https://t.co/Y1dCTQTSP0  
  (Media: Photo)

- **@charliekirk11** (ID: 1602064146391965697, Timestamp: Sun, 11 Dec 2022 22:13:52 GMT)  
  Content: “Transgender” Navy SEAL Chris Beck has announced he made a mistake and that transitioning “destroyed my life.” How many children will be saying the same thing in 10 years if we don’t stop this madness now?

### Posts from December 12, 2022 (Monday):
- **@ScottPresler** (ID: 1602360472757571587, Timestamp: Mon, 12 Dec 2022 17:51:21 GMT)  
  Content: Here’s my 2023 schedule, so far:  
  February  
  4: Delaware County, PA  
  18: Rochester, NY  
  22: Charlotte, NC  
  March  
  1-4: CPAC  
  Priority states include:  
  ✔️KY & LA (governorships)  
  ✔️NJ & VA (state legislatures)  
  ✔️PA & WI (state Supreme Courts)

- **@CoachTReed** (ID: 1602425701080207360, Timestamp: Mon, 12 Dec 2022 22:10:33 GMT)  
  Content: Come support your JSU Tigers vs Texas Longhorns December 14 @ 11:00a AT JACKSON STATE UNIVERSITY. This will be an unforgettable experience. We will host our local elementary, middle and high schools during this game. Come catch the excitement. WE NEED YOU TO PACK THE HOUSE!  
  (Media: Photo)

- **@charliekirk11** (ID: 1602452218556186624, Timestamp: Mon, 12 Dec 2022 23:55:55 GMT)  
  Content: BREAKING: Loudoun County's ex-school superintendent and his spokesman have been indicted for lying to the public after a boy wearing a skirt raped a female student in the girl's bathroom. School officials had the victim's father arrested when he protested about it.

### Posts from December 13, 2022 (Tuesday):
- **@TWlegion** (ID: 1602706148968251393, Timestamp: Tue, 13 Dec 2022 16:44:57 GMT)  
  Content: 🚨Tiger Woods & Charlie Woods are both listed on the interview schedule for Friday at 2 PM at the PNC

- **@charliekirk11** (ID: 1602823035228016640, Timestamp: Wed, 14 Dec 2022 00:29:25 GMT)  
  Content: Interracial marriage has been fully legal in the United States since 1967. Same-sex marriage has been legal since 2015. There are only two possible outcomes of the RFRA:  
  1. It will do nothing.  
  2. Christians will be legally harassed for their beliefs.  
  Guess which is more likely.

### Posts from December 14, 2022 (Wednesday):
- **@charliekirk11** (ID: 1603051727854379009, Timestamp: Wed, 14 Dec 2022 15:38:09 GMT)  
  Content: Instead, Mitch McConnell is telling the lead negotiators to finish no later than December 22, because he intends “to be on the road going home” on December 23. I guess stopping human trafficking, millions of illegals and 100k OD deaths per year is less important than a vacation.

- **@charliekirk11** (ID: 1603174314919878656, Timestamp: Wed, 14 Dec 2022 23:45:16 GMT)  
  Content: https://www.amfest.com/  
  Join us in Phoenix, Arizona THIS SATURDAY for the largest event in the conservative movement. 🇺🇸🔥  
  (Media: Photo)  
  *Thread context/replies include:*  
  - @Highway_30 (Dec 15): Maybe I should just pop up. #Godspeed  
  - @slave_2_liberty (Dec 15): Yuge  
  - @AriDrennen (Dec 15): Hey Charlie, why are you giving discounted hotel rooms to 16 year olds, what's that about?

### Posts from December 15, 2022 (Thursday):
- **@AriDrennen** (ID: 1603440746538967041, Timestamp: Thu, 15 Dec 2022 17:23:59 GMT)  
  Content: Next week is TPUSA's annual AmericaFest conference, featuring speeches from Charlie Kirk, Matt Walsh, Candace Owens, and other right wing figures fueling a panic about alleged "grooming" by LGBTQ activists. TPUSA is providing discounted hotel rooms for 16 year olds to be there.  
  (Media: Photo)  
  *Thread context/replies include:*  
  - @AriDrennen (follow-up): A teenager attending AmericaFest can hear speeches from Tim Pool, James Lindsay, and other leading figures in spreading the "groomer" slander against LGBTQ people — as well as Matt Gaetz, who recently faced allegations he had sex with a 17-year-old in exchange for money.  
  - @newsrepertoire (Dec 15): The fact that not even Adult VIPs can get a discounted hotel room is definitely weird

- **@jonnhy_jme** (ID: 1603538432076259328, Timestamp: Thu, 15 Dec 2022 23:52:09 GMT)  
  Content: Members of NFSC Are departing to AMFEST 2022 In Phoenix, Arizona  
  NFSC 成员将启程前往亚利桑那州凤凰城参加 2022 年 AMFEST  
  #AMERICAFEST #NFSC #USA #Phoenix  
  (Media: 3 photos)

- **@BettyLies** (ID: 1603524895471812608, Timestamp: Thu, 15 Dec 2022 22:58:21 GMT)  
  Content: James Lindsay will be making a presentation at TPUSA’s AmericaFest conference, which is offering discounted rooms to 16-year-olds. Shocker.  
  (In reply to the Ari Drennen post above)

- **@DCAtomy** (ID: 1603521177171156994, Timestamp: Thu, 15 Dec 2022 22:43:35 GMT)  
  Content: Protest Day 26: We will be here for at least 90 days and will not compromise until the people who collaborate with the CCP pay their price.  
  (Media: Video)

- **@BrodyLevesque** (ID: 1603509484105580544, Timestamp: Thu, 15 Dec 2022 21:57:07 GMT)  
  Content: WASHINGTON – A decade ago, Charlie Kirk founded Turning Point USA, whose stated intent is playing “offense with a sense of urgency to win America’s culture war” on high school and college campuses.

- **@anthony70685949** (ID: 1603497406007500809, Timestamp: Thu, 15 Dec 2022 21:09:07 GMT)  
  Content: I'm against illegal immigration, but these people are coming from places in the world where communism is the rule is it possible I'm just saying is it possible that these people will be more conservative than we will be?

- **@PostaDiFalcone** (ID: 1603493298634645521, Timestamp: Thu, 15 Dec 2022 20:52:48 GMT)  
  Content: Turning Point USA: Can College Students Recite The Pledge of Allegiance? Can College Students Recite The Pledge of Allegiance?  
  🔵 AMFEST2022 REGISTRATION: https://bit.ly/3gi53YK  
  🇺🇸 Subscribe to the channel ►https://t.co/L99h2q9p6P  
  🇺🇸 TurningPoi…

- **@m1nu73m3n** (ID: 1603486117721886721, Timestamp: Thu, 15 Dec 2022 20:24:16 GMT)  
  Content: Turning Point USA: Can College Students Recite The Pledge of Allegiance?

- **@Kelly27Ms** (ID: 1603481197765484544, Timestamp: Thu, 15 Dec 2022 20:04:43 GMT)  
  Content: @jimmyjohns  
  So you’re speaking at Turning Point…No more Jimmy John’s for me or my family. Not canceling just using the power of my dollar. I’ll support someone else because I am disgusted by Charlie Kirk and the things he has done and said.

- **@shelly35160** (ID: 1603538131806027777, Timestamp: Thu, 15 Dec 2022 23:50:57 GMT)  
  Content: Charlie Kirk DESTROYS College Student's "White Privilege" Argument https://t.co/vMw6K8TBxV via @YouTube

- **@CDennig** (ID: 1603516789509324801, Timestamp: Thu, 15 Dec 2022 22:26:09 GMT)  
  Content: College kid ziocon gatekeepers. Charlie Kirk has moved a little to the right, but only after getting Groyped really hard. Difficult to tell if his changes are genuine, or if he's just good at seeing which way the wind blows.

### No additional posts found for December 16, 2022, in the search results.  
**Notes on completeness:**  
- Searches targeted mentions of events, speaking, tours, campuses, Phoenix/Arizona, AMFEST/AmericaFest, and direct posts from @charliekirk11/@TPUSA.  
- The primary event referenced across posts is **TPUSA’s AmericaFest 2022 conference in Phoenix, Arizona, on Saturday, December 17, 2022** (promoted by Charlie Kirk and @TPUSA with speaker drops and registration links). Speakers mentioned in context: Charlie Kirk, Matt Walsh, Candace Owens, Tim Pool, James Lindsay, Matt Gaetz.  
- No other specific Charlie Kirk or TPUSA speaking events, campus appearances, or locations were identified in the December 10–16, 2022, window.  
- All data pulled directly from tool results; posts include full text, media notes where present, and relevant thread context.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-12-10 to 2022-12-16**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-12-10 to 2022-12-16 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
