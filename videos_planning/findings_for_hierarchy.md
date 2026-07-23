findings_for_hierarchy.md — VIDEO PIPELINE FINDINGS

Written by videos_planning/p_update_video_hierarchy.md, run 2026-07-23.
This is the human work list. Everything here is something a person has to
decide or do; nothing in it is fixed by re-running the pipeline.

==========================================================================
1. THE CENSUS IN THE PROMPT IS WRONG BY 8x — READ THIS FIRST
==========================================================================

p_update_video_hierarchy.md's KNOWLEDGE section says the corpus is 'on the
order of 55-65 video entries' and warns that 'if the rebuilt YAML has
hundreds of video entries, something is wrong'. It is 400, and nothing is
wrong. The census counted the repo corpus and skipped the mirror.

  ~/_Mirror/Politics/Charlie_Kirk_Mi   325 video files, 20.3 GB, across 71
                                       concept-filed directories
  ALL 325 are fully processed: 325 .transcription, 322 .ai_description,
  325 .ocr. Not one is missing a sidecar.

The mirror is the LARGEST and BEST-DOCUMENTED part of the video corpus, and
its directory names are years of hand filing by concept — the strongest
clustering signal this pipeline has. The prompt's own Stage 2 lists it as
source 5, so it was included. Update the census section of the prompt so the
next run does not treat 400 entries as a bug.

Other census corrections measured on disk:
  * videos/ holds 49 .mp4, not 46.
  * 4 disk files have no manifest record, not 1: 2026310419405504514.mp4,
    2038934507307343872.mp4, _QwGo0LyZ3I.mp4, kirk-parents-hearing-3006.mp4.
  * The 18 manifest-records-with-no-disk-file figure is exactly right.

==========================================================================
2. videos/manifest.yaml WAS NOT VALID YAML — FIXED
==========================================================================

Line 402 read:
    description: 'Erika Kirk takes the torch after Charlie's assassination'
An apostrophe inside a single-quoted YAML scalar must be doubled. The file
would not parse at all, so no stage that reads the manifest could run. It is
now:
    description: 'Erika Kirk takes the torch after Charlie''s assassination'
This is the only edit this run made outside videos.yaml and this directory.
Whatever writes manifest.yaml (the /ck_add_text skill) should quote-escape.

==========================================================================
3. THE .ocr FORMAT, RECORDED (Stage 1 asked for this)
==========================================================================

An .ocr sidecar is a YAML document, NOT bare text. Keys observed on all 327:
  source, status, engine, level, generated, kind, language, stride_seconds,
  frames_sampled, truncated, text, blocks
`text` is a block scalar holding every sampled frame's glyphs concatenated.
`blocks` is a list of {text, confidence, start, end} with per-frame timing —
so OCR carries TIMESTAMPS, which the prompt did not know. For a screen-
recorded post, blocks[].start/end is a second source of timing alongside the
ai_description shot list. Worth harvesting on a later pass.

Two ai_description formats also differ from the prompt's description:
  * The twelve ## sections are NOT always in the documented order.
    Parse by header name, never by position.
  * Some sidecars open with a preamble line before ## Overview
    ('Certainly! Here is a hyper-detailed factual description...').
    A parser that takes everything before the first ## as the overview gets
    the preamble instead.
  * Shot-list bullets use both '* **00:00 - 00:10**' and '- **00:00**:'.

==========================================================================
4. TRANSCRIPTION WORK LIST — 34 videos with no transcription of any kind
==========================================================================

Neither the video nor an audio sibling has a .transcription. Until these are
run through Large File Bridge they cannot be clustered or placed on evidence,
and this run placed them structurally or not at all.

  * 1965869689755812061                                                none
  * 1965871960702828885                                                none
  * 1965884012565766172                                                none
  * 1965890646746513821                                                none
  * 1965892000185725129                                                none
  * 1965913654840406034                                                none
  * 1966235480732873149                                                none
  * 1966293765158560167                                                none
  * 1969832388823003519                                                none
  * 2026310419405504514.mp4                                            video
  * 2038934507307343872.mp4                                            video
  * 2069185145555255370_source                                         none
  * 2075691199575265757                                                none
  * 2076465128329846991                                                none
  * 2079560806690324910.mp4                                            video
  * 2079684519762993659.mp4                                            video
  * kirk-parents-hearing-3006.mp4                                      video
  * site/QmedrrPge7Bj8vUN6xxq1Zfz1CgwuY6xGAtWFFbU4tmg4R                none
  * yt/0pvEGO4W85k                                                     none
  * yt/0ykbt_WGOZE                                                     none
  * yt/1RbDMiEReys                                                     none
  * yt/1xTpQ9RHkvk                                                     none
  * yt/2exo7iJ-qdc                                                     none
  * yt/8HkNMTNHsa8                                                     none
  * yt/J2DKRfwSt94                                                     none
  * yt/PLnZT7Gz_VSN520UilgmZqikvi3n1MsuZR                              none
  * yt/PLuXXbBFpPc0lhc6PfJae8Rav-gMNpmeuL                              none
  * yt/X8UKjN5cjvw                                                     none
  * yt/ccRNaLGavf8                                                     none
  * yt/qpGPZHdil1E                                                     none
  * yt/v6yrnyo                                                         none
  * yt/v705uyi                                                         none
  * yt/w-ng95XlQb4                                                     none
  * yt/wcD2khO3rOA                                                     none

