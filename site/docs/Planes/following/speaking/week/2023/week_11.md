---
unlisted: true
title: "Week 11 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W11"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-03-12 to 2023-03-18."
status: completed
hide_table_of_contents: true
---

# Week 11, 2023

- Date range: 2023-03-12 to 2023-03-18
- Queried at (UTC): 2026-08-24T19:06:18Z
- Model: grok-4.3
- API status: completed
- Response id: 49c3ce36-2707-9860-b94d-475c9a97f5fa

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-03-12 to the end of the week 2023-03-18.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR \"will be\" OR \"speaking at\" OR campus) since:2023-03-12 until:2023-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance) (at OR in) (since:2023-03-12 until:2023-03-19)",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus) since:2023-03-12 until:2023-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus) since:2023-03-12 until:2023-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA_Events (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus) since:2023-03-12 until:2023-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where Charlie will speak between March 12-18 2023",
      "limit": "10",
      "from_date": "2023-03-12",
      "to_date": "2023-03-19"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1635823755548319750"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1635821908964036609"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1635751427883814912"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1636442276993069056"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1636865022411304960"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR @charliekirk11 OR @TPUSA) (UC Davis OR \"UC Davis\" OR Davis) (event OR speaking OR speak OR tour OR \"live free\" OR appearance) since:2023-03-12 until:2023-03-19",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (Rutgers OR LSU OR \"March 20\" OR \"March 21\") (event OR speaking OR speak OR tour OR appearance) since:2023-03-12 until:2023-03-19",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (tour OR event OR speaking OR \"UC Davis\" OR Rutgers OR LSU) since:2023-03-12 until:2023-03-19",
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
  "input_tokens": 29512,
  "input_tokens_details": {
    "cached_tokens": 13184
  },
  "output_tokens": 4985,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 34497,
  "num_sources_used": 0,
  "num_server_side_tools_used": 14,
  "cost_in_usd_ticks": 1055093000,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 14,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 17737,
    "output_tokens": 4316
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636531663978078212",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636531663978078212"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635733869176709120",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635733869176709120"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636561059518590983",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636561059518590983"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636834963604779013",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636834963604779013"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636545846388080641",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636545846388080641"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636081553225965568",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636081553225965568"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635751427883814912",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635751427883814912"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636442276993069056",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636442276993069056"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635734827373821952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635734827373821952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636805109244887066",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636805109244887066"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636794715206197248",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636794715206197248"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635720419914436608",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635720419914436608"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636511683232296960",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636511683232296960"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635735983194017792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635735983194017792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635809208988999681",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635809208988999681"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636825346451357713",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636825346451357713"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636873624392200192",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636873624392200192"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636864178437668866",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636864178437668866"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636865656305115136",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636865656305115136"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635825533316644864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635825533316644864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636851767421067264",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636851767421067264"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636865133350883328",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636865133350883328"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636442284127567872",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636442284127567872"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636858529100230656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636858529100230656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636867775762407424",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636867775762407424"
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
    "url": "https://x.com/i/status/1635858250204585987",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635858250204585987"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636834961738326016",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636834961738326016"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636834961008504836",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636834961008504836"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636032972360155136",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636032972360155136"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635823755548319750",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635823755548319750"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636160081707552768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636160081707552768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636865022411304960",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636865022411304960"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636442279069233152",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636442279069233152"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635397870219300864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635397870219300864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635817103617048577",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635817103617048577"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636181438751203329",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636181438751203329"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636867462787416066",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636867462787416066"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635821908964036609",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635821908964036609"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1635657873312333824",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1635657873312333824"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1636127157905944576",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1636127157905944576"
  }
]
```

## Grok response

```text
**All relevant X/Twitter posts from the date range March 12–18, 2023 (posts dated March 12 to March 18, 2023, capturing activity for the week of March 12–18), mentioning public speaking events, appearances, tours, or locations where Charlie Kirk or TPUSA would speak. Data includes full post content, author, timestamp (GMT), engagement metrics, media where present, and context/replies where directly relevant to events. No summarization—raw extracted data only. No posts found for March 12–13 in results.**

