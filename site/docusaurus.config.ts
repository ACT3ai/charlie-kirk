import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const siteUrl = process.env.DOCUSAURUS_URL ?? "https://whoassassinatedcharliekirk.com";
const baseUrl = process.env.DOCUSAURUS_BASE_URL ?? "/";

const siteTitle = "Who Assassinated Charlie Kirk";
const siteTagline = "Investigating the September 10, 2025 assassination at Utah Valley University";
const siteDescription =
  "Citizen-led investigation into the September 10, 2025 assassination of Charlie Kirk at Utah Valley University: evidence, timelines, suspects, intelligence-service connections, and proposed legal reforms.";
const socialCard = "img/docusaurus-social-card.jpg";

const config: Config = {
  title: siteTitle,
  tagline: siteTagline,
  favicon: "img/favicon.ico",
  staticDirectories: ["internals/static"],

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: siteUrl,
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl,
  trailingSlash: false,

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "ACT3ai", // Usually your GitHub org/user name.
  projectName: "charlie-kirk", // Usually your repo name.

  onBrokenLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  // Global head tags for SEO: language, JSON-LD structured data (Organization +
  // WebSite), and rich social cards. Per-page descriptions are set via
  // frontmatter and override these defaults. Canonical URLs are emitted
  // per-page by Docusaurus automatically — never add a site-wide canonical
  // here, or every page will canonicalize to the homepage and be deindexed.
  headTags: [
    {
      tagName: "meta",
      attributes: {
        name: "robots",
        content: "index, follow, max-image-preview:large, max-snippet:-1",
      },
    },
    {
      tagName: "meta",
      attributes: {
        name: "author",
        content: "ACT 3 AI, Inc.",
      },
    },
    {
      tagName: "meta",
      attributes: {
        property: "og:site_name",
        content: siteTitle,
      },
    },
    {
      tagName: "meta",
      attributes: {
        property: "og:locale",
        content: "en_US",
      },
    },
    {
      tagName: "script",
      attributes: {
        type: "application/ld+json",
      },
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "WebSite",
        name: siteTitle,
        url: siteUrl,
        description: siteDescription,
        inLanguage: "en-US",
        potentialAction: {
          "@type": "SearchAction",
          target: `${siteUrl}/search?q={search_term_string}`,
          "query-input": "required name=search_term_string",
        },
      }),
    },
    {
      tagName: "script",
      attributes: {
        type: "application/ld+json",
      },
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Organization",
        name: "ACT 3 AI, Inc.",
        url: siteUrl,
        logo: `${siteUrl}/img/Header_Charlie.jpeg`,
      }),
    },
  ],

  plugins: [
    [
      "@docusaurus/plugin-client-redirects",
      {
        // Redirect every bare directory path to its overview page so external
        // backlinks like /Fix or /Tyler_Robinson land on real content instead
        // of GitHub Pages' 301-then-404 chain.
        createRedirects(existingPath: string) {
          const from: string[] = [];
          if (existingPath.endsWith("/overview")) {
            const parent = existingPath.replace(/\/overview$/, "");
            if (parent !== "") {
              from.push(parent);
            }
          }
          // The photo cluster formerly published under /Photos/Table_Hand_off.
          // It was renamed to /Photos/Table_And_Charlie (with the Hand_Off and
          // Lady_Hand_Off sub-clusters renamed too) to drop wording that implied
          // anyone deliberately passed an object. Map every old path forward so
          // existing backlinks keep resolving.
          if (existingPath.startsWith("/Photos/Table_And_Charlie")) {
            const old = existingPath
              .replace("/Photos/Table_And_Charlie", "/Photos/Table_Hand_off")
              .replace("/At_The_Table", "/Hand_Off")
              .replace("/Woman_At_Table", "/Lady_Hand_Off")
              .replace("/Img_Table_Item_60dcfa", "/Img_Hand_Off_Item_60dcfa");
            from.push(old);
            if (old.endsWith("/overview")) {
              from.push(old.replace(/\/overview$/, ""));
            }
          }
          return from.length ? from : undefined;
        },
        // Pages Google still has indexed but that have been moved or removed.
        // Each entry generates a static HTML stub that meta-refreshes to `to`.
        redirects: [
          { from: "/Tyler/overview", to: "/Tyler_Robinson/overview" },
          { from: "/Tyler/Recruited", to: "/Tyler_Robinson/Recruited" },
          { from: "/Tyler/Travel", to: "/Tyler_Robinson/Travel" },
          { from: "/Tyler/Girlfriend/overview", to: "/Tyler_Robinson/Girlfriend/overview" },
          { from: "/Tyler/Trial/overview", to: "/Tyler_Robinson/Trial/overview" },
          { from: "/Plane/N1098L/overview", to: "/Planes/N1098L/overview" },
          { from: "/Plane/Leadership/overview", to: "/Planes/overview" },
          { from: "/Topics3/Planes/overview", to: "/Planes/overview" },
          { from: "/aircraft_flight_analysis/overview", to: "/Planes/overview" },
          { from: "/Killer/Planes_Drones_Theories", to: "/Planes/overview" },
          { from: "/Israel/israel-planes", to: "/Charlie/Israel_Donors_Motive" },
          { from: "/Before/PreEvent_Flights_And_Travel", to: "/Before/overview" },
          { from: "/CIA/overview", to: "/Proof_Intel_Services/overview" },
          { from: "/Influencers/podcasts-project-costa-2", to: "/Influencers/podcasts-project-constitution" },
          { from: "/property_locations/overview", to: "/Locations/overview" },
          { from: "/property_locations", to: "/Locations/overview" },
          // Cabot alibi moved under the new Fort Huachuca Level 3 cluster.
          { from: "/US_Intelligence/Cabot_alibi", to: "/US_Intelligence/Fort_Huachuca/Cabot_alibi" },
        ],
      },
    ],
  ],

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.ts",
          // Path to the source file inside the repo. Docs live in site/docs,
          // and the generated edit URL is appended with the relative path of
          // each source file. Without /edit/main/site/ every page emitted a
          // github.com 404 link that GSC was reporting as a broken outbound.
          editUrl: "https://github.com/ACT3ai/charlie-kirk/edit/main/site/",
          showLastUpdateTime: true,
          exclude: [
            "**/_*.{js,jsx,ts,tsx,md,mdx}",
            "**/_*/**",
            "**/*.test.{js,jsx,ts,tsx}",
            "**/__tests__/**",
            "**/prompts/**",
            "**/CLAUDE.md",
          ],
        },
        blog: false,
        pages: {
          path: "internals/src/pages",
        },
        theme: {
          customCss: "./internals/src/css/custom.css",
        },
        sitemap: {
          changefreq: "weekly",
          priority: 0.5,
          lastmod: "date",
          // /404 — noindex page, must never appear in sitemap.
          // /Tyler/**, /Plane/**, /Topics3/**, /CIA/** — old directory paths
          //   that only exist as plugin-client-redirects stubs; they carry
          //   noindex and a meta-refresh, so Google marks them as
          //   "Excluded by noindex" and "Page with redirect".
          // /aircraft_flight_analysis/**, /Killer/Planes_Drones_Theories,
          //   /Israel/israel-planes, /Before/PreEvent_Flights_And_Travel,
          //   /Influencers/podcasts-project-costa-2 — explicit redirect sources.
          ignorePatterns: [
            "/tags/**",
            "/404",
            "/404.html",
            "/404/",
            "/Tyler/**",
            "/Plane/**",
            "/Topics3/**",
            "/CIA/**",
            "/aircraft_flight_analysis/**",
            "/Killer/Planes_Drones_Theories",
            "/Israel/israel-planes",
            "/Before/PreEvent_Flights_And_Travel",
            "/Influencers/podcasts-project-costa-2",
          ],
          // Filter out redirect stubs generated by plugin-client-redirects.
          // createRedirects creates a stub at every parent path of an /overview
          // page (e.g., /Fix → /Fix/overview). Those stubs carry noindex +
          // meta-refresh, so Google reports them as "Excluded by noindex" and
          // "Page with redirect". Exclude them from the sitemap so Google
          // does not surface them as submitted-URL errors.
          createSitemapItems: async (params) => {
            const { defaultCreateSitemapItems, ...rest } = params;
            const items = await defaultCreateSitemapItems(rest);
            const itemUrls = new Set(items.map((item) => item.url));
            return items.filter((item) => {
              // If path + "/overview" is itself a sitemap URL, this item is a
              // redirect stub (parent directory), not real content — exclude it.
              const candidateOverview = item.url.replace(/\/?$/, "/overview");
              return !itemUrls.has(candidateOverview);
            });
          },
          filename: "sitemap.xml",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Default social card used by Open Graph / Twitter when a page has no own image
    image: socialCard,
    metadata: [
      { name: "description", content: siteDescription },
      {
        name: "keywords",
        content:
          "Charlie Kirk, Charlie Kirk assassination, Charlie Kirk shooting, Utah Valley University, UVU, September 10 2025, Tyler Robinson, TPUSA, Turning Point USA, investigation, intelligence services, cover-up, FBI, CIA, Mossad, who killed Charlie Kirk",
      },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: siteTitle },
      { name: "twitter:description", content: siteDescription },
      { name: "twitter:image", content: `${siteUrl}/${socialCard}` },
      { property: "og:type", content: "website" },
      { property: "og:title", content: siteTitle },
      { property: "og:description", content: siteDescription },
      { property: "og:image", content: `${siteUrl}/${socialCard}` },
      { property: "og:url", content: siteUrl },
    ],
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "Who Assassinated Charlie Kirk",
      logo: {
        alt: "Who Assassinated Charlie Kirk - investigation site logo",
        src: "img/Header_Charlie.jpeg",
      },
      items: [
        { to: "/Fix/overview", label: "Fix Laws", position: "left" },
        { to: "/Proof_Not_Tyler/overview", label: "Proof Not Tyler", position: "left" },
        { to: "/Proof_Intel_Services/overview", label: "Proof Intel Services", position: "left" },
        { to: "/CoverUp/overview", label: "Cover Up", position: "left" },
        { to: "/Your_Actions_Fix_It/overview", label: "Your Actions Fix It", position: "left" },
      ],
    },
    footer: {
      style: "dark",
      copyright: `Copyright © ${new Date().getFullYear()} ACT 3 AI, Inc. All rights reserved.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
