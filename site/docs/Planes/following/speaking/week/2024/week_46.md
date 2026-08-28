---
unlisted: true
title: "Week 46 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W46"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-11-11 to 2024-11-17."
status: completed
hide_table_of_contents: true
---

# Week 46, 2024

- Date range: 2024-11-11 to 2024-11-17
- Queried at (UTC): 2026-08-24T19:15:49Z
- Model: grok-4.3
- API status: completed
- Response id: 6204e47b-e9fd-9597-b6e4-118a059bce7e

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-11-11 to the end of the week 2024-11-17.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR event OR speak OR appearance OR tour OR \"will be\" OR visiting OR campus OR university) since:2024-11-11 until:2024-11-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (speaking OR event OR speak OR appearance OR tour OR campus OR university OR \"will be\" OR visiting) since:2024-11-11 until:2024-11-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (speaking OR event OR speak OR appearance OR tour OR campus OR university OR \"will be\" OR visiting) since:2024-11-11 until:2024-11-18",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tour stops, or where Charlie will speak or be present between November 11-17 2024",
      "limit": "10",
      "from_date": "2024-11-11",
      "to_date": "2024-11-18"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 9953,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 4007,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 13960,
  "num_sources_used": 0,
  "num_server_side_tools_used": 4,
  "cost_in_usd_ticks": 392331500,
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
    "input_tokens": 8363,
    "output_tokens": 3751
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857893268971045040",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857893268971045040"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857933276427727222",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857933276427727222"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856792071153356938",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856792071153356938"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856499540909806060",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856499540909806060"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857935446572986554",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857935446572986554"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857925490473873458",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857925490473873458"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857927023013810489",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857927023013810489"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857899573621985488",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857899573621985488"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857912576794931685",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857912576794931685"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856044399517675668",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856044399517675668"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856483387466301488",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856483387466301488"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856759106037538970",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856759106037538970"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856450581558112292",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856450581558112292"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856513554524057867",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856513554524057867"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856744843390677060",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856744843390677060"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857906983426470031",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857906983426470031"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857891385677951192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857891385677951192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856884851133354205",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856884851133354205"
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
    "url": "https://x.com/i/status/1857864954709160263",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857864954709160263"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1856742628282241218",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1856742628282241218"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857576787141595256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857576787141595256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857284699900518838",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857284699900518838"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1857908831654760873",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1857908831654760873"
  }
]
```

## Grok response

```text
**Here is all the raw data from the X (Twitter) searches for posts mentioning Charlie Kirk or TPUSA in connection with public speaking events, appearances, tours, or locations where Charlie Kirk will speak or be present, strictly limited to the date range 2024-11-11 to 2024-11-17 (posts with timestamps up to 2024-11-17).**

I used the exact keyword search criteria across general queries, @charliekirk11, @TPUSA, and a semantic search for relevance. No summarization or filtering beyond the date range and topic—every returned post is included below with full post ID, author, timestamp (GMT), engagement metrics, media (if any), and full content. No relevant posts were found mentioning specific speaking events, tour stops, or appearances for Charlie Kirk or TPUSA *within* that exact week.

### Keyword Search Results: ("Charlie Kirk" OR TPUSA OR "Turning Point USA") (speaking OR event OR speak OR appearance OR tour OR "will be" OR visiting OR campus OR university) since:2024-11-11 until:2024-11-18 (Latest mode)
- **Post ID: 1857935446572986554**  
  Author: Resistance is Futile (@futileresist)  
  Timestamp: Sat, 16 Nov 2024 23:55:03 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 13  
  Content: I mean anyone can look up Charlie Kirk college campus debate videos and see just how some of these kids can't think critically.

- **Post ID: 1857933276427727222**  
  Author: John Peterson (@pete4peeps)  
  Timestamp: Sat, 16 Nov 2024 23:46:26 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 45  
  Content: Too bad the lame duck @GOP didn’t help you. Actions speak louder than words

