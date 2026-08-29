---
unlisted: true
title: "Week 29 2022 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2022-W29"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2022-07-16 to 2022-07-22."
status: completed
hide_table_of_contents: true
---

# Week 29, 2022

- Date range: 2022-07-16 to 2022-07-22
- Queried at (UTC): 2026-08-24T19:02:34Z
- Model: grok-4.3
- API status: completed
- Response id: 2124d2f6-e910-9fd0-bec3-e7321fc610aa

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2022-07-16 to the end of the week 2022-07-22.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR rally OR campus) since:2022-07-16 until:2022-07-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (event OR speaking OR speak OR tour OR appearance OR \"will be\" OR speaking OR rally OR campus) since:2022-07-16 until:2022-07-23 filter:links",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie will speak between July 16-22 2022",
      "limit": "10",
      "from_date": "2022-07-16",
      "to_date": "2022-07-22",
      "min_score_threshold": "0.1"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Student Action Summit\" OR SAS2022 OR #SAS2022 OR \"SAS 2022\") (Tampa OR Florida) since:2022-07-16 until:2022-07-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA since:2022-07-16 until:2022-07-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 since:2022-07-16 until:2022-07-23",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (Tampa OR \"Student Action Summit\" OR SAS) since:2022-07-16 until:2022-07-23",
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
  "input_tokens": 23147,
  "input_tokens_details": {
    "cached_tokens": 4160
  },
  "output_tokens": 8462,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 31609,
  "num_sources_used": 0,
  "num_server_side_tools_used": 7,
  "cost_in_usd_ticks": 807207500,
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
    "input_tokens": 14403,
    "output_tokens": 8065
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550253541377335297",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550253541377335297"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549891908029202439",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549891908029202439"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549908957736706049",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549908957736706049"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550214931433283585",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550214931433283585"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550157950580400128",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550157950580400128"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549892480169963521",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549892480169963521"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550094495944957952",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550094495944957952"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549882498636603393",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549882498636603393"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550205133987975168",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550205133987975168"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550127755789864960",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550127755789864960"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550237522416082944",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550237522416082944"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550139925017767936",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550139925017767936"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550132178813472768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550132178813472768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1548315504372117505",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1548315504372117505"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550169712948137984",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550169712948137984"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549606753280503809",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549606753280503809"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550196454953828355",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550196454953828355"
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
    "url": "https://x.com/i/status/1550144036576657408",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550144036576657408"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549851827696386048",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549851827696386048"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550172706116882432",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550172706116882432"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549081750864891905",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549081750864891905"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549553431584448512",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549553431584448512"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550105659848499201",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550105659848499201"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1548748114546262017",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1548748114546262017"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550237148653166593",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550237148653166593"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550071178651484161",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550071178651484161"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549778391947251712",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549778391947251712"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550165908030734336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550165908030734336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550133407396442115",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550133407396442115"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550176720623370240",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550176720623370240"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549984287583342593",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549984287583342593"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550264906246754305",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550264906246754305"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550200714529587200",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550200714529587200"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549001041303244802",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549001041303244802"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550189510851530762",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550189510851530762"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550148755382587395",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550148755382587395"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549120912112332800",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549120912112332800"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549188447608492034",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549188447608492034"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550241899721633793",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550241899721633793"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550204318409580544",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550204318409580544"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550130259831373828",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550130259831373828"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549893941679591424",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549893941679591424"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549860914672721920",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549860914672721920"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549801703985123334",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549801703985123334"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550101286858752000",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550101286858752000"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550204567870218249",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550204567870218249"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550251985038876672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550251985038876672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549554955102478336",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549554955102478336"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549889967781920768",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549889967781920768"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550201441377308672",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550201441377308672"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1550210172051755009",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1550210172051755009"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1549493609464045569",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1549493609464045569"
  }
]
```

## Grok response

```text
**Here is all the raw X (Twitter) post data** from the searched results matching your exact criteria (posts referencing Charlie Kirk or TPUSA/TPUSA events/speaking appearances between 2022-07-16 and 2022-07-22, with full content, metadata, and no summarization or filtering beyond the tool results). I used keyword and semantic searches limited to the date range; results are presented as retrieved (including duplicates across searches). No other posts in the results directly announced or detailed specific speaking events by Charlie Kirk himself outside the context of the TPUSA event.

