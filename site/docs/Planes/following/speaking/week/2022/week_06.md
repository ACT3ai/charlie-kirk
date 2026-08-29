---
unlisted: true
title: "Week 06 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W06"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-02-05 to 2022-02-11."
status: completed
hide_table_of_contents: true
---

# Week 06, 2022

- Date range: 2022-02-05 to 2022-02-11
- Queried at (UTC): 2026-08-24T18:59:14Z
- Model: grok-4.3
- API status: completed
- Response id: 15cc83bf-4e15-94cd-8cd3-a3d9623372e6

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-02-05 to the end of the week 2022-02-11.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR speaks) since:2022-02-05 until:2022-02-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance) since:2022-02-05 until:2022-02-12 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak",
      "limit": "10",
      "from_date": "2022-02-05",
      "to_date": "2022-02-12"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\" OR @TPUSA) (event OR speaking OR speak OR tour OR appearance OR \"will speak\" OR \"speaking at\" OR \"Charlie will be\") since:2022-02-05 until:2022-02-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus OR college OR university) since:2022-02-05 until:2022-02-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"Charlie Kirk\") since:2022-02-05 until:2022-02-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk speaking at events or TPUSA events in February 2022",
      "limit": "10",
      "from_date": "2022-02-05",
      "to_date": "2022-02-12"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 19612,
  "input_tokens_details": {
    "cached_tokens": 10176
  },
  "output_tokens": 5658,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 25270,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 629752000,
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
    "input_tokens": 10817,
    "output_tokens": 5239
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1491108961604730881",
    "start_index": 311,
    "end_index": 372,
    "title": "1"
  }
]
```

## Grok response

```text
**No posts were found directly from Charlie Kirk (@charliekirk11) or the official @TPUSA account announcing or detailing his personal public speaking events, appearances, or locations where he would speak during the date range February 5–11, 2022 (using the `until:2022-02-12` cutoff for the end of the week).**[[1]](https://x.com/charliekirk11/status/1491108961604730881)

Searches across keyword, advanced filters (including links and from: specific accounts), and semantic queries for relevant terms like events, speaking, tours, appearances, campus/college events, or "Charlie will be" yielded no matching announcements from those core accounts in the period.

### Related Posts from the Search Period
Here are **all** relevant posts returned from the searches (including any tangential mentions of TPUSA/Charlie Kirk events or speaking). These are presented verbatim with full metadata—no summaries or omissions. Most discuss other TPUSA-related activities, criticism, or unrelated events.

- **[post:0] ID: 1491920249620340736**  
  **Author:** Stanford Turning Point USA - @Stanford_GOP  
  **Timestamp:** Thu, 10 Feb 2022 23:41:20 GMT  
  **Content:** TICKETS FOR VICE PRESIDENT MIKE PENCE AT STANFORD OPEN TO PUBLIC 👇👇👇  
  Tickets to our event featuring Vice President @Mike_Pence are now open to members of the community and the general public! To reserve a ticket use the promo code “SCRCOMMUNITY”.  
  https://www.eventbrite.com/e/how-to-save-america-from-the-woke-left-tickets-255591289427  
  @yaf  
  **Engagement:** Likes=120, Reposts=20, Quotes=22, Replies=162, Bookmarks=2, Views=N/A

- **[post:1] ID: 1491915120460533762**  
  **Author:** World Over Easy - @tacotime05  
  **Timestamp:** Thu, 10 Feb 2022 23:20:57 GMT  
  **Content:** @TPUSA is corrupt as well. Just as @tylerbowyer on governor candidate @BryanMasche 
  2 to 3 times Tyler has purposely denied candidate masche to attend or speak at certain events. They push their narrative just like the crappy MSM!  #Voter #Integrity ??  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:2] ID: 1491903068929236994**  
  **Author:** “I am Charlie Kirk” Deidre🇺🇸 - @thedeidree  
  **Timestamp:** Thu, 10 Feb 2022 22:33:04 GMT  
  **Content:** I’m so sorry for your son and the family.   The gov is lying to us all and hiding info.  You treat your the way you feel best and take care of him!   Will be praying for his recovery.  Take care sir.  
  **Engagement:** Likes=5, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:3] ID: 1491858112374095878**  
  **Author:** FreetoTalkandTrade - @Free2TalknTrade  
  **Timestamp:** Thu, 10 Feb 2022 19:34:26 GMT  
  **Content:** One day those kids will be in charge of things and those imposing the draconian rules will be at their mercy.  
  Just sayin'  This is how life works.  
  In case the adults are not forward thinking to be aware of what may come to them...  
  **Engagement:** Likes=8, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:4] ID: 1491920249620340736** (duplicate of post:0)  
  **Author:** Stanford Turning Point USA - @Stanford_GOP  
  **Timestamp:** Thu, 10 Feb 2022 23:41:20 GMT  
  (Same content as above)

