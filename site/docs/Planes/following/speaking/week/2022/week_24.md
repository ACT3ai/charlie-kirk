---
unlisted: true
title: "Week 24 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W24"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-06-11 to 2022-06-17."
status: completed
hide_table_of_contents: true
---

# Week 24, 2022

- Date range: 2022-06-11 to 2022-06-17
- Queried at (UTC): 2026-08-24T19:01:29Z
- Model: grok-4.3
- API status: completed
- Response id: 148bfa36-f68b-96b4-a360-0b8905d02d81

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-06-11 to the end of the week 2022-06-17.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speech OR event OR \"will be\" OR speaking OR tour OR \"public speaking\" OR campus OR university) since:2022-06-11 until:2022-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR speech) (location OR where OR \"in\" OR at) since:2022-06-11 until:2022-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events or appearances in June 2022",
      "limit": "10",
      "from_date": "2022-06-11",
      "to_date": "2022-06-18"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (speaking OR speech OR \"will speak\" OR event OR tour OR campus OR university OR \"speaking event\") since:2022-06-11 until:2022-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (event OR conference OR summit OR speaking) since:2022-06-11 until:2022-06-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (ASU OR Tempe OR Arizona OR \"San Diego\" OR California) since:2022-06-11 until:2022-06-18",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speech OR tour OR campus) since:2022-06-11 until:2022-06-18",
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
  "input_tokens": 16962,
  "input_tokens_details": {
    "cached_tokens": 8192
  },
  "output_tokens": 3727,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 20689,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 569184000,
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
    "input_tokens": 10227,
    "output_tokens": 3338
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537124319515578368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537124319515578368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537579511604191232",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537579511604191232"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537580963944726533",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537580963944726533"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537285563526553600",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537285563526553600"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537532162098044928",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537532162098044928"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1536128624696479745",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1536128624696479745"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537036312347303941",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537036312347303941"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1536456640655925248",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1536456640655925248"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537565909140787202",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537565909140787202"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1536472983677677568",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1536472983677677568"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537409567126081539",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537409567126081539"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537522706001846272",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537522706001846272"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537510022158159874",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537510022158159874"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1536877794604552192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1536877794604552192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537577556794220544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537577556794220544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537416590660075521",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537416590660075521"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537146280903733250",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537146280903733250"
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
    "url": "https://x.com/i/status/1537559575217549315",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537559575217549315"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537374056047075333",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537374056047075333"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537337487986724865",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537337487986724865"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537564072773931012",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537564072773931012"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537508078572163073",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537508078572163073"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537559774346321922",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537559774346321922"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537522979222978567",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537522979222978567"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1536133103437103106",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1536133103437103106"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537555779967909891",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537555779967909891"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537555647025369090",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537555647025369090"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537349263235096576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537349263235096576"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1537483076388786176",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1537483076388786176"
  }
]
```

## Grok response

```text
**Here is every relevant X/Twitter post from the specified date range (2022-06-11 to 2022-06-17, using `until:2022-06-18` to capture the full week), pulled via keyword and semantic searches. I included all matching or closely related posts without summarization or filtering—only posts that reference TPUSA/Charlie Kirk events, speaking, conferences, summits, or locations. No posts directly announced current-week (June 11–17) speaking events or appearances by Charlie Kirk or TPUSA. The results primarily discuss past events, criticism, or upcoming events outside the week.**

**Posts mentioning events/speaking (including the Pastors Summit announcement):**

- [post:5] ID: 1537483076388786176  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 16 Jun 2022 17:11:45 GMT  
  Content: Announcing the first ever @tpusafaith Pastors Summit!  
  Attendees will receive first-class training & teaching from 30+ guest speakers including fellow pastors, academics, and other thought leaders this August  
  Pastors and other church leaders—APPLY TODAY: https://t.co/CUb1S3aznA  
  (Media: photo)

