# Thesis Checkpoint

Last updated: 2026-08-06 (same session, continued: Chapter 5 written
against real pipeline results).

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
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | **Written this session, in full** — chapter-opening paragraph, §5.1–§5.4, and §5.5 (re-enabled from `\iffalse`), all against real measured results from the point-1 pipeline (see below) |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | **Partially written this session** — chapter-opening paragraph, §6.1 ("Security vs. Complexity Trade-offs", point 4's Redis/log-persistence limitation) and §6.2 ("Validation Methodology Limitations", point 6's schema-vs-correctness and temperature limitation) now have real prose. §6.3–6.5 (production migration, Redis scalability, future extensions) still `\iffalse` |
| 7 | Conclusions | `capitoli/conclusions.tex` | Skeleton — 2 sections, no prose |

Chapters 1–4 are done and now also reworded against the professor's
feedback. Chapter 6 has gone from fully unwritten to two real sections.
Chapter 5's remaining prose (§5.1–§5.4) and Chapter 7 are still next,
paused behind the feedback round below.

## Git state

- `main` is up to date with `origin/main`, commit `b20b888`, untouched
  this session — nothing was committed or pushed.
- All of this session's work (the rewording pass below + the new
  `Tesi_UniTN/diff/` logs) lives **uncommitted, on a local branch named
  `dev`**, branched off `main` at `b20b888`. It was moved there via
  `git stash` → `git checkout -b dev` → `git stash pop` at the end of the
  session, verified clean at every step (stash list empty, diff against
  HEAD matches exactly the 11 expected files, `main` confirmed untouched).
  **Nothing has been committed on `dev` yet** — next session should
  either commit there or decide whether to merge into `main`.
- Diff logs for every completed feedback point live in `Tesi_UniTN/diff/`
  (currently untracked/new on `dev`): `narrow_the_privacy_claims.txt`,
  `distinguish_deterministic_execution_from_correctness.txt`,
  `correct_the_persistence_description.txt`,
  `reframe_the_contribution_and_novelty.txt`,
  `clarify_the_prototype_scope.txt`. Each records, per edit: file,
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
  repository, outside this thesis repo. **Status unknown from within this
  session** — it hasn't reported back yet. Risk flagged to the professor:
  the Anthropic API token available may be expired, which could block it.
- Point 3 (threat model) intentionally left untouched — explicitly
  optional per the professor's own note.

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

1. **Chapter 5's new prose is uncommitted as of this writing** —
   confirm with whoever picks this up next whether it's been committed
   since. Same `dev` branch as the point-2/4/5/6/7 rewording pass
   (commit `63133c8`, pushed to `origin/dev`).
2. **`dev` branch is not merged to `main`.** Decide when/whether to
   merge or open a PR — nothing beyond `dev` has been pushed.
3. **Point 3 (threat model)** — still optional, still not started, out
   of scope for this session per explicit instruction.
4. **Chapter 7 (Conclusions)** — not started. Chapter 5 is now done, so
   this is the next actual writing gap.
5. **UC-C's substitute-finding branch was never exercised** in this
   validation run, since it ran outside the mock dataset's absence-ticket
   date window (2026-03-28–2026-04-10). Stated as a limitation in
   `Validation.tex` itself, not hidden. A re-run during that window
   (dataset and harness are reusable, per the pipeline's own docs) would
   exercise it, if a fuller UC-C trace is wanted for the defense version.

## Next session

1. Decide `dev`'s fate (commit remaining work / merge to `main` / open a
   PR) — check whether Chapter 5 got committed before this session ended.
2. Chapter 7 (Conclusions) — the one remaining unwritten chapter.
3. Optionally tackle point 3 (threat model) if time allows.
4. Optionally re-run the UC-C validation inside the mock dataset's date
   window for a fuller substitute-finding trace before the defense.