PARTIAL TRANSCRIPTS — 38 videos. The ASR stopped before the end of the media
(the header's '✓ full' marker is absent), so transcript_complete is false.
These are the dangerous ones: a page written from one of them confidently
describes a video it only heard part of. Re-run them.

  * 2046416264562921472.mp3
  * 2070615710003589174.mp4
  * 2071072788132118610.mp4
  * 2077277163053564059.mp4
  * 2077951056697331723.mp4
  * 2077994177216827578_1.mp4
  * AES_Interview.mp4
  * AES_Interview_compressed.mp4
  * Blue_Side.mp4
  * Candace Owens - 🚨BREAKING NEWS!🚨 On September 10th, after Charlie’s assasi
  * Damin Toell - oh no [2036081362869030912].mp4
  * Darth Powell - If you think Charlie Kirk was shot with a 30-06  You're a f
  * Diligent Denizen 🇺🇸 - ‼️🇺🇸： Google Trend searches for TYLER JAMES ROBINSON
  * Drone_Shot_South.mp4
  * French Legionaire.mp4
  * Funneral.mp4
  * HustleBitch - 🚨 THEY WERE MUCH CLOSER THAN YOU THINK - WATCH AND PAY ATTEN
  * Jason Cain - I believe I have found the #CharlieKirk #Sniper shooting loca
  * Jason Cain - I believe I have found the #CharlieKirk #Sniper shooting loca
  * MJTruthUltra - UPDATE： Charlie Kirk  Candace Owens latest finding about th
  * MJTruthUltra - UPDATE： Charlie Kirk  Candace Owens latest finding about th
  * Marissa - Absolute proof he was not shot! [2075401619152539648].mp4
  * Mr Commonsense - @shaunmmaguire Newly Discovered Crowd Video Of A Man CELE
  * Muppet Masher - It comes from under his shirt. I don't know what else to s
  * Project Constitution - 🚨ALERT： BREAKING Down The MYSTERY FLIGHT BEFORE CHA
  * Project Constitution - 🚨Breaking： Newly Uncovered Footage Appears to Show 
  * RAW_CIA_Drones.mp4
  * SU_BBT.mp4
  * Shaun Maguire - Of all the videos of people celebrating the assassination 
  * South_Side.mp4
  * South_Side_Stairs.mp4
  * Tyler_Running.mp4
  * US_did_ 911 - @jonaaronbray Okay, the official narrative is BS. That has b
  * YREFY Laine Schoneberger.mp4
  * _MvCUbhcVsUi8L9G [_MvCUbhcVsUi8L9G].mp4
  * https%3A%2F%2Fx.com%2FProjectConstitu%2Fstatus%2F1999947478901088281.mp4
  * roofshooter3.ia.mp4
  * roofshooter3.mp4

NO AI DESCRIPTION — 44 videos.

  * 1965869689755812061
  * 1965871960702828885
  * 1965884012565766172
  * 1965890646746513821
  * 1965892000185725129
  * 1965913654840406034
  * 1966235480732873149
  * 1966293765158560167
  * 1969832388823003519
  * 2026310419405504514.mp4
  * 2038934507307343872.mp4
  * 2046414464447287296.mp3
  * 2046416264562921472.mp3
  * 2046416264567140352.mp3
  * 2068463186668605858.mp3
  * 2069185145555255370.mp3
  * 2069185145555255370_source
  * 2071736376215920842_extracted.mp3
  * 2072814926133866634.mp3
  * 2075691199575265757
  * 2076465128329846991
  * 2079560806690324910.mp4
  * 2079684519762993659.mp4
  * Project Constitution - 🚨 BREAKING： UNDENIABLE PROOF OF MULTIPLE SHOOTERS I
  * Teacher_Lounge_Shooter.mp4
  * Yes, Still MORE DISTURBING Searches from before Charlie Kirk Passed [tA7GE
  * kirk-parents-hearing-3006.mp4
  * site/QmedrrPge7Bj8vUN6xxq1Zfz1CgwuY6xGAtWFFbU4tmg4R
  * yt/0pvEGO4W85k
  * yt/0ykbt_WGOZE
  * yt/1RbDMiEReys
  * yt/1xTpQ9RHkvk
  * yt/2exo7iJ-qdc
  * yt/8HkNMTNHsa8
  * yt/J2DKRfwSt94
  * yt/PLnZT7Gz_VSN520UilgmZqikvi3n1MsuZR
  * yt/PLuXXbBFpPc0lhc6PfJae8Rav-gMNpmeuL
  * yt/X8UKjN5cjvw
  * yt/ccRNaLGavf8
  * yt/qpGPZHdil1E
  * yt/v6yrnyo
  * yt/v705uyi
  * yt/w-ng95XlQb4
  * yt/wcD2khO3rOA
==========================================================================
5. IPFS: 337 of 395 CIDs ARE NOT PINNED — EVERY ONE PUBLISHES AS A DEAD PLAYER
==========================================================================

This is the single biggest obstacle to publishing the video hierarchy at all.
The site plays video from public IPFS gateways; an unpinned CID is served by
no gateway. It plays perfectly on this machine because the local node has the
blocks, and an IPFS Companion browser extension will make it look fine here
too — and it is dead for every visitor.

  pinned:      58  (essentially just the videos/ corpus from manifest.yaml)
  NOT pinned:  337  (essentially the entire mirror)

NOTHING WAS PINNED BY THIS RUN, deliberately. Pinning announces content to
the public IPFS network and is irreversible in practice. Pinning the mirror
would publish 20 GB of material that has never been reviewed for what it
contains — bystander faces, uninvolved voices, private captures. That review
is the prerequisite, and videos_planning/exclude_videos.txt is where its
output goes. Any pinning job MUST filter every entry in that file first.

17 entries have no CID at all and cannot be published with a player:
  * 2071736376215920842_extracted.mp3                            x
  * yt/0pvEGO4W85k                                               youtube
  * yt/0ykbt_WGOZE                                               youtube
  * yt/1RbDMiEReys                                               youtube
  * yt/1xTpQ9RHkvk                                               youtube
  * yt/2exo7iJ-qdc                                               youtube
  * yt/8HkNMTNHsa8                                               youtube
  * yt/J2DKRfwSt94                                               youtube
  * yt/PLnZT7Gz_VSN520UilgmZqikvi3n1MsuZR                        youtube
  * yt/PLuXXbBFpPc0lhc6PfJae8Rav-gMNpmeuL                        youtube
  * yt/X8UKjN5cjvw                                               youtube
  * yt/ccRNaLGavf8                                               youtube
  * yt/qpGPZHdil1E                                               youtube
  * yt/v6yrnyo                                                   rumble
  * yt/v705uyi                                                   rumble
  * yt/w-ng95XlQb4                                               youtube
  * yt/wcD2khO3rOA                                               youtube

==========================================================================
6. WHERE THE INVESTIGATION HAS NO VIDEO COVERAGE AT ALL
==========================================================================

The tree mirrors the whole site on purpose, so the empty nodes are a real
research output: they are the parts of the investigation with no footage.
1,389 of 1,559 nodes are empty and carry publishable: false.

THESE LEVEL 2 SECTIONS HAVE ZERO VIDEO IN THE ENTIRE CORPUS:

  * After Events                                 After
  * Analysis and Documentation                   analysis_documentation
  * Campus and University                        campus_university
  * Companies & Organizations                    Companies_Organizations
  * Electrocution — The B-Field Resonant Cascade Electrocution
  * Government Evidence                          gov
  * Government Organizations                     government_organizations
  * Key Individuals                              key_individuals
  * Legal                                        Legal
  * Legal Investigation                          legal_investigation
  * Motive                                       Motive
  * Narrative                                    Narrative
  * New Laws (Fix)                               Fix
  * Organizations and Groups                     organizations_groups
  * Political Context                            political_context
  * Proof Intel Services                         Proof_Intel_Services
  * Proof Not Tyler                              Proof_Not_Tyler
  * Property & Locations                         Locations
  * Security and Law Enforcement                 security_law_enforcement
  * Social Media Analysis                        social_media_analysis
  * Suspicious                                   Suspicious
  * Technology and Surveillance                  technology_surveillance
  * The Laws                                     laws
  * Tyler Robinson Not Assassin                  Tyler_Robinson_Not_Assassin
  * Vote                                         Vote
  * Your Actions Fix It                          Your_Actions_Fix_It

publishable: false MUST BE HONOURED by p_yaml_to_site.md and
p_level2_update.md. Generating a page per node would add ~1,389 empty
'Videos -> FBI -> Search Warrants' pages that say nothing and hand a visitor
arriving from a topic page a dead end where they expected footage.

==========================================================================
7. should_be_on_pages FAILS TWO OF THE FOUR ACCEPTANCE TARGETS — READ WHY
==========================================================================

  measured                       target            result
  should_be_on_pages == []       5%-25%            33%   FAIL (too many empty)
  >= 1 page                      >= 75%            66%   FAIL (too few placed)
  >= 2 pages                     >= 20%            44%   PASS
  on_pages == [] for all         must not be 100%   no    PASS

THIS WAS NOT TUNED TOWARD THE BAND, AND SHOULD NOT BE. Hand audits of ten
randomly sampled proposals were run against four successive configurations:

  config                                          hand-audited precision
  lexical scoring, images-pipeline rules                 4/10
  + distinctive-token gate, evidence floor               (same misses)
  + claim-vs-scene token split                           2/10
  + two-distinctive-title-tokens, cluster binding        5/10   <- shipped

Loosening the gates to reach 75% coverage puts the precision back at 2-4/10,
i.e. it manufactures publishing instructions that a human then has to undo on
live pages. The prompt itself says a weak topical match is worse than none.
So the shipped configuration is the precise one, and the coverage gap is
reported here as work rather than hidden by relaxing a threshold.

WHY VIDEO SCORES WORSE THAN THE IMAGES PIPELINE (which hand-audited 65-70%):

  Roughly half this corpus is RAW EVENT FOOTAGE, not commentary. A clip of
  the UVU crowd has a long transcript — hundreds of words of ambient chatter,
  'Whoo! USA! USA!' — which is high-volume and topically empty. Against 1,495
  pages that are all about the same event, that noise always finds something
  to match. An image never had this failure mode: a photo with nothing in it
  produced a short description and scored low, whereas ambient audio produces
  a LONG transcript and scores high.

  The fix that worked was to stop trusting per-video text and trust the
  CLUSTER instead. The cluster map in build_tree.py was authored by hand from
  the mirror's own concept directories, and a cluster name states what its
  footage is about far more reliably than one clip's transcript. 36 of 126
  corpus clusters bound to a specific site page this way; the remaining 90
  are the top of the work list below.

HOW TO ACTUALLY RAISE COVERAGE — three things, in order of value:

  a) BIND THE REMAINING 90 CORPUS CLUSTERS TO SITE PAGES BY HAND. This is
     ~90 decisions, each covering several videos, and each far more reliable
     than a per-video guess. Add them as an explicit table in
     generator/plan_should_be.py next to CLUSTER_PAGE.
  b) CREATE THE MISSING PAGES. 429 assignments were dropped because their
     target page already held six videos. A page over the cap is a page that
     wants a child page — see section 8.
  c) TRANSCRIBE THE 33. Section 4.
