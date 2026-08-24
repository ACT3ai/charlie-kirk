---
unlisted: true
title: "Week 10 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W10"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-03-05 to 2022-03-11."
status: completed
hide_table_of_contents: true
---

# Week 10, 2022

- Date range: 2022-03-05 to 2022-03-11
- Queried at (UTC): 2026-08-24T19:00:01Z
- Model: grok-4.3
- API status: completed
- Response id: 7dd5650e-ae2a-9362-a5ef-5502d804c037

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-03-05 to the end of the week 2022-03-11.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR campus OR \"will be\" OR appears OR appearance OR \"speaking at\" OR \"speaks at\") since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (tour OR \"speaking tour\" OR \"campus tour\") since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR campus) since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus) since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSAevents (event OR speaking OR speak OR tour OR campus) since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between March 5-11 2022",
      "limit": "10",
      "from_date": "2022-03-05",
      "to_date": "2022-03-12"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\") (event OR gala OR speaking OR \"speaks at\" OR appearance OR \"will speak\" OR \"speaking tour\" OR campus) since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Florida OR gala OR Prager OR \"Babylon Bee\") since:2022-03-05 until:2022-03-12",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"TPUSA\" (event OR tour OR speaking OR campus) since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2022-03-05 until:2022-03-12",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Kids & Country Gala\" OR \"Florida Citizens Alliance\") (Charlie OR Kirk OR TPUSA) since:2022-03-05 until:2022-03-12",
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
  "input_tokens": 22907,
  "input_tokens_details": {
    "cached_tokens": 9152
  },
  "output_tokens": 8056,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 30963,
  "num_sources_used": 0,
  "num_server_side_tools_used": 12,
  "cost_in_usd_ticks": 991641500,
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
    "input_tokens": 15227,
    "output_tokens": 7414
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501995784522326019",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501995784522326019"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501298536289161217",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501298536289161217"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501914519425064964",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501914519425064964"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501256433316282375",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501256433316282375"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501288454742757379",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501288454742757379"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501188485121593344",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501188485121593344"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501226837950697473",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501226837950697473"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500894049095589889",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500894049095589889"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501973596058669068",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501973596058669068"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501657834873782275",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501657834873782275"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501611145790046212",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501611145790046212"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502061395533348865",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502061395533348865"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501618835325132808",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501618835325132808"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501191921812844546",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501191921812844546"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501481786127564800",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501481786127564800"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501552131597291521",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501552131597291521"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501710539038154754",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501710539038154754"
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
    "url": "https://x.com/i/status/1501180942173491202",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501180942173491202"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500549577337933837",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500549577337933837"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501948829507014662",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501948829507014662"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500939985473531912",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500939985473531912"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502055717343309832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502055717343309832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500963820092674052",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500963820092674052"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501283110440214532",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501283110440214532"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501275781107884032",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501275781107884032"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501309529987813376",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501309529987813376"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501983076733227009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501983076733227009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501270997046992900",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501270997046992900"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501509203055321094",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501509203055321094"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500836627836456963",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500836627836456963"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502035837890052099",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502035837890052099"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501415916218707969",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501415916218707969"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502024971048075267",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502024971048075267"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501559932881149955",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501559932881149955"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501332347291013120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501332347291013120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501910580055191556",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501910580055191556"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500565161265954816",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500565161265954816"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501717505408217095",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501717505408217095"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502059206370897937",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502059206370897937"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501338637744623620",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501338637744623620"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501519415845822476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501519415845822476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1500852522021363718",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1500852522021363718"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502018940586930178",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502018940586930178"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1502027424405635078",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1502027424405635078"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501400528126763016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501400528126763016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501966277446938632",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501966277446938632"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1501719302784778240",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1501719302784778240"
  }
]
```

## Grok response

```text
**Here is all the raw data from the X/Twitter searches for posts mentioning Charlie Kirk, TPUSA, or Turning Point USA in connection with public speaking events, appearances, tours, campus visits, or where Charlie Kirk would speak, limited to the date range March 5–11, 2022 (posts timestamped March 5 to March 11 inclusive).** No summarization or filtering applied beyond the search parameters. All matching posts and their full metadata are included below, grouped by tool/search for clarity. No other relevant posts were found in the results.

