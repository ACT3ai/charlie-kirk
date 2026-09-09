/**
 * Swizzle of the Docusaurus `Root` component.
 *
 * WHAT THIS IS FOR
 * ----------------
 * The citizen-investigator notice rail. It is SITE CHROME — the same layer as
 * the navbar and the footer — not page content. It is declared once, here, and
 * therefore appears on 100% of pages with no per-page list, no front matter, no
 * generator, and nothing that can be forgotten when a page is added.
 *
 * WHY `Root` AND NOT `Layout` OR `DocItem/Layout`
 * -----------------------------------------------
 * Upstream describes Root as the "wrapper at the very top of the app, applied
 * constantly, that does not depend on the current route". That is exactly the
 * guarantee wanted here:
 *
 *   * `DocItem/Layout` covers only doc pages, and only the ones the swizzle's
 *     own conditions let through. That is what this replaced — it ran off a
 *     generated 100-path allow-list, so 5,816 pages never showed the notice.
 *   * `Layout` covers more, but a page can render its own layout, and Layout
 *     remounts on navigation.
 *   * `Root` wraps the entire application, including the 404 page. There is no
 *     route that escapes it.
 *
 * THE RAIL NEVER TOUCHES THE TABLE OF CONTENTS
 * --------------------------------------------
 * The rail lives OUTSIDE the content column, in a gutter reserved on the right
 * edge of the page. The table of contents is untouched: every page that had a
 * right-hand TOC still has it, in its normal place and at its normal width. The
 * two are unrelated pieces of furniture and neither can displace the other.
 *
 * The gutter is reserved in CSS (`--ck-rail-width`, in the CK_CITIZEN_NOTICE
 * block of internals/src/css/custom.css) by padding `.main-wrapper` and
 * `.footer`. The rail itself is fixed to the viewport inside that gutter, so it
 * cannot overlap anything.
 *
 * LOCATION: this file must live at <siteDir>/src/theme/, NOT under
 * internals/src/ with the rest of this site's source. Docusaurus hardcodes the
 * swizzle lookup to <siteDir>/src/theme and silently ignores overrides anywhere
 * else — a build with a swizzle under internals/ succeeds, warns nothing, and
 * renders nothing. See site/src/README_THEME.md.
 */
import React from 'react';
import type {ReactNode} from 'react';

import CitizenNotice from '@site/internals/src/components/CitizenNotice';

export default function Root({children}: {children: ReactNode}): JSX.Element {
  return (
    <>
      {children}
      <CitizenNotice />
    </>
  );
}