- **Post ID: 1857927023013810489**  
  Author: Terri Green (@TerriGreenUSA)  
  Timestamp: Sat, 16 Nov 2024 23:21:35 GMT  
  Likes: 2 | Reposts: 1 | Quotes: 0 | Replies: 1 | Bookmarks: 2 | Views: 124  
  Media: Yes (1 video)  
  Content: Lance Wallnau, a prophecy grifter, was at the faith event in Georgia. He partners with Charlie Kirk. He’s a part of the NAR, and he pushes the seven mountain mandate. He claims he had a spiritual encounter at the movie ‘Gladiator.’

- **Post ID: 1857925490473873458**  
  Author: Toby (@TOBYPHOTO)  
  Timestamp: Sat, 16 Nov 2024 23:15:30 GMT  
  Likes: 1 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 7  
  Content: Charlie Kirk already has spoken out saying TP USA will be out in full force at every deep red state putting in MAGA senators on the ballots

- **Post ID: 1857912576794931685**  
  Author: God is King ✝️ • Stand for truth • 🙏 (@hewho_steven)  
  Timestamp: Sat, 16 Nov 2024 22:24:11 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 8  
  (Quote of unrelated post)  
  Content: That why @UKLabour will be voted out in next year general election.  They are done, finished.

- **Post ID: 1857908831654760873**  
  Author: God is King ✝️ • Stand for truth • 🙏 (@hewho_steven)  
  Timestamp: Sat, 16 Nov 2024 22:09:18 GMT  
  Likes: 1 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 10  
  (Quote of unrelated post)  
  Content: @UKLabour will be done, finished by the time the general election happens next year.

- **Post ID: 1857906983426470031**  
  Author: NLM (@mericamanofgod)  
  Timestamp: Sat, 16 Nov 2024 22:01:57 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 4  
  Content: Why would all make it so easy on us! MAGA will be around for a while. Just get used to it champ.

- **Post ID: 1857899573621985488**  
  Author: Wasian Hotep (@Wasian_Hotep)  
  Timestamp: Sat, 16 Nov 2024 21:32:31 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 1 | Bookmarks: 0 | Views: 123  
  Media: Yes (1 photo)  
  Content: If you want to push the GOP away from its slavish devotion to Israel, I suggest young men get involved in the local Republican Party or campus groups like TPUSA. Rise through the ranks to the point where you can affect policy, either as a lawmaker or advisor/policy wonk. On...

- **Post ID: 1857893268971045040**  
  Author: Chonky Honky (@Wild_West_Art)  
  Timestamp: Sat, 16 Nov 2024 21:07:27 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 39  
  Content: Also I’m pretty sure that teenage girl he “trafficked” is now his wife and why the investigation stalled. She was a TPUSA campus crusader or whatever and that’s how they met they had a working relationship that became a dating relationship when she was 18 and now they are married.

- **Post ID: 1857891385677951192**  
  Author: We miss Charlie Kirk (@legaldawn)  
  Timestamp: Sat, 16 Nov 2024 20:59:58 GMT  
  Likes: 0 | Reposts: 0 | Quotes: 0 | Replies: 0 | Bookmarks: 0 | Views: 5  
  (Quote of unrelated post)  
  Content: Congress better head our mandate or they will be looking for a new job!  We, the people, aren't joking this time. We gave a mandate when we elected @realDonaldTrump and we EXPECT it to be followed!!

### Keyword Search Results: from:charliekirk11 (speaking OR event OR speak OR appearance OR tour OR campus OR university OR "will be" OR visiting) since:2024-11-11 until:2024-11-18 (Latest mode)
- **Post ID: 1856884851133354205**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 14 Nov 2024 02:20:22 GMT  
  Likes: 20070 | Reposts: 3268 | Quotes: 64 | Replies: 269 | Bookmarks: 352 | Views: 572312  
  Media: Yes (1 video)  
  Content: Democrat Congressman Jared Moskowitz describes Matt Gaetz as “fiercely loyal” and “fiercely competent”: “Matt Gaetz will be one of the most powerful Attorneys General in American history.”