### Keyword search results (general queries for events/speaking/tour/campus + date range):
- **[post:0]** ID: 1502059206370897937  
  Author: Just Meg 🇺🇸🙏🏻❤️ - @Meggiebee59  
  Timestamp: Thu, 10 Mar 2022 23:09:56 GMT  
  Content: Gorgeous. 💕💕. It’s just a number. Will be 63 in August. Have enjoyed every minute! ☺️☺️😎😎  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:1]** ID: 1502055717343309832  
  Author: Florida Citizens Alliance - @go_flca  
  Timestamp: Thu, 10 Mar 2022 22:56:04 GMT  
  Content: What a special event last night! Thank you to Charlie Kirk, Dennis Prager, and The Babylon Bee for joining us at our Kids & Country Gala last evening🤍  
  And of course thank you to the 500 PEOPLE that joined us. Florida, you are amazing!🇺🇸  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Media: 4 photos (event-related images)

- **[post:2]** ID: 1502035837890052099  
  Author: We miss Charlie Kirk - @legaldawn  
  Timestamp: Thu, 10 Mar 2022 21:37:04 GMT  
  Content: and it's about to get worse. Ukraine is part of the Great Reset and Russia isn't. Elites know that if Ukraine loses, great reset loses. Although I do not like civilians being killed, Russia appears to be our only hope for freedom and that makes NO SENSE!  
  (Quote of unrelated post)  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:3]** ID: 1502027424405635078  
  Author: Cyrus Never forget Charlie Kirk - @thaicargo  
  Timestamp: Thu, 10 Mar 2022 21:03:38 GMT  
  Content: I wonder why we see EU generals , Russian Generals , American Generals speaking but not ONE Ukrainian I wonder why?!  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:4]** ID: 1502024971048075267  
  Author: Ναταλί Γλέζου 🕊 الانت�اضة سوف تنتصر - @NataliGlezou  
  Timestamp: Thu, 10 Mar 2022 20:53:54 GMT  
  Content: Russia will NEVER N E V E R abandon Donbas and Donetsk there live Russians and Russian speaking people anti fascists who resisted West’s Coup … Perhaps if we reach such a turning point Russian Army will realize that there is no other alternative than reassuring peoples’ lives…  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:5]** ID: 1502018940586930178  
  Author: Adam Thomas Dommeyer - @AdamDommeyer  
  Timestamp: Thu, 10 Mar 2022 20:29:56 GMT  
  Content: Here is my @TPUSA #TPUSAFaith March 2022 speaking schedule:  
  March 13- Ottertail, MN  
  March 15- Rosemount, MN  
  March 19- Wisconsin Dells, WI  
  March 21- Burlington, WI  
  March 23- Moorhead, MN  
  March 28- Woodbury, MN  
  Message me for details! 🇺🇸  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:6]** ID: 1501995784522326019  
  Author: Noreal’s Event 💜 - @ojegbalemeh  
  Timestamp: Thu, 10 Mar 2022 18:57:55 GMT  
  Content: At this moment everyone is feeling the stress in this UAR.  
  Please let’s get our PVC  
  2023 has to be a turning point.  
  Enough is enough.  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:7]** ID: 1501983076733227009  
  Author: Austin Nealeigh - @AustinN  
  Timestamp: Thu, 10 Mar 2022 18:07:25 GMT  
  Content: This coming Monday!! You won’t want to miss this freedom loving fun event! Tons of amazing raffle prizes as well! #biggovsucks #Brandontatum #oregon #Conservative #2a #portland #tpusa  
  Engagement: Likes=1, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Media: 1 photo (event flyer)

- **[post:8]** ID: 1501966277446938632  
  Author: crazy8wizard - @crazy8wizard  
  Timestamp: Thu, 10 Mar 2022 17:00:40 GMT  
  Content: I don’t mind that the Grand Inquisitor doesn’t match his appearance in Rebels or even that he doesn’t match the Pau’ans in ROTS. My problem is that the head prosthetics make his head look bigger than his face and it reminds me of those shrunken face Charlie Kirk memes  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Media: 2 photos