### Posts from first keyword search ("Charlie Kirk" OR TPUSA OR "Turning Point USA" + event/speaking keywords, Latest mode):
- **[post:0]** ID: 1550264906246754305 | Author: @AmericaToLove | Timestamp: Thu, 21 Jul 2022 23:42:10 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A  
  Content: COVID's silver lining. The more unvaccinated republicans there are the fewer republicans there will be to influence future elections.  
  Thank you Charlie Kirk!

- **[post:1]** ID: 1550251985038876672 | Author: @luxurybrokerfl | Timestamp: Thu, 21 Jul 2022 22:50:50 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550251943024533504/pu/vid/888x478/FKMi7Lc1gWo8kK2Y.mp4?tag=12 (duration: 13438 ms)  
  Content: Me on my way to #Tampa for the @TPUSA event. #Americafirst #tampa

- **[post:2]** ID: 1550237522416082944 | Author: @manicracing6 | Timestamp: Thu, 21 Jul 2022 21:53:22 GMT | Engagement: Likes=10, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: After the last few days of sunshine I no sport a fantastic tan.....  
  We need a holiday so I've booked a dinghy for a few hours to assist in getting our 5 star hotel for free ....  
  Simple enough to plan....  
  No need for id or even speaking the language just claim no inglish

- **[post:3]** ID: 1550237148653166593 | Author: @PatriotMobile | Timestamp: Thu, 21 Jul 2022 21:51:52 GMT | Engagement: Likes=1, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYOK3APWAAA-8bS.jpg  
  Content: Patriot Mobile is proud to sponsor @TPUSA's #SAS2022!  
  Stop by our booth:  
  - Free 'I Identify As A Patriot' t-shirts!  
  - Chance to win iPhone by posting on social media wearing t-shirt, tag Patriot Mobile & use hashtags #SAS2022 & #PatriotMobile  
  - Winner will be chosen on Saturday!

- **[post:4]** ID: 1550200714529587200 | Author: @Heerak4Congress | Timestamp: Thu, 21 Jul 2022 19:27:06 GMT | Engagement: Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550200476787941377/pu/vid/1280x720/RuycerDNwawkZkOZ.mp4?tag=12 (duration: 139991 ms)  
  Content: Heerak gives a tour of Stafford Air and Space Museum in Weatherford, OK.  
  @GeorgetownCR @crsatuva @TPUSA @yaf @RichAndersonRPV @cToddGilbert @VASenateGOP @vahousegop @VBYR @RichmondYRs @VirginiaYRs @yrnf @YALiberty @JudiciaryGOP @HouseGOP @SenateGOP @GOPLeader @LeaderMcConnell @CR

- **[post:5]** ID: 1550176720623370240 | Author: @Ladyoftheplains | Timestamp: Thu, 21 Jul 2022 17:51:45 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: Watching BG Masters speak on RAVoice Charlie Kirk show.  
  Very dynamic, creative thinker, candidate for Senate.

- **[post:6]** ID: 1550165908030734336 | Author: @AllAboutEve____ | Timestamp: Thu, 21 Jul 2022 17:08:47 GMT | Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: OK it’s time to talk about this. In almost every space someone has something negative about the listeners. We are your numbers and supporters. If we speak up you know for sure we are going to be attacked by some of people that should be run off.I joined in 2015 & am well informed

### Posts from second keyword search (same query + filter:links, Latest mode):
- **[post:7]** ID: 1550251985038876672 | Author: @luxurybrokerfl | Timestamp: Thu, 21 Jul 2022 22:50:50 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550251943024533504/pu/vid/888x478/FKMi7Lc1gWo8kK2Y.mp4?tag=12 (duration: 13438 ms)  
  Content: Me on my way to #Tampa for the @TPUSA event. #Americafirst #tampa