- **[post:5] ID: 1491757024979337217**  
  **Author:** Darius Mayfield - @MrMayfieldUSA  
  **Timestamp:** Thu, 10 Feb 2022 12:52:44 GMT  
  **Content:** JOIN @RikMehta_NJ & I on March 3rd for a Townhall discussion presented by @tpusa_rutgers & @ridertpusa   
  Speaking to & hearing from the next generation is vital and I forward to seeing their support carry US to victory!   
  A vote for Darius is a vote for America AND common sense.  
  (Includes media: photo)  
  **Engagement:** Likes=6, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:6] ID: 1491658300114538499**  
  **Author:** Jesse formerly known as Darth Crypto - @DefNotDarth  
  **Timestamp:** Thu, 10 Feb 2022 06:20:27 GMT  
  **Content:** Listen to this into. They DESPISE YOU! They truly view us as vermin.  
  You don’t speak from the expansive lexicon enjoyed by educated, respectable citizens like us. You prols make grammatical errors and your rural parlance offends our elite ears! Be gone peasant!  
  (Quotes another post about Marjorie Taylor Greene)  
  **Engagement:** Likes=20, Reposts=4, Quotes=2, Replies=1, Bookmarks=0, Views=N/A

- **[post:7] ID: 1491632940639469569**  
  **Author:** ana fuentes - @anaydemi  
  **Timestamp:** Thu, 10 Feb 2022 04:39:40 GMT  
  **Content:** Charlie provide bussing again? Sounds like another historic event!  
  (Includes media: photo)  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:8] ID: 1491522539830403072**  
  **Author:** Shannon Watts - @shannonrwatts  
  **Timestamp:** Wed, 09 Feb 2022 21:20:59 GMT  
  **Content:** This violent rhetoric from leaders is in turn emboldening extremists. At an Idaho event with TPUSA founder Charlie Kirk, a man asked: "When do we get to use the guns? ... How many elections are they going to steal before we kill these people?"  
  **Engagement:** Likes=63, Reposts=10, Quotes=1, Replies=7, Bookmarks=1, Views=N/A

- **[post:9] ID: 1491510438374232064**  
  **Author:** Stanford Turning Point USA - @Stanford_GOP  
  **Timestamp:** Wed, 09 Feb 2022 20:32:54 GMT  
  **Content:** Yesterday under the cover of night the leftist agitators planning to disrupt our event with Vice President @Mike_Pence quietly put their banner underneath ours instead of tearing it down. This is proof that freedom of speech and conservative ideas are winning @Stanford.  
  @yaf  
  (Includes media: photo)  
  **Engagement:** Likes=5, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:10] ID: 1491494631325851650**  
  **Author:** Andy Vermaut - @AndyVermaut  
  **Timestamp:** Wed, 09 Feb 2022 19:30:05 GMT  
  **Content:** Andy Vermaut shares:Tucker: Our leaders are trying to intimidate truckers for speaking out.: Guests: Ezra Levant, Glenn Greenwald; Charlie Kirk, Blake Masters, Johann Hari, Clary… https://t.co/8uipoocmhk Thank you. #ThankYouJournalistsForTheNewsWeGetFromYou #AndyVermautThanksYou  
  (Includes media: photo)  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:11] ID: 1491491510180663305**  
  **Author:** Brandon Shubert - @theshu1992  
  **Timestamp:** Wed, 09 Feb 2022 19:17:41 GMT  
  **Content:** Getting High School students educated and involved is vital to changing minds. Amazing job @1776MichaelaM speaking to this freshman group today 👏😎@TPUSA  
  (Includes media: video)  
  **Engagement:** Likes=31, Reposts=8, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:12] ID: 1491047322955837443**  
  **Author:** Dinesh D'Souza - @DineshDSouza  
  **Timestamp:** Tue, 08 Feb 2022 13:52:38 GMT  
  **Content:** It’s happening! Fort Lauderdale, Florida. Saturday, February 19. Tickets at https://t.co/S4eEjln2Eu  
  (Includes media: photo)  
  **Engagement:** Likes=170, Reposts=43, Quotes=0, Replies=21, Bookmarks=0, Views=N/A

