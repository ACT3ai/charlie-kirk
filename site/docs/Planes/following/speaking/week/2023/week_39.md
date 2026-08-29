---
unlisted: true
title: "Week 39 2023 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2023-W39"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2023-09-24 to 2023-09-30."
status: completed
hide_table_of_contents: true
---

# Week 39, 2023

- Date range: 2023-09-24 to 2023-09-30
- Queried at (UTC): 2026-08-24T19:09:09Z
- Model: grok-4.3
- API status: completed
- Response id: 99d44ff3-d2f6-9e11-a13f-701b6680174c

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2023-09-24 to the end of the week 2023-09-30.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR speaks) since:2023-09-24 until:2023-09-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR speaks) since:2023-09-24 until:2023-09-30",
      "limit": "10",
      "mode": "Top"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between September 24-30 2023",
      "limit": "10",
      "from_date": "2023-09-24",
      "to_date": "2023-09-30",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR speaking OR speak OR tour OR appearance OR campus OR \"will be\" OR speaking) since:2023-09-24 until:2023-09-30",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (event OR speaking OR speak OR tour OR appearance OR campus OR \"will be\" OR speaking) since:2023-09-24 until:2023-09-30",
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
  "input_tokens": 11169,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 5232,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 16401,
  "num_sources_used": 0,
  "num_server_side_tools_used": 5,
  "cost_in_usd_ticks": 488156500,
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
    "input_tokens": 9579,
    "output_tokens": 4917
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706486711864131923",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706486711864131923"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706405375249973344",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706405375249973344"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707123078009155615",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707123078009155615"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707473755365339162",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707473755365339162"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707575898575446463",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707575898575446463"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1705939501455901000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1705939501455901000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707096823138054467",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707096823138054467"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706051166969180473",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706051166969180473"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707843551957025222",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707843551957025222"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707462817056424173",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707462817056424173"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707867523155452275",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707867523155452275"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706768003776626792",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706768003776626792"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707496948175941784",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707496948175941784"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1705794605097078924",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1705794605097078924"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707830198408982687",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707830198408982687"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707864366207389926",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707864366207389926"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706425437830689108",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706425437830689108"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707812812033241505",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707812812033241505"
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
    "url": "https://x.com/i/status/1706718203701850197",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706718203701850197"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707900871617728586",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707900871617728586"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707879229130490146",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707879229130490146"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706708076231794816",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706708076231794816"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707217699552588238",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707217699552588238"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1706465390182941059",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1706465390182941059"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707863715465273813",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707863715465273813"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707142503198081263",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707142503198081263"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1707445466802319562",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1707445466802319562"
  }
]
```

## Grok response

```text
**Here is all the relevant X/Twitter post data from the specified date range (2023-09-24 to 2023-09-30) matching the search criteria for Charlie Kirk or TPUSA public speaking events/appearances.** I have included every post returned across the searches (keyword "Latest", keyword "Top", semantic, and official accounts) without summarization, filtering, or omission. Posts are presented with their full available metadata as returned by the tools. No posts were found from @TPUSA in the date range.

### From x_keyword_search (Latest mode, general query):
- **Post ID: 1707900871617728586**  
  Author: JSONOFGOD (@USStallion)  
  Timestamp: Fri, 29 Sep 2023 23:31:13 GMT  
  Content: Keep speaking Charlie!  
  Engagement: Likes=1, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=45

- **Post ID: 1707879229130490146**  
  Author: Jeff M Richter (@JeffMRichter2)  
  Timestamp: Fri, 29 Sep 2023 22:05:13 GMT  
  Content: Charlie Kirk calls for Arizona lawmakers to defund state universities at ASU event  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=10

- **Post ID: 1707864366207389926**  
  Author: Pete M (@Peter34652)  
  Timestamp: Fri, 29 Sep 2023 21:06:10 GMT  
  Content: That's the way it always is. It will be the same when this new batch gets old.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=11

- **Post ID: 1707863715465273813**  
  Author: Kathie Anderson (@KathieA04536309)  
  Timestamp: Fri, 29 Sep 2023 21:03:34 GMT  
  Content: Going on Charlie Kirk’s show speaks volumes. The guy’s a jerk.  
  Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=19

- **Post ID: 1707843551957025222**  
  Author: Blake McBay (@bjmcbay)  
  Timestamp: Fri, 29 Sep 2023 19:43:27 GMT  
  Content: @tpusaetsu put on the most electric event of the year so far with @Riley_Gaines_! Hundreds of people showed up. After running out of room, many people just stood outside the door wanting to listen! It is so encouraging to see young people listening to a voice or reason! @TPUSA  
  Media: 4 items (videos and photos of the event)  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=175

