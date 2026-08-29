---
unlisted: true
title: "Week 19 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W19"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-05-07 to 2023-05-13."
status: completed
hide_table_of_contents: true
---

# Week 19, 2023

- Date range: 2023-05-07 to 2023-05-13
- Queried at (UTC): 2026-08-24T19:07:18Z
- Model: grok-4.3
- API status: completed
- Response id: f23f59e0-a128-9a4a-a788-cd8e0cdd7640

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-05-07 to the end of the week 2023-05-13.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR campus OR \"public speaking\" OR appearance OR visit OR \"will be\" OR speaking OR \"speaking at\") since:2023-05-07 until:2023-05-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR tour OR \"speaking tour\" OR \"campus tour\") since:2023-05-07 until:2023-05-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, tours, or where he will speak between May 7 and May 13 2023",
      "limit": "10",
      "from_date": "2023-05-07",
      "to_date": "2023-05-13"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR \"will be\" OR appearance OR campus) since:2023-05-07 until:2023-05-14",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR campus OR \"public speaking\") since:2023-05-07 until:2023-05-14",
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
  "input_tokens": 10299,
  "input_tokens_details": {
    "cached_tokens": 3008
  },
  "output_tokens": 4631,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 14930,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 462928500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 5,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 8709,
    "output_tokens": 4326
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656822402179903488",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656822402179903488"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656724898838872065",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656724898838872065"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656832562348675073",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656832562348675073"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656654934698516483",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656654934698516483"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656041454144483329",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656041454144483329"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657134843845652480",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657134843845652480"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657123760787320834",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657123760787320834"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1655487760411791360",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1655487760411791360"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657126061396852752",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657126061396852752"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657072095870713871",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657072095870713871"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657128392079163393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657128392079163393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657132663101169666",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657132663101169666"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657125861144002565",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657125861144002565"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656673808441544705",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656673808441544705"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1655428322069827589",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1655428322069827589"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657064815234277376",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657064815234277376"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1655936984924442625",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1655936984924442625"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656162025465323527",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656162025465323527"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1655270727891681282",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1655270727891681282"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1657157263835136000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1657157263835136000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656077853233156097",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656077853233156097"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1656701832021024769",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1656701832021024769"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1655295845246418945",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1655295845246418945"
  }
]
```

## Grok response

```text
**Here is every relevant X post found from the specified searches (keyword and semantic) for the exact date range 2023-05-07 to 2023-05-13 (posts up to 2023-05-13 inclusive, matching the query's "end of the week 2023-05-13"). No summarization or filtering applied—full post content, metadata, and context included where available. Only posts mentioning Charlie Kirk, TPUSA/Turning Point USA, or related events/speaking appearances are retained.**

### Posts from advanced keyword searches ("Charlie Kirk" OR TPUSA OR "Turning Point USA" + event/speaking/tour terms, since:2023-05-07 until:2023-05-14, Latest mode):
- **[post:0]** ID: 1657157263835136000  
  Author: Jelerian (@Jelerien)  
  Timestamp: Fri, 12 May 2023 22:54:14 GMT  
  Content: "And if there weren't an issue why would schools have parents sign releases before allowing students to be photographed? This will be an expensive lesson to learn."  
  (No direct event mention; tangential reply context.)

- **[post:1]** ID: 1657134843845652480  
  Author: Elon's Dealer (@Elonlosthismind)  
  Timestamp: Fri, 12 May 2023 21:25:09 GMT  
  Content: "The event is at Trump's Doral Resort. Trump's lapdogs front and center. They are telling you who they are. Mike Flynn Charlie Kirk Mike Lindell Alex Jones RFK Jr Pete Navarro Kash Patel Ken Paxton Sidney Powell Lin Wood Roger Stone"

- **[post:2]** ID: 1657132663101169666  
  Author: Carnicero Grande (@BenFranklin001)  
  Timestamp: Fri, 12 May 2023 21:16:29 GMT  
  Content: "She's announcing it at a trans event. Look at the pic."

- **[post:3]** ID: 1657128392079163393  
  Author: Carnicero Grande (@BenFranklin001)  
  Timestamp: Fri, 12 May 2023 20:59:31 GMT  
  Content: "Women use the women's bathroom regardless of appearance. If it causes an issue, that's the fault of the woman wearing "man face". She should be more respectful."

- **[post:4]** ID: 1657126061396852752  
  Author: Reba Seaton (@rs2o2oViis00n)  
  Timestamp: Fri, 12 May 2023 20:50:15 GMT  
  Content: "And every time I speak with young people, I’m fired up to do even more to expose the Left’s toxic lies and to inspire the next generation to stand strong against “Woke” culture. Candace Owens YWLS Reba, that’s why I’m so excited to speak at Turning Point USA’s Young"

- **[post:5]** ID: 1657125861144002565  
  Author: Reba Seaton (@rs2o2oViis00n)  
  Timestamp: Fri, 12 May 2023 20:49:27 GMT  
  Content: "Turning Point USA I’ve traveled across the country with BLEXIT and Turning Point USA. I’ve met thousands of enthusiastic, America-loving young people – and thousands of angry, hateful Leftist protestors, too. And every time I speak with young"

- **[post:6]** ID: 1657123760787320834  
  Author: HerewardTheWake 🇺🇸 (@BCH1066)  
  Timestamp: Fri, 12 May 2023 20:41:07 GMT  
  Likes: 5, Reposts: 1, Replies: 2, Views: 161  
  Media: 1 photo (https://pbs.twimg.com/media/Fv9JRpbWwAAFWkc.jpg)  
  Content: "That’s pretty rich from a guy going on tour with Charlie Kirk and Mark Meadows."

### Additional keyword search results (tour/event-specific terms, since:2023-05-07 until:2023-05-14, Latest mode):
- **[post:7]** ID: 1657134843845652480 (duplicate of post:1)  
  Author: Elon's Dealer (@Elonlosthismind)  
  Timestamp: Fri, 12 May 2023 21:25:09 GMT  
  Content: "The event is at Trump's Doral Resort. Trump's lapdogs front and center. They are telling you who they are. Mike Flynn Charlie Kirk Mike Lindell Alex Jones RFK Jr Pete Navarro Kash Patel Ken Paxton Sidney Powell Lin Wood Roger Stone"

- **[post:8]** ID: 1657132663101169666 (duplicate of post:2)

- **[post:9]** ID: 1657123760787320834 (duplicate of post:6)

- **[post:10]** ID: 1657072095870713871  
  Author: Terri Green (@TerriGreenUSA)  
  Timestamp: Fri, 12 May 2023 17:15:49 GMT  
  Likes: 6, Reposts: 2, Replies: 2, Bookmarks: 2, Views: 1739  
  Media: 1 video (https://video.twimg.com/amplify_video/1657072028464054284/vid/720x1280/hD3Vn9sD37qEspyP.mp4?tag=14, duration: 96387 ms)  
  Content: "I just can’t with TPUSA faith. Watch the man get shaken. This is a political stunt wrapped up to look like a faith event. They say Indiana was able to experience our FIRST Let Us Worship with Kingdom to The Capitol INSIDE the Capitol!"

- **[post:11]** ID: 1657064815234277376  
  Author: Aundreya Schluessler (@aundreyasch1776)  
  Timestamp: Fri, 12 May 2023 16:46:53 GMT  
  Likes: 11, Reposts: 1, Replies: 0, Bookmarks: 0, Views: 202  
  Media: 2 photos (https://pbs.twimg.com/media/Fv8TqDAWABwm-nb.jpg and https://pbs.twimg.com/media/Fv8TqDMWAAEdwnS.jpg)  
  Content: "A great night this past Thursday at a collaborative event with some of the strongest parent groups in the state! The focus of the night was awareness for school choice! @TPUSA @tpusastudents"

- **[post:12]** ID: 1656832562348675073  
  Author: AirCondaTv (I am Charlie Kirk) 🇺🇸 (@AircondaTvT)  
  Timestamp: Fri, 12 May 2023 01:23:59 GMT  
  Likes: 3, Reposts: 0, Replies: 0, Bookmarks: 0, Views: 178  
  Media: 1 photo (https://pbs.twimg.com/media/Fv5AXBeWcAIvD__.jpg)  
  Content: "Holy crap! You telling me that I am actually #Live on time? Why yes, yes I am! Live on @rumblevideo playing #ARKSurvivalEvolved running my #MayThe4th event. We will continue to build our Prehistoric Galactic Empire & raising money for @StackUpDotOrg #CallToAmrs! Let's see if we can put more of a dent into their goal of $350K before the end of this month. #TheRegiment #GetWet #RumbleTakeover #RumbleGaming"

- **[post:13]** ID: 1656822402179903488  
  Author: Terri Green (@TerriGreenUSA)  
  Timestamp: Fri, 12 May 2023 00:43:37 GMT  
  Likes: 10, Reposts: 2, Replies: 5, Bookmarks: 0, Views: 2140  
  Media: 1 video (https://video.twimg.com/ext_tw_video/1656731178714398728/vid/1244x720/0bdmqpPtUfvvtU3v.mp4?tag=14, duration: 347835 ms)  
  Content: "No thanks. The re awaken tour that features Charlie Kirk and….well… the rest explains itself. Here’s the link. This is not parody. This is a circus, and republicans getting involved with it are on a slippery slope. https://t.co/77Jx76ClhX"

### Posts from semantic search (Charlie Kirk or TPUSA public speaking events/appearances/tours May 7-13 2023, limited to date range):
- **[post:14]** ID: 1656654934698516483  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 11 May 2023 13:38:10 GMT  
  Likes: 2031, Reposts: 470, Quotes: 31, Replies: 178, Bookmarks: 23, Views: 491025  
  Media: 3 photos (https://pbs.twimg.com/media/Fv2e4W3aMAA-ehj.jpg, https://pbs.twimg.com/media/Fv2e4W3aAAA62d9.jpg, https://pbs.twimg.com/media/Fv2e4XCaAAAL6js.jpg)  
  Content: "🚨🚨Introducing the ALL-NEW Turning Point Action Conference, ACTCON 2023, coming to West Palm Beach July 15-16. This will be the first multi-day event hosted, produced, and organized by TPUSA’s 501c4 sister organization @tpaction . Bongino, Bannon, Vance, Hawley, Poso, Benny, Gaetz, Vivek, Boebert, Harmeet, and MANY more major announcements coming soon, so stay tuned. Tickets available at"

- **[post:15]** ID: 1656077853233156097  
  Author: JennyCohn ✍🏻 📢 (@jennycohn1)  
  Timestamp: Tue, 09 May 2023 23:25:03 GMT  
  Likes: 205, Reposts: 115, Quotes: 46, Replies: 64, Bookmarks: 16, Views: 80623  
  Media: 1 photo (https://pbs.twimg.com/media/FvuSBuiaYAAzoGx.jpg)  
  Content: "Charlie Kirk of TPUSA is hosting a Pastors Summit. Mark Meadows (document burner/former Trump chief of staff) will speak, as will Eric Metaxas who emceed the 12/12/20 “Jericho March” where OathKeepers leader Stewart Rhodes & Mike Flynn spoke. h/t @mandersonville #Christofascism"

- **[post:16]** ID: 1656701832021024769  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 11 May 2023 16:44:31 GMT  
  Likes: 2252, Reposts: 398, Quotes: 6, Replies: 142, Bookmarks: 8, Views: 181367  
  Content: "BREAKING: Turning Point Action Conference—ACTCON 2023—to feature all-star line-up with: Bongino Vivek Ramaswamy Bannon Posobiec Gaetz Dhillon Boebert Benny Johnson Hawley Vance And MORE coming https://humanevents.com/2023/05/11/turning-point-action-conference-to-feature-all-star-line-up-with-jack-posobiec-charlie-kirk-steve-bannon-dan-bongino?utm_campaign=64501"

- **[post:17]** ID: 1656673808441544705  
  Author: Turning Point Action (@TPAction)  
  Timestamp: Thu, 11 May 2023 14:53:10 GMT  
  Likes: 1083, Reposts: 277, Quotes: 14, Replies: 47, Bookmarks: 4, Views: 57233  
  Media: 2 photos (https://pbs.twimg.com/media/Fv2v53JaEAAca09.jpg, https://pbs.twimg.com/media/Fv2v53SaIAURxAo.jpg)  
  Content: "Turning Point Action is ecstatic to be hosting its FIRST-EVER multi-day conference July 15 & 16 in West Palm Beach, FL! We’ll have the most BASED voices of the conservative movement that you won’t want to miss! ⬇️SPOTS ARE FILLING FAST!⬇️ Register NOW at https://t.co/r0aQDCp7NP"

- **[post:18]** ID: 1655428322069827589  
  Author: Sawyer Merritt (@SawyerMerritt)  
  Timestamp: Mon, 08 May 2023 04:24:03 GMT  
  Likes: 341, Reposts: 19, Quotes: 1, Replies: 7, Bookmarks: 1, Views: 31194  
  Content: "It is scheduled to start at 3:00pm in Robstown, just outside of Corpus Christi. The event will also include other local, state and federal leaders, according to a report by KIIITV."

- **[post:19]** ID: 1655270727891681282  
  Author: Freedom 🇺🇸🦅 (@PU28453638)  
  Timestamp: Sun, 07 May 2023 17:57:49 GMT  
  Likes: 446, Reposts: 176, Quotes: 6, Replies: 56, Bookmarks: 0, Views: 19825  
  Media: 4 photos (https://pbs.twimg.com/media/FviztN5XsAEw7Vr.jpg, https://pbs.twimg.com/media/FvizvnSXsAApTns.jpg, https://pbs.twimg.com/media/FvizvoEWAAEnq3g.jpg, https://pbs.twimg.com/media/Fvizvo2XsAI9745.jpg)  
  Content: "45th President of the United States Donald J. Trump will Hold a Rally in Des Moines Iowa, 🥳🥳🥳 Saturday May 13 7:PM CDT Retweet if you are Excited and are going to watch it."

- **[post:20]** ID: 1656724898838872065  
  Author: Alice Cooper (@alicecooper)  
  Timestamp: Thu, 11 May 2023 18:16:11 GMT  
  Likes: 681, Reposts: 65, Quotes: 6, Replies: 30, Bookmarks: 9, Views: 52039  
  Media: 1 video (https://video.twimg.com/ext_tw_video/1656724846879952896/pu/vid/720x1280/wDfbT-mV4kHPLPL-.mp4?tag=12, duration: 27900 ms)  
  Content: "What ya tryin' to do? Next Up: May 13 - Knoxville, TN May 14 - Spartanburg, SC May 15 - North Charleston, SC May 17 - Shreveport, LA May 18 - Biloxi, MS 🎟 https://t.co/8uJZpSQpcH 🎥 @merpus.perillo.13"

- **[post:21]** ID: 1655487760411791360  
  Author: Live Talks LA (@LiveTalksLA)  
  Timestamp: Mon, 08 May 2023 08:20:14 GMT  
  Likes: 198, Reposts: 19, Quotes: 3, Replies: 85, Bookmarks: 6, Views: 48130  
  Media: 3 photos (https://pbs.twimg.com/media/Fvl4DYGaMAAUHn8.jpg, https://pbs.twimg.com/media/Fvl4lt5aEAEU30V.jpg, https://pbs.twimg.com/media/Fvl4w0QagAAAyoY.jpg)  
  Content: ".@michiokaku Thanks for a great event on Friday. Thx @mcnallyterrence for interviewing. The virtual event airs May 10 at 6p PT/9pm ET and available on video-on-demand for five days. Tix include a signed book: https://t.co/SAMzAggvRT @doubledaybooks @penguinrandom"

- **[post:22]** ID: 1655936984924442625  
  Author: Bobby Weir (@BobWeir)  
  Timestamp: Tue, 09 May 2023 14:05:17 GMT  
  Likes: 508, Reposts: 30, Quotes: 4, Replies: 18, Bookmarks: 2, Views: 41270  
  Media: 1 photo (https://pbs.twimg.com/media/FvsR6LGaEAMa1Ea.jpg)  
  Content: "Mon. 5/8/23 Barton Hall, @Cornell University, Ithaca, NY Showtime: 733pm-11:40pm Next show: Fri. 5/19/23 LA Forum 📷: Matt Busch"

- **[post:23]** ID: 1655295845246418945  
  Author: General Mike Flynn (@GenFlynn)  
  Timestamp: Sun, 07 May 2023 19:37:38 GMT  
  Likes: 857, Reposts: 256, Quotes: 6, Replies: 46, Bookmarks: 1, Views: 86095  
  Content: "For those attending or planning on attending this upcoming weekend's Reawaken America event at the Trump Doral in Miami, Florida, in this short video we have updates on the schedule of events, parking, tickets (4 left as of this msg). And other significant speakers and singers! This RA Tour event is going to be amazing."

### Posts from from:charliekirk11 search (event/speaking terms, since:2023-05-07 until:2023-05-14, Latest mode):
- **[post:24]** ID: 1656654934698516483 (duplicate of post:14)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 11 May 2023 13:38:10 GMT  
  Content: (Full text identical to post:14 above)

- **[post:25]** ID: 1656162025465323527  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 10 May 2023 04:59:31 GMT  
  Likes: 19, Reposts: 0, Replies: 6, Bookmarks: 0, Views: 2204  
  Content: "No one company can or should do it alone. Creating a larger free speech ecosystem/alliance will be mutually beneficial, drawing in more users, more advertisers, more social and political influence."

### Posts from from:TPUSA search (event/speaking terms, since:2023-05-07 until:2023-05-14, Latest mode):
- **[post:26]** ID: 1656041454144483329  
  Author: Turning Point USA (@TPUSA)  
  Timestamp: Tue, 09 May 2023 21:00:25 GMT  
  Likes: 71, Reposts: 37, Quotes: 3, Replies: 2, Bookmarks: 0, Views: 9090  
  Media: 1 photo (https://pbs.twimg.com/media/FvtwEiKaQAA4kVr.jpg)  
  Content: "We’re excited to announce that @YeonmiParkNK will be speaking at #YWLS2023 this June in Dallas, TX! Head to https://t.co/86vbXokIfn to register for the country’s LARGEST conference for conservative women 🪩🎉"

**No other posts matched the exact criteria across all searches. No direct mentions of specific Charlie Kirk/TPUSA speaking events strictly within May 7-13, 2023 (most references are to upcoming July events, Reawaken America Tour, or past/past-tense tours). All raw data above is exhaustive from the tool results.**
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-05-07 to 2023-05-13**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2023-05-07 to 2023-05-13 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
