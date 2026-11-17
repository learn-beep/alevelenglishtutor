# alevelenglishtutor.com

Static Astro site for AQA A-level English, in two sections, deployed on Netlify:
- **English Language** (A level 7702 / AS 7701) at `/language/`
- **English Literature A** (A level 7712 / AS 7711) at `/literature/`

Shared pages at the root: the subject chooser, tutoring (no tutor named yet: the page describes the tutoring in general), about, privacy, terms, report a mistake, thank-you.
Built from the Geography two-board site with the `subject-revision-site` skill (November 2026).

## Run locally
    npm install
    npm run build      # node scripts/build.mjs: builds both sections and the shared pages into dist/
    npx astro dev      # one section at a time: whatever is in src/data (English Language after a build)

## How the two-section build works
`scripts/build.mjs` copies one section's files from `boards/<section>/` into `src/data/`, runs `astro build`, moves the
output under `dist/<section>/` and prefixes that section's internal links. A third build with `board.id = null` gives the
root pages. `public/` (crops in `public/img/<paper>/`, forms) is copied once. It also writes the sitemap.

Everything that differs between the sections is in `boards/<section>/board.json`: topic groups and where each is examined,
paper names, question-type pages, self-marking levels, mock-paper shapes, notes.

Set `CROPS=off` in Netlify's environment to replace every crop with a link to AQA's past-paper page.

## Data
`python3 scripts/export.py --bank "<Question Bank folder>" --topics boards/<section>/topics.json --config boards/<section>/config.json --out boards/<section>/data`
reads a question bank export (`data/index.js`) and writes the section's data files. `python3 scripts/webp_all.py <bank> [<bank>]`
converts the image bundles to WebP crops in `public/img/`. `scripts/make_topics.py` writes the two `topics.json` files
(Language: 14 topics from the spec content; Literature: 25 topics, one per set text plus the unseen and comparison questions).

Banks: `Dropbox\Teaching\English\AQA\Language\Question Bank` and `Dropbox\Teaching\English\AQA\Literature A\Question Bank`.

## Facts to update each year
- `boards/<section>/exams.json`: 2027 dates from AQA's timetable and key-dates pages (AS 7701/2 date not confirmed: check).
- `boards/<section>/boundaries.json`: Language out of 500 (papers ×2, NEA ×1); Literature A out of 375 (papers ×2, NEA ×1.5), separate 2A/2B boundaries.
- New papers: rebuild the banks, re-export, rerun `webp_all.py`.
- AQA added three optional Literature A texts for 2027 (The Island of Missing Trees, Wake, Mr Loverman): add topics when questions exist.

## Content to be checked by a tutor
- The self-marking levels and the type-page descriptions in each board.json.
- `src/data/tutors.json` is empty: add a tutor (slug, name, title, photo, bio, offers, fee) when one is chosen.
