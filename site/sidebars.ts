import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Manual flat sidebar.
 *
 * Every entry is a single clickable link to a Level 2 overview page.
 * No categories, no expansion, no nested children. Sub-pages (Level 3+)
 * are reached by navigating into the corresponding overview page.
 *
 * Order matches the `position` values previously set in each top-level
 * `_category_.json` file. New Level 2 sections should be added here in
 * the appropriate slot.
 */
const sidebars: SidebarsConfig = {
  docs: [
    {type: 'doc', id: 'charlie-kirk', label: 'Home'},
    {type: 'doc', id: 'Charlie/overview', label: 'Charlie Kirk'},
    {type: 'doc', id: 'Before/overview', label: 'Before the Shooting'},
    {type: 'doc', id: 'Tyler_Robinson/overview', label: 'Tyler Robinson'},
    {type: 'doc', id: 'Killer/overview', label: 'The Killer'},
    {type: 'doc', id: 'After/overview', label: 'After the Shooting'},
    {type: 'doc', id: 'UVU/overview', label: 'UVU Campus'},
    {type: 'doc', id: 'Tent/overview', label: 'The Tent'},
    {type: 'doc', id: 'Tyler/overview', label: 'Tyler (Suspect)'},
    {type: 'doc', id: 'Theories/overview', label: 'Theories'},
    {type: 'doc', id: 'Timeline/overview', label: 'Timeline'},
    {type: 'doc', id: 'Vote/overview', label: 'Vote'},
    {type: 'doc', id: 'People/overview', label: 'People'},
    {type: 'doc', id: 'Fix/overview', label: 'Fix Laws'},
    {type: 'doc', id: 'Motive/overview', label: 'Motive'},
    {type: 'doc', id: 'Shooting_Locations/overview', label: 'Shooting Locations'},
    {type: 'doc', id: 'CoverUp/overview', label: 'Cover Up'},
    {type: 'doc', id: 'Influencers/overview', label: 'Influencers'},
    {type: 'doc', id: 'Media/overview', label: 'Media'},
    {type: 'doc', id: 'Videos/overview', label: 'Videos'},
    {type: 'doc', id: 'Israel/overview', label: 'Israel'},
    {type: 'doc', id: 'Medical/overview', label: 'Autopsy & Medical'},
    {type: 'doc', id: 'maps/overview', label: 'Maps'},
    {type: 'doc', id: 'US_Intelligence/overview', label: 'U.S. Intelligence'},
    {type: 'doc', id: 'Photos/overview', label: 'Photos'},
    {type: 'doc', id: 'TPUSA/overview', label: 'TPUSA'},
    {type: 'doc', id: 'Censorship/overview', label: 'Censorship'},
    {type: 'doc', id: 'FBI/overview', label: 'FBI'},
    {type: 'doc', id: 'Locations/overview', label: 'Locations'},
    {type: 'doc', id: 'Planes/overview', label: 'Planes'},
    {type: 'doc', id: 'Drones/overview', label: 'Drones'},
    {type: 'doc', id: 'Other/overview', label: 'Other'},
    {type: 'doc', id: 'Proof_Not_Tyler/overview', label: 'Proof Not Tyler'},
    {type: 'doc', id: 'Proof_Intel_Services/overview', label: 'Proof Intel Services'},
    {type: 'doc', id: 'Your_Actions_Fix_It/overview', label: 'Your Actions Fix It'},
    {type: 'doc', id: 'Gun_Bullet/overview', label: 'Gun & Bullet'},
    {type: 'doc', id: 'Patsys/overview', label: 'Patsys'},
    {type: 'doc', id: 'GoogleSearches/overview', label: 'Google Searches'},
    {type: 'doc', id: 'intelligence/overview', label: 'Intelligence'},
    {type: 'doc', id: 'gov/overview', label: 'Government'},
    {type: 'doc', id: 'conspiracy_theories/overview', label: 'Conspiracy Theories'},
    {type: 'doc', id: 'key_individuals/overview', label: 'Key Individuals'},
    {type: 'doc', id: 'legal_investigation/overview', label: 'Legal Investigation'},
    {type: 'doc', id: 'government_organizations/overview', label: 'Government Organizations'},
    {type: 'doc', id: 'campus_university/overview', label: 'Campus & University'},
    {type: 'doc', id: 'political_context/overview', label: 'Political Context'},
    {type: 'doc', id: 'technology_surveillance/overview', label: 'Technology & Surveillance'},
    {type: 'doc', id: 'timeline_events/overview', label: 'Timeline Events'},
    {type: 'doc', id: 'social_media_analysis/overview', label: 'Social Media Analysis'},
    {type: 'doc', id: 'security_law_enforcement/overview', label: 'Security & Law Enforcement'},
    {type: 'doc', id: 'media_response/overview', label: 'Media Response'},
    {type: 'doc', id: 'organizations_groups/overview', label: 'Organizations & Groups'},
    {type: 'doc', id: 'property_locations/overview', label: 'Property & Locations'},
    {type: 'doc', id: 'analysis_documentation/overview', label: 'Analysis & Documentation'},
    {type: 'doc', id: 'other_topics/overview', label: 'Other Topics'},
    {type: 'doc', id: 'Topics3/overview', label: 'Topics3'},
    {type: 'doc', id: 'Topics', label: 'Investigation Topics'},
    {type: 'doc', id: 'Topic-Analyses', label: 'Topic Analyses'},
  ],
};

export default sidebars;
