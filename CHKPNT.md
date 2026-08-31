# Thesis Checkpoint

**Session close, 2026-09-01, branch `main`.** Full rework of
`slides/slide.tex` in response to a point-by-point review from the
supervisor (relatore), delivered by the user as six numbered points
plus a final consistency check, with an explicit operational rule
followed all session: one point at a time, diff shown and approved
before writing, no em dash, no invented data or citations, theme/colors
unchanged, deck same length or shorter. Defense date confirmed by the
user: 15 September 2026.

**Point 1, absolute privacy claims removed.** Searched the deck for
`blind`, `without access`, `no exposure`, `never sees`, `guarantee` and
listed every hit before touching anything, per instruction. Fixed
subtitle (`Keeping the AI Model Blind...` to `Substituting Real Employee
Data Before It Reaches the AI Model`, describes the mechanism instead of
asserting an outcome), a "why four services" bullet, and the mechanism
slide's title, all previously contradicted by the deck's own 2/50 leak
result. Left two instances deliberately unchanged on the user's explicit
reasoning: the gap slide's "no exposure" bullet (a stated requirement
under a column headed "REQUIRED BY", not a claim of achievement) and the
research-question quote (already hedged by its own closing clause).
"Guarantee" in the routing slide's repeatability note was flagged as
out of scope (a different topic, LLM output repeatability, not privacy)
and left as is after the user agreed.

**Point 2, three different test-set sizes explained, not just labeled.**
Read `Tesi_UniTN/capitoli/Validation.tex` in full to ground this rather
than guessing. Three genuinely separate, purpose-built sets: 50 prompts
/ 82 labelled spans for detection (the leak audit reuses this same set,
doesn't have its own), 21 prompts x 5 repetitions for routing
(repetition needed because temperature 1.0 sampling isn't observable in
one pass), 12 end-to-end scenarios across three use cases for
correctness (business-logic coverage, not a statistical sample). A first
attempt at per-slide "why different" lines was rejected by the user for
starting from the recognition table instead of asking the user for the
real reason first; the user then supplied the actual reasoning (each
stage needs different evidence) and the lines were rewritten around
that, with several rounds of wording correction (no numbers repeated
three times on one slide, no unverified claims presented as confirmed
findings, position relative to existing text matters for readability).

**Point 3, two missing citations.** Gap slide (existing-architecture
assumption) and contributions slide (novelty of the evaluation
methodology). Did not search the web, per instruction, only the thesis's
own already-verified sources. Gap-slide citation resolved directly:
`background.tex` supports both halves of the claim (`anthropic2024mcp`
for "trusted with raw data," `openai2025privacyfilter` for "denied
access entirely" via one-way redaction), both already in `biblio.bib`,
year fields checked directly against the `.bib` entries rather than
inferred from the citation keys (the `openai2025privacyfilter` key says
2025, the actual `year` field says 2026, used the field). Contributions
slide's novelty claim was originally unresolvable ("prove a methodology
didn't exist before" isn't a claim any citation can support), fixed by
reframing per the user's chosen option: cite the two closest existing
works already in the thesis (Hou et al. 2025, Albanese et al. 2026) and
state precisely what they don't test (tool-execution correctness),
instead of asserting a general absence.

**Point 4, MCP given its own slide.** The mechanism slide previously
carried three messages (diagram, two "Bound" annotations, an MCP
footnote); split so the diagram stands alone and MCP gets a dedicated
slide (what it is / why chosen / what without it), plain language, no
unexplained jargon including "tool calling." The two "Bound" boxes moved
to a new backup slide. Placement was corrected once by the user: the MCP
slide belongs after the end-to-end example, not before, so the committee
already has a concrete case to hang the explanation on.

**Point 5, four results cut to three.** The 12/12 correctness result
(lowest sample size, measures a stage already described as
deterministic) moved to backup. Every main-deck reference to it checked
and updated: the "instrument" slide's "reference system" line was
rewritten around a user-supplied replacement so it no longer promises a
result the main deck doesn't show.

**Point 6, jargon and slide order.** "Recall" removed from the one
main-deck title that used it unexplained (backup keeps it). "Tokenisation"
replaced with the deck's own established phrase ("placeholder
substitution"), in both the main contributions slide and the backup
architecture slide. The validation-method slide (mentions "mock
backend") moved out from between the gap and architecture slides to
right after MCP, before the results section, so the architecture is
established before the audience meets test-methodology vocabulary. The
product name "Antares AI" was relocated (not just left removed) to open
the "why four services" slide, so the committee knows what system is
being described before the first diagram, and also kept on the
validation-method slide per the user's explicit call (closes the loop
after two content slides with no product name).

**A supervisor-level read-through the user asked for explicitly**
(read the deck end to end as a non-technical committee would, list only
contradictions-between-slides and unexplained-jargon-on-first-use,
propose nothing) surfaced two real findings, both fixed in a follow-up
pass: the validation-method slide claimed "each [stage] on its own set
of test requests" while the leak-audit slide two slides later says it
"reuses the detection requests" (a real contradiction, not a rewording
choice); and "span," "placeholder," "payload," and "prompt" were each
first used in the main deck without ever being defined, "prompt" in
particular reintroducing vocabulary the deck otherwise avoids in favour
of "request." All four fixed with user-supplied exact wording where
given; one partial fix from an earlier pass ("span" removed from a
slide's first bullet but not its third) was caught and completed in
this pass too.

**Template alignment, requested last.** Switched the deck's visual
identity to match Lorenzo Attolico's co-defense deck, per the
supervisor's "use a common template" instruction from the *previous*
session (see entry below) — `\usetheme{moloch}` does not exist in
`tectonic`'s package bundle (confirmed twice, by direct test, not
memory) and was not force-installed; the user explicitly said stay on
`metropolis` (moloch's underlying theme, functionally and visually
identical, just distributed under a different name for a German
trademark reason) rather than risk a local package-file hack. `FiraSans`
was added successfully once its real constraint was found by testing,
not assumed: it must load *after* `\usetheme{metropolis}`, not before —
loading before crashes `tectonic` with a segfault (exit 139), a fact
established by direct reproduction at both the start and the end of this
session, not inferred. `\institute` simplified to "University of
Trento". Removed two now-unused preamble definitions (`vincolo` TikZ
style, `slideorange` color) after confirming with `grep` that nothing
referenced them anymore, following the Bound-boxes-to-backup move in
point 4.