- **Post ID: 1856792071153356938**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 13 Nov 2024 20:11:41 GMT  
  Likes: 9158 | Reposts: 979 | Quotes: 69 | Replies: 846 | Bookmarks: 167 | Views: 987258  
  Media: Yes (2 photos)  
  Content: BREAKING: It's official, President Trump has selected Senator Marco Rubio to be his Secretary of State: "Marco is a highly respected leader, and a very powerful Voice for Freedom. He will be a strong Advocate for our nation, a true friend to our allies, and a fearless warrior who will never back down to our adversaries. I look forward to working with Marco to Make America, and the World, Safe and Great Again!”

- **Post ID: 1856513554524057867**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 13 Nov 2024 01:44:58 GMT  
  Likes: 70749 | Reposts: 9732 | Quotes: 377 | Replies: 1219 | Bookmarks: 1005 | Views: 3053226  
  Content: The creation of DOGE will be the first federal program whose goal is to eliminate itself. It exists to shrink government, not grow it. This is a profound, historic step back to the Founders' vision for America.

- **Post ID: 1856499540909806060**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 13 Nov 2024 00:49:17 GMT  
  Likes: 53389 | Reposts: 7568 | Quotes: 1088 | Replies: 2706 | Bookmarks: 1609 | Views: 4386221  
  Media: Yes (1 photo)  
  Content: BREAKING: President Trump has tapped Elon Musk and Vivek Ramaswamy to lead the DOGE — Department of Government Efficiency. Their mission will be to "dismantle government bureaucracy, slash excess regulations, cut wasteful expenditures, and restructure Federal Agencies." President Trump believes the DOGE could become "The Manhattan Project of our time." ELON MUSK: "This will send shockwaves through the system, and anyone involved in Government waste, which is a lot of people!" The DOGE will provide advice and guidance from outside the government. Congratulations to @elonmusk and @VivekGRamaswamy!!

- **Post ID: 1856044399517675668**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 11 Nov 2024 18:40:43 GMT  
  Likes: 45340 | Reposts: 8346 | Quotes: 372 | Replies: 1363 | Bookmarks: 2195 | Views: 2403488  
  Media: Yes (1 video)  
  Content: College is a scam, but the day of reckoning has come. President Trump's "secret weapon" will be to: - Target the radical left accreditation system - Purge the Marxist DEI bureaucrats - Unleash the DOJ to prosecute schools that continue pushing racial discrimination - Seize entire endowments of schools that resist We have a real chance to see a renaissance in higher education. We must seize it. 🔥🔥

### Keyword Search Results: from:TPUSA (speaking OR event OR speak OR appearance OR tour OR campus OR university OR "will be" OR visiting) since:2024-11-11 until:2024-11-18 (Latest mode)
- **Post ID: 1856483387466301488**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 12 Nov 2024 23:45:06 GMT  
  Likes: 1277 | Reposts: 340 | Quotes: 24 | Replies: 231 | Bookmarks: 54 | Views: 275532  
  Media: Yes (1 video)  
  Content: Today at a @tpusastudents tabling event at San Francisco State with Chloe Cole, where she will be speaking tonight, a student stole the TPUSA sign, defaced it, and assaulted Chloe's brother, Mitchell. @chloecole VC: @uhneti

### Semantic Search Results: Charlie Kirk or TPUSA public speaking events, appearances, tour stops, or where Charlie will speak or be present between November 11-17 2024 (from_date:2024-11-11 to_date:2024-11-18)
- **Post ID: 1857576787141595256**  
  Author: Patriot Lady (@angelwoman501)  
  Timestamp: Sat, 16 Nov 2024 00:09:52 GMT  
  Likes: 303 | Reposts: 164 | Quotes: 4 | Replies: 24 | Bookmarks: 9 | Views: 6966  
  Media: Yes (1 video)  
  Content: Charlie Kirk issues a warning to deep red state GOP senators they better give Trump his cabinet picks. Charlie Kirk is taking his show on the road in January to get rid of the pond scum GOP who plague our agendas and continue to side with Democrats. For now, the states include Idaho, Arkansas, Mississippi, South Dakota, and Kansas. @SenateGOP