==========================================================================
8. WANTED PAGES THAT DO NOT EXIST (pages over the six-video load)
==========================================================================

429 planned placements were dropped because the target page was already
carrying six videos. Each of these is a concept with more footage than one
page should hold — i.e. a page that wants child pages under it. Creating them
is the cleanest way to raise video coverage on the site.

Ranked by how much footage is queued behind them (overflow count):

    9 videos  site/docs/Narrative/Shot_in_the_heart.mdx
    6 videos  site/docs/People/donald-trump.mdx
    6 videos  site/docs/Suspects/Black_Clothing_Suspect.mdx
    6 videos  site/docs/Suspicious/UVU_9_10/all-black-construction-worker.mdx
    6 videos  site/docs/FBI/Kash_Patel_Briefings.mdx
    6 videos  site/docs/Israel_Main_Suspect/charlie-said-israel-would-kill-him.mdx
    6 videos  site/docs/People/hunter-kozak.mdx
    6 videos  site/docs/distraction_people/George_Zinn.mdx
    6 videos  site/docs/Influencers/podcasts-megyn-kelly.mdx
    6 videos  site/docs/People/blake-bednarz.mdx
    6 videos  site/docs/Suspicious/Cause_of_Death/entrance-or-exit.mdx
    6 videos  site/docs/Suspicious/Cause_of_Death/shirt-before-blood.mdx
    6 videos  site/docs/UVU/CIA-UVU-Profiles.mdx
    6 videos  site/docs/US_Intelligence/cia.mdx
    6 videos  site/docs/TPUSA/TPUSA_Opposite_Charlie.mdx
    6 videos  site/docs/Censorship/Censorship_Investigation_Index.mdx
    6 videos  site/docs/Influencers/podcasts-project-constitution.mdx
    6 videos  site/docs/Influencers/x/project-constitution.mdx
    6 videos  site/docs/Suspicious/UVU_9_10/rick-cutler-hand-device.mdx
    6 videos  site/docs/Suspicious/Defense_Attorneys/parents-declined-attorneys.mdx
    6 videos  site/docs/Tent/Platform_Water_Bottles.mdx
    6 videos  site/docs/Drones/Butler_PA_Drone_Parallel.mdx
    6 videos  site/docs/Influencers/podcasts-dave-smith.mdx
    6 videos  site/docs/Suspicious/UVU_9_10/stairs-guy-backpack.mdx
    6 videos  site/docs/Security_Team/next-event-no-plan.mdx
    6 videos  site/docs/Gov_Mind_Control/mkultra-program.mdx
    6 videos  site/docs/Mic/rode-wireless-mic.mdx
    6 videos  site/docs/distraction_people/Pellet_Gun_Man.mdx
    6 videos  site/docs/Killer/Close_Range_Theories.mdx
    6 videos  site/docs/Planes/N1098L/overview.mdx
    6 videos  site/docs/Suspicious/TPUSA_Peripheral/schoneberger-yrefy-sponsor.mdx
    6 videos  site/docs/Influencers/podcasts-patrick-bet-david.mdx
    5 videos  site/docs/Locations/Washington_County_Sheriff.mdx
    5 videos  site/docs/Suspicious/FBI/patel-shut-down-kent-probe.mdx
    5 videos  site/docs/court/mirandize/baron-coleman-early-turn-in.mdx
    5 videos  site/docs/Timeline/rental-cars-vehicle-movements-timeline.mdx
    5 videos  site/docs/distraction_people/Hunter_Kozak.mdx
    5 videos  site/docs/Israel/threat-to-western-politicians-iran-war.mdx
    5 videos  site/docs/Fix/Churches.mdx
    5 videos  site/docs/Suspicious/Trial_Legal/uncalled-roof-eyewitness.mdx

