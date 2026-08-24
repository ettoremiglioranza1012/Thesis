# Project Context — Antares AI / Thesis

At the start of every conversation, first read `CHKPNT.md` in the repo root. It is a session checkpoint: which chapters are written, what was done last session, what's open, and what to do next. It is not documentation of the codebase and can go stale — treat it as a starting point to confirm against the actual files, not as ground truth on its own. Update it at the end of any session that changes chapter status.

Then read all files in `internship_documents/` in parallel to load full project context:

- `internship_documents/Internship_information.md`
- `internship_documents/README.md`
- `internship_documents/mcp-server.md`
- `internship_documents/anonymization-service.md`
- `internship_documents/gliner-service.md`
- `internship_documents/mcp-client.md`
- `internship_documents/miorelli-client.md`
- `internship_documents/Final_Internship_Report.pdf` (pages 1–9)
- `internship_documents/Slides_Progetto_AI_Antares_Demo.pdf` (pages 1–13)

After reading, briefly confirm context is loaded and note the approximate context window usage (target: under 50% of 200K tokens).

---

# Thesis Writing Style — AI Pattern Avoidance

When writing or editing thesis prose, **never** use the following patterns. They are strong signals of AI-generated text and must be actively avoided.

## Banned constructions

**Em dash overuse.** Do not use `---` as a dramatic pause or parenthetical substitute. One or two per page is already a lot. Use commas, parentheses, or restructure the sentence instead.

**Rule of three.** Do not group ideas into triplets just because it sounds satisfying: "X, Y, and Z". If two things are enough, use two. If four are real, use four. Triplets chosen for rhythm rather than content are an AI tell.

**"Not X, but Y" contrasts.** Avoid "not merely X, but Y", "not an add-on but a foundational principle", "not just X — it's Y". These read as manufactured depth. Say the positive thing directly.

**Buzzwords.** Never use: *delve*, *crucial*, *testament*, *tapestry*, *nuanced*, *robust* (when describing software), *seamless*, *holistic*, *dynamic landscape*, *navigating*, *paramount*, *foster*, *underscore* (as a verb), *demonstrate* (prefer *show*), *facilitate* (prefer *allow* or *let*).

**Formulaic transitions and conclusions.** Do not write: "In conclusion", "Ultimately", "It is worth noting that", "It is important to emphasise that", "This chapter has shown that", "As discussed above". Cut them. The content should speak without a narrator announcing it.

**Vague positivity and diplomatic hedging.** Avoid phrases that soften every claim into mush: "it can be argued that", "it is generally accepted that", "in many cases", "to some extent". If a claim is true, state it. If it has a condition, state the condition precisely.

**Sentence-length monotony.** Vary sentence length deliberately. Short sentences land harder. A long sentence that develops a thought through several clauses can carry real weight, but only if it is followed by something shorter that punctuates it. Never write five sentences in a row of roughly the same length.

**Perfect-but-sterile formality.** Academic writing can use contractions occasionally. "It's", "doesn't", "won't" are not informal — they are normal English. A thesis that never uses them reads like a legal document.

**"Is/are" avoidance.** Do not replace a plain "is" or "are" with an elaborate stand-in verb to sound more formal: "serves as", "stands as", "marks", "represents", "functions as", "boasts". If the sentence means "X is Y", write "X is Y".

**Manufactured analytical tags.** Do not close a sentence with a dangling "-ing" clause that pretends to add analysis without adding content: "...highlighting the importance of X", "...underscoring the need for Y", "...reflecting broader trends in Z". If the implication is worth stating, give it its own sentence with a real claim in it, or cut it.

**Vague connective filler.** Avoid "in connection with", "in association with", "associated with", "connected to" as a substitute for stating the actual relationship. Name the relationship directly: "X causes Y", "X is a special case of Y", "X depends on Y".

**Extended buzzword list.** In addition to the words already banned above, also avoid: *garner, enduring, enhance, interplay, intricate/intricacies, key (as a filler adjective), landscape (used abstractly), meticulous/meticulously, pivotal, showcase/showcasing, valuable, vibrant, boast/boasts, align with, bolstered, emphasizing, highlight (as a verb), groundbreaking, renowned, diverse array*.

**The "despite X, faces challenges" formula.** Do not structure a limitations discussion as: state something positive, pivot with "despite" or "however", name a vague challenge, resolve it with equally vague reassurance ("nonetheless demonstrates promise", "remains an area for future work"). If a limitation is real, name it precisely and say what it would take to fix it. Don't manufacture balance for its own sake.

**Repeated paragraph shape.** Watch for the same internal structure recurring across consecutive paragraphs: claim, then evidence, then a stated implication, then a transition sentence. Two or three paragraphs built on this exact template in a row read as generated even when each is individually fine. Vary how a paragraph opens and closes.