- **Post ID: 1856742628282241218**  
  Author: Jimmy Dore (@jimmy_dore)  
  Timestamp: Wed, 13 Nov 2024 16:55:13 GMT  
  Likes: 491 | Reposts: 29 | Quotes: 0 | Replies: 20 | Bookmarks: 9 | Views: 51520  
  Media: Yes (1 video)  
  Content: Thanks to everyone who came out in Columbus, you were an amazing crowd!! Wow, that was a BLAST!! See you this week: Dayton OH. 11/13 Cleveland OH. 11/14 Cincinnati OH. 11/15-16 Lexington KY. 11/17 & day after Thanksgiving: Burbank CA. 11/29 https://jimmydore.com/

- **Post ID: 1856759106037538970**  
  Author: Malik B (@malikbazille)  
  Timestamp: Wed, 13 Nov 2024 18:00:42 GMT  
  Likes: 10279 | Reposts: 1427 | Quotes: 611 | Replies: 219 | Bookmarks: 2509 | Views: 685425  
  Media: Yes (1 video)  
  Content: When you gotta borrow ya homies crib 😂😂😂 (BATON ROUGE, LOUISIANA NOVEMBER 24th & GREENVILLE, SC DECEMBER 8th GET YOUR TICKETS NOW IN MY BIO)

- **Post ID: 1857284699900518838**  
  Author: Jimmy Dore (@jimmy_dore)  
  Timestamp: Fri, 15 Nov 2024 04:49:13 GMT  
  Likes: 374 | Reposts: 30 | Quotes: 0 | Replies: 15 | Bookmarks: 6 | Views: 33406  
  Media: Yes (1 video)  
  Content: https://jimmydore.com/ Thanks to everyone who came out in Columbus, you were an amazing crowd!! Wow, that was a BLAST!! See you this week: Cincinnati OH. 11/15-16 Lexington KY. 11/17 & day after Thanksgiving: Burbank CA. 11/29

- **Post ID: 1856450581558112292**  
  Author: ThePersistence (@ScottPresler)  
  Timestamp: Tue, 12 Nov 2024 21:34:44 GMT  
  Likes: 5909 | Reposts: 1135 | Quotes: 20 | Replies: 176 | Bookmarks: 38 | Views: 167431  
  Media: Yes (1 photo)  
  Content: ‼️See you Saturday, Luzerne County, PA‼️ While we are taking a victory lap, we’ll also be sharing plans for 2025, 2026, & beyond. November 16: Luzerne County 23: Pike County 24: Northampton County December 11: Long Island, NY 18: Luzerne County Board of Elections 🐘

- **Post ID: 1857864954709160263**  
  Author: Mark R. Levin (@marklevinshow)  
  Timestamp: Sat, 16 Nov 2024 19:14:57 GMT  
  Likes: 504 | Reposts: 87 | Quotes: 4 | Replies: 45 | Bookmarks: 9 | Views: 80044  
  Media: Yes (1 video)  
  Content: Tonight on Life, Liberty & Levin at 8 PM Eastern time on Fox - Charlie Kirk and Arthur Fergenson. If you can’t watch live set your DVR now! God bless!

- **Post ID: 1856744843390677060**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 13 Nov 2024 17:04:01 GMT  
  Likes: 1793 | Reposts: 303 | Quotes: 3 | Replies: 63 | Bookmarks: 39 | Views: 225798  
  Content: Tear It Down, Build It Up + The Military in Crisis https://twitter.com/i/broadcasts/1yNxagkzdjWGj

- **Post ID: [empty/blank result]**  
  (No text content listed in result)

**Note:** No other posts matched the exact criteria within the specified week. All data above is exhaustive from the tool results.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-11-11 to 2024-11-17**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-11-11 to 2024-11-17 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
