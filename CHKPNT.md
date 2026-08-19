# Thesis Checkpoint

Last updated: 2026-08-19 (Chapter 7 written, all seven chapters now have
full prose; a tone/structure pass across Chapters 5 and 7; merged to
`main` and pushed).

This file is a working checkpoint for picking the thesis back up in a new
session. It is not a memory file and not documentation of the codebase —
it is a snapshot of where the writing stood the last time someone closed
the laptop. Update it at the end of any session that changes chapter
status, not mid-session.

---

## Chapter status

| # | Chapter | File | State |
|---|---------|------|-------|
| 1 | Introduction | `capitoli/Introduction.tex` | **Written** — full prose, revised this session (points 2, 5, 7) |
| 2 | Background & Related Work | `capitoli/background.tex` | **Written** — full prose. Untouched this session: already correctly hedges every claim the feedback round flagged, used as the calibration reference for every rewording done elsewhere |
| 3 | System Architecture | `capitoli/architecture.tex` | **Written** — full prose, revised this session (points 2, 4, 7) |
| 4 | Implementation Details | `capitoli/Implementation.tex` | **Written** — full prose, revised this session (points 2, 4, 5 confirmed no change needed, 6, 7) |
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | **Written (prior session), revised this session** — content unchanged from the point-1 pipeline results, but §5.3's harness-bug paragraph and §5.4.1's date-window explanation were removed entirely (they read as excuse-making for fully self-controlled tooling/data), §5.2.1 and §5.5.2 were trimmed of defensive meta-commentary, and §5.4.1 was retitled to match its now-authorization-only content. All 6 data tables and every number unchanged |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | **Written this session, in full** — chapter-opening paragraph and all five sections. §6.1/§6.2 came from the feedback rewording pass (points 4, 6); §6.3 (production migration) reflects on and prioritises the point-7 caveat already in `Implementation.tex` rather than repeating it; §6.4 (Redis scalability) is new analysis, ties the TTL gap from §6.1 to memory growth under load; §6.5 (future extensions: voice, local models) is deliberately more speculative/lower-confidence, framed as open measurement questions rather than claims |
| 7 | Conclusions | `capitoli/conclusions.tex` | **Written this session, in full, then rewritten once for tone** — §7.1 answers the three research questions from `sec:intro_objectives` against Chapter 5's actual measured numbers (payload audit, GLiNER P/R/F1, 12/12 E2E, routing 95.2%/~100%, the UC-A tokenisation-example correction), then states Chapter 6's honest limitations (Redis TTL, UC-C substitute branch never exercised, mock-only validation) without softening them; §7.2 reflects on enterprise-adoption implications (pseudonymisation vs. anonymisation, MCP's enforcement point holding under measurement, the Presidio→GLiNER pivot as what privacy-by-design costs in practice). First draft read as too rhetorical; rewritten into a plainer academic register, same content |

All seven chapters now have full prose. This was the last unwritten
chapter.

## Git state

- `main` is up to date with `origin/main`, commit `5e7523a` (the Chapter
  6 finish from last session). This session started by deleting the old
  local `dev` (it had one unpushed commit, `774fdc2` duplicated content
  already on `main`, per explicit user instruction — destructive,
  confirmed first) and recreating `dev` fresh from `main`.
- All of this session's work is on `dev`: Chapter 7 (`conclusions.tex`)
  written in full and then de-dramatised, a stale-claim fix in
  `discussion.tex` §6.2, a tone and structure pass across
  `Validation.tex` (Chapter 5), `CHKPNT.md` itself, and the rebuilt
  `main.pdf`. Committed on `dev`, fast-forward merged into `main`, and
  pushed to `origin/main` at the user's explicit request — see the
  commit hash this checkpoint update itself will be committed under.
- Diff logs for every completed feedback point plus the one external
  correction from prior sessions still live in `Tesi_UniTN/diff/`:
  `narrow_the_privacy_claims.txt`,
  `distinguish_deterministic_execution_from_correctness.txt`,
  `correct_the_persistence_description.txt`,
  `reframe_the_contribution_and_novelty.txt`,
  `clarify_the_prototype_scope.txt`,
  `correct_uc_a_tokenization_example.txt`. No new diff log was written
  this session for the §6.2 fix — it wasn't a professor-feedback-point
  rewording, it was correcting a chapter that had gone stale against a
  later chapter's actual results.

## What happened this session (2026-08-19)

- Recreated `dev` from `main` (destructive delete of the old, redundant
  `dev`, confirmed with the user first — see Git state above).
- Read `CHKPNT.md`, all of `internship_documents/`, and the relevant
  thesis chapters (`conclusions.tex`, `Introduction.tex`,
  `discussion.tex`, `Validation.tex`, `background.tex`) per the standing
  project instructions, before writing anything.
- Wrote Chapter 7 (`conclusions.tex`) in full. §7.1 answers the three
  research questions from `sec:intro_objectives` against Chapter 5's
  actual measured numbers, states Chapter 6's honest limitations without
  softening them, and highlights that validation itself caught a real
  error (the UC-A tokenisation example). §7.2 reflects on broader
  enterprise-adoption implications: pseudonymisation vs. anonymisation
  under GDPR, MCP's enforcement point holding under measurement (not
  just under the protocol's own description), the Presidio→GLiNER pivot
  as what privacy-by-design costs in practice versus how it reads in a
  proposal, and a scoped, non-hyperbolic closing claim about what
  generalises past this one system. Deliberately did **not** use any
  cost/EUR figures from the internship demo slides (`Slides_...pdf`) —
  those numbers were never integrated into the thesis's own chapters, so
  introducing them fresh in the conclusion would have been scope creep.
- While researching Chapter 7, found that `discussion.tex` §6.2
  (Validation Methodology Limitations) had gone stale: it claims "no
  systematic test suite in this thesis" measures routing accuracy, but
  `Validation.tex` §5.5 (written in a later pass of a prior session) does
  exactly that — 21 prompts × 5 repetitions = 105 trials, reported in
  `tab:routing_summary`. Flagged this to the user via AskUserQuestion
  rather than silently fixing or silently ignoring it; user chose to fix
  it now. Rewrote both paragraphs of §6.2 to state that routing accuracy
  **was** measured, and reframed the real residual limitation correctly:
  not "no measurement," but the *scope* of the 21-prompt hand-built set
  (representativeness against real deployment traffic, paraphrasing,
  adversarial phrasing) and what temperature-1.0 consistency across 5
  reps does and doesn't establish (no variance observed on these 21
  prompts, not proof no prompt could ever vary).