- **Post ID: 1707830198408982687**  
  Author: We are Charlie Kirk (@georgew90447947)  
  Timestamp: Fri, 29 Sep 2023 18:50:23 GMT  
  Content: Austin will be the next San Francisco!  
  Engagement: Likes=2, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=15

- **Post ID: 1707812812033241505**  
  Author: Aly (@lilalyp)  
  Timestamp: Fri, 29 Sep 2023 17:41:18 GMT  
  Content: I attended a phenomenal event put on by @MtnStatesPolicy this week in Spokane at The Gathering House - #TheWomanPanel 👩🏻👩🏼👩🏽👩🏻‍🦰 Hearing women in education and policy speak out about free market principles was SO inspiring! 🗽 Can’t wait for next month! 🗓️ @TPUSA @tpusastudents  
  Media: 4 photos  
  Engagement: Likes=5, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=112

### From x_keyword_search (Top mode, general query):
- **Post ID: 1706708076231794816**  
  Author: FIRE (@TheFIREorg)  
  Timestamp: Tue, 26 Sep 2023 16:31:29 GMT  
  Content: FIRE is pleased to read that @ASU found no evidence of viewpoint discrimination regarding the closure of the T.W. Lewis Center and will once again be hosting an event featuring Charlie Kirk and Dennis Prager this Wednesday.  
  (Quoted post about ASU closing the Lewis Center)  
  Engagement: Likes=41, Reposts=5, Quotes=4, Replies=3, Bookmarks=2, Views=13992

- **Post ID: 1707096823138054467**  
  Author: Libs of TikTok (@libsoftiktok)  
  Timestamp: Wed, 27 Sep 2023 18:16:13 GMT  
  Content: BREAKING: I went with @TPUSA to Burbank, CA to ask #MayorSpanky about the public spanking he got from a drag queen at an event that was open to children and why he lied about it. Watch what happens next!  
  Media: 1 video  
  Engagement: Likes=20459, Reposts=5897, Quotes=256, Replies=857, Bookmarks=479, Views=3775780

- **Post ID: 1707123078009155615**  
  Author: Human Events (@HumanEvents)  
  Timestamp: Wed, 27 Sep 2023 20:00:33 GMT  
  Content: Charlie Kirk: "Politicians do not want to speak out against the massive looting, because they don't want to be called a racist."  
  Media: 1 video  
  Engagement: Likes=20, Reposts=3, Quotes=1, Replies=1, Bookmarks=1, Views=8878

- **Post ID: 1706425437830689108**  
  Author: 🔥 Lzzy 🔥 (@ElizabethPDove)  
  Timestamp: Mon, 25 Sep 2023 21:48:22 GMT  
  Content: "A group of alt-right and 'dissident right' activists have joined forces with neo-Nazis and others on the far-right fringes to attack conservatives who they feel aren’t true conservatives, both online and in person. 'Sunday, for instance, members of this group heckled Donald Trump Jr. at an event in California. And conservative speakers have been beset by the 'groypers' at events in Texas, Tennessee and Arizona as well. This group, which calls itself the 'groyper army' — 'groyper' being a reference to a meme of Pepe the Frog, itself a meme overtaken by the alt-right — purports to be supporting 'traditional values' within conservatism, like immigration restrictionism. And it argues that relatively mainstream conservative student groups like Turning Point USA need to be confronted because they are shutting down 'socially conservative Christians and supporters of President Trump’s agenda' and promoting 'degeneracy' by having gay speakers." https://t.co/9F9UTuhK9j I just have one question. How could say you support President Trump's agenda in one breath and attack his son publicly in another?  
  Engagement: Likes=22, Reposts=6, Quotes=0, Replies=4, Bookmarks=1, Views=2997

- **Post ID: 1707445466802319562**  
  Author: Austin Erickson (@Austin4_Liberty)  
  Timestamp: Thu, 28 Sep 2023 17:21:36 GMT  
  Content: 🚨 Red Mountain High School in Mesa, AZ is pretending that the cancellation of an approved TPUSA High School event with Will Witt and Rep Austin Smith was just due to scheduling conflicts. However, it's become clear they caved to leftist pressure. 🚨  
  Media: 1 photo  
  Engagement: Likes=34, Reposts=14, Quotes=2, Replies=1, Bookmarks=0, Views=5896

