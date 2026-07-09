---
name: crucible-handoff
# prettier-ignore
description: Session-close ritual for Crucible writing projects. Measures real word counts with wc -w, reconciles story-bible staleness, updates the project CLAUDE.md status block, and writes a structured SESSION handoff document so the next session can resume cold. Use when the author says "end the writing session," "handoff," "wrap up this session," "prep the next chapter," "write the session doc," or at the natural end of any drafting, editing, or expansion session.
---

# Crucible Handoff

Close a writing session so the NEXT session (possibly a fresh context with no
memory of this one) can resume without loss. The handoff document is the real
state of the project; treat writing it with the same care as writing prose.

## Why this exists

In real projects, self-reported running word counts drifted 28% from reality,
the story bible fell 4+ chapters behind the draft, and the project CLAUDE.md
went stale by an entire book. Every one of those failures happened because
session close was manual and optional. This skill makes it a checklist.

## Phase 1 — Measure (never estimate)

1. Locate draft chapter files (exclude `*.pre-edit.md`).
2. Measure with `wc -w` per book/draft directory:
   ```bash
   cat draft/*/chapter-*.md | wc -w   # adjust path to project layout; exclude .pre-edit.md
   ```
3. Compare against the counts recorded in the project CLAUDE.md. Report the
   delta explicitly. If a previously recorded count disagrees with the measured
   one by more than 2%, say so — do not silently overwrite history; note the
   correction in the handoff doc.

## Phase 2 — Reconcile the story bible

1. Determine the last chapter the story bible covers (per-chapter tables or
   chapter summaries in the bible).
2. Determine the last chapter that exists in the draft.
3. If the bible is behind: list the uncovered chapters and, for each scene
   touched THIS session, update the bible now (character states, established
   facts, tracked numbers, foreshadowing plants, timeline).
4. If chapters from BEFORE this session are uncovered, do not reconstruct them
   silently — flag them in the handoff doc as a bible-staleness debt and ask
   the author whether to reconcile now.

## Phase 3 — Update the project CLAUDE.md

Update ONLY the status fields: current phase, book/chapter/scene position,
measured word counts (labeled with today's date), last activity date, and the
"next" pointer to the new handoff doc. Do not rewrite other sections.

## Phase 4 — Write the handoff document

File: `SESSION-<NAME>.md` at the project root, where `<NAME>` describes the
next session's work (e.g. `SESSION-CH18-PREP`, `SESSION-EDIT-BOOK2`). Use this
exact section order (it is the established shape):

1. **Header** — title, date, beat/purpose of next session.
2. **Previous Session Summary** — chapters/scenes completed with MEASURED word
   counts; review results table if a review ran (agent | result | key fixes).
3. **Running Totals** — per book + total, all measured, all dated.
4. **Current State** — tracked numbers (each with its current value and
   direction), character/constellation status table, protagonist physical
   state, key objects and their locations.
5. **Next Chapter Prep** — scene-by-scene: POV, location, what happens, plants
   to place, key lines to land, per-scene word targets.
6. **Voice Notes** — per-POV register reminders for the next chapters,
   including any DO-NOT-CONTAMINATE warnings.
7. **Tic Watch** — the hard-limits table plus session-specific watch items
   (new tics observed this session).
8. **Continuity Checklist** — checkbox list of verifiable facts the next
   session must confirm before writing.
9. **Decisions** — every judgment call made this session that wasn't in the
   outline (what, why, where logged).
10. **Restart command** — the literal line to start the next session with:
    `*Start next session with: "read SESSION-<NAME>.md and <action>"*`

Content rules:
- Every number in the doc is measured or bible-verified, never remembered.
- Every state claim must be checkable (a fact, a count, a location) — no vibes.
- If anything was left mid-scene or mid-fix, say exactly where and what remains.

## Phase 5 — Confirm

Present a short summary: measured totals (with deltas), bible status
(reconciled / debt flagged), CLAUDE.md updated, handoff doc path, restart
command. Then use AskUserQuestion to confirm the handoff is complete or
capture anything the author wants added.