- Verified with a clean `tectonic` build (via `build.py`) after both
  edits — no new errors, only pre-existing overfull/underfull hbox
  warnings plus one new (harmless) overfull hbox in `conclusions.tex`.
- User flagged that `conclusions.tex` read as overly rhetorical
  ("LinkedIn tone") — punchy two-line reveals, aphoristic closers,
  "hot take" framing. Rewrote both sections of Chapter 7 into a plainer,
  more measured academic register. Same facts, numbers, and citations
  throughout; only the delivery changed.
- User then flagged a recurring pattern in `Validation.tex`: several
  passages over-explained self-inflicted or fully-controlled limitations
  (an evaluation-harness bug, a mock dataset's fixed dates, a black-box
  framing for tooling the team wrote itself) with defensive multi-sentence
  justifications, some ending in meta-commentary that named itself as
  "not an excuse" — which reads as one anyway. Went through the whole
  chapter and:
  - Simplified §5.2.1's opening (redundant triple restatement of "this
    isn't circular").
  - Cut §5.5.1's dramatic one-liner ("It was carried out.") and trimmed
    adjacent meta-commentary.
  - Simplified §5.4.1's date-window explanation, then per a follow-up
    request **removed it entirely** (matching the earlier full removal
    of the §5.3 harness-bug paragraph).
  - Fully removed the §5.3 harness-bug paragraph and its UC-C
    cross-reference, both flagged as making the team look like it
    didn't control its own tooling.
  - Rewrote the R-C6 routing-discrepancy paragraph and the
    fragmented-token paragraph in §5.5.2, cutting the self-aware
    "not an excuse for it" framing.
  - Found and fixed one downstream inconsistency this created:
    `conclusions.tex` §7.1 still echoed the old "black-box detection
    method" wording after `Validation.tex` had dropped it.
- Re-reviewed the full chapter afterward per user request and found two
  structural side effects of the cuts, both then fixed: §5.4.1's heading
  ("Workflow Logic: Colleagues, Substitutes, and Authorization") no
  longer matched its authorization-only content after the removal
  (retitled to "Authorization Paths and Absence Reporting"), and
  Table~\ref{tab:ucc_e2e}'s \texttt{Absent} column had gone from
  over-explained to unexplained (added back one plain sentence, not a
  paragraph). Also cleaned up a stray double blank line.
- Compiled and sent the rebuilt PDF to the user for review after the
  Chapter 5 fixes.

## What happened in earlier sessions

- Received a 7-point professor feedback round (Prof. Miorandi) on
  chapters 1–4, given before Chapter 5 existed (mostly inferred from the
  ToC): (1) validation chapter needs quantitative evidence, (2) narrow
  the privacy claims, (3) add a threat model (optional/"if time allows"),
  (4) correct the Redis/log-persistence description, (5) reframe the
  contribution/novelty claim, (6) distinguish deterministic execution
  from correctness, (7) clarify the prototype scope.
- Drafted and sent a point-by-point response confirming the feedback's
  accuracy against the actual implementation (kept in chat only, not
  committed to the repo, per instruction).
- Closed **points 2, 4, 5, 6, 7** via targeted rewording passes across
  the abstract and chapters 1/3/4, one point at a time, each logged in
  its own `Tesi_UniTN/diff/*.txt` file and verified with a clean
  `tectonic` build after every pass.
