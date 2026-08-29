---
unlisted: true
title: "Week 50 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W50"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-12-09 to 2024-12-15."
status: completed
hide_table_of_contents: true
---

# Week 50, 2024

- Date range: 2024-12-09 to 2024-12-15
- Queried at (UTC): 2026-08-24T19:16:21Z
- Model: grok-4.3
- API status: completed
- Response id: bb911682-e9fb-96a8-8840-db4a95e1497d

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-12-09 to the end of the week 2024-12-15.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Turning Point\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR campus OR rally) since:2024-12-09 until:2024-12-16",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Turning Point\") (speaking OR speak OR event OR tour OR \"public speaking\" OR appearance OR campus OR rally) since:2024-12-09 until:2024-12-16 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, campus tours, or where Charlie will speak between December 9 and December 15 2024",
      "limit": "10",
      "from_date": "2024-12-09",
      "to_date": "2024-12-15"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Turning Point\" OR AmFest OR AMFEST OR \"AmericaFest\") (Phoenix OR AZ OR Arizona) (speak OR speaking OR event OR tour OR campus OR rally OR appearance) since:2024-12-09 until:2024-12-16",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speak OR speaking OR AmFest OR AMFEST OR Phoenix OR campus) since:2024-12-09 until:2024-12-16",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speak OR speaking OR AmFest OR AMFEST OR Phoenix OR campus OR tour) since:2024-12-09 until:2024-12-16",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Mar-a-Lago OR \"Mar a Lago\" OR \"Mar-a-Lago\") since:2024-12-09 until:2024-12-16",
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
  "input_tokens": 19039,
  "input_tokens_details": {
    "cached_tokens": 9984
  },
  "output_tokens": 5118,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 24157,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 611105500,
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
    "input_tokens": 10498,
    "output_tokens": 4651
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867757820843896838",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867757820843896838"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866902265287553079",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866902265287553079"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868020829839368245",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868020829839368245"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868025951788876032",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868025951788876032"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868036548593365314",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868036548593365314"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866126271953912123",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866126271953912123"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867223944962716077",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867223944962716077"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866167473705537605",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866167473705537605"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866171403097297223",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866171403097297223"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868037226380276022",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868037226380276022"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867757491528118410",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867757491528118410"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867988983231426990",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867988983231426990"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866217904707878919",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866217904707878919"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866157060074918140",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866157060074918140"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868040024031424672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868040024031424672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867915413738156432",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867915413738156432"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866917107113357816",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866917107113357816"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867987390683562043",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867987390683562043"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868036854999634430",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868036854999634430"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868009104616427917",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868009104616427917"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867987195782730077",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867987195782730077"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868039624825930129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868039624825930129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866572042989936885",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866572042989936885"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867273333819232546",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867273333819232546"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1867880713615204562",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1867880713615204562"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1868007229229797620",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1868007229229797620"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1866997437925413057",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1866997437925413057"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range December 9–15, 2024 (using since:2024-12-09 until:2024-12-16), containing mentions of Charlie Kirk, TPUSA/Turning Point USA, or related events/speaking appearances. No summarization—full post content, metadata, and context included as retrieved. No posts directly announced new Charlie Kirk campus/public speaking events strictly within Dec 9–15; references primarily tie to upcoming AmFest 2024 (Dec 19–22 in Phoenix, AZ) or a past Mar-a-Lago event.**

### Posts from keyword searches (Latest mode, focused on speaking/events):
- **[post:0]** ID: 1868039624825930129  
  Author: Dragonmist @ thelastcave (@thedark7caves)  
  Timestamp: Sat, 14 Dec 2024 21:05:27 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=10  
  Content: Speaking of the Navy, are you the very same Charlie Kirk that denies the sworn testimony and interviews of U.S.S. Liberty survivors?

- **[post:1]** ID: 1868037226380276022  
  Author: Dr President-Elect Turning Point Tim Buktu (@MichiganWave)  
  Timestamp: Sat, 14 Dec 2024 20:55:55 GMT  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=240  
  Content: There's something amorphous and quickly forgettable about S Sweeney. She looks vaguely like someone who had plastic surgery to achieve a textbook appearance for a C/D list actress or TV commercial extra. It's almost droid-like.

