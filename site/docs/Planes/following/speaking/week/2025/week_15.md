---
unlisted: true
title: "Week 15 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W15"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-04-09 to 2025-04-15."
status: completed
hide_table_of_contents: true
---

# Week 15, 2025

- Date range: 2025-04-09 to 2025-04-15
- Queried at (UTC): 2026-08-24T19:17:55Z
- Model: grok-4.3
- API status: completed
- Response id: d7d7f089-65b3-9817-b8b6-9a3a862c7d19

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-04-09 to the end of the week 2025-04-15.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR events OR \"public speaking\" OR appearance OR tour OR campus) since:2025-04-09 until:2025-04-16",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR events OR \"public speaking\" OR appearance OR tour OR campus) since:2025-04-09 until:2025-04-16 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between April 9 and April 15 2025",
      "limit": "10",
      "from_date": "2025-04-09",
      "to_date": "2025-04-15",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "Charlie Kirk",
      "count": "5"
    },
    "status": "completed"
  },
  {
    "name": "x_user_search",
    "input": {
      "query": "TPUSA",
      "count": "5"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (Boise OR \"Boise State\" OR Purdue OR MSU OR Michigan OR UConn OR Connecticut OR \"American Comeback Tour\") since:2025-04-09 until:2025-04-16",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR tour OR speak OR speaking OR Purdue OR Boise OR MSU) since:2025-04-09 until:2025-04-16",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR tour OR speak OR speaking OR Purdue OR Boise OR MSU) since:2025-04-09 until:2025-04-16",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1911917626546405526"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1911910297507701012"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1911889296283361520"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1911837577729950117"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 29254,
  "input_tokens_details": {
    "cached_tokens": 13568
  },
  "output_tokens": 3596,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 32850,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 913111000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 12,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 17134,
    "output_tokens": 3099
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910761105917628687",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910761105917628687"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1965983581798555648",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1965983581798555648"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910109232428351530",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910109232428351530"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/491719838",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/491719838"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910099549986910209",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910099549986910209"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911867258051416204",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911867258051416204"
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
    "url": "https://x.com/i/status/1910387051314503795",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910387051314503795"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911924386724196725",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911924386724196725"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911889296283361520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911889296283361520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911917376385519879",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911917376385519879"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911837577729950117",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911837577729950117"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1909765701101031514",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1909765701101031514"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911851196068790643",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911851196068790643"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911917752836596026",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911917752836596026"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/2014285051173773312",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/2014285051173773312"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/292929271",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/292929271"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911907295602287091",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911907295602287091"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911666395554762837",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911666395554762837"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911924210672271450",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911924210672271450"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1560011403519348736",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1560011403519348736"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910000175369928881",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910000175369928881"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910489034654171355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910489034654171355"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911921915427438963",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911921915427438963"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911919883689898135",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911919883689898135"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911262696038928520",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911262696038928520"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911912516223115392",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911912516223115392"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910420170734252078",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910420170734252078"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911917258676539688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911917258676539688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911917626546405526",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911917626546405526"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1909803276528501103",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1909803276528501103"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911918800120975497",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911918800120975497"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1966575521493643265",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1966575521493643265"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911919161258762458",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911919161258762458"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911912345494045139",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911912345494045139"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911905888752771167",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911905888752771167"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/19274342",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/19274342"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1577047350089961473",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1577047350089961473"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/1529565023902674944",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/1529565023902674944"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911861631812092254",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911861631812092254"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910103579890680317",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910103579890680317"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/user/775339747472400385",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/user/775339747472400385"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1911910297507701012",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1911910297507701012"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910496773967405167",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910496773967405167"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1910386895135346780",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1910386895135346780"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1909817812585267445",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1909817812585267445"
  }
]
```

## Grok response

```text
**Here is all the relevant X (Twitter) post data** from the searches for Charlie Kirk or TPUSA/Turning Point USA public speaking events, appearances, tours, or speaking locations, strictly within the date range **2025-04-09 to 2025-04-15** (using `until:2025-04-16` to capture up to the end of April 15). No summarization—full post content, metadata, and threads where fetched are included verbatim. Only posts with direct or referenced event details are shown; irrelevant or off-topic posts were filtered out in the process.