- **Post ID: 1707473755365339162**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 28 Sep 2023 19:14:01 GMT  
  Content: Arizona Republic: "Charlie Kirk calls for Arizona lawmakers to defund state universities at ASU event" 🔥🔥🔥 https://www.azcentral.com/story/news/politics/arizona/2023/09/28/charlie-kirk-calls-for-arizona-lawmakers-to-defund-universities/70936441007/  
  Engagement: Likes=408, Reposts=64, Quotes=2, Replies=94, Bookmarks=2, Views=44582

- **Post ID: 1706405375249973344**  
  Author: Evan Kilgore 🇺🇸 (@EvanAKilgore)  
  Timestamp: Mon, 25 Sep 2023 20:28:39 GMT  
  Content: Speaking properly Basic math Common courtesy Critical thinking Listening Problem solving Sadly, you can't really expect these anymore.  
  Engagement: Likes=8, Reposts=1, Quotes=0, Replies=1, Bookmarks=0, Views=473

- **Post ID: 1707217699552588238**  
  Author: The State Press (@statepress)  
  Timestamp: Thu, 28 Sep 2023 02:16:32 GMT  
  Content: Kirk and Turning Point USA volunteers gathered outside the Memorial Union to debate students and promote the Health, Wealth & Happiness 2.0 event happening that night. https://www.statepress.com/article/2023/09/turning-point-charlie-kirk-asu-student-debate  
  Engagement: Likes=8, Reposts=3, Quotes=1, Replies=1, Bookmarks=0, Views=2800

- **Post ID: 1707575898575446463**  
  Author: misha (@birdsigma)  
  Timestamp: Fri, 29 Sep 2023 01:59:54 GMT  
  Content: Ed Seidel unintentionally(?) giving tpusa an absurd amount of free publicity for their nasty little event in his gross little message is so on brand.  
  Engagement: Likes=6, Reposts=0, Quotes=0, Replies=3, Bookmarks=0, Views=340

- **Post ID: 1707496948175941784**  
  Author: Matthew Boedy (@MatthewBoedy)  
  Timestamp: Thu, 28 Sep 2023 20:46:10 GMT  
  Content: By day Charlie Kirk praises free speech on campus and his college student supporters who gathered at his Arizona State event. (After he was booed at another school) By night, Kirk calls for the state to defund their degree programs. 🤔🤷🏽‍♂️👇🏽  
  Media: 3 photos  
  Engagement: Likes=3, Reposts=2, Quotes=1, Replies=0, Bookmarks=1, Views=548

### From x_semantic_search:
- **Post ID: 1706051166969180473**  
  Author: The Gateway Pundit (@gatewaypundit)  
  Timestamp: Sun, 24 Sep 2023 21:01:09 GMT  
  Content: President Trump to Deliver Remarks In Summerville, SC Monday – EVENT SOLD OUT via @gatewaypundit https://www.thegatewaypundit.com/2023/09/president-trump-deliver-remarks-summerville-sc-monday-event/?utm_source=rss&utm_medium=rss&utm_campaign=president-trump-deliver-remarks-summerville-sc-monday-event  
  Engagement: Likes=468, Reposts=135, Quotes=3, Replies=14, Bookmarks=0, Views=15049

- **Post ID: 1707867523155452275**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Fri, 29 Sep 2023 21:18:42 GMT  
  Content: Donald Trump LIVE from Anaheim, California RAILING against the Gold State's insane politicians is the BEST thing you'll see today: 🔥🤣😂  
  Media: 1 video  
  Engagement: Likes=4660, Reposts=1136, Quotes=54, Replies=391, Bookmarks=61, Views=184551