==========================================================================
9. BYTE-IDENTICAL DUPLICATE FILES IN THE MIRROR
==========================================================================

12 files are byte-for-byte copies of another file already in the corpus —
same CID, different name ('Jesse_ON_FIRE', '... copy', '... copy 2'). They
are one video, not several, so the duplicate is folded into its twin and its
path recorded in the surviving entry's duplicate_paths. Nothing was deleted
from disk. Worth cleaning up in the mirror itself:

  keep  1965892000185725129
    dup 1965913654840406034
  keep  Double_Shot.mp4
    dup Front_Left_Camera.mp4
  keep  FINAL_CIA_Drones.mp4
    dup v3 New CIA Video.mp4
  keep  Jesse_ON_FIRE.mp4
    dup Jesse_ON_FIRE copy.mp4
    dup Jesse_ON_FIRE copy 2.mp4
  keep  10_Drones.mp4
    dup Crowdsource The Truth - These unknown flying objects were record
  keep  Project Constitution - TPUSA's Tyler Bowyer DOUBLY EXPOSED – Birth
    dup Project Constitution - 🚨 BREAKING： NEW DRONE FOOTAGE  From The T
  keep  James Li - 🚨 Meet Skyler Baird — he is the “eyewitness” who： - app
    dup James Li - 🚨 Meet Skyler Baird — he is the “eyewitness” who： - a
  keep  10_Pellet_Gun.mp4
    dup War Reporter - 🚨 BREAKING： The alleged shooter of Charlie Kirk h
  keep  SU_BBT.mp4
    dup Candace Owens - 🚨BREAKING NEWS!🚨 On September 10th, after Charli
  keep  12.ia.mp4
    dup 13.ia.mp4
  keep  4k_60fps_from_South.mp4
    dup 4K_South_High_Res_Close_60fps.mp4

==========================================================================
10. SCHEMA ADDITIONS THIS RUN MADE
==========================================================================

Beyond the expanded schema the prompt specifies, one optional property was
added because the corpus needed it:

  duplicate_paths   list of other files on this machine whose bytes are
                    identical to this entry's. [] when there are none. See
                    section 9. Without it, folding a duplicate would lose the
                    record that the second file exists.