- **[post:9]** ID: 1501910580055191556  
  Author: Daily 'Bad Takes' Wire - @DailyWireCutter  
  Timestamp: Thu, 10 Mar 2022 13:19:21 GMT  
  Content: Also, people like Matt Walsh openly want the ability to use the N-Word else no one can use it. Yet I bet, if I went to a TPUSA event, called him a cracker and a groyper, wore a shirt with this photo on it, he'd ironically want to restrict my speech and take the mic away.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Media: 1 photo

- **[post:10]** ID: 1501717505408217095 (and related)  
  Author: summer SAW NO MORE DREAM - @essentricseason  
  Timestamp: Thu, 10 Mar 2022 00:32:08 GMT  
  Content: This is where I tell the story where when TPUSA visited my campus they spent a long time yelling until eventually they told me “this is the fault of the Jews in Hollywood”  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:11]** ID: 1501618835325132808  
  Author: Christine GEeeeeee - @Christi07343333  
  Timestamp: Wed, 09 Mar 2022 18:00:03 GMT  
  Content: I agree shouldn't it be called international "People that bleed" Day. Has a nice ring to it except it implies people that are wounded in a war or an event.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:12]** ID: 1501509203055321094  
  Author: Campus Reform - @campusreform  
  Timestamp: Wed, 09 Mar 2022 10:44:25 GMT  
  Content: March Madness Liberal Bias Bracket:  
  Which shows the worst liberal bias?  
  TPUSA Club Suspended vs. Professor Defends Pedophilia  
  Engagement: Likes=0, Reposts=0, Quotes=1, Replies=1, Bookmarks=0, Views=N/A

- **[post:13]** ID: 1501288454742757379  
  Author: Steve Benedict - @SteveBenedict17  
  Timestamp: Tue, 08 Mar 2022 20:07:14 GMT  
  Content: Speaking of grooming, why do kids who attend TPUSA events have to sign a waiver releasing you from liability for rape?  
  Engagement: Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:14]** ID: 1501191921812844546  
  Author: Evan - @ereller25  
  Timestamp: Tue, 08 Mar 2022 13:43:39 GMT  
  Content: I got what you meant. Personally I think the whole debate over campus speech is overblown and exacerbated by right wing trolls. Seems like when people pitch a fit they've usually got a segment on Fox and a job offer from TPUSA immediately after.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:15]** ID: 1500963820092674052  
  Author: Populist Pundit - @PunditPopulist  
  Timestamp: Mon, 07 Mar 2022 22:37:15 GMT  
  Content: This led to the infamous 'populist wars' where followers of Saurabh Sharma bullied Charlie Kirk for his 'market fundamentalism' on his campus tour, which, in turn, led to the creation of American Moment.  
  Engagement: Likes=45, Reposts=2, Quotes=0, Replies=4, Bookmarks=6, Views=N/A  
  Media: 1 photo

### Specific Florida/Kids & Country Gala search results (March 5–11, 2022):
- **[post:16]** ID: 1502055717343309832 (duplicate of post:1 above)  
  Author: Florida Citizens Alliance - @go_flca  
  Timestamp: Thu, 10 Mar 2022 22:56:04 GMT  
  Content: What a special event last night! Thank you to Charlie Kirk, Dennis Prager, and The Babylon Bee for joining us at our Kids & Country Gala last evening🤍  
  And of course thank you to the 500 PEOPLE that joined us. Florida, you are amazing!🇺🇸  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Media: 4 photos

- **[post:17]** ID: 1501973596058669068  
  Author: Liam Adams - @liamsadams  
  Timestamp: Thu, 10 Mar 2022 17:29:45 GMT  
  Content: Charlie Kirk, just sitting next to Dennis Prager and the Eric Metaxas booth.  
  Engagement: Likes=2, Reposts=1, Quotes=1, Replies=1, Bookmarks=0, Views=N/A  
  Media: 3 photos

