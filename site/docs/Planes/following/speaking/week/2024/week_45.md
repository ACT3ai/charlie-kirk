---
unlisted: true
title: "Week 45 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W45"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-11-04 to 2024-11-10."
status: completed
hide_table_of_contents: true
---

# Week 45, 2024

- Date range: 2024-11-04 to 2024-11-10
- Queried at (UTC): 2026-08-24T19:15:37Z
- Model: grok-4.3
- API status: completed
- Response id: c7346d31-46b3-9a7a-98df-1c7bf124c769

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-11-04 to the end of the week 2024-11-10.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR \"public speaking\" OR campus OR university OR college) since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR \"public speaking\" OR campus OR university OR college) since:2024-11-04 until:2024-11-11 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR \"public speaking\" OR campus OR university OR college) since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR \"public speaking\" OR campus OR university OR college) since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between November 4 and November 10 2024",
      "limit": "10",
      "from_date": "2024-11-04",
      "to_date": "2024-11-11"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR \"speaking at\" OR \"speaking event\" OR campus OR university OR college OR \"prove me wrong\" OR \"brainwashed tour\") since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Seattle OR Auburn OR \"Grand Canyon\" OR Phoenix OR \"Georgia voters\" OR Georgia) (event OR speaking OR speak OR tour OR appearance) since:2024-11-04 until:2024-11-11",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (campus OR university OR college OR event OR speaking OR tour OR \"prove me wrong\" OR \"brainwashed\") since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (campus OR university OR college OR event OR speaking OR tour OR \"prove me wrong\" OR \"brainwashed\" OR Auburn) since:2024-11-04 until:2024-11-11",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (tour OR \"brainwashed tour\" OR \"prove me wrong\" OR campus) since:2024-11-04 until:2024-11-11",
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
  "input_tokens": 28126,
  "input_tokens_details": {
    "cached_tokens": 13376
  },
  "output_tokens": 2510,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 30636,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 773877000,
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
    "input_tokens": 16186,
    "output_tokens": 1806
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1855017064458863103",
    "start_index": 248,
    "end_index": 309,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854250154720653453",
    "start_index": 309,
    "end_index": 370,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854241338835018188",
    "start_index": 370,
    "end_index": 431,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854228541602181450",
    "start_index": 431,
    "end_index": 492,
    "title": "4"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854064472517693890",
    "start_index": 492,
    "end_index": 553,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1853512685066862793",
    "start_index": 553,
    "end_index": 614,
    "title": "6"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1853478124387995890",
    "start_index": 614,
    "end_index": 675,
    "title": "7"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1855017064458863103",
    "start_index": 1492,
    "end_index": 1553,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854250154720653453",
    "start_index": 1926,
    "end_index": 1987,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854241338835018188",
    "start_index": 2384,
    "end_index": 2445,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854228541602181450",
    "start_index": 2838,
    "end_index": 2899,
    "title": "4"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1854064472517693890",
    "start_index": 3151,
    "end_index": 3212,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1853512685066862793",
    "start_index": 3563,
    "end_index": 3624,
    "title": "6"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1853478124387995890",
    "start_index": 4246,
    "end_index": 4307,
    "title": "7"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1854608437990003073",
    "start_index": 4728,
    "end_index": 4781,
    "title": "8"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1854294779770642784",
    "start_index": 4950,
    "end_index": 5003,
    "title": "9"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/FrontlinesTPUSA/status/1855399541224423642",
    "start_index": 5394,
    "end_index": 5458,
    "title": "10"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/FrontlinesTPUSA/status/1855399541224423642",
    "start_index": 5458,
    "end_index": 5522,
    "title": "10"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/ldhvcufash/status/1855390748067156095",
    "start_index": 5721,
    "end_index": 5780,
    "title": "11"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/PatriotVerity/status/1854727605536145757",
    "start_index": 6222,
    "end_index": 6284,
    "title": "12"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/KariLake/status/1853517963111936290",
    "start_index": 6644,
    "end_index": 6701,
    "title": "13"
  }
]
```

## Grok response

```text
**No posts in the specified date range (2024-11-04 to 2024-11-10, inclusive) directly announce or detail upcoming or scheduled public speaking events, appearances, tours, or locations where Charlie Kirk or TPUSA will speak during that exact week.**[[1]](https://x.com/charliekirk11/status/1855017064458863103)[[2]](https://x.com/charliekirk11/status/1854250154720653453)[[3]](https://x.com/charliekirk11/status/1854241338835018188)[[4]](https://x.com/charliekirk11/status/1854228541602181450)[[5]](https://x.com/charliekirk11/status/1854064472517693890)[[6]](https://x.com/charliekirk11/status/1853512685066862793)[[7]](https://x.com/charliekirk11/status/1853478124387995890)

All retrieved posts from keyword and semantic searches (including from @charliekirk11, @TPUSA, and general mentions) focus on **past or completed activities** from the recent semester/election cycle, retrospective reflections on the 2024 election, or unrelated topics. Here is every relevant post returned, reproduced in full with no summarization or omission:

### Posts from @charliekirk11 (Charlie Kirk's account):
- Post ID 1855017064458863103 (Fri, 08 Nov 2024 22:38:27 GMT): "BREAKING: James O'Keefe just exposed that: Ruben Gallego hates Kari Lake so much that 'he wants her to die.' Sen. Sinema had an unwritten rule that ASU gets whatever it wants, setting herself up for President of the university. Corruption is already getting exposed." (Quote of James O'Keefe post about Sinema/ASU; no event mention.)[[1]](https://x.com/charliekirk11/status/1855017064458863103)
- Post ID 1854250154720653453 (Wed, 06 Nov 2024 19:51:01 GMT): "Kari Lake has a chance of winning. We will be streaming TONIGHT to go over all of this. There are over 1 million votes outstanding and she's currently only down 59,000 votes. Lots of RED votes left to count. Trump expanding his margins which could carry Kari." (Streaming announcement, not a speaking event.)[[2]](https://x.com/charliekirk11/status/1854250154720653453)
- Post ID 1854241338835018188 (Wed, 06 Nov 2024 19:15:59 GMT): "Our Prove Me Wrong campus debate clips were seen 2.1 billion times this semester on TikTok, IG, 𝕏 and YouTube. The vast majority of those were viewed by 18-29-year-olds, and the Kamala campaign never knew how to counter. YOUNG PEOPLE SHOWED UP FOR TRUMP 🔥🔥" (Retrospective on "Prove Me Wrong" campus debates/clips; no future dates.)[[3]](https://x.com/charliekirk11/status/1854241338835018188)
- Post ID 1854228541602181450 (Wed, 06 Nov 2024 18:25:08 GMT): "🚨BREAKING: Jack Smith's prosecution is OVER: 'The DOJ, where Jack Smith works, cannot prosecute a sitting president… Fox News is told that Jack Smith will be gone from his post as special counsel, meaning the cases will be gone before Trump takes the oath of office on January 20.' I'm not tired of winning." (No event details.)[[4]](https://x.com/charliekirk11/status/1854228541602181450)
- Post ID 1854064472517693890 (Wed, 06 Nov 2024 07:33:11 GMT): "Grand Canyon University in Phoenix, Arizona CELEBRATING Trump’s HISTORIC VICTORY 🇺🇸" (With video; references a past visit/celebration at GCU, not a scheduled speaking event in the range.)[[5]](https://x.com/charliekirk11/status/1854064472517693890)
- Post ID 1853512685066862793 (Mon, 04 Nov 2024 19:00:35 GMT): "24 campus visited this semester. Over 1 billion social media views. Tens of thousands of Gen Z voters registered. Over 250K low prop votes chased. Countless minds changed. We left it all out on the field. Let’s win. 🇺🇸🇺🇸🇺🇸" (With video; retrospective summary of semester campus visits.)[[6]](https://x.com/charliekirk11/status/1853512685066862793)
- Post ID 1853478124387995890 (Mon, 04 Nov 2024 16:43:15 GMT): "Listen to these young Georgia voters terrified that the American Dream is slipping away for them. At every single campus I’ve visit in the last year, over 40 total, this is the number one fear I hear. They don’t think they’ll ever own a home or afford to have a family. They feel like their government cares more about illegal migrants than them. They know Trump, a businessman who has already successfully shepherded one of the greatest economies in American history, will do it again." (With video; references past campus visits in Georgia and elsewhere.)[[7]](https://x.com/charliekirk11/status/1853478124387995890)

### Posts from @TPUSA (Turning Point USA account):
- Post ID 1854608437990003073 (Thu, 07 Nov 2024 19:34:43 GMT): "Georgetown University Offers Students “Self-Care Suite” with Coloring Books, Hot Chocolate to Relieve Post-Election Stress https://tpusa.com/live/georgetown-university-offer-students-self-care-suite-with-coloring-books-hot-chocolate-to-relieve-post-election-stress/" (Link to article; no speaking event.)[[8]](https://x.com/TPUSA/status/1854608437990003073)
- Post ID 1854294779770642784 (Wed, 06 Nov 2024 22:48:21 GMT): "Last night at Auburn University:" (With video; references a past event/appearance at Auburn University.)[[9]](https://x.com/TPUSA/status/1854294779770642784)

### Other relevant posts mentioning Charlie Kirk or TPUSA (general search results):
- Post ID 1855399541224423642 (Sat, 09 Nov 2024 23:58:16 GMT, @FrontlinesTPUSA): "SEATTLE: ANTIFA agitators dressed in black bloc made an appearance at the protest at the Space Needle. @TPUSA | @choeshow" (With video; references a protest in Seattle involving TPUSA, not a speaking event by Charlie Kirk.)[[10]](https://x.com/FrontlinesTPUSA/status/1855399541224423642)[[10]](https://x.com/FrontlinesTPUSA/status/1855399541224423642)
- Post ID 1855390748067156095 (Sat, 09 Nov 2024 23:23:20 GMT, @ldhvcufash): "How Charlie Kirk's 'Brainwashed' Tour Helped Reelect Trump - Newsweek" (Mentions the "Brainwashed Tour" retrospectively.)[[11]](https://x.com/ldhvcufash/status/1855390748067156095)
- Post ID 1854727605536145757 (Fri, 08 Nov 2024 03:28:14 GMT, @PatriotVerity): "A lot of people were surprised to see President Trump winning Arizona in the early vote & on election day. I found this video from Grand Canyon University (GCU) in Phoenix, AZ where @charliekirk11 & @TPUSA went for their 'You're Being Brainwashed' Tour. It all makes sense now." (With video; references past "You're Being Brainwashed" Tour stop at GCU/Phoenix.)[[12]](https://x.com/PatriotVerity/status/1854727605536145757)
- Post ID 1853517963111936290 (Mon, 04 Nov 2024 19:21:33 GMT, @KariLake): "‼️ YOU’RE INVITED! 🇺🇸 We have a rally TONIGHT in Prescott, AZ at the County Courthouse Square — this will be a HISTORIC event. Don’t miss out! For more information visit: https://t.co/V6sZ4ivWZC I hope to see you there! ♥️" (Kari Lake rally; unrelated to Charlie Kirk/TPUSA speaking.)[[13]](https://x.com/KariLake/status/1853517963111936290)

**All other posts returned** (e.g., discussions of voter registration, election reactions, unrelated events, or quotes) contain no mentions of scheduled speaking events, tours, appearances, or locations for Charlie Kirk or TPUSA in the 2024-11-04 to 2024-11-10 window. Searches for specific terms like "Brainwashed Tour," "Prove Me Wrong," campus events, or combinations with locations (Seattle, Auburn, Phoenix/GCU, Georgia) yielded only historical references. No announcements of future events within or immediately after the range were found.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-11-04 to 2024-11-10**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-11-04 to 2024-11-10 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
