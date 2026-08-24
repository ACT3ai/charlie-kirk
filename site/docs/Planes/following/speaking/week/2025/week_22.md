---
unlisted: true
title: "Week 22 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W22"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-05-28 to 2025-06-03."
status: completed
hide_table_of_contents: true
---

# Week 22, 2025

- Date range: 2025-05-28 to 2025-06-03
- Queried at (UTC): 2026-08-24T19:18:43Z
- Model: grok-4.3
- API status: completed
- Response id: 060731de-b5a2-9915-9a9e-01f0cbfc7f6a

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-05-28 to the end of the week 2025-06-03.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR event OR speak OR \"public speaking\" OR tour OR appearance OR campus OR rally) since:2025-05-28 until:2025-06-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA) (event OR speaking OR \"will be\" OR appear OR speak) since:2025-05-28 until:2025-06-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "posts about Charlie Kirk or TPUSA public speaking events, appearances, or where Charlie Kirk will speak or attend events between May 28 and June 3 2025",
      "limit": "10",
      "from_date": "2025-05-28",
      "to_date": "2025-06-04"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point\" OR \"Turning Point USA\" OR tpaction) (rally OR event OR speaking OR \"will speak\" OR appearance OR \"speaking event\" OR campus OR tour OR \"public event\") (Phoenix OR PHX OR Arizona OR AZ OR Biggs) since:2025-05-28 until:2025-06-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (event OR rally OR speaking OR speak OR appearance OR tour) since:2025-05-28 until:2025-06-04",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:tpusa (event OR rally OR speaking OR speak OR appearance OR tour) since:2025-05-28 until:2025-06-04",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:tpaction (event OR rally OR speaking OR speak OR appearance OR tour) since:2025-05-28 until:2025-06-04",
      "limit": "5",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA or Turning Point events, rallies, speaking appearances, where Charlie Kirk will be speaking or attending events May 28 to June 3 2025",
      "limit": "10",
      "from_date": "2025-05-28",
      "to_date": "2025-06-04"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1928854432818802864"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1928939297341919462"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1929598890111914054"
    },
    "status": "completed"
  },
  {
    "name": "x_thread_fetch",
    "input": {
      "post_id": "1928854432818802864"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Biggs for Governor\" OR \"Biggs For Governor\" OR \"Andy Biggs\" rally) (Charlie Kirk OR TPUSA OR TPAction OR \"Turning Point\") since:2025-05-28 until:2025-06-04",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "\"Women's Leadership Summit\" (TPUSA OR \"Turning Point\" OR \"Charlie Kirk\") since:2025-05-28 until:2025-06-04",
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
  "input_tokens": 44051,
  "input_tokens_details": {
    "cached_tokens": 24832
  },
  "output_tokens": 4113,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 48164,
  "num_sources_used": 0,
  "num_server_side_tools_used": 14,
  "cost_in_usd_ticks": 1092726500,
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
    "input_tokens": 20607,
    "output_tokens": 3419
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/Missy46/status/1927558110731739316",
    "start_index": 1087,
    "end_index": 1142,
    "title": "1"
  }
]
```

## Grok response

```text
**Here is all the relevant X (Twitter) data found for public speaking events or appearances by Charlie Kirk or TPUSA/TPAction within the exact date range May 28–June 3, 2025 (posts from May 28 to June 3 inclusive).** No summarization or filtering beyond the query scope; full post content, metadata, and context (where available via threads) are included verbatim. Only posts directly referencing or promoting such events/appearances were located after multiple targeted searches.

