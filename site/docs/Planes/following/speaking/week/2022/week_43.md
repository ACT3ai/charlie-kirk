---
unlisted: true
title: "Week 43 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W43"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-10-22 to 2022-10-28."
status: completed
hide_table_of_contents: true
---

# Week 43, 2022

- Date range: 2022-10-22 to 2022-10-28
- Queried at (UTC): 2026-08-24T19:04:08Z
- Model: grok-4.3
- API status: completed
- Response id: 7c7704a7-86b2-9934-8512-65c3779d68a1

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-10-22 to the end of the week 2022-10-28.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR speech OR event OR \"public speaking\" OR tour OR campus OR \"will be\" OR appearing OR appearance) since:2022-10-22 until:2022-10-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA) (event OR tour OR speaking OR campus) since:2022-10-22 until:2022-10-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, speeches, or where Charlie will speak between October 22 and October 28 2022",
      "limit": "10",
      "from_date": "2022-10-22",
      "to_date": "2022-10-28"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA) (event OR speaking OR speech OR speak OR campus OR tour) (UC Davis OR \"University of California\" OR Davis) since:2022-10-22 until:2022-10-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (UNM OR \"University of New Mexico\" OR Albuquerque) since:2022-10-22 until:2022-10-29",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 OR from:TPUSA since:2022-10-22 until:2022-10-29",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Turning Point\" OR TPUSA) (event OR speaking) (cancelled OR canceled OR cancel) since:2022-10-22 until:2022-10-29",
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
  "input_tokens": 20872,
  "input_tokens_details": {
    "cached_tokens": 9920
  },
  "output_tokens": 4872,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 25744,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 628540000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 7,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 12372,
    "output_tokens": 4448
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1583819213109882880",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1583819213109882880"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1584870324705038336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1584870324705038336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585646291207393282",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585646291207393282"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1584626546605973504",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1584626546605973504"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585749742423678977",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585749742423678977"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585736311998058496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585736311998058496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585307350113869824",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585307350113869824"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585778213204029440",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585778213204029440"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585020818324881408",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585020818324881408"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585714062159097856",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585714062159097856"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585654099243978755",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585654099243978755"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585771058619097091",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585771058619097091"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585756578874916864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585756578874916864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1584678069352005633",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1584678069352005633"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585731242770694145",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585731242770694145"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585766744123056128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585766744123056128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585305920245878788",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585305920245878788"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1583666369693765632",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1583666369693765632"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585763612672626691",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585763612672626691"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585731336467230720",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585731336467230720"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585642196476170242",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585642196476170242"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585754113559924737",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585754113559924737"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585716937325105152",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585716937325105152"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585695164625977348",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585695164625977348"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585479133466791937",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585479133466791937"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585760222475231232",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585760222475231232"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585775618569838592",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585775618569838592"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1584319251112161281",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1584319251112161281"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585736530278354946",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585736530278354946"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585743958042288128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585743958042288128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585692913492971520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585692913492971520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585721567291486209",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585721567291486209"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585758587686916097",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585758587686916097"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1583620415443718144",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1583620415443718144"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1583998205661831170",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1583998205661831170"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585729193706278912",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585729193706278912"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585761262046449664",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585761262046449664"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1583825817557090304",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1583825817557090304"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585732150808059904",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585732150808059904"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1585721364060590080",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1585721364060590080"
  }
]
```

## Grok response

```text
**Here is all the relevant X (Twitter) post data from the searches for the date range 2022-10-22 to 2022-10-28 (inclusive of posts up to 2022-10-28 23:59:59).** I used keyword searches for terms related to Charlie Kirk, TPUSA, speaking events, speeches, campus tours, and similar, plus semantic search. No posts were found that announce or detail **upcoming** public speaking events by Charlie Kirk himself or TPUSA chapters/speakers **within that exact week** (i.e., events scheduled for Oct 22–28, 2022). 