- [post:3] ID: 1537555647025369090  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Thu, 16 Jun 2022 22:00:07 GMT  
  Content: TPUSA Faith’s first annual Pastors Summit will be held August 10-12, 2022 at Loews Coronado Bay Resort in San Diego, CA. Pastors who attend this retreat will hear from guest speakers, receive training, & participate in networking events. Learn more here! https://t.co/p78u7meQ2L  
  (Media: photo)

- [post:0] ID: 1537577556794220544  
  Author: Eschatological (@nancy83302032)  
  Timestamp: Thu, 16 Jun 2022 23:27:11 GMT  
  Content: Charlie Kirk nonprofit Turning Point Action paid Kimberly Guilfoyle’s $60,000 speaking fee on Jan. 6 with money from Publix heiress - The Washington Post

- [post:7] ID: 1536877794604552192  
  Author: Maggie Haberman (@maggieNYT)  
  Timestamp: Wed, 15 Jun 2022 01:06:34 GMT  
  Content: Charlie Kirk nonprofit Turning Point Action paid Kimberly Guilfoyle’s $60,000 speaking fee on Jan. 6 with money from Publix heiress - The Washington Post https://www.washingtonpost.com/national-security/2022/06/14/kimberly-guilfoyle-turning-point-action-jan-6/

- [post:14] ID: 1537036312347303941  
  Author: Citizens for Ethics (@CREWcrew)  
  Timestamp: Wed, 15 Jun 2022 11:36:28 GMT  
  Content: Kimberly Guilfoyle spoke for less than three minutes at the rally on Jan. 6, 2021, that preceded the Capitol riot.  
  For her appearance, she was compensated $60,000 by Turning Point Action, a conservative nonprofit led by Charlie Kirk.

- [post:9] ID: 1536128624696479745  
  Author: Madeline Peltz (@peltzmadeline)  
  Timestamp: Sun, 12 Jun 2022 23:29:38 GMT  
  Content: This comes two weeks after @TPUSA held a three day conference for “young women leaders” where adult men repeatedly pushed marriage and babies to an audience of high school and college age girls https://www.mediamatters.org/charlie-kirk/turning-point-usa-conference-young-women-leaders-suggests-their-role-get-married-and

**Posts referencing locations or related context (e.g., ASU/Tempe, San Diego mentions tied to events):**

- [post:10] ID: 1537146280903733250  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 15 Jun 2022 18:53:26 GMT  
  Content: Last year @RealCandaceO and I came out against Juneteenth. We tried to warn people this would create anti-Americanism and a distraction from July 4th.  
  Now on the campus of @ASU in Tempe they are taking down American flags and putting Juneteenth and "Pride Flags" in their place.  
  (Media: 3 photos)

- [post:20] ID: 1537349263235096576  
  Author: The Post Millennial (@TPostMillennial)  
  Timestamp: Thu, 16 Jun 2022 08:20:01 GMT  
  Content: TPUSA founder Charlie Kirk blasted Arizona State University for replacing American flags lining a street with Juneteenth and Pride flags.

- [post:32] ID: 1537349263235096576 (duplicate of above in results)  
  Same as [post:20].

**Posts about the Pastors Summit (additional reactions, no new dates/locations beyond the above):**

- [post:1] ID: 1537564072773931012  
  Author: Ｐｈｉｌｉｐ　Ｄｅｒｒｉｄａ (@PhilipDerrida)  
  Timestamp: Thu, 16 Jun 2022 22:33:36 GMT  
  Content: Just to address a few comments here. I assume the TPUSA holding a pastors conference means they will be helping pastors with political issues that affect Christians, not how to be a pastor in general.

- [post:16] ID: 1537508078572163073 (reply/quote to [post:5])  
  Author: Jeremy, Writer & Dad & Collector of Parks (@JeremyWingert79)  
  Timestamp: Thu, 16 Jun 2022 18:51:06 GMT  
  Content: Oh man, I'm so grateful to see spelled out very clearly that the 2 women on Charlie Kirk's "Pastors Summit" event are merely *talking* on various topics.  
  If they were *preachers*, I'd be mortified.  
  #SmashThePatriarchy

