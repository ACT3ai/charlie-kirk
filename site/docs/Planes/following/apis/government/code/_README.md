# `government/code` — public-domain datasets and the records-request route

| script | source | what it gets |
|---|---|---|
| `faa_registry.js` | FAA Releasable Aircraft Database | Downloads the daily registry archive, extracts the records for every N-registered tail this investigation tracks, and writes them to `../data/faa_registry/tracked_tails_faa_master.json`. |

```
node faa_registry.js
```

## What is committed and what is not

The extracted records for our tails **are** committed. The 70 MB source archive and the 185 MB
`MASTER.txt` it expands to are **not** — `../data/.gitignore` excludes them, because they are
re-downloadable from the FAA in a minute and have no business in this repo.

That `.gitignore` covers **data archives only**. It must never be used to exclude an image. An image
that exists on disk but is untracked renders perfectly in local development and 404s for every real
visitor, because the live site is built from the repo, not from anyone's laptop.

## Licence — and why this pass is different

United States government works are **public domain**. This is the one pass where mirroring the data
onto the site in full is the right thing to do rather than a licence problem. Compare the commercial
pass, where the finding may be published but the payload may not.

## The limit that shapes this whole pass

**The FAA registry covers N-registered aircraft only.** Every Egyptian SU- tail at the centre of the
following claim is absent from it, and no equivalent public Egyptian registry download exists.

So the best free government record available describes the aircraft nobody is arguing about and is
silent on the aircraft everybody is arguing about. **The foreign side cannot be settled by a
download. It can only be settled by a request** — see `../p_get_data.mdx` for who actually holds
which record, and note that ramp, fuel, landing-fee and badge records sit with the *airport*, under
**state** public-records law, not with any federal agency.

## No request has been filed yet

`../requests/` is empty. When it is not, one file per request, named
`<YYYY-MM-DD>_<agency>_<subject>.md`, saved before the request is sent, and tracked in
`../knowledge.mdx` with its tracking number and statutory due date.

**Silence is a result.** An agency that misses its deadline has produced a finding, and it gets
published with the dates.