_key MINTING NOTE. The prompt says to prefer a site section's page_key from
pages.csv 'when it is free'. None are free — pages.csv already uses every one
of them for the site page the node MIRRORS. So every node key in videos.yaml
carries a Vid_ prefix (Vid_FBI, Vid_Exploding_Microphone, ...). That keeps
_keys unique file-wide AND collision-free against pages.csv when the video
pages are eventually added to it. The node records the page it mirrors in
site_page / site_level_2, which is what Stage 9's merge actually needs.

==========================================================================
11. on_pages SUBTRACTIONS (recorded, per the union rule)
==========================================================================

should_be_on_pages is a SUPERSET of on_pages. 10 observed placements were
deliberately NOT carried into the plan, each with its reason:

  * 1965869689755812061                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_5.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1965871960702828885                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_3.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1965884012565766172                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_8.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1965890646746513821                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_2.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1965913654840406034                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_7.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1966235480732873149                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_4.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1966293765158560167                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_6.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 1969832388823003519                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_9.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * 2076465128329846991                          -> site/docs/Photos/Official_Narrative/Narrative_Shot_in_the_Heart/Img_Photo_Narrative_Shot_in_the_Heart_1.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target
  * site/QmedrrPge7Bj8vUN6xxq1Zfz1CgwuY6xGAtWFFb -> site/docs/Photos/Mic/Img_Photo_448e0d.mdx
      reason: the page is under site/docs/Photos — the images pipeline's output, which Stage 13 may not target

Note what those subtractions reveal: the IMAGES pipeline has placed VIDEO
CIDs on pages under site/docs/Photos. Those are videos filed as images. Worth
a look from the images side — this pipeline may not touch /Photos.

==========================================================================
12. STAGE 12 IS CORRECTLY EMPTY
==========================================================================

video_page is "" on all 400 entries. site/docs/Videos holds only overview.mdx
and buckley-carlson-kash-patel-valhalla.mdx, neither of which carries the
ck_video_cid frontmatter the binding matches on. Both are PROTECTED hand-
written pages and were not guessed at by filename. video_page fills in once
p_yaml_to_site.md generates the Level 5 pages and stamps them.

==========================================================================
13. WHAT THE NEXT RUN SHOULD DO FIRST
==========================================================================

  1. Fix the census section of p_update_video_hierarchy.md (section 1 here).
  2. Review the mirror for publishability, fill exclude_videos.txt, and only
     then consider pinning. 337 unpinned CIDs is the gate on the whole
     hierarchy going live.
  3. Hand-bind the 90 unbound corpus clusters to site pages (section 7a).
  4. Transcribe the 33, re-run the 38 partials (section 4).
  5. Harvest blocks[].start/end timing out of the .ocr sidecars (section 3).

## Stage 3 write-up findings

### agent_06

* Vid_4k_Full_56bSKCp - transcript AND ai_description both describe a Michigan House Election Integrity Committee hearing (Lansing, HOUSE TV stamp 06/03/25), not UVU footage. Entry is unverifiable as filed; media needs opening.
* Vid_Ryne_Simmons_bPUC272 - ai_description identifies the event footage as the July 2024 Butler PA rally; its own on-screen text list reads "THE AMERICAN COMEBACK TOUR" (UVU, Sept 10 2025).
* Vid_Short_Video_Clip_Captures_qzHCQmC, Vid_Short_Video_Clip_Captures_s4Sc3Ex, Vid_Video_Captures_Live_Outdoor_qNoKV2w, Vid_Video_Captures_Chaotic_Scene_2GZEXPr - ai_descriptions name the seated Prove Me Wrong speaker as Steven Crowder; it is Charlie Kirk.
* Vid_Short_Raw_Documentary_Style_VNHn6qz - ai_description places the event at University of Washington, Seattle; it is UVU.
* Vid_4k_60fps_South_5duWBzw - ai_description guesses Denver, Colorado and reads the post-shot scramble as security tackling a disruptor; neither is supported.
* Vid_3_Drones_PfsVmL5 - filed in the drone cluster but no aerial object appears; ai_description also guesses Phoenix, Arizona.
* Vid_5_No_Drones_Ae575Xv - filed in the drone cluster; filename and footage both confirm no drone. Kept as a control angle.
* Vid_12_Short_Drone_Video_AV87bDo and Vid_Crowdsource_Truth_Do_Any_1966510 - same underlying 16s clip (identical timecode 00;13;11;07, watermark, audio, magnifier loop) held as two entries.
* Vid_Ryan_1_k6rkFas and Vid_Jammles_ShadowofEzra_Says_Photos_1982156 - Vid_Ryan_1 embeds the whole of the Jammles clip behind 67s of commentary; overlapping content in one cluster.
* Vid_Censorship_Ld3J1DY - filed under "Censorship of the Investigation" but contains no suppression claim; it is Gov. Cox broadcast material on social media harms. Fits as official-speech, not suppression.
* Vid_David_Nino_Rodriguez_Man_1982164 - ai_description guesses Las Vegas, Nevada with nothing on screen supporting it.
* Vid_Bechedith_Re_Baroncoleman_VLuvMully_2076295 - ai_description reads the booking-sheet arrest date as 09/11/2021; the document is 2025.
* Vid_FaithDrivUr_Narrator_Says_Police_2078917 - the courtroom exhibit monitor timecode reads 9/10/2021 9:24:48 AM; camera clock year error, footage is Sept 10 2025.
* Vid_MarioNawfal_Erika_Kirk_Takes_6L9661F - no media file, no transcript, no ai_description; only archived post text exists. Page written without a player.

### agent_01

