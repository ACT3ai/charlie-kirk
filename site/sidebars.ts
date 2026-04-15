import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    'charlie-kirk',                          // Home — always first

    // === TOC-scored items, sorted highest → lowest ===

    'Charlie/overview',                       // 120  (B1R1 Left + interest 22)
    'Before/overview',                        // 115  (B2R1 Left + interest 17)
    'Tyler_Robinson/Trial/overview',          // 109  (B1R2 Left "Court" + interest 19)
    'Killer/overview',                        // 107  (B1R3 Left + interest 24)
    'After/overview',                         // 104  (B2R2 Left + interest 15)
    'UVU/Courtyward',                         // 103  (B2R1 Center + interest 14)
    'Tent/overview',                          // 103  (B2R1 Center + interest 14)
    'Tyler_Robinson/overview',                // 102  (B1R1 Right + interest 22)
    'Tyler/shooting/overview',                // 101  (B2R1 Right + interest 21)
    'Theories/overview',                      //  99  (B2R2 Center + interest 19)

    {                                         //  97.5 (B1R4 Left + interest 22)
      type: 'category',
      label: 'Timeline',
      collapsed: false,
      items: [
        'Timeline/overview',
        'Timeline/Charlie_Kirk',
        'Timeline/Sept_8_to_13',
        'Timeline/Tyler_Robinson/2025_Sept',
        'Timeline/Tyler_Robinson/Mirandizing',
        'Timeline/Tyler_Robinson/Affidavit_Probable_Cause',
      ],
    },

    'Vote/overview',                          //  97  (B1R1 Center + interest 8)
    'People/overview',                        //  95  (B2R3 Left + interest 15)
    'Fix/overview',                           //  93  (B1R2 Center + interest 12)
    'Motive/overview',                        //  91  (B1R5 Left + interest 23)
    'Shooting_Locations/overview',            //  89  (B1R2 Right + interest 17)
    'Tyler/Before',                           //  89  (B2R2 Right + interest 18)
    'CoverUp/overview',                       //  82  (B2R5 Left + interest 20)
    'Influencers/podcasts',                   //  82  (B2R3 Center + interest 11)
    'Media/overview',                         //  82  (B2R4 Left + interest 11)
    'Videos/overview',                        //  80  (B1R3 Right + interest 15)
    'Israel/overview',                        //  78  (B1R6 Left + interest 18)
    'Fix/Politicans',                         //  75  (B1R4 Center + interest 9)
    'Charlie/Autopsy',                        //  75  (B1R7 Left + interest 22)
    'Influencers/overview',                   //  74  (B2R4 Center + interest 12)
    'maps/overview',                          //  72  (B1R5 Center + interest 13)
    'CIA/overview',                           //  71  (B2R5 Center + interest 18)
    'Photos/overview',                        //  70  (B1R4 Right + interest 13)
    'TPUSA/overview',                         //  69  (B2R6 Left + interest 16)
    'Censorship/overview',                    //  67  (B1R6 Center + interest 16)
    'FBI/overview',                           //  64  (B1R7 Center + interest 20)
    'UVU/overview',                           //  64  (B1R5 Right + interest 14)
    'Locations/overview',                     //  62  (B1R5 Right + interest 12)
    'Planes/overview',                        //  61  (B2R5 Right + interest 17)
    'Drones/overview',                        //  59  (B2R6 Center + interest 15)
    'Medical/overview',                       //  56  (B1R6 Right + interest 14)
    'Other/overview',                         //  40  (B2R6 Right + interest 5)

    // === Not in TOC — sorted by interest score only ===

    'Influencers/x',                          //  10
    'Influencers/youtube',                    //  10
    'conspiracy_theories/overview',           //   8
    'aircraft_flight_analysis/overview',      //   8
    // 'key_individuals/overview',            // removed — merged into People/overview
    'legal_investigation/overview',           //   7
    'government_organizations/overview',      //   6
    'campus_university/overview',             //   6
    'political_context/overview',             //   6
    'technology_surveillance/overview',       //   6
    'timeline_events/overview',               //   5
    'social_media_analysis/overview',         //   5
    'security_law_enforcement/overview',      //   5
    'media_response/overview',                //   5
    'organizations_groups/overview',          //   5
    'property_locations/overview',            //   5
    'Topics',                                 //   5
    'Topic-Analyses',                         //   5
    'Topics3/overview',                       //   5
    'analysis_documentation/overview',        //   3
    'other_topics/overview',                  //   3
  ],
};

export default sidebars;