- **Post ID: 1705939501455901000**  
  Author: Grasshopper (@17Grasshopper)  
  Timestamp: Sun, 24 Sep 2023 13:37:26 GMT  
  Content: 🚨EYES ON!👇 💥Elon && Scavino Crumbs💥 Are we Getting a Heads-Up?! Elon Dropping: Great Difference, no matter how you COUNT IT 265-3MILLION= 262MILLION DIFFERENCE,.. ##262 👉25TH👈RED RED STRINGER 👉27TH👈HUSSEIN 👉28TH👈HUSSEIN ANALYZE👀 COINCIDENCE😉 MORE than ONE meaning. 👉Hussein RED INDICTMENTS variables👈 Think CIRCLE. EXPAND your thinking. Take MULTIPLE paths. One CONNECTS to ANOTHER. LEARN to read the map. The map is the KEY. FIND the keystone. What holds everything together? Q Now Take that with the CRUMBS of Scavino,.. [MONDAY] (((25TH?!))) Next Week - BIGGER. PUBLIC. We LISTENED [20/80 />/ 40/60]. Q So are we getting a Heads Up For Monday 25th, Tuesday 26th and Wednesday 27th?! Stay tuned Patriots it might get Spicy,. Please Join us On Rumble and HIT THAT Notification🔔 so You Won't Miss Another Live Stream AGAIN😎👇 https://t.co/dWdEr8r3NL This afternoon: We will go Live after the TGA Show for a Live Q&A. Monday: We will cover the Trump Speech Tuesday: 3PM EST we will watch The greatest show on earth togeter! Wednesday: We Might Go Live with a Mid-Week WEEK Special Update on all the Crumbs from the Q-Team Friday: we will Cover the Trump Speech Live and Decode His Crumbs Live On air All Grasshopper Links:😎👇 https://t.co/BkwMdQWm8e Grasshopper Collection:😎👇 https://t.co/4aToxR4u61 Chat🔗 https://t.co/i12cMGTmLO @8Notables @Allenma15086871 @andweknow @Leonidas_17GOI @Joanne60183156 @Jmsesq555 @LFGRT99 @hhpatriotnc @Tinktweets45 @TifaniesweTs @TwatIntelHQ @FFreeSSpeech @juliedonuts @BrainStorm_Joe @17ThankQ @Stylzbeats @faulkner951 @TKCrecovered  
  Media: 1 photo  
  Engagement: Likes=207, Reposts=100, Quotes=6, Replies=11, Bookmarks=10, Views=18425

- **Post ID: 1707142503198081263**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Wed, 27 Sep 2023 21:17:44 GMT  
  Content: “Mostly-Peaceful” Philly Looters and Mar-a-Lago is Worth WHAT?? With @DonaldJTrumpJr 🔥⬇️ https://podcasts.apple.com/us/podcast/the-charlie-kirk-show/id1460600818  
  Engagement: Likes=234, Reposts=58, Quotes=1, Replies=42, Bookmarks=0, Views=41557

- **Post ID: 1706768003776626792**  
  Author: Kari Lake (@KariLake)  
  Timestamp: Tue, 26 Sep 2023 20:29:36 GMT  
  Content: I’m so excited to be speaking at the #WalkAway Campaign’s EPIC Patriot weekend called #WalkACon! It’s time we get energized, motivated and ready to WIN in 2024! I’ll be headlining Sunday’s brunch & signing books after for all of you! TICKETS: https://t.co/2PBYyYOZwg  
  Media: 1 photo  
  Engagement: Likes=807, Reposts=169, Quotes=7, Replies=143, Bookmarks=1, Views=88165

- **Post ID: 1706486711864131923**  
  Author: Illinigirl62 (@hsjphil01)  
  Timestamp: Tue, 26 Sep 2023 01:51:51 GMT  
  Content: DeSantis On Deck for September 25th-29th Tuesday •Ron DeSantis will be interviewed by Doug Wagner on News Radio 600 WMT in Cedar Rapids, Iowa. •Ron DeSantis will be interviewed by Fox News’ Laura Ingraham in the 7 PM ET hour. Wednesday •Ron DeSantis will participate in the second GOP debate at the Reagan Library. •Ron DeSantis and Casey DeSantis join Never Back Down's Post-Debate After Party as special guests in Westlake Village, California. Thursday •Ron DeSantis will be interviewed by Dana Perino and Bill Hemmer on Fox News’ America’s Newsroom in the 11 AM ET hour. This time is wrong, I think. America’s Newsroom is from 7:00-9:00 ET. Friday •DeSantis will host a campaign event in Long Beach, California.  
  Media: 1 photo  
  Engagement: Likes=308, Reposts=78, Quotes=5, Replies=14, Bookmarks=6, Views=10044

- **Post ID: 1705794605097078924**  
  Author: MS NOW (@MSNOWNews)  
  Timestamp: Sun, 24 Sep 2023 04:01:40 GMT  
  Content: The #WITHpod tour is underway! @chrislhayes was in Austin for the kick off. @JoyAnnReid joins Chris LIVE in Philadelphia Monday, October 16th. Get tickets here https://www.ms.now/withpodtour  
  Engagement: Likes=179, Reposts=34, Quotes=1, Replies=41, Bookmarks=2, Views=184310

