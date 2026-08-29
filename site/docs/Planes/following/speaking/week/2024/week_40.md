---
unlisted: true
title: "Week 40 2024 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2024-W40"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2024-09-30 to 2024-10-06."
status: completed
hide_table_of_contents: true
---

# Week 40, 2024

- Date range: 2024-09-30 to 2024-10-06
- Queried at (UTC): 2026-08-24T19:15:06Z
- Model: grok-4.3
- API status: completed
- Response id: 625e945e-63e4-9d41-9ab5-a69c39332cd3

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2024-09-30 to the end of the week 2024-10-06.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR campus OR speech) since:2024-09-30 until:2024-10-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR campus OR speech) since:2024-09-30 until:2024-10-07 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR campus OR speech) since:2024-09-30 until:2024-10-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR campus OR speech) since:2024-09-30 until:2024-10-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSAevents (event OR speaking OR speak OR tour OR \"will be\" OR appearing OR appearance OR campus OR speech) since:2024-09-30 until:2024-10-07",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, campus tours, or where Charlie will speak between September 30 and October 6 2024",
      "limit": "10",
      "from_date": "2024-09-30",
      "to_date": "2024-10-07"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\" OR \"Prove Me Wrong\" OR \"You're Being Brainwashed\" OR TPUSAstudents) (event OR speaking OR speak OR tour OR rally OR campus OR \"will be\" OR appearing OR appearance OR speech OR \"tabling\" OR \"voter registration\") since:2024-09-30 until:2024-10-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Montana OR Missoula OR \"University of Montana\" OR Reno OR \"Washoe\" OR UNR OR \"Grand Canyon University\" OR GCU OR Phoenix) since:2024-09-30 until:2024-10-07",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (Montana OR Missoula OR Reno OR Phoenix OR GCU OR \"Grand Canyon\" OR \"Prove Me Wrong\" OR event OR rally) since:2024-09-30 until:2024-10-07",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (Montana OR Missoula OR Reno OR Phoenix OR GCU OR \"Grand Canyon\" OR \"Prove Me Wrong\" OR event OR rally) since:2024-09-30 until:2024-10-07",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Save Big Sky Rally\" OR \"You're Being Brainwashed Tour\" since:2024-09-30 until:2024-10-07",
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
  "input_tokens": 31116,
  "input_tokens_details": {
    "cached_tokens": 14208
  },
  "output_tokens": 3587,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 34703,
  "num_sources_used": 0,
  "num_server_side_tools_used": 11,
  "cost_in_usd_ticks": 879441000,
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
    "input_tokens": 18334,
    "output_tokens": 2850
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842203554762957204",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842203554762957204"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841568559056429273",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841568559056429273"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842696353362944476",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842696353362944476"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842596190904566159",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842596190904566159"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842631221802570182",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842631221802570182"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842030568382595402",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842030568382595402"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842195058277200140",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842195058277200140"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841553758188179485",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841553758188179485"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841931441346888098",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841931441346888098"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842641052949205047",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842641052949205047"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842675993451856348",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842675993451856348"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841579963876835796",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841579963876835796"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842714710250270782",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842714710250270782"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841989276260827248",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841989276260827248"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1840786749741527494",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1840786749741527494"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842706434187747551",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842706434187747551"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842642454945890747",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842642454945890747"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841219057586225573",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841219057586225573"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841584715821941111",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841584715821941111"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842703445511508355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842703445511508355"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841967684462014739",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841967684462014739"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842652749034344931",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842652749034344931"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841939498906570828",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841939498906570828"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841832718583087423",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841832718583087423"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841991024371237052",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841991024371237052"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842046893360390423",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842046893360390423"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841928444755771550",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841928444755771550"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842327392867766345",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842327392867766345"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1840860247038071075",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1840860247038071075"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1840817185385824341",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1840817185385824341"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842649202708410846",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842649202708410846"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841581657410961790",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841581657410961790"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1840827660605477313",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1840827660605477313"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842692631807361365",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842692631807361365"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1840817167992045764",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1840817167992045764"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841961780228325832",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841961780228325832"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842710917471158578",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842710917471158578"
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
    "url": "https://x.com/i/status/1842714076235137194",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842714076235137194"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842692075634262480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842692075634262480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842714728604356796",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842714728604356796"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1841913397417513128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1841913397417513128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842615191789613545",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842615191789613545"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842058589877502175",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842058589877502175"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842675696465805365",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842675696465805365"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1842701930595803641",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1842701930595803641"
  }
]
```

## Grok response

```text
**All relevant X posts from the specified date range (2024-09-30 to 2024-10-06, interpreted as posts dated through 2024-10-06 with the `until:2024-10-07` cutoff for the end of the week) mentioning or related to Charlie Kirk or TPUSA public speaking events, campus appearances, tours, rallies, or where Charlie Kirk will speak.** 

I included **every matching post** returned by the searches (no summarization or filtering beyond relevance to events/speaking). Results focus on the query keywords and accounts. Many posts reference ongoing or recent TPUSA "You're Being Brainwashed Tour" stops, "Prove Me Wrong" tabling/speaking events, voter registration drives, and rallies. No results were found for some narrow account-specific searches (e.g., @TPUSAevents).

### Posts from searches (chronological by post ID/timestamp where possible; duplicates across calls removed):

- **[post:24] ID: 1841219057586225573** (Tue, 01 Oct 2024 20:50:06 GMT)  
  Author: Turning Point USA - @TPUSA  
  Content: A WIN FOR FREE SPEECH: A federal judge has issued a preliminary injunction against the University of New Mexico, preventing it from imposing security fees on the @tpusastudents chapter for an event featuring @Riley_Gaines_. The ruling responds to claims that the fees discriminated against conservative viewpoints.  
  (Mentions a TPUSA chapter event with Riley Gaines at University of New Mexico; media: photo.)

- **[post:23] ID: 1841219057586225573** (same as above; duplicate in results).

- **[post:56] ID: 1840817185385824341** (Mon, 30 Sep 2024 18:13:12 GMT)  
  Author: Turning Point USA - @TPUSA  
  Content: Charlie has ARRIVED at the University of Montana (with some members of the football team in tow) for another Prove Me Wrong tabling event 🔥  
  @charliekirk11 @tpusastudents  
  (Media: video of arrival for tabling/speaking event.)

- **[post:25] ID: 1840817185385824341** (same as above; duplicate in results).

- **[post:28] ID: 1840817167992045764** (Mon, 30 Sep 2024 18:13:08 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: See you today Montana!!  
  TPPAC and @tpaction are thrilled to be in Missoula with @SheehyforMT for our Save Big Sky Rally.  
  Join us today at 3:30pm MDT on campus at the University of Montana after our Prove Me Wrong event.  
  Tickets 👉 https://t.co/xPdvvp1ev8  
  (Media: photo.)

- **[post:33] ID: 1840827660605477313** (Mon, 30 Sep 2024 18:54:49 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: University of Montana we see you!!  
  MASSIVE crowd in Big Sky Country for our Prove Me Wrong event. Thousands have turned out ahead of our rally later today with the next US Senator from the great state of Montana, @SheehyforMT!!  
  Let's go!! 🇺🇸🇺🇸  
  (Media: 4 videos.)

- **[post:29] ID: 1840860247038071075** (Mon, 30 Sep 2024 21:04:19 GMT)  
  Author: NBC Montana - @NBCMontana  
  Content: Save Big Sky Rally with Charlie Kirk held at University of Montana ahead of Tester, Sheehy debate  
  (Media: video.)

- **[post:48] ID: 1841939498906570828** (Thu, 03 Oct 2024 20:32:52 GMT)  
  Author: H P - @Gchef57  
  Content: Conservative activist Charlie Kirk holds rally for Tim Sheehy in Missoula https://montanafreepress.org/2024/09/30/conservative-activist-charlie-kirk-holds-rally-for-sheehy-in-missoula-ahead-of-debate-with-tester/ via @MTFreePress  
  Charlie K and T Shithead are lying pukes, along with C Jacobsen. Wake up you little hillbilly asswipes !!  
  (References the Missoula rally event.)

- **[post:61] ID: 1841553758188179485** (Wed, 02 Oct 2024 19:00:05 GMT)  
  Author: Montana Kaimin - @MontanaKaimin  
  Content: “Save Big Sky Rally,” brings Republican Tim Sheehy to the University of Montana with Charlie Kirk to push the Republican vote.  
  Story by Emily Messer  
  Photo by Aiden Havens  
  #MontanaSenate #Sheehy #PoliticsOnCampus  
  Read here: https://t.co/6NcouvLIMm  
  (Media: photo; references the rally.)

- **[post:54] ID: 1841568559056429273** (Wed, 02 Oct 2024 19:58:53 GMT)  
  Author: Turning Point USA - @TPUSA  
  Content: Current scene at Grand Canyon University, where we are hosting our Voter Registration Drive with @charliekirk11 🇺🇸  
  @tpusastudents  
  (Media: photo of the event.)

- **[post:53] ID: 1841579963876835796** (Wed, 02 Oct 2024 20:44:12 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: 🚨Hosted another MASSIVE Voter Registration event at Grand Canyon University in Phoenix!  
  Kids are climbing up trees and hanging from sign posts to be a part of it. Unreal energy!!  
  + 500 NEW GEN Z VOTERS... and the team is still going.  
  This is how we win. 🇺🇸🇺🇸  
  (Media: 4 videos.)

- **[post:52] ID: 1841584715821941111** (Wed, 02 Oct 2024 21:03:05 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: Amazing event.  
  (Reply/contextual to the GCU event.)

- **[post:21] ID: 1841581657410961790** (Wed, 02 Oct 2024 20:50:56 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: Campus energy has shifted.  
  (Contextual to recent campus events.)

- **[post:20] ID: 1841584715821941111** (same as [post:52]; duplicate).

- **[post:46] ID: 1841967684462014739** (Thu, 03 Oct 2024 22:24:52 GMT)  
  Author: Kylie Johnson - @Kylovesamerica  
  Content: Just a recap from the brainwashed tour stop at University of Montana!! Featuring my students from the Teton County activism hub! 🇺🇸  
  @tpaction @TPUSA @tpusastudents  
  (Media: 3 photos.)

- **[post:59] ID: 1841913397417513128** (Thu, 03 Oct 2024 18:49:09 GMT)  
  Author: Rachel Farmer - @rachelfarm04  
  Content: 🚨CHAPEL HILL🚨  
  Don’t miss @charliekirk11 & @VivekGRamaswamy at UNC this October for @TPUSA’s You’re Being Brainwashed Tour! 📺🌀  
  GET YOUR TICKETS ➡️ https://theturningpointtour.com/  
  See YOU there‼️  
  (Media: photo; announces upcoming UNC event.)

- **[post:60] ID: 1841832718583087423** (Thu, 03 Oct 2024 13:28:34 GMT)  
  Author: Shannon Stover - @sstover_  
  Content: SO EXCITED to have @VivekGRamaswamy at Penn State University on 10/17!! ⚡️💥  
  You’re Being Brainwashed Tour Part 3 in Steel😵‍💫🤩  
  @TPUSA | @tpusastudents |@TpusaGreatLakes  
  (Media: photo; announces upcoming Penn State event with Vivek.)

- **[post:42] ID: 1842327392867766345** (Fri, 04 Oct 2024 22:14:13 GMT)  
  Author: Schayden Gorai - @schaykg  
  Content: Made a pit stop in Missoula Montana to help register voters at the @TPUSA “You’re being brainwashed tour” with @charliekirk11 and @SheehyforMT  
  We registered triple digits for New Gen-Z Voters on campus!  
  Gen-Z can change the tide of this election! Let’s make it happen!  
  (Media: 4 photos.)

- **[post:43] ID: 1842046893360390423** (Fri, 04 Oct 2024 03:39:37 GMT)  
  Author: dazzle - @dazzlingmuses  
  Content: Here's an interview he did with Charlie kirk in front of a live audience in Missoula  
  https://rumble.com/v5gy7yl-turning-point-action-presents-the-save-big-sky-rally-live-with-charlie-kirk.html  
  (References the Missoula rally/interview.)

- **[post:57] ID: 1842641052949205047** (Sat, 05 Oct 2024 19:00:36 GMT)  
  Author: Washoe County Republican Party - @RealWashoeGOP  
  Content: Save the Date! Turning Point USA's YOU'RE BEING BRAINWASHED TOUR is coming to Reno!  
  Grab your seat now!  
  #TurningPointUSA #WashoeGOP #UNR #MAGA  
  (Media: photo; promotes upcoming Reno tour stop.)

- **[post:13] ID: 1842641052949205047** (same as above; duplicate).

- **[post:9] ID: 1842675696465805365** (Sat, 05 Oct 2024 21:18:15 GMT)  
  Author: Stephen Twomey Jr - @TwomeyJr  
  Content: Charlie Kirk DARES College Student to Be More Prepared Next Time 👀 - YouTube is it amazing how all these people complain about him being on their campus but running around with Jew hating signs is OK https://www.youtube.com/shorts/qu6lGnCa2Og  
  (Mentions Charlie Kirk on campus; video link.)

- **[post:6] ID: 1842675696465805365** (same as above; duplicate).

- **[post:34] ID: 1842596190904566159** (Sat, 05 Oct 2024 16:02:20 GMT)  
  Author: Charlie Kirk - @charliekirk11  
  Content: Check out this 🧵laying out some of our efforts at @tpaction this cycle.  
  Hundreds of full-time staff + thousands of volunteers blanketing the key states of WI and AZ (as well as MI-7, NV-3) through our Chase the Vote project.  
  We also have teams in PA, GA, NC, FL, and IA.  
  Hosting dozens of events, five Trump rallies, a JD Vance town hall, MAHA events, massive voter registrations drives at campuses across the country and more.  
  We're sprinting through the finish line.  
  Let's win 🇺🇸🇺🇸  
  (Mentions dozens of TPUSA/TPAction events, voter registration drives at campuses, and Trump rallies; no specific dates/locations in this post.)

- Other posts in results (e.g., [post:0]–[post:22], [post:26]–[post:27], [post:30]–[post:32], [post:35]–[post:41], [post:44]–[post:45], [post:47], [post:49]–[post:51], [post:55], [post:58]) were either off-topic (Trump rallies, general commentary, unrelated tours like Korn), not directly about Charlie Kirk/TPUSA speaking events in the date range, or duplicates. No additional event-specific posts matched the exact criteria.

**Notes on data:**  
- Key events referenced in range: University of Montana (Prove Me Wrong tabling + Save Big Sky Rally with Tim Sheehy on/around Sept 30), Grand Canyon University/Phoenix (voter registration drive on/around Oct 2).  
- Upcoming/promoted: Reno (You're Being Brainwashed Tour), UNC Chapel Hill (with Vivek Ramaswamy), Penn State (with Vivek).  
- All content is directly from the tool results. No external links or media were altered. If more posts exist beyond the tool limits, they were not returned in these searches.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2024-09-30 to 2024-10-06**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event** — the **1** most significant of **2** this page touches, foreign-fleet and same-day first, then most recent. The full set is on [the contacts index](/Planes/Incidents/overview) and on each aircraft's own page.

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2024-09-30](/Planes/Incidents/N582MM-2024-09-30-KMSO) | [N582MM](/Planes/N582MM/overview) | [KMSO](/Planes/Airports/KMSO) | Missoula, MT | Charlie | **Same day** |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
