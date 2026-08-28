---
unlisted: true
title: "Week 18 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W18"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-04-29 to 2024-05-05."
status: completed
hide_table_of_contents: true
---

# Week 18, 2024

- Date range: 2024-04-29 to 2024-05-05
- Queried at (UTC): 2026-08-24T19:12:39Z
- Model: grok-4.3
- API status: completed
- Response id: 5f97fcff-f381-9f56-9b4e-9bc8c9163907

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-04-29 to the end of the week 2024-05-05.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearance OR speaking OR \"speaking at\" OR \"at\" OR visit OR visiting) since:2024-04-29 until:2024-05-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearance OR \"speaking at\" OR visit OR visiting) since:2024-04-29 until:2024-05-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus OR \"will be\" OR appearance OR \"speaking at\" OR visit OR visiting) since:2024-04-29 until:2024-05-06",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus visits, or where Charlie will speak between April 29 and May 5 2024",
      "limit": "10",
      "from_date": "2024-04-29",
      "to_date": "2024-05-06",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 10669,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 4639,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 15308,
  "num_sources_used": 0,
  "num_server_side_tools_used": 4,
  "cost_in_usd_ticks": 417081500,
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
    "input_tokens": 9079,
    "output_tokens": 4357
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785006181209268539",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785006181209268539"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1784738071587545554",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1784738071587545554"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786432918027685995",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786432918027685995"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786906279278940479",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786906279278940479"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785437224697270697",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785437224697270697"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786056019925495941",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786056019925495941"
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
    "url": "https://x.com/i/status/1785413459221622791",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785413459221622791"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785347220700790818",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785347220700790818"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786905763513766020",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786905763513766020"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786419845313302530",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786419845313302530"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786901834679865357",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786901834679865357"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785756302184165878",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785756302184165878"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786899075260109017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786899075260109017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785748938773180796",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785748938773180796"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785737623107219637",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785737623107219637"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785452617520582815",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785452617520582815"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786192379323797667",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786192379323797667"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785365222280376596",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785365222280376596"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786906066938216455",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786906066938216455"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785779125602631989",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785779125602631989"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786396710094414134",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786396710094414134"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786755872313810958",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786755872313810958"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1785022365023293549",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1785022365023293549"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1786140786813517988",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1786140786813517988"
  }
]
```

## Grok response

```text
**Here is every relevant post** from the X searches (keyword and semantic) matching the exact date range **2024-04-29 to 2024-05-05** (posts up to 2024-05-05 inclusive, per the `until:2024-05-06` cutoff). I included **all data** without summarizing, filtering, or omitting any post that referenced Charlie Kirk, TPUSA, events, speaking, campus visits, appearances, or tours. Posts are presented in the order returned by the tools (mostly chronological by mode).

### From @charliekirk11 (Charlie Kirk's account) – keyword search:
- **Post ID: 1785779125602631989**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Wed, 01 May 2024 21:11:36 GMT  
  **Content:** 🚨🚨 SPEAKER DROP 🚨🚨 Brand new additions to the lineup for The People's Convention in Detroit, MI June 14-16. Biggest names in the movement. You CAN'T miss it. https://t.co/Kwn6vrz4CM @tpaction #PEOPLES2024  
  **Media:** 1 photo (lineup graphic)  
  **Engagement:** Likes=3153, Reposts=811, Quotes=91, Replies=602, Bookmarks=107, Views=743435

- **Post ID: 1786396710094414134**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Fri, 03 May 2024 14:05:39 GMT  
  **Content:** On college campuses, beyond the chaos and fem/lib humanities majors with nose piercings, you’re seeing the beginnings of a culture wide, generational reset. The young men have had enough. You’re about to see millions of them get pissed off enough to reject the left’s entire premise. Celebrate the prodigal sons as they come home. This video was from my visit to Cal Poly SLO about a month before the recent protests started. @TPUSA  
  **Media:** 1 video (campus footage)  
  **Engagement:** Likes=67342, Reposts=11570, Quotes=764, Replies=2698, Bookmarks=1552, Views=3834765

- **Post ID: 1786419845313302530**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Fri, 03 May 2024 15:37:35 GMT  
  **Content:** Greg Gutfeld makes some keen observations about the campus protesters: "When you look at the protests, there's two things you got to notice. Mostly young women...they look miserable, disheveled. Meanwhile when you see those counterprotestors, those frat boys, healthy, good looking guys, they got it together." "Leftism has led young women down a path where their only purpose they perceive is outrage...they've devoted their aimless energy into causes that serve to only undermine their future, their happiness." "We've derided motherhood where their only baby is abortion."  
  **Media:** 1 video (Gutfeld clip)  
  **Engagement:** Likes=33704, Reposts=7374, Quotes=283, Replies=871, Bookmarks=1304, Views=2531083