- Adopted a working principle partway through: rewordings for points
  2/4/5/6/7 must be **agnostic to whether the quantitative validation
  pipeline (point 1) ever gets built** — any forward reference to
  Chapter 5 states that it will address a question, not that it will
  report a specific (possibly nonexistent) result. This resolved a
  sentence in the abstract that had been stuck DEFERRED since the very
  first pass, entangled across three separate points.
- Changed policy on Chapter 6: limitations surfaced during a rewording
  pass now get written into `discussion.tex` as real prose during that
  same pass, instead of drafted-and-deferred. §6.1 and §6.2 exist because
  of this.
- Delegated point 1 (the actual quantitative validation pipeline: GLiNER
  precision/recall/F1 with a false-negative list, semantic routing
  accuracy and consistency across repeated runs given the routing model's
  temperature 1.0, UC-A/B/C expected-vs-observed, and a payload PII-leak
  audit) to a separate Claude Code agent working in the application's own
  repository, outside this thesis repo. **It landed later in this same
  session** — see the dedicated section below.
- Point 3 (threat model) intentionally left untouched — explicitly
  optional per the professor's own note.
- Finished Chapter 6 (`discussion.tex`): §6.3, §6.4, §6.5 written,
  un-`\iffalse`'d, chapter-opening paragraph updated to name all five
  sections. Investigated a citation-rendering issue the user flagged as
  broken first (see open items) — found no reproducible problem, but
  wrote this pass's new content without adding any new `biblio.bib`
  entries as a precaution.

## Point 1 (quantitative pipeline) — landed

The separate Claude Code agent working in
`/Users/ettoremiglioranza/Projects/AI-powered-workforce-management-system`
(a different local repo, not this one) succeeded. Handoff artifact:
`Docs/validation-pipeline.md` in that repo, raw results in
`Validation/results/*.{json,csv,md}`. Every headline number in that doc
was independently cross-checked against the raw result files before use
(not taken on faith) — all confirmed accurate. Summary of what it found:

- GLiNER coverage P/R/F1: 0.938/0.915/0.926. Strict: 0.840/0.829/0.834.
  7 false negatives (4 date-range phrasing, 2 emails, 1 bare city name),
  5 false positives, all explainable.
- Payload PII-leak audit: 2 leaks out of 50 prompts scanned, both
  correlating with a GLiNER false negative, zero uncorrelated leaks —
  empirical confirmation that the privacy property has no independent
  bypass path.
- Routing: 95.2% measured (100/105 trials), but the one discrepancy
  (R-C6) is a log-diffing observability blind spot, not a routing error —
  true accuracy is very likely 105/105. 21/21 prompts fully consistent
  across 5 repetitions despite temperature=1.0.
- End-to-end UC-A/B/C: 12/12 cases matched an independent, non-shared-
  code reference implementation.
- One correction propagated directly into this repo by that agent (not
  by me): `architecture.tex`'s UC-A tokenisation worked example was
  wrong (described 2 tokens, GLiNER actually produces 3, fragmenting the
  compound site/company descriptor). Verified and logged in
  `Tesi_UniTN/diff/correct_uc_a_tokenization_example.txt`.

All of this is now written into `Validation.tex` §5.5, with both the
routing caveat (measured vs. true accuracy) and the itemized
false-negative list reported explicitly, not summarised into a single
headline number — that was flagged as the one place a naive summary
would misreport what was actually found.

## Open items carried forward

1. **A citation-related issue was flagged by the user as broken in the
   final PDF, in an earlier session, but was never independently
   reproduced.** `\printbibliography` is correctly configured
   (`fine.tex`), the BibTeX log shows no warnings/errors, and all
   `biblio.bib` entries printed correctly as of the last check
   (spot-checked Albanese = [1] and Vaswani = [30] in both body and
   list). No new `biblio.bib` entries were added this session either.
   **The specific symptom the user saw was never identified — ask for
   a concrete example (which citation, where in the PDF) before trusting
   the citation system fully or adding new entries.**
2. **Point 3 (threat model)** — still optional per the professor's own
   note, still not started.
3. **UC-C's substitute-finding branch was never exercised** in the
   validation run behind Chapter 5, since it ran outside the mock
   dataset's absence-ticket date window (2026-03-28–2026-04-10). Stated
   as a limitation in `Validation.tex` and now also in `conclusions.tex`
   §7.1, not hidden. A re-run during that window (dataset and harness are
   reusable, per the pipeline's own docs) would exercise it, if a fuller
   UC-C trace is wanted for the defense version.
4. **This session's work is committed, merged to `main`, and pushed.**
5. **All seven chapters now have full prose** — the thesis is,
   content-wise, complete for the first time. What's left is polish
   (items 1–3 above), not a writing gap.

## Next session

1. Chase down the citation-system symptom flagged above before adding
   any new `biblio.bib` entries — get a concrete example first.
2. Optionally tackle point 3 (threat model) if time allows.
3. Optionally re-run the UC-C validation inside the mock dataset's date
   window for a fuller substitute-finding trace before the defense.
4. With all chapters now drafted, a full read-through pass for
   cross-chapter consistency (the kind of staleness that hit
   `discussion.tex` §6.2 this session) would be worthwhile before
   considering the thesis defense-ready.