* Vid_TBD_mwSLnKH - State Farm Stadium (Glendale, AZ) memorial footage filed in the "South Side Shot Analysis" ballistics cluster; own frames contradict the filing.
* Vid_Funneral_dKD6hNm - same misfiling (Glendale memorial pan). Also the file has NO audio stream at all, contradicting the ai_description's account of ambient crowd noise.
* Vid_South_Side_ZXD4iw6 - ai_description places the clip at the AGR building, Butler PA; it is the UVU courtyard (matching interior appears in Vid_Inside_Vents_R8NRStG).
* Vid_South_Side_Stairs_KuQuRkf - ai_description guesses Washington DC; it is UVU. Transcript is completely empty (music-only edit).
* Vid_Mile_Kovacevic_HustleBitch_Between_1971989 - ai_description places it at Mt. San Antonio College, Walnut CA; it is UVU.
* Vid_Project_Constitution_MIND_BLOWING_1978201 - ai_description guesses Salt Lake City; it is Orem/UVU.
* Vid_Short_Video_Clip_Captures_xrYHJoc - ai_description reads the instant of the shot as a man tackling the questioner to the ground; the audio is the final Q&A exchange and every other angle shows a mass startle drop. Automated "tackle" reading is wrong.
* Vid_Thomas_Perera_Am_JohnCullen_1977744_3 - ai_description reads the SAME instant as a "sucker punch" and places it in Seattle WA; both wrong. Two independent automated misreads of the same second.
* Vid_Thomas_Perera_Am_JohnCullen_1977744 - ai_description says Butler PA / Trump rally; the transcript says "Charlie's sitting there" and the banner reads PROVE ME WRONG. It is UVU.
* Vid_Thomas_Perera_Am_JohnCullen_1977744_2 - ai_description says Butler PA with Trump at the podium, yet records YREFY/YREFY.COM banners behind the podium and UVU stage audio. It is UVU.
* Vid_14_Visible_Ia_VinKu55 vs Vid_14_Visible_d1k73u7 - same footage, two audio passes; the machine transcripts contradict each other on the key line ("There's NO shot fired right now" vs "He's been shot"). Neither is quotable as testimony.
* Vid_Wendy7839570959_Witness_Camera_Saying_2079042 - ai_description of the inset footage reads it as a white substance splashed on a man's face; the inset audio is the pre-shot stage exchange, so that reading does not fit.
* Vid_Sword_Truth_Hey_Troofevades_2016609 - the clip is an AI-generated illustration (poster says he asked Grok to imagine it); the aerial background is a generic red-brick quad, not UVU, and "0.4mm Algorithm Precision" is not physically meaningful. Transcript is boilerplate artefact text.
* Vid_Conman_Please_Share_Video_1977286_3 - transcript is noise only ("Thank you. You"); the clip has no speech, so the drone claim exists only in the post text.
* Vid_Inside_Vents_R8NRStG - transcript is the lyrics of the backing song, not speech; risks being read as narration or testimony.
* Vid_Shiloheffort_Media_Orig_SH4D0W_2077994_2 - the poster framing archived in Charlie_Kirk.txt describes a question about HAND movements; the held edit marks hair-touching. Archived claim and held artefact do not match.
* Vid_Side_Shot_rjArE7Q and Vid_Side_Shot_2_EB6QBt1 - the same presentation held twice (6:53 short cut, 13:08 full cut) as two separate cluster entries.
* Vid_Yard_1_EpS4n6m and the Vid_14_Visible pair - the name "Isaac" is called in both; possibly the same filming party, worth checking before treating them as independent captures.
* Vid_Aducarrabh_Slow_Motion_Object_8MBbCYs, Vid_Dr_Speaker_Heart_Shot_M4NUARg, Vid_Bizarro_Videos_Vest_Ricochet_HS3Fpz7, Vid_Cashloren_Glenn_Beck_Tells_wvJ1rfZ - no media, no transcript, no ai_description; written from archived post text (and, for two of them, transcripts preserved in Charlie_Kirk.txt).
* PUBLICATION RISK - Vid_Side_Shot_rjArE7Q / Vid_Side_Shot_2_EB6QBt1 name no one but point on screen at two identifiable private bystanders and assert they shot Charlie Kirk. Both are currently "pending"/unpinned. They should not be pinned and made playable without a review.
* PUBLICATION RISK - Vid_Shiloheffort_Media_Orig_SH4D0W_2077994 and _2 are already pinned and playable, and the short edit puts a named living private individual on screen with the caption "Actor?". Counterpoints are carried in the write-ups, but the embeds themselves carry the accusation.

### agent_03

