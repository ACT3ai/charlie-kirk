/**
 * CitizenNotice — the narrow right-hand rail that replaces the table of contents
 * on the 100 pages listed in internals/src/citizenNoticePages.ts.
 *
 * What it says, and why it is worth saying: nearly everything on this site is an
 * allegation made by citizen investigators working in public on X, not a finding
 * of fact. They are working around the fact that almost all of the government's
 * information is withheld from them. Readers deserve to be told that on the page
 * itself rather than in a policy page nobody opens, and they deserve a way to
 * report anything that is wrong.
 *
 * Width is set in custom.css, not here — see the CK_CITIZEN_NOTICE block.
 */
import React from 'react';

const CONTACT = 'hollandscitizen@gmail.com';

export default function CitizenNotice(): JSX.Element {
  return (
    <aside
      className="ck-citizen-notice"
      role="complementary"
      aria-label="About the information on this page"
    >
      <p className="ck-citizen-notice__lead">
        Allegations made by citizen&nbsp;investigators on&nbsp;X.
      </p>

      <p>
        Almost everything on these pages is an allegation raised by someone
        else &mdash; in practice close to 100% of it by people and investigators
        on X.
      </p>

      <p>
        They are doing their best to investigate while being denied nearly all
        of the information the government holds. What you are reading is what
        they were able to work out with very limited access, not a finding of
        fact.
      </p>

      <p>
        We try to make everything as accurate as possible, and we have AI check
        it as well.
      </p>

      <p className="ck-citizen-notice__cta">
        If anything here is factually incorrect, please tell us. We have a
        process to update it, and we want to.
      </p>

      <p className="ck-citizen-notice__email">
        <a href={`mailto:${CONTACT}?subject=Correction%20to%20whoassassinatedcharliekirk.com`}>
          {CONTACT}
        </a>
      </p>
    </aside>
  );
}
