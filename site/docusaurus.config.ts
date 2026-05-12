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

  // Global head tags for SEO: canonical URL, language, JSON-LD structured data
  // (Organization + WebSite), and rich social cards. Per-page descriptions are
  // set via frontmatter and override these defaults.
  headTags: [
    {
      tagName: "link",
      attributes: {
        rel: "canonical",
        href: siteUrl,
      },
    },
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
        logo: `${siteUrl}/img/logo.svg`,
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
          if (existingPath.endsWith("/overview")) {
            const parent = existingPath.replace(/\/overview$/, "");
            if (parent !== "") {
              return [parent];
            }
          }
          return undefined;
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
          ignorePatterns: ["/tags/**"],
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
        src: "img/logo.svg",
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
