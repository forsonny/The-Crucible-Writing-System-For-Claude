---
allowed-tools: Read, Glob, Grep, Bash, Skill, AskUserQuestion, Write, Edit, Task
argument-hint: [book directory | chapter range] [target word count]
description: Safe word-count expansion pipeline - fix-first baseline, small voice-matched additions, mandatory re-audit. Grows an under-length draft without introducing tics or plot inventions.
---

# /crucible-expand

Grow an under-length book or chapter toward its word target using the proven
pipeline: tic-clean baseline first, additions of 100-200 words inside existing
scenes, per-chapter re-audit, measured reporting. Never adds plot, scenes,
characters, or world rules.

## Usage

- `/crucible-suite:crucible-expand draft/book1 100000` - Expand Book 1 to 100K
- `/crucible-suite:crucible-expand draft/book2/chapter-05.md 5000` - One chapter
- `/crucible-suite:crucible-expand` - The skill will ask for scope and target

## Execution Instructions

**IMPORTANT:** When this command is invoked, you MUST:

0. **ALWAYS use the AskUserQuestion tool** for presenting options to the user
   (NOT plain text A/B/C options)

1. **Invoke the crucible-expand skill** using the Skill tool. The skill drives
   all phases: baseline + backups, mandatory tic-clean pass (via the
   crucible-tic-audit skill), expansion map (author-approved), the expansion
   loop with per-chapter re-scans, post-campaign audit, and handoff.

2. **Pass the arguments through** as scope and target. If omitted, the skill
   asks.

3. **Enforce the gate:** no chapter is expanded before it passes the tic
   scanner on this campaign. This is the treadmill-prevention rule; do not
   waive it for speed.

## Prerequisites

- A drafted book or chapter measurably under its target (`wc -w`).
- Outline and story bible available (expansion must verify against both).
- The crucible-tic-audit skill (bundled in this plugin).
