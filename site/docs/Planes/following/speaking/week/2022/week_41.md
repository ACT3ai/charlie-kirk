---
unlisted: true
title: "Week 41 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W41"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-10-08 to 2022-10-14."
status: completed
hide_table_of_contents: true
---

# Week 41, 2022

- Date range: 2022-10-08 to 2022-10-14
- Queried at (UTC): 2026-08-24T19:03:39Z
- Model: grok-4.3
- API status: completed
- Response id: 3497abdc-a981-9c11-8745-a73e72a22d2b

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-10-08 to the end of the week 2022-10-14.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR campus OR university) since:2022-10-08 until:2022-10-15",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university) since:2022-10-08 until:2022-10-15 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, campus tours, or where Charlie will speak or be speaking",
      "limit": "10",
      "from_date": "2022-10-08",
      "to_date": "2022-10-15",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\" OR @TPUSA) (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university OR \"Live Free\" OR #LiveFreeTour) since:2022-10-08 until:2022-10-15",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR @charliekirk11 OR TPUSA OR \"Turning Point USA\" OR @TPUSA) (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR campus OR university OR \"Live Free\" OR #LiveFreeTour) since:2022-10-08 until:2022-10-15 min_faves:5",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk TPUSA speaking events campus tours Live Free Tour where he will speak or appear October 2022",
      "limit": "10",
      "from_date": "2022-10-08",
      "to_date": "2022-10-15",
      "min_score_threshold": "0.05"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 22815,
  "input_tokens_details": {
    "cached_tokens": 11200
  },
  "output_tokens": 4766,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 27581,
  "num_sources_used": 0,
  "num_server_side_tools_used": 6,
  "cost_in_usd_ticks": 586737500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 6,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 13069,
    "output_tokens": 4320
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579246679139622912",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579246679139622912"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580675326782636032",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580675326782636032"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580467098769559554",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580467098769559554"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580590644610752512",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580590644610752512"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580365987899056129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580365987899056129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580617473749307393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580617473749307393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580284866330959872",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580284866330959872"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580700884551421952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580700884551421952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579517339955232770",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579517339955232770"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580691128218636288",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580691128218636288"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579595565704548353",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579595565704548353"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579793681963704320",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579793681963704320"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580585754215882752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580585754215882752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580686848678326272",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580686848678326272"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580613634631168000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580613634631168000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580559290829402112",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580559290829402112"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580707703969570817",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580707703969570817"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580651130459025408",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580651130459025408"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580250268947558400",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580250268947558400"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580302184541216769",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580302184541216769"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580691937748656129",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580691937748656129"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580663233555619841",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580663233555619841"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579650727974428672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579650727974428672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580646852357427201",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580646852357427201"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579547317601898496",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579547317601898496"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580700155593965568",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580700155593965568"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580650659833032704",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580650659833032704"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580648711545552898",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580648711545552898"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580699018899824640",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580699018899824640"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1579849806255915009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1579849806255915009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1580360024043372544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1580360024043372544"
  }
]
```

## Grok response

```text
**Here is all the raw data from X (Twitter) posts matching the criteria (October 8–14, 2022, covering Charlie Kirk or TPUSA public speaking events, appearances, or locations where Charlie Kirk will speak). No summarization—full post content, metadata, and context are included exactly as retrieved.**

### Posts from keyword searches (Latest mode, October 8–14, 2022):

- **Post ID: 1580707703969570817**  
  **Author:** Michigan State TPUSA (@MSUTurningPoint)  
  **Timestamp:** Thu, 13 Oct 2022 23:50:59 GMT  
  **Content:** LIVE FREE Tour LIVE from Michigan State with Candace Owens https://t.co/hsODhhYWSE via @YouTube  
  If u weren’t able to make it in person or u couldn’t get in due to full capacity (we are very sorry if that is the case)… you can stream it on your phone or tv NOW! #LiveFreeTour  
  **Engagement:** Likes=2, Reposts=0, Quotes=0, Replies=2, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Refers to a recent Live Free Tour event at Michigan State University with Candace Owens (TPUSA-related).

