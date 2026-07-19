# Thesis Checkpoint

Last updated: 2026-07-19 (end of the session that drafted Chapter 4).

This file is a working checkpoint for picking the thesis back up in a new
session. It is not a memory file and not documentation of the codebase —
it is a snapshot of where the writing stood the last time someone closed
the laptop. Update it at the end of any session that changes chapter
status, not mid-session.

---

## Chapter status

| # | Chapter | File | State |
|---|---------|------|-------|
| 1 | Introduction | `capitoli/Introduction.tex` | **Written** — full prose |
| 2 | Background & Related Work | `capitoli/background.tex` | **Written** — full prose, revised |
| 3 | System Architecture | `capitoli/architecture.tex` | **Written** — full prose |
| 4 | Implementation Details | `capitoli/Implementation.tex` | **Written this session** — all 5 sections |
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | Skeleton — headings only, §5.5 disabled via `\iffalse` |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | Skeleton — entire chapter in `\iffalse` |
| 7 | Conclusions | `capitoli/conclusions.tex` | Skeleton — 2 sections, no prose |

Chapters 1–4 are done. Chapter 5 is next.

## Git state

- `main` is up to date with `origin/main` (GitHub, for the professor).
- Chapter 4 was drafted on branch `chapter_4`, merged to `main` via fast-forward, and pushed.
- Latest commit: `e504a31` (CLAUDE.md workflow + `.gitignore` fix for local `.otf` font cache files).

## What happened this session

- Drafted all of Chapter 4 (`Implementation.tex`): tech stack (§4.1), the
  Presidio→GLiNER pivot (§4.2), MCP tool exposure via `ask_antares` (§4.3),
  `JobTools` use case orchestration for UC-A/B/C (§4.4), and the
  `IMiorelliService` abstraction with its stub/mock pattern and NSwag
  migration path (§4.5).
- Added ~10 new `biblio.bib` entries; fixed two pre-existing citation
  errors caught during review (Presidio key/year mismatch, Redis
  anachronistic author) that were also present in `background.tex`.
- Established and used the citation-sourcing → draft → independent
  verification-agent pipeline now codified in `CLAUDE.md`.
- Fixed several overfull-hbox line breaks caused by long inline
  `\texttt{}` identifiers by converting dense comma-separated lists to
  `itemize` blocks; added `microtype` to `Impaginazione/packages.tex`.
- Extended `CLAUDE.md` with the writing-process rules learned along the
  way (cross-chapter citation-key checks, writing the chapter-opening
  paragraph alongside a chapter's first section).

## Open item carried forward

Chapter 5's disabled §5.5 ("Privacy and Functional Validation") asks for
quantitative routing-accuracy and NER-performance numbers. **No formal
benchmark or eval logs exist** in the internship documents or the repo —
confirmed by grep, no hits on recall/precision/F1/benchmark language
anywhere in `internship_documents/`. Asked the user directly whether
informal test notes exist; got no response yet. Default plan, absent an
answer: write §5.5 as worked-example qualitative validation (representative
Italian inputs, including adversarial/tricky cases, traced through the
system) rather than claiming aggregate metrics that were never measured.
Re-ask before drafting that specific subsection if it still matters.

## Next session

Start Chapter 5 (`Validation.tex`), following the same one-section-at-a-time
pipeline already in `CLAUDE.md`:

1. §5.1 Workforce Management Domain Overview
2. §5.2 Use Case A: Spatial Querying for Construction Sites
3. §5.3 Use Case B: Colleague Identification and Proximity Ranking
4. §5.4 Use Case C: Holiday Request and Absence Analysis
5. §5.5 Privacy and Functional Validation (currently `\iffalse` — resolve the open item above before writing this one)

Each of §5.2–§5.4 should read as a worked trace through the corresponding
use case already implemented in Chapter 4 (§4.4): the anonymised prompt as
it reaches the LLM, the tool call Claude produces, deanonymisation and
execution against the mock backend, and the report returned. Real example
prompts already exist in `internship_documents/mcp-client.md` (UC-A, UC-B,
UC-C scenarios) — use those rather than inventing new ones.