### UC Davis / "Live Free Tour" Event (March 14–15, 2023)
- **Post [post:38]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Tue, 14 Mar 2023 21:15:05 GMT. Likes: 3520, Reposts: 1083, Quotes: 92, Replies: 584, Bookmarks: 58, Views: 294181. Media: Video (duration ~81s). Content: "UC Davis Chancellor Gary S. May took the time to record a bizarre video and slander me and our amazing students at TPUSA ahead of our event tonight, so I took the time to respond. WATCH:" (Video response to chancellor).  
  Relevant replies/context: Multiple users reacting to the pre-event tension.

- **Post [post:57]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Tue, 14 Mar 2023 20:05:19 GMT. Likes: 6579, Reposts: 657, Quotes: 97, Replies: 1291, Bookmarks: 9, Views: 520474. Media: Photo (barricades). Content: "Barricades for my speech tonight at UC Davis."

- **Post [post:56]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Tue, 14 Mar 2023 20:13:43 GMT. Likes: 1032, Reposts: 166, Quotes: 2, Replies: 51, Bookmarks: 0, Views: 105088. Content: "REGISTER and come out tonight in big numbers and show UC Davis that conservatives will not be silenced. And if you disagree, I'll invite you to the front of the line for a peaceful exchange of ideas." (Link to tpusa.com/livefree).

- **Post [post:55]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Tue, 14 Mar 2023 20:09:07 GMT. Likes: 655, Reposts: 99, Quotes: 3, Replies: 75, Bookmarks: 1, Views: 60924. Content: "REGISTER and come out tonight in big numbers and show UC Davis that conservatives will not be silenced. And if you disagree, I'll invite you to the front of the line for a peaceful exchange of ideas."

- **Post [post:37]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Wed, 15 Mar 2023 01:55:09 GMT. Likes: 35001, Reposts: 7002, Quotes: 906, Replies: 4924, Bookmarks: 331, Views: 5042307. Media: Video (duration ~52s). Content: "NEW VIDEO: Violent leftwing agitators just smashed through windows outside of the event venue here at UC Davis. Reports are that some of this group made their way into the building before police successfully removed them. Pray for peace and safety for all involved. 🙏"  
  Replies include: Elon Musk reply ("Not a peaceful protest at all"); Charlie Kirk follow-up ("Very proud of our @TPUSA chapter leaders and staff for holding the line tonight. Thank you to the police who are doing a great job as well!").

- **Post [post:35]**: Author: Turning Point USA (@TPUSA). Timestamp: Wed, 15 Mar 2023 02:02:30 GMT. Likes: 3592, Reposts: 1550, Quotes: 329, Replies: 1327, Bookmarks: 77, Views: 1069391. Media: Video (duration ~38s). Content: "🚨BREAKING: Antifa is attempting to overrun the venue hosting Charlie Kirk at UC Davis. They have begun violently smashing through the windows in an attempt to shut down the voice of those they oppose."  
  Direct replies: TPUSA post [post:24] ("🔴LIVE: TPUSA Presents The LIVE FREE Tour w/ @Charliekirk11 at UC Davis https://www.youtube.com/live/bxT2R9YLUag?feature=share"); TPUSA post [post:25] ("HAPPENING NOW AT UC DAVIS: Police carry Antifa members out of the LIVE FREE TOUR venue’s second floor") with media (photo).

- **Post [post:36]**: Author: VOZ (@Voz_US). Timestamp: Fri, 17 Mar 2023 23:00:07 GMT. Likes: 3, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 1494. Content: "WATCH: Damaged Property, Officer Wounded Ahead Of Charlie Kirk Event in California."

