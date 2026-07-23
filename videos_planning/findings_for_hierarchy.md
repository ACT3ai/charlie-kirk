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