- **[post:13] ID: 1491378035496407043**  
  **Author:** Ron Filipkowski - @RonFilipkowski  
  **Timestamp:** Wed, 09 Feb 2022 11:46:46 GMT  
  **Content:** Charlie Kirk is planning on opening K-12 ‘America First’ Academies. The mission statement says public schools teach “a false narrative about America,” and his schools will offer a “reliable, quality, honest America-first education.” https://www.washingtonpost.com/politics/2022/02/08/charlie-kirk-turning-point-academy-strongmind/  
  **Engagement:** Likes=1455, Reposts=435, Quotes=455, Replies=1312, Bookmarks=77, Views=N/A

- **[post:14] ID: 1490113258128171009**  
  **Author:** Rev. Dr. William J. Barber II - @RevDrBarber  
  **Timestamp:** Sun, 06 Feb 2022 00:01:00 GMT  
  **Content:** I’m honored, along with my #PoorPeoplesCampaign co-chair Rev. Dr. @LizTheo, to accept the invitation from Pastor Paul Dunn at First Baptist Church in Charleston, WV, to preach from this historic pulpit where Rev. Dr. King preached in 1960, tomorrow Sunday 2/6 at 11am ET. Join us.  
  (Includes media: video)  
  **Engagement:** Likes=281, Reposts=77, Quotes=10, Replies=6, Bookmarks=2, Views=N/A

- **[post:15] ID: 1490890675608502273**  
  **Author:** The Post Millennial - @TPostMillennial  
  **Timestamp:** Tue, 08 Feb 2022 03:30:11 GMT  
  **Content:** Charlie Kirk @charliekirk11 comments on the 40% increase in deaths among people ages 18-64:  
  "Where are the people we put in charge to actually care about the wellbeing of our people?"  
  (Includes media: video)  
  **Engagement:** Likes=1231, Reposts=505, Quotes=95, Replies=195, Bookmarks=90, Views=N/A

- **[post:16] ID: 1490429712237137921**  
  **Author:** ThePersistence - @ScottPresler  
  **Timestamp:** Sun, 06 Feb 2022 20:58:28 GMT  
  **Content:** Today, I’m speaking at Godspeak Calvary Chapel @ 6 pm.  
  (Includes media: photo)  
  **Engagement:** Likes=2052, Reposts=290, Quotes=10, Replies=35, Bookmarks=3, Views=N/A

- **[post:17] ID: 1491192244237631495**  
  **Author:** BigBen7.com - @_BigBen7  
  **Timestamp:** Tue, 08 Feb 2022 23:28:30 GMT  
  **Content:** Ben will be a guest speaker at the 'Ignite Men's Impact Weekend' Conference.  It will be held on  March 11th-12th in Lynchburg, VA.  
  For all the info and to purchase tickets: https://t.co/t2Al0MU4mw  
  (Includes media: photo)  
  **Engagement:** Likes=439, Reposts=35, Quotes=3, Replies=12, Bookmarks=2, Views=N/A

- **[post:18] ID: 1491826913073147920**  
  **Author:** Independent Medical Alliance - @Honest_Medicine  
  **Timestamp:** Thu, 10 Feb 2022 17:30:27 GMT  
  **Content:** Dr. Pierre Kory joins Del Bigtree today at 11am PST/2 pm EST to talk about COVID treatments, trucker convoys and what happens next. Tune in to watch: https://thehighwire.com/watch/  
  (Includes media: photo)  
  **Engagement:** Likes=187, Reposts=50, Quotes=3, Replies=4, Bookmarks=4, Views=N/A