- **[post:8]** ID: 1550237148653166593 | Author: @PatriotMobile | Timestamp: Thu, 21 Jul 2022 21:51:52 GMT | Engagement: Likes=1, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYOK3APWAAA-8bS.jpg  
  Content: Patriot Mobile is proud to sponsor @TPUSA's #SAS2022!  
  Stop by our booth:  
  - Free 'I Identify As A Patriot' t-shirts!  
  - Chance to win iPhone by posting on social media wearing t-shirt, tag Patriot Mobile & use hashtags #SAS2022 & #PatriotMobile  
  - Winner will be chosen on Saturday!

- **[post:9]** ID: 1550200714529587200 | Author: @Heerak4Congress | Timestamp: Thu, 21 Jul 2022 19:27:06 GMT | Engagement: Likes=0, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550200476787941377/pu/vid/1280x720/RuycerDNwawkZkOZ.mp4?tag=12 (duration: 139991 ms)  
  Content: Heerak gives a tour of Stafford Air and Space Museum in Weatherford, OK.  
  @GeorgetownCR @crsatuva @TPUSA @yaf @RichAndersonRPV @cToddGilbert @VASenateGOP @vahousegop @VBYR @RichmondYRs @VirginiaYRs @yrnf @YALiberty @JudiciaryGOP @HouseGOP @SenateGOP @GOPLeader @LeaderMcConnell @CR

- **[post:10]** ID: 1550132178813472768 | Author: @realmadiselee | Timestamp: Thu, 21 Jul 2022 14:54:46 GMT | Engagement: Likes=24, Reposts=11, Quotes=0, Replies=2, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/tweet_video/FYMs9IaUsAEbIiq.mp4 (duration: 0 ms)  
  Content: ACTIVISTS & STAFF HURRYING TO THEIR SEATS TO HEAR @AndrewSypher speak!!  
  @TPUSA’s CLS 2022 HAS BEGUN!

- **[post:11]** ID: 1550101286858752000 | Author: @CryptidPolitics | Timestamp: Thu, 21 Jul 2022 12:52:00 GMT | Engagement: Likes=1, Reposts=0, Quotes=0, Replies=1, Bookmarks=1, Views=N/A  
  Content: We are seeing the Trump / DeSantis showdown beginning to take shape.  
  Trump will be in Florida to speak at a TPUSA event while DeSantis headlines a Rubio re-election event.  
  Trump STILL has not endorsed RDS re-election. RDS hasn’t asked.  
  #DeSantis2024

- **[post:12]** ID: 1550094495944957952 | Author: @patriottakes | Timestamp: Thu, 21 Jul 2022 12:25:01 GMT | Engagement: Likes=207, Reposts=66, Quotes=8, Replies=30, Bookmarks=6, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYMKuk9XgAAYS85.jpg  
  Content: The man who sexually harassed AOC just had white nationalist Nick Fuentes on his podcast. He also announced he is working with @TPUSA and will be at their Student Action Summit.

- **[post:13]** ID: 1549984287583342593 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 05:07:06 GMT | Engagement: Likes=52, Reposts=13, Quotes=0, Replies=5, Bookmarks=1, Views=N/A  
  Content: This weekend, a sense of pride and direction in the American way of life will be restored.  
  https://www.thecollegefix.com/conservative-conference-will-train-the-future-leaders-america-needs/

