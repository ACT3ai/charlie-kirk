---
unlisted: true
title: "Week 27 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W27"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-07-02 to 2022-07-08."
status: completed
hide_table_of_contents: true
---

# Week 27, 2022

- Date range: 2022-07-02 to 2022-07-08
- Queried at (UTC): 2026-08-24T19:01:45Z
- Model: grok-4.3
- API status: completed
- Response id: 976c20c9-14b4-9f97-806f-645fbf0da809

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-07-02 to the end of the week 2022-07-08.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR event OR speaking OR \"will speak\" OR \"speaks at\" OR \"speaking at\" OR tour OR \"campus tour\" OR appearance OR \"will be\" OR location OR venue) since:2022-07-02 until:2022-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR \"public speaking\" OR \"will speak\" OR \"speaks\" OR appearance) since:2022-07-02 until:2022-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak in July 2022",
      "limit": "10",
      "from_date": "2022-07-02",
      "to_date": "2022-07-08",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR @TPUSA OR \"Turning Point\") (event OR speaking OR speak OR \"will speak\" OR appearance OR \"speaking at\" OR \"will be speaking\" OR tour OR \"campus tour\" OR \"public event\" OR venue OR location OR \"this week\" OR \"next week\" OR July OR \"July 2022\") since:2022-07-02 until:2022-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (SAS OR \"Student Action Summit\" OR \"faith reps\" OR \"faith leaders\") since:2022-07-02 until:2022-07-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 OR from:TPUSA since:2022-07-02 until:2022-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk TPUSA speaking events locations appearances July 2022",
      "limit": "10",
      "from_date": "2022-07-02",
      "to_date": "2022-07-08",
      "min_score_threshold": "0.05"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (speaking OR \"will speak\" OR \"speaks at\" OR \"speaking at\" OR \"will be speaking\" OR event OR appearance OR \"public speaking\" OR tour OR \"campus tour\" OR \"speaking event\") (July OR 2022 OR location OR venue OR \"this week\" OR \"next week\" OR Tampa OR Florida OR Wisconsin OR \"Westby\" OR Arizona OR \"Rocklin\" OR \"Destiny Church\") since:2022-07-02 until:2022-07-09",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Student Action Summit\" OR SAS2022 OR #SAS2022) (Charlie Kirk OR TPUSA) since:2022-07-02 until:2022-07-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR SAS OR summit OR tour OR appearance) since:2022-07-02 until:2022-07-09",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR SAS OR summit OR tour OR appearance) since:2022-07-02 until:2022-07-09",
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
  "input_tokens": 43321,
  "input_tokens_details": {
    "cached_tokens": 26624
  },
  "output_tokens": 3405,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 46726,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 897085500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 11,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 18015,
    "output_tokens": 2603
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544698307175501826",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544698307175501826"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545186778797072385",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545186778797072385"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544361499707297792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544361499707297792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543636069983195136",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543636069983195136"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545116438393806848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545116438393806848"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544868156786835457",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544868156786835457"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545103529215283200",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545103529215283200"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545169046038986752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545169046038986752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543622115534016519",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543622115534016519"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544395991260045312",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544395991260045312"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545055227241369602",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545055227241369602"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543041787496890368",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543041787496890368"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544420760520892416",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544420760520892416"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543630243444899840",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543630243444899840"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544879996119834624",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544879996119834624"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544731668690264070",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544731668690264070"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545046457178157058",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545046457178157058"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545135069827928064",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545135069827928064"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544367051761823744",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544367051761823744"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543972319621779456",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543972319621779456"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545176543466590208",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545176543466590208"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545112552400642049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545112552400642049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545060078650269696",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545060078650269696"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545048133951844353",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545048133951844353"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545170641455915009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545170641455915009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545172002155114496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545172002155114496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545166152690696194",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545166152690696194"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544755095836958723",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544755095836958723"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545117343696596992",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545117343696596992"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545195047020220416",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545195047020220416"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543264328446578688",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543264328446578688"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545170336722948100",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545170336722948100"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543363077080489987",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543363077080489987"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545101116215414785",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545101116215414785"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545125161392689153",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545125161392689153"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545045308861607936",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545045308861607936"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544426335346491394",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544426335346491394"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543982110524022788",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543982110524022788"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544734665977856002",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544734665977856002"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545117850129633284",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545117850129633284"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545136214566735878",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545136214566735878"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1544427478768238592",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1544427478768238592"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545179987254292480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545179987254292480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545193633753604096",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545193633753604096"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1543748327052804098",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1543748327052804098"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545195658583351298",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545195658583351298"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545094206154211331",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545094206154211331"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545061498808143872",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545061498808143872"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545120474316693504",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545120474316693504"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545094593556795392",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545094593556795392"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545103159449702401",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545103159449702401"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1545075488804069376",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1545075488804069376"
  }
]
```

## Grok response

```text
**All relevant X (Twitter) posts from the specified date range (2022-07-02 to 2022-07-08, inclusive) mentioning or discussing public speaking events, appearances, locations, or where Charlie Kirk or TPUSA/Turning Point USA would speak or appear are included below in full (no summarization).** These were identified via keyword and semantic searches targeting the date window. Many posts reference future events outside the week (e.g., upcoming SAS2022 or local events), but only those posted within the range are shown. Irrelevant or off-topic posts (e.g., general mentions of Charlie Kirk without event details) were filtered out where possible, but all matching the criteria are listed.