### TPUSA-specific search results (March 5–11, 2022):
- **[post:18]** ID: 1502018940586930178 (duplicate of post:5 above)  
  Author: Adam Thomas Dommeyer - @AdamDommeyer  
  Timestamp: Thu, 10 Mar 2022 20:29:56 GMT  
  Content: Here is my @TPUSA #TPUSAFaith March 2022 speaking schedule:  
  March 13- Ottertail, MN  
  March 15- Rosemount, MN  
  March 19- Wisconsin Dells, WI  
  March 21- Burlington, WI  
  March 23- Moorhead, MN  
  March 28- Woodbury, MN  
  Message me for details! 🇺🇸  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:19]** ID: 1501983076733227009 (duplicate of post:7 above)  
  Author: Austin Nealeigh - @AustinN  
  Timestamp: Thu, 10 Mar 2022 18:07:25 GMT  
  Content: This coming Monday!! You won’t want to miss this freedom loving fun event! Tons of amazing raffle prizes as well! #biggovsucks #Brandontatum #oregon #Conservative #2a #portland #tpusa  
  Engagement: Likes=1, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Media: 1 photo

- **[post:20]** ID: 1501910580055191556 (duplicate of post:9 above)  
  Author: Daily 'Bad Takes' Wire - @DailyWireCutter  
  Timestamp: Thu, 10 Mar 2022 13:19:21 GMT  
  Content: Also, people like Matt Walsh openly want the ability to use the N-Word else no one can use it. Yet I bet, if I went to a TPUSA event, called him a cracker and a groyper, wore a shirt with this photo on it, he'd ironically want to restrict my speech and take the mic away.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Media: 1 photo

- **[post:21]** ID: 1501717505408217095 (duplicate of post:10 above)  
  Author: summer SAW NO MORE DREAM - @essentricseason  
  Timestamp: Thu, 10 Mar 2022 00:32:08 GMT  
  Content: This is where I tell the story where when TPUSA visited my campus they spent a long time yelling until eventually they told me “this is the fault of the Jews in Hollywood”  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A

- **[post:22]** ID: 1501618835325132808 (duplicate of post:11 above)  
  Author: Christine GEeeeeee - @Christi07343333  
  Timestamp: Wed, 09 Mar 2022 18:00:03 GMT  
  Content: I agree shouldn't it be called international "People that bleed" Day. Has a nice ring to it except it implies people that are wounded in a war or an event.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:23]** ID: 1501509203055321094 (duplicate of post:12 above)  
  Author: Campus Reform - @campusreform  
  Timestamp: Wed, 09 Mar 2022 10:44:25 GMT  
  Content: March Madness Liberal Bias Bracket:  
  Which shows the worst liberal bias?  
  TPUSA Club Suspended vs. Professor Defends Pedophilia  
  Engagement: Likes=0, Reposts=0, Quotes=1, Replies=1, Bookmarks=0, Views=N/A

- **[post:24]** ID: 1501288454742757379 (duplicate of post:13 above)  
  Author: Steve Benedict - @SteveBenedict17  
  Timestamp: Tue, 08 Mar 2022 20:07:14 GMT  
  Content: Speaking of grooming, why do kids who attend TPUSA events have to sign a waiver releasing you from liability for rape?  
  Engagement: Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

- **[post:25]** ID: 1501191921812844546 (duplicate of post:14 above)  
  Author: Evan - @ereller25  
  Timestamp: Tue, 08 Mar 2022 13:43:39 GMT  
  Content: I got what you meant. Personally I think the whole debate over campus speech is overblown and exacerbated by right wing trolls. Seems like when people pitch a fit they've usually got a segment on Fox and a job offer from TPUSA immediately after.  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A

### @charliekirk11 account posts (March 5–11, 2022; no direct event announcements):
- **[post:26]** ID: 1501710539038154754  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Thu, 10 Mar 2022 00:04:27 GMT  
  Content: If our leaders believed Putin was truly an existential threat to our national security, why was the US involved in multiple high security bio labs in a country that shares a border with Russia?  
  Engagement: Likes=4957, Reposts=1200, Quotes=64, Replies=295, Bookmarks=12, Views=N/A

- **[post:27]** ID: 1501657834873782275  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Wed, 09 Mar 2022 20:35:01 GMT  
  Content: Billions of dollars have flowed into Ukraine over the years and we have very little idea of where it went or what it was used for.  
  We know Ukrainian Money made Hunter Biden rich. John Kerry's son was involved as well.  
  So why are we trying to send $14 Billion MORE to Ukraine?  
  Engagement: Likes=7440, Reposts=2542, Quotes=197, Replies=686, Bookmarks=30, Views=N/A