- **Post ID: 1706718203701850197**  
  Author: Charlie LeDuff (@Charlieleduff)  
  Timestamp: Tue, 26 Sep 2023 17:11:43 GMT  
  Content: Irony of ironies: Biden flies directly over East Palestine, Ohio and lands in Detroit... just 150 miles away. Gives bullhorn remarks to UAW strikers (Joe voted for Nafta). He'll then fly directly to Frisco for two days of fundraising. Tomorrow, Trump will rally a group of mostly retired autoworkers at a non-union plant in metro Detroit. We're fucked. I'm live tonight in EP,OH w/ @ChrisCuomo  
  Media: 1 photo  
  Engagement: Likes=369, Reposts=95, Quotes=10, Replies=79, Bookmarks=6, Views=40192

- **Post ID: 1707462817056424173**  
  Author: Illinigirl62 (@hsjphil01)  
  Timestamp: Thu, 28 Sep 2023 18:30:33 GMT  
  Content: Updated DeSantis on Deck- September 28-30 DeSantis On Deck Today •Ron DeSantis was interviewed by Dana Perino and Bill Hemmer on Fox News’ America’s Newsroom earlier this morning. Friday •Ron DeSantis will host a campaign event in Long Beach, California that will be livestreamed on https://t.co/xldC0gVru8 and across our social platforms. •Ron DeSantis will sit down with Bill Maher for an interview that will air on Real Time with Bill Maher at 10pm ET on HBO. •Ron DeSantis will be the keynote speaker at the California GOP Convention in Anaheim, California.  
  Engagement: Likes=227, Reposts=46, Quotes=2, Replies=21, Bookmarks=3, Views=9320

### From x_keyword_search (from:charliekirk11):
- **Post ID: 1707473755365339162** (duplicate of above)  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Thu, 28 Sep 2023 19:14:01 GMT  
  Content: Arizona Republic: "Charlie Kirk calls for Arizona lawmakers to defund state universities at ASU event" 🔥🔥🔥 https://www.azcentral.com/story/news/politics/arizona/2023/09/28/charlie-kirk-calls-for-arizona-lawmakers-to-defund-universities/70936441007/  
  Engagement: Likes=408, Reposts=64, Quotes=2, Replies=94, Bookmarks=2, Views=44582

- **Post ID: 1706465390182941059**  
  Author: Charlie Kirk (@charliekirk11)  
  Timestamp: Tue, 26 Sep 2023 00:27:08 GMT  
  Content: America's foreign-born population is approaching 50,000,000 for the first time in history under Joe Biden — and it's fueling ALL current population growth. You have the Open Borders lobby to thank when... Your kids go to school with kids who don’t speak English. A fentanyl overdose claims the life of a friend or family members. You local hospital’s ER is perpetually overrun. Your wages are so depressed you can't survive on a working class job. Your streets are filthy, dangerous, and filled with sullen groups of young military-age men. You look around your communities and see strangers, people who can’t name the Founding Fathers and who have never heard of the Battle of the Bulge. Polls consistently show that Americans want less immigration, an end to chain migration, deportations for immigrant criminals, and a secure border. Instead we get Joe Biden's invasion.  
  Media: 1 photo  
  Engagement: Likes=2485, Reposts=897, Quotes=63, Replies=500, Bookmarks=72, Views=383817

### From x_keyword_search (from:TPUSA):
No results found.

This constitutes the complete, unsummarized dataset of all matching posts from the tools for the exact week range. Key events referenced include a Charlie Kirk/TPUSA event at ASU (Arizona State University) on or around September 27-28, 2023 (including campus debate and "Health, Wealth & Happiness 2.0"), a TPUSA event with Riley Gaines by @tpusaetsu, and a TPUSA High School event cancellation at Red Mountain High School in Mesa, AZ. Other posts mention TPUSA activities but do not detail additional speaking dates in the range.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2023-09-24 to 2023-09-30**, the range this page covers.

**Ground contacts near a sourced Charlie / Erika / TPUSA event** — the **2** most significant of **3** this page touches, foreign-fleet and same-day first, then most recent. The full set is on [the contacts index](/Planes/Incidents/overview) and on each aircraft's own page.

| Date (UTC) | Aircraft | Airport | City, State | Whose event | When |
|---|---|---|---|---|---|
| [2023-09-28](/Planes/Incidents/N560TW-2023-09-28-KSDL) | [N560TW](/Planes/N560TW/overview) | [KSDL](/Planes/Airports/KSDL) | Scottsdale, AZ | Charlie | Day after |
| [2023-09-28](/Planes/Incidents/N582MM-2023-09-28-KPHX) | [N582MM](/Planes/N582MM/overview) | [KPHX](/Planes/Airports/KPHX) | Phoenix, AZ | Charlie | Day after |

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