- **Post [post:43]**: Author: Washington Free Beacon (@FreeBeacon). Timestamp: Fri, 17 Mar 2023 19:02:03 GMT. Likes: 19, Reposts: 7, Quotes: 1, Replies: 1, Bookmarks: 0, Views: 2909. Content: "A Sacramento Bee op-ed writer and UC Davis chancellor falsely claimed that Charlie Kirk has called for violence against transgender people. Ahead of Kirk’s appearance at UC Davis, rioters smashed windows, hurled eggs, and assaulted police officers. https://freebeacon.com/campus/how-liberal-misinformation-led-to-violent-protest-of-conservative-uc-davis-speaker/"

- **Post [post:40]**: Author: California Republican Assembly (CRA) (@cragop). Timestamp: Fri, 17 Mar 2023 21:00:40 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 36. Content: "#467 - Tolerant ANTIFA Mob Riots at UC Davis to Keep TPUSA Founder from Speaking."

- **Post [post:41]**: Author: The Rundown - 2A News & Conservative Views (@craig_deluz). Timestamp: Fri, 17 Mar 2023 21:00:40 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 13. Content: "#467 - Tolerant ANTIFA Mob Riots at UC Davis to Keep TPUSA Founder from Speaking."

- **Post [post:42]**: Author: Benjamin Murphy CC (@benjmurrf). Timestamp: Fri, 17 Mar 2023 21:00:40 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 33. Content: "#467 - Tolerant ANTIFA Mob Riots at UC Davis to Keep TPUSA Founder from Speaking."

- **Post [post:1]**: Author: JJ McCormick (@joejmccormick). Timestamp: Fri, 17 Mar 2023 23:11:03 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 10. Content: "Charlie Kirk Campus Event Violently Attacked After Liberal News Outlet Publishes False 'Lynching' Accusation."

- **Post [post:6]**: Author: SilverRaine (@SerenitysCalm). Timestamp: Fri, 17 Mar 2023 22:56:46 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 5. Content: "Charlie Kirk Campus Event Violently Attacked After Liberal News Outlet Publishes False 'Lynching' Accusation."

- **Post [post:4]**: Author: Newtonbomb (@Wesleymooch). Timestamp: Fri, 17 Mar 2023 23:00:33 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 5. Content: "The woke including antifa are blatantly following fascistic Tendencies by demanding what people do and not do. I don't like Charlie Kirk much but antifa tried to stop him from speaking, that is woke and that is fascism and they can all f*** off."

- **Post [post:5]**: Author: VOZ (@Voz_US). Timestamp: Fri, 17 Mar 2023 23:00:07 GMT. Likes: 3, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 1494. Content: "WATCH: Damaged Property, Officer Wounded Ahead Of Charlie Kirk Event in California." (Duplicate reference to above).

- **Post [post:13]**: Author: joe t (@jtinaglia). Timestamp: Fri, 17 Mar 2023 20:22:27 GMT. Likes: 0, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 49. Media: Photo. Content: "Woke Mob Violently Attacks Charlie Kirk Event. A conservative activist's speaking event at a college in California descended into chaos and violence after a liberal outlet slandered.."

- **Post [post:16]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Wed, 15 Mar 2023 19:06:53 GMT. Likes: 3822, Reposts: 1078, Quotes: 47, Replies: 325, Bookmarks: 10, Views: 112541. Content: "BREAKING: SacBee APOLOGIZES for smearing Charlie Kirk after Antifa violence at UC Davis TPUSA event: “A review of the video shows that Kirk never advocated for trans people to be lynched.” https://thepostmillennial.com/breaking-sacbee-apologizes-for-smearing-charlie-kirk-after-antifa-violence-at-uc-davis-tpusa-event?utm_campaign=64501"

- **Post [post:49]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Thu, 16 Mar 2023 01:43:48 GMT. Likes: 2745, Reposts: 879, Quotes: 21, Replies: 201, Bookmarks: 23, Views: 104909. Media: Video (~200s). Content: "Went on with Jesse Watters tonight to explain what happened at UC Davis last night, and most importantly why it happened. Hint: UC Davis Chancellor Gary S. May and Sacramento Bee played leading roles."