- **[post:28]** ID: 1501611145790046212  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Wed, 09 Mar 2022 17:29:30 GMT  
  Content: Sending Kamala Harris to Poland to solve the Ukrainian crisis is like sending Dr. Jill Biden to do heart surgery.  
  Engagement: Likes=11609, Reposts=2100, Quotes=120, Replies=390, Bookmarks=22, Views=N/A

- **[post:29]** ID: 1501415916218707969  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Wed, 09 Mar 2022 04:33:44 GMT  
  Content: Did you know:  
  According to a new Rasmussen Reports poll, 52% of voters "believe it is likely" cheating affected the outcome of the 2020 presidential election.  
  33% say it’s very likely.  
  Remind me again why we're not even allowed to ask questions about 2020?  
  Engagement: Likes=7659, Reposts=2057, Quotes=68, Replies=315, Bookmarks=39, Views=N/A

- **[post:30]** ID: 1501400528126763016  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Wed, 09 Mar 2022 03:32:35 GMT  
  Content: The price of crude oil increased 513% between the moment Biden took office and Putin invaded Ukraine.  
  It has increased 25% since the invasion.  
  The price you're paying at the pump is Biden's fault, not Putin's.  
  Engagement: Likes=19413, Reposts=7028, Quotes=322, Replies=475, Bookmarks=218, Views=N/A

- **[post:31]** ID: 1501332347291013120  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 08 Mar 2022 23:01:39 GMT  
  Content: More people should know the name Victoria Nuland.  
  Engagement: Likes=1291, Reposts=279, Quotes=6, Replies=84, Bookmarks=3, Views=N/A

- **[post:32]** ID: 1501309529987813376  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 08 Mar 2022 21:30:59 GMT  
  Content: If there is a nuclear war they will blame Trump.  
  Engagement: Likes=5152, Reposts=544, Quotes=47, Replies=297, Bookmarks=6, Views=N/A

- **[post:33]** ID: 1501283110440214532  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 08 Mar 2022 19:46:00 GMT  
  Content: Biden started killing the American energy sector on January 20th, 2021  
  Even before the invasion—gas was over $3.50 on average  
  Gas is now $4.17/gallon on average—an all-time high  
  They're going to try and blame this on Putin  
  Don't let them get away with it. Joe Biden owns this.  
  Engagement: Likes=4209, Reposts=1289, Quotes=50, Replies=153, Bookmarks=9, Views=N/A

- **[post:34]** ID: 1501275781107884032  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 08 Mar 2022 19:16:53 GMT  
  Content: Every state should pass an anti-grooming law like the one the left is protesting in Florida. Protect our kids, it shouldn't be complicated.  
  Engagement: Likes=2919, Reposts=539, Quotes=11, Replies=99, Bookmarks=2, Views=N/A

- **[post:35]** ID: 1501270997046992900  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Tue, 08 Mar 2022 18:57:52 GMT  
  Content: It's no coincidence that Biden Regime just released a Saudi terrorist from Guantanamo known as the ’20th Hijacker’ of 9/11 as they're actively negotiating energy purchases with the Saudis.  
  Seems like these people will do literally anything except the obvious solutions at home.  
  Engagement: Likes=2518, Reposts=791, Quotes=38, Replies=92, Bookmarks=18, Views=N/A

### @TPUSA account posts (March 5–11, 2022; no direct event announcements matching criteria):
- **[post:36]** ID: 1501914519425064964  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Thu, 10 Mar 2022 13:35:00 GMT  
  Content: ABSOLUTE TRUTH @RepBurgessOwens!  
  Society thrives when men support women and women support men!  
  #GenFree #AMFEST2021  
  Engagement: Likes=178, Reposts=33, Quotes=2, Replies=11, Bookmarks=2, Views=N/A  
  Media: 1 video

- **[post:37]** ID: 1501719302784778240  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Thu, 10 Mar 2022 00:39:17 GMT  
  Content: "Inflation is one form of taxation that can be imposed without legislation."  
  Milton Friedman  
  Engagement: Likes=161, Reposts=62, Quotes=1, Replies=7, Bookmarks=2, Views=N/A