- **[post:19] ID: 1491112863305703425**  
  **Author:** EC3 // The Top 1% // - @therealec3  
  **Timestamp:** Tue, 08 Feb 2022 18:13:04 GMT  
  **Content:** #PressRelease⁣  
  ⁣  
  From the propaganda desk of the essential character⁣  
  #ControlYourNarrative⁣  
  Office@controlyournarrative.com⁣  
   ⁣  
  Control Your Narrative presents “Awakening: Live”⁣  
  Orlando, FL 3-5-22 and Dallas, TX 3-31-22⁣  
   ⁣  
  (Includes media: 2 photos)  
  **Engagement:** Likes=167, Reposts=36, Quotes=3, Replies=6, Bookmarks=1, Views=N/A

- **[post:20] ID: 1490791049270202368**  
  **Author:** NEWSMAX - @NEWSMAX  
  **Timestamp:** Mon, 07 Feb 2022 20:54:18 GMT  
  **Content:** NBA veteran Enes Kanter Freedom has been confirmed to speak at the three-day Conservative Political Action Conference later this month, according to CPAC Chairman Matt Schlapp. https://t.co/rG2DAVtMqu  
  (Includes media: photo)  
  **Engagement:** Likes=263, Reposts=41, Quotes=22, Replies=16, Bookmarks=1, Views=N/A

- **[post:21] ID: 1491433407934791682**  
  **Author:** TAMU Young Americans for Freedom - @tamuyaf  
  **Timestamp:** Wed, 09 Feb 2022 15:26:48 GMT  
  **Content:** 🚨 TODAY’S THE DAY 🚨  
  We are so excited for @MattWalshBlog’s lecture TONIGHT at 7:00pm in Bethancourt Ballroom (MSC 2300)  
  Tickets are SOLD OUT, but don’t fret. Doors open at 6:00pm and we have a standby line to fill any empty seats (no matter when they are emptied 👀)  
  @yaf  
  **Engagement:** Likes=191, Reposts=14, Quotes=1, Replies=11, Bookmarks=1, Views=N/A

- **[post:22] ID: 1491920249620340736** (duplicate of post:0)  
  (Same content)

- **[post:23] ID: 1491915120460533762** (duplicate of post:1)  
  (Same content)

- **[post:24] ID: 1491896923665612807**  
  **Author:** Tara - @Tara77281716  
  **Timestamp:** Thu, 10 Feb 2022 22:08:39 GMT  
  **Content:** @POTUS @LeaderMcConnell @RepAdamSchiff @charliekirk11 @SpeakerPelosi   
  Democrats are treating me like a person without rights again.   
  I should be able to speak to my children without Harris telling Omar to tell an Epstein #FBI agent in MN..  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:25] ID: 1491854614278426632**  
  **Author:** Shannon Bohn #Mystic, #Sophia #Magdalene #Lilith - @SBMcCallister  
  **Timestamp:** Thu, 10 Feb 2022 19:20:32 GMT  
  **Content:** Jack Posobeic Event planning  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:26] ID: 1491845043572908032**  
  **Author:** Opinionated Burt - @OpinionatedBurt  
  **Timestamp:** Thu, 10 Feb 2022 18:42:30 GMT  
  **Content:** The vaccine has a <1% adverse event rate and you people are still refusing to take it. You should feel extremely stupid.  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=N/A

- **[post:27] ID: 1491843512110878720**  
  **Author:** right 2 know ⚖️ - @metro2truth  
  **Timestamp:** Thu, 10 Feb 2022 18:36:25 GMT  
  **Content:** You would think under any normal circumstances that would be important with their scammed over 1/6 planned event!  No, they would rather go after people that question them.  Sad! I wish there was a vote today to replace them all…..  
  **Engagement:** Likes=3, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:28] ID: 1491396465989763080**  
  **Author:** Turning Point USA - @TPUSA  
  **Timestamp:** Wed, 09 Feb 2022 13:00:00 GMT  
  **Content:** AMAZING message from @KayleighMcEnany!  
  You were made for such a time as this. ALWAYS speak & fight for the Truth!  
  #GenFree #AMFEST2021  
  (Includes media: video)  
  **Engagement:** Likes=752, Reposts=127, Quotes=6, Replies=113, Bookmarks=3, Views=N/A

- **[post:29] ID: 1490890675608502273** (duplicate of post:15)  
  (Same content)

