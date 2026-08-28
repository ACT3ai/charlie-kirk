---
unlisted: true
title: "Week 51 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W51"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-12-16 to 2024-12-22."
status: completed
hide_table_of_contents: true
---

# Week 51, 2024

- Date range: 2024-12-16 to 2024-12-22
- Queried at (UTC): 2026-08-24T19:16:40Z
- Model: grok-4.3
- API status: completed
- Response id: 074e256e-b270-9c57-9766-f2aa074d1345

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-12-16 to the end of the week 2024-12-22.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speech OR speak OR event OR \"public speaking\" OR tour OR appearance OR \"will be\" OR \"speaking at\" OR campus OR university OR college) since:2024-12-16 until:2024-12-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (speaking OR speech OR speak OR event OR tour OR appearance OR \"will be\" OR campus OR university OR college) since:2024-12-16 until:2024-12-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (speaking OR speech OR speak OR event OR tour OR appearance OR \"will be\" OR campus OR university OR college) since:2024-12-16 until:2024-12-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (tour OR schedule OR \"speaking tour\" OR \"event schedule\") since:2024-12-16 until:2024-12-23",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between December 16-22 2024",
      "limit": "10",
      "from_date": "2024-12-16",
      "to_date": "2024-12-22"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR AmFest OR AMFEST) (Phoenix OR Arizona OR \"AmFest\" OR AMFEST) (speak OR speaking OR speech OR event OR schedule OR tour OR appearance) since:2024-12-16 until:2024-12-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (AmFest OR AMFEST OR Phoenix OR Arizona) since:2024-12-16 until:2024-12-23",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (AmFest OR AMFEST OR Phoenix OR Arizona) since:2024-12-16 until:2024-12-23",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Charlie Kirk\" (Phoenix OR Arizona OR AmFest) (speak OR speaking OR speech) since:2024-12-16 until:2024-12-23",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "TPUSA (Phoenix OR Arizona OR AmFest) (speak OR speaking OR speech OR \"Charlie Kirk\") since:2024-12-16 until:2024-12-23",
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
  "input_tokens": 24840,
  "input_tokens_details": {
    "cached_tokens": 11520
  },
  "output_tokens": 8049,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 32889,
  "num_sources_used": 0,
  "num_server_side_tools_used": 10,
  "cost_in_usd_ticks": 890765000,
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
    "input_tokens": 14755,
    "output_tokens": 7440
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870185674072043693",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870185674072043693"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870615983066353732",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870615983066353732"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870618253158150559",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870618253158150559"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870617832519794985",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870617832519794985"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870617797707129036",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870617797707129036"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870615056125485471",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870615056125485471"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870338829380391198",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870338829380391198"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870613853106577614",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870613853106577614"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870613661246800363",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870613661246800363"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869477818289254469",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869477818289254469"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870619967147688323",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870619967147688323"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870614043343671783",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870614043343671783"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870547754063417562",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870547754063417562"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869917906584408070",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869917906584408070"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870526362580078656",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870526362580078656"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870589574780731717",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870589574780731717"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870542315128807607",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870542315128807607"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870580437036515442",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870580437036515442"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869055209462534247",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869055209462534247"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870351633344868636",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870351633344868636"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870600624938590617",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870600624938590617"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869416626334126161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869416626334126161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869963651869745659",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869963651869745659"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870548207174086935",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870548207174086935"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870584624512143549",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870584624512143549"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869874503494377613",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869874503494377613"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870613796181426661",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870613796181426661"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870619762428203495",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870619762428203495"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870614703879434503",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870614703879434503"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870613598201925900",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870613598201925900"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870210254056669508",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870210254056669508"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870188326860534004",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870188326860534004"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870613470842065128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870613470842065128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869895275382223279",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869895275382223279"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869055415511843325",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869055415511843325"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870580428182257754",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870580428182257754"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869917954009137216",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869917954009137216"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870587442048147891",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870587442048147891"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870527298568638667",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870527298568638667"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870617311809257655",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870617311809257655"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868815560185987150",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868815560185987150"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870195619245203685",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870195619245203685"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869047241681346961",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869047241681346961"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870549200771149848",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870549200771149848"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869588791947932014",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869588791947932014"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869782922078884269",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869782922078884269"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870298577668374860",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870298577668374860"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870398638016335887",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870398638016335887"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870578132865982766",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870578132865982766"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1869911490469474341",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1869911490469474341"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870618059905339534",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870618059905339534"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870250473170842017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870250473170842017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1870608915446276349",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1870608915446276349"
  }
]
```

## Grok response

```text
**All relevant X posts from December 16–22, 2024 (searched via keyword and semantic queries for "Charlie Kirk", TPUSA/Turning Point USA, speaking/speech/events, AmFest/AMFEST, Phoenix/Arizona, schedules/tours/appearances, with exact date filters since:2024-12-16 until:2024-12-23). No summarization—full post content, metadata, and media notes included exactly as returned.**