- **[post:38]** ID: 1501552131597291521  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Wed, 09 Mar 2022 13:35:00 GMT  
  Content: America is no longer just in a political fight. We are in a culture war of good vs. evil.  
  TAKE A STAND.  
  @SebGorka #AMFEST2021  
  Engagement: Likes=237, Reposts=61, Quotes=2, Replies=17, Bookmarks=4, Views=N/A  
  Media: 1 video

- **[post:39]** ID: 1501519415845822476  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Wed, 09 Mar 2022 11:25:00 GMT  
  Content: The Left's plan for public schools:  
  1) Drop Fs from report cards.  
  2) Teach woke garbage.  
  3) Destroy America.  
  And Santa Barbara leads the way!  
  Engagement: Likes=71, Reposts=32, Quotes=2, Replies=8, Bookmarks=1, Views=N/A  
  Media: 3 photos

- **[post:40]** ID: 1501298536289161217  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Tue, 08 Mar 2022 20:47:18 GMT  
  Content: If we're going to start freezing assets, can we start with members of Congress who got rich off of insider trading? 👀  
  Engagement: Likes=1690, Reposts=325, Quotes=18, Replies=60, Bookmarks=0, Views=N/A

- **[post:41]** ID: 1501256433316282375  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Tue, 08 Mar 2022 18:00:00 GMT  
  Content: “In prosperous times in America, it’s easier for us to say “look at these countries, how can we help them?” @MorganZegers  
  Is America’s reaction to the Ukraine/Russia situation justified?🤔 @JonnyRoot_ @Clegg1776 @Duncan_Colton  
  Let us know your thoughts in the replies👇  
  Engagement: Likes=28, Reposts=8, Quotes=0, Replies=8, Bookmarks=0, Views=N/A  
  Media: 1 video

- **[post:42]** ID: 1501188485121593344  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Tue, 08 Mar 2022 13:30:00 GMT  
  Content: It's time to stop letting the left walk all over conservatives and America.  
  TAKE A STAND. 🇺🇸  
  @JesseBWatters #AMFEST2021  
  Engagement: Likes=47, Reposts=20, Quotes=0, Replies=3, Bookmarks=0, Views=N/A  
  Media: 1 video

- **[post:43]** ID: 1500939985473531912  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Mon, 07 Mar 2022 21:02:33 GMT  
  Content: Bold stripes, bright stars, brave hearts 🇺🇸🇺🇸🇺🇸 #iHeartAmerica  
  What's your FAVORITE thing about America?  
  Engagement: Likes=59, Reposts=8, Quotes=2, Replies=8, Bookmarks=0, Views=N/A  
  Media: 1 photo

- **[post:44]** ID: 1500894049095589889  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Mon, 07 Mar 2022 18:00:01 GMT  
  Content: What role does the southern border play in human trafficking? 👇  
  Noel Thomas has all the answers. 🗣  
  How do you think we could best protect our borders?  
  #TPUSALIVE  
  Engagement: Likes=20, Reposts=4, Quotes=0, Replies=2, Bookmarks=0, Views=N/A  
  Media: 1 video

- **[post:45]** ID: 1500852522021363718  
  Author: Turning Point USA - @TPUSA  
  Timestamp: Mon, 07 Mar 2022 15:15:00 GMT  
  Content: Leave a "✋" in the replies if you want commies to leave you and your country alone!  
  #BigGovSucks  
  Engagement: Likes=46, Reposts=5, Quotes=0, Replies=26, Bookmarks=1, Views=N/A  
  Media: 1 photo

### Semantic search results (no additional direct event matches beyond above):
- **[post:46]** ID: 1501180942173491202  
  Author: FandemicTour - @FandemicTour  
  Timestamp: Tue, 08 Mar 2022 13:00:01 GMT  
  Content: ⭐️ Join us on our "Official Facebook Page" Wednesday, March 9th at 5 PM EST as we go LIVE talking all things Fandemic, and our special guest Nick Carter talks about how you can see him in person at our show this March 18th-20th!  
  🎟 Get your 2022 pass! [link]  
  Engagement: Likes=308, Reposts=45, Quotes=6, Replies=15, Bookmarks=2, Views=N/A  
  Media: 1 photo