**Global hyphen ban, carried over from a mid-session ad hoc request**
(not one of the six numbered points, came up separately): every literal
`-` in visible slide text was replaced with commas, colons, or spacing,
and `\hyphenpenalty=10000` / `\exhyphenpenalty=10000` were added to the
preamble after discovering `tectonic`'s automatic line-wrap hyphenation
was silently inserting a literal hyphen into a wrapped title
(`data ex-posure`) that no explicit edit had put there.

**Final state:** main deck 14 frames, 1 backup divider, 5 backup frames,
21 PDF pages (one `\pause` reveal on the gap slide adds a page). Order:
title, problem, gap+RQ, why-four-services, mechanism, end-to-end
example, MCP, validation method, detection (91.5%), leak audit (2/50),
routing (95.2%), limitations, contributions, thank you. Backup:
divider, four services, two design bounds, methodology detail,
correctness (12/12), full limitations list. Every build verified clean
via `uv run python build.py --clean` and a full page-by-page visual read
via the PDF-reading tool, not just a compile-success check, following
the same discipline as the prior slide session (silent beamer overflow
has no compile-time signal).

**Open items:** the gap slide's citation placeholder is now filled
(point 3 resolved both citations, not just one, contrary to what was
still open at the end of the point-3 discussion mid-session). No live
timed read-through has happened yet (carried over from the prior slide
session, still true). No speaker notes, by the same standing choice.
Whether this deck has actually been sent to the supervisor ahead of the
15 September 2026 defense is unconfirmed. `Tesi_UniTN/Impaginazione/inizio.tex`
and `Tesi_UniTN/frontespizio.sty` remain modified but deliberately
uncommitted from a prior session (see entry below), untouched again this
session; same for the untracked `Tesi_UniTN/tesi_Miglioranza_*.pdf` and
`professor_review_draft.md`. This session's own changes
(`slides/slide.tex`, new `slides/figures/unitn_logo.png`) were committed
and pushed separately from those pre-existing untouched items.

---

**Session close, 2026-08-30 (later session), branch `main`.** The thesis
was already delivered (see entry below); this session was scoped
entirely to building the defense slide deck for a Monday deadline,
starting from an internship demo skeleton the user copied into
`slides/` (`slide.tex`, `CNU.sty`, `final_runtime_flow.png`, `pic/`,
`ref.bib`).