- **Post ID: 1786432918027685995** (quote of above)  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Fri, 03 May 2024 16:29:32 GMT  
  **Content:** It's a decade long movement in the making. We have no idea how big this could get, but for the countless patriots on campus, their moment to speak up has just arrived. The counter revolution is here. There is no stopping what is coming.  
  **Engagement:** Likes=7805, Reposts=1302, Quotes=40, Replies=263, Bookmarks=64, Views=246973

- **Post ID: 1786192379323797667**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Fri, 03 May 2024 00:33:43 GMT  
  **Content:** It’s subjective. It will be used against conservatives before it’s used against leftists.  
  **Engagement:** Likes=1386, Reposts=185, Quotes=46, Replies=34, Bookmarks=52, Views=82154

- **Post ID: 1786140786813517988**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Thu, 02 May 2024 21:08:43 GMT  
  **Content:** Trump supporting students at Ole Miss make the Pro-Hamas crowd instantly regret their decision... The pro-America crowd on campus is rising up! 🇺🇸🇺🇸  
  **Media:** 1 video  
  **Engagement:** Likes=14645, Reposts=2871, Quotes=90, Replies=303, Bookmarks=155, Views=255956

- **Post ID: 1785756302184165878**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Wed, 01 May 2024 19:40:54 GMT  
  **Content:** President Trump calls out college presidents amid nationwide campus protests: "To every college president I say remove the encampments immediately, vanquish the radicals, and take back our campuses for all of the normal students who want a safe place from which to learn."  
  **Media:** 1 video  
  **Engagement:** Likes=14680, Reposts=2607, Quotes=61, Replies=179, Bookmarks=71, Views=261261

- **Post ID: 1785748938773180796**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Wed, 01 May 2024 19:11:39 GMT  
  **Content:** In response to campus anti-Israel protests, the House is rushing to to vote on a new bill, HR 6090. This new bill would officially define "Antisemitism" so the federal government can sue, prosecute, or sanction more people, businesses, and universities for supposed violations of civil rights law. I abhor antisemitism, but this bill is flagrantly unconstitutional and an appalling attack on the First Amendment. This bill would make it illegal to compare Israeli policies to Nazi policies. It would make it illegal to describe Israel as racist. It would make it illegal to accuse an American citizen of being more loyal to Israel than to the United States. All of those behaviors might be stupid or repugnant, but they are indisputably protected by the First Amendment. Yet now, Congressional Republicans are rushing to gut the First Amendment in order to pass a Europe-style ban on supposed "hate speech." Rioters should be arrested. Unhinged Israel-hating students who take over buildings and refuse to leave should be expelled. But I stand with @RepThomasMassie: This bill is an affront to the Constitution and must not pass.  
  **Engagement:** Likes=18430, Reposts=4008, Quotes=760, Replies=1912, Bookmarks=1177, Views=4063358

- **Post ID: 1785737623107219637**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Wed, 01 May 2024 18:26:41 GMT  
  **Content:** Laura Ingraham SLAMS Democrats for coddling illegal campus protests for political gain: "If this were some type of pro-MAGA or conservative gathering...this thing would have been shut down in 48 hours and these kids would be in jail right now. That would be unfair, but that's what they would do. In this case they've made a political decision. They've decided that Michigan and the election is more important..." "They have been given tacit thumbs up to keep going."  
  **Media:** 1 video  
  **Engagement:** Likes=1837, Reposts=392, Quotes=14, Replies=103, Bookmarks=29, Views=127272

- **Post ID: 1785452617520582815**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Tue, 30 Apr 2024 23:34:10 GMT  
  **Content:** This is a classic case of the indoctrination I see on campus. He believes conservatives are rich fascists while progressives are just defenders of the working class — when the exact opposite is closer to the truth. He goes from name calling to asking honest questions. 💡💡  
  **Media:** 1 video  
  **Engagement:** Likes=10886, Reposts=2585, Quotes=167, Replies=462, Bookmarks=1045, Views=495251

- **Post ID: 1785365222280376596**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Tue, 30 Apr 2024 17:46:54 GMT  
  **Content:** I’m loving all the GOP unity against Jew hatred. It has no place in America. Can we get the same unity about the institutional hatred of white people on campus? It’s even more embedded than the antisemitism.  
  **Engagement:** Likes=2670, Reposts=349, Quotes=105, Replies=824, Bookmarks=31, Views=163196

