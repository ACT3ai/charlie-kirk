---
unlisted: true
title: "Week 21 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W21"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-05-20 to 2024-05-26."
status: completed
hide_table_of_contents: true
---

# Week 21, 2024

- Date range: 2024-05-20 to 2024-05-26
- Queried at (UTC): 2026-08-24T19:12:35Z
- Model: grok-4.3
- API status: completed
- Response id: cac4c330-9d8a-9024-8036-76a12518ea5c

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-05-20 to the end of the week 2024-05-26.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR \"will be speaking\" OR \"speaking at\" OR \"speaking event\") since:2024-05-20 until:2024-05-27",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR speaking) (2024 OR May) since:2024-05-20 until:2024-05-27",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between May 20-26 2024",
      "limit": "10",
      "from_date": "2024-05-20",
      "to_date": "2024-05-26",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR \"Peoples Convention\" OR TPUSA OR \"Turning Point\") since:2024-05-20 until:2024-05-27",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR convention OR \"Charlie Kirk\") since:2024-05-20 until:2024-05-27",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA) (Michigan OR Detroit OR Arizona OR \"May 25\" OR \"May 24\" OR \"May 26\" OR \"May 23\" OR \"May 22\" OR \"May 21\" OR \"May 20\") (event OR speaking OR speak) since:2024-05-20 until:2024-05-27",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk TPUSA events or speaking appearances May 20 to May 26 2024",
      "limit": "10",
      "from_date": "2024-05-20",
      "to_date": "2024-05-26",
      "min_score_threshold": "0.05"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR @charliekirk11 OR @TPUSA) (event OR speaking OR speak OR appearance OR tour OR \"will speak\" OR \"speaking at\" OR \"on stage\" OR \"speaking event\") since:2024-05-20 until:2024-05-27 -from:charliekirk11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "Charlie Kirk (Michigan OR Detroit OR Arizona OR Phoenix OR \"May 25\" OR \"May 24\" OR \"May 26\") (event OR speaking) since:2024-05-20 until:2024-05-27",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1794505845234933972"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 33524,
  "input_tokens_details": {
    "cached_tokens": 20672
  },
  "output_tokens": 2051,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 35575,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 753269000,
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
    "input_tokens": 14216,
    "output_tokens": 1389
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794507575704088860",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794507575704088860"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794466902930268234",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794466902930268234"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793260601591865727",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793260601591865727"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794479330417938487",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794479330417938487"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794471881955057826",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794471881955057826"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793770863118172455",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793770863118172455"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794018092000870700",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794018092000870700"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794409407314317420",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794409407314317420"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794066902827798724",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794066902827798724"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1792672619050991821",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1792672619050991821"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793082561461436880",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793082561461436880"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794030500002378017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794030500002378017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794171672192487725",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794171672192487725"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794505845234933972",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794505845234933972"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794344011831857390",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794344011831857390"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794325768190996528",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794325768190996528"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793074372712022241",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793074372712022241"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794417691547369721",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794417691547369721"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794513194649817327",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794513194649817327"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794493365612118355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794493365612118355"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1792700459180040540",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1792700459180040540"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794380094095679680",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794380094095679680"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794458387259826289",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794458387259826289"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794064309036937565",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794064309036937565"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1792359547870531806",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1792359547870531806"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793817859937955993",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793817859937955993"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794443840742736378",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794443840742736378"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794407193762017302",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794407193762017302"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794144731544588764",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794144731544588764"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1792359284992610405",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1792359284992610405"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1793703562830385603",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1793703562830385603"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794472501445038162",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794472501445038162"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1792909252459106373",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1792909252459106373"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794496968666083665",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794496968666083665"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794180699265618220",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794180699265618220"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1794505372302278950",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1794505372302278950"
  }
]
```

## Grok response

```text
**All relevant X posts from the search (May 20–26, 2024, inclusive of the week ending May 26) mentioning Charlie Kirk or TPUSA in the context of public speaking events, appearances, or where Charlie will speak are included below in full (no summarization). Only posts with any direct or implied connection to events/speaking were returned; irrelevant or zero-result queries were omitted.**