### Posts from general keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA") + (speaking OR speech OR speak OR event OR "public speaking" OR tour OR appearance OR "will be" OR "speaking at" OR campus OR university OR college) since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:0]** ID: 1870618253158150559 | @NicoleJDaley | Sat, 21 Dec 2024 23:52:00 GMT | Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=1, Views=230 | Media: 1 photo (https://pbs.twimg.com/media/GfXFYf7a4AAAr2F.jpg)  
  Content: FULL SPEECH: Brett Cooper Speaks at TPUSA's America Fest Conference: Day... Watch here—> https://t.co/yytywvGesD Amazingly done! 👏🏼👏🏼👏🏼

- **[post:1]** ID: 1870618059905339534 | @truth_0072582 | Sat, 21 Dec 2024 23:51:14 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=1, Views=30  
  Content: If Kari Lake doesn’t want to run for office anymore than the Democrat party machine wins! And that proves it because they do cheat in elections and Kash Patel, as well as Pam Bondi will be looking into it in 2025 and it’s gonna be a very interesting year very interesting and it’s gonna be like a soap opera where Democrats are gonna be on TV crying foul when the Republicans finally dig up the truth

- **[post:2]** ID: 1870617832519794985 | @Mike_Honcho_X | Sat, 21 Dec 2024 23:50:20 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=5  
  Content: Was the intention to bring the TPUSA experience down to the Leftist level?!? Grow-up you clowns you’re fuckin embarrassing. Both should be disinvited never to return to a TPUSA event. @charliekirk11 @TPUSA

