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
    {type: 'doc', id: 'Tyler_Robinson_Not_Assassin/overview', label: 'Tyler Robinson Not Assassin'},
    {type: 'doc', id: 'Israel_Main_Suspect/overview', label: 'Israel Main Suspect'},
    {type: 'doc', id: 'US_Intelligence_Assisted/overview', label: 'US Intelligence Assisted'},
    {type: 'doc', id: 'Charlie/overview', label: 'Charlie Kirk'},
    {type: 'doc', id: 'Before/overview', label: 'Before the Shooting'},
    {type: 'doc', id: 'Tyler_Robinson/overview', label: 'Tyler Robinson'},
    {type: 'doc', id: 'Killer/overview', label: 'The Killer'},
    {type: 'doc', id: 'After/overview', label: 'After the Shooting'},
    {type: 'doc', id: 'court/overview', label: 'Court & Trial'},
    {type: 'doc', id: 'Israel/overview', label: 'Israel'},
    {type: 'doc', id: 'Iran/overview', label: 'Iran War'},
    {type: 'doc', id: 'Mic/overview', label: 'Microphone'},
    {type: 'doc', id: 'Planes/overview', label: 'Planes'},
    {type: 'doc', id: 'UVU/overview', label: 'UVU Campus'},
    {type: 'doc', id: 'CoverUp/overview', label: 'Cover Up'},
    {type: 'doc', id: 'TPUSA/overview', label: 'TPUSA'},
    {type: 'doc', id: 'Tent/overview', label: 'The Tent'},
    {type: 'doc', id: 'Theories/overview', label: 'Theories'},
    {type: 'doc', id: 'Narrative/overview', label: 'Narrative'},
    {type: 'doc', id: 'Timeline/overview', label: 'Timeline'},
    {type: 'doc', id: 'People/overview', label: 'People'},
    {type: 'doc', id: 'intelligence/overview', label: 'Intelligence Services'},
    {type: 'doc', id: 'Fix/overview', label: 'New Laws (Fix)'},
    {type: 'doc', id: 'Motive/overview', label: 'Motive'},
    {type: 'doc', id: 'Influencers/overview', label: 'Influencers'},
    {type: 'doc', id: 'Media/overview', label: 'Media'},
    {type: 'doc', id: 'Videos/overview', label: 'Videos'},
    {type: 'doc', id: 'Medical/overview', label: 'Medical'},
    {type: 'doc', id: 'maps/overview', label: 'Maps'},
    {type: 'doc', id: 'US_Intelligence/overview', label: 'U.S. Intelligence'},
    {type: 'doc', id: 'Gov_Mind_Control/overview', label: 'Gov Mind Control'},
    {type: 'doc', id: 'Photos/overview', label: 'Photos'},
    {type: 'doc', id: 'cameras/overview', label: 'Surveillance Cameras'},
    {type: 'doc', id: 'Censorship/overview', label: 'Censorship'},
    {type: 'doc', id: 'FBI/overview', label: 'FBI'},
    {type: 'doc', id: 'Locations/overview', label: 'Locations'},
    {type: 'doc', id: 'Drones/overview', label: 'Drones'},
    {type: 'doc', id: 'Other/overview', label: 'Other'},
    {type: 'doc', id: 'Proof_Not_Tyler/overview', label: 'Proof Not Tyler'},
    {type: 'doc', id: 'Proof_Intel_Services/overview', label: 'Proof Intel Services'},
    {type: 'doc', id: 'Fix/overview', label: 'Your Actions Fix It'},
    {type: 'doc', id: 'Gun_Bullet/overview', label: 'Gun & Bullet'},
    {type: 'doc', id: 'distraction_people/overview', label: 'Distraction People'},
    {type: 'doc', id: 'GoogleSearches/overview', label: 'Google Searches'},
    {type: 'doc', id: 'gov/overview', label: 'Government'},
    {type: 'doc', id: 'key_individuals/overview', label: 'Key Individuals'},
    {type: 'doc', id: 'Legal/overview', label: 'Legal'},
    {type: 'doc', id: 'government_organizations/overview', label: 'Government Organizations'},
    {type: 'doc', id: 'campus_university/overview', label: 'Campus & University'},
    {type: 'doc', id: 'political_context/overview', label: 'Political Context'},
    {type: 'doc', id: 'technology_surveillance/overview', label: 'Technology & Surveillance'},
    {type: 'doc', id: 'Security_Team/overview', label: 'Security Team'},
    {type: 'doc', id: 'Law_Enforcement/overview', label: 'Law Enforcement'},
    {type: 'doc', id: 'organizations_groups/overview', label: 'Organizations & Groups'},
    {type: 'doc', id: 'Topics3/overview', label: 'Topics3'},
    {type: 'doc', id: 'Topics', label: 'Investigation Topics'},
    {type: 'doc', id: 'Defamation/overview', label: 'Defamation Cases'},
  ],
};

export default sidebars;