* Vid_John_Cullen_BenSwann_Thought_1969719, Vid_John_Cullen_SharylAttkisson_4_1969372, Vid_Charo_BlakeBednarz_Grok_Attached_1978846 - whisper transcripts contain only the filler token "you" repeated; all three videos are genuinely silent, so the sidecar is correct but useless. Lean on ai_description.
* Vid_Spy_Plane_Analysis_oW3EvAi and Vid_Blake_Bednarz_Original_Post_1978553 - identical recording held twice; transcripts match word for word. One is credited to Bednarz, one filed untitled.
* Vid_Alley_Files_Oh_Wow_2032224 and Vid_Red_Pill_Dispenser_Official_2038934 - same broadcast segment; the Red Pill copy is a phone pointed at a monitor and adds ~20s of preamble, the Alley Files copy runs longer and is cleaner.
* Vid_Charo_BlakeBednarz_Grok_Attached_1978846 - content is a chatbot output asserting the low passes were routine drone-retrieval training, i.e. exculpatory; filed inside the spy-plane cluster where it reads as supporting evidence. Also names a crew roster that conflicts with a second roster in CK_FILE.
* Vid_Alley_Files_Another_Video_2033665 - ai_description reads the post-shot close-protection response as a spectator vaulting the barrier and tackling the speaker, and names the seated man as Steven Crowder. Both wrong; potential libel source if copied into prose.
* Vid_Alley_Files_Heres_Short_2044122 - ai_description again names the speaker Steven Crowder.
* Vid_Blood_Hands_Black_Shirt_t7yTCYe and Vid_Blood_Hands_Black_Shirt_UESJx2U - filenames promise a black-shirted person with blood on their hands; neither ai_description records blood or such a person. Clip 1 is an older man being carried from the plaza by officers; clip 2 is 10s of crowd on the stairs.
* Vid_Blood_Hands_Black_Shirt_t7yTCYe - ai_description places the location in Longmont, Colorado; it is the UVU plaza.
* Vid_Blood_Hands_Black_Shirt_UESJx2U - ai_description guesses Fort Collins, Colorado; tent text ("AMERICAN...", "PROVE ME WRONG") fixes it as UVU.
* Vid_Project_Constitution_URGENT_CALL_1981171 - ai_description guesses Butler, Pennsylvania; American Comeback / Prove Me Wrong branding fixes it as UVU.
* Vid_Muppet_Masher_Comes_Under_2066468 - post caption asserts something comes from under the subject's shirt; ai_description describes the opening body movement as laughter and records no shirt, blood or injury. Needs a human frame-by-frame before it is used as evidence.
* Vid_Meidas_Charise_Lee_MONEY_2029848 - dates its own source (a "February 2026 Epstein ledger") after the events it purports to explain, names entities that do not match the documented TPUSA corporate structure, and accuses several named living people. Unusable as evidence.
* Vid_Rubber_Duck_TM_REMEMBER_2032172 - archival 2012 CNN Sandy Hook footage with a hoax-framing caption, no connection to this investigation. Recommend removal from the public hierarchy.
* Vid_Sword_Truth_Https_T_2033545 - 8:23 anonymous monologue accusing a named living widow of complicity and guilt with zero documentation, plus abusive language. Recommend removal from the public hierarchy.
* Vid_Teacher_Lounge_Shooter_4uXg3De - no ai_description sidecar at all (transcript only). Filed under the Teachers Lounge cluster but is a George Webb livestream about shot geometry, not that room. Back half contains sustained unverified allegations against a named serving federal official plus speculation about private individuals' identities; only the front section is publishable.
* Vid_Project_Constitution_ALERT_BREAKING_1986565 - filed under the Piper N59906 cluster but is almost entirely about low-altitude drones and security jurisdiction; the fixed-wing aircraft is not its subject.
* Vid_Project_Constitution_ALERT_BREAKING_1986847 - whisper transcript is empty (music-only clip). Also: the graphics half and the aerial-imagery half are never joined by anything on screen, and the tail number is never shown.
* Vid_ProjectConstitu_FBI_Ignored_Eyewitnesses_2045871 / _2 - the two entries are the two clips of one X post; _2 (the shorter) is a CNN broadcast segment, _1 (the longer) is a studio commentary monologue. Neither title reflects that.
* Vid_Project_Constitution_Breaking_Newly_1979071 - ai_description identifies the walking subject as "likely Dylan Rounds," a person from an unrelated Utah missing-person case; wholly wrong and it also seeded the page description.
* Vid_Project_Constitution_Breaking_Newly_1979071 - transcript is ASR filler over a silent clip ("I'm not sure. Okay." repeating). Not a transcript.
* Vid_Troofevades_Demonstration_Real_Shaped_2071072 - same ASR-filler-over-silence failure; qwen3-asr output is unusable.
* Vid_Tyler_Running_xJyU633 - filed and named as Tyler running; the six seconds show an interior pan across the UVU Hall of Flags with staff at tables. Nobody is running and nobody is identifiable.
* Vid_0HOUR_Hey_Jimmy_Rustlin_1965902 - filed under Tyler Robinson Footage; the frames show a small white object crossing the sky, not a person. Belongs nearer the drones/airborne-object cluster.
* Vid_Clothing_Change_qHbnd8p and Vid_Clothing_Change_Copy_YMV1Zzv - duplicates of the same Gov. Cox press-conference answer (22s vs 23s subtitled). Two cluster slots for one artefact.
* Vid_Blake_Bednarz_UVU_Reviews_1981078 and _1981078_2 - near-duplicate pair from the same post (#1 and #2), both 31s. Same issue.
* Vid_Blake_Bednarz_UVU_Reviews_1981078 - transcript mishears "gang violence" as "gang buttons"; the companion capture renders it correctly.
* Vid_Blake_Bednarz_Reward_Current_1978863 - transcript is the same half-sentence looping ~6 times, which is accurate to the file but reads as a broken transcript.
* Vid_Virginia_Tech_Sept_4_BJ8f2PK - file name carries a September 4 date but the speech is plainly post-assassination (Kelly speaks of Kirk in the past tense and of the courage of attending "given what happened"). Stored date is wrong.
* Vid_SAS_July_11_PrD4MBV - ai_description shot list ends at 22:26 with the outro card, against a stated 32:27 runtime; capture appears to include trailing material.
* Vid_Megyn_Kelly_Charlie_Kirk_YWSyzDK - is a 2:14 excerpt of Vid_SAS_July_11_PrD4MBV (same July 11 SAS conversation). Both are held as separate cluster entries; the relationship is now stated on both pages.
* Vid_Realhonestash_Source_Clip_UFaZsYm - no transcript, no ai_description, no local file, no sha256; only a CID and a source URL shared with Vid_Realhonestash_Candace_Owens_Covers_2069185. Page written honestly as "not established".
* Vid_Realhonestash_Candace_Owens_Covers_2069185 - archive copy is an .mp3 audio extraction, so no visual description can exist; "What The Footage Shows" says so rather than guessing.
* Vid_Realstewpeters_Stew_Peters_Explains_2069997 - transcript renders "Elbit Systems of America" phonetically as "Albert Systems of America" throughout (Charlie_Kirk.txt already carries the bracketed correction), and "McEwen, Tennessee" as "Macau"/"McCowan".
* Vid_Muppet_Masher_TommyLaRussoLLC_2075684 and Vid_Project_Constitution_Breaking_Newly_1979071 - appear to be the same Wyze porch camera on the same morning (stamps 08:22:50 and 08:22:30), filed as unrelated entries by different posters.
* PUBLICATION CAUTION - Vid_Blake_Bednarz_Who_Guy_1985423 is a crowdsourced "who is this guy?" request that isolates and zooms on an unnamed young event volunteer who is doing nothing but handling merchandise. Currently pending/unpinned. It should not be pinned and made playable without a review; the write-up names no one and states no conduct is alleged.
* PUBLICATION CAUTION - Vid_Project_Constitution_BREAKING_CHARLIE_1976506 points on screen at an unidentified person running during the evacuation and asserts in text that he is the shooter, while simultaneously running a "DO YOU KNOW THIS PERSON?" appeal. Pending/unpinned; same review recommendation.
* Vid_High_Res_Table_Item_jY48QtB - ai_description labels the clip as Butler PA, July 13 2024, with Benny Johnson at the desk; the signage it itself lists (TURNING POINT USA, YREFY.COM, AMERICAN COMEBACK) is UVU on Sept 10 2025.
* Vid_Vide_353_3mwXTjc - ai_description names the man at the table as Steven Crowder and calls the event his tour; it is the TPUSA Prove Me Wrong table at UVU.
* Vid_DguzChVxdJ3Fq5m2_mqMvtwW - same Steven Crowder misattribution on a second file; the machine pass makes this error repeatedly across the corpus.
* Vid_In2ThinAir_WATCH_Charlie_Kirks_1972341 - ai_description reads the footage as three men praying and then a medical episode; it is the seconds after the shot at the table, per the post's own caption and the folder it sits in.
* Vid_Project_Constitution_EXCLUSIVE_BRAND_1977138 - ai_description states the questioner "physically attacks a security guard" and calls him argumentative and the instigator of a fight. No attack is on the recording; the audio at that instant is the last Q&A line. This is the most harmful automated misread found in this batch and it was retracted explicitly on the page.
* Vid_Erika_Evil_Doors_XsWAQXY - ai_description does not identify the speaker at all (calls her an unnamed blonde presenter delivering a PBS news segment) and reads the memorial placard as "a sign for a boy named Charlie". The 17 minutes are Erika Kirk's address; the PBS card is only the broadcaster's end slate.
* Vid_ProjectConstitu_Project_Constitution_Video_2002152 - ai_description calls the montage a memorial slideshow commemorating the life of Bobby Harpole. The site's own profile records him as living; the funeral-home item relates to the family's funeral-services background.
* Vid_MvCUbhcVsUi8L9G_YPH91X5 vs Vid_RyanMatta_BlakeBednarz_RealCandaceO_IanCarrollShow_1968566 - two passes over near-identical UVU exterior camera footage stamped 9/10/2025 12:23:35 disagree on the subject: one reads a long-barrelled rifle in both hands, the other a backpack and no carried object.
* Vid_Vide_35_kKkV3NJ appears to be a subset of Vid_XBHHgwl_EZFACOKB_ptfhcUv (same LDS exchange audio, same angle) but the two are filed in different clusters - Vid_Table_Charlie and Vid_Raw_Shooting_860c. Worth deduplicating or cross-referencing.
* CLUSTER FILING - Vid_RyanMatta_FBI_Needs_Immediately_1984001, _1984014 and Vid_Project_Constitution_NEW_AndrewKolvet_1975655 are filed under Vid_UVU_Venue / Citizen Analysis of the Footage (Part 5). None of the three is analysis of UVU footage: two are studio commentary about Egyptian flight records, one is a Charlie Kirk Show segment about a text chain. Same problem in Part 3 with Vid_Censored_Humans_Charlie_Kirk_2019832 (studio Epstein monologue) and Vid_Final_Cut_Tile_Why_2033216 (AmericaFest stage debate).
* Empty or unusable transcripts in this batch: Vid_High_Res_Table_Item_jY48QtB, Vid_In2ThinAir_WATCH_Charlie_Kirks_1972341, Vid_RyanMatta_BlakeBednarz_RealCandaceO_IanCarrollShow_1968566 (all silence filler); Vid_10_Full_Video_46HJJFb ("Yes"); Vid_Hand_Off_pANvLdZ (one garbled line); Vid_FeelingThePain_HolonCitizen_Stelzner_N1150_2027989 (two syllables); Vid_MvCUbhcVsUi8L9G_YPH91X5 (recogniser hallucination over silence); Vid_French_Legionaire_F1TACDV (no audio stream at all); Vid_ProjectConstitu_Project_Constitution_Video_2002152 (music only); Vid_Vide_222_9tmMm9G (distant PA, unattributable).
* PRIVACY - ai_descriptions for Vid_Public_Bureau_Investigation_Realjesseonfire_2039944 and Vid_Tate_Helmuth_BlakeBednarz_Here_1981181 record vehicle licence plate characters; Vid_ProjectConstitu_Project_Constitution_Video_2002152 names a young family member on a scholarship certificate. All three suppressed on the published pages; they should be scrubbed from videos.yaml too.
* PUBLICATION CAUTION - Vid_French_Legionaire_F1TACDV is a slideshow that pairs a young private individual's souvenir cap with French Foreign Legion imagery and asserts he stood inside a restricted zone. It names nobody but shows his face from six angles. It is currently unpinned; pinning it would publish a face-based identification resting on a tourist cap.
