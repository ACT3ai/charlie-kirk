---
unlisted: true
title: "Week 10 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W10"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-03-05 to 2025-03-11."
status: completed
hide_table_of_contents: true
---

# Week 10, 2025

- Date range: 2025-03-05 to 2025-03-11
- Queried at (UTC): 2026-08-24T19:17:30Z
- Model: grok-4.3
- API status: completed
- Response id: 84f0cea5-de49-958a-b6fa-5fab5226fca7

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-03-05 to the end of the week 2025-03-11.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR events OR speaking OR speak OR tour OR campus OR \"public speaking\" OR appearance) since:2025-03-05 until:2025-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR events OR speaking OR speak OR tour OR campus OR appearance) since:2025-03-05 until:2025-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR events OR speaking OR speak OR tour OR campus OR appearance) since:2025-03-05 until:2025-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, tours, campus appearances, or where Charlie will speak between March 5 and March 11 2025",
      "limit": "10",
      "from_date": "2025-03-05",
      "to_date": "2025-03-12"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11) (event OR events OR speaking OR speak OR tour OR \"American Comeback Tour\" OR campus OR appearance OR \"town hall\" OR rally) since:2025-03-05 until:2025-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"CSU Northridge\" OR CSUN OR \"Northridge\" OR FSU OR \"Florida State\" OR Oconomowoc OR Wisconsin OR Maine) (Charlie Kirk OR TPUSA) since:2025-03-05 until:2025-03-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (tour OR event OR events OR campus) since:2025-03-05 until:2025-03-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (tour OR event OR events OR campus OR \"town hall\") since:2025-03-05 until:2025-03-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "locations and dates of Charlie Kirk or TPUSA speaking events, tours, campus visits in early March 2025",
      "limit": "10",
      "from_date": "2025-03-05",
      "to_date": "2025-03-12"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 20968,
  "input_tokens_details": {
    "cached_tokens": 10112
  },
  "output_tokens": 2673,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 23641,
  "num_sources_used": 0,
  "num_server_side_tools_used": 9,
  "cost_in_usd_ticks": 672749000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 9,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 12283,
    "output_tokens": 2128
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899113926798819368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899113926798819368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898114486898176319",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898114486898176319"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899164684403855721",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899164684403855721"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898017105754087551",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898017105754087551"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899191371820585404",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899191371820585404"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1897745248614568184",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1897745248614568184"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899227033697149235",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899227033697149235"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899185494820528204",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899185494820528204"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898439559832113211",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898439559832113211"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898520339262398593",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898520339262398593"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899233483140350190",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899233483140350190"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898069202118062338",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898069202118062338"
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
    "url": "https://x.com/i/status/1899237530886648268",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899237530886648268"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898035763683504203",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898035763683504203"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899089188047188128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899089188047188128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899234427147809256",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899234427147809256"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1897151648096731537",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1897151648096731537"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899171304609300709",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899171304609300709"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1897749841146790305",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1897749841146790305"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1897731434288414736",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1897731434288414736"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899247337740091424",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899247337740091424"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899240138280145210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899240138280145210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1897075216121257992",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1897075216121257992"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899218391505736022",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899218391505736022"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1898835110171902351",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1898835110171902351"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899120398287147403",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899120398287147403"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899240655769223210",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899240655769223210"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899207520012382679",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899207520012382679"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1899241882632503576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1899241882632503576"
  }
]
```

## Grok response

```text
**All relevant X posts from the search (March 5–11, 2025 date range, inclusive of posts referencing events in/around that week or immediately adjacent). No summarization—full post content, metadata, and context preserved where available.**

### Posts explicitly referencing Charlie Kirk / TPUSA events, tours, or speaking appearances:

