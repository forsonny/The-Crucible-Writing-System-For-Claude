# Crucible Project — Operating Manual

This file is the operating manual for working on this novel. Follow it exactly.
When this file and any other document disagree, use the Source of Truth table below.

## Project Info

- Book Title: [TITLE]
- **Series**: [SERIES NAME] Book [#]
- **Genre**: [GENRE — fantasy/sci-fi/dystopian-utopian/space-opera/thriller/alternate-history/romantasy]
- **Genre Pack**: genre-packs/[GENRE]/
- **Target**: [TARGET] words
- **Current**: [CURRENT] words (measured with `wc -w` — see Rule 1)

## Current Status

- **Phase**: [planning|outlining|writing|editing]
- **Chapter**: [#]
- **Scene**: [#]
- **Last Activity**: [DATE]

Keep this block current: update it at the end of every session, with measured
numbers, before writing the session handoff.

## Source of Truth

| Question | Authoritative source | Never trust instead |
|---|---|---|
| Word counts | `wc -w` on the draft files, run now | Any count written in any document |
| Session state | The newest session handoff doc | A stale status block |
| Continuity facts | The story bible | Your memory of earlier chapters |
| Voice and style | The style profile | Generic "good prose" instincts |
| Plot, scenes, beats | The outline | Improvisation |
| Structure rules | The Crucible Structure (36 beats, Forge Points at beats 6/11/21/28/33) | — |

## Session Protocol

**Start**: read this file → read the newest session handoff → read the style
profile → query the story bible section-by-section as needed (never bulk-load it)
→ read only the outline sections relevant to today's work.

**End** (or run `/crucible-suite:crucible-handoff`):
1. Re-measure word counts with `wc -w`. Never carry forward written totals.
2. Confirm the story bible covers every scene touched this session.
3. Update the Current Status block above.
4. Write a session handoff doc: what was completed (measured numbers) → current
   state (tracked facts) → next-session prep (scene-by-scene) → style watch items →
   continuity checklist → the literal command to restart with.

**The scene loop**: write scene → self-audit against the style profile's
"What to Avoid" list → fix violations → update story bible → update this file.
Every scene, no exceptions.

## Project Rules

1. **Measure, don't estimate.** Every word count comes from `wc -w`, dated.
   Self-reported running totals drift badly.
2. **The outline is law.** Never invent characters, plot points, or world rules
   not in the outline/bible. Minor texture inventions (an object, a room detail)
   must be flagged inline: `[INVENTED: description]`.
3. **Verify before writing.** Check every reused fact (names, states, objects,
   numbers) against the story bible before it goes on the page.
4. **Tracked numbers move one way.** Any quantity the story tracks (counts,
   percentages, progressions) must be monotonic and may change only AFTER its
   on-page cause.
5. **Fix first, then expand.** Never expand prose that hasn't passed a style
   audit. Expand in small additions (≤200 words) that match surrounding voice —
   large insertions establish their own (wrong) patterns.
6. **Back up before campaigns.** Before any edit or expansion pass, copy each
   target chapter to `<name>.pre-edit.md`.
7. **Verify checker findings.** Review agents sometimes report errors that do not
   exist. Before fixing any reported issue, confirm it against the quoted chapter
   text. No quote, no fix.
8. **A review needs all five agents.** A bi-chapter review is valid only if the
   outline, continuity, timeline, prose, and voice checkers ALL returned reports.
9. **Keep the bible live.** Bible updates happen inside the scene loop, not
   "later". At session end the bible's latest chapter must equal the draft's.
10. **POV registers don't leak.** Each POV character's voice markers (from the
    style profile) stay in that character's scenes only.

## Quality Bars (checkable)

**A scene is done when:** word count is inside its scene-type budget; it serves a
nameable strand (Quest/Fire/Constellation); it passes the style profile's
avoid-list; every fact was bible-verified and every invention flagged; it ends on
a hook or turn; the bible is updated.

**A chapter is done when:** all outlined scenes are present; measured length is
within ±15% of the chapter target; POV voice matches the profile; tracked numbers
are consistent; all planned plants are placed.

**A bi-chapter review is done when:** all 5 agents reported; every finding was
verified against quoted text; criticals are fixed; scores and fixes are recorded.

**An edit/expansion pass is done when:** `.pre-edit.md` backups existed first;
before/after word counts are measured and logged; a post-pass style audit shows
no new violations.

## Escalation — Ask the Author, Exactly When

Stop and ask before acting if ANY of these hold:
1. The work requires anything not in the outline/bible beyond minor
   `[INVENTED:]`-taggable texture.
2. Adding, killing, renaming, or fundamentally altering a character.
3. Moving, merging, or skipping a beat — especially the structural pillars
   (beats 6, 11, 21, 28, 33: the Forge Points and Apex).
4. Changing the planned trajectory of any tracked number.
5. Any review axis scores ≤ 6 out of 10.
6. Two authoritative sources conflict.
7. An edit would cut more than 10% of a chapter.

Otherwise proceed autonomously and log every judgment call in the session handoff.

## Commands

- `/crucible-suite:crucible-status` - Check progress
- `/crucible-suite:crucible-continue` - Resume from any phase
- `/crucible-suite:crucible-plan` - Start or continue planning
- `/crucible-suite:crucible-outline` - Generate chapter outlines
- `/crucible-suite:crucible-write` - Draft prose
- `/crucible-suite:crucible-edit` - Revise manuscript
- `/crucible-suite:crucible-review` - Trigger manual review
- `/crucible-suite:crucible-tic-audit` - Deterministic style-tic scan + fix pass
- `/crucible-suite:crucible-expand` - Safe expansion pipeline (fix-first, small additions)
- `/crucible-suite:crucible-handoff` - Session-close ritual (counts, bible, handoff doc)
- `/crucible-suite:crucible-restore` - Restore from backup

Note: plugin hooks are currently DISABLED. Nothing backs up, reminds, or validates
automatically — every safety step in this manual is manual.

## Recent Decisions

- [Decision 1]
- [Decision 2]

## Open Questions

- [Question needing author input]

---

> **How Context Works**: This root CLAUDE.md loads at session start.
> Subdirectory CLAUDE.md files (in `planning/`, `outline/`, `draft/`) load
> lazily when Claude reads files in those directories. The story bible and
> style profile are queried on-demand, not auto-loaded. Use `/compact` during
> long sessions to reclaim context space.