- **[post:2]** ID: 1868036854999634430  
  Author: Prettypeachylife (@Linzie224)  
  Timestamp: Sat, 14 Dec 2024 20:54:27 GMT  
  Engagement: Likes=6, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=420  
  Content: I know that he’s been buying farmland, trying to kill off people but the way Charlie Kirk wrote that post I thought there was a new specific event.

- **[post:3]** ID: 1868036548593365314  
  Author: Claire Gorlich (@clairegorlich)  
  Timestamp: Sat, 14 Dec 2024 20:53:14 GMT  
  Engagement: Likes=36, Reposts=1, Quotes=1, Replies=9, Bookmarks=2, Views=2524  
  Media: Yes (photo: https://pbs.twimg.com/media/GeyZVkpWcAAmtBG.jpg)  
  Content: I am deeply honored and humbled to share that I was invited to Mar-a-Lago this past weekend, where I was presented with the Campus Warrior Award by Charlie Kirk and Turning Point USA.

- **[post:4]** ID: 1868025951788876032  
  Author: Nick Ptinis (@Nick_P_NB)  
  Timestamp: Sat, 14 Dec 2024 20:11:07 GMT  
  Engagement: Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=84  
  Content: Yes it was, It felt like were at a turning point that the PM set his past mistakes right. It was crushing when it was put down like some criminal uprising. @PierrePoilievre If (When) you become PM would you be willing to having a Trucker holliday to commemorate the event?

- **[post:5]** ID: 1868020829839368245  
  Author: @joseph717 (@joseph7173)  
  Timestamp: Sat, 14 Dec 2024 19:50:46 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=7  
  Content: RFK Jr.: Trump Rally in Georgia - Turning Point Action https://t.co/X2pEXFfHs1 via @YouTube

- **[post:6]** ID: 1868009104616427917  
  Author: TPUSA Faith (@tpusafaith)  
  Timestamp: Sat, 14 Dec 2024 19:04:11 GMT  
  Engagement: Likes=30, Reposts=10, Quotes=1, Replies=0, Bookmarks=2, Views=1467  
  Media: Yes (video: https://video.twimg.com/amplify_video/1868008933857579008/vid/avc1/1080x1920/7TYcj1qveQ1ZUnXy.mp4?tag=16, duration: 45458 ms)  
  Content: If we can deny the truth of what a man and woman are, where do the lies stop? 💬 Truth matters, and standing firm in it is more important than ever. Riley Gaines will be speaking at #AmFest2024, Dec. 19-22 in Phoenix, AZ. Use promo code FAITH50 for 50% off General Admission! 🔗 Register now at

- **[post:7]** ID: 1868007229229797620  
  Author: heel duh (@davidheel5duuh)  
  Timestamp: Sat, 14 Dec 2024 18:56:44 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=3  
  Content: A Republican went to a turning point event? Wow!

- **[post:8]** ID: 1868037226380276022 (duplicate from earlier search)  
  (Same as post:1 above)

- **[post:9]** ID: 1868036548593365314 (duplicate)  
  (Same as post:3 above)

- **[post:10]** ID: 1868020829839368245 (duplicate)  
  (Same as post:5 above)

- **[post:11]** ID: 1868009104616427917 (duplicate)  
  (Same as post:6 above)

- **[post:12]** ID: 1867988983231426990  
  Author: Kacee Allen (@KaceeRAllen)  
  Timestamp: Sat, 14 Dec 2024 17:44:13 GMT  
  Engagement: Likes=263, Reposts=54, Quotes=6, Replies=13, Bookmarks=51, Views=42442  
  Media: Yes (video: https://video.twimg.com/amplify_video/1867988694226837505/vid/avc1/886x494/hHpvE8tPSdYSnsx8.mp4?tag=16, duration: 113261 ms)  
  Content: USS Liberty survivor Phil Tourney calls Charlie Kirk and Ben Shapiro cowards for labeling the event as a “conspiracy” and says he will debate them on live television.

- **[post:13]** ID: 1867987390683562043  
  Author: Devin Arizona 🇺🇲 (@DesertCrusade)  
  Timestamp: Sat, 14 Dec 2024 17:37:54 GMT  
  Engagement: Likes=21, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=1219  
  Media: Yes (photo: https://pbs.twimg.com/media/GexsEF-aoAEmKr5.jpg)  
  Content: Just got my tickets for AMFest by @TPUSA!! Sooo many awesome speakers including the man himself, President-Elect @realDonaldTrump!! This is going to be a LEGENDARY event! 🇺🇲🇺🇲🇺🇲🫡

- **[post:14]** ID: 1867987195782730077  
  Author: Jaguar Roper (@JaguarRoper)  
  Timestamp: Sat, 14 Dec 2024 17:37:07 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=35  
  Content: Trump Set To Speak At Turning Point’s AmericaFest In Phoenix – Arizona Daily Independent

### Posts from semantic search (Dec 9–15, 2024 focus):
- **[post:15]** ID: 1866997437925413057  
  Author: MAGA Voice (@MAGAVoice)  
  Timestamp: Thu, 12 Dec 2024 00:04:10 GMT  
  Engagement: Likes=537, Reposts=77, Quotes=4, Replies=25, Bookmarks=5, Views=15350  
  Media: Yes (photo: https://pbs.twimg.com/media/GejoRknaEAIADhV.jpg)  
  Content: BREAKING 🚨 Charlie Kirk announced President Trump will be speaking at TPUSA in Phoenix 🇺🇸 I PRAY TRUMP DOES MORE RALLIES LIKE THIS TRUMP IS A ROCKSTAR 🔥

- **[post:16]** ID: (empty/invalid)  
  (No text content)

- **[post:17]** ID: 1866217904707878919  
  Author: Hon.Moses Kuria,HSC (@HonMoses_Kuria)  
  Timestamp: Mon, 09 Dec 2024 20:26:35 GMT  
  Engagement: Likes=2158, Reposts=216, Quotes=47, Replies=420, Bookmarks=64, Views=250139  
  Content: 4pm tomorrow. Pen and notebook required. Plus lots of popcorn

- **[post:18]** ID: 1866157060074918140  
  Author: Sean Feucht (@seanfeucht)  
  Timestamp: Mon, 09 Dec 2024 16:24:49 GMT  
  Engagement: Likes=477, Reposts=129, Quotes=5, Replies=24, Bookmarks=13, Views=8921  
  Media: Yes (video: https://video.twimg.com/amplify_video/1866156977178742784/vid/avc1/720x1280/gRJYG7il7WPS9ahd.mp4?tag=16, duration: 25400 ms)  
  Content: Pray for the many Christian’s across Syria today. 🙏🏽🇸🇾 Join us THIS FRIDAY in Texas as we worship, pray and stand with the persecuted church for “PEACE ON EARTH.” Date: Friday December 13, 2024 Time: 7:30pm Location: Vintage Church 171 Farm to Market 3219, Harker Heights, TX

- **[post:19]** ID: 1867273333819232546  
  Author: Kirk Cameron (@KirkCameron)  
  Timestamp: Thu, 12 Dec 2024 18:20:29 GMT  
  Engagement: Likes=325, Reposts=49, Quotes=1, Replies=63, Bookmarks=5, Views=12415  
  Media: Yes (video: https://video.twimg.com/amplify_video/1867273270044540928/vid/avc1/1080x1920/UnCtNaQo5txPxFzC.mp4?tag=16, duration: 56189 ms)  
  Content: I’m going on tour this coming February! Join me and my friend @matthammitt for an inspiring night of prayer, worship, and insights from my new book Born To Be Brave! Get your tickets today at https://t.co/tKVnZn68SO

- **[post:20]** ID: 1866126271953912123  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 09 Dec 2024 14:22:28 GMT  
  Engagement: Likes=2518, Reposts=546, Quotes=40, Replies=249, Bookmarks=99, Views=484273  
  Media: Yes (photo: https://pbs.twimg.com/media/GeXN6F4XcAAoJJ7.jpg)  
  Content: 🚨🚨AMFEST 2024 is just 10 days away (!!). AmFest was already the largest multi-day event in the movement, but this year will be biggest event in Turning Point history. The fight to take our country back is just beginning. Join us 👉https://t.co/GQa2nEmNNm 🇺🇸🇺🇸

- **[post:21]** ID: 1867223944962716077  
  Author: Caleb Curtain (@CalebCurtain)  
  Timestamp: Thu, 12 Dec 2024 15:04:14 GMT  
  Engagement: Likes=209, Reposts=19, Quotes=6, Replies=32, Bookmarks=0, Views=27049  
  Content: Visits to East Carolina, Old Dominion and Tulsa set up for next week🙏🏾

- **[post:22]** ID: 1866167473705537605  
  Author: Jack Posobiec (@JackPosobiec)  
  Timestamp: Mon, 09 Dec 2024 17:06:12 GMT  
  Engagement: Likes=439, Reposts=22, Quotes=1, Replies=24, Bookmarks=3, Views=48286  
  Content: Coming up LIVE on the Charlie Kirk Show to discuss the ACQUITTAL of Daniel Penny in NYC

- **[post:23]** ID: 1866572042989936885  
  Author: David Archuleta (@DavidArchie)  
  Timestamp: Tue, 10 Dec 2024 19:53:48 GMT  
  Engagement: Likes=233, Reposts=18, Quotes=1, Replies=5, Bookmarks=4, Views=13845  
  Media: Yes (photo: https://pbs.twimg.com/media/GedlUAXW4AAu9Df.jpg)  
  Content: Miami! I'll see you at @Pridelines #UnMasking on December 14th. Grab your tickets now! https://t.co/2VsUUW0hKQ #Pridelines

### Additional keyword search results (Phoenix/AmFest focus):
- **[post:24]** ID: 1868040024031424672  
  Author: SilverbanglesAZ (@SilverBanglesAZ)  
  Timestamp: Sat, 14 Dec 2024 21:07:02 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=84  
  Content: He told Pete, “Katie Hobbs bought AmFest tickets to hear Trump speak” ..

- **[post:25]** ID: 1868009104616427917 (duplicate)  
  (Same as post:6/11 above; references Riley Gaines at AmFest)

- **[post:26]** ID: 1867987390683562043 (duplicate)  
  (Same as post:13 above)

- **[post:27]** ID: 1867987195782730077 (duplicate)  
  (Same as post:14 above)

- **[post:28]** ID: 1867915413738156432  
  Author: Knights Templar North America (@PaleRider47538)  
  Timestamp: Sat, 14 Dec 2024 12:51:53 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=42  
  Media: Yes (photo: https://pbs.twimg.com/media/GewrHGBXgAAtAsJ.jpg)  
  Content: The Biggest Conservative Movement in the Country...Turning Point’s annual event, AmericaFest, will be held December 19-22, 2024, at the Phoenix Convention Center with headliner PRESIDENT-ELECT DONALD J. TRUMP For more information, go here: https://t.co/OofTNrEhSy Those who attend this one-of-a-kind, four-day event will hear from dozens of the nation’s top leaders, network with thousands of like-minded attendees and 100+ partnering organizations, and experience concerts featuring top artists in the country- all while celebrating the greatest country in the world, America. Following a Turning Point event, these attendees return to their campuses and communities more energized than ever. #Follow Turning Point USA @TPUSA on twitter ("X")

- **[post:29]** ID: 1867880713615204562  
  Author: 𝙵𝚛𝚘𝚗𝚝 𝙿𝚊𝚐𝚎𝚜 𝚃𝚘𝚍𝚊𝚢 📰 (@ukpapers)  
  Timestamp: Sat, 14 Dec 2024 10:34:00 GMT  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=273  
  Media: Yes (photo: https://pbs.twimg.com/media/Gev3ErPWkAAAhKG.jpg)  
  Content: 🇺🇸 Trump To Speak At Conference In Phoenix ▫AmericaFest gathering draws Cruz, Kirk, other GOP loyalists ▫@stephanie_murr https://t.co/EpcyHam4VT👈 #frontpagestoday #USA @azcentral 🇺🇸

### Charlie Kirk's own posts (from:charliekirk11):
- **[post:30]** ID: 1866171403097297223  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Mon, 09 Dec 2024 17:21:48 GMT  
  Engagement: Likes=4811, Reposts=572, Quotes=128, Replies=1854, Bookmarks=94, Views=379492  
  Media: Yes (video: https://video.twimg.com/amplify_video/1866171291377471488/vid/avc1/640x344/MX8XEA4ugx8DLul0.mp4?tag=14, duration: 39489 ms)  
  Content: Jordan Neely's father, speaking after the verdict which found Daniel Penny NOT GUILTY: "I've had enough of this. The system is rigged. Come on people. Let's do something about this." Was he asking BLM to activate? If so, what does he want them to do?

- **[post:31]** ID: 1866126271953912123 (duplicate)  
  (Same as post:20 above; promotes AmFest 2024)

### TPUSA account search: No results found in the date range.

### Mar-a-Lago/award-related posts:
- **[post:32]** ID: 1868036548593365314 (duplicate)  
  (Same as post:3/9 above; Campus Warrior Award presentation by Charlie Kirk/TPUSA)

- **[post:33]** ID: 1867757820843896838  
  Author: C.A. Hartnell (@cahartnell)  
  Timestamp: Sat, 14 Dec 2024 02:25:40 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=148  
  Media: Yes (photo: https://pbs.twimg.com/media/Geub1kJbsAERxIP.jpg)  
  Content: Here I am inside the Mar a Lago #ballroom taking a pic in their gorgeous mirror with the gilt walls and a huge, sparkling chandelier. #Maralago #PalmBeach #mirror #TPUSAGala @tpusa #gala #fun

- **[post:34]** ID: 1867757491528118410  
  Author: C.A. Hartnell (@cahartnell)  
  Timestamp: Sat, 14 Dec 2024 02:24:21 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=124  
  Media: Yes (photo: https://pbs.twimg.com/media/GeubihWaIAAG32X.jpg)  
  Content: Got to visit Mar a Lago in Palm Beach, Florida, for a Turning Point USA Gala and fun, fabulous event! #Maralago #Florida #TPUSA #fun #PalmBeach @tpusa @charliekirk

- **[post:35]** ID: 1866917107113357816  
  Author: Richard Charles Wrecht (@DickCWrecht)  
  Timestamp: Wed, 11 Dec 2024 18:44:58 GMT  
  Engagement: Likes=3, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=115  
  Content: Can you believe as recently as last year this guy was a spiritual advisor to Charlie Kirk? Today, Charlie is in Mar a Lago, picking cabinet appointments. Lindsay is getting <10k impressions arguing with nitrous addicts on xitter. Schizophrenia comes at you fast.

- **[post:36]** ID: 1866902265287553079  
  Author: Charlie Kirk O.G. MAGA! (@El_Duderino_352)  
  Timestamp: Wed, 11 Dec 2024 17:46:00 GMT  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=14  
  Content: Watch: Mel Gibson Praises ‘Those Exposing All These Wolves in Sheep’s Clothing that Prey Upon Our Young’ in Powerful Mar-a-Lago Speech

**Note:** All data pulled directly from tool results. AmFest references consistently point to Dec 19–22, 2024 (outside this week’s range) in Phoenix with Trump, Charlie Kirk, and others speaking. Mar-a-Lago posts reference a recent/past weekend gala/award event. No other campus tours, rallies, or specific speaking stops by Charlie Kirk announced in the exact Dec 9–15 window.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-12-09 to 2024-12-15**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2024-12-09 to 2024-12-15 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