**Distanced impersonal hedging.** Avoid routing a claim through a distancing frame instead of just stating it: "one might argue that", "it could be suggested that", "a reader may notice that". State the claim directly and own it, or attribute it to a specific source.

*(This list was last extended 2026-08-24 against Wikipedia's actively maintained "Signs of AI writing" guidance and 2025 corpus research on AI-influenced vocabulary in academic writing. Re-check current commentary on Claude Sonnet's specific tells periodically — model behaviour drifts across versions.)*

## What to do instead

Write like a precise engineer explaining something real to a smart colleague. Take positions. Use short sentences when you want something to land. Quote numbers and names rather than describing things vaguely. If a design choice was made for a specific reason, state that reason directly without softening it.

The goal is prose that is technically exact, easy to read quickly, and sounds like a person wrote it.

---

# Thesis Writing Process — Sourcing, Citations, Verification

This process applies every time a new section or paragraph is drafted, not just at chapter start.

## Before writing a section

1. Read `Tesi_UniTN/biblio.bib` and any references already surfaced in the current conversation/thinking chain. List which existing entries are relevant to the section about to be written, and reuse them before adding new ones.
2. Identify claims in the planned section that need external support and are not yet covered by an existing entry. For each one, search the web for one or two references specific to that exact paragraph's claim, not generic background sources. Prefer primary sources (the original paper, spec, or standard) over secondary summaries.
3. Add any new reference to `biblio.bib` with a complete, correct entry before citing it.

## Citation density

This is a master's thesis: citation density must be high. Any non-trivial factual claim, comparison, or design rationale that isn't original to this project's own work should carry a citation. Err toward more citations rather than fewer.

## Post-write citation verification

After a paragraph is drafted, every citation in it must be independently verified back to its source before the paragraph is considered done: does the cited work actually exist, does it say what the paragraph claims it says, and is the citation key correctly formatted in `biblio.bib`. Run this verification as a separate pass (a distinct agent invocation), not as a self-check by the same pass that wrote the prose, so fabricated or misattributed citations get caught rather than rubber-stamped.

## Fixing a flagged citation: check every chapter, not just the current one

Bib keys get reused across chapters that were already written and reviewed in earlier sessions. If verification flags a `biblio.bib` entry (wrong year, wrong author, wrong field), grep all of `capitoli/*.tex` for that citation key before editing it — fix the entry once, but confirm every `\cite{}` usage across the whole thesis still matches the corrected entry, not just the usage in the section currently being drafted.

## Chapter-opening paragraph

The first time a section is drafted in a chapter that still has no prose (only `\chapter{}` and section skeletons), also write the short unsectioned roadmap paragraph that follows `\chapter{}`: state the chapter's premise and name what each section covers, in the style already used in the chapters that have this (e.g. `architecture.tex`, `background.tex`). Don't leave a chapter's first drafted section to open cold with no framing.

## Technical depth — pseudocode over language-specific code

This is a thesis, not documentation. Do not reproduce actual C# or Python syntax, real method signatures, or verbatim code blocks in chapter prose. Describe algorithms and control flow in language-agnostic pseudocode or plain prose instead, reserving concrete syntax for the rare case where the exact syntax itself is the point being made.

---

# Thesis Build

The thesis compiles locally with **tectonic** via a uv-managed Python build script.

```bash
# From Tesi_UniTN/:
uv run python build.py          # build PDF
uv run python build.py --clean  # remove artefacts, then build
uv run python build.py --open   # build and open PDF in Preview
```

`tectonic` handles all LaTeX and BibTeX passes automatically. If `tectonic` is missing: `brew install tectonic`.

Images must be placed in `Tesi_UniTN/Immagini/` (capital I — case-sensitive on Overleaf's Linux host). Reference them as `\includegraphics{Immagini/filename}` (no extension needed).

---

# Thesis Project — LaTeX (Overleaf)

Located in `Tesi_UniTN/`. Read these files in parallel alongside the internship documents:

- `Tesi_UniTN/Impaginazione/inizio.tex` (contains the abstract and front matter)
- `Tesi_UniTN/capitoli/Introduction.tex`
- `Tesi_UniTN/capitoli/background.tex`
- `Tesi_UniTN/capitoli/architecture.tex`
- `Tesi_UniTN/capitoli/Implementation.tex`
- `Tesi_UniTN/capitoli/Validation.tex`
- `Tesi_UniTN/capitoli/discussion.tex`
- `Tesi_UniTN/capitoli/conclusions.tex`
- `Tesi_UniTN/biblio.bib`