Posts are presented with full content, author, timestamp (GMT), and any media/links quoted in the original results. No external links or additional context added.

### Posts mentioning TPUSA/Charlie Kirk speaking events or appearances:

- **Post ID: 1545112552400642049**  
  **Author:** Adam Thomas Dommeyer (@AdamDommeyer)  
  **Timestamp:** Thu, 07 Jul 2022 18:28:33 GMT  
  **Content:** I will be speaking on "Standing Up Against Critical Race Theory" on behalf of @tpusafaith @TPUSA at the We the People of Vernon County Patriots Event in Westby, WI this Sunday. Join us and hear why churches must speak out against radical leftist ideology!  
  **Media:** 1 photo (event flyer)  
  **Engagement:** Likes=6, Reposts=4, Quotes=0, Replies=2, Bookmarks=0  

- **Post ID: 1545048133951844353**  
  **Author:** michaela schmidt (@michaelas1776)  
  **Timestamp:** Thu, 07 Jul 2022 14:12:35 GMT  
  **Content:** Join Florida Faith Reps, @MinielAmbar & myself discussing all things SAS, Florida student stipend opportunities, and a chance to meet Charlie Kirk at #SAS2022 🌴🇺🇸🌅 @tpusafaith  

  Faith Leaders DM for this Invite only event !!  

  Tickets:  
  https://t.co/KebvxaYGb2  

  #tpusafaith  
  **Media:** 2 photos (promotional images)  
  **Engagement:** Likes=7, Reposts=3, Quotes=1, Replies=1, Bookmarks=0  

- **Post ID: 1545060078650269696**  
  **Author:** Republican Party of Arizona (@AZGOP)  
  **Timestamp:** Thu, 07 Jul 2022 15:00:03 GMT  
  **Content:** This Saturday go check out Turning Point Action's first Super Saturday Event of the Year!  
  In Goodyear, AZ. Special Guests include @charliekirk11 , @merissacaldwell , @DrPaulGosar , and @ScottPresler  
  **Media:** 1 photo (event graphic)  
  **Engagement:** Likes=156, Reposts=48, Quotes=1, Replies=6, Bookmarks=1  

- **Post ID: 1544755095836958723**  
  **Author:** nekomancey (@bakekitsune2022)  
  **Timestamp:** Wed, 06 Jul 2022 18:48:09 GMT  
  **Content:** We love ya Dave, keep up the fight. I agree with you for staying and keeping people informed about what twitter is doing.     

  Btw I listen to your podcast every day. Thanks for all the work you do! Hope to see you speak in Tampa at the TPUSA event.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0  

- **Post ID: 1544731668690264070**  
  **Author:** Natalia Marie Carissimi (@NanLee1124)  
  **Timestamp:** Wed, 06 Jul 2022 17:15:04 GMT  
  **Content:** What an event with TWO GREATS-@ScottPresler and @charliekirk11 🇺🇸🥊🇺🇸  
  July 9th 10am Goodyear AZ Get Out the Vote- Super Saturday! Elect True Conservatives and #MAGA #AmericaFirst #Vote 🇺🇸  
  **Media:** Quoted post with photo (event details: Goodyear Recreation Campus, 420 South Estrella Parkway, Goodyear, AZ 85338, Sat., July 9 @ 10 am)  
  **Engagement:** Likes=2, Reposts=3, Quotes=0, Replies=0, Bookmarks=0  

- **Post ID: 1543630243444899840**  
  **Author:** Students For Trump (@TrumpStudents)  
  **Timestamp:** Sun, 03 Jul 2022 16:18:23 GMT  
  **Content:** SO. EXCITED. 🙌🇺🇸  

  JOIN US on Saturday July 9th for an AMAZING event with featured speakers @JeffDeWitAZ, @charliekirk11, AND MORE! 👀  

  REGISTER NOW ➡️ https://t.co/HG8VDsa0On  
  **Media:** 2 photos (promotional graphics)  
  **Engagement:** Likes=16, Reposts=7, Quotes=0, Replies=1, Bookmarks=0  

- **Post ID: 1543636069983195136**  
  **Author:** Turning Point USA (@TPUSA)  
  **Timestamp:** Sun, 03 Jul 2022 16:41:33 GMT  
  **Content:** Do EVERYTHING you can do to preserve this great country. 🇺🇸  

  Hear from @donaldjtrumpjr at #SAS2022 by using the promo code “1776” for 17% off of VIP tickets, & 76% off of GA tickets: http://tpusa.com/SAS  

  *Ends July 5th at midnight*  
  **Media:** 2 photos (promotional images)  
  **Engagement:** Likes=213, Reposts=53, Quotes=2, Replies=25, Bookmarks=1  

