---
name: crucible-expand
# prettier-ignore
description: Safe word-count expansion pipeline for Crucible manuscripts. Grows an under-length book or chapter toward its target without introducing style tics, plot inventions, or voice drift, using the proven fix-first / small-additions / re-audit sequence. Use when the author says "expand the book," "grow chapter X," "this book is under target," "add words," "get book N to 100k," or when a draft's measured word count is materially below its target.
---

# Crucible Expand

Grow a manuscript toward its word target WITHOUT degrading it. This pipeline
exists because naive expansion demonstrably fails: in a real project, large
expansion passes re-introduced the exact tics the previous edit pass had
removed (the "treadmill"), and a 9-session campaign was needed to discover the
rules below. Follow them; do not improvise a different pipeline.

## The three laws of expansion (learned the hard way)

1. **Fix first, then expand.** A tic-clean baseline BEFORE adding prose.
   Expanding dirty prose multiplies the dirt.
2. **Small additions win.** Many ~100–200 word additions match the surrounding
   voice; large per-chapter dumps establish their own (wrong) patterns.
   No single addition may exceed 200 words.
3. **Expansion adds texture, never plot.** Deepen interiority, extend existing
   scenes, enrich sensory grounding. Never new scenes, characters, plot
   points, or world rules. Anti-hallucination rules apply in full;
   `[INVENTED: ...]` only for minor texture.

## Phase 0 — Baseline and safety

1. Measure the true current count: `wc -w` on chapter files, EXCLUDING
   `*.pre-edit.md`. Record per chapter and total. Never start from a written
   count.
2. Back up: copy every target chapter to `chapter-NN.pre-edit.md` (skip any
   that already have one from a previous campaign — do not overwrite old
   backups; ask the author how to handle them).
3. Confirm the target with AskUserQuestion: total target, and whether any
   chapters are off-limits.

## Phase 1 — Tic-clean baseline (mandatory)

Run the crucible-tic-audit skill (scan + judgment + fixes) over every target
chapter. Do not proceed until every target chapter PASSES the scanner. This
step is not optional and not skippable for time — it is the treadmill
prevention.

## Phase 2 — Expansion map

Before writing a word, build and present the map:

- Per chapter: current count, target count, gap.
- Per chapter: WHERE the words go — which scenes are thinnest against their
  scene-type budgets (action 1,500–2,500 / dialogue 1,000–2,000 / reflection
  800–1,500 / transitional 500–1,000 / climax 2,500–4,000), and WHAT KIND of
  prose each gap needs (interiority, sensory grounding, beat extension,
  reaction space).
- Flag any chapter whose gap exceeds ~20% of its current length — those need
  author sign-off before expansion (a gap that large usually means a missing
  scene, which is an OUTLINE question, not an expansion question).

Present the map with AskUserQuestion before proceeding.

## Phase 3 — Expand (the loop)

Per chapter, in order:

1. Read the chapter in full plus its outline section and relevant bible
   entries.
2. Make additions of 100–200 words each, inside existing scenes, each one:
   - in the scene's POV register (check the style profile's per-character
     voice notes; POV contamination is the classic expansion failure),
   - within the allowed metaphor domains,
   - respecting every tic cap (the em-dash budget does not grow with the
     scene),
   - never touching tracked numbers, plants, or key lines.
3. After each chapter: re-run the tic scanner ON THAT CHAPTER. Expansion is
   the #1 source of re-introduced tics; a chapter that fails gets fixed before
   the next chapter is touched.
4. Measure the chapter with `wc -w`; log before/after in a running table.

## Phase 4 — Post-campaign audit

1. Full tic scan over all touched chapters — must PASS.
2. Spot continuity check: tracked numbers unchanged, no new proper nouns
   without `[INVENTED:]`, book-boundary threads intact.
3. Optionally run the 5-agent review (`/crucible-suite:crucible-review`) on
   the most-expanded chapters. Remember: a review is valid only if all 5
   agents return; verify any reported error against quoted text before fixing.

## Phase 5 — Report and hand off

Report: per-chapter before/after table (measured), total delta vs. target,
tic-scan status, backups list. Then run the crucible-handoff skill to close
the session properly.

## Hard rules

- Never expand a chapter that hasn't passed Phase 1 on this campaign.
- Never exceed 200 words per addition.
- Never invent plot, scenes, characters, or world rules.
- Never let a chapter end the session in a failed-scan state.
- Never trust or report an unmeasured word count.
