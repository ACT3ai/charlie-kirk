# Why this `src/` directory exists

Everything else on this site lives under `internals/` — `internals/src/css`,
`internals/src/pages`, `internals/static`. Those three are relocatable because
`docusaurus.config.ts` points at them explicitly (`staticDirectories`, the pages
plugin's `path`, and `theme.customCss`).

Theme component overrides are the exception. Docusaurus resolves `@theme/...`
overrides from `<siteDir>/src/theme` and that path is **not configurable** — there
is no preset option for it. So the one swizzled component has to sit here:

    src/theme/DocItem/Layout/          swizzle of @docusaurus/theme-classic
                                       DocItem/Layout; renders the citizen notice
                                       rail on the pages listed in
                                       internals/src/citizenNoticePages.ts

Everything it depends on still lives under `internals/`, imported via the `@site`
alias:

    internals/src/components/CitizenNotice/   the rail's markup
    internals/src/citizenNoticePages.ts       the 100 page paths (generated)
    internals/src/css/custom.css              its width and styling

Do not move `src/theme` into `internals/`. It was tried on 2026-09-04: the build
succeeded, reported no error, and simply ignored the override — all 100 pages
rendered without the notice. A silently-ignored swizzle is the failure mode to
watch for here.