### Posts from semantic search (Charlie Kirk or TPUSA public speaking events... between July 16-22 2022):
- **[post:14]** ID: 1550201441377308672 | Author: @reneeAZpatriot4 | Timestamp: Thu, 21 Jul 2022 19:29:59 GMT | Engagement: Likes=192, Reposts=163, Quotes=6, Replies=39, Bookmarks=3, Views=N/A  
  Content: 🇺🇲 TRUMP RALLY 🇺🇲   
    Prescott Valley, AZ  
             Friday  
            7/22/22  
           7pm MST  
  Special Guest Speakers:  
  ✔Kari Lake  
  ✔Blake Masters  
  ✔Abe Hamadeh  
  ✔Mark Finchem  
  ✔Richard Grenell  
  ✔Sheriff Mark Lamb  
  ✔Kelly Ward  
  ✔Mike Lindell  
  WATCH HERE👇

- **[post:15]** ID: 1548315504372117505 | Author: @1813Doncarlo | Timestamp: Sat, 16 Jul 2022 14:35:57 GMT | Engagement: Likes=156, Reposts=63, Quotes=10, Replies=12, Bookmarks=0, Views=N/A  
  Content: Donald Trump is scheduled to speak in Washington, D.C. on July 26, at an event sponsored by a rightwing group, America First Policy Institute.  
  WTF.    
  Trump shouldn't be permitted within 100 miles of D.C.  
  A man who staged a coup in a deadly attack on the Capitol should be banned

- **[post:16]** ID: 1549120912112332800 | Author: @charliekirk11 | Timestamp: Mon, 18 Jul 2022 19:56:21 GMT | Engagement: Likes=203, Reposts=65, Quotes=7, Replies=18, Bookmarks=0, Views=N/A  
  Content: Turning Point USA chapters change the world  
  Join us this weekend  
  http://TPUSA.com/SAS

- **[post:17]** ID: 1549188447608492034 | Author: @kirkmin | Timestamp: Tue, 19 Jul 2022 00:24:43 GMT | Engagement: Likes=228, Reposts=1, Quotes=2, Replies=15, Bookmarks=1, Views=N/A  
  Content: Show tomorrow morning at 9. Live on YouTube.

- **[post:18]** ID: 1549081750864891905 | Author: @SouthPark | Timestamp: Mon, 18 Jul 2022 17:20:44 GMT | Engagement: Likes=291, Reposts=30, Quotes=21, Replies=12, Bookmarks=10, Views=N/A  
  Content: South Park The 25th Anniversary Experience is going cross-country! Local time 10AM to 6PM.   
   New York: 7/23 Union Square  
   Chicago: 7/30 Navy Pier  
   Red Rocks: 8/9 - 8/10 Red Rocks Trading Post*  
   Denver: 8/12 - 8/13 McGregor Square  
   Los Angeles: 8/20 Hollywood & Vine  
  *Hours TBD

- **[post:19]** ID: 1549001041303244802 | Author: @kylegriffin1 | Timestamp: Mon, 18 Jul 2022 12:00:01 GMT | Engagement: Likes=4761, Reposts=839, Quotes=36, Replies=82, Bookmarks=15, Views=N/A  
  Content: Save the date. The January 6th Committee's next hearing is in primetime: Thursday, July 21 at 8pm.

- **[post:20]** ID: 1550241899721633793 | Author: @KariLake | Timestamp: Thu, 21 Jul 2022 22:10:45 GMT | Engagement: Likes=471, Reposts=114, Quotes=2, Replies=26, Bookmarks=1, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYOQymgUIAA5ogh.jpg  
  Content: There’s less than 1 day until President Trump’s Save AMERICA Rally in Prescott Valley!   
  Join President Trump and @karilake by getting your tickets today!  
  TICKETS: https://t.co/Rul9l9kcW7

- **[post:21]** ID: (empty ID) | Author: (unknown) | Timestamp: (none) | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: (No text content)

- **[post:22]** ID: 1548748114546262017 | Author: @kinley_brenda | Timestamp: Sun, 17 Jul 2022 19:14:59 GMT | Engagement: Likes=116, Reposts=82, Quotes=5, Replies=4, Bookmarks=2, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FX5CM5TXkAEGu5p.jpg  
  Content: 🧨 COMING SOON 🧨  
  “The Missing 187 Minutes”  
  The final Jan 6 public hearing is Thursday, July 21st at 8:00 pm EST  
  🎥 Will go through minute-by-minute from the time TFG left the rally until he issued statement to crowd to go home  
  #Jan6Justice   
  #DemVoice1   
  #Dems4USA

