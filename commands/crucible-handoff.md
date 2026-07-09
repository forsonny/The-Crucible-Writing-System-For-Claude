---
allowed-tools: Read, Glob, Grep, Bash, Skill, AskUserQuestion, Write, Edit
argument-hint: [next-session name, e.g. "CH18-PREP"]
description: Session-close ritual - measure real word counts, reconcile the story bible, update CLAUDE.md status, and write the SESSION handoff doc for cold-start resume.
---

# /crucible-handoff

Close the current writing session safely: measured word counts (`wc -w`, never
estimates), story-bible reconciliation, CLAUDE.md status update, and a
structured `SESSION-<NAME>.md` handoff document the next session can resume
from with zero shared context.

## Usage

- `/crucible-suite:crucible-handoff CH18-PREP` - Close session, prep chapter 18
- `/crucible-suite:crucible-handoff` - Close session; the skill will ask what
  the next session's focus is and name the doc accordingly

## Execution Instructions

**IMPORTANT:** When this command is invoked, you MUST:

0. **ALWAYS use the AskUserQuestion tool** for presenting options to the user
   (NOT plain text A/B/C options)

1. **Invoke the crucible-handoff skill** using the Skill tool. The skill
   drives all five phases: Measure, Reconcile bible, Update CLAUDE.md,
   Write handoff doc, Confirm.

2. **Pass the argument through** as the handoff doc name hint. If omitted,
   the skill asks for the next session's focus.

3. **Never skip the measurement phase.** Even a "nothing changed" session gets
   measured counts in its handoff doc.

## Prerequisites

- An active Crucible project (drafting, editing, or expanding).
- Works in any phase; the handoff doc shape adapts to the work done.