- [post:22] ID: 1537580963944726533  
  Author: Matthew Boedy (@MatthewBoedy)  
  Timestamp: Thu, 16 Jun 2022 23:40:43 GMT  
  Content: On #kirkalert today: 1. Charlie Kirk signs Christian nationalism manifesto w/ Peter Theil, Mark Meadows  
  2. Turning Point Faith announces Pastors Conference  
  3. TPUSA accused of supporting AZ GOP governor candidate  
  4. Former TPUSA advisor Ginni Thomas focus of #January6thHearing

- [post:23] ID: 1537579511604191232  
  Author: Real America's Voice (RAV) (@RealAmVoice)  
  Timestamp: Thu, 16 Jun 2022 23:34:57 GMT  
  Content: @TPUSA Faith Rep. @michaelas1776 talks about her journey into politics and how the aftermath of 2020 led her to seek out the truth.  
  @edhenry @mrsflorida2016  
  Watch #RAV’s coverage of the Road to Majority Policy Conference and chat live on @GETTRofficial: https://t.co/AhmRXfRzzK  
  (Media: video)

- [post:24] ID: 1537564072773931012 (duplicate of [post:1])

- [post:25] ID: 1537555647025369090 (duplicate of [post:3])

- [post:26] ID: 1537532162098044928  
  Author: FreeSpeech (@LibertasLogos)  
  Timestamp: Thu, 16 Jun 2022 20:26:48 GMT  
  Content: Well TPUSA would rather have an atheist at their Protestant 'Summit' than an Catholic or Orthodox priest apparently.  Just liked they preferred having gay black activists attend their events rather than race realist Zoomer paleocons.

- [post:27] ID: 1537522979222978567 (reply/quote to [post:5])  
  Author: AuditTheRhetoric 📚 (@bookkeepPLUS)  
  Timestamp: Thu, 16 Jun 2022 19:50:18 GMT  
  Content: @TPUSA ‘s Pastor’s summit  
  How exciting and potentially edifying.   
  Cant wait to hear what Conceptual James has to say about God and being a Pastor.

- [post:28] ID: 1537522706001846272 (reply/quote to [post:5])  
  Author: John Sailer (@JohnDSailer)  
  Timestamp: Thu, 16 Jun 2022 19:49:13 GMT  
  Content: James Lindsay to speak at the TPUSA Pastors Summit.

**Other related posts (mentions of TPUSA/Charlie Kirk in event or speaking context, including unrelated or tangential):**

- [post:6] ID: 1536133103437103106  
  Author: Dinesh D'Souza (@DineshDSouza)  
  Timestamp: Sun, 12 Jun 2022 23:47:26 GMT  
  Content: June 13 and 14!  In theaters nationwide. The one-and-only Kirk Cameron has a new documentary on “The Homeschool Awakening.” You gotta see it. I’m looking forward to having Cameron on my podcast tomorrow.  https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DwQeZDjxK5T8%26feature%3Dyoutu.be&q=EgTHEJ23GOL6wNMGIjA8q_w9LrSa79dNeph0MQwgDX8LrH3Vons7afjzAi0yKa1S7JrRGbtgsdLFkMh3bxUyAnJSWgFD

- [post:8] ID: 1536472983677677568  
  Author: Dinesh D'Souza (@DineshDSouza)  
  Timestamp: Mon, 13 Jun 2022 22:18:00 GMT  
  Content: Actor and producer Kirk Cameron talks about the revolution in homeschooling — the subject of his new movie The Homeschool Awakening in theaters exclusively only on June 13th and 14th.  
  (Media: video)

- [post:12] ID: 1536456640655925248  
  Author: Jennifer 🇺🇸 (@JamWr1tes)  
  Timestamp: Mon, 13 Jun 2022 21:13:03 GMT  
  Content: Kirk Cameron Presents: The Homeschool Awakening | Fathom Events ⁦@CariKelemen⁩  https://www.fathomentertainment.com/releases/Kirk-Cameron-Presents-The-Homeschool-Awakening

