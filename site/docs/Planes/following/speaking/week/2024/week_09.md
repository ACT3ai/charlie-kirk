---
unlisted: true
title: "Week 09 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W09"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-02-26 to 2024-03-03."
status: completed
hide_table_of_contents: true
---

# Week 09, 2024

- Date range: 2024-02-26 to 2024-03-03
- Queried at (UTC): 2026-08-24T19:11:32Z
- Model: grok-4.3
- API status: completed
- Response id: f635c406-a84d-9f46-ab37-f57369f555d0

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-02-26 to the end of the week 2024-03-03.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speak OR speaking OR \"public speaking\" OR appearance OR tour OR campus OR \"will be\" OR \"speaking at\" OR \"speaks at\") since:2024-02-26 until:2024-03-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR \"will speak\" OR \"speaking\" OR \"speaks\" OR \"public speaking\") (from:charliekirk11 OR from:TPUSA) since:2024-02-26 until:2024-03-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between February 26 and March 3 2024",
      "limit": "10",
      "from_date": "2024-02-26",
      "to_date": "2024-03-04"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"TPUSA Faith\" OR \"TP Action\") (event OR speak OR speaking OR \"public speaking\" OR appearance OR tour OR campus OR \"will be\" OR \"speaking at\" OR \"speaks at\" OR conference OR summit OR rally OR \"Strong Church\" OR \"Faith Strong\") since:2024-02-26 until:2024-03-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR tour OR campus OR \"will be\" OR conference OR summit OR rally OR Arizona OR Phoenix OR \"Strong Church\" OR pastors) since:2024-02-26 until:2024-03-04",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR \"public speaking\" OR tour OR \"will be\" OR conference OR summit OR rally OR \"Strong Church\" OR pastors OR Mesa) since:2024-02-26 until:2024-03-04",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk speaking events, TPUSA conferences, pastor summits, campus tours, or public appearances in late February to early March 2024",
      "limit": "10",
      "from_date": "2024-02-26",
      "to_date": "2024-03-04"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 27112,
  "input_tokens_details": {
    "cached_tokens": 11456
  },
  "output_tokens": 2477,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 29589,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 630537000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 7,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 17117,
    "output_tokens": 1941
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763964228476809597",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763964228476809597"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763987455500222543",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763987455500222543"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763671210695729280",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763671210695729280"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1764059227083911609",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1764059227083911609"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1761935984017748400",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1761935984017748400"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763455067116474841",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763455067116474841"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763954389503352952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763954389503352952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763974335218528715",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763974335218528715"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762639796982182115",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762639796982182115"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762308284390985836",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762308284390985836"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762962831153205387",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762962831153205387"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762648267811340291",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762648267811340291"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763951080868651039",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763951080868651039"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763680714753704311",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763680714753704311"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762678619615502448",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762678619615502448"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762537800149213512",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762537800149213512"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763990191520292929",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763990191520292929"
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
    "url": "https://x.com/i/status/1762229554851254729",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762229554851254729"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762845178761449682",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762845178761449682"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1764059919467090022",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1764059919467090022"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763938521293680666",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763938521293680666"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763738714218651946",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763738714218651946"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1763897524367077708",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1763897524367077708"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762644628636119300",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762644628636119300"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1764048888124629270",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1764048888124629270"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1764071103381786728",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1764071103381786728"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762161443212759153",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762161443212759153"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1762978893172990025",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1762978893172990025"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1764029110798417950",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1764029110798417950"
  }
]
```

## Grok response

```text
**Here is a complete, unsummarized compilation of all relevant X posts found within the specified date range (posts from 2024-02-26 to 2024-03-03, using searches up to 2024-03-04 to capture the end of the week).** I used multiple keyword and semantic searches focused on Charlie Kirk, TPUSA/Turning Point USA, and related terms for events, speaking, conferences, summits, tours, appearances, etc. Only posts with direct or contextual relevance to public speaking events, where Charlie Kirk or TPUSA representatives are speaking or events are occurring, are included. Irrelevant or off-topic posts (e.g., general commentary, unrelated events) were filtered out during review.

No posts were found announcing or describing new Charlie Kirk personal speaking events specifically scheduled *within* Feb 26–Mar 3, 2024. The relevant activity centers on a large ongoing TPUSA Faith pastor/church leaders summit/conference in Arizona (Phoenix area, partnered with Dream City Church), which ran across multiple days in this window, including training sessions. Additional TPUSA-related speaking mentions include a representative at a school board meeting and a future/planned campus event announcement. All posts are presented in full with metadata.

### Key Relevant Posts (Chronological by Timestamp, Earliest to Latest):