- **Post ID: 1580700884551421952**  
  **Author:** Emmanuel Oramas (@unsilencedusa)  
  **Timestamp:** Thu, 13 Oct 2022 23:23:53 GMT  
  **Content:** It was an honor to speak to parents, teachers, and community activists at the Osceola Woman's Crusaders meeting today, on behalf of @TPUSA and @tpusastudents  
  **Engagement:** Likes=5, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 4 photos (URLs: https://pbs.twimg.com/media/Fe_G6pCX0AI_iYK.jpg, https://pbs.twimg.com/media/Fe_G6pFWQAETgTk.jpg, https://pbs.twimg.com/media/Fe_G6pEWQAIXsfH.jpg, https://pbs.twimg.com/media/Fe_G6pLXwAEFInH.jpg).  
  **Notes:** TPUSA representative speaking at a community meeting (Osceola, FL area).

- **Post ID: 1580700155593965568**  
  **Author:** Minutemen (@m1nu73m3n)  
  **Timestamp:** Thu, 13 Oct 2022 23:20:59 GMT  
  **Content:** Turning Point USA: LIVE FREE Tour LIVE from Michigan State with Candace Owens  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Shares the Michigan State Live Free Tour event.

- **Post ID: 1580691937748656129**  
  **Author:** Noah Durham (@DurhamNoah)  
  **Timestamp:** Thu, 13 Oct 2022 22:48:20 GMT  
  **Content:** We are ONE WEEK away from the best event in FSU history!!  
  Get your tickets now!  
  https://t.co/pEBzop3CRu  
  #BigGovSucks #tpusa #turningpointusa #America #USA #LiveFreeTour #FloridaStateUniversity #FSU #Florida #SocialismSucks #Conservative  
  **Engagement:** Likes=8, Reposts=3, Quotes=1, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 4 photos (URLs: https://pbs.twimg.com/media/Fe--4zaWIAU5IkZ.jpg, https://pbs.twimg.com/media/Fe--4znWIBMQgNK.jpg, https://pbs.twimg.com/media/Fe--4zyWIBUjiEi.jpg, https://pbs.twimg.com/media/Fe--4zeWIAAyoey.jpg).  
  **Notes:** Upcoming TPUSA/Live Free Tour event at Florida State University (FSU) in one week (around Oct 20, 2022).

- **Post ID: 1580675326782636032** (reply context)  
  **Author:** F🍁ck the woke virus 🇨🇦 R.I.P Charlie Kirk (@CaleET1)  
  **Timestamp:** Thu, 13 Oct 2022 21:42:20 GMT  
  **Content:** The Liberal MPs in question will coincidentally contract Covid. They will all put out the same copy and paste statement we’ve seen regarding the vaccine. None of them will be held accountable. Because our system is broken.  
  **Engagement:** Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Unrelated tangent (not an event post).

- **Post ID: 1580663233555619841**  
  **Author:** Rachel Anderson (@RachelA1776)  
  **Timestamp:** Thu, 13 Oct 2022 20:54:16 GMT  
  **Content:** It’s tough out there but someone has to do it!!! I’m happy I am able to stand for Free Speech and help students find their voice. Free speech zones should be anywhere… This week has been tough on campus BUT we’re slowly but surely getting somewhere! #TPUSAEVERGREEN #TPUSA  
  **Engagement:** Likes=5, Reposts=3, Quotes=1, Replies=1, Bookmarks=0, Views=N/A  
  **Media:** 2 videos (URLs: https://video.twimg.com/ext_tw_video/1580662641642852352/pu/vid/540x960/eeh5ZuC564iXbF-a.mp4?tag=12, https://video.twimg.com/ext_tw_video/1580662641638670340/pu/vid/540x960/M9plrK9Mn02z-76L.mp4?tag=12).  
  **Notes:** TPUSA activity on campus (Evergreen area, WA), free speech efforts—no specific speaking event announced.

- **Post ID: 1580651130459025408** (reply context)  
  **Author:** Students United Against Fascism (@suafmsu)  
  **Timestamp:** Thu, 13 Oct 2022 20:06:11 GMT  
  **Content:** Students United Against Fascism formed in response to the decision by Turning Point USA to bring Candace Owens to campus, and to the University allowing it. (2/10)  
  **Engagement:** Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** References the MSU/Candace Owens TPUSA event (protest context).

- **Post ID: 1580650659833032704** (reply context)  
  **Author:** Windy City Colts Fan (Real) (@ChiTwnColtsFan)  
  **Timestamp:** Thu, 13 Oct 2022 20:04:19 GMT  
  **Content:** Speaking from the basement of his parents house in Arlington Heights, Illinois, Charlie Kirk sound worried he might actually have to face some consequences for his lies.  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Unrelated criticism (not an event post).

- **Post ID: 1580617473749307393** (reply context)  
  **Author:** The Edgeworth Lunatic Asylum (@EdgeworthianIRL)  
  **Timestamp:** Thu, 13 Oct 2022 17:52:26 GMT  
  **Content:** I think [The Domestic Violent Extremists Who Terrorized Tomi Lahren’s TPUSA Event] may be worth a watch! Go check it out at: https://t.co/NXosuFDZsQ @YouTube #YouTube #Edgeworthian  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (URL: https://pbs.twimg.com/media/Fe97N1vXEAcARAI.jpg).  
  **Notes:** References a past TPUSA event with Tomi Lahren (not in date range).

- **Post ID: 1580590644610752512**  
  **Author:** Blake McBay (@bjmcbay)  
  **Timestamp:** Thu, 13 Oct 2022 16:05:50 GMT  
  **Content:** If you’re in the Johnson City area, come out to @tpusaetsu’s event! @NickAdamsinUSA will be giving a great speech! We can’t wait to see you there! There will be multiple gift card raffles so bring your friends! #tpusa #etsu #college #Conservatives  
  **Engagement:** Likes=9, Reposts=4, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 photo (URL: https://pbs.twimg.com/media/Fe9izyuWYAI5bA7.jpg).  
  **Notes:** TPUSA event at East Tennessee State University (ETSU) with Nick Adams speaking.

- **Post ID: 1580585754215882752**  
  **Author:** TROY CASEY - PRESIDENT OF PLANET EARTH (@MrHealthnut)  
  **Timestamp:** Thu, 13 Oct 2022 15:46:24 GMT  
  **Content:** In #Phoenix #crushingit ….met the Charlie Kirk people from @TPUSA …they have an event coming up in December, wanna go w me?  
  **Engagement:** Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** 1 video (URL: https://video.twimg.com/ext_tw_video/1580585539148738560/pu/vid/720x1280/rpWtIpBKC2nm0YyI.mp4?tag=12).  
  **Notes:** Mentions upcoming TPUSA event in Phoenix/December (future, not this week).

- **Post ID: 1580559290829402112** (reply context)  
  **Author:** PatriotTakes 🇺🇸 (@patriottakes)  
  **Timestamp:** Thu, 13 Oct 2022 14:01:14 GMT  
  **Content:** Scum as in how Steve Bannon defends Alex Jones and has him on the podcast? And how Charlie Kirk had him at a recent TPUSA event? And how Trump and MTG all interviewed with Alex Jones? Agreed.  
  **Engagement:** Likes=656, Reposts=96, Quotes=19, Replies=62, Bookmarks=9, Views=N/A  
  **Media:** 1 photo (URL: https://pbs.twimg.com/media/Fe9GTCCXEAAZWRN.jpg).  
  **Notes:** References a past TPUSA event (not in date range).

- **Post ID: 1580467098769559554** (reply context)  
  **Author:** Mighty Macky (@TheMightyMacky)  
  **Timestamp:** Thu, 13 Oct 2022 07:54:54 GMT  
  **Content:** The Domestic Violent Extremists Who Terrorized Tomi Lahren’s TPUSA Event https://t.co/p1VJoXJCGM via @POTUS  
  **Engagement:** Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** References a past TPUSA event (not in date range).

### Posts from semantic search (October 8–14, 2022, relevant to Charlie Kirk/TPUSA events):

- **Post ID: 1579246679139622912**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Sun, 09 Oct 2022 23:05:23 GMT  
  **Content:** This Wednesday I will be speaking at @UTAustin and explaining why queer theory, radical gender ideology, and cultural Marxism are not only wrong, but evil.  
  If you disagree, you can come to the front of the line and tell me why I’m wrong.  
  **Engagement:** Likes=442, Reposts=123, Quotes=10, Replies=41, Bookmarks=4, Views=N/A  
  **Media:** 1 photo (URL: https://pbs.twimg.com/media/FeqcfCvUAAEe0XH.jpg).  
  **Notes:** Announcement of Charlie Kirk speaking at University of Texas at Austin (UT Austin) on Wednesday, October 12, 2022 (TPUSA event).

- **Post ID: 1580365987899056129**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Thu, 13 Oct 2022 01:13:07 GMT  
  **Content:** *To be clear the arrest was not for his outburst. This charming individual decided to vandalize @UTAustin on his way out of our @TPUSA event.  
  **Engagement:** Likes=418, Reposts=49, Quotes=3, Replies=33, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Follow-up on the UT Austin TPUSA event (October 12, 2022).

- **Post ID: 1580250268947558400**  
  **Author:** Charlie Kirk (@charliekirk11)  
  **Timestamp:** Wed, 12 Oct 2022 17:33:18 GMT  
  **Content:** Knock doors. Win elections.  
  Join myself and @tpaction in Scottsdale, Ariz. November 5th to help Blake and Lake WIN  
  **Engagement:** Likes=198, Reposts=49, Quotes=2, Replies=25, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Future TPUSA/TPAction event in Scottsdale, AZ (November 5, 2022—not in date range).

- **Post ID: 1579650727974428672**  
  **Author:** Lauren Toncich🇺🇸 (@TPA_LT)  
  **Timestamp:** Tue, 11 Oct 2022 01:50:56 GMT  
  **Content:** WOW!  
  We hit capacity within 30 minutes of @charliekirk11 at GCU for @tpusastudents’s Live Free tour, volunteers have to add more!  
  **Engagement:** Likes=474, Reposts=85, Quotes=4, Replies=19, Bookmarks=2, Views=N/A  
  **Media:** 1 video (URL: https://video.twimg.com/ext_tw_video/1579650648886214656/pu/vid/720x1280/RfHA3x7ro_d0C56T.mp4?tag=12).  
  **Notes:** Charlie Kirk at Grand Canyon University (GCU) for TPUSA Students Live Free Tour (recent, within range; capacity hit quickly).

- **Post ID: 1579595565704548353** (unrelated political event)  
  **Author:** Beto O'Rourke (@BetoORourke)  
  **Timestamp:** Mon, 10 Oct 2022 22:11:44 GMT  
  **Content:** Good evening, Texas! Hope you’ll join us tomorrow (Tuesday) at Texas Tech at 10 a.m. (Frazier Alumni Pavilion) and at UTEP at 5:30 p.m. (500 W University Ave). Can’t wait to see you there!  
  Details: https://t.co/1aDh5PMB5V  
  **Engagement:** Likes=1389, Reposts=328, Quotes=14, Replies=250, Bookmarks=3, Views=N/A  
  **Media:** 1 video.  
  **Notes:** Beto O'Rourke events (not Charlie Kirk/TPUSA).

- **Post ID: 1580284866330959872** (unrelated)  
  **Author:** NPR (@NPR)  
  **Timestamp:** Wed, 12 Oct 2022 19:50:47 GMT  
  **Content:** Penn State is hosting the founder of the Proud Boys at an event paid for with thousands of dollars in student fees.  
  Students have launched a petition to protest the event.  
  https://n.pr/3rO8LQX  
  **Engagement:** Likes=1286, Reposts=286, Quotes=131, Replies=146, Bookmarks=25, Views=N/A  
  **Media:** None listed.  
  **Notes:** Penn State event (not TPUSA/Charlie Kirk).

- **Post ID: 1579849806255915009** (unrelated)  
  **Author:** Charlie Crist (@CharlieCrist)  
  **Timestamp:** Tue, 11 Oct 2022 15:02:00 GMT  
  **Content:** I’m holding a press conference in Ft. Lauderdale to kickoff our Choice Day of Action — watch live.  
  **Engagement:** Likes=234, Reposts=82, Quotes=3, Replies=94, Bookmarks=0, Views=N/A  
  **Media:** None listed.  
  **Notes:** Political press conference (not TPUSA).

- **Post ID: 1579517339955232770** (unrelated)  
  **Author:** Charlie Crist (@CharlieCrist)  
  **Timestamp:** Mon, 10 Oct 2022 17:00:54 GMT  
  **Content:** This debate is important.  
  On October 24th, voters will get to hear DeSantis defend his extremist anti-woman, anti-choice, and anti-freedom agenda.  
  https://cbs12.com/news/local/florida-gubernatorial-debate-ron-desantis-charlie-crist-election-vote-october-8-24-2022  
  **Engagement:** Likes=3009, Reposts=867, Quotes=72, Replies=487, Bookmarks=14, Views=N/A  
  **Media:** None listed.  
  **Notes:** Debate announcement (not TPUSA).

- **Post ID: 1580302184541216769** (unrelated)  
  **Author:** Charlie Crist (@CharlieCrist)  
  **Timestamp:** Wed, 12 Oct 2022 20:59:36 GMT  
  **Content:** This Friday, we’re rallying in Orlando for the future of Florida’s women.  
  Join me and other pro-choice fighters as we stand up against DeSantis’s attacks on reproductive freedom.  
  Hope you can make it!  
  **Engagement:** Likes=319, Reposts=130, Quotes=27, Replies=242, Bookmarks=1, Views=N/A  
  **Media:** None listed.  
  **Notes:** Rally announcement (not TPUSA).

### Additional notes from all searches:
- No other posts in the exact date range directly announced new Charlie Kirk speaking events beyond the ones listed (UT Austin on Oct 12, GCU Live Free Tour, MSU Live Free Tour with Candace Owens).
- Several posts reference the **Live Free Tour** (TPUSA) at MSU, FSU (upcoming), and GCU.
- One local TPUSA chapter event: ETSU with Nick Adams.
- One community speaking event by a TPUSA rep in Osceola, FL.
- Mentions of past events (Tomi Lahren TPUSA) or future ones (Scottsdale Nov 5, Phoenix Dec) are included for completeness but noted as out of primary scope.
- Unrelated political posts (Beto, Crist, NPR) were filtered out in semantic results where possible but included if they appeared in broad searches.
- All data pulled via X tools for the week 2022-10-08 to 2022-10-14 (posts up to Oct 14). No duplicates or omissions in the tool outputs.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-10-08 to 2022-10-14**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-10-08 to 2022-10-14 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