- **Post ID: 1545045308861607936**  
  **Author:** TPUSA South Central College (@tpusasc)  
  **Timestamp:** Thu, 07 Jul 2022 14:01:21 GMT  
  **Content:** Hey Texans! Not only do we have Texas Senator Ted Cruz coming to SAS this month, we also still have scholarships for you that will cover your ticket cost, lodging, and reimburse your travel costs!   

  Applications close in 3 days!   

  Apply at https://t.co/J2k5FeT6gs  
  **Media:** 1 photo (promotional graphic)  
  **Engagement:** Likes=8, Reposts=6, Quotes=0, Replies=1, Bookmarks=0  

- **Post ID: 1544395991260045312**  
  **Author:** Rickey Adam Jr. (@RickeyAdamJr)  
  **Timestamp:** Tue, 05 Jul 2022 19:01:12 GMT  
  **Content:** “School Choice” speaks for itself come show support for kids across the country @TPUSA’s Student Action Summit July 22-24 in Tampa. Your zip code should not determine the quality of education your kids receive! https://t.co/uq13NGkL8j https://t.co/LcALBIbd6T  
  **Media:** 1 photo (promotional image)  
  **Engagement:** Likes=18, Reposts=10, Quotes=1, Replies=1, Bookmarks=0  

- **Post ID: 1543972319621779456**  
  **Author:** Bobby Sauce (@takenaps)  
  **Timestamp:** Mon, 04 Jul 2022 14:57:41 GMT  
  **Content:** I'm going to @tpusa's Student Action Summit in the freedom-loving state of Florida! Join me from July 22-24 if you want to have the time of your life with the best conservatives around.   

  Use code "TPUSAAMBASSADOR" for $$$ off!   

  Tickets here!  
  **Engagement:** Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0  

- **Post ID: 1543363077080489987**  
  **Author:** RealBenGeller (@RealBenGeller)  
  **Timestamp:** Sat, 02 Jul 2022 22:36:46 GMT  
  **Content:** Excited to be joining @TPUSA as a breakout speaker this year at Student Action Summit. My hope is to share my experience being a young Legislator to inspire the next generation of Young American Leaders. 🇺🇸  
  **Media:** 1 photo (promotional graphic)  
  **Engagement:** Likes=7, Reposts=1, Quotes=0, Replies=0, Bookmarks=0  

- **Post ID: 1545179987254292480**  
  **Author:** JFC (@Willow48094008)  
  **Timestamp:** Thu, 07 Jul 2022 22:56:31 GMT  
  **Content:** The City of Rocklin allowed Pastor Greg Fairrington of Destiny Church to spew his GQP political garbage at a city funded location. The same pastor who had Charlie Kirk as a guest. WTF.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0  

- **Post ID: 1543622115534016519**  
  **Author:** PatriotTakes 🇺🇸 (@patriottakes)  
  **Timestamp:** Sun, 03 Jul 2022 15:46:06 GMT  
  **Content:** The family that brought you Trump University is promoting Charlie Kirk’s new book, “The College Scam.”  
  **Media:** 1 video  
  **Engagement:** Likes=912, Reposts=172, Quotes=70, Replies=241, Bookmarks=25  

- **Post ID: 1543982110524022788**  
  **Author:** Jack Posobiec (@JackPosobiec)  
  **Timestamp:** Mon, 04 Jul 2022 15:36:35 GMT  
  **Content:** BREAKING: The Human Events 4th of July Special just dropped!  

  The State of American Freedom. Featuring:  

  Charlie Kirk @charliekirk11   
  Alex Clark @realalexclark   
  Drew Hernandez @DrewHLive   

  Enjoy!  
  https://t.co/cWSztzYDsb  
  **Media:** 1 photo (promotional graphic)  
  **Engagement:** Likes=372, Reposts=58, Quotes=2, Replies=13, Bookmarks=3  

- **Post ID: 1544420760520892416**  
  **Author:** Jack Posobiec (@JackPosobiec)  
  **Timestamp:** Tue, 05 Jul 2022 20:39:37 GMT  
  **Content:** How America Is Different from Our Childhoods—with Charlie Kirk, Jack Posobiec, Alex Clark, and Drew Hernandez  

  https://t.co/yXdtTKPX0X  
  **Media:** 1 photo (promotional graphic)  
  **Engagement:** Likes=255, Reposts=34, Quotes=1, Replies=9, Bookmarks=8  

### Additional notes on coverage:
- No direct posts from @charliekirk11 or @TPUSA in the results explicitly announced new speaking events *within* the exact week of July 2-8, 2022 (their activity focused on other topics like politics and promotions).
- References to past events (e.g., Charlie Kirk at Destiny Church in Rocklin) or general TPUSA activities appear, but no additional specific upcoming locations beyond those listed.
- The searches returned a high volume of unrelated posts; only those directly tying to speaking events/appearances for Charlie Kirk or TPUSA are included here.
- All data is verbatim from the tool results. No posts were found for other specific locations or events strictly tied to the queried week beyond the above.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-07-02 to 2022-07-08**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-07-02 to 2022-07-08 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