**Structure chosen: Idea 3, "lead with the claim, defend it."** Out of
three proposed structures (mirror the three research questions; trace
one request live through the diagram; open with the closing claim and
defend it), the user picked Idea 3 and asked for a threat-model slide
added to the plan. Final 11-slide deck: title → the claim (3
preconditions from `conclusions.tex` §7.2) → motivation → architecture
(components, then the runtime-flow diagram) → threat model (STRIDE +
OWASP LLM Top 10, from `discussion.tex`'s existing `tab:threat_model`)
→ methodology → evidence mapped to the three preconditions → what the
evidence doesn't cover → claim restated → questions. A planning doc
(`slides/plan.md`) was written first with per-slide content and
reasoning, iterated with the user, then deleted once the `.tex` was
built from it, per explicit request.

**A significant discovery, found incidentally, not gone looking for.**
While fixing a Get/Pop wording mismatch the user flagged between a
slide bullet and the diagram, a checksum comparison showed
`slides/final_runtime_flow.png` (as the user had copied it in) was
byte-identical to `Tesi_UniTN/Immagini/antares_ai_secure_flow_corrected.png`
— the thesis's own Figure 3.1, referenced by `architecture.tex`. That
file had gone missing from disk (an uncommitted deletion, not caused by
this session) at the same time, which meant **the delivered thesis's
own diagram still said "pop, read + delete"**, contradicting the
Get-not-Pop text that earlier sessions spent considerable effort
getting right in `architecture.tex`/`discussion.tex`. Flagged this to
the user directly rather than silently fixing or silently committing
the file deletion. The user copied the (by-then-corrected) image back
into `Tesi_UniTN/Immagini/`; this session renamed it to the filename
LaTeX expects (`antares_ai_secure_flow_corrected.png`) and verified a
clean thesis rebuild with Figure 3.1 now correct (checked directly in
the compiled PDF, page 19). The image fix itself was a pixel-level
patch (Python/Pillow, run via `uv run --with pillow`): measured the
exact bounding box and font of the original "pop, read / + delete"
label, erased it with a matched white rectangle, and redrew "get, read
/ (non-destructive)" in the same font/size/color/position, verified not
to collide with the diagram's dashed connector line. Backup of the
pre-patch image left at `/tmp/final_runtime_flow.orig.png` (not
committed, session-local).

**Two real, silent beamer overflow bugs found and fixed** — content
clipped off the bottom of a frame with no compile error, only visible
by reading each rendered page in full: the "What the Evidence Doesn't
Cover" slide's seventh bullet was invisible until spacing was
tightened, and the "Why It's Hard" slide's fourth bullet was clipped
until it was shrunk. Also: the runtime-flow diagram, being nearly
square (2720×2640px), was constrained only by `width` and overflowed
past the bottom of its frame — including a legend row that was entirely
hidden — until also constrained by `height` with `keepaspectratio`. A
separate bug in the title page (`\\[4pt]` inside `\institute{}` leaking
literally into the footline, which reuses the same string) was fixed
with proper `\author[short]{full}`-style short forms.

**Two content-accuracy corrections from the user, both instructive.**
(1) After a "not X, not Y" pattern reappeared in a rewritten bullet
despite an earlier explicit ban on the construction (extending
`CLAUDE.md`'s own thesis-style rule to the slides), did a full sweep
and fixed every instance, not just the flagged one. (2) The user
caught a Redis Get/Pop bullet that had invented an unsupported causal
narrative ("Pop was tried, would only work once, so Get was chosen for
that reason") — "this is not actually what happened, dig better."
Rewrote it to state only what `discussion.tex` already establishes
(present-tense structural fact plus consequence: switching to `Pop`
today would break multi-call correctness; "a real, unresolved
trade-off," not a historical decision narrative), instead of
inventing thesis-adjacent history under time pressure. Both are now
useful as a general pattern: check literal instructions were actually
followed everywhere, not just where flagged, and never dress up a
present-tense structural fact as a decision history the record doesn't
support.

**Style passes, both user-initiated:** all sentence-level em dashes
(`---`) replaced with commas across the deck, deliberately leaving
compound-word hyphens (`non-destructive`, `server-side`, etc.) and the
Wilson CI numeric range (`89--98%`) untouched, since neither is the
construction being targeted and the CI range would be misstated by a
comma. Separately, "Why It's Hard" → "Motivation" and "What the
Evidence Doesn't Cover" → "Limitations of the Evidence," with the
bullet prose under both rewritten to drop contractions and informal
phrasing.

**Title slide fixes:** co-supervisor's company corrected to Saidea
S.r.l. (was wrongly Delta Informatica); added the full list of all
seven Data Science interdepartmental programme departments (the user
first asked for just one, matching `inizio.tex`'s single
`\Dipartimento{}` field, then clarified they wanted all seven — this
is an interdepartmental UniTN programme, not a single-department one),
sized down twice on request (`\footnotesize` → `\scriptsize` →
`\tiny`) to keep the title page from feeling crowded.

**Infrastructure:** `slides/build.py` added, mirroring
`Tesi_UniTN/build.py`'s `uv run python build.py [--clean|--open]`
interface exactly, so the user can rebuild independently. `.gitignore`
gained `slides/slide.pdf` (build output, same convention as
`Tesi_UniTN/main.pdf`). Every edit this session was verified with a
full `uv run python build.py` plus a page-by-page visual read via the
PDF-reading tool before being reported as done — necessary because the
overflow bugs above were real and silent, with no compile-time signal.

**Git state:** nine commits made this session, all pushed to
`origin/main` (`5807bfe` through `83b7f0d`), each scoped tightly to
only the file(s) actually touched by that step. Deliberately excluded
from every commit: `Tesi_UniTN/Impaginazione/inizio.tex` and
`Tesi_UniTN/frontespizio.sty`, both still modified in the working tree
per the prior session's explicit "don't commit yet" instruction (see
entry below) — untouched again this session; and the untracked
`Tesi_UniTN/tesi_Miglioranza_*.pdf` / `professor_review_draft.md`,
also untouched.

**Open items for next session:**
1. No live timed read-through has happened. The planning doc estimated
   ~14:00 of the 15-minute slot before it was deleted; that number was
   never verified against actual speaking pace and doesn't survive
   anywhere but this note.
2. No speaker notes were added to `slide.tex` (`\note{}`), by explicit
   user choice — narration is left to the presenter.
3. Whether the Monday deadline was met, and whether the deck was
   actually sent to the professor, is unconfirmed as of this write-up.
4. `Tesi_UniTN/Impaginazione/inizio.tex` and `Tesi_UniTN/frontespizio.sty`
   remain uncommitted from the prior session — check with the user
   before assuming they're ready to commit now that slide work has
   also landed on `main`.
5. The threat-model table (slide 6) still lists a "Caller identity
   fallback" row; the equivalent bullet was removed from slide 9 on
   request, but the table row was left in place since it wasn't asked
   for — worth confirming that asymmetry is intentional.

---

**THESIS DELIVERED — 2026-08-30.** The thesis has been submitted/handed
in. This session (short, front-matter only) fixed the title page
(`Tesi_UniTN/Impaginazione/inizio.tex`, `Tesi_UniTN/frontespizio.sty`):
added `\Dipartimento{Dipartimento di Sociologia e Ricerca Sociale}`
above the existing `\CorsoDiLaurea` line, and replaced the bottom
"Final examination date: September 15, 2026" line with "Anno Accademico
25/26" (dropped the hardcoded "Final examination date:" label in the
`.sty` so `\DataEsame`'s value prints on its own). Rebuilt clean each
time via `uv run python build.py`. **Per explicit user instruction, this
session's changes were NOT committed or pushed** — working tree has
`Tesi_UniTN/Impaginazione/inizio.tex` and `Tesi_UniTN/frontespizio.sty`
modified, plus untracked `Tesi_UniTN/tesi_Miglioranza_257311.pdf`,
`Tesi_UniTN/tesi_Miglioranza_Ettore_257311.pdf`, `professor_review_draft.md`,
and a `slides/` directory — none of these were reviewed or touched this
session beyond what's described above. Any future session should check
with the user before assuming further thesis-content changes are wanted
now that it's delivered.

---

Session close, 2026-08-25. Continuation of the review-response work:
after the Pop/Get disclosure landed (see entry below), the user pushed
back on how it read — the "nothing in the project record states this
as intentional" framing, repeated near-verbatim in `architecture.tex`
§3.4, `Implementation.tex`, and `discussion.tex` §6.1, sounded like
flagging an oversight the author only noticed after the fact. Reworded
all three to state the same fact (server-side deanonymisation uses
`Get`, not `Pop`; mappings are never removed by the application) without
the meta-commentary on intent — same substance, neutral tone. Commit
`66a4db5`.

Also did a careful line-by-line consistency check of a professor-facing
email draft the user was writing (summarising how all 12 review points
were addressed) before it went out: caught that "l'affermazione che il
client non ha business logic era falsa" mislabelled which clause of the
original sentence was actually false (it was "holds no sensitive data",
not "performs no business logic", which stayed true throughout), and
that an early draft of the Pop/Get explanation claimed the user had
personally set `Get` "during validation, for more test cases" — which
contradicted the thesis's own "not documented as intentional" phrasing
at the time. Resolved by giving neutral wording that states the fact
without claiming either deliberate-intent or accidental-oversight, so
it's compatible with the thesis regardless of which history is true.

`review-response-lit-depth` merged into `main` (fast-forward,
`0902829..66a4db5`, later `88bd8f4` for a checkpoint-only sanity-check
commit) and pushed to `origin/main`. `Tesi_UniTN/main.pdf` untracked
and physically deleted from disk per item 2 of the supervisor's review.
Verified with a clean `git fetch` that `origin/main` matches local
`main` exactly — confirmed twice after the user reported not seeing the
push (turned out to be a stale GitHub page view, not an actual gap).

Separately, produced a short list (page numbers in the compiled PDF, no
prose) of every passage in the thesis that makes a factual claim about
the *real* Antares/Miorelli system (ERP description, the management
data-boundary constraint, the "large volume of personnel data" claim,
the real-tenant migration path, the "agreed with the host company"
scope decision) as opposed to the mock/stub `MiorelliServiceStub`
content, for the user to hand to their internship tutor for a fast
company-side accuracy check. Not saved to a file — given directly in
chat, already copy-pasted by the user.

Final build clean (`uv run python build.py`), PDF sent to the user
twice via `SendUserFile` in this session for their own review and to
attach to an email. Branch state: `main` and `review-response-lit-depth`
both at `88bd8f4`, both pushed, working tree clean.

---

Last updated: 2026-08-25, same branch (`review-response-lit-depth`),
follow-up session. After the previous session's Pop/Get softening
landed (commits `deabd1e`, `9a5d377`), the user — who knows the actual
implementation — confirmed directly that the real system always calls
`Get`, never `Pop`: contexts are never removed by the application on any
path, only cleared when the Redis process itself restarts (no
persistence volume, no TTL). This is a reversal of the standing
[[feedback_thesis_codebase_scope]] decision from two sessions ago (which
kept private-source findings out of the thesis) — the user explicitly
asked this time to disclose it as a named limitation instead of staying
silent on the mechanism, and to explain clearly, in the architecture
chapter and in the Ch.5 UC-A passage, that deanonymisation runs as the
first action of *every* individual business-tool invocation (not once,
centrally, after Claude picks a tool), which is why three separate tool
calls sharing one `contextId` don't collide under `Get`.

Rewrote every touched passage across `architecture.tex` (§3.1's
"End-to-end security" bullet, §3.4's `/deanonymize-known` description,
§3.6.1's Redis-atomicity paragraph, §3.6.3's worked deanonymisation
trace), `Implementation.tex` (`IAnonymizationContextStore` description),
`discussion.tex` (§6.1 security/complexity trade-offs, split into "what
was a deliberate scope decision" — no TTL, no persistence volume — vs.
"what is an unexplained implementation gap" — Get instead of Pop; §6.3
scalability paragraph), `conclusions.tex` (§7.1, §7.2), and
`Validation.tex`'s UC-A multi-call passage (now gives the full causal
chain: per-invocation deanonymisation → three separate `/deanonymize-known`
calls on one `contextId` → no collision because `Get` is non-destructive
→ this says nothing about what a genuinely one-time-use `Pop` would have
done). Every passage cross-references the others rather than repeating
the same explanation. Note for future sessions: this claim (`Get`
instead of `Pop`) rests on the actual C# source, not on
`internship_documents/anonymization-service.md`, which still documents
`Pop` as the mechanism — the docs and the real code disagree here, and
only the thesis now reflects the code. Clean `uv run python build.py`
after every edit; independent grep for banned ToV patterns on all
touched files came back clean. Committed and pushed (see Git state).

---

Last updated (previous entry): 2026-08-24, new session on branch `review-response-lit-depth`
(one commit, `af15762`, ahead of `main`). Asked to independently review,
as a critical outside reader, whether the committed 12-point response
actually held up — not just re-read the checkpoint's own self-report.
Found and fixed a real internal contradiction the committed session had
missed: `architecture.tex` §3.4 stated `/deanonymize-known` is one-time-use
and that a repeated call with the same `contextId` "will find no context
and fail cleanly," while the same commit's own new Ch.5 UC-A multi-call
analysis reports 2 of 5 canonical-prompt repetitions issuing three
separate deanonymize calls against one `contextId`, all succeeding. Fixed
by softening the Ch.3/Implementation.tex claims to state one-time-use as
design intent rather than an operational guarantee, and adding explicit
cross-references between `architecture.tex` §3.4/§3.6.1, `Implementation.tex`,
and `Validation.tex`'s UC-A passage so the tension is visible to a reader
in either direction, without asserting a mechanism this thesis doesn't
measure (consistent with [[feedback_thesis_codebase_scope]] — no new
forensic disclosure, only removal of an unsupported claim). Also cleaned
up two ToV/overclaiming leftovers a fresh grep sweep caught that the
committed session's per-chapter agents missed: "highlights" in the
abstract's closing sentence (`inizio.tex`), and an absolutist "must
preserve full business logic accuracy" line in `architecture.tex` §3.2
(reworded as a design objective checked in Ch.5, not asserted as fact).
Clean `uv run python build.py` after every edit. Not yet committed on
this branch — see Git state below. A full Italian-language report
answering the professor's 12-point review (items 4–13; items 1–3 were
administrative/personal and out of scope) was written directly in chat
for the user to send, not saved to a file.

---

Last updated (previous entry): 2026-08-24, same session continued (after the 12-point
review below landed, the user separately said the "skinny thesis"
complaint hadn't really been addressed and asked for a literature-depth
expansion pass across all 7 chapters, run as: 7 parallel forks surveying
each chapter for genuine literature-groundable gaps → synthesised into 5
themes (GLiNER/NER, Redis, MCP/security foundations, validation metrics,
privacy engineering/GDPR) → 5 parallel forks doing deep bibliographic
research per theme → ~30 citation placements written into all 7 chapters
→ 5 parallel independent verification agents re-checking every claim
against the actual cited sources, including recomputing a statistic by
hand. Verification caught 4 real problems, all fixed: a stubbs2015
citation whose claim was directly contradicted by the paper's own
results table, a Redis-atomicity claim in Implementation.tex that
doesn't hold for the actual `Pop` implementation (fixed by softening the
claim, not by disclosing the underlying implementation gap — consistent
with this session's earlier codebase-scoping decision, see
[[feedback_thesis_codebase_scope]]), a citation pointing at the wrong
Deloitte report for a statistic, and a mismatched Redis Cluster/Sentinel
citation. `biblio.bib` grew from 46 to 76 entries. Full detail in the
dedicated section below, after the 12-point review writeup it follows.
Not yet committed — see Git state.

---

Last updated (previous entry): 2026-08-24, later session (user gave a 12-point review of
the draft — items 2–13, no item 1 — covering git hygiene, a cross-reader
ask, depth/tone complaints about Chapter 5, an AI-disclaimer question,
overall "too much Claude ToV," a request to tie Ch.5's validation results
back to the Ch.1 research questions, a demand for a deeper root-cause
explanation of the GLiNER date-range false negatives instead of "Italian
is hard," a request to clarify the UC-A three-tool-call behaviour (and
whether it contradicts Ch.4's "exactly one sub-tool" system-prompt
claim), a real internal inconsistency in Ch.3's deanonymization worked
example, an MCP-protocol-currency check, an overclaiming client-PII
sentence in Ch.3, and an abstract/intro realignment ask. All 12 items
addressed this session — see the dedicated section below. Not yet
committed, see Git state).