### Primary Event: Biggs for Governor Rally (Hosted by TPAction / Featuring Charlie Kirk)
- **Event details from posts**: Rally on **Saturday, May 31, 2025**, at the historic Biltmore Hotel and Resort in Phoenix, AZ (PHX, Arizona). Hosted by @tpaction. Featured speeches by Charlie Kirk, Andy Biggs (@andybiggs4az), and others including @BasedMikeLee, @EliCrane_CEO, @RepGosar, @sherifflamb1, @ByronDonalds, @BurgessOwens, @laurenboebert, @mattgaetz. Promoted as a major campaign kickoff event. Live streams and clips posted. Multiple references confirm Charlie Kirk spoke/appeared and hosted/promoted it.[[1]](https://x.com/Missy46/status/1927558110731739316)

**Full relevant posts (in chronological order where possible):**

- **Post [post:57]**: Author: Missy46 (@Missy46). Timestamp: Wed, 28 May 2025 02:50:40 GMT.  
  Content: "·Paid for by TURNING POINT PAC INC Andy Biggs is officially running for Governor, and the movement starts NOW. Join us for his official campaign kickoff rally with special guest Charlie Kirk. Trump-endorsed. Arizona First. Let’s go! 📷 Saturday, May 31 | 📷 3PM 📷 Phoenix, AZ"

- **Post [post:58]**: Author: Missy46 (@Missy46). Timestamp: Wed, 28 May 2025 02:50:08 GMT.  
  Content: "This just posted on FB. Charlie Kirk seems to believe Trump has endorsed Biggs. If so then her ads are misleading. Join the Biggs kickoff rally! Trump-endorsed Andy Biggs is kicking off his campaign. Be there May 31 — limited tickets remain. Book now Turning Point Action"

- **Post [post:36] / [post:48] / [post:49]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Sat, 31 May 2025 16:41:47 GMT.  
  Content: "🚨🚨TODAY: Join us for the Biggs for Arizona Rally hosted by @tpaction at the historic Biltmore Hotel and Resort in Phoenix, AZ. The future of Arizona starts TODAY. Tickets 👉https://www.tpaction.com/whyandybiggs @andybiggs4az @BasedMikeLee @EliCrane_CEO @RepGosar @sherifflamb1 @ByronDonalds @BurgessOwens @laurenboebert @mattgaetz"  
  Media: Photo of promotional graphic.  
  **Thread replies include**:  
  - @TheScoop_US (Sat, 31 May 2025 16:44:28 GMT): "@charliekirk11 Historic turnout in Phoenix! The America First movement is UNSTOPPABLE with champions like @andybiggs4az and @charliekirk1776 leading the charge. Liberals are shaking as Arizona patriots rise to save our state from Democrat disaster. The red wave starts NOW!"  
  - @jrl_josh (Sat, 31 May 2025 17:18:36 GMT): "People all over Arizona and the US want Andy Biggs for Governor of AZ. Karrin Taylor Robson should honorably step aside, and let Andy focus on beating Katie Hobbs."  
  - @KBinSC (Sat, 31 May 2025 16:57:59 GMT): "Turning point rallys are AMAZING"

- **Post [post:35] / [post:47]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Sat, 31 May 2025 22:19:01 GMT.  
  Content: "Turning Point Action Presents The Biggs For Governor Rally LIVE from PHX, AZ https://x.com/i/broadcasts/1kvJpyWWVdZxE"  
  **Thread replies include**:  
  - @TheScoop_US (Sat, 31 May 2025 22:19:33 GMT): "@charliekirk11 🔥 Andy Biggs & Charlie Kirk leading the charge in AZ! This rally is HUGE for taking back our state from radical Dems. Let’s secure a red wave in 2026 and Make Arizona Great Again! 🇺🇸."  
  - @OneXOneY (Sat, 31 May 2025 22:19:37 GMT): "Biggs rallying strong, real leadership coming to Arizona."  
  - @RealKeatonHobby (Sat, 31 May 2025 22:20:27 GMT): "Let's go! Biggs for Governor! Arizona is in for a special rally! Thank you Charlie!"

- **Post [post:33]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Sat, 31 May 2025 23:27:38 GMT.  
  Content: "“Andy has been a deeply principled conservative his whole life, and he’s fighting everyday to make America great. The American people speak, Andy listens.” -@RepGosar on Andy Biggs 🇺🇸 @tpaction"  
  Media: Video clip from the rally.

- **Post [post:34]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Sat, 31 May 2025 22:54:46 GMT.  
  Content: "“You delivered the White House to Donald Trump, and you’re going to deliver the Governor’s Mansion to Andy Biggs.” @mattgaetz’s full speech at @tpaction’s Biggs For Governor rally 🔥"  
  Media: Video clip from the rally.

- **Post [post:41]**: Author: Turning Point Action (@TPAction). Timestamp: Sat, 31 May 2025 22:19:39 GMT.  
  Content: "TPAction Presents The Biggs For Governor Rally LIVE from PHX, AZ https://twitter.com/i/broadcasts/1MYxNwppzlNKw"

- **Post [post:52]**: Author: Rachel Alexander (@Rach_IC). Timestamp: Sat, 31 May 2025 23:29:23 GMT.  
  Content: "Charlie Kirk speaking at the TPUSA rally for Andy Biggs for governor, is focusing on how Arizona is grand central for politics since Trump, highlighting the 2020 election where no one believed Biden won the state. Now thanks to all the hard work, Arizona was the best performing swing state in 2024. 🇺🇲🇺🇲🇺🇲🇺🇲"  
  Media: Photo.

- **Post [post:53]**: Author: Charlie Kirk (@charliekirk11). Timestamp: Sat, 31 May 2025 22:54:46 GMT (same as above, cross-referenced).  
  (Full content as listed in [post:34].)

- **Post [post:26]**: Author: $mokecheddathaassgetta (@Latino69Heat69). Timestamp: Mon, 02 Jun 2025 21:23:34 GMT.  
  Content: "Congressman Andy Biggs talks Trump, undoing Hobbs' work at Phoenix campaign rally Republican 'Little' Biggs focused on Trump at rally for his gubernatorial campaign. Rally hosted by conservative nonprofit Turning Point USA in his 1st major campaign event. https://www.kjzz.org/elections/2025-06-01/congressman-andy-biggs-biggs-talks-trump-undoing-hobbs-work-at-phoenix-campaign-rally"

- **Post [post:27] / [post:51]**: Author: PatriotTakes (@patriottakes). Timestamp: Mon, 02 Jun 2025 21:12:01 GMT.  
  Content: "During his rally for Andy Biggs, Charlie Kirk attacked John McCain, who passed away from cancer in 2018: “They were using the Republican name to get your support, but they weren’t actually going to DC to fight for your values.”"  
  Media: Video clip.

- **Post [post:29]**: Author: Sup Mario Bro (@SupMarioBro). Timestamp: Mon, 02 Jun 2025 17:00:52 GMT.  
  Content: "Arizona is so excited to get @andybiggs4az on the ballot to elect him as Arizonas next Governor! @tpaction had a tremendously successful rally on Saturday and the support is pouring in with petition signatures and donations. Thank you, Arizonans for making your voices heard! I received these screenshots on 𝕏 in support of Andy Biggs! Get some!!! 🇺🇸"  
  Media: Two photos.

- **Post [post:31]**: Author: Turning Point Action Coalitions (@TPACoalitions). Timestamp: Mon, 02 Jun 2025 01:10:59 GMT.  
  Content: ""Us moms, especially in Arizona, we deserve that. We deserve a governor who is going to protect our children, our family rights, but also protect our kids from being pawns in a crazy culture and political game that we are facing." @MrsErikaKirk speaking on why Moms are ralling behind Andy Biggs for governor of Arizona! Join the movement 👉"  
  Media: Video.

- **Post [post:32]**: Author: Kevin Stankiewicz, PE (@KevinStankiewi5). Timestamp: Sun, 01 Jun 2025 21:58:48 GMT.  
  Content: "I enjoyed the Biggs rally, but where were the 'Biggs for Arizona Governor' T-shirts and hats? I wanted one but I did not see any. Actually, can you make a nice 'Biggs for AZ Gov' polo shirt too, for more formal occasions or locations? I also volunteered but have not heard back."

- **Post [post:56]**: Author: The Scoop (@TheScoop_US). Timestamp: Fri, 30 May 2025 14:54:59 GMT.  
  Content: "@charliekirk11 Andy Biggs is surging with Charlie Kirk’s endorsement! 🚀 Arizona needs a fearless America First leader to secure the border, crush the left’s agenda, and make AZ the Florida of the West. Let’s rally behind Biggs and deliver a historic RED WAVE in 2026! 🇺🇸."

### Other Mentions of Events/Appearances
- **Women's Leadership Summit / Young Women’s Leadership Summit (YWLS2025)**: Promoted by TPUSA as an upcoming event (June 13-15, 2025, in Dallas, TX), with ticket sales active through early June. Multiple posts reference speakers including Charlie Kirk. No posts from the exact date range indicate it occurred within May 28–June 3.  
  **Relevant posts**:  
  - **Post [post:42] / [post:59]**: Author: Turning Point USA (@TPUSA). Timestamp: Mon, 02 Jun 2025 18:00:00 GMT.  
    Content: "We’re celebrating 10 incredible years of the largest conference for conservative women, and you’re invited! Now through June 6, use code '10YEAR' to get 40% off GA tickets to our Women’s Leadership Summit in Dallas, TX 💐 https://www.ywls2025.com?utm_source=social&utm_medium=x&utm_campaign=10year"  
    Media: Photo.  
  - **Post [post:60]**: Author: Rachel Farmer (@rachelfarm04). Timestamp: Sat, 31 May 2025 00:31:14 GMT.  
    Content: "LADIESSSS, DON’T MISS #YWLS2025! 🎀 Only 2 WEEKS until @TPUSA’s Young Women’s Leadership Summit, the BIGGEST event in the country for conservative ladies! ✨💅 REGISTER NOW ➡️ https://t.co/mwFZyN596O See YOU in Dallas! 🤠"  
    Media: Two photos.  
  - **Post [post:61]**: Author: Jonathan Shanks (@JonathanWShanks). Timestamp: Fri, 30 May 2025 13:12:04 GMT.  
    Content: "The Young Women’s Leadership Summit is TWO WEEKS AWAY! 💅🏻✨ Join hundreds of patriotic @tpusastudents at an exclusive @TPUSAEvents conference in Dallas! 🤠 Ask me how you can get your ticket for 50% off! 🤑 June 13-15 | https://t.co/AAEmvWd1rA @charliekirk11 @TPUSA #YWLS2025"  
    Media: Video.  
  - **Post [post:62]**: Author: Kelsey McCormick (@kelssmccormick). Timestamp: Fri, 30 May 2025 12:32:49 GMT.  
    Content: "Let's go girls!! 2 WEEKS until @TPUSA's Young Women's Leadership Summit! 🎀👠 You don't want to miss the largest gathering of conservative gals in the country! 💅🏽💄 REGISTER TODAY https://t.co/oy0BMaO1mA"  
    Media: Two photos.  
  - **Post [post:63]**: Author: Ashley Glasgow (@ashleyglasgow27). Timestamp: Thu, 29 May 2025 18:32:58 GMT.  
    Content: "The Young Women’s Leadership Summit is right around the corner - with speakers like @charliekirk11, @LilaGraceRose, @conservmillen, and @imbrettcooper. 📍 Dallas, TX 📅 June 13-15 🔗 Register now at: https://t.co/oU1uL3jtYE 🌷🌼💐🌻🌸🪻 @TPUSAEvents @TPUSA @tpusastudents"  
    Media: Four photos.

### Additional Context Posts (Indirect References)
- **Post [post:46]**: Author: The Gateway Pundit (@gatewaypundit). Timestamp: Mon, 02 Jun 2025 00:06:06 GMT.  
  Content: "SPLC Labels Turning Point USA as a “Hate Group”-Charlie Kirk Responds: “A cheap smear from a washed-up org that’s been fleecing scared grandmas for decades” https://www.thegatewaypundit.com/2025/06/splc-labels-turning-point-usa-as-hate-group/" (Mentions TPUSA but no new event.)

- **Post [post:38]**: Author: Defiant L’s (@DefiantLs). Timestamp: Wed, 28 May 2025 16:02:56 GMT.  
  Content: "Charlie Kirk holds nothing back after the Southern Poverty Law Center tries to label his TPUSA organization as a hate group: 'This is them trying to make us basically surrender at Turning Point USA. We're going to do the opposite.'"  
  Media: Video (no event details).

- **Post [post:21]**: Author: BelannF (@BelannF). Timestamp: Fri, 30 May 2025 14:55:12 GMT.  
  Content: "CHARLIE KIRK TELLS US WHY THIS COUNTRY IS SO DIVIDED. ... unlike Charlie Kirks meetings with students - He loves to hear what students who identify as Liberals have to say..."  
  Media: Video (general reference to Kirk's student meetings).

No other posts in the searches referenced additional public speaking events, tours, campus appearances, or scheduled locations for Charlie Kirk or TPUSA/TPAction specifically between May 28–June 3, 2025. All data pulled directly from X tools.
```