### Posts about Purdue University (American Comeback Tour / Prove Me Wrong event)
- **Post ID: 1911910297507701012**  
  **Author:** TONY™ (@TONYxTWO)  
  **Timestamp:** Mon, 14 Apr 2025 22:31:51 GMT  
  **Content:** Holy smokes!!   
  Look at this turnout for Charlie Kirk at Purdue!!!   
  The next generation is in good hands 🔥👇🏼  
  *(Media: Video of large crowd at the event)*  
  **Engagement:** Likes=61298, Reposts=8826, Quotes=256, Replies=901, Bookmarks=727, Views=766114  

  **Thread replies (selected relevant):**  
  - **Post ID: 1911917376385519879** (Author: Tom @sweetNsour2341, Timestamp: Mon, 14 Apr 2025 22:59:58 GMT): 🔥 Massive turnout at Purdue for Charlie Kirk’s American Comeback Tour! Hundreds rally for conservative values at a liberal stronghold. Is this a sign Gen Z is shifting right? Drop your take! 🗣️ #CharlieKirkAtPurdue  
  - **Post ID: 1911912516223115392** (Author: GinnyM @PatriotXV11, Timestamp: Mon, 14 Apr 2025 22:40:40 GMT): 🚨🚨🚨 Look at Charlie Kirk’s turnout at Purdue! I do believe a change is overdue.  
  - **Post ID: 1911919883689898135** (Author: Lisa Moser @Boilermaker86, Timestamp: Mon, 14 Apr 2025 23:09:56 GMT): No it’s not. Purdue is very conservative. So is the surrounding area.  
  - **Post ID: 1911919161258762458** (Author: Ftworthfan @ftworthfan, Timestamp: Mon, 14 Apr 2025 23:07:04 GMT): Go Purdue!  
  - **Post ID: 1911917752836596026** (Author: Born in a Small Town @BornT8060, Timestamp: Mon, 14 Apr 2025 23:01:28 GMT): Lol! West Lafayette IN is NOT a liberal area and Purdue is a Conservative college. Kirk will be well received. 🇺🇸  
  - **Post ID: 1911921915427438963** (Author: TDBuckeyes @StetsonSpurs19D, Timestamp: Mon, 14 Apr 2025 23:18:01 GMT): Impressive @Purdue that's more students than a home football game!!!! Just kidding!!! O - H At least you aren't Wisconsin! Lolol, See you this fall! Have a fun Spring and great Summer...!!!! I - O  
  - **Post ID: 1911924210672271450** (Author: Civitas @ReddDorn, Timestamp: Mon, 14 Apr 2025 23:27:08 GMT): Purdue students are incredibly bright and driven.  
  - **Post ID: 1911919677866995916** (Author: LH-America First @lor66301, Timestamp: Mon, 14 Apr 2025 23:09:07 GMT): The younger generation especially males (but some females) are starting to understand the repercussion of a so called Democratic (socialist/communist) party. They want to bring Prosperity back so they can own homes and find the American dream again. They understand it will not happen under the far left rule.  
  - **Post ID: 1912015992936366570** (Author: Laurie @LaurieGrayson, Timestamp: Tue, 15 Apr 2025 05:31:50 GMT): This is our future!!! Not the protesting aliens on student visa trying to disrupt!! These young adults are hungry for the truth and Charlie Kurk gives it to them. So no matter how big the AOC & Bernie crowd is don’t forget this crowd is bigger and hungry they ARE THE FUTURE!!  
  - **Post ID: 1911921012486070552** (Author: DocM @NotThatDocM, Timestamp: Mon, 14 Apr 2025 23:14:25 GMT): The future of America is conservative  