- **[post:23]** ID: 1549493609464045569 | Author: @realJennaEllis | Timestamp: Tue, 19 Jul 2022 20:37:19 GMT | Engagement: Likes=213, Reposts=46, Quotes=2, Replies=10, Bookmarks=5, Views=N/A  
  Content: WATCH: Charlie Kirk tells trans activist to stop 'trying to remove everything that offends you in the world'  
  https://thepostmillennial.com/

### Additional posts from targeted keyword searches (Student Action Summit / SAS2022 / Tampa / from:TPUSA / from:charliekirk11 / etc.):
- **[post:24]** ID: 1550204567870218249 | Author: @NowellJS | Timestamp: Thu, 21 Jul 2022 19:42:25 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: 🔴 PRESIDENT DONALD TRUMP AT TPUSA STUDENT ACTION SUMMIT LIVE IN TAMPA, F... https://t.co/RbSswVXroU via @YouTube

- **[post:25]** ID: 1550196454953828355 | Author: @cl_tampabay | Timestamp: Thu, 21 Jul 2022 19:10:10 GMT | Engagement: Likes=10, Reposts=6, Quotes=1, Replies=2, Bookmarks=0, Views=N/A  
  Content: Tampa Bay activist groups will protest Turning Point USA's Student Action Summit

- **[post:26]** ID: 1550189510851530762 | Author: @rayroa | Timestamp: Thu, 21 Jul 2022 18:42:35 GMT | Engagement: Likes=3, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: Tampa Bay activist groups will protest Turning Point USA's Student Action Summit

- **[post:27]** ID: 1550169712948137984 | Author: @LizWillis_ | Timestamp: Thu, 21 Jul 2022 17:23:54 GMT | Engagement: Likes=60, Reposts=10, Quotes=0, Replies=5, Bookmarks=0, Views=N/A  
  Content: Headed to Tampa for @TPUSA Student Action Summit! Can’t wait to see everyone there!   
  #SAS2022 🇺🇸 ☀️

- **[post:28]** ID: 1550144036576657408 | Author: @fineout | Timestamp: Thu, 21 Jul 2022 15:41:53 GMT | Engagement: Likes=2, Reposts=1, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: Lots of Republican action happening over the next few days in Florida....  
  @TPUSA holding its Student Action Summit in Tampa  
  @FloridaGOP holding its Sunshine Summit in Hollywood  
  Maverick Inc. holding Mavcon22 in Tampa ...  
  Rubio, Scott, Moody, Donalds, Cammack at multiple events

- **[post:29]** ID: 1550105659848499201 | Author: @jenvanlaar | Timestamp: Thu, 21 Jul 2022 13:09:23 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: Tampa for @TPUSA Student Action Summit

- **[post:30]** ID: 1550071178651484161 | Author: @vannschaffner | Timestamp: Thu, 21 Jul 2022 10:52:22 GMT | Engagement: Likes=1, Reposts=0, Quotes=1, Replies=0, Bookmarks=0, Views=N/A  
  Content: SAS 2022 - Turning Point USA #Tampa!

- **[post:31]** ID: 1549908957736706049 | Author: @TheBrandonMorse | Timestamp: Thu, 21 Jul 2022 00:07:46 GMT | Engagement: Likes=4, Reposts=0, Quotes=0, Replies=1, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYJh-z_XEAUmBRQ.jpg  
  Content: Making sure everything is setup to stream at the @RedState booth for RedState Live! at @TPUSA’s #sas2022 in Tampa! See you there tomorrow!

