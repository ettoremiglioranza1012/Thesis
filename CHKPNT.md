# Thesis Checkpoint

Last updated: 2026-08-20 (responded to Prof. Miorandi's feedback email on
the pre-2026-08-19 draft: fixed a residual overclaiming issue between
Chapter 5/6/7 on routing accuracy, fixed two overclaiming phrases in
Chapters 1 and 7, expanded the Chapter 2 bibliography, and added
literature citations to Chapters 5 and 6, which previously had almost
none. 12 new `biblio.bib` entries, independently verified, 3 reworded
after verification flagged issues. Not yet committed — see Git state).

This file is a working checkpoint for picking the thesis back up in a new
session. It is not a memory file and not documentation of the codebase —
it is a snapshot of where the writing stood the last time someone closed
the laptop. Update it at the end of any session that changes chapter
status, not mid-session.

---

## Chapter status

| # | Chapter | File | State |
|---|---------|------|-------|
| 1 | Introduction | `capitoli/Introduction.tex` | **Written** — full prose, revised this session (points 2, 5, 7 in earlier sessions; this session fixed the "full operational correctness" overclaim in §1.4 Contributions, one of the professor's cited examples) |
| 2 | Background & Related Work | `capitoli/background.tex` | **Written** — full prose. This session added 5 new citations to the two thinnest subsections (§2.2 MCP, §2.3 PII/NER fundamentals) plus one in §2.1 (semantic routing), in response to the professor's "bibliografia troppo scarna" note. 27 unique citations now (was 22) |
| 3 | System Architecture | `capitoli/architecture.tex` | **Written** — full prose, revised in earlier sessions (points 2, 4, 7). Untouched this session — spot-checked for overclaiming language, found already well-hedged |
| 4 | Implementation Details | `capitoli/Implementation.tex` | **Written** — full prose, revised in earlier sessions (points 2, 4, 5 confirmed no change needed, 6, 7). Untouched this session — spot-checked, "guarantee(d)" instances are legitimate C#/schema type-system claims, not overreach |
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | **Written (prior session), revised this session** — the "True accuracy (adjusted, see below): ~100% (105/105)" table row and its surrounding prose were reworded: that figure was an inference from manually reading one discrepant trial's response text, not a re-measurement across all 105 trials, and the thesis was stating it as a settled fact. Now reports only the measured 95.2% and explains the one discrepancy as a detection-method artefact, without asserting a precise adjusted number. Also gained 3 new literature citations (test-oracle methodology, CoNLL-2003 NER evaluation convention, self-consistency/multi-sample LLM inference) — previously had zero |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | **Written this session, in full** (§6.1–§6.5, all in earlier sessions). This session: no content changes beyond adding 3 new literature citations (RBAC, distributed-systems HA patterns, ASR-named-entity-recognition interaction) — previously had only 1 (`redis2009`). §6.2's routing-accuracy framing, already fixed the night before the professor's email, is what actually resolves his "Ch.5 needs to align with Ch.6" complaint |
| 7 | Conclusions | `capitoli/conclusions.tex` | **Written this session, in full, then rewritten once for tone** (all in earlier sessions). This session: reworded the "true accuracy at 105 of 105" claim in §7.1 to match the Chapter 5 fix above, and reworded the "at no point... does any component... hold both a token and the value" absolutist framing to state the design claim (by construction) separately from what Chapter 5 actually measured (detection-recall-dependent leak rate) |

All seven chapters now have full prose. This was the last unwritten
chapter.

## Git state

- Working directly on `main` this session, no `dev` branch created.
  `main` was at `5f795dd` (the Chapter 7 / tone-pass commit from
  2026-08-19) at session start, clean.
- **As of this checkpoint update, this session's changes are staged in
  the working tree but not yet committed**: `CHKPNT.md`, `biblio.bib`,
  `capitoli/Introduction.tex`, `capitoli/Validation.tex`,
  `capitoli/background.tex`, `capitoli/conclusions.tex`,
  `capitoli/discussion.tex`, and the rebuilt `main.pdf`. Commit only
  when the user asks.
- Diff logs for every completed feedback point plus the one external
  correction from prior sessions still live in `Tesi_UniTN/diff/`:
  `narrow_the_privacy_claims.txt`,
  `distinguish_deterministic_execution_from_correctness.txt`,
  `correct_the_persistence_description.txt`,
  `reframe_the_contribution_and_novelty.txt`,
  `clarify_the_prototype_scope.txt`,
  `correct_uc_a_tokenization_example.txt`. No new diff log written this
  session — this work responds to a professor email, not a numbered
  feedback point from the earlier round.

## What happened this session (2026-08-20)

Prof. Miorandi emailed feedback on the pre-2026-08-19 draft (he'd pulled
and reviewed before the Chapter 7 / tone-pass session landed, so some of
what he flagged was already stale by the time the user read the email).
The user asked for a plan to dissect the email's two points plus a third,
self-initiated one, then approved executing it. Plan at
`/Users/ettoremiglioranza/.claude/plans/shimmering-kindling-adleman.md`
(note: this plan file gets overwritten by whatever the most recent
planning pass in the repo was — the back-matter cleanup below overwrote
it after the citation work landed; if you need the citation-work plan
text specifically, it's summarised in full below and not recoverable
from that file after this point).

**Point 1 — "Ch.5 va allineato con Ch.6 §6.2", claims too strong
("full operational correctness", "structurally isolates sensitive
data"), dislikes "True accuracy" wording.** Read the current text (not
the checkpoint) before acting, since the checkpoint said Ch.6 §6.2 was
already fixed the night before. Found: the literal staleness the
professor likely saw probably was already fixed (independent of his
email). But a real, more specific problem remained and is almost
certainly what "True accuracy" was flagging: `Validation.tex`'s Table
5.6 had a row `True accuracy (adjusted, see below): ~100% (105/105)`,
repeated in `conclusions.tex` §7.1, stating as settled fact a number
that was actually a manual, single-case inference (reading one
discrepant trial's response text by hand, not re-running all 105
trials). Reworded both: the table now reports only the measured 95.2%,
and the prose in both chapters explains the one discrepancy as a
detection-method artefact found by manual inspection, without asserting
a precise adjusted percentage. Also fixed "full operational correctness"
in `Introduction.tex` §1.4 (asserted before any validation exists in the
thesis — almost certainly the professor's own paraphrase target) and the
"at no point... does any component... hold both a token and the value"
absolutist line in `conclusions.tex` §7.1 (separated the by-construction
architectural claim from what Chapter 5 actually measured, which depends
on detection recall, not just topology). Spot-checked the remaining
`guarantee`/`entirely`/`structural` hits across all chapters — all
legitimate (compiler/schema guarantees, code-structure descriptions),
no further changes needed.

**Point 2 — "bibliografia Ch.2 troppo scarna."** Counted citations per
chapter: background.tex had 22 unique keys, unevenly spread — §2.4 (SOTA)
well-cited, §2.2 (MCP) only 4, §2.3 (PII/NER fundamentals) only 3. Added
5 new citations to the two thin subsections plus one in §2.1: JSON-RPC
2.0 spec (MCP's wire format), a tool-description-quality paper
(`faghih2025toolpreferences`, EMNLP 2025) for the semantic-routing
subsection, classical CRF/BiLSTM-CRF NER citations
(`lafferty2001crf`, `huang2015bilstmcrf`), and a clinical de-identification
paper (`dernoncourt2017deidentification`) grounding the recall-over-precision
design rationale.

**User's own third point — Ch.5/Ch.6 need literature grounding.**
Confirmed near-zero: `Validation.tex` had 0 citations, `discussion.tex`
had 1 (`redis2009`). Added citations for the general methodological/
engineering claims embedded in each chapter's own-results discussion:
`Validation.tex` gained a test-oracle-problem citation (independent-
reference validation methodology), a CoNLL-2003 citation (the standard
span-and-label NER evaluation convention), and a self-consistency-
decoding citation (motivates not trusting a single LLM generation).
`discussion.tex` gained an RBAC citation (§6.3, identity/authorization
prerequisite), a Kleppmann *Designing Data-Intensive Applications*
citation (§6.4, HA/replication/partitioning patterns), and two ASR
citations (§6.5, one on named-entity underrepresentation in ASR training
data, one on WER's poor correlation with downstream NER damage).

**Verification pass (separate agent, per CLAUDE.md).** All 11 new
citations at that point were checked independently: existence, bib
entry accuracy, and whether the cited work actually supports the exact
claim in the citing sentence. 8 of 11 came back clean. 3 were flagged
and fixed:
- `dernoncourt2017deidentification` — the thesis had called it "the same
  recall-first design decision," but the paper doesn't describe an
  explicit recall-weighted training objective; it does report recall
  >99% as its headline result and flags patient-name recall as the
  priority gap. Reworded to "recall-first framing" and cited the
  specific numbers instead of characterising it as a design choice.
- `wang2022selfconsistency` — the thesis had framed self-consistency
  decoding as an "LLM evaluation setting," but the paper's actual
  contribution is an inference-time accuracy-improvement technique
  (sample multiple generations, majority-vote), not an evaluation
  methodology. Reworded to state the shared premise (a single generation
  may not represent typical model behaviour) without mischaracterising
  what the paper is for.
- `jannet2015asrner` — cited for the claim that named entities are rarer
  in ASR training data, but that specific paper's confirmed contribution
  is an evaluation metric (ATENE) correlating ASR errors with downstream
  NER damage, not a study of training-data frequency. Added a second,
  better-fitting citation (`mao2020underrepresented`, arXiv:2005.08742)
  specifically for the training-data-frequency claim, and kept
  `jannet2015asrner` for the WER-doesn't-correlate-with-NER-damage claim
  it does support.

`biblio.bib` grew from 34 to 46 entries. Every new key confirmed
used exactly once via grep before and after the fixes. Clean `tectonic`
build after every edit pass (pre-existing overfull/underfull hbox
warnings only, no new errors, no undefined citations).

**Separately, later the same session: removed the dead Glossary,
Nomenclature list, and Index apparatus.** User asked for an analysis of
the back-matter (Glossary, Nomenclature, List of Figures, List of
Tables, Index) — whether it's aligned with the thesis and worth keeping.
Read the compiled PDF page by page rather than trusting the TOC: found
the TOC linked to a "Glossary" and a "Nomenclature list" at page 43, but
neither actually existed in the PDF — Chapter 7 ends and the very next
physical content is the Bibliography. The Index didn't even get a
phantom TOC entry, just silently absent. Root cause: zero `\gls{}`, zero
`\nomenclature{}`, zero `\index{}` calls anywhere in any of the seven
chapters — these three systems were wired up from the original UniTN
starter template in `Impaginazione/packages.tex` and never touched
since. The Glossary's only defined entries were literally the
`glossaries` package's own tutorial examples ("set," "Fish Age,"
"élite," etc.), not thesis content. User confirmed none of these three
are required by UniTN's template — safe to remove rather than populate
retroactively across seven already-written chapters. List of Figures
(1 entry, Ch.3's architecture diagram) and List of Tables (7 entries,
Ch.3 + Ch.5) are both genuinely functional and were left untouched.
Removed the `imakeidx`/`nomencl`/`glossaries` package blocks from
`Impaginazione/packages.tex`, the `\printglossaries`/`\printnomenclature`
calls from `Impaginazione/inizio.tex`, and the `\printindex` call from
`Impaginazione/fine.tex`. Rebuilt clean; confirmed via `main.toc` that
the chapter list now goes straight from "7 Conclusions" to
"Bibliography," and the page transition (Ch.7 end → Bibliography start)
has no gap or orphaned heading. Page count dropped from 64 to 61 — the
three dead sections were each still forcing a blank page break even
though they rendered no content, so this also fixed three latent blank
pages, not just the TOC links.

## What happened in the 2026-08-19 session

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

1. **This session's changes (2026-08-20) are uncommitted.** Working tree
   has `CHKPNT.md`, `biblio.bib`, and five `capitoli/*.tex` files
   modified, plus the rebuilt `main.pdf`. Commit (and push, if asked)
   next session unless the user wants to review the diff first — this
   is the reply to the professor's email, so it's likely to go out soon.
2. **A citation-related issue was flagged by the user as broken in the
   final PDF, in an even earlier session, but was never independently
   reproduced.** Still unresolved, still no concrete repro. This
   session added 12 new `biblio.bib` entries (34 → 46) without hitting
   the symptom, and the clean `tectonic` build after every pass showed
   no undefined-citation warnings, but that doesn't rule out whatever
   the user originally saw. Ask for a concrete example (which citation,
   where in the PDF) if it resurfaces.
3. **Point 3 (threat model)** — still optional per the professor's own
   note, still not started.
4. **UC-C's substitute-finding branch was never exercised** in the
   validation run behind Chapter 5, since it ran outside the mock
   dataset's absence-ticket date window (2026-03-28–2026-04-10). Stated
   as a limitation in `Validation.tex` and `conclusions.tex` §7.1, not
   hidden. A re-run during that window (dataset and harness are
   reusable, per the pipeline's own docs) would exercise it, if a fuller
   UC-C trace is wanted for the defense version.
5. **All seven chapters have full prose and, as of this session, no
   known overclaiming or citation-support issues** in the specific spots
   the professor flagged or that a full-chapter grep sweep for
   guarantee/entirely/structural/100%-type language surfaced. That
   sweep was targeted (grep-driven, then read in context), not a
   line-by-line read of every chapter — a slower full read-through
   could still turn up something the grep missed.

## Next session

1. Commit and, if asked, push this session's changes — the user is
   replying to a professor email and likely wants this out soon.
2. Chase down the citation-system symptom flagged above before adding
   any more `biblio.bib` entries — get a concrete example first.
3. Optionally tackle point 3 (threat model) if time allows.
4. Optionally re-run the UC-C validation inside the mock dataset's date
   window for a fuller substitute-finding trace before the defense.
5. A full line-by-line read-through pass (not grep-driven) for
   cross-chapter consistency and any remaining overclaiming language
   would still be worthwhile before considering the thesis
   defense-ready — this session's fixes were targeted at what the
   professor and the user specifically flagged, not exhaustive.