The results primarily reference:
- Past/recent events (e.g., a pro-life speech at UNM/University of New Mexico TPUSA chapter involving Ian Haworth and Tomi Lahren references, with security details).
- A TPUSA/MAGA Hulk event at UC Davis that faced protests, violence, and cancellation (around Oct 25–27, 2022).
- General discussions, no direct announcements of new events in the window.

All posts are included below in full (as retrieved; timestamps are GMT). Duplicates across searches are noted but listed once where possible. No Charlie Kirk or TPUSA official posts promoted speaking events in the target week.

### Posts from keyword searches (general + specific terms like "speaking", "event", "campus", "TPUSA"):
- **[post:0]** ID: 1585778213204029440  
  Author: nemik's bravest soldier 🇵🇸 - @RedRaxus  
  Timestamp: Thu, 27 Oct 2022 23:39:23 GMT  
  Content: The fact that TPUSA had a meltdown over the Minneapolis Marxist School and yet had nothing to say about the Phoenix School on their flagship campus. Also, "we EXPOSED these Marxists by INFILTRATING (i.e. attending) their public event that they were in no way trying to hide!"

- **[post:1]** ID: 1585775618569838592  
  Author: Cash Loren - @Cashloren  
  Timestamp: Thu, 27 Oct 2022 23:29:04 GMT  
  Content: Freedom of speech is essential for democracy.

- **[post:2]** ID: 1585771058619097091  
  Author: Higher Ed Dive - @HigherEdDive  
  Timestamp: Thu, 27 Oct 2022 23:10:57 GMT  
  Content: Updates: -Federal judge dismisses Seattle Pacific’s lawsuit against attorney general -Fight prompts UC Davis to cancel Turning Point USA event -New legislation would require colleges to report demographic information about endowment management https://www.highereddive.com/news/tracking-how-the-coronavirus-is-impacting-colleges/574858/

- **[post:3]** ID: 1585766744123056128  
  Author: Amelia Bancroft - @AmeliaBanc  
  Timestamp: Thu, 27 Oct 2022 22:53:48 GMT  
  Content: Oh are you referring to the protest to a Turning Point USA event that was disrupted and turned into a brawl by the Proud Boys? Doesn't sound like the "woke" students were the issue there.

- **[post:4]** ID: 1585761262046449664  
  Author: UltraMAGAdereck72 - @dereck72vapes  
  Timestamp: Thu, 27 Oct 2022 22:32:01 GMT  
  Content: Fight Breaks Out Amongst Protesters Causing TPUSA Event To Get CANCELLED... https://t.co/btc3svQ6tc via @YouTube

- **[post:5]** (Duplicate of post:0)

- **[post:6]** ID: 1585763612672626691  
  Author: Churchill - @Churchi15246971  
  Timestamp: Thu, 27 Oct 2022 22:41:21 GMT  
  Content: #Speaking too SOON! The #Scripture in my Spirit is "Be wise as a serpent. & harmless as a dove." For @charliekirk11 @StephenM @GOPChairwoman. You hv to #monitor the counting too; SAME 4 #Dems. Figure out Y this #Bible verse:)!

- **[post:7]** (Duplicate of post:4)

- **[post:8]** ID: 1585760222475231232  
  Author: FRONTLINES TPUSA - @FrontlinesTPUSA  
  Timestamp: Thu, 27 Oct 2022 22:27:53 GMT  
  Content: Catch this interview with UC Davis student who was maced on her own campus by ANTIFA. Exclusive on Real America’s Voice. 7:30PT/10:30ET. All watch links in bio!  
  (Media: Video)

- **[post:9]** ID: 1585758587686916097  
  Author: Vicki - @gojeffie24  
  Timestamp: Thu, 27 Oct 2022 22:21:23 GMT  
  Content: Violent Clashes Outside TPUSA Event at UC Davis

- **[post:10]** ID: 1585756578874916864  
  Author: Fred Owsley Let's Go Brandon DemocRats=KleptocRats - @owsley_fred  
  Timestamp: Thu, 27 Oct 2022 22:13:24 GMT  
  Content: Violent Clashes Outside TPUSA Event at UC Davis