This file is a working checkpoint for picking the thesis back up in a new
session. It is not a memory file and not documentation of the codebase —
it is a snapshot of where the writing stood the last time someone closed
the laptop. Update it at the end of any session that changes chapter
status, not mid-session.

---

## Chapter status

| # | Chapter | File | State |
|---|---------|------|-------|
| 1 | Introduction | `capitoli/Introduction.tex` | **Written**, revised this session — one "not X, but Y" construction fixed in §1.2, the three research questions in §1.3 rewritten to vary sentence template (were three identical "The Nth question is...: " openers back to back), two stray "demonstrated" buzzword hits fixed. This is the only chapter the ToV sweep was allowed to touch beyond Ch.5/3 this session — see below |
| 2 | Background & Related Work | `capitoli/background.tex` | **Written**, revised this session — new paragraph on MCP protocol currency (item 11: the implemented system targets the Nov 2024 spec baseline; Streamable HTTP replaced HTTP+SSE as of 2025-03-26, OAuth 2.1 authorization added since), one new independently-verified `biblio.bib` entry (`mcp2025specnov`). ToV fixes: one "demonstrated", one dangling "-ing" tag, one "this chapter has shown"-style closing paragraph reworded |
| 3 | System Architecture | `capitoli/architecture.tex` | **Written**, revised this session — two real fixes, not just style: §3.6.3's deanonymization worked example was internally inconsistent with §3.6.1's own token mapping (claimed `<LOCATION_0001>` deanonymizes to the full address "Bergamo Via della Fonda 5" when §3.6.1 maps it to "Bergamo" alone) — fixed to match. §3.2's client-PII claim ("holds no sensitive data") was overclaiming — the client constructs the raw prompt itself, so it transiently holds cleartext PII before the anonymization call; reworded to say precisely what is and isn't true. Three "is/are avoidance" ToV fixes (`serves as` × 2, `acts as` × 1) |
| 4 | Implementation Details | `capitoli/Implementation.tex` | **Written**, revised this session — ToV only: one "demonstrate", one "it is worth being explicit about" formulaic transition, two of nine "X, not Y" contrastive constructions reworded for variety (rest left as legitimate technical distinctions) |
| 5 | Use Cases & Validation | `capitoli/Validation.tex` | **Written, substantially rewritten this session** — this was the core of the session's work, see the dedicated section below. New: a deepened, evidence-grounded UC-A multi-call discussion (call pattern varies across the 5 repetitions: 3 separate / 1 merged / 2+1 split, not a fixed "three times"), a structural root-cause hypothesis for the GLiNER date-range false negatives (range spans vs. the bare `"date"` label, tied to UC-C), and a new closing subsection explicitly mapping all three Ch.1 research questions to what this chapter measured and what it doesn't establish. Plus ToV fixes: three repeated-paragraph-template instances varied, two "It is worth" transitions cut |
| 6 | Discussion & Future Work | `capitoli/discussion.tex` | **Written**, revised this session — new paragraph on MCP transport/authorization migration (item 11, pairs with the Ch.2 addition). ToV fixes: one "demonstrate", two "X, not Y"/"not X; it is Y" constructions reworded |
| 7 | Conclusions | `capitoli/conclusions.tex` | **Written**, revised this session — reread for consistency after the Ch.3/5 fixes above, no factual claim needed changing. ToV fixes only: two "not X, it Y" constructions reworded, two sentence-length-monotony paragraphs (5 and 4 long sentences in a row) each got one short punctuating sentence added, one "not X but Y" reworded |

