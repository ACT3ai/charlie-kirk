/**
 * Swizzle of @docusaurus/theme-classic 3.10.1 DocItem/Layout.
 *
 * LOCATION: this file must live at <siteDir>/src/theme/, NOT under internals/src/
 * with the rest of this site’s source. Docusaurus hardcodes the swizzle lookup to
 * <siteDir>/src/theme and silently ignores overrides anywhere else — a build with
 * this file under internals/ succeeds, warns nothing, and renders no notice.
 * See site/src/README_THEME.md.
 *
 * WHY THIS FILE EXISTS, AND WHY IT IS NOT THE SMALLER TOC SWIZZLE
 * --------------------------------------------------------------
 * On the 100 pages listed in internals/src/citizenNoticePages.ts the right-hand
 * rail shows the citizen-investigator notice instead of the table of contents.
 *
 * The obvious smaller override would be theme/DocItem/TOC/Desktop, which just
 * swaps what goes INSIDE the rail. That does not work here. Upstream decides
 * whether the rail exists at all:
 *
 *     const canRender = !frontMatter.hide_table_of_contents && toc.length > 0;
 *
 * and 1,951 of this site's 2,696 non-Photos/Videos pages set
 * hide_table_of_contents: true — including 93 of the 100 pages in our list. On
 * every one of those, upstream renders NO right column, so a TOC-level swizzle
 * would have had nothing to render into and the notice would silently never
 * appear. Owning the layout is what lets the notice show on a page that has
 * deliberately suppressed its TOC.
 *
 * Everything else is upstream's behaviour, unchanged. A page NOT in the list
 * renders exactly as it did before this file existed.
 *
 * On a Docusaurus upgrade, re-diff against
 * node_modules/@docusaurus/theme-classic/lib/theme/DocItem/Layout/index.js.
 */
import React from 'react';
import clsx from 'clsx';
import {useWindowSize} from '@docusaurus/theme-common';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import {useLocation} from '@docusaurus/router';
import DocItemPaginator from '@theme/DocItem/Paginator';
import DocVersionBanner from '@theme/DocVersionBanner';
import DocVersionBadge from '@theme/DocVersionBadge';
import DocItemFooter from '@theme/DocItem/Footer';
import DocItemTOCMobile from '@theme/DocItem/TOC/Mobile';
import DocItemTOCDesktop from '@theme/DocItem/TOC/Desktop';
import DocItemContent from '@theme/DocItem/Content';
import DocBreadcrumbs from '@theme/DocBreadcrumbs';
import ContentVisibility from '@theme/ContentVisibility';

import CitizenNotice from '@site/internals/src/components/CitizenNotice';
import {isCitizenNoticePage} from '@site/internals/src/citizenNoticePages';

import styles from './styles.module.css';

/**
 * Decide if the toc should be rendered, on mobile or desktop viewports.
 * Upstream, unchanged.
 */
function useDocTOC() {
  const {frontMatter, toc} = useDoc();
  const windowSize = useWindowSize();
  const hidden = frontMatter.hide_table_of_contents;
  const canRender = !hidden && toc.length > 0;
  const mobile = canRender ? <DocItemTOCMobile /> : undefined;
  const desktop =
    canRender && (windowSize === 'desktop' || windowSize === 'ssr') ? (
      <DocItemTOCDesktop />
    ) : undefined;
  return {hidden, mobile, desktop};
}

export default function DocItemLayout({children}) {
  const docTOC = useDocTOC();
  const {metadata} = useDoc();
  const {pathname} = useLocation();

  // Our only divergence from upstream.
  const showCitizenNotice = isCitizenNoticePage(pathname);

  // The rail exists if the notice is showing OR upstream wanted a desktop TOC.
  // The notice wins the slot when both are true — that is the "replace the right
  // bar" the notice is for.
  const hasRail = showCitizenNotice || Boolean(docTOC.desktop);

  return (
    <div className="row">
      <div
        className={clsx(
          'col',
          // Upstream narrows the content column to 75% whenever a rail is
          // present. When the rail is the narrow notice we give most of that
          // width back, because the notice is a third of a TOC's width.
          showCitizenNotice
            ? styles.docItemColCitizen
            : !docTOC.hidden && styles.docItemCol,
        )}>
        <ContentVisibility metadata={metadata} />
        <DocVersionBanner />
        <div className={styles.docItemContainer}>
          <article>
            <DocBreadcrumbs />
            <DocVersionBadge />
            {/* The mobile TOC is left exactly as upstream had it. The notice is
                rendered separately below so it appears on narrow screens too,
                where there are no columns at all. */}
            {docTOC.mobile}
            <DocItemContent>{children}</DocItemContent>
            {showCitizenNotice && (
              <div className="ck-citizen-notice-mobile">
                <CitizenNotice />
              </div>
            )}
            <DocItemFooter />
          </article>
          <DocItemPaginator />
        </div>
      </div>
      {hasRail && (
        <div className={clsx('col', showCitizenNotice ? 'ck-citizen-col' : 'col--3')}>
          {showCitizenNotice ? <CitizenNotice /> : docTOC.desktop}
        </div>
      )}
    </div>
  );
}
