/**
 * CitizenNotice — the narrow right-hand notice rail.
 *
 * Rendered once, as site chrome, by the `Root` swizzle at site/src/theme/Root.tsx.
 * It therefore appears on every page of the site. It is NOT page content, it is
 * NOT tied to any page list, and it does NOT replace, hide, move, or compete
 * with the table of contents — the TOC keeps its own column, untouched.
 *
 * WHAT IT SAYS, AND WHY IT IS WORTH SAYING
 * ----------------------------------------
 * Nearly everything on this site is an allegation raised by citizen
 * investigators working in public on X. It is not a finding of fact, and it is
 * not this site claiming that any named person did anything wrong or illegal.
 * Those investigators are working around the fact that almost all of the
 * government's information is withheld from them. Readers deserve to be told
 * that on the page itself rather than in a policy page nobody opens, and they
 * deserve a way to report anything that is wrong.
 *
 * IT IS ALSO THE CORRECTIONS DESK. The rail is the only place a reader is told,
 * on the page they are actually reading, that a name or a fact here can be
 * wrong and that writing in fixes it. That channel is not decorative — the
 * hat-and-plaid identification on the September 10 detail was corrected from
 * Chester Barnes to Derek "Pepper" Williams because somebody wrote in. So the
 * rail is split into two halves by a rule: the DISCLAIMER above it, the ACTION
 * below it. A reader who only reads the bottom half still knows what to do.
 *
 * WORD COUNT IS A CONSTRAINT, NOT A STYLE CHOICE. The rail is hard-capped at
 * 100px wide, which is roughly 16 characters a line. Every word added here
 * costs about one more line of height. Keep it tight — the copy below is
 * deliberately shorter than the disclaimer it replaced so that adding the
 * corrections half did not make the rail taller.
 *
 * Width and placement live in the CK_CITIZEN_NOTICE block of
 * internals/src/css/custom.css, not here.
 */
import React from 'react';

const CONTACT = 'hollandscitizen@gmail.com';

export default function CitizenNotice(): JSX.Element {
  return (
    <aside
      className="ck-rail"
      role="complementary"
      aria-label="About the information on this site"
    >
      <p className="ck-rail__lead">Allegations, not findings.</p>

      <p>
        Nearly all of this is a claim raised by citizen investigators
        on&nbsp;X.
      </p>

      <p>We are not saying any person did anything wrong or illegal.</p>

      <p>
        They work while denied nearly all the information the government holds.
      </p>

      <p>We aim to be accurate. AI checks it too.</p>

      <div className="ck-rail__action">
        <p className="ck-rail__cta">Wrong name? Wrong fact?</p>

        <p>Tell us. We correct on the record.</p>

        <p className="ck-rail__email">
          <a
            href={`mailto:${CONTACT}?subject=Correction%20to%20whoassassinatedcharliekirk.com`}
            aria-label={`Email a correction to ${CONTACT}`}
          >
            {CONTACT}
          </a>
        </p>
      </div>
    </aside>
  );
}