All seven chapters have full prose. `Impaginazione/inizio.tex`'s abstract
was also revised this session (see below) — two overclaiming phrases that
had been fixed in `Introduction.tex` in the 2026-08-20 session were never
mirrored into the abstract; now fixed there too. The AI disclaimer was
promoted from a footnote to a standalone paragraph before the table of
contents.

## Git state

- Worked directly on `main`, no `dev` branch. `main` was at `0902829`
  (the supervisor-feedback / back-matter-cleanup commit) at the start of
  this session, working tree clean apart from the self-referential
  `CHKPNT.md` update from the previous session (see below).
- **This session's changes are not yet committed.** Working tree has
  `.gitignore`, `CHKPNT.md`, `CLAUDE.md`, `Tesi_UniTN/biblio.bib`,
  `Tesi_UniTN/Impaginazione/inizio.tex`, and all seven
  `Tesi_UniTN/capitoli/*.tex` files modified, plus `Tesi_UniTN/main.pdf`
  staged as deleted (untracked per item 2 below, still present on disk).
  Commit when asked — this session did a lot in one sitting and the user
  has not yet asked for a commit.
- **Practice change (item 2 of this session's review): `Tesi_UniTN/main.pdf`
  is no longer tracked in git.** Added to `.gitignore`, removed from the
  index with `git rm --cached` (kept on disk). Anyone pulling the repo
  now builds their own copy via `uv run python build.py` instead of
  relying on a possibly-stale committed PDF.
- Diff logs for every completed feedback point plus the one external
  correction from prior sessions still live in `Tesi_UniTN/diff/`:
  `narrow_the_privacy_claims.txt`,
  `distinguish_deterministic_execution_from_correctness.txt`,
  `correct_the_persistence_description.txt`,
  `reframe_the_contribution_and_novelty.txt`,
  `clarify_the_prototype_scope.txt`,
  `correct_uc_a_tokenization_example.txt`. No new diff log written in the
  2026-08-20 session (it responded to a professor email, not a numbered
  feedback point) or this session (it responds to the user's own 12-point
  review, not a numbered feedback point from the professor's round
  either).

## What happened this session (2026-08-24, later session)

The user opened the session by asking to build up context (per this
file and `internship_documents/`), then gave a 12-point review of the
draft — numbered 2 through 13, item 1 was not included in their message.
A plan was written (`/Users/ettoremiglioranza/.claude/plans/ancient-questing-owl.md`)
covering all 12 items, refined once after the user corrected the scoping
(see below), approved, and executed in full.

**Items 9, 10, 12 — investigation and a scoping correction that matters
for future sessions.** Items 9 (UC-A's "three tool calls" behaviour), 10
(a Ch.3 worked-example puzzle: deanonymizing one token returned a value
that didn't match its own stated mapping), and 12 (does the MCP client
actually see PII?) read like they might be real bugs, not just prose
issues. Investigated directly against the actual implementation repo,
`/Users/ettoremiglioranza/Projects/AI-powered-workforce-management-system`
(source + raw validation logs from the 2026-08-06 run), not by guessing.
Found real things: `IAnonymizationContextStore.Pop` (the "atomic
read-and-delete" the thesis describes) is declared and implemented but
never called anywhere in the actual code — `Deanonymize()` uses
non-destructive `Get()` instead, so Redis contexts are never removed on
any path, a bigger persistence gap than what the thesis states. The user
then corrected the approach directly: the professor and any other reader
have no access to that codebase and cannot cross-check it, so the
thesis's real coherence obligation is to itself and to
`internship_documents/`, not to whatever gets found in private source —
"turn things in our favour regarding the codebase." This is now saved as
a standing memory ([[feedback_thesis_codebase_scope]] in the user's
auto-memory) for future sessions: don't introduce a new, more damaging
finding into the thesis purely because private source-reading surfaced
it, if it isn't already reflected in the docs or an existing validation
artifact the thesis already draws on. The `Pop`-is-dead-code finding was
therefore **not** written into the thesis. What *was* fixed: item 10
(Ch.3's worked example now matches its own stated token mapping, a plain
internal-consistency fix needing no code claims at all) and item 9 (the
UC-A multi-call discussion in Ch.5 was rewritten using data from
`Validation/results/routing_eval_results.json`, which the validation
pipeline already produced and the thesis already draws on in earlier
sessions — legitimate, not new forensic digging), reporting the real
call-pattern variance (3 separate calls / 1 merged / 2+1 split across the
5 repetitions) and naming, without asserting Redis internals, that the
observed safety is dataset-specific rather than architecturally
guaranteed. Item 12 was fixed directly from `internship_documents/mcp-
client.md`, no code access needed — the client does construct the raw
prompt (with real PII) before calling `/anonymize`, so "holds no
sensitive data" was a real overclaim, now corrected.

**Items 4, 7, 8 — Chapter 5 substantially rewritten**, per the user's
explicit "parti da Ch.5" instruction. Added: a deepened GLiNER
false-negative discussion with a structural hypothesis for the
date-range misses (range spans vs. the bare `"date"` label with no
`"date range"`/`"period"` option, tied explicitly to UC-C's absence-
period phrasing) instead of "Italian is hard"; a new closing subsection
(`subsec:usecases_rq_mapping`) mapping each of the three Ch.1 research
questions to exactly what Ch.5 measured and what it doesn't establish,
directly answering the "gap between strong claims and partial
validation" complaint; a more discorsivo register throughout the edited
passages.

**Item 11 — MCP protocol currency.** Confirmed via web research: the
implemented system targets the Nov 2024 MCP spec baseline; Streamable
HTTP replaced HTTP+SSE as the transport as of the 2025-03-26 revision,
and an OAuth 2.1 authorization framework was added, both absent from the
original spec. New paragraphs in `background.tex` §2.2 and
`discussion.tex` (production-migration section), one new `biblio.bib`
entry (`mcp2025specnov`), independently verified by a separate agent
(all three thesis-side claims came back CONFIRMED, nothing fabricated or
misdated).

**Item 5 — AI disclaimer.** Already existed as a footnote (the user
caught my own initial "it's missing" claim mid-investigation — I'd
mis-assessed this). Asked the user directly what the actual concern was;
answer was visibility, not wording. Promoted from a footnote on the
Acknowledgments heading to a standalone paragraph before
`\tableofcontents`, substance unchanged.

**Item 13 — abstract/Introduction realignment.** Found two overclaiming
phrases in the abstract (`Impaginazione/inizio.tex`) that had been fixed
in `Introduction.tex` in the 2026-08-20 session but never mirrored into
the abstract itself: "preserving full operational correctness" (dropped,
matching how Introduction.tex handled it) and "preserves the correctness
of business logic throughout the entire request lifecycle" (reworded to
state it as a design objective checked against measurement, not an
established fact). `Introduction.tex` itself needed no further changes —
already properly hedged.

**Item 2 — git practice.** `Tesi_UniTN/main.pdf` added to `.gitignore`
and untracked (`git rm --cached`, kept on disk) — it goes stale easily
and should be built locally, not committed.

**Item 3 — Lorenzo Attolico cross-read.** The user's own action, not
something done in-session.

**Item 6 — full ToV sweep, in full, not deferred.** Researched current
Claude/Sonnet writing tells beyond what `CLAUDE.md` already banned
(primarily against Wikipedia's actively maintained "Signs of AI writing"
page, plus 2025 corpus research on AI-influenced academic vocabulary).
Updated `CLAUDE.md`'s "Thesis Writing Style" section with the new
patterns: is/are avoidance, manufactured dangling "-ing" analytical
tags, vague connective filler, an extended buzzword list, the "despite
X, faces challenges" formula, repeated paragraph shape, distanced
impersonal hedging. Launched 7 parallel read-only agents, one per
chapter, against the full (updated) pattern list — all reported back
clean overall, mostly borderline "X, not Y" contrasts that turned out to
be legitimate precise technical distinctions rather than padding. Per
the user's explicit instruction, fixed Chapter 1 first and stopped to
report before continuing — the user then said "go ahead with every
chapter, you have my permission," and the remaining six chapters were
fixed in the same sitting. This 5-step workflow (research → update
CLAUDE.md → parallel per-chapter identification agents → fix chapters
myself → checkpoint after the first chapter) is now saved as a standing
memory ([[feedback_thesis_tov_sweep_workflow]]) for future "clean up the
AI tone" requests.

**Verification throughout:** clean `uv run python build.py` after every
edit pass across the whole session (only the pre-existing
overfull/underfull hbox warnings, no new errors, no undefined
citations). A final grep sweep across every chapter for the core and
extended buzzword lists, formulaic transitions, and em dash counts
turned up two more stray "demonstrated" instances the per-chapter agents
had missed (`Introduction.tex`'s and the abstract's opening sentences,
both "LLMs have demonstrated..." — likely from when the two were drafted
in parallel), fixed directly.

**Not yet done:** none of this session's twelve items were left
incomplete. The one thing genuinely deferred is item 3 (Lorenzo
Attolico), which was never this session's to do. See Open items below
for what a fuller line-by-line read-through (not grep/agent-driven)
might still turn up, and whether a commit is wanted.

## What happened next, same session: literature-depth expansion ("skinny thesis")

After the 12-point review above landed, the user said the professor's
"la tesi è ancora molto skinny" complaint hadn't really been addressed
at the scale it calls for, and asked for a structured literature-depth
pass: survey every chapter for genuine gaps, synthesise into ~5 themes,
research each theme properly, write real additions, then counter-check
everything. Ground rule throughout, stated explicitly by the user: every
addition had to explain a real mechanism, compare to a real alternative,
or ground a design choice already made — never a sentence added just to
raise a citation count.

**Phase 1 — chapter survey.** 7 parallel forks, one per chapter,
identified candidate spots (2–7 per chapter) where a literature-grounded
explanation would deepen the content, with explicit priority on GLiNER,
Redis, MCP, and validation metrics per the user's instruction. All 7
reported back; `Introduction.tex` came back thinnest (one real
candidate), `background.tex` and `Validation.tex` richest.

**Phase 2 — synthesis and deep research.** The ~35 candidate spots
grouped cleanly into 5 recurring themes: GLiNER/zero-shot NER, Redis/
in-memory architecture, MCP protocol foundations and classical security
theory, validation/evaluation methodology, and privacy engineering/GDPR
depth. 5 parallel forks did deep bibliographic research per theme,
instructed explicitly not to just confirm suggested candidate papers but
to independently verify them — several were corrected or replaced during
this pass already (e.g. a PR-curve-methodology paper was swapped for a
more NER-specific one). Result: ~28 real, individually-checked sources,
reported to the user in full before writing anything.

**Phase 3 — writing.** All ~30 citation placements written into all 7
chapters (`background.tex` got 9, the richest; `Introduction.tex` got 1,
the leanest), plus 28 new `biblio.bib` entries (46 → collected in one
batch, then 2 more added mid-writing for the Introduction.tex item and a
Redis-latency split, landing at 76 total). Every addition is 1–4 real
sentences of explanation tied to a citation, not a citation bolted onto
unchanged prose. `uv run python build.py` run after every chapter's
edits, clean throughout.

**Phase 4 — independent verification, per the user's explicit
"counter-check" request and this repo's standing citation-verification
process.** 5 parallel fresh (non-fork) agents, one per theme, each
re-verifying every citation in that theme from scratch: does the source
exist, does it actually say what the thesis claims, is the bib entry
correct. Explicitly instructed to recompute any stated numbers rather
than trust them. **4 real problems found and fixed:**

1. **`stubbs2015deidentification`** (background.tex) — the thesis
   claimed the paper showed "systems tuned for recall... outperforming
   precision-tuned alternatives." The verifier read the paper's actual
   Table 2: every one of the 10 systems has precision *higher* than
   recall, the opposite of the claim, and the paper never makes a
   recall-vs-precision system comparison at all. Reworded to what the
   paper actually argues (a coverage/binary-detection scoring rationale,
   which the thesis already uses via `sundheim1995muc6` elsewhere).
2. **`redis2025docs`** (Implementation.tex) — a new sentence claimed
   Redis's single-threaded execution guarantees no two concurrent `Pop`
   calls on the same context can both succeed. The verifier actually
   read `RedisAnonymizationContextStore.Pop` in the real implementation
   repo and found it issues a separate `Get` then a separate
   `store.Remove()` — two independent commands, not one atomic
   operation — so the claim as written is false. **Fixed by softening
   the thesis sentence to only claim what's true** (each individual
   Redis command is atomic), not by writing the race condition into the
   thesis — consistent with this session's earlier, explicit decision
   (see [[feedback_thesis_codebase_scope]]) not to introduce new
   findings from private source-reading that the existing documentation
   and `internship_documents/` don't already support. This is a
   citation-accuracy fix (my own added claim didn't hold up), not new
   forensic disclosure.
3. **`deloitte2024genai` → renamed `deloitte2024ethics`** (Introduction.tex)
   — cited the wrong Deloitte report. The 40%-cite-privacy-as-top-concern
   statistic is from Deloitte's "State of Ethics and Trust in Technology"
   survey (~1,848 respondents, Sept 2024), not the Q4 2024 "State of
   Generative AI in the Enterprise" pulse survey, which covers different
   material entirely. Bib entry replaced, citing sentence reworded (also
   dropped an unverifiable "ahead of cost, accuracy, or workforce impact"
   ranking claim, and corrected "roughly doubled" to the precise
   25%→40% figures).
4. **`redis2025cluster`** (discussion.tex) — one bib entry's title
   claimed to cover both Redis Cluster and Redis Sentinel, but only
   linked the Cluster spec URL; the Sentinel claim had no real source.
   Split into two entries (`redis2025cluster`, `redis2025sentinel`),
   cited separately. Also fixed a mismatched citation in
   `architecture.tex` (a latency claim was pointing at Redis's
   Transactions doc, which never discusses latency) by adding a
   dedicated `redis2025latency` entry.

23 of 27 unique checks came back CONFIRMED outright, including a fully
independent recomputation of the Wilson score confidence interval added
to the routing-accuracy figure (100/105 trials) — the verifier
recalculated it in Python from scratch and confirmed "roughly 89% to
98%" is accurate. One additional minor fix (a missing co-author on the
JSON Schema spec entry) was applied directly by that verification agent.

All fixes rebuilt clean. `biblio.bib`: 76 entries total. Every new key
confirmed cited at least once, no orphaned entries, via a final grep
sweep across all chapters.

## What happened in the 2026-08-20 session

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

1. **A draft Italian reply email to Prof. Miorandi was prepared in the
   2026-08-20 session (in chat, not saved to a repo file) but sending it
   was not confirmed in-session.** It summarises exactly what changed in
   response to his three points (§6.2 alignment, "True accuracy" and
   overclaiming wording, Ch.2 bibliography) plus the unprompted Ch.5/6
   citation additions and the back-matter cleanup. Check with the user
   whether it was actually sent before assuming the professor has seen
   this round of fixes.
2. **A citation-related issue was flagged by the user as broken in the
   final PDF, in an even earlier session, but was never independently
   reproduced.** Still unresolved, still no concrete repro. The
   2026-08-20 session added 12 new `biblio.bib` entries (34 → 46)
   without hitting the symptom, and the clean `tectonic` build after
   every pass showed no undefined-citation warnings, but that doesn't
   rule out whatever the user originally saw. Ask for a concrete example
   (which citation, where in the PDF) if it resurfaces.
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
   known overclaiming, internal-consistency, or citation-support issues**
   in the specific spots the professor or the user flagged, or that this
   session's 7-agent ToV sweep surfaced. That sweep was pattern-driven
   (a fixed banned-construction list applied per chapter), not a
   line-by-line read for factual/argumentative soundness — a slower full
   read-through could still turn up something neither the grep sweeps
   nor the pattern agents were built to catch.
6. **This session's changes are uncommitted, and now substantial.**
   Modified: `.gitignore`, `CHKPNT.md`, `CLAUDE.md`, `Tesi_UniTN/biblio.bib`
   (46 → 76 entries), `Tesi_UniTN/Impaginazione/inizio.tex`, all seven
   `Tesi_UniTN/capitoli/*.tex`; `Tesi_UniTN/main.pdf` untracked. Two
   distinct pieces of work landed in one sitting — the 12-point review
   (git hygiene, Ch.5 rewrite, Ch.3 fixes, MCP currency, abstract
   realignment, full ToV sweep) and the literature-depth expansion
   (~30 citation placements across all 7 chapters, independently
   verified). Worth reviewing the diff, and possibly worth splitting
   into two commits along that boundary rather than one, before pushing.
7. **The `Pop`-vs-`Get` finding from this session's codebase
   investigation was deliberately left out of the thesis** (see the
   dedicated write-up above and [[feedback_thesis_codebase_scope]] in
   memory) — not a TODO, a documented decision. Don't reintroduce it
   without checking with the user first, even if it resurfaces on a
   future investigation of the same external repo. Note it resurfaced
   indirectly during the literature-expansion citation verification (a
   new Redis-atomicity claim didn't hold up against the real `Pop`
   implementation) — that was fixed by softening the thesis's own claim,
   not by disclosing the gap, staying consistent with this decision.
8. **Three citations carry a residual, lower-confidence flag worth a
   second look before the defense, even though verification confirmed
   them:** `sundheim1995muc6` (MUC-6's precise scoring mechanics are
   formally defined in a companion paper by Chinchor in the same
   proceedings volume, which Sundheim's own paper defers to — the
   citation is defensible as used, just worth knowing), `ietf2025oauth21`
   (an active but still-changing IETF draft, correctly cited with an
   access date rather than a pinned revision, but will keep incrementing
   revision numbers), and `qu2024toollearning` (minor year ambiguity
   between the arXiv submission, 2024, and the journal's formal issue
   date, which some indexes list as 2025 — `year={2024}` is defensible
   but not the only reasonable choice).

## Next session

1. Confirm whether the draft email to the professor was sent (still
   pending from the 2026-08-20 session); if not, it's still available to
   send (see Open items above).
2. Chase down the citation-system symptom flagged above before adding
   any more `biblio.bib` entries — get a concrete example first.
3. Optionally tackle point 3 (threat model) if time allows.
4. Optionally re-run the UC-C validation inside the mock dataset's date
   window for a fuller substitute-finding trace before the defense.
5. Ask the user whether to commit this session's changes (see Open item
   6 above) — a large, reviewable diff, not yet committed, possibly
   worth two commits rather than one.
6. A full line-by-line read-through pass (not pattern/grep-driven) for
   cross-chapter consistency, argumentative soundness, and any remaining
   overclaiming language would still be worthwhile before considering
   the thesis defense-ready — every pass so far, including this
   session's, has been targeted at specific flagged issues or a fixed
   pattern list, never exhaustive. With ~30 new literature-grounded
   passages added this session, this read-through matters more than it
   did before — check that the new material reads as integrated
   explanation, not a bibliography exercise bolted onto existing prose.
