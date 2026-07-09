---
allowed-tools: Read, Glob, Grep, Bash, Skill, AskUserQuestion, Edit
argument-hint: [chapter file | chapter range | book directory | "all"]
description: Deterministic prose-tic audit against hard per-chapter style caps, with optional subtractive fix pass. Run before any expansion and after any edit pass.
---

# /crucible-tic-audit

Scan manuscript chapters against the project's hard tic caps (filter words,
said-bookisms, em-dash limits, signature-word overuse, declarative-opening
percentage, metaphor-domain drift), judge context-dependent flags, and
optionally fix violations subtractively.

## Usage

- `/crucible-suite:crucible-tic-audit draft/book1` - Audit a whole book
- `/crucible-suite:crucible-tic-audit draft/book2/chapter-07.md` - One chapter
- `/crucible-suite:crucible-tic-audit all` - Audit every draft directory

## Execution Instructions

**IMPORTANT:** When this command is invoked, you MUST:

0. **ALWAYS use the AskUserQuestion tool** for presenting options to the user
   (NOT plain text A/B/C options)

1. **Invoke the crucible-tic-audit skill** using the Skill tool. The skill
   drives the full workflow: deterministic scan via
   `${CLAUDE_PLUGIN_ROOT}/skills/crucible-tic-audit/scripts/tic_scan.py`,
   judgment pass on flagged items, and the optional fix pass.

2. **Pass the argument through** as the scan scope. If no argument was given,
   locate the project's draft directory and ask the user which scope to audit.

3. **Never fix without asking.** The scan and judgment report always runs;
   edits happen only after the user chooses a fix option.

## Prerequisites

- Written chapters (`chapter-NN.md` or `chNN.md`); `*.pre-edit.md` backups are
  always excluded.
- Optional: a `tic-caps.json` at the project root to override the bundled
  default caps.