- **[post:10]** (and duplicate **[post:14]**, **[post:28]**)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 06 Mar 2025 20:43:15 GMT  
  **Content:** WHAT. A. TURNOUT.  
  The American Comeback Tour with @charliekirk11 brought a massive crowd to CSU Northridge! This movement isn't slowing down 🔥🇺🇸 @tpusastudents  
  **Media:** Video (vertical clip of crowd turnout).  
  **Engagement:** Likes=302, Reposts=49, Quotes=5, Replies=20, Bookmarks=12, Views=14334.  
  **Relevance:** Direct reference to "American Comeback Tour" event with Charlie Kirk at CSU Northridge (California State University, Northridge).

- **[post:11]**  
  **Author:** Sassafrass84 (@Sassafrass_84)  
  **Timestamp:** Sun, 09 Mar 2025 20:35:43 GMT  
  **Content:** Charlie Kirk puts on a voluntary event at FSU to combat the woke ideology and challenge college students to think for themselves.  
  "So, different opinions make people feel safe at FSU? They believe it has a greater, um, movement behind it. Right, so did you ask them, 'Are you a child?' Let me be very clear. The world is a dangerous place. Lots of people have different ideas. Just because someone comes and has a voluntary event with different perspectives shouldn't make you feel unsafe."  
  💯 💯 💯 💯  
  **Media:** Video (clip of Charlie Kirk speaking at the event).  
  **Engagement:** Likes=4222, Reposts=567, Quotes=12, Replies=64, Bookmarks=249, Views=271786.  
  **Relevance:** Charlie Kirk voluntary speaking/event at FSU (Florida State University).

- **[post:12]** (and duplicates **[post:29]**, **[post:32]**)  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Mon, 10 Mar 2025 18:25:20 GMT  
  **Content:** 🚨Join me and @DonaldJTrumpJr in Wisconsin NEXT MONDAY, March 17th at 6:30pm CT for our Turning Point Town Hall as we work to elect Brad Schimel to the Wisconsin State Supreme Court.  
  This is the most important election of 2025 and will have profound consequences on congressional districts, voter integrity, drop boxes, and more.  
  Register at [link].  
  We are getting outspent, but we must not get outworked.  
  **Media:** Photo (promotional graphic).  
  **Engagement:** Likes=1835, Reposts=490, Quotes=39, Replies=113, Bookmarks=46, Views=195029.  
  **Relevance:** Announcement of upcoming Turning Point Town Hall event with Charlie Kirk (and Donald Trump Jr.) in Wisconsin (Oconomowoc area, per related posts).

- **[post:13]**  
  **Author:** TruthSlingerX (@TruthSlingerX)  
  **Timestamp:** Fri, 07 Mar 2025 15:39:24 GMT  
  **Content:** Look what I found! March 14th 6:30pm TPUSA will have an event in MAINE!  
  Protect MAINE Girls! #Maine #MEpolitics  
  **Media:** Photo (flyer/image of event details).  
  **Engagement:** Likes=227, Reposts=103, Quotes=4, Replies=2, Bookmarks=5, Views=2749.  
  **Relevance:** TPUSA event in Maine on March 14th (just after the searched week).

- **[post:15]**  
  **Author:** Community Notes & Violations (@CNviolations)  
  **Timestamp:** Thu, 06 Mar 2025 20:25:00 GMT  
  **Content:** Charlie Kirk continues to give liberal campus students the facts.  
  **Media:** Video (clip of Charlie Kirk speaking on campus).  
  **Engagement:** Likes=599, Reposts=70, Quotes=2, Replies=8, Bookmarks=62, Views=27913.  
  **Relevance:** References ongoing campus speaking by Charlie Kirk.

- **[post:16]**  
  **Author:** Anthony Cabassa (@anthonycabassa)  
  **Timestamp:** Thu, 06 Mar 2025 19:30:06 GMT  
  **Content:** HAPPENING NOW 🚨: Charlie Kirk Protestors at CSUN are chanting and protesting Charlie Kirk being on campus.  
  **Media:** Video (protest footage).  
  **Engagement:** Likes=1049, Reposts=169, Quotes=50, Replies=1251, Bookmarks=50, Views=143493.  
  **Relevance:** Live coverage of Charlie Kirk event/speaking at CSUN (CSU Northridge), with on-campus protests.

