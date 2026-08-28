---
unlisted: true
title: "Week 30 2025 Charlie Kirk / TPUSA speaking search"
sidebar_label: "2025-W30"
description: "Grok X-search dump for Charlie Kirk / TPUSA speaking posts 2025-07-23 to 2025-07-29."
status: completed
hide_table_of_contents: true
---

# Week 30, 2025

- Date range: 2025-07-23 to 2025-07-29
- Queried at (UTC): 2026-08-24T19:19:24Z
- Model: grok-4.3
- API status: completed
- Response id: 6facbcc0-8510-9dc2-bc75-6a15fb8205c7

## Query sent to Grok

```text
Search twitter and x.com posts for where Charlie Kirk or TPUSA has public speaking events or where Charlie will be and speak.  Look at posts between the week date range 2025-07-23 to the end of the week 2025-07-29.  Include all data. Don't summarize
```

## Grok X-search tool calls

```text
[
  {
    "name": "x_keyword_search",
    "input": {
      "query": "(\"Charlie Kirk\" OR TPUSA OR \"Turning Point USA\") (speaking OR speaks OR event OR events OR tour OR \"public speaking\" OR campus OR \"will be\" OR \"speaking at\" OR \"speaking in\") since:2025-07-23 until:2025-07-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:charliekirk11 (speaking OR event OR events OR tour OR \"will be\" OR campus) since:2025-07-23 until:2025-07-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_keyword_search",
    "input": {
      "query": "from:TPUSA (speaking OR event OR events OR tour OR \"will be\" OR campus) since:2025-07-23 until:2025-07-30",
      "limit": "10",
      "mode": "Latest"
    },
    "status": "completed"
  },
  {
    "name": "x_semantic_search",
    "input": {
      "query": "Charlie Kirk or TPUSA public speaking events, appearances, campus visits, or tour stops where Charlie Kirk will speak",
      "limit": "10",
      "from_date": "2025-07-23",
      "to_date": "2025-07-30"
    },
    "status": "completed"
  }
]
```

## Usage

```text
{
  "input_tokens": 8639,
  "input_tokens_details": {
    "cached_tokens": 3072
  },
  "output_tokens": 2433,
  "output_tokens_details": {
    "reasoning_tokens": 0
  },
  "total_tokens": 11072,
  "num_sources_used": 0,
  "num_server_side_tools_used": 4,
  "cost_in_usd_ticks": 336556500,
  "server_side_tool_usage_details": {
    "web_search_calls": 0,
    "x_search_calls": 4,
    "code_interpreter_calls": 0,
    "file_search_calls": 0,
    "mcp_calls": 0,
    "document_search_calls": 0,
    "image_generation_calls": 0
  },
  "context_details": {
    "input_tokens": 7049,
    "output_tokens": 2186
  }
}
```

## Annotations / citations

```text
[
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948808314705641847",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948808314705641847"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948546419738169492",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948546419738169492"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948065047030489581",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948065047030489581"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949947722099744946",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949947722099744946"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949969669470740864",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949969669470740864"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949970588619121048",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949970588619121048"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949963496709370156",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949963496709370156"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948614924445646876",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948614924445646876"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949954109508821074",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949954109508821074"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948480575788007665",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948480575788007665"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948717012135358503",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948717012135358503"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948453973633237147",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948453973633237147"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949972884861968608",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949972884861968608"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949977765412741148",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949977765412741148"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948395805209199090",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948395805209199090"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948173784021930004",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948173784021930004"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949979606750011401",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949979606750011401"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949967941455270187",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949967941455270187"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948789289728540932",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948789289728540932"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948411387237302316",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948411387237302316"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1948488390594245084",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1948488390594245084"
  },
  {
    "type": "url_citation",
    "url": "https://x.com/i/status/1949949917805568071",
    "start_index": 0,
    "end_index": 0,
    "title": "https://x.com/i/status/1949949917805568071"
  }
]
```

## Grok response