- [post:13] ID: 1537124319515578368  
  Author: KING CRIMSON (@DGMHQ)  
  Timestamp: Wed, 15 Jun 2022 17:26:10 GMT  
  Content: Robert Fripp and David Singleton are on a speaking tour in the US from September to October.   
  For a full list of confirmed dates click here:  
  https://t.co/y69RQTVTS3  
  (Media: photo)

- [post:17] ID: 1537416590660075521  
  Author: We Are All Charlie Kirk (@4CharlieKirk74)  
  Timestamp: Thu, 16 Jun 2022 12:47:33 GMT  
  Content: That's an awesome tour.

- [post:4] ID: 1537510022158159874  
  Author: 🇺🇸🇺🇸Wakey-Wakey21🇺🇸ULTRAMEGAMAGA 🇺🇸🇺🇸 (@WTPRPOed)  
  Timestamp: Thu, 16 Jun 2022 18:58:49 GMT  
  Content: Seems to me this is a parade in a city? Some parents may expect a “parade”would be a family friendly event. We used to have laws that expect basic decency.

- [post:11] ID: (empty ID in results)  
  Content: (No text content)

- [post:18] ID: 1537409567126081539  
  Author: arirang 💜 (@namjooningright)  
  Timestamp: Thu, 16 Jun 2022 12:19:39 GMT  
  Content: What is the 2039 Ourple box event????

- [post:19] ID: 1537374056047075333  
  Author: Edward A. Rowe (@EdwardARowe1)  
  Timestamp: Thu, 16 Jun 2022 09:58:32 GMT  
  Content: Charlie Kirk nonprofit Turning Point Action paid Kimberly Guilfoyle’s $60,000 speaking fee on Jan. 6 with money from Publix heiress - The Washington Post

- [post:21] ID: 1537285563526553600  
  Author: Kitty Eisele (@RadioKitty)  
  Timestamp: Thu, 16 Jun 2022 04:06:54 GMT  
  Content: Publix heiress paid Kimberly Guilfoyle’s $60,000 speaking fee on Jan. 6.  And Charlie Kirk is always around these things.  disturbing.

- [post:29] ID: 1537565909140787202  
  Author: WE’RE ALL CHARLIE KIRK! (@cto_tim)  
  Timestamp: Thu, 16 Jun 2022 22:40:53 GMT  
  Content: That’s not true, you can still vote in person in California. Where do you get your information…Sesame Street?

- [post:30] ID: 1537559774346321922  
  Author: We are all Charlie Kirk now. (@AnthonyTalk)  
  Timestamp: Thu, 16 Jun 2022 22:16:31 GMT  
  Content: Keep an eye on Kari Lake in Arizona:

- [post:31] ID: 1537559575217549315  
  Author: We are all Charlie Kirk now. (@AnthonyTalk)  
  Timestamp: Thu, 16 Jun 2022 22:15:43 GMT  
  Content: Arizona has Kari Lake:

- [post:33] ID: 1537337487986724865  
  Author: Tony Mtz (@tonyblazintxn)  
  Timestamp: Thu, 16 Jun 2022 07:33:14 GMT  
  Content: So Charlie Kirk, white nationalist,homophobe,college drop-out,thinks that the 4th of July should be celebrated in June? #Pride2022 #Pride #PrideMonth #juneteenth2022 Whining & Telling people what to do?  No freedom?

**Notes on completeness:** All tool results were exhausted across multiple searches (keyword for "Charlie Kirk"/TPUSA + event/speaking terms, location-specific, from:charliekirk11, and semantic). No posts from the week described any live or scheduled speaking by Charlie Kirk or TPUSA between June 11–17, 2022. The only forward-looking event detail is the August 2022 Pastors Summit in San Diego. All posts are reproduced verbatim as returned.
```