- **Post [post:50]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Wed, 15 Mar 2023 22:08:06 GMT. Likes: 369, Reposts: 94, Quotes: 1, Replies: 24, Bookmarks: 5, Views: 49237. Content: "🚨NEW EPISODE featuring James O'Keefe🚨 He breaks some major news on his future plans. Then, I explain what really happened at UC Davis."

- **Post [post:51]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Wed, 15 Mar 2023 01:04:41 GMT. Likes: 1563, Reposts: 189, Quotes: 14, Replies: 265, Bookmarks: 7, Views: 229223. Media: 3 photos. Content: "My welcoming committee at UC Davis."

- **Post [post:53]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Wed, 15 Mar 2023 01:04:41 GMT. (Cross-reference to media in [post:51]).

- **Post [post:21]**: Author: Turning Point USA (@TPUSA). Timestamp: Thu, 16 Mar 2023 19:00:18 GMT. Likes: 81, Reposts: 14, Quotes: 0, Replies: 7, Bookmarks: 0, Views: 6503. Content: "It’s not unusual for TPUSA to experience protests and petitions from radical leftists at campus events, but to have LEGISLATORS calling for the cancellation of an event is a new escalation in the culture war." (Context from Pitt thread, but references general campus events).

### Other Mentions / Upcoming Events Referenced in Range
- **Post [post:26]**: Author: Erin Reed (@ErinInTheMorn). Timestamp: Fri, 17 Mar 2023 00:55:28 GMT. Likes: 439, Reposts: 14, Quotes: 0, Replies: 6, Bookmarks: 2, Views: 24619. Content: "Anyway, here are Charlie Kirk's next couple tour stops: Rutgers - March 20th LSU - March 21st."

- **Post [post:27]**: Author: Talia Jane (@taliaotg). Timestamp: Wed, 15 Mar 2023 04:19:34 GMT. Likes: 350, Reposts: 77, Quotes: 8, Replies: 1, Bookmarks: 7, Views: 70847. Media: Photo (flyer). Content: "Charlie Kirk & Candace Owens are scheduled to speak at @RutgersU New Brunswick on Monday, March 20th. I received this flyer giving notice of a planned counter demonstration featuring Kirk’s extremely shrunken face about their visit to “spew fascist propaganda.”"

- **Post [post:47]**: Author: Aleana Toth (@AleanaSmiley). Timestamp: Thu, 16 Mar 2023 23:36:04 GMT. Likes: 21, Reposts: 6, Quotes: 0, Replies: 2, Bookmarks: 0, Views: 812. Media: 2 photos. Content: "Big day for TPUSA’s LSU chapter! They were awarded $1,000 & recognized by @AGJeffLandry for their hard work! He made sure to highlight the Live Free Tour at LSU - happening Tuesday the 21st ft. @RealCandaceO @TPUSA @tpusa_gulf @tpusastudents @TPUSAEvents."

- **Post [post:22]**: Author: Turning Point USA (@TPUSA). Timestamp: Thu, 16 Mar 2023 19:00:17 GMT. Likes: 14, Reposts: 3, Quotes: 0, Replies: 2, Bookmarks: 0, Views: 1682. Content: "The Turning Point USA chapter at Pitt has an event scheduled on March 27 featuring former NCAA swimmer Riley Gaines. Another group on campus will be hosting a debate on April 18th that will feature @realDailyWire host @michaeljknowles and transgender scholar Deirdre McCloskey." (Pitt context in thread [post:39]).