- **[post:32]** ID: 1549893941679591424 | Author: @JordynAB716 | Timestamp: Wed, 20 Jul 2022 23:08:05 GMT | Engagement: Likes=22, Reposts=6, Quotes=0, Replies=2, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYJUUHWXoAkXQUT.jpg  
  Content: Happy to be in Tampa with these ladies at @TPUSA’s #CLS2022 !! Excited for these next few days & then ##SAS2022 !!!

- **[post:33]** ID: 1550210172051755009 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 20:04:41 GMT | Engagement: Likes=90, Reposts=21, Quotes=4, Replies=13, Bookmarks=3, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550210084940222468/pu/vid/720x1280/kcRsatH_TLQVW401.mp4?tag=12 (duration: 36866 ms)  
  Content: Jobob must be identifying as the opposite of a male...  
  Merriam Webster is literally changing the meaning of words to fit the Left's agenda | @JobobTaeleifi @theisabelb

- **[post:34]** ID: 1550157950580400128 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 16:37:10 GMT | Engagement: Likes=22, Reposts=3, Quotes=0, Replies=4, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550157818094911489/pu/vid/720x1280/eiW_xYBAjpBoLOW4.mp4?tag=12 (duration: 14981 ms)  
  Content: We are 1 day away from #SAS2022 …  
  How HYPED are you?! 🔥🇺🇸

- **[post:35]** ID: 1550148755382587395 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 16:00:38 GMT | Engagement: Likes=62, Reposts=22, Quotes=1, Replies=6, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550148681223081984/pu/vid/720x1280/ygVCQybvTUYUDZvO.mp4?tag=12 (duration: 15000 ms)  
  Content: Check out #CLS2022 preparing students for another year of saving America! 🔥 🇺🇸 @JobobTaeleifi

- **[post:36]** ID: 1550133407396442115 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 14:59:39 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: @meganejohnson29 way to go, Megan! 🙌🏻🇺🇸

- **[post:37]** ID: 1549984287583342593 | Author: @TPUSA | Timestamp: Thu, 21 Jul 2022 05:07:06 GMT | Engagement: Likes=52, Reposts=13, Quotes=0, Replies=5, Bookmarks=1, Views=N/A  
  Content: This weekend, a sense of pride and direction in the American way of life will be restored.  
  https://www.thecollegefix.com/conservative-conference-will-train-the-future-leaders-america-needs/

- **[post:38]** ID: 1549892480169963521 | Author: @TPUSA | Timestamp: Wed, 20 Jul 2022 23:02:17 GMT | Engagement: Likes=35, Reposts=5, Quotes=0, Replies=7, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYJS_lEVEAAVydc.jpg  
  Content: Two more days until the biggest summer party of the year 🇺🇸 🏝  
  Who are you most excited to see? #SAS2022

- **[post:39]** ID: 1549891908029202439 | Author: @TPUSA | Timestamp: Wed, 20 Jul 2022 23:00:01 GMT | Engagement: Likes=82, Reposts=39, Quotes=2, Replies=5, Bookmarks=1, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/amplify_video/1549843967260299264/vid/1280x720/H9GwJMQocKAzUM9S.mp4?tag=14 (duration: 55680 ms)  
  Content: ANTIFA TARGETS WHITE 10 YEAR OLDS: Today on Frontlines, special guest Blaze TV host @ElijahSchaffer will be joining Drew covering a Portland ANTIFA KIDS Summer Camp   
  Tune into this full episode ⬇️  
  https://t.co/VwCvgL3R7U

- **[post:40]** ID: 1549889967781920768 | Author: @TPUSA | Timestamp: Wed, 20 Jul 2022 22:52:18 GMT | Engagement: Likes=2, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: @1776MichaelaM 🔥🔥🔥

- **[post:41]** ID: 1549882498636603393 | Author: @TPUSA | Timestamp: Wed, 20 Jul 2022 22:22:37 GMT | Engagement: Likes=69, Reposts=13, Quotes=0, Replies=1, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1549882375512793089/pu/vid/1280x720/daw3OScLAfdZN8Bg.mp4?tag=12 (duration: 117784 ms)  
  Content: The left thought we would remain silent—they were wrong.  
  We are proud to stand alongside the Scottsdale Moms RISING UP against the Scottsdale Unified School District for spying on parents and children.  
  Watch more ➡️ https://t.co/1MiCJ0xjgm

