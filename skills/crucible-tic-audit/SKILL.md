---
name: crucible-tic-audit
# prettier-ignore
description: Deterministic prose-tic audit for Crucible manuscripts. Scans chapters against hard per-chapter style caps (filter words, said-bookisms, em-dash limits, signature-word overuse, declarative-opening percentage, sentence-length stats, metaphor-domain drift) using a regex scanner, then runs a judgment pass for context-dependent tics and optionally applies subtractive fixes. Use when the author says "tic audit," "check my tics," "style audit," "scan for filter words," "em-dash check," before ANY expansion campaign, after any edit or expansion pass, or when prose review scores are low.
---

# Crucible Tic Audit

Enforce the manuscript's style contract mechanically. The scanner counts; you
judge; fixes are subtractive-first. This audit is MANDATORY before any
expansion work (see crucible-expand) — expanding un-audited prose creates the
fix/expand treadmill.

## Why this exists

Manual tic hunting consumed entire editing sessions in real projects, and every
expansion pass re-introduced the tics the previous edit pass removed. The
scanner makes the mechanical part instant and repeatable. The numbers below
were measured, not invented: one project hit 90 over-explanation instances
across 6 chapters and 65-70% declarative openings before caps were enforced.

## Phase 1 — Scan

1. Locate the draft. Chapter files match `chapter-NN.md` (also `chNN.md`);
   ALWAYS exclude `*.pre-edit.md` backups (the scanner does this for
   directories automatically).
2. Run the scanner:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/crucible-tic-audit/scripts/tic_scan.py" <chapter-or-dir> [--json]
   ```
   Caps resolution: `--caps <file>` > `tic-caps.json` at the project root >
   bundled defaults in `assets/tic-caps.json`. If the project's style profile
   specifies different limits, generate a project `tic-caps.json` from it first
   and tell the author you did.
3. Present the per-chapter PASS/FAIL table exactly as the scanner reports it.
   Exit code 1 means at least one violation exists.

## Phase 2 — Judgment pass (LLM, on flagged items only)

The scanner cannot judge context. For each chapter that FAILED or carries
metaphor-drift flags, read the chapter and rule on:

- **Metaphor-drift flags**: a flagged word is a violation only when used
  figuratively outside the allowed domains ("a tide of refugees" = violation;
  a literal river = fine). Quote each violating sentence.
- **Over-explanation**: strong image or dialogue line followed by a sentence
  that interprets it ("Meaning: ...", restating the line, defining a word just
  used). The scanner cannot see these; you must. List each with a quote.
- **False positives**: a counted tic inside quoted dialogue may be
  characterization (e.g., a character who says "something" habitually). Rule
  each one explicitly; do not silently excuse them.

Every judgment MUST carry a quote from the chapter text. No quote, no finding.

## Phase 3 — Fix pass (only if the author asks)

Use AskUserQuestion to offer: fix everything / fix specific chapters / report
only.

Fix rules:
1. Fixes are SUBTRACTIVE first: cut the explaining sentence, delete the filter
   word and describe directly, replace the em-dash with a period or comma.
   Rewriting is the fallback, adding words is last resort.
2. Never change plot, dialogue meaning, tracked numbers, or POV register.
3. Fix in place, chapter by chapter. After each chapter, re-run the scanner on
   that file to confirm PASS before moving on.
4. Report before/after: violations per chapter and net word delta (measure
   with `wc -w`, never estimate).

## Output format

```
============================================================
TIC AUDIT: <scope>
============================================================
SCAN:      X/Y chapters PASS  (scanner table above)
JUDGMENT:  N confirmed context violations (quoted)
           M false positives excused (reasons given)
FIXES:     [not requested | K violations fixed, re-scan PASS]
WORD DELTA: before -> after (wc -w)
============================================================
```

## Hard rules

- Never "fix" a violation you cannot quote.
- Never edit a chapter without a `.pre-edit.md` backup if this audit is part
  of an edit/expansion campaign (the campaign owns the backups; a standalone
  quick fix of <10 instances may proceed without, but say so).
- Never touch `*.pre-edit.md` files.
- If a cap seems wrong for this project (e.g., the signature word differs),
  ASK the author — do not silently change caps.