- **Post ID: 1910387051314503795** (from @charliekirk11)  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 10 Apr 2025 17:39:00 GMT  
  **Content:** Another INSANE crowd at Purdue University today.   
  I’m telling you, the energy on these college campuses is unlike anything I’ve ever seen.   
  🇺🇸🇺🇸🇺🇸  
  *(Media: 4 items including photos and videos of the crowd)*  
  **Engagement:** Likes=30680, Reposts=4075, Quotes=184, Replies=1124, Bookmarks=400, Views=1431300  

- **Post ID: 1910420170734252078** (from @TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 10 Apr 2025 19:50:37 GMT  
  **Content:** At Purdue’s “Prove Me Wrong” event with @charliekirk11, here’s how one protester reacted when TPUSA Contributor @topheronx tried to have a simple conversation.  
  @tpusastudents  
  *(Media: Video)*  
  **Engagement:** Likes=3605, Reposts=1147, Quotes=170, Replies=1069, Bookmarks=187, Views=248237  

- **Post ID: 1910386895135346780** (from @TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Thu, 10 Apr 2025 17:38:23 GMT  
  **Content:** The American Comeback Tour with @charliekirk11 hit Purdue University—and the students showed out. 🔥🇺🇸  
  @tpusastudents  
  *(Media: Photo)*  
  **Engagement:** Likes=390, Reposts=49, Quotes=3, Replies=13, Bookmarks=10, Views=13478  

### Posts about Boise State University (American Comeback Tour)
- **Post ID: 1911917626546405526**  
  **Author:** Idaho Republican News (@RepublicanIdaho)  
  **Timestamp:** Mon, 14 Apr 2025 23:00:58 GMT  
  **Content:** Charlie Kirk is bringing the American Comeback Tour to Boise State University tomorrow, April 15th at 12PM MDT. Idaho Republican News will be there covering the event and capturing footage to help spotlight Turning Point USA’s message to young conservatives across Idaho 🇺🇸   
  #BoiseState #CharlieKirk #TPUSA #idaho #AmericanComebackTour #IdahoNews #news #IdahoRepublican  
  *(Media: Video)*  
  **Engagement:** Likes=13, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=827  

- **Post ID: 1911917258676539688**  
  **Author:** Idaho News Now (@idaho_now)  
  **Timestamp:** Mon, 14 Apr 2025 22:59:30 GMT  
  **Content:** UPDATE: The organizers of the Charlie Kirk Event are requesting people park in the Lincoln Avenue Garage. While the event itself will take place across the street at Boise Intramural Field.  
  **Engagement:** Likes=15, Reposts=5, Quotes=0, Replies=0, Bookmarks=0, Views=793  

- **Post ID: 1911861631812092254**  
  **Author:** Paige Adams (@paigeadams1218)  
  **Timestamp:** Mon, 14 Apr 2025 19:18:28 GMT  
  **Content:** Attention @tpusastudents at @BoiseState!! Charlie Kirk will be on campus tomorrow!! You won’t want to miss it! RSVP below!!🎉👏🏻🤯🇺🇸🫡  
  🔗: https://tpusa.com/events/  
  #tpusa #freespeech #usa #biggovsucks #tpusastudents #socialismsucks #studentactivism #freedom  
  *(Media: Video)*  
  **Engagement:** Likes=12, Reposts=5, Quotes=1, Replies=0, Bookmarks=0, Views=943  

### Posts about Michigan State University (MSU) (American Comeback Tour)
- **Post ID: 191051** (referenced via link in post below; direct event post from search)  
  **Post ID: 1910761105917628687** (from @TPUSA)  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Fri, 11 Apr 2025 18:25:22 GMT  
  **Content:** Massive turnout today at Michigan State University for the American Comeback Tour with @charliekirk11 🇺🇸  
  @tpusastudents  
  *(Media: Video)*  
  **Engagement:** Likes=428, Reposts=73, Quotes=7, Replies=19, Bookmarks=7, Views=66886  

- **Post ID: 1911837577729950117**  
  **Author:** Kathleen Hawkins (@kjhawkins47)  
  **Timestamp:** Mon, 14 Apr 2025 17:42:53 GMT  
  **Content:** Charlie Kirk debates MSU students on ‘The American Comeback Tour,’ receives mixed welcome https://statenews.com/article/2025/04/charlie-kirks-american-comeback-tour-makes-a-stop-at-msu  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=57  

### Posts about UConn / Connecticut (TPUSA event with Alex Stein)
- **Post ID: 1911889296283361520**  
  **Author:** The Connecticut Centinal (@CTCentinal)  
  **Timestamp:** Mon, 14 Apr 2025 21:08:24 GMT  
  **Content:** Alex Stein Debates UConn Students On Trans Issues, Abortion And More At TPUSA Event  
  https://connecticutcentinal.com/culture/2025/04/14/alex-stein-debates-uconn-students-on-trans-issues-abortion-and-more-at-tpusa-event/  
  **Engagement:** Likes=49, Reposts=19, Quotes=2, Replies=3, Bookmarks=4, Views=10819  

  **Thread replies (selected relevant):**  
  - **Post ID: 1911890886767559103** (Author: Anthony St.Pierre @astpierre55, Timestamp: Mon, 14 Apr 2025 21:14:43 GMT): Great crowd and great event! Glad you were able to make it! 🇺🇸  
  - **Post ID: 1911894623640756257** (Author: Erik Unfiltered Podcast @eriknotsorry, Timestamp: Mon, 14 Apr 2025 21:29:34 GMT): 🤣🤣🤣 fucking furrys🤣🤣🤣 I'm rolling!!!  
  - **Post ID: 1912015896429707409** (Author: Quadziki @quadziki, Timestamp: Tue, 15 Apr 2025 05:31:27 GMT): Change that ugly ahh pic of me 😭🫵🏻  

### Other related mentions (Davis, CA / UCDavis TPUSA event disruption)
- **Post ID: 1911918800120975497** (and duplicate in second search)  
  **Author:** Heidi Edelweiss 🇺🇸🇩🇪 (@IMpwdx4x9bz)  
  **Timestamp:** Mon, 14 Apr 2025 23:05:38 GMT  
  **Content:** Have to ask: HOW MANY DEAD/TRAUMATIZED KIDS are acceptable to the Leftist-Progressive Politicians & their MSM, like @CAgovernor ? @UCDavisPolice @cityofdavispd DID NOTHING while UNHINGED Protesters DESTROYED @TPUSA EVENT. #LivesDontMatter2ActBlue #UCDavis #Sanctuary #Homeless #ActBlue #cartels #terrorists #EnoughIsEnough @POTUS @AGPamBondi @FBIDDBongoni @TheOfficerTatum  
  *(Quotes a post about a shooting at a Picnic Day event)*  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=23  

### Additional TPUSA event mentions (no specific date/location in range but referenced)
- **Post ID: 1911905888752771167**  
  **Author:** Adam Thomas Dommeyer (@AdamDommeyer)  
  **Timestamp:** Mon, 14 Apr 2025 22:14:20 GMT  
  **Content:** REGISTRATION IS OPEN! Register for #SAS2025 NOW! This will be an EPIC @TPUSA event in sunny Florida! It’ll be YUGE! You won’t wanna miss this! 🌴🌴🌴🌴 @tpusastudents @tpusafaith @TPUSAEvents  
  *(Media: Photo)*  
  **Engagement:** Likes=12, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=2338  

No direct posts from @charliekirk11 or @TPUSA announcing events on April 9 specifically in the range (one April 9 post from Charlie Kirk was a podcast, not an event). All data pulled exclusively from the specified week. No other locations or events matched the exact criteria.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-04-09 to 2025-04-15**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2025-04-09 to 2025-04-15 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