- **Post [post:39]**: Author: Turning Point USA (@TPUSA). Timestamp: Thu, 16 Mar 2023 19:00:17 GMT. Likes: 73, Reposts: 45, Quotes: 4, Replies: 15, Bookmarks: 0, Views: 12705. Content: "🚨BREAKING: PA Legislators Call for the Cancellation of TPUSA Event at the University of Pittsburgh https://tpusa.com/live/pa-legislators-call-for-the-cancellation-of-tpusa-event-at-the-university-of-pittsburgh/" (Thread includes student petition and legislator details).

- **Post [post:23]**: Author: Turning Point USA (@TPUSA). Timestamp: Wed, 15 Mar 2023 02:09:33 GMT. Likes: 146, Reposts: 53, Quotes: 2, Replies: 10, Bookmarks: 3, Views: 39046. Content: "🔴LIVE: TPUSA Presents The LIVE FREE Tour w/ @Charliekirk11 at UC Davis https://www.youtube.com/live/bxT2R9YLUag?feature=share." (Live stream reference).

- **Post [post:25]**: Author: Turning Point USA (@TPUSA). Timestamp: Wed, 15 Mar 2023 01:36:04 GMT. Likes: 225, Reposts: 61, Quotes: 6, Replies: 27, Bookmarks: 1, Views: 118464. Media: Photo. Content: "HAPPENING NOW AT UC DAVIS: Police carry Antifa members out of the LIVE FREE TOUR venue’s second floor."

- **Post [post:0] / [post:8]**: Author: Kate Burns (@Katerqburns). Timestamp: Fri, 17 Mar 2023 23:34:18 GMT. Likes: 1, Reposts: 0, Quotes: 0, Replies: 1, Bookmarks: 0, Views: 665. Quoted post (Feb 10, 2023): "First 9 dates below 🚨" with photo. Content: "The first stop of the kingdom to the Cali tour by 🥬worship, Sean Feucht and TPUSA faith is kicking off now in Baton Rouge." (Mentions TPUSA Faith tour, not Charlie Kirk specifically).

- **Post [post:7]**: Author: MONICA PAIGE✰TPUSA (@MonicaPaigeTV). Timestamp: Fri, 17 Mar 2023 22:07:27 GMT. Likes: 25, Reposts: 3, Quotes: 1, Replies: 3, Bookmarks: 0, Views: 6444. Content: "I had the absolute pleasure speaking with @OliLondonTV today about the dangers of child gender transitioning - after TLC’s “I Am Jazz” star, Jazz Jennings still doesn’t feel like “herself.” Side topic: Dylan Mulvaney — is it all an act??! 😯😯" (TPUSA-affiliated speaker, not event location).

- **Post [post:34]**: Author: Turning Point USA (@TPUSA). Timestamp: Mon, 13 Mar 2023 21:50:11 GMT. Likes: 273, Reposts: 104, Quotes: 7, Replies: 30, Bookmarks: 4, Views: 243228. Content: "Tune in at 7PM EST/4PM PST for a MAJOR ANNOUNCEMENT from @charliekirk11 & @RealCandaceO" (Announcement context, possibly related to tours).

- **Post [post:3]**: Author: LadyS 🇺🇸 ✨ #StandWithHumanRights (@midsearch). Timestamp: Fri, 17 Mar 2023 23:02:38 GMT. Likes: 1, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 12. Content: "Using faith to pander for Russia and China. New low for @tpusa @charliekirk11 People will discuss, facts will be revealed before the election and you will be a joke in the conversation. Your making."

- **Post [post:2]**: Author: AirCondaTv (I am Charlie Kirk) 🇺🇸 (@AircondaTvT). Timestamp: Fri, 17 Mar 2023 23:09:49 GMT. Likes: 1, Reposts: 0, Quotes: 0, Replies: 0, Bookmarks: 0, Views: 121. Content: Personal streaming post, unrelated to events.

No additional posts in the exact date range referenced other specific Charlie Kirk/TPUSA speaking events or locations beyond the UC Davis event (March 14/15) and references to upcoming Rutgers (March 20) and LSU (March 21) stops. All data pulled directly from tool results for the specified week.
```

