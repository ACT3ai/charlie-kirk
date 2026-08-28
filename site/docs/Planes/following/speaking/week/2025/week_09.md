---
unlisted: true
title: "Week 09 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W09"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-02-26 to 2025-03-04."
status: completed
hide_table_of_contents: true
---

# Week 09, 2025

- Date range: 2025-02-26 to 2025-03-04
- Queried at (UTC): 2026-08-24T19:17:26Z
- Model: grok-4.3
- API status: completed
- Response id: e4fb1cc0-d6a5-926e-a6d1-b5c778f32d31

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-02-26 to the end of the week 2025-03-04.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearance OR campus OR university) since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university OR TPUSA) since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university OR \"Charlie Kirk\") since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (speaking OR event OR \"will speak\" OR \"speaks at\" OR tour) since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, campus visits, or where Charlie will speak between Feb 26 and March 4 2025",
      "limit": "10",
      "from_date": "2025-02-26",
      "to_date": "2025-03-05"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"American Comeback Tour\") (USC OR \"University of Southern California\" OR \"at USC\") since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR speaking) (March OR \"next week\" OR upcoming OR \"will be\" OR \"coming to\") since:2025-02-26 until:2025-03-05",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (USC OR Florida OR \"University of Florida\" OR \"Florida State\" OR tour OR event) since:2025-02-26 until:2025-03-05",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (USC OR Florida OR \"University of Florida\" OR \"Florida State\" OR tour OR event) since:2025-02-26 until:2025-03-05",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA events at USC, University of Southern California, or any other locations in early March 2025",
      "limit": "5",
      "from_date": "2025-02-26",
      "to_date": "2025-03-05"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 31649,
  "input_tokens_details": {
    "cached_tokens": 14592
  },
  "output_tokens": 2761,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 34410,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 811421500,
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
    "input_tokens": 18536,
    "output_tokens": 2140
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1895182869070520592",
    "start_index": 1049,
    "end_index": 1110,
    "title": "1"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/charliekirk11/status/1895520674690879674",
    "start_index": 1269,
    "end_index": 1330,
    "title": "2"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1895201099927474215",
    "start_index": 1606,
    "end_index": 1659,
    "title": "3"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TPUSA/status/1895530471255310536",
    "start_index": 1848,
    "end_index": 1901,
    "title": "4"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/HelenCasey1970/status/1896696921328357764",
    "start_index": 2127,
    "end_index": 2189,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/CaptainCarson11/status/1896692700847677907",
    "start_index": 2335,
    "end_index": 2398,
    "title": "6"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/HelenCasey1970/status/1896696921328357764",
    "start_index": 2569,
    "end_index": 2631,
    "title": "5"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/Elmagico42o/status/1896682868937748775",
    "start_index": 2918,
    "end_index": 2977,
    "title": "7"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/JWheelertv/status/1896672682500112449",
    "start_index": 3139,
    "end_index": 3197,
    "title": "8"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/thebenroyer/status/1896667045581971736",
    "start_index": 3565,
    "end_index": 3624,
    "title": "9"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/eyeoftheSTORMsd/status/1896651795922886913",
    "start_index": 3804,
    "end_index": 3868,
    "title": "10"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/TaggartRearden/status/1896701130119512244",
    "start_index": 3979,
    "end_index": 4042,
    "title": "11"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/JWheelertv/status/1896689127359480186",
    "start_index": 4256,
    "end_index": 4315,
    "title": "12"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/REALCAWOMAN1776/status/1896686813827457189",
    "start_index": 4410,
    "end_index": 4474,
    "title": "13"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/PaulaDuvall2/status/1896684507698508044",
    "start_index": 4644,
    "end_index": 4705,
    "title": "14"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/SaveLibertyUS/status/1896683567318728998",
    "start_index": 4830,
    "end_index": 4892,
    "title": "15"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/tpusafaith/status/1896603119255253440",
    "start_index": 5230,
    "end_index": 5289,
    "title": "16"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/gabe_saint35/status/1895927640022007918",
    "start_index": 5461,
    "end_index": 5522,
    "title": "17"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/JonathanWShanks/status/1895507382262014015",
    "start_index": 5674,
    "end_index": 5738,
    "title": "18"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/tpusafaith/status/1895504238416953620",
    "start_index": 5929,
    "end_index": 5988,
    "title": "19"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/gabe_saint35/status/1895365386511753395",
    "start_index": 6218,
    "end_index": 6279,
    "title": "20"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/tpusa_gaso/status/1895319503535513761",
    "start_index": 6424,
    "end_index": 6483,
    "title": "21"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/JakePoling/status/1895223717019681037",
    "start_index": 6725,
    "end_index": 6784,
    "title": "22"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/tpusafaith/status/1895163682868601028",
    "start_index": 6975,
    "end_index": 7034,
    "title": "23"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (2025-02-26 to 2025-03-04, with searches extending slightly into 03-05 for completeness) mentioning Charlie Kirk or TPUSA public speaking events, appearances, tours, or speaking locations are included below without summarization.** Posts were retrieved via keyword and semantic searches focused on events, speaking, tours, campuses, universities, "American Comeback Tour," and related terms. Only posts with explicit or direct references to events/appearances in this period are listed; unrelated or non-event posts (e.g., general commentary) were excluded.

### Posts from @charliekirk11 (Charlie Kirk's account):
- [post:12] ID: 1895182869070520592 (Thu, 27 Feb 2025 18:43:01 GMT): "We're at the University of Florida today for the second stop of the American Comeback Tour with @TPUSA. There's INCREDIBLE energy on the ground with thousands of young patriots showing up. So much campus momentum. Never seen anything like it. The kids are alright!! 🇺🇸🇺🇸" (Media: videos and photo of the event).[[1]](https://x.com/charliekirk11/status/1895182869070520592)
- [post:9] ID: 1895520674690879674 (Fri, 28 Feb 2025 17:05:20 GMT): "Already INSANE energy at Florida State University today 🔥 WE ARE SO BACK" (Media: video).[[2]](https://x.com/charliekirk11/status/1895520674690879674)

### Posts from @TPUSA (Turning Point USA's account):
- [post:18] ID: 1895201099927474215 (Thu, 27 Feb 2025 19:55:28 GMT): "Today’s crowd at the University of Florida for our second stop of the American Comeback Tour with @charliekirk11 🇺🇸 WE ARE SO BACK!!!!" (Media: video).[[3]](https://x.com/TPUSA/status/1895201099927474215)
- [post:17] ID: 1895530471255310536 (Fri, 28 Feb 2025 17:44:16 GMT): "Florida State University students break out the war chant at today's tour stop with @charliekirk11 🇺🇸" (Media: video).[[4]](https://x.com/TPUSA/status/1895530471255310536)

### Other posts mentioning events/appearances (including USC on March 3, 2025):
- [post:1] ID: 1896696921328357764 (Mon, 03 Mar 2025 22:59:19 GMT): "JUST IN: USC campus police arrest a second person at Charlie Kirk's event."[[5]](https://x.com/HelenCasey1970/status/1896696921328357764)
- [post:5] ID: 1896693789126988233 (Mon, 03 Mar 2025 22:42:33 GMT): "Lmao why is Charlie Kirk at my campus debating" (Media: video of the event).[[6]](https://x.com/CaptainCarson11/status/1896692700847677907)
- [post:19] ID: 1896696921328357764 (Mon, 03 Mar 2025 22:59:19 GMT): "JUST IN: USC campus police arrest a second person at Charlie Kirk's event." (Duplicate of [post:1]).[[5]](https://x.com/HelenCasey1970/status/1896696921328357764)
- [post:21] ID: 1896682868937748775 (Mon, 03 Mar 2025 22:03:29 GMT): "🇺🇸‼️Los Angeles, Happening Now: Charlie Kirk is at USC debating students about DEI. At least 1 Antifa member arrested by USC Police.‼️ campus police arrest a second person at Charlie Kirk’s event.‼️" (Media: videos).[[7]](https://x.com/Elmagico42o/status/1896682868937748775)
- [post:22] ID: 1896672682500112449 (Mon, 03 Mar 2025 21:23:00 GMT): "BREAKING: USC campus police arrest a second person at Charlie Kirk’s event" (Media: video).[[8]](https://x.com/JWheelertv/status/1896672682500112449)
- [post:23] ID: 1896667045581971736 (Mon, 03 Mar 2025 21:00:36 GMT): "For a school that has had low public political organization since encampments were removed in May, the University of Southern California seems quite open to having right-wing commentator Charlie Kirk and his Turning Point USA-hosted “American Comeback Tour” in the campus’ center." (Media: photo).[[9]](https://x.com/thebenroyer/status/1896667045581971736)
- [post:26] ID: 1896651795922886913 (Mon, 03 Mar 2025 20:00:00 GMT): "Eye of the STORM LIVE-> The American Comeback Tour with Charlie Kirk" (Link to a live broadcast of the tour).[[10]](https://x.com/eyeoftheSTORMsd/status/1896651795922886913)
- [post:38] ID: 1896701130119512244 (Mon, 03 Mar 2025 23:16:03 GMT): "Fight on! 🇺🇸 Good job @USC & @TPUSA 😁🙌".[[11]](https://x.com/TaggartRearden/status/1896701130119512244)
- [post:40] ID: 1896689127359480186 (Mon, 03 Mar 2025 22:28:21 GMT): "Charlie Kirk, at USC, goes after progressive Jewish Americans. “Liberal Jews are funding their own demise every day,” he says." (Media: video).[[12]](https://x.com/JWheelertv/status/1896689127359480186)
- [post:42] ID: 1896686813827457189 (Mon, 03 Mar 2025 22:19:09 GMT): "USC...AND CHARLIE KIRK".[[13]](https://x.com/REALCAWOMAN1776/status/1896686813827457189)
- [post:43] ID: 1896684507698508044 (Mon, 03 Mar 2025 22:09:59 GMT): "AWESOME!!!!!!!!!!!!!!!! USC is my father's Alma Mater!! 🇺🇸♥️😁 You're a WINNER, Charlie Kirk!! 💪💪💪".[[14]](https://x.com/PaulaDuvall2/status/1896684507698508044)
- [post:44] ID: 1896683567318728998 (Mon, 03 Mar 2025 22:06:15 GMT): "Wow… massive crowd at USC listening to Charlie Kirk!".[[15]](https://x.com/SaveLibertyUS/status/1896683567318728998)

### Additional related posts (mentions of upcoming or other TPUSA/Charlie Kirk events in/around the period):
- [post:45] ID: 1896603119255253440 (Mon, 03 Mar 2025 16:46:35 GMT): "@charliekirk11 will be speaking at Faith Forward Pastors' Summit in Gainesville, GA on March 18 - 20." (Note: Outside the core week but referenced in range).[[16]](https://x.com/tpusafaith/status/1896603119255253440)
- [post:47] ID: 1895927640022007918 (Sat, 01 Mar 2025 20:02:28 GMT): "Another event happening with @tpusa_uwyo1776 on March 27th!" (RSVP link provided; outside core week).[[17]](https://x.com/gabe_saint35/status/1895927640022007918)
- [post:49] ID: 1895507382262014015 (Fri, 28 Feb 2025 16:12:31 GMT): "@realalexclark will be here 3/20!" (At Franciscan University; outside core week).[[18]](https://x.com/JonathanWShanks/status/1895507382262014015)
- [post:50] ID: 1895504238416953620 (Fri, 28 Feb 2025 16:00:01 GMT): "@AWatsonOLY will be speaking at Faith Forward Pastors' Summit in Gainesville, GA on March 18 - 20." (Outside core week).[[19]](https://x.com/tpusafaith/status/1895504238416953620)
- [post:51] ID: 1895365386511753395 (Fri, 28 Feb 2025 06:48:16 GMT): "If you are in or around Laramie next week, you should check out the @tpusa_uwyo1776 event that is happening!" (RSVP link; "next week" aligns with early March).[[20]](https://x.com/gabe_saint35/status/1895365386511753395)
- [post:52] ID: 1895319503535513761 (Fri, 28 Feb 2025 03:45:57 GMT): "Will Witt is coming to Georgia Southern on April 1st" (Outside core week).[[21]](https://x.com/tpusa_gaso/status/1895319503535513761)
- [post:53] ID: 1895223717019681037 (Thu, 27 Feb 2025 21:25:20 GMT): "Looking forward to speaking in Michigan next week on how to stand up for your values as a student..." (From a TPUSA regional manager; "next week" aligns with early March).[[22]](https://x.com/JakePoling/status/1895223717019681037)
- [post:54] ID: 1895163682868601028 (Thu, 27 Feb 2025 17:26:47 GMT): "@lucasmiles will be speaking at Faith Forward Pastors' Summit in Gainesville, GA on March 18 - 20." (Outside core week).[[23]](https://x.com/tpusafaith/status/1895163682868601028)

No other posts in the searches directly detailed additional Charlie Kirk or TPUSA speaking events, locations, or schedules strictly within 2025-02-26 to 2025-03-04 beyond the University of Florida (Feb 27), Florida State University (Feb 28), and USC (March 3, part of the American Comeback Tour). Posts reference the ongoing "American Comeback Tour" with Charlie Kirk and TPUSA. All data from tool results is included verbatim where relevant.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-02-26 to 2025-03-04**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2025-03-03](/Planes/Incidents/N582MM-2025-03-03-KHHR) | [N582MM](/Planes/N582MM/overview) | [KHHR](/Planes/Airports/KHHR) | Hawthorne, CA | Charlie | **Same day** |
| [2025-03-03](/Planes/Incidents/N872RA-2025-03-03-KVNY) | [N872RA](/Planes/N872RA/overview) | [KVNY](/Planes/Airports/KVNY) | Van Nuys, CA | Charlie | **Same day** |
| [2025-03-04](/Planes/Incidents/N582MM-2025-03-04-KHHR) | [N582MM](/Planes/N582MM/overview) | [KHHR](/Planes/Airports/KHHR) | Hawthorne, CA | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