- **[post:11]** ID: 1585754113559924737  
  Author: Real America's Voice (RAV) - @RealAmVoice  
  Timestamp: Thu, 27 Oct 2022 22:03:37 GMT  
  Content: What does the left do in desperation as power slips away? They get violent. TPUSA MAGA Hulk event targeted... Watch @RealDrGina #PrimeTime at 7pm ET with special guests @Stephend1776, @danielledsouzag, @ChrisNikic, and @Oscarelblue Watch LIVE➡ https://therokuchannel.roku.com/watch/5525024e9e8054d4ad1cf9fadbfcf8c8/americas-voice  
  (Media: Photo)

- **[post:12]** ID: 1585749742423678977  
  Author: Michaela - @1776MichaelaM  
  Timestamp: Thu, 27 Oct 2022 21:46:15 GMT  
  Content: What’s spookier than socialism?! Not being on campus with @NikkelleHudak! From witch’s brew to breaking TVs, there’s simply never a dull moment with Nikkelle and @AndrewSypher as we work with our @TPUSA leaders on campus. 🧙‍♀️⚡️💜  
  (Media: 4 items including photos and video)

- **[post:13]** ID: 1585743958042288128  
  Author: kiwi - @espressodoggy  
  Timestamp: Thu, 27 Oct 2022 21:23:15 GMT  
  Content: believed that protesting the event was in favor of promoting free speech by discouraging the spread of hateful ideas. At the end of the day we have freedom to protest because institutions that undermine freedom will always exist, even if you disagree that TPUSA is one of them.

### Additional posts from targeted keyword searches (UC Davis, UNM, cancellation, etc.):
- **[post:14]** ID: 1585020818324881408  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 25 Oct 2022 21:29:46 GMT  
  Content: Join myself and Kari Lake, Blake Masters, and Abe Hamadeh in Scottsdale on Saturday, November 5th to GOTV with Turning Point Action. Knock doors. Win elections.