- **[post:47]** ID: 1500549577337933837  
  Author: Matt Walsh - @MattWalshBlog  
  Timestamp: Sun, 06 Mar 2022 19:11:12 GMT  
  Content: This event will be Monday, March 14, at 530 at instructional center 103  
  Engagement: Likes=535, Reposts=54, Quotes=1, Replies=34, Bookmarks=3, Views=N/A

- **[post:48]** ID: 1500836627836456963  
  Author: Christina Pushaw 🐊 🇺🇸 - @ChristinaPushaw  
  Timestamp: Mon, 07 Mar 2022 14:11:50 GMT  
  Content: Starting at 10am - WATCH LIVE on @GovRonDeSantis Rumble & FB: Governor Ron DeSantis, Surgeon General Dr. Joseph Ladapo, Physicians, and Epidemiologists Discuss Failure of Lockdowns and Mandates  
  Engagement: Likes=391, Reposts=75, Quotes=5, Replies=33, Bookmarks=2, Views=N/A

- **[post:49]** ID: 1501559932881149955  
  Author: iHeartRadio - @iHeartRadio  
  Timestamp: Wed, 09 Mar 2022 14:06:00 GMT  
  Content: .@charlieputh is performing at our #iHeartAwards on March 22nd and I'm freaking out!!! 💡❤️  
  Run don't walk and buy your tickets right now: [link]  
  Engagement: Likes=326, Reposts=66, Quotes=19, Replies=22, Bookmarks=3, Views=N/A  
  Media: 1 photo

- **[post:50]** ID: 1500565161265954816  
  Author: Charlie Kirk - @charliekirk11  
  Timestamp: Sun, 06 Mar 2022 20:13:08 GMT  
  Content: Republican Governor Spencer Cox is refusing to protect women's sports. He is signaling he will pander to the trans lobby to continue the destruction of children. Why? He is likely being paid off by Big Pharma who make billions off hormone blockers and chemical castration.  
  Engagement: Likes=4068, Reposts=1271, Quotes=128, Replies=178, Bookmarks=99, Views=N/A

- **[post:51]** ID: 1501226837950697473  
  Author: Beck - @beck  
  Timestamp: Tue, 08 Mar 2022 16:02:24 GMT  
  Content: Something different coming up - announcing two solo acoustic shows this month. Tickets are on sale Wednesday, March 9 at 12pm CT. See you there!  
  3/19 Austin, TX | ACL Live at The Moody Theater [link]  
  3/21 Nashville, TN | Basement East [link]  
  Engagement: Likes=165, Reposts=16, Quotes=7, Replies=19, Bookmarks=1, Views=N/A  
  Media: 1 photo

- **[post:52]** ID: 1502061395533348865  
  Author: Matt Walsh - @MattWalshBlog  
  Timestamp: Thu, 10 Mar 2022 23:18:38 GMT  
  Content: My event at Georgia Tech on Monday March 14 is free to the public. Register here:  
  [link]  
  Engagement: Likes=328, Reposts=40, Quotes=3, Replies=25, Bookmarks=1, Views=N/A

- **[post:53]** ID: 1501481786127564800  
  Author: MNA - @Engr_Naveed111  
  Timestamp: Wed, 09 Mar 2022 08:55:28 GMT  
  Content: Lower Dir !!!  
  PM’s Mass Contact Drive’s next Stop is KP  
  Prime Minister Imran Khan will address to the Public Rally at Lower Dir on Friday 11th March , 2022.  
  Engagement: Likes=198, Reposts=29, Quotes=0, Replies=4, Bookmarks=0, Views=N/A

**No results** were returned for dedicated @TPUSAevents account searches or other targeted queries (e.g., from:TPUSAevents or pure tour-specific phrases) within the date range. No posts from TPUSA's official accounts announced Charlie Kirk speaking events in this exact week. The only explicit Charlie Kirk appearance referenced is his participation in the Florida Citizens Alliance "Kids & Country Gala" (held the evening of March 9, 2022, referenced in posts on March 10). Other mentions are general or unrelated to events in the specified week. All data above is exhaustive from the tool outputs.
```