- **Post ID: 1785347220700790818**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Tue, 30 Apr 2024 16:35:22 GMT  
  **Content:** When you storm a school building, occupy it, smash it up, and take janitors hostage, what else can you call it except a campus insurrection? The students responsible for this should be arrested, for sure. But even more importantly, they should be expelled, tried, and given a jail sentence. At a minimum, they deserve worse than anyone who got jail time for standing on the steps of the US Capitol with a megaphone, or walking through a door and then walking back out.  
  **Media:** 1 video  
  **Engagement:** Likes=13728, Reposts=3331, Quotes=99, Replies=616, Bookmarks=99, Views=243034

### From @TPUSA (Turning Point USA account) – keyword search:
- **Post ID: 1785413459221622791**  
  **Author:** Turning Point USA @TPUSA  
  **Timestamp:** Tue, 30 Apr 2024 20:58:34 GMT  
  **Content:** Our @tpusastudents at UNC Chapel Hill filmed this footage on campus. A group of patriotic students displayed an American flag in response to pro-Hamas activists who tore down the American flag and replaced it with a Palestinian flag on the main campus flag pole.  
  **Media:** 1 video + 1 photo  
  **Engagement:** Likes=190, Reposts=46, Quotes=3, Replies=15, Bookmarks=5, Views=19687

- **Post ID: 1785006181209268539**  
  **Author:** Turning Point USA @TPUSA  
  **Timestamp:** Mon, 29 Apr 2024 18:00:12 GMT  
  **Content:** The one and only @megynkelly is joining us at #YWLS2024 in San Antonio, TX! 🎉 Don’t forget to secure your spot for the nation’s LARGEST event for conservative women: https://t.co/Z96ozRGJKG  
  **Media:** 1 photo  
  **Engagement:** Likes=194, Reposts=76, Quotes=14, Replies=23, Bookmarks=2, Views=180638

### Other accounts mentioning Charlie Kirk / TPUSA events or speaking (keyword search):
- **Post ID: 1786906279278940479**  
  **Author:** Charlie Kirk's Bonus Hole @JoshAllenFan2  
  **Timestamp:** Sat, 04 May 2024 23:50:30 GMT  
  **Content:** Making it a "top priority in the next 5 years" has polled around 10% since at least 2017.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=40

- **Post ID: 1786906066938216455** (quote of Nick Fuentes post)  
  **Author:** Just another psyop @The_Novi_Chalk  
  **Timestamp:** Sat, 04 May 2024 23:49:40 GMT  
  **Content:** Bizarro world. Read the screenshots of Charlie Kirk's gushing allegiance to Jews. Name one other group this happens to. And we're supposed to pretend like there's not some global conspiracy going on here? Ppl talk about white supremacy but this is obvious Jewish supremacy at work  
  **Quoted Post (Nick Fuentes):** TPUSA has been operating a secret website for at least two weeks distancing itself from Candace Owens. It also affirms Charlie Kirk’s allegiance to Israel and the Jewish people. This is North Korea-level stuff, totally bizarre and dystopian. AMERICA FIRST 🇺🇸  
  **Media (quoted):** 2 photos (screenshots)  
  **Engagement:** Likes=5, Reposts=1, Quotes=0, Replies=2, Bookmarks=0, Views=368