- **[post:15]** ID: 1583620415443718144  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Sat, 22 Oct 2022 00:45:03 GMT  
  Content: It required 100+ campus security, UNM PD, and New Mexico State Police just for one pro-life speaker to address our TPUSA chapter. TPUSA will NEVER stop going right into their ideological strongholds. Thank God Ian and our students made it out safely.  
  (Quoted post references Ian Haworth's pro-life speech at UNM TPUSA/Students for Life event titled “How Men Can Fight For Life,” with protests/security.)

- **[post:16]** ID: 1583825817557090304  
  Author: Renee 🇺🇸 WE WILL NOT COMPLY - @reneeAZpatriot4  
  Timestamp: Sat, 22 Oct 2022 14:21:15 GMT  
  Content: 🇺🇸SAVE AMERICA RALLY🇺🇸 Saturday 10/22/22 7:00pm CDT Robstown, TX 2:00pm - Doors Open 4:00pm - Speakers Remarks 7:00pm - President Trump 👇WATCH HERE👇 Newsmax OANN Right Side Broadcasting on RUMBLE https://t.co/wDjAUSb1XS  
  (Media: Video)

- **[post:17]** ID: 1583819213109882880  
  Author: Democrats - @TheDemocrats  
  Timestamp: Sat, 22 Oct 2022 13:55:01 GMT  
  Content: On October 28, join @BarackObama in Atlanta, Georgia as he rallies voters and discusses what’s at stake in the midterm elections. We’re just 17 days from Election Day—let’s bring it home! RSVP now:

- **[post:18]** ID: 1585305920245878788  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Wed, 26 Oct 2022 16:22:39 GMT  
  Content: BREAKING: UC Davis cancels TPUSA event after female student attacked by far-left protesters https://thepostmillennial.com/uc-davis-cancels-tpusa-event-after-female-student-attacked-by-far-left-protesters

- **[post:19]** ID: 1583998205661831170  
  Author: Charles Campisi - @1813Doncarlo  
  Timestamp: Sun, 23 Oct 2022 01:46:16 GMT  
  Content: The obscene travesty continues: Trump held a hate rally in Corpus Christi, Texas, to whip up & throw red meat to his rabid MAGA cretins & loons, when he should be in a courtroom standing trial for obstruction, espionage, theft of government property, sedition & insurrection.

- **[post:20]** ID: 1585307350113869824  
  Author: Charlie Crist - @CharlieCrist  
  Timestamp: Wed, 26 Oct 2022 16:28:20 GMT  
  Content: I’m thrilled to be joining President @JoeBiden next Tuesday in Miami! Come rally with us as we gear up to mobilize Democrats in every corner of Florida — RSVP below.

- **[post:21]** ID: 1584870324705038336  
  Author: Charlie Crist - @CharlieCrist  
  Timestamp: Tue, 25 Oct 2022 11:31:45 GMT  
  Content: I’ll be live this morning on a few different networks to talk about our win on the debate stage last night. - 9:10 AM: @Morning_Joe - 9:40 AM: @GMA - 10:00 AM: @CNN - 10:30 AM: @FoxNews Hope you can tune in!

- **[post:22]** ID: 1584678069352005633  
  Author: Charlie Crist - @CharlieCrist  
  Timestamp: Mon, 24 Oct 2022 22:47:48 GMT  
  Content: I'm taking the debate stage soon to hold Ron DeSantis accountable for his failed leadership. Watch the #FLGovDebate LIVE at 7:00 PM ET at

- **[post:23]** ID: 1584319251112161281  
  Author: Charlie Crist - @CharlieCrist  
  Timestamp: Sun, 23 Oct 2022 23:01:59 GMT  
  Content: Join Karla Hernández for a virtual pre-debate rally with community leaders & grassroots supporters! https://twitter.com/i/broadcasts/1mrxmkdraoWGy

- **[post:24]** (Duplicate of post:8)

- **[post:25]** (Duplicate of post:9)

- **[post:26]** (Duplicate of post:10)

- **[post:27]** ID: 1585736530278354946  
  Author: Roy Cam - @Roy_Cam  
  Timestamp: Thu, 27 Oct 2022 20:53:45 GMT  
  Content: Violent Clashes Outside TPUSA Event at UC Davis

- **[post:28]** ID: 1585731336467230720  
  Author: Andy Ngo - @MrAndyNgo  
  Timestamp: Thu, 27 Oct 2022 20:33:06 GMT  
  Content: #Antifa are calling for an attack on a @TPUSA student tabling event at @sacstate. Antifa have been escalating their targeting of the conservative student group & have even assaulted students trying to get inside a TPUSA event at UC Davis. https://t.co/ecRNMUMkzZ  
  (Media: 4 photos)

- **[post:29]** ID: 1585731242770694145  
  Author: Connie Wohlford - @wohlford_connie  
  Timestamp: Thu, 27 Oct 2022 20:32:44 GMT  
  Content: Violent Clashes Outside TPUSA Event at UC Davis

- **[post:30]** ID: 1585695164625977348  
  Author: John OBrien - @johnob99  
  Timestamp: Thu, 27 Oct 2022 18:09:22 GMT  
  Content: Antifa, a Democrat supported violent group of thugs, causes mayhem again: Violent Clashes Outside TPUSA Event at UC Davis

- **[post:31]** ID: 1584626546605973504  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Mon, 24 Oct 2022 19:23:04 GMT  
  Content: "Tomi Lahren, her father, and several members of the TPUSA chapter were barricaded in a back room in the student union for 45 minutes while campus police called in reinforcements from the Albuquerque Police Department and the New Mexico State Police" https://t.co/BW2TKqUB5u

- **[post:32]** ID: 1583666369693765632  
  Author: NM505🇺🇸🇺🇸🇺🇸🇺🇸🇺🇸 - @T505411  
  Timestamp: Sat, 22 Oct 2022 03:47:40 GMT  
  Content: I’m so sorry this happened and I am ashamed that to say that I’m from Albuquerque! UNM is known to be a very liberal college though

- **[post:33]** (Duplicate of post:15; includes quoted thread on UNM TPUSA event)

- **[post:44]** ID: 1585771058619097091 (Duplicate of post:2)

- **[post:45]** (Duplicate of post:4)

- **[post:46]** ID: 1585721567291486209  
  Author: @armiak.bsky.social - @duboo  
  Timestamp: Thu, 27 Oct 2022 19:54:17 GMT  
  Content: An event at UC Davis featuring "MAGA HULK" organized by the rightwing group Turning Point USA was canceled Tuesday night after around 100 people clashed in a massive brawl. Some of those fighting "might have worn Proud Boys apparel."

- **[post:47]** ID: 1585646291207393282  
  Author: Nancy Willing - @nannyfat  
  Timestamp: Thu, 27 Oct 2022 14:55:10 GMT  
  Content: UC Davis event hosted by conservative student group Turning Point USA canceled after 100-person brawl breaks out https://t.co/ev1l2lynk2 via @SFGate

### Posts from Charlie Kirk (@charliekirk11) and TPUSA (@TPUSA) accounts (Oct 22–28, 2022):
These are the only ones retrieved in the date range from their accounts (none promote speaking events in the week):
- **[post:34]** ID: 1585736311998058496  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 20:52:52 GMT  
  Content: New Poll from InsiderAdvantage: Oz (R) 48% (+3) Fetterman (D) 45% Boom!

- **[post:35]** ID: 1585732150808059904  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 20:36:20 GMT  
  Content: NYC: Man hijacks city bus in broad daylight with two dozen passengers on board. Gov. Hochul: "I Don’t Know Why That’s So Important To You"

- **[post:36]** ID: 1585729193706278912  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Thu, 27 Oct 2022 20:24:35 GMT  
  Content: Calling conservatives fascists 🤝 advocating for fascism @jamesklug  
  (Media: Video)

- **[post:37]** ID: 1585721364060590080  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Thu, 27 Oct 2022 19:53:29 GMT  
  Content: Freedom of speech is not a “threat to democracy.”

- **[post:38]** ID: 1585716937325105152  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 19:35:53 GMT  
  Content: BREAKING: Daniel Mota Dos Reis has been arrested for allegedly breaking into Katie Hobbs' campaign HQ While screaming, "THIS IS MAGA COUNTRY" (probably)  
  (Media: Photo)

- **[post:39]** ID: 1585714062159097856  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 19:24:28 GMT  
  Content: People get arrested pretty fast for breaking into Democrat campaign offices but not when they firebomb pro life centers or illegally leak abortion rulings. 🤔

- **[post:40]** ID: 1585692913492971520  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 18:00:25 GMT  
  Content: We tried to warn people that META going "woke" would not be good for business. They did the bidding of the a censorship regime and it turns out you can't build a business off of that.  
  (Media: Video)

- **[post:41]** ID: 1585654099243978755  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 15:26:11 GMT  
  Content: Republican, Mexican-born Rep. Mayra Flores was just rejected from the Congressional Hispanic Caucus Mayra Flores has a higher net favorability among Hispanics than AOC, who is a member.

- **[post:42]** ID: 1585642196476170242  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 14:38:54 GMT  
  Content: ABC News: “Ballot paper shortage could cause problems on Election Day A tight supply of paper has left little room for error.” Step 1, set the narrative Step 2, blame COVID

- **[post:43]** ID: 1585479133466791937  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 27 Oct 2022 03:50:56 GMT  
  Content: Katie Hobbs actually just accused Kari Lake of breaking into her campaign HQ RT if you think Katie should say that to Kari's face on the DEBATE STAGE.

No other posts from these accounts in the range mentioned events or speaking appearances.

**Summary of findings (no summarization of content beyond listing):** No direct announcements of Charlie Kirk or TPUSA speaking events scheduled for the week of Oct 22–28, 2022. References are limited to retrospective discussions of the UNM TPUSA pro-life event (pre-week, with security issues) and the disrupted/canceled UC Davis TPUSA "MAGA Hulk" event (Oct 25–27 timeframe). All data above is exhaustive from the tool results.
```