- **[post:42]** ID: 1549860914672721920 | Author: @TPUSA | Timestamp: Wed, 20 Jul 2022 20:56:51 GMT | Engagement: Likes=4, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: @STEPHMHAMILL SEE YOU SOON🎉

- **[post:43]** ID: 1550204318409580544 | Author: @charliekirk11 | Timestamp: Thu, 21 Jul 2022 19:41:25 GMT | Engagement: Likes=10361, Reposts=3217, Quotes=151, Replies=288, Bookmarks=28, Views=N/A  
  Content: So let me get this straight. The US Gov’t will let millions of unvaccinated illegals stream across the border and buy them plane tickets to anywhere they want to go, but they won’t let the world’s best tennis player come to New York and compete in the US Open?  
  This is a disgrace

- **[post:44]** ID: 1550139925017767936 | Author: @charliekirk11 | Timestamp: Thu, 21 Jul 2022 15:25:32 GMT | Engagement: Likes=6133, Reposts=1654, Quotes=119, Replies=256, Bookmarks=13, Views=N/A  
  Content: So 47 Republicans vote to redefine marriage, but not a single Democrat broke with the party line to block the sale of America’s Strategic Petroleum Reserves to China.   
  One side plays to win, and the other is doing everything it can to lose.

- **[post:45]** ID: 1550130259831373828 | Author: @charliekirk11 | Timestamp: Thu, 21 Jul 2022 14:47:08 GMT | Engagement: Likes=3073, Reposts=359, Quotes=13, Replies=147, Bookmarks=2, Views=N/A  
  Content: No, COVID is not what caused Joe Biden's brain fog.

- **[post:46]** ID: 1550127755789864960 | Author: @charliekirk11 | Timestamp: Thu, 21 Jul 2022 14:37:11 GMT | Engagement: Likes=11619, Reposts=2030, Quotes=269, Replies=1296, Bookmarks=22, Views=N/A  
  Content: BREAKING: Twice vaccinated and twice boosted Joe Biden tests positive for COVID-19

- **[post:47]** ID: 1549851827696386048 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 20:20:45 GMT | Engagement: Likes=7339, Reposts=2684, Quotes=108, Replies=216, Bookmarks=86, Views=N/A  
  Content: According to a new report from the German Ministry of Health, 1 in 5,000 INJECTIONS results in a "severe reaction."   
  There have been 600 million INJECTIONS in America, which means 120,000+ "severe reactions"   
  Why is this not the #1 news story in the country??    
  It's criminal

- **[post:48]** ID: 1549801703985123334 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 17:01:34 GMT | Engagement: Likes=3634, Reposts=715, Quotes=21, Replies=136, Bookmarks=12, Views=N/A  
  Content: Notice Mayra Flores didn't vote to redefine marriage like the 47 members of the feckless GOP. Maybe it’s because she represents voters who aren't yet totally captured by the white liberal mind pathogen.

- **[post:49]** ID: 1549778391947251712 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 15:28:56 GMT | Engagement: Likes=109, Reposts=31, Quotes=3, Replies=8, Bookmarks=1, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYHrO7LVUAAYr0K.jpg  
  Content: @tpaction is proud to endorse America's Governor from the free state of Florida, Ron DeSantis.

- **[post:50]** ID: 1549606753280503809 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 04:06:54 GMT | Engagement: Likes=16576, Reposts=2282, Quotes=259, Replies=1048, Bookmarks=39, Views=N/A  
  Content: Marriage is a covenant before the Lord between one man and one woman.

- **[post:51]** ID: 1549554955102478336 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 00:41:05 GMT | Engagement: Likes=10007, Reposts=3181, Quotes=189, Replies=458, Bookmarks=26, Views=N/A  
  Content: 9 million new illegal aliens will be in America by the end of Biden’s first term.   
  No sane country would allow this to happen.