- **Post ID: 1786905763513766020** (quote of Charlie Kirk post above)  
  **Author:** paul @tigger1972  
  **Timestamp:** Sat, 04 May 2024 23:48:27 GMT  
  **Content:** JFC tulsi(who reposted this of course) Challenge: get in a time machine, go back in time and tell your supporters in 2020 that in 4 years you'd be at TPUSA event. Their reaction would be interesting  
  **Quoted Post:** (same as post 1785779125602631989 – The People's Convention speaker drop)  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=29

- **Post ID: 1786901834679865357**  
  **Author:** chaos - self ordained Pastor @watershedChaos  
  **Timestamp:** Sat, 04 May 2024 23:32:51 GMT  
  **Content:** .@charliekirk11 the great betrayal against candace owens by TPUSA shows that there is no pro american campus organisation in the US only those for a foreign people and foreign causes  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=34

- **Post ID: 1786899075260109017**  
  **Author:** Charlie Kirk @iamcharliekirk4  
  **Timestamp:** Sat, 04 May 2024 23:21:53 GMT  
  **Content:** They will be back sooner than we think 💯  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=296

### Semantic search results (additional relevant posts in the date range):
- **Post ID: 1785779125602631989** (duplicate of above – Charlie Kirk speaker drop for The People's Convention)  
  **Timestamp:** Wed, 01 May 2024 21:11:36 GMT

- **Post ID: 1786396710094414134** (duplicate of above – Charlie Kirk Cal Poly SLO visit reference)  
  **Timestamp:** Fri, 03 May 2024 14:05:39 GMT

- **Post ID: 1786755872313810958**  
  **Author:** 🔆KEZZMIT🔆 @Kezzmit  
  **Timestamp:** Sat, 04 May 2024 13:52:50 GMT  
  **Content:** He’ll get the same notoriety as Kyle Rittenhouse…he’ll be invited to be guest speaker at the Republican National Convention, CPAC and Turning Point USA. Watch.  
  **Engagement:** Likes=678, Reposts=28, Quotes=3, Replies=114, Bookmarks=4, Views=103949

- **Post ID: 1785437224697270697**  
  **Author:** ACLU of Texas @ACLUTx  
  **Timestamp:** Tue, 30 Apr 2024 22:33:00 GMT  
  **Content:** TEXAS STUDENTS: Join us May 3 at 3 p.m. CT for a virtual training on your rights as a public college or university student. You'll learn about: 📢 Protections under the First Amendment. 📢 What to do if approached by law enforcement. 📢 & More. Sign up: https://www.aclutx.org/events/know-your-rights-protesting-texas-colleges-universities  
  **Engagement:** Likes=274, Reposts=164, Quotes=17, Replies=80, Bookmarks=19, Views=21635

- **Post ID: 1785022365023293549**  
  **Author:** Curtis Houck @CurtisHouck  
  **Timestamp:** Mon, 29 Apr 2024 19:04:30 GMT  
  **Content:** CBS's @Weijia Jiang: “I’m sorry if I missed this, but is the answer no, the administration has not been in touch with anyone at Columbia?” KJP: “I — I don't have any — uh — read out — I should have — I should have answered this in, I believe that was Jeff's question, um, I — I don't have any calls to read out to you of a conversations with any university, any university leaders — uh, at this time. Uh, obviously the president's going to go speak at Morehouse, and so we've been in touch with them because he's going to give a deliver a commencement speech. He's looking forward to doing that. It is such an important moment in time for graduates, and he's gonna go obviously to — uh — to West Point. Those are the two that he's doing.”  
  **Media:** 1 video  
  **Engagement:** Likes=2064, Reposts=568, Quotes=91, Replies=318, Bookmarks=119, Views=500727

- **Post ID: 1785756302184165878** (duplicate of above)  
  **Timestamp:** Wed, 01 May 2024 19:40:54 GMT

- **Post ID: 1786056019925495941**  
  **Author:** Charlie Kirk @charliekirk11  
  **Timestamp:** Thu, 02 May 2024 15:31:53 GMT  
  **Content:** A masked pro-Gaza protester at UCLA explains how leftists are dead set on tearing down America’s institutions: “Given that the University of California is founded upon colonialism, it’s inherently a violent institution. There needs to be an adjustment of US imperialism.” The left is a fundamentally anti-civilization movement. It must be stopped.  
  **Engagement:** Likes=1129, Reposts=290, Quotes=33, Replies=254, Bookmarks=29, Views=139711

- **Post ID: 1784738071587545554**  
  **Author:** MichaelRapaport @MichaelRapaport  
  **Timestamp:** Mon, 29 Apr 2024 00:14:49 GMT  
  **Content:** Madison Wisconsin at Comedy On State 5/2 Turtle Lake,Wisconsin at St.Croix Casino 5/3 Cincinnati at The Funny Bone 5/17 & 5/18 Batavia,IL at the Comedy Vault 6/6-6/8 Cue the Tom Petty Music🥊🥊  
  **Engagement:** Likes=354, Reposts=32, Quotes=2, Replies=38, Bookmarks=1, Views=23194

(No additional posts with content were returned in the semantic search beyond these.)

**No other posts** in the tool results mentioned specific upcoming public speaking events, campus appearances, or tours for Charlie Kirk or TPUSA strictly within **April 29–May 5, 2024**. The results reference a past visit (Cal Poly SLO) and future events outside the window (People's Convention June 14-16, YWLS2024). All data is included exactly as returned.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-04-29 to 2024-05-05**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-04-29 to 2024-05-05 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