- **Post ID: 1761935984017748400**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 26 Feb 2024 02:07:28 GMT  
  Content: Tomorrow over 1,500 pastors from across the country will be in ARIZONA at Strong Church Dream Conference, for a massive week of training, prayer, teaching, and kingdom building! ⁦@tpusafaith⁩  
  Media: 1 photo (https://pbs.twimg.com/media/GHOnVyxaQAAHyLZ.jpg)  
  Engagement: Likes=1100, Reposts=180, Quotes=5, Replies=124, Bookmarks=12, Views=88457

- **Post ID: 1762308284390985836**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Tue, 27 Feb 2024 02:46:51 GMT  
  Content: MASSIVE OPENING NIGHT  
  Over 2,000 church leaders, 1,200 are pastors, from across the country at our TPUSA FAITH STRONG CHURCH event in Arizona with our great partners Dream City Church!  
  The combined reach of these pastors is in the many MILLIONS  
  @tpaction will also sponsor a day of training on ballot chasing, voter registration, and how we WIN this year!   
  This is the largest pastors summit we’ve ever done, perhaps the largest of its kind in the country!  
  Three more days of training ahead   
  ONWARD!  
  🇺🇸  
  Media: 1 photo (https://pbs.twimg.com/media/GHT6C0_bAAAQaeo.jpg)  
  Engagement: Likes=2506, Reposts=429, Quotes=25, Replies=202, Bookmarks=25, Views=194511

- **Post ID: 1762644628636119300**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 28 Feb 2024 01:03:22 GMT  
  Content: TONIGHT: @REVWUTRUTH will be speaking at the Mesa Public Schools board meeting 🔥  
  Stay tuned...  
  Media: 1 photo (https://pbs.twimg.com/media/GHYr7-NbsAAJiMy.jpg)  
  Engagement: Likes=76, Reposts=15, Quotes=2, Replies=4, Bookmarks=1, Views=11390

- **Post ID: 1762678619615502448**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Wed, 28 Feb 2024 03:18:26 GMT  
  Content: .@REVWUTRUTH to the Mesa Public Schools Governing Board: "If you pervert the hearts and minds of kids in this district, you will reap it..."  
  Media: 1 video (https://video.twimg.com/amplify_video/1762678373070106624/vid/avc1/720x1280/DKEeGAVr_djoW6mB.mp4?tag=14, duration: 80405 ms)  
  Engagement: Likes=799, Reposts=251, Quotes=23, Replies=26, Bookmarks=41, Views=37856

- **Post ID: 1762978893172990025**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 28 Feb 2024 23:11:37 GMT  
  Content: Another WIN today!  
  Today we hosted over 100 students and Brandon Tatum as part of our outreach program to a black majority high school in Charlotte, NC! We have a very active TPUSA chapter at this school, Victory Academy.  
  In addition to wrapping up one of the biggest pastor trainings in the country with over 2,000 pastors and ministry heads in Phoenix, we are scaling our urban outreach program across the country!  
  Onward!  
  🇺🇸  
  Media: 1 photo (https://pbs.twimg.com/media/GHdbshtXwAAsGkl.jpg)  
  Engagement: Likes=1153, Reposts=182, Quotes=4, Replies=70, Bookmarks=5, Views=79486

- **Post ID: 1762648267811340291**  
  Author: Rachel Anderson (@RachelA1776)  
  Timestamp: Wed, 28 Feb 2024 01:17:50 GMT  
  Content: 🚨🚨🚨  
  @charliekirk11 is coming to University of Washington!  
  Join amazing student patriots as we host the founder of the largest conservative organization Charlie Kirk, May 7th! 🇺🇸  
  Grab your free tickets here! 🎟️  
  https://t.co/7SeXsaQHmu  
  @TPUSA @tpusastudents   
  #UW #UniversityofWashington #CharlieKirk #LiveFree #Conservatives   
  @tylerbowyer @juliecbarrett @MattForYakima @RealHannahJoy @choeshow @thehoffather  
  Media: 1 photo (https://pbs.twimg.com/media/GHYvQZZbUAAIQ9q.jpg)  
  Engagement: Likes=357, Reposts=52, Quotes=0, Replies=17, Bookmarks=2, Views=61489

- **Post ID: 1762537800149213512**  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 27 Feb 2024 17:58:52 GMT  
  Content: TPUSA is hosting our 8th annual Chapter Leadership Summit in Detroit, MI, from June 12-14th! 🎉 🇺🇸  
  This FREE SUMMIT is designed to provide students with new methods and skills needed to effectively and successfully lead their TPUSA Chapter.  
  APPLY NOW: https://t.co/hF6COL40AZ  
  Media: 1 photo (https://pbs.twimg.com/media/GHXKxD2W0AEcM3c.jpg)  
  Engagement: Likes=162, Reposts=64, Quotes=6, Replies=14, Bookmarks=0, Views=58937

### Additional Contextual Mentions (Mentions of Past/Related TPUSA Events, No New Scheduling in Date Range):
- **Post ID: 1764029110798417950** (Reply context)  
  Author: Lucky Teter (@TheMagaHulk)  
  Timestamp: Sat, 02 Mar 2024 20:44:48 GMT  
  Content: At least he white knighted for Rob Smith at that TPUSA event.  
  Engagement: Likes=14, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=962  
  (References a prior TPUSA event involving Rob Smith.)

- **Post ID: 1763951080868651039**  
  Author: Seth R Wheeler (@Da__Myth)  
  Timestamp: Sat, 02 Mar 2024 15:34:44 GMT  
  Content: @TPUSA in case you need a speaker for the next event, here’s a good promo video  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=5  
  (Offers self as potential future speaker for TPUSA.)

No other posts in the searches directly detailed additional Charlie Kirk or TPUSA public speaking events strictly within the Feb 26–Mar 3 window. The Arizona pastor summit appears to be the primary active event spanning the period (announced starting Feb 26, opening night Feb 27, ongoing training through at least Feb 28). Future events (e.g., University of Washington in May, Detroit summit in June) were announced but fall outside the date range. All data from tool results is included without summarization or omission of qualifying posts.
```

