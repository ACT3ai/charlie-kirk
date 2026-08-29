---
unlisted: true
title: "Week 32 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W32"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-08-06 to 2023-08-12."
status: completed
hide_table_of_contents: true
---

# Week 32, 2023

- Date range: 2023-08-06 to 2023-08-12
- Queried at (UTC): 2026-08-24T19:08:17Z
- Model: grok-4.3
- API status: completed
- Response id: 1835dde6-06e4-9883-808e-7c95fdc5465b

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-08-06 to the end of the week 2023-08-12.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"will be\" OR \"speaking at\" OR appearance OR campus) since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR tour) (2023 OR August) since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where he will speak between August 6-12 2023",
      "limit": "10",
      "from_date": "2023-08-06",
      "to_date": "2023-08-12"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus OR TPUSA) since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus) since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Young Jewish Leadership Summit\" OR YJLS OR \"yjls2023\") since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11) (Iowa OR \"state fair\" OR \"Turning Point Action\" OR TPAction) since:2023-08-06 until:2023-08-13",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (summit OR event OR speaking) (Jewish OR Prager OR Dennis) since:2023-08-06 until:2023-08-13",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (speak OR speaking OR event OR appearance) (August OR 8/ OR \"this week\") since:2023-08-06 until:2023-08-13",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPAction since:2023-08-06 until:2023-08-13",
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
  "input_tokens": 17952,
  "input_tokens_details": {
    "cached_tokens": 9536
  },
  "output_tokens": 2577,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 20529,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 688697000,
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
    "input_tokens": 9827,
    "output_tokens": 2031
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688254728487219200",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688254728487219200"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690082877369909250",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690082877369909250"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689782188688957441",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689782188688957441"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689373382956167171",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689373382956167171"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690082274723921922",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690082274723921922"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688167189264658433",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688167189264658433"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690143188194058242",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690143188194058242"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690125789067710465",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690125789067710465"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688831363791851520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688831363791851520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690129392695922688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690129392695922688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690126885714558977",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690126885714558977"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689016515029504002",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689016515029504002"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690098712067129344",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690098712067129344"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690076903162486784",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690076903162486784"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689036415835779072",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689036415835779072"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689060193147953152",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689060193147953152"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689849723753205760",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689849723753205760"
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
    "url": "https://x.com/i/status/1688985672969773058",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688985672969773058"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690137974699429892",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690137974699429892"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690147935323852800",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690147935323852800"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1689649359460372481",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1689649359460372481"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688944326670266368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688944326670266368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688915406046769153",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688915406046769153"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690077319824834561",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690077319824834561"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690140409954275331",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690140409954275331"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690129129931481088",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690129129931481088"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1688831435799715840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1688831435799715840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1690139821434392576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1690139821434392576"
  }
]
```

## Grok response

```text
**All relevant X (Twitter) posts from the specified date range (2023-08-06 to 2023-08-12, using until:2023-08-13 for the end of the week) mentioning Charlie Kirk, TPUSA, or related events/speaking appearances are included below with full details. No summarization.** No direct posts from @charliekirk11 or @TPUSA about his personal speaking schedule were found in the range. The primary matching event is the TPUSA Young Jewish Leadership Summit (YJLS / #yjls2023) in Los Angeles, with attendee and speaker posts confirming activity during the week (notably August 10–11). One unrelated TPAction post about a Vivek Ramaswamy event is also included as it references the organization.

- **Post ID: 1690147935323852800**  
  Author: Juggy Gayles (@Rusty91104)  
  Timestamp: Fri, 11 Aug 2023 23:47:23 GMT  
  Content: You were speaking with one  
  Engagement: Likes=6, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=179  
  (Mentions speaking in context of Charlie Kirk/TPUSA discussion; no event details.)

- **Post ID: 1690143188194058242**  
  Author: Berkley Corey (@berkenstocks99)  
  Timestamp: Fri, 11 Aug 2023 23:28:32 GMT  
  Content: Such a phenomenal time tabling at the @TPUSA Young Jewish Leadership Summit and hearing @DennisPrager speak! 🙌🏻✨❤️🇺🇸  
  #dennisprager #yjls2023 #tpusa #turningpointusa #yjls #jewishsummit #youngjewishleadershipsummit #prageru #losangeles #charliekirk  
  Engagement: Likes=149, Reposts=26, Quotes=1, Replies=11, Bookmarks=2, Views=47907  
  Media: 4 photos (tabling/event scenes at the summit).  
  (Confirms TPUSA event in Los Angeles with speakers including Dennis Prager; attendee activity on Aug 11.)

- **Post ID: 1690129129931481088**  
  Author: I AM CHARLIE KIRK (@disagreesowhat)  
  Timestamp: Fri, 11 Aug 2023 22:32:40 GMT  
  Content: Victor & Ruben, love your resolve. Its NOT ENOUGH. Jara & BOT ran the table last evening! It was DISGUSTING. What are you doing today? Tomorrow? Why are teachers entering campus'?! Why such few negotiating sessions? Why is CCEA slow to act like other unions act (UPS, SAG AFTRA)?  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16  
  (Mentions "campus" in a union/education context tied to Charlie Kirk username; no public speaking event.)

- **Post ID: 1690126885714558977**  
  Author: I AM CHARLIE KIRK (@disagreesowhat)  
  Timestamp: Fri, 11 Aug 2023 22:23:45 GMT  
  Content: Victor & Ruben, love your resolve. Its NOT ENOUGH. Jara & BOT ran the table last evening! It was DISGUSTING. What are you doing today? Tomorrow? Why are teachers entering campus'?! Why such few negotiating sessions? Why is CCEA slow to act like other unions act (UPS, SAG AFTRA)?  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=27  
  (Duplicate/reply context to above; "campus" mention.)

- **Post ID: 1690098712067129344**  
  Author: Ian Haworth (@ighaworth)  
  Timestamp: Fri, 11 Aug 2023 20:31:48 GMT  
  Content: “Antisemitism is a conspiracy theory that’s built on ignorance, and the only treatment for ignorance is education.”  
  Had a great time speaking at @TPUSA’s “Young Jewish Leadership Summit”! #yjls2023  
  Engagement: Likes=8, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=855  
  Media: 1 photo.  
  (Speaker confirmation at TPUSA YJLS; event activity Aug 11.)

- **Post ID: 1690082877369909250**  
  Author: Jann in the Kush (@Jann83607320)  
  Timestamp: Fri, 11 Aug 2023 19:28:52 GMT  
  Content: Speaking of shams Charlie Kirk.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  (Casual mention of Charlie Kirk in "speaking" context; no event.)

- **Post ID: 1690082274723921922**  
  Author: slop machine (@corgoration)  
  Timestamp: Fri, 11 Aug 2023 19:26:29 GMT  
  Content: EXTREMELY excited for this one, will be on repeat  
  Engagement: Likes=6, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=401  
  (No direct relation to events; tangential.)

- **Post ID: 1690077319824834561**  
  Author: Charlie Kirk Fans Christ is King (@Kadidin_Newmai)  
  Timestamp: Fri, 11 Aug 2023 19:06:47 GMT  
  Content: You are speaking up because of no confidence motion, or else you won't  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  (Mentions "speaking up"; username tie to Charlie Kirk.)

- **Post ID: 1690076903162486784**  
  Author: I am CHARLIE KIRK (@manicracing6)  
  Timestamp: Fri, 11 Aug 2023 19:05:08 GMT  
  Content: An absolutely genuine question here....  
  Who do I contact regarding an event I'd like to organise for September next year 2024....  
  It will be a celebration of white people and only white people as per your black only event this year  
  Same sort of programme too  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=13  
  (Mentions organizing an "event"; username tie.)

- **Post ID: 1690140409954275331**  
  Author: Turning Point Action (@TPAction)  
  Timestamp: Fri, 11 Aug 2023 23:17:29 GMT  
  Content: Join Vivek Ramaswamy & Turning Point Action at the Iowa State Fair!  
  Saturday, August 12th  
  1:00 - 5:00 PM  
  Don’t miss this! 🇺🇸  
  Engagement: Likes=532, Reposts=74, Quotes=5, Replies=58, Bookmarks=1, Views=35525  
  Media: 1 photo.  
  (TPAction event announcement for Aug 12; no Charlie Kirk mention.)

- **Post ID: 1689782188688957441**  
  Author: Justine Brooke Murray (@Justine_Brooke)  
  Timestamp: Thu, 10 Aug 2023 23:34:03 GMT  
  Content: Looking forward to speaking at @TPUSA’s Young Jewish Leadership Summit tomorrow! See you in Commiefornia! ✈️  
  Engagement: Likes=7, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=517  
  (Pre-event speaker post for YJLS; confirms Aug 11 timing.)

- **Post ID: 1689649359460372481** (from @charliekirk11)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 10 Aug 2023 14:46:14 GMT  
  Content: A San Francisco tour company will charge $30 to explore the city's DOOM LOOP from City Hall to the Tenderloin and Union Square:  
  “We will view the open-air drug markets, the abandoned tech offices, the outposts of the non-profit industrial complex, and the deserted department stores.”  
  What a flaming turd of a city San Francisco has become.  
  Engagement: Likes=1736, Reposts=306, Quotes=37, Replies=257, Bookmarks=14, Views=417181  
  (No event/speaking announcement.)

**Additional notes from searches:**  
- No other posts from @charliekirk11 or @TPUSA in the range referenced speaking events, tours, or appearances.  
- Semantic search and other keyword variants returned unrelated or out-of-range results (e.g., movie showings, unrelated summits, or posts outside Aug 6–12).  
- The TPUSA Young Jewish Leadership Summit in Los Angeles is the only confirmed public speaking/appearance event tied to TPUSA/Charlie Kirk context during the week, based on multiple attendee and speaker posts (Aug 10–11 activity). No specific dates/times for Charlie Kirk himself were posted. All data extracted directly from tool results.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-08-06 to 2023-08-12**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-08-06 to 2023-08-12 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