### Posts from Charlie Kirk (@charliekirk11):
- **Post ID: 1794064309036937565** (May 24, 2024, 17:53:58 GMT)  
  Content: 🚨NEW SPEAKER DROP🚨  
  Turning Point Action's The Peoples Convention June 14-16 in Detroit just got even better.  
  Just three weeks away!   
  Tickets👉 https://t.co/fY9yd2b1PB  
  @realDonaldTrump @VivekGRamaswamy @RealBenCarson @DonaldJTrumpJr @RealCandaceO @bennyjohnson @TulsiGabbard @ByronDonalds @KristiNoem @KariLake @Nigel_Farage @SenRickScott @JackPosobiec @kimguilfoyle @EliCrane_CEO @leemzeldin @RogerJStoneJr @WarrenDavidson @TomKlingenstein @mattgaetz @TheOfficerTatum @ScottPresler @EricBurlison @realMikeLindell @RepCloudTX  
  Ignore the polls.   
  Register voters.  
  Chase ballots.  
  Let's go!!  
  🇺🇸🇺🇸  
  (Media: 1 photo)  
  Engagement: Likes=2427, Reposts=574, Quotes=54, Replies=341, Bookmarks=75, Views=573630

- **Post ID: 1794066902827798724** (May 24, 2024, 18:04:16 GMT) – Reply to above thread  
  Content: Thank you. It's going to be an important event. All ACTION  
  Engagement: Likes=68, Reposts=5, Quotes=0, Replies=13, Bookmarks=0, Views=4159

- **Post ID: 1793082561461436880** (May 22, 2024, 00:52:51 GMT)  
  Content: Our faith team has a major win to celebrate today!  
  TPUSA Faith just hit 3,000 official church partners! These are churches we have established a relationship with which are actively working to register voters and defend liberty.  
  A major milestone!  
  Onward!  
  (Media: 1 photo)  
  Engagement: Likes=640, Reposts=112, Quotes=8, Replies=75, Bookmarks=7, Views=57741

### Other relevant posts mentioning Charlie Kirk or TPUSA events/speaking (May 20–26, 2024):
- **Post ID: 1794505845234933972** (May 25, 2024, 23:08:28 GMT)  
  Author: @Curry_Crab1  
  Content: Charlie Kirk is having an event in Michigan, Bannon will be on the floor hosting his show, you can talk to him there, meet more maga people  
  (Thread context/reply: User @JoshuaMorott states they are not on location there.)  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=30

- **Post ID: 1794443840742736378** (May 25, 2024, 19:02:05 GMT)  
  Author: @AFpost  
  Content: Trump scheduled to headline Detroit TPUSA event in June.  
  Follow: @AFpost  
  (Media: 1 photo)  
  Engagement: Likes=178, Reposts=12, Quotes=2, Replies=8, Bookmarks=0, Views=10369

- **Post ID: 1794171672192487725** (May 25, 2024, 01:00:35 GMT)  
  Author: @BarryMarkson1 (quoting @RonFilipkowski)  
  Content: Kari Lake keeps showing us how extreme she is. On stage at a TPUSA event with anti-Semites, racists and conspiracy theorists. Kari isn’t pro business or pro Arizona. Kari is a conspiracy theorist and nothing more.  
  Engagement: Likes=92, Reposts=35, Quotes=2, Replies=12, Bookmarks=0, Views=16253

- **Post ID: 1792672619050991821** (May 20, 2024, 21:43:53 GMT)  
  Author: @DebbieSchlussel  
  Content: Yup. And they are all having a circle jerk in Detroit in June to coincide with the Trump, Candace TPUSA event there. I'm sure the Nazis will go over very well in Detroit  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=32

- **Post ID: 1792359547870531806** (May 20, 2024, 00:59:51 GMT)  
  Author: @DebbieSchlussel  
  Content: Fuentes is having his national convention in Detroit in June to coincide with TPUSA event featuring Trump and Nick's buddy Candace. Who is funding the event? (American First PAC)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=43

- **Post ID: 1792359284992610405** (May 20, 2024, 00:58:48 GMT)  
  Author: @DebbieSchlussel  
  Content: Fuentes is having his national convention in Detroit in June to coincide with TPUSA event featuring Trump and Nick's buddy Candace. Who is funding the event? (American First PAC)  
  Engagement: Likes=5, Reposts=2, Quotes=4, Replies=2, Bookmarks=0, Views=4039

No posts from @TPUSA were found in the date range. No other posts in the searched range directly referenced Charlie Kirk or TPUSA public speaking events, tours, or appearances specifically occurring between May 20–26, 2024 (most references point to future June events in Detroit/Michigan). All data from tool results is included verbatim above.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-05-20 to 2024-05-26**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-05-20 to 2024-05-26 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
