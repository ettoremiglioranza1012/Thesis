# Thesis Checkpoint

Last updated: 2026-08-06 (same session, continued again: Chapter 6
finished).

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
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | **Written this session, in full** — chapter-opening paragraph, §5.1–§5.4, and §5.5 (re-enabled from `\iffalse`), all against real measured results from the point-1 pipeline (see below), plus 6 data tables (E2E results ×3, GLiNER metrics, itemized false negatives, routing summary) |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | **Written this session, in full** — chapter-opening paragraph and all five sections. §6.1/§6.2 came from the feedback rewording pass (points 4, 6); §6.3 (production migration) reflects on and prioritises the point-7 caveat already in `Implementation.tex` rather than repeating it; §6.4 (Redis scalability) is new analysis, ties the TTL gap from §6.1 to memory growth under load; §6.5 (future extensions: voice, local models) is deliberately more speculative/lower-confidence, framed as open measurement questions rather than claims |
| 7 | Conclusions | `capitoli/conclusions.tex` | Skeleton — 2 sections, no prose. **Next actual writing gap** |

Chapters 1–4 are done and now also reworded against the professor's
feedback. Chapter 6 has gone from fully unwritten to two real sections.
Chapter 5's remaining prose (§5.1–§5.4) and Chapter 7 are still next,
paused behind the feedback round below.

## Git state

- `main` is up to date with `origin/main`, commit `cd04ab6`. Everything
  from this session — the point-2/4/5/6/7 rewording pass, Chapter 5 in
  full, and the six data tables added to it afterward — is committed and
  pushed, in three commits: `63133c8` (rewording), `774fdc2` (Chapter 5
  prose), `cd04ab6` (Chapter 5 tables).
- The work was drafted on a local branch `dev` first (stash → new branch
  → stash pop, verified clean at every step), then fast-forward merged
  into `main` (`--ff-only`, no conflicts possible since `main` hadn't
  moved) and pushed directly. The table-addition commit was made directly
  on `main` per explicit instruction, after the merge.
- `dev` still exists, both locally and as `origin/dev`, but `main` now
  has everything `dev` has — it's redundant. Fine to delete whenever
  (`git branch -d dev` / `git push origin --delete dev`), not urgent.
- Diff logs for every completed feedback point plus the one external
  correction live in `Tesi_UniTN/diff/`: `narrow_the_privacy_claims.txt`,
  `distinguish_deterministic_execution_from_correctness.txt`,
  `correct_the_persistence_description.txt`,
  `reframe_the_contribution_and_novelty.txt`,
  `clarify_the_prototype_scope.txt`,
  `correct_uc_a_tokenization_example.txt`. Each records, per edit: file,
  chapter/section, old text, new text, and why.

## What happened this session

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
   final PDF, but not independently reproduced.** Investigated before
   writing Chapter 6's remaining sections: `\printbibliography` is
   correctly configured (`fine.tex`), the BibTeX log shows no
   warnings/errors, and all 34 `biblio.bib` entries print correctly in
   the compiled PDF with in-text numbers cross-referencing correctly
   (spot-checked Albanese = [1] and Vaswani = [30] in both body and
   list). As a precaution, §6.3-6.5 were written without adding any new
   `biblio.bib` entries, reusing only citations already in the document.
   **The specific symptom the user saw was never identified — ask for
   a concrete example (which citation, where in the PDF) before trusting
   the citation system fully or adding new entries.**
2. **Point 3 (threat model)** — still optional, still not started, out
   of scope for this session per explicit instruction.
3. **Chapter 7 (Conclusions)** — not started. This is now the only
   unwritten chapter. Needs to summarise what Chapters 5 and 6 actually
   established against the objectives stated in Chapter 1
   (`sec:intro_objectives`).
4. **UC-C's substitute-finding branch was never exercised** in the
   validation run behind Chapter 5, since it ran outside the mock
   dataset's absence-ticket date window (2026-03-28–2026-04-10). Stated
   as a limitation in `Validation.tex` itself, not hidden. A re-run
   during that window (dataset and harness are reusable, per the
   pipeline's own docs) would exercise it, if a fuller UC-C trace is
   wanted for the defense version.
5. **`dev` branch is redundant** now that `main` has everything it had —
   safe to delete locally and on `origin` whenever, not urgent.

## Next session

1. **Chapter 7 (Conclusions)** — the only remaining unwritten chapter.
   Summarise achieved results against Chapter 1's three research
   questions (Section~\ref{sec:intro_objectives}), referencing the real
   measured numbers from Chapter 5 and the honestly-stated limitations
   from Chapter 6, not re-asserting anything Chapter 6 already qualified.
2. Chase down the citation-system symptom flagged above before adding
   any new `biblio.bib` entries — get a concrete example first.
3. Optionally tackle point 3 (threat model) if time allows.
4. Optionally re-run the UC-C validation inside the mock dataset's date
   window for a fuller substitute-finding trace before the defense.
5. Housekeeping: delete the now-redundant `dev` branch (local + remote).