- **[post:52]** ID: 1549553431584448512 | Author: @charliekirk11 | Timestamp: Wed, 20 Jul 2022 00:35:02 GMT | Engagement: Likes=2179, Reposts=299, Quotes=21, Replies=123, Bookmarks=2, Views=N/A  
  Content: Uncontrolled migration makes us a nation of strangers.

- **[post:53]** ID: 1550253541377335297 | Author: @RealAmVoice | Timestamp: Thu, 21 Jul 2022 22:57:01 GMT | Engagement: Likes=8, Reposts=4, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: Watch @RealDrGina  #PrimeTime LIVE from TPUSA's Student Action Summit!  
  https://t.co/KAkn9eEBV5

- **[post:54]** ID: 1550251985038876672 | Author: @luxurybrokerfl | Timestamp: Thu, 21 Jul 2022 22:50:50 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - video URL: https://video.twimg.com/ext_tw_video/1550251943024533504/pu/vid/888x478/FKMi7Lc1gWo8kK2Y.mp4?tag=12 (duration: 13438 ms)  
  Content: Me on my way to #Tampa for the @TPUSA event. #Americafirst #tampa

- **[post:55]** ID: 1550214931433283585 | Author: @AldoButtazzoni | Timestamp: Thu, 21 Jul 2022 20:23:35 GMT | Engagement: Likes=22, Reposts=1, Quotes=1, Replies=0, Bookmarks=0, Views=N/A | Media: Yes (1 item) - photo URL: https://pbs.twimg.com/media/FYN4QjAWIAAI1-x.jpg  
  Content: Just landed in Tampa. If you see me at SAS say hi!   
  @TPUSA

- **[post:56]** ID: 1550205133987975168 | Author: @ccc74905bff84db | Timestamp: Thu, 21 Jul 2022 19:44:40 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: LIVE AT TPUSA TAMPA - TRUMP DESANTIS

- **[post:57]** ID: 1550204567870218249 | Author: @NowellJS | Timestamp: Thu, 21 Jul 2022 19:42:25 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: 🔴 PRESIDENT DONALD TRUMP AT TPUSA STUDENT ACTION SUMMIT LIVE IN TAMPA, F... https://t.co/RbSswVXroU via @YouTube

- **[post:58]** ID: 1550172706116882432 | Author: @SsLjXjov8VeK8Dw | Timestamp: Thu, 21 Jul 2022 17:35:48 GMT | Engagement: Likes=0, Reposts=0, Quotes=0, Replies=0, Bookmarks=0, Views=N/A  
  Content: 在GETTR看 Jack Posobiec 🇺🇸直播  
  LIVE AT TPUSA TAMPA - TRUMP DESANTIS

- **[post:59]** ID: 1550169712948137984 | Author: @LizWillis_ | Timestamp: Thu, 21 Jul 2022 17:23:54 GMT | Engagement: Likes=60, Reposts=10, Quotes=0, Replies=5, Bookmarks=0, Views=N/A  
  Content: Headed to Tampa for @TPUSA Student Action Summit! Can’t wait to see everyone there!   
  #SAS2022 🇺🇸 ☀️

This exhausts all matching posts returned by the tool calls within the specified date range. The primary event referenced across multiple posts is the TPUSA Student Action Summit (#SAS2022 or SAS 2022) in Tampa, Florida, occurring that weekend (with attendees arriving/traveling on July 21, 2022, and references to Trump speaking there). No additional standalone Charlie Kirk solo speaking events were found in the results for the exact week.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2022-07-16 to 2022-07-22**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2022-07-16 to 2022-07-22 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**Airports named on this page:**

* [HEAR — El Arish International Airport](/Planes/Airports/HEAR), El Arish, Egypt — 3 recorded ground visits, 2 tracked aircraft

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 292 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