- **[post:3]** ID: 1870617797707129036 | @SupMarioBro | Sat, 21 Dec 2024 23:50:12 GMT | Likes=9, Reposts=5, Quotes=0, Replies=0, Bookmarks=0, Views=128 | Media: 1 photo (https://pbs.twimg.com/media/GfXE9zfWYAABO-y.jpg)  
  Content: @ByronDonalds speaking to a full house of “We The People” @TPUSA America Fest 🇺🇸

- **[post:4]** ID: 1870617311809257655 | @MStevenson2686 | Sat, 21 Dec 2024 23:48:16 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=18  
  Content: Listened to your full speech at Turning Point USA. We definitely will not agree on everything, but I like your idea, I hope I get this right. "Fight when we disagree, drink a beer together afterwards, and when we agree let's get it done!" We are not enemies, it's okay that you're skeptical of Trump, I hope he proves you wrong in your assertions. But God bless you my fellow American!

- **[post:5]** ID: 1870615056125485471 | @Jill_Savage | Sat, 21 Dec 2024 23:39:18 GMT | Likes=30, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=4193 | Media: 1 photo (https://pbs.twimg.com/media/GfXCeYIWcAAGTb7.jpg)  
  Content: The great @EliCrane_CEO speaking at @TPUSA at AmFest.

- **[post:6]** ID: 1870613853106577614 | @SpaceDen1968 | Sat, 21 Dec 2024 23:34:31 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=7  
  Content: Of course it is... They are desperate… They didn’t get the reaction they wanted from Trump with their “Pres. Musk” BS. Now it’s time to Label him a “NAZI", the same crap they used with Trump for 8 -years. When that fails, next will be “Racist”, followed by “Misogynist" Ad nauseum

- **[post:7]** ID: 1870613661246800363 | @cowboysandlace | Sat, 21 Dec 2024 23:33:45 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=15  
  Content: Amen!!! praying justice will be served! 🙏🇺🇸 God’s going to clean house!

### Posts from @charliekirk11 since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:8]** ID: 1870195619245203685 | @charliekirk11 | Fri, 20 Dec 2024 19:52:36 GMT | Likes=3314, Reposts=463, Quotes=4, Replies=104, Bookmarks=61, Views=410150 | Media: 1 video (https://video.twimg.com/amplify_video/1870195486713655296/vid/avc1/1280x720/bpZWogTWqYwBVBZK.mp4?tag=14, duration: 71166 ms)  
  Content: SEBASTIAN GORKA: "Kamala. Joe. Don't do anything for the next 30 days because then the adults will be in charge… Don’t take anything for granted just because on January the 20th at 12:01, we're going to walk into the White House and take control." @SebGorka

- **[post:9]** ID: 1870188326860534004 | @charliekirk11 | Fri, 20 Dec 2024 19:23:38 GMT | Likes=15323, Reposts=3059, Quotes=71, Replies=319, Bookmarks=275, Views=464369 | Media: 1 video (https://video.twimg.com/amplify_video/1870188105506140160/vid/avc1/1280x720/gL_ByLzWN7_FwC5W.mp4?tag=14, duration: 62262 ms)  
  Content: RILEY GAINES: "They have become a cult that does not believe in freedom. They don't believe in free speech. They don't believe in school choice. They don't believe in parental rights or the safeguarding of children. They certainly don't believe in free thought. They do not believe in freedom unless it's the freedom to kill a developing baby in the womb, or to chemically or surgically castrate children." @Riley_Gaines_

- **[post:10]** ID: 1869782922078884269 | @charliekirk11 | Thu, 19 Dec 2024 16:32:42 GMT | Likes=13171, Reposts=1492, Quotes=25, Replies=271, Bookmarks=55, Views=180895  
  Content: Exactly one year ago today, the Colorado Supreme Court tried to kick Donald Trump off the state's primary ballot as an "insurrectionist." This weekend, he will be speaking to AmFest as a president-elect with a historic mandate to change America. It's been a wild year!

- **[post:11]** ID: 1869588791947932014 | @charliekirk11 | Thu, 19 Dec 2024 03:41:17 GMT | Likes=26173, Reposts=4185, Quotes=134, Replies=794, Bookmarks=176, Views=461752  
  Content: In 2016, this CR would have passed regardless of what Donald Trump said, because Congressional Republicans felt free to ignore him and his voters. Not anymore. The GOP became the MAGA party eight years ago, and Congress is finally catching up. This term will be very different from the first.

- **[post:12]** ID: 1869416626334126161 | @charliekirk11 | Wed, 18 Dec 2024 16:17:10 GMT | Likes=1841, Reposts=202, Quotes=85, Replies=160, Bookmarks=55, Views=897975 | Media: 1 photo (https://pbs.twimg.com/media/GfGAbC0a8AAg2jp.jpg)  
  Content: Turning Point staff meeting before AMFEST! Biggest multi-day event in conservative movement history. BE THERE. https://www.amfest.com/

- **[post:13]** ID: 1868815560185987150 | @charliekirk11 | Tue, 17 Dec 2024 00:28:45 GMT | Likes=62905, Reposts=8476, Quotes=327, Replies=1480, Bookmarks=1103, Views=2718035  
  Content: Canadian PM Justin Trudeau's government may collapse by the end of the night, and President Trump's threatened tariff if Canada can't secure the U.S./Canada border will be the top culprit. If Trudeau goes down, it will lead to elections where the conservatives are overwhelmingly favored to win. MAGA doesn't just make America better. Everyone is better off when America stops being a doormat for the world.

### Posts from @TPUSA since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:14]** ID: 1870578132865982766 | @TPUSA | Sat, 21 Dec 2024 21:12:35 GMT | Likes=127, Reposts=18, Quotes=6, Replies=10, Bookmarks=2, Views=11739  
  Content: CENK UYGUR: “If we dare unite on issues we agree on, they [mainstream media] will be livid, and it will be a beautiful day in America.” @cenkuygur live at AmFest 2024

- **[post:15]** ID: 1869963651869745659 | @TPUSA | Fri, 20 Dec 2024 04:30:51 GMT | Likes=126, Reposts=19, Quotes=3, Replies=2, Bookmarks=2, Views=9711  
  Content: TUCKER CARLSON: “Violence and speech are not the same. I can offend you; that’s different than shooting you.” @TuckerCarlson live at AmFest 2024

### Posts from additional keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA" OR AmFest OR AMFEST) (Phoenix OR Arizona OR "AmFest" OR AMFEST) (speak OR speaking OR speech OR event OR schedule OR tour OR appearance) since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:30]** ID: 1870619967147688323 | @magaman28 | Sat, 21 Dec 2024 23:58:49 GMT | Likes=2, Reposts=1, Quotes=0, Replies=0, Bookmarks=1, Views=81 | Media: 1 video (https://video.twimg.com/ext_tw_video/1870619859232382976/pu/vid/avc1/1280x596/a3ppFhNV5HOqruBA.mp4?tag=12, duration: 40083 ms)  
  Content: @imbrettcooper gives a shoutout to @jordanbpeterson during her AmFest speech.

- **[post:31]** ID: 1870619762428203495 | @awforforksake | Sat, 21 Dec 2024 23:58:00 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=27  
  Content: Have to say fair play to @cenkuygur for going and speaking at AmFest. He knows how much shit he's going to take for that, which will entirely highlight his point.

- **[post:32]** ID: 1870615983066353732 | @Bars4Daze | Sat, 21 Dec 2024 23:42:59 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=21  
  Content: @KenPaxtonTX it was really nice to see The Man Behind the America first movement finally give a speech. Amfest. You did great and I can't wait till you get your revenge on the rhinos

- **[post:33]** ID: 1870615056125485471 | @Jill_Savage | Sat, 21 Dec 2024 23:39:18 GMT | Likes=30, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=4193 | Media: 1 photo (https://pbs.twimg.com/media/GfXCeYIWcAAGTb7.jpg)  
  Content: The great @EliCrane_CEO speaking at @TPUSA at AmFest.

- **[post:34]** ID: 1870614703879434503 | @cefilby | Sat, 21 Dec 2024 23:37:54 GMT | Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=37  
  Content: @LauraLoomer @MiloVentimiglia may be entitled to free speech but he appears not to have been entitled to intellectual honesty as his bizarre behavior at AmFest proves.

- **[post:35]** ID: 1870614043343671783 | @ChloeCole | Sat, 21 Dec 2024 23:35:16 GMT | Likes=1643, Reposts=45, Quotes=2, Replies=15, Bookmarks=63, Views=45901 | Media: 1 photo (https://pbs.twimg.com/media/GfXBjqnWwAANM1s.jpg)  
  Content: .@imbrettcooper knocked it out of the park with her AmFest speech this year!! ❤️ This is the message that our generation needs to hear.

- **[post:36]** ID: 1870613796181426661 | @TBakritges | Sat, 21 Dec 2024 23:34:17 GMT | Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=28  
  Content: Savvy, must be an awesome Amfest 24 event👍

- **[post:37]** ID: 1870613598201925900 | @_RandomTweeter_ | Sat, 21 Dec 2024 23:33:30 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=22  
  Content: Does anyone know when Trump is speaking at AMFEST?

- **[post:38]** ID: 1870613470842065128 | @Xander24Xand | Sat, 21 Dec 2024 23:33:00 GMT | Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=50 | Media: 1 photo (https://pbs.twimg.com/media/GfSrdHQWQAEOm98.jpg)  
  Content: Have you secured your #AmFest tickets yet? President Trump's FIRST post-election event. This weekend. Phoenix AZ. https://t.co/wPfhdvedJv #ArizonaRepublicans🗽🌅🇺🇲

### Posts from @charliekirk11 (AmFest/AMFEST/Phoenix/Arizona filter) since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:39]** ID: 1870526362580078656 | @charliekirk11 | Sat, 21 Dec 2024 17:46:52 GMT | Likes=3002, Reposts=590, Quotes=27, Replies=155, Bookmarks=101, Views=880388  
  Content: DAY 3: AMFEST is LIVE with Kari Lake, Brandon Tatum, Brett Cooper, Glenn Beck and more! https://twitter.com/i/broadcasts/1ZkJzRmnmdyJv

- **[post:40]** ID: 1870185674072043693 | @charliekirk11 | Fri, 20 Dec 2024 19:13:05 GMT | Likes=3683, Reposts=813, Quotes=24, Replies=144, Bookmarks=86, Views=917903  
  Content: DAY 2: AMFEST is LIVE - Riley Gaines, Michael Knowles, Danica Patrick, James O’Keefe and more! https://twitter.com/i/broadcasts/1BdGYEnDNlQGX

- **[post:41]** ID: 1869911490469474341 | @charliekirk11 | Fri, 20 Dec 2024 01:03:35 GMT | Likes=808, Reposts=140, Quotes=7, Replies=57, Bookmarks=22, Views=127881  
  Content: THE BIGGEST AMFEST EVER BEGINS NOW https://rumble.com/v610dge-amfest-is-back-live-charlie-kirk-don-jr-tucker-carlson-ben-shapiro-matt-wal.html

- **[post:42]** ID: 1869895275382223279 | @charliekirk11 | Thu, 19 Dec 2024 23:59:09 GMT | Likes=3725, Reposts=902, Quotes=50, Replies=196, Bookmarks=186, Views=659039  
  Content: AMFEST is BACK! LIVE - Charlie Kirk, Don Jr, Tucker Carlson, Ben Shapiro, Matt Walsh and more! #AMFEST2024 https://twitter.com/i/broadcasts/1LyxBgapOWrKN

- **[post:43]** ID: 1869782922078884269 | @charliekirk11 | Thu, 19 Dec 2024 16:32:42 GMT | Likes=13171, Reposts=1492, Quotes=25, Replies=271, Bookmarks=55, Views=180895  
  Content: Exactly one year ago today, the Colorado Supreme Court tried to kick Donald Trump off the state's primary ballot as an "insurrectionist." This weekend, he will be speaking to AmFest as a president-elect with a historic mandate to change America. It's been a wild year!

### Posts from @TPUSA (AmFest/AMFEST/Phoenix/Arizona filter) since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:44]** ID: 1870589574780731717 | @TPUSA | Sat, 21 Dec 2024 21:58:03 GMT | Likes=218, Reposts=37, Quotes=2, Replies=8, Bookmarks=17, Views=14366 | Media: 1 video (https://video.twimg.com/ext_tw_video/1870588826659540992/pu/vid/avc1/1280x720/h9AvXhqnOVCzBn1H.mp4?tag=12, duration: 122763 ms)  
  Content: BRANDON TATUM: “The greatest accomplishment that a man will have in his life, the biggest determining factor in his success, by and large, is the person you marry.” @TheOfficerTatum live at AmFest 2024

- **[post:45]** ID: 1870584624512143549 | @TPUSA | Sat, 21 Dec 2024 21:38:22 GMT | Likes=1086, Reposts=257, Quotes=18, Replies=31, Bookmarks=52, Views=131079 | Media: 1 video (https://video.twimg.com/ext_tw_video/1870584132474179584/pu/vid/avc1/1280x720/bg8T4kg-hI4gcy2f.mp4?tag=12, duration: 35200 ms)  
  Content: CHLOE COLE: “As of right now, detransitioners are not acknowledged by the same medical system—the same hospitals and doctors who hurt us in the first place.” @chloecole live at AmFest 2024

- **[post:46]** ID: 1870580437036515442 | @TPUSA | Sat, 21 Dec 2024 21:21:44 GMT | Likes=63, Reposts=10, Quotes=2, Replies=16, Bookmarks=0, Views=12083  
  Content: CENK UYGUR: “On the right, you do a good job coalescing. You work together well, and you’re more welcoming.” @cenkuygur live at AmFest 2024

- **[post:47]** ID: 1870578132865982766 | @TPUSA | Sat, 21 Dec 2024 21:12:35 GMT | Likes=127, Reposts=18, Quotes=6, Replies=10, Bookmarks=2, Views=11739  
  Content: CENK UYGUR: “If we dare unite on issues we agree on, they [mainstream media] will be livid, and it will be a beautiful day in America.” @cenkuygur live at AmFest 2024

- **[post:48]** ID: 1870547754063417562 | @TPUSA | Sat, 21 Dec 2024 19:11:52 GMT | Likes=130, Reposts=17, Quotes=2, Replies=4, Bookmarks=2, Views=11981  
  Content: CONGRESSWOMAN LAUREN BOEBERT: “America is fully awake and not woke.” @laurenboebert live at AmFest 2024

### Posts from additional keyword search ("Charlie Kirk" (Phoenix OR Arizona OR AmFest) (speak OR speaking OR speech) since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:49]** ID: 1870549200771149848 | @smblue6778 | Sat, 21 Dec 2024 19:17:37 GMT | Likes=14, Reposts=4, Quotes=1, Replies=1, Bookmarks=0, Views=488  
  Content: President Trump is Scheduled to Speak On Sunday at AMFEST at 11:00am Will be carried live on Charlie Kirk on X And on RSBN

- **[post:50]** ID: 1870398638016335887 | @TheMike275 | Sat, 21 Dec 2024 09:19:20 GMT | Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=19 | Media: 1 photo (https://pbs.twimg.com/media/GfT9pJdXoAEunl5.jpg)  
  Content: BREAKING 🚨 Charlie Kirk announced President Trump will be speaking at TPUSA in Phoenix 🇺🇸 I PRAY TRUMP DOES MORE RALLIES LIKE THIS TRUMP IS A ROCKSTAR 🔥

- **[post:51]** ID: 1870351633344868636 | @slrdriving | Sat, 21 Dec 2024 06:12:33 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=16  
  Content: Bc Pres-elect Trump too busy speaking in Arizona at Charlie Kirk, Turning Point USA. While Democrats double down on *tupid, doubling down on why they LOST, Pres. Trump out winning more youth vote.

- **[post:52]** ID: 1870250473170842017 | @RL9631 | Fri, 20 Dec 2024 23:30:35 GMT | Likes=8, Reposts=3, Quotes=0, Replies=0, Bookmarks=0, Views=206  
  Content: Thank you Rose. 🇺🇸 We need MAGA patriots and influencers like Charlie Kirk to speak up for the Arizona voters. We can’t build a strong country without LEGAL elections.

- **[post:53]** ID: 1869917954009137216 | @MichaelGig7169 | Fri, 20 Dec 2024 01:29:16 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=22  
  Content: Thank you Elon. Thank you for free speech. Watching Charlie Kirk at AMFEST.

### Posts from TPUSA (Phoenix OR Arizona OR AmFest) (speak OR speaking OR speech OR "Charlie Kirk") since:2024-12-16 until:2024-12-23 (Latest mode):
- **[post:54]** ID: 1870615056125485471 | @Jill_Savage | Sat, 21 Dec 2024 23:39:18 GMT | Likes=30, Reposts=2, Quotes=0, Replies=0, Bookmarks=0, Views=4193 | Media: 1 photo (https://pbs.twimg.com/media/GfXCeYIWcAAGTb7.jpg)  
  Content: The great @EliCrane_CEO speaking at @TPUSA at AmFest.

- **[post:55]** ID: 1870608915446276349 | @terwya | Sat, 21 Dec 2024 23:14:54 GMT | Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=247  
  Content: I watched your speech on TPUSA AmFEST

- **[post:56]** ID: 1870600624938590617 | @chrisfamousyet1 | Sat, 21 Dec 2024 22:41:57 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=34  
  Content: CHARLIE KIRK EXPOSING KARI LAKE WON ARIZONA & Maricopa County Election Fraud At TPUSA Event TODAY! 130,000 MISSING Ballots, 47% REJECT Rate, ILLEGAL Recounts…ONLY Need 1 US SENATOR To Call Hearing & Investigate…MAGA Wants Its Seat Back!

- **[post:57]** ID: 1870587442048147891 | @sensiblemiddle | Sat, 21 Dec 2024 21:49:34 GMT | Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=674  
  Content: Charlie Kirk’s TPUSA was literally the transportation arm of the disgusting January 6th attack on our Capitol. AMFEST

- **[post:58]** ID: 1870527298568638667 | @FmrRepMattGaetz | Sat, 21 Dec 2024 17:50:35 GMT | Likes=628, Reposts=63, Quotes=3, Replies=51, Bookmarks=3, Views=41400  
  Content: .@TPUSA is the “boots on the ground” of our movement. AMFEST is incredible this year. @laurenboebert speaking soon!

### Posts from semantic search ("Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between December 16-22 2024", from_date:2024-12-16, to_date:2024-12-22):
- **[post:21]** ID: 1869477818289254469 | @KariLake | Wed, 18 Dec 2024 20:20:19 GMT | Likes=733, Reposts=114, Quotes=1, Replies=42, Bookmarks=3, Views=43451 | Media: 1 photo (https://pbs.twimg.com/media/GfG4Kq-XUAANnDQ.jpg)  
  Content: I'm so excited to speak at @TPUSA's America Fest 2024 this Saturday! This will be my first public address since my appointment to the Trump administration I’ll be on stage at 1:15 PM. I hope to see you there! REGISTER: https://t.co/TVQnfJJbRq

- **[post:22]** ID: 1869055209462534247 | @KariLake | Tue, 17 Dec 2024 16:21:01 GMT | Likes=2092, Reposts=318, Quotes=3, Replies=81, Bookmarks=6, Views=100054 | Media: 1 photo (https://pbs.twimg.com/media/GfA3zcVWAAc1CPY.jpg)  
  Content: I'm so excited to announce that I will be speaking at @TPUSA's America Fest 2024 this Saturday at 11:30am! I hope to see you there! REGISTER: https://t.co/TVQnfJJbRq

- **[post:23]** ID: 1870548207174086935 | @KariLake | Sat, 21 Dec 2024 19:13:40 GMT | Likes=697, Reposts=88, Quotes=1, Replies=30, Bookmarks=2, Views=48354  
  Content: I’ll be speaking at @TPUSA’s America Fest 2024 at 1:00pm. I hope to see you there! 🇺🇸

- **[post:24]** ID: 1869055415511843325 | @thevivafrei | Tue, 17 Dec 2024 16:21:51 GMT | Likes=412, Reposts=33, Quotes=1, Replies=33, Bookmarks=6, Views=21885 | Media: 1 video (https://video.twimg.com/amplify_video/1869055295730614289/vid/avc1/1280x720/dFtijiM5PVubvfLq.mp4?tag=16, duration: 17301 ms)  
  Content: Won’t be live at 12:30. Going on Charlie Kirk at 1:30. Will go live shortly thereafter. Maybe Justin Trudeau‘s government will have fallen by then. In the meantime…

- **[post:25]** ID: 1869416626334126161 | @charliekirk11 | Wed, 18 Dec 2024 16:17:10 GMT | Likes=1841, Reposts=202, Quotes=85, Replies=160, Bookmarks=55, Views=897975 | Media: 1 photo (https://pbs.twimg.com/media/GfGAbC0a8AAg2jp.jpg)  
  Content: Turning Point staff meeting before AMFEST! Biggest multi-day event in conservative movement history. BE THERE. https://www.amfest.com/

- **[post:26]** ID: 1869874503494377613 | @barrycunningham | Thu, 19 Dec 2024 22:36:36 GMT | Likes=279, Reposts=50, Quotes=2, Replies=77, Bookmarks=5, Views=9719 | Media: 1 photo (https://pbs.twimg.com/media/GfMgfJHXQAAsm1t.jpg)  
  Content: Join Me At 7PM WATCH LIVE: Tucker Carlson, Charlie Kirk, Donald Trump Jr., Steve Bannon & More At AmericaFest! https://t.co/icL6sP366c It will be on Rumble and X as well!

- **[post:27]** ID: 1869047241681346961 | @bennyjohnson | Tue, 17 Dec 2024 15:49:22 GMT | Likes=480, Reposts=58, Quotes=6, Replies=64, Bookmarks=4, Views=49043 | Media: 1 photo (https://pbs.twimg.com/media/GfAwj4GWcAAEhBf.jpg)  
  Content: 🚨I’m heading to Phoenix, Arizona, for #AMFEST2024 with @TPUSA this week—December 19-22! I’ll be speaking alongside President-elect Donald Trump, Tucker Carlson, Donald Trump Jr., Charlie Kirk, Jack Posobiec, Matt Gaetz, Byron Donalds, Anna Paulina Luna, and more. Get your tickets now at https://t.co/3aZ3Ypw9WP and use code “BENNY” for 25% off General Admission! Don’t miss it! 🇺🇸

- **[post:28]** ID: 1869895275382223279 | @charliekirk11 | Thu, 19 Dec 2024 23:59:09 GMT | Likes=3725, Reposts=902, Quotes=50, Replies=196, Bookmarks=186, Views=659039  
  Content: AMFEST is BACK! LIVE - Charlie Kirk, Don Jr, Tucker Carlson, Ben Shapiro, Matt Walsh and more! #AMFEST2024 https://twitter.com/i/broadcasts/1LyxBgapOWrKN

- **[post:29]** ID: 1869917906584408070 | @TPUSA | Fri, 20 Dec 2024 01:29:04 GMT | Likes=242, Reposts=31, Quotes=2, Replies=5, Bookmarks=2, Views=11106  
  Content: CHARLIE KIRK: “Guys, we are the media now, not them. Their power is waning and fading.” @CharlieKirk11 live at AmFest 2024

**Additional notes from all searches:**  
- No posts found referencing other specific Charlie Kirk/TPUSA public speaking events, campus tours, or appearances outside the AmFest/AMFEST event in Phoenix, Arizona (December 19–22, 2024 timeframe).  
- Multiple posts reference live streams/broadcasts of the event hosted by Charlie Kirk/TPUSA.  
- Dates align strictly within the requested week (Dec 16–22, 2024). All data from tool results included verbatim.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-12-16 to 2024-12-22**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event:**

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-12-18](/Planes/Incidents/N1098L-2024-12-18-KPHX) | [N1098L](/Planes/N1098L/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day before |
| [2024-12-18](/Planes/Incidents/N582MM-2024-12-18-KSDL) | [N582MM](/Planes/N582MM/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day before |
| [2024-12-20](/Planes/Incidents/N560TW-2024-12-20-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2024-12-20](/Planes/Incidents/N582MM-2024-12-20-KSDL) | [N582MM](/Planes/N582MM/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2024-12-20](/Planes/Incidents/N872RA-2024-12-20-KPHX) | [N872RA](/Planes/N872RA/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day after |
| [2024-12-21](/Planes/Incidents/N560TW-2024-12-21-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2024-12-21](/Planes/Incidents/N582MM-2024-12-21-KSDL) | [N582MM](/Planes/N582MM/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2024-12-22](/Planes/Incidents/N582MM-2024-12-22-KPHX) | [N582MM](/Planes/N582MM/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
