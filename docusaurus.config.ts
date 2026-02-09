import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const siteUrl = process.env.DOCUSAURUS_URL ?? "https://whoassassinatedcharliekirk.com";
const baseUrl = process.env.DOCUSAURUS_BASE_URL ?? "/";

const config: Config = {
  title: "My Site",
  tagline: "Dinosaurs are cool",
  favicon: "img/favicon.ico",

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

  onBrokenLinks: "throw",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.ts",
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/ACT3ai/hollywood-whitepaper",
        },
        blog: {
          showReadingTime: true,
          editUrl: "https://github.com/ACT3ai/charlie-kirk",
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: "img/docusaurus-social-card.jpg",
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "Home",
      logo: {
        alt: "My Site Logo",
        src: "img/logo.svg",
      },
      items: [
        { href: "https://act3TV.com/Charlie_Kirk/", label: "Charlie Kirk Movie", position: "left" },
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