```text
**All relevant X posts from the date range July 23–29, 2025 (using `since:2025-07-23 until:2025-07-30` for the week), containing mentions of Charlie Kirk, TPUSA, or related events/speaking appearances.** No posts were found that announce or reference any specific upcoming or ongoing public speaking events, campus visits, tours, or appearances by Charlie Kirk or TPUSA during this exact week. The searches returned discussions, past events, media appearances, and unrelated commentary instead.

Here is every post retrieved (full, unedited content; sorted by tool results for completeness; no summarization or filtering applied beyond the search criteria):

**From general keyword search (`("Charlie Kirk" OR TPUSA OR "Turning Point USA") (speaking OR speaks OR event OR events OR tour OR "public speaking" OR campus OR "will be" OR "speaking at" OR "speaking in")` since:2025-07-23 until:2025-07-30, Latest mode):**

- [post:0] @JohnnyP82597 (Mon, 28 Jul 2025 23:45:41 GMT): "Charlie Kirk was and always will be a fucking Israeli shill. His entire fucking career was backed by Jewish money theyinfiltrate and subvert the conservative movement in America to perpetuate the continued theft of American taxpayer dollars to support the Jews and their genocide"

- [post:1] @grok (Mon, 28 Jul 2025 23:38:22 GMT): "MarkVanDrie The trans activist was detained for vandalism at UC Berkeley's TPUSA event in October 2024 after throwing tomato juice on students and materials. Chloe Cole pressed charges. She was arrested, but received two years probation with the felony dropped."

- [post:2] @Spring177542202 (Mon, 28 Jul 2025 23:18:59 GMT): "Yes, Israel literally IS starving Palestinians in Gaza. It's documented and they will be prosecuted for war crimes. The death penalty would be too nice for these psychos. Charlie "I work for Israel" Kirk is a foreign agent and as is his organization TPUSA."

- [post:3] @tpusafaith (Mon, 28 Jul 2025 23:09:51 GMT): "Lila Rose shares a powerful reminder to every pastor: politics matter. Join @LilaGraceRose and other great voices at the Faith Forward Pastors' Summit, happening August 6–8 in Los Angeles, CA. This event is open to all pastors and ministry leaders who are ready to stand for truth in today’s culture. 📍Register now at" (includes video media)

- [post:4] @grok (Mon, 28 Jul 2025 23:06:12 GMT): "Yes, Charlie Kirk has visited the Western Wall in Jerusalem, including during his 2023 Israel tour where the itinerary featured the site and its tunnels. He's a vocal supporter of Israel."

- [post:5] @Actuator1776 (Mon, 28 Jul 2025 22:59:20 GMT): "This will be the end of TPUSA and Charlie will have no choice but to join Fox News and repeat the narratives."

- [post:6] @CitizenRoark (Mon, 28 Jul 2025 22:41:40 GMT): "And you are aware it will be overturned in the end. I mean we’ve seen this episode play out over and over. Yet you still go online and plant a flag of victory? Hmmm yeah funny how alll those flags get quietly removed a few weeks later after you dems get your asses put in place."

- [post:7] @RoverUSA10 (Mon, 28 Jul 2025 22:04:22 GMT): "Speaking like this about another countries, mayor is a damn disgrace. And then you have this fucking Charlie Kirk, who pretends to be a great Christian looking down on a man just because he's Muslim ! Kirk is a loser"

- [post:8] @eddiejillete (Mon, 28 Jul 2025 21:47:43 GMT): "Multimillionaire Tucker Carlson stating opinions on a Podcast that he does from home or at TPUSA event are not acts of bravery."

- [post:9] @LibsRFullRetard (Mon, 28 Jul 2025 21:38:59 GMT): "How did it do it? Like practically speaking?"

**From Charlie Kirk's account search (`from:charliekirk11 (speaking OR event OR events OR tour OR "will be" OR campus)` since:2025-07-23 until:2025-07-30, Latest mode):**

- [post:10] @charliekirk11 (Thu, 24 Jul 2025 15:54:09 GMT): "Hulk Hogan was a genuine, uniquely American creation. Fearlessly original. Flawed but unbowed. He had the courage to stand on his own principles, and he never stopped fighting for his country. An American icon. He will be missed." (includes video media)

- [post:11] @charliekirk11 (Thu, 24 Jul 2025 14:52:14 GMT): "🚨DNI Tulsi Gabbard will be LIVE on The Charlie Kirk Show today at 12:30PM ET. Watch it here on 𝕏 or Rumble ⬇️ https://rumble.com/CharlieKirk Subscribe to The Charlie Kirk Show ⬇️ https://podcasts.apple.com/us/podcast/the-charlie-kirk-show/id1460600818" (includes photo media)

- [post:12] @charliekirk11 (Thu, 24 Jul 2025 00:10:00 GMT): "These are citical executive orders. This ensures that just like the modern economic order was built upon the US financial system, the future of AI will be built upon American AI models — and they won't be woke. Difficult to overstate just how critical this could prove to the future of humanity." (quoted post about Trump AI executive orders; includes video media)

**From TPUSA account search (`from:TPUSA (speaking OR event OR events OR tour OR "will be" OR campus)` since:2025-07-23 until:2025-07-30, Latest mode):** No results found.

**From semantic search (relevant posts mentioning events/appearances in the date range):** 

- [post:13] @FuentesUpdates (Fri, 25 Jul 2025 05:22:56 GMT): "Antisеmitism went mainstream and people don't want to support Israel anymore. In response to this, Charlie Kirk is holding struggle sessions at TPUSA to moderate what the students are saying." (includes video media)

- [post:14] @AFpost (Thu, 24 Jul 2025 20:29:04 GMT): "Charlie Kirk hosted a “focus group” with TPUSA student leaders where he encouraged allowing moderate criticism of Israel to prevent broader “Jew hate.” Follow: @AFpost"

- [post:15] @Phil_Johnson_ (Fri, 25 Jul 2025 16:55:48 GMT): "5-6 September 2025 I'll be at the Cornerstone Conference in Daytona Beach, with Todd Friel, Ken Ham, Virgil Walker, Tom Ascol, HB Charles, Dr. Stephen Nichols, and Christopher Johnson. Come if you can. Daytona's Peabody Auditorium. https://www.wjlu.org/conference" (includes photo media; unrelated to Charlie Kirk/TPUSA)

- [post:16] @Quadcarl (Fri, 25 Jul 2025 12:08:35 GMT): "Next Friday (August 1st) I will be speaking at a rally when I arrive at the State Capitol in Madison at noon. I hope to see you there." (includes video media; unrelated)

- [post:17] @charliekirk11 (Thu, 24 Jul 2025 18:43:22 GMT): "There is no denying that Israel has become a massive topic in U.S. politics, and particularly among Gen Z. At our recent Student Action Summit, I hosted a focus group with our TPUSA students to get a sense of what they think about the topic. As you'll see, they don't hate Israel or Jewish people, but they are skeptical about the state of America's current relationship with the country, and they want to be confident America's leaders are putting their own country first. I have been working hard to help conservative politicians, donors, and friends of Israel better understand this dynamic. Now, in a conversation that is sure to frustrate both sides of the discussion, they can hear Gen Z conservatives in their own words. @TPUSA" (includes video media; references a past/recent Student Action Summit)

- [post:18] @charliekirk11 (Wed, 23 Jul 2025 16:57:55 GMT): "A quick personal update: I’ll be guest hosting Fox & Friends this weekend! Tune in at 6am eastern Saturday & Sunday as I join my good friends Rachel campos-Duffy and Charlie Hurt. @RCamposDuffy @CharlesHurt https://www.axios.com/newsletters/axios-am" (includes photo media; media appearance, not public speaking event)

- [post:19] @charliekirk11 (Fri, 25 Jul 2025 18:11:23 GMT): "TPUSA's Student Action Summit 2025 vs. DNC's Voters of Tomorrow Summit 2025" (includes 2 photos media)

- [post:20] @NickJFuentes (Thu, 24 Jul 2025 21:00:08 GMT): "Charlie Kirk just hosted a struggle session with teenagers to get them to admit they aren’t “antisemitic Jew Haters.” They are trying so hard to put a lid on the noticing and control the narrative but it’s already too late."

- [post:21] @UnderhillVicky (Fri, 25 Jul 2025 00:50:43 GMT): "If you are in anywhere near Waco/Crawford so see the next Governor of Texas. @DocPeteChambers will be speaking at this meeting on Saturday." (includes photo media; unrelated)

No additional posts matched the criteria across the searches. All content is presented exactly as retrieved.
```


---

{/* CK_NEW_EVIDENCE_LINKS:START */}

## Flight-record pages for what is on this page

This investigation keeps one page per airport and one page per recorded ground contact, built directly from the recovered ADS-B traces. These are the ones that fall inside **2025-07-23 to 2025-07-29**, the range this page covers.

**No tracked aircraft was on the ground near a sourced event in this window.** Across 2025-07-23 to 2025-07-29 the recovered traces record no contact. That is a coverage statement as much as anything — see the limits on the linked pages.

**The two indexes:**

* [Every airport in this investigation](/Planes/Airports/overview) — 290 fields, each with its complete recovered ground-visit and flight-leg record
* [Every interesting date, all aircraft](/Planes/Incidents/overview) — 147 ground contacts near a sourced event, across 110 pages
* [Investigating Deleted Flights](/Planes/investigating_deleted_flights) — how the data was recovered, how much of it we hold, and where it is still missing

{/* CK_NEW_EVIDENCE_LINKS:END */}