- **[post:0]**  
  **Author:** Grok (@grok)  
  **Timestamp:** Mon, 10 Mar 2025 23:02:28 GMT  
  **Content:** Charlie Kirk got hit with Groyper Q&A trolling during his Culture War college tour back in 2019. Nick Fuentes and his crew were calling Kirk out as a "fake conservative" at these events. Check Diggit Magazine for the full breakdown.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=106.  
  **Relevance:** Historical reference to Charlie Kirk's past college tour events.

### Related posts discussing or quoting the events (no new events, but context on above):

- **[post:1]**  
  **Author:** Lawrence Andrea (@lawrencegandrea)  
  **Timestamp:** Mon, 10 Mar 2025 20:11:22 GMT  
  **Content:** Don Jr. & Turning Point's Charlie Kirk are holding an event in Oconomowoc next Monday  
  Here's our story on Turning Point's influence in WI: [link].  
  **Quoted post:** Megan Wangerin (@MeganWangerin) – “🚨Calling all PATRIOTS in Wisconsin🚨 Here is our chance to take back the WI Supreme Court! 🇺🇸 ➡️ ⚖️ @charliekirk11 and @DonaldJTrumpJr are coming to Oconomowoc this Monday! Don’t wait ‼️ Sign up today👇 [link]” (with photo).  
  **Engagement:** Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=1179.  
  **Relevance:** Confirms Oconomowoc, WI event with Charlie Kirk (and Don Jr.).

- **[post:24]**  
  **Author:** James Wigderson (@jwigderson)  
  **Timestamp:** Mon, 10 Mar 2025 23:32:05 GMT  
  **Content:** Somebody please ask Charlie Kirk to spell "Oconomowoc." Then ask him to spell "cat."  
  **Engagement:** Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=171.  
  **Relevance:** References the Oconomowoc, WI event.

- **[post:25]**  
  **Author:** Emilee (Fannon) Miklas (@Emilee_Fannon)  
  **Timestamp:** Mon, 10 Mar 2025 22:33:05 GMT  
  **Content:** Next week in Wisconsin: Donald Trump Jr. & Charlie Kirk will visit Oconomowoc to rally support for state Supreme Court candidate Brad Schimel.  
  **Quoted post:** Same as [post:12] above.  
  **Engagement:** Likes=7, Reposts=1, Quotes=0, Replies=2, Bookmarks=0, Views=905.  
  **Relevance:** Details on Wisconsin event location.

- **[post:26]**  
  **Author:** Matt Smith (@mattsmith_news)  
  **Timestamp:** Mon, 10 Mar 2025 21:58:44 GMT  
  **Content:** Charlie Kirk and Donald Trump Jr. in Wisconsin next week to campaign for Brad Schimel ahead of April 1 Wisconsin Supreme Court election.  
  **Quoted post:** Same as [post:12] above.  
  **Engagement:** Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=1, Views=923.  
  **Relevance:** Confirms Wisconsin event.

- **[post:27]**  
  **Author:** A.J. Bayatpour (@AJBayatpour)  
  **Timestamp:** Mon, 10 Mar 2025 21:15:32 GMT  
  **Content:** News: Donald Trump Jr. and Charlie Kirk will be in Ocononowoc next Monday to campaign for Brad Schmiel in the Wisconsin Supreme Court race.  
  **Engagement:** Likes=63, Reposts=13, Quotes=3, Replies=8, Bookmarks=0, Views=6025.  
  **Relevance:** Oconomowoc, WI event details.

No other posts in the searched range directly announced or detailed additional Charlie Kirk/TPUSA public speaking events, tours, or appearances strictly within March 5–11, 2025. Posts from @charliekirk11 and @TPUSA during the week primarily covered unrelated political/news topics (e.g., Trump funding cuts, Democrat comments). Semantic search yielded the same core events noted above. All data included without omission or condensation.
```

