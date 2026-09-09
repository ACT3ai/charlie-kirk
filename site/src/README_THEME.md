# site/src/theme — why this directory exists here and nowhere else

This site keeps its source under `site/internals/src/`, not `site/src/`. There is
exactly one exception, and it is not a preference: **Docusaurus hardcodes the
component-swizzle lookup to `<siteDir>/src/theme`.** An override placed anywhere
else is silently ignored — the build succeeds, warns about nothing, and renders
nothing. That failure mode has already cost a day once. Do not "tidy" this
directory back under `internals/`.

## What is in here

    src/theme/Root.tsx     the notice rail, as site chrome, on 100% of pages

`Root` is the Docusaurus wrapper that sits at the very top of the app, applied
constantly and independent of the current route. Declaring the rail there is
what makes it structural — the same layer as the navbar and the footer. There is
no page list, no front matter flag, and no generator, so there is no way for a
new page to miss it.

Supporting files, which live in the normal place:

    internals/src/components/CitizenNotice/   the rail's markup and copy
    internals/src/css/custom.css              CK_CITIZEN_NOTICE block: width,
                                              the reserved gutter, mobile shape

## The rail must never interfere with the table of contents

The rail sits in a gutter reserved at the right edge of the page, outside the
content area — past the TOC, not in place of it. Every page that has a
right-hand table of contents keeps it, unchanged.

This replaced an earlier design (commit `635047b1`, 2026-09-04) that swizzled
`DocItem/Layout` and had the notice *take over* the TOC column on a generated
list of 100 pages. That approach was wrong twice over: it covered 100 of 5,916
pages, and where it did appear it removed the table of contents. Both the
swizzle and its generator (`tools/gen_citizen_pages.py`,
`internals/src/citizenNoticePages.ts`) were deleted. Do not reintroduce a
per-page list for this.

## On a Docusaurus upgrade

`Root.tsx` does not copy any upstream implementation — it renders `{children}`
plus the rail — so it does not drift with upstream and needs no re-diff. The two
things to re-check are that `.main-wrapper` and `.footer` are still the class
names carrying the page body and the footer container, since the CSS reserves
the gutter by padding them.