- **[post:30] ID: 1491428836290236418**  
  **Author:** Josh Marshall - @joshtpm  
  **Timestamp:** Wed, 09 Feb 2022 15:08:38 GMT  
  **Content:** this is nuts. one part Hitler Youth, one part Trump Steaks  https://www.washingtonpost.com/politics/2022/02/08/charlie-kirk-turning-point-academy-strongmind/?tid=ss_tw  
  **Engagement:** Likes=103, Reposts=17, Quotes=2, Replies=14, Bookmarks=3, Views=N/A

- **[post:31] ID: 1491108961604730881**  
  **Author:** Charlie Kirk - @charliekirk11  
  **Timestamp:** Tue, 08 Feb 2022 17:57:34 GMT  
  **Content:** If your school mandates masks, you must fight back. We at  @TPUSA support you. Push back against this tyrannical nonsense. You will win!  
  **Engagement:** Likes=1851, Reposts=312, Quotes=7, Replies=90, Bookmarks=3, Views=N/A

- **[post:32] ID: 1491524351501344768**  
  **Author:** Charlie Kirk - @charliekirk11  
  **Timestamp:** Wed, 09 Feb 2022 21:28:11 GMT  
  **Content:** It's super creepy to watch Democrats fight so hard just to be able to talk to elementary school children about gay sex.  
  **Engagement:** Likes=7730, Reposts=1857, Quotes=107, Replies=305, Bookmarks=18, Views=N/A

- **[post:33] ID: 1491815475017306126**  
  **Author:** The TCA - @OfficialTCA  
  **Timestamp:** Thu, 10 Feb 2022 16:45:00 GMT  
  **Content:** The TCA Virtual Winter Press Tour continues today with @AMC_TV,  @AMCPlus, @AcornTV, @Shudder and @sundance_now. We will have panels on @SOTUSundance, #PartnersinCrime,#DarkWinds, #QueerforFear, #TenPercent, #ThatDirtyBlackBag and @KillingEve #TCA22  
  (Includes media: video)  
  **Engagement:** Likes=207, Reposts=30, Quotes=14, Replies=7, Bookmarks=5, Views=N/A

- **[post:34] ID: 1491912877929807873**  
  **Author:** Charlie Angus - @CharlieAngusNDP  
  **Timestamp:** Thu, 10 Feb 2022 23:12:03 GMT  
  **Content:** How about this buddy - go get elected.   
  Then come and tell us how you're going to run the country.   
  In the meantime if your pals are going to jam the 9-11 phone lines and cut off supplies at the border, how about you explain your theory of constitutional anarchy to the judge?  
  **Engagement:** Likes=155, Reposts=37, Quotes=2, Replies=18, Bookmarks=0, Views=N/A

- **[post:35] ID: 1491828039008894980**  
  **Author:** Charlie Spiering - @charliespiering  
  **Timestamp:** Thu, 10 Feb 2022 17:34:55 GMT  
  **Content:** Protesters in Culpeper, Virginia greet Joe Biden with shouts of “Let’s Go Brandon” and signs reading "Joe Biden Sucks" and FJB  
  **Engagement:** Likes=437, Reposts=118, Quotes=7, Replies=25, Bookmarks=4, Views=N/A

- **[post:36] ID: 1491588454513217537**  
  **Author:** Charlie Kirk - @charliekirk11  
  **Timestamp:** Thu, 10 Feb 2022 01:42:54 GMT  
  **Content:** Joe Biden’s America: No Pipelines, just Crack Pipes.  
  **Engagement:** Likes=8866, Reposts=1831, Quotes=63, Replies=249, Bookmarks=9, Views=N/A

- **[post:37] ID: 1491830160022200334**  
  **Author:** Charlie Spiering - @charliespiering  
  **Timestamp:** Thu, 10 Feb 2022 17:43:21 GMT  
  **Content:** One protester on the route of Biden’s trip to Culpeper, Va has a sign reading "Build Crack Better"  
  **Engagement:** Likes=3811, Reposts=544, Quotes=52, Replies=69, Bookmarks=11, Views=N/A

All tool results (keyword, semantic, account-specific) were exhausted. No additional posts matched the criteria.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-02-05 to 2022-02-11**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-02-05 to 2022-02-11 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
