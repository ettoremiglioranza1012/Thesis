# Thesis Checkpoint

Last updated: 2026-08-06 (end of the session that handled the first round
of professor feedback).

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
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | Skeleton — headings only, §5.5 disabled via `\iffalse`. **Drafting still paused**, untouched this session |
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

## Open items carried forward

1. **Point 1's pipeline status is unknown.** Check on it next session.
   If it lands, its results go into §5.5 and get added on top of the
   agnostic language already written into chapters 1/3/4/6 (not replacing
   it). If it doesn't land in time, §5.5 gets written as an explicit
   statement of what wasn't measured, consistent with the agnostic
   framing already in place.
2. **`dev` branch is uncommitted.** Decide whether to commit there, keep
   iterating, or merge to `main` — nothing has been pushed.
3. **Point 3 (threat model)** — still optional, still not started.
4. **Chapter 5 (§5.1–§5.4) and Chapter 7** — drafting paused for the
   entire feedback round, not resumed yet.

## Next session

1. Check on the pipeline agent (point 1).
2. Decide `dev`'s fate (commit / keep working / merge).
3. Resume Chapter 5 drafting per the original plan (§5.1 domain overview,
   §5.2–§5.4 the three use-case traces using the real prompts from
   `internship_documents/mcp-client.md`), then write §5.5 once point 1's
   outcome is known.
4. Optionally tackle point 3 (threat model) if time allows.
5. Chapter 7 (Conclusions) after Chapter 5 is done.
