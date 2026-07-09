# Crucible Writing System — Plugin Development Manual

This repo is the `crucible-suite` Claude Code plugin: a multi-genre novel-writing
system built on the Crucible Structure (36 beats, 3 strands, Forge Points, Mercy
Engine, Dark Mirror). This file is the operating manual for changing the PLUGIN.
For writing novels WITH the plugin, see `templates/CLAUDE.md` (copied into projects).

## Repo Map — What You May Touch

| Path | What it is | Rules |
|---|---|---|
| `commands/` | 11 thin dispatchers (`crucible-*.md`) | Plugin code |
| `skills/` | 7 skills (SKILL.md + references/ + scripts/) | Plugin code |
| `agents/` | 5 read-only checker agents | Plugin code |
| `scripts/` | Shared Python (detection, state, backup, hooks) | Plugin code |
| `hooks/hooks.json` | Hook wiring — currently DISABLED (empty `{}`) | See Landmine 2 |
| `rules/`, `genre-packs/`, `templates/` | Guidance, genre overlays, project scaffold | Plugin code |
| `The-Crucible-Structure/` | Author-facing methodology docs (16 docs + worksheets) | Docs; see Canonical Rulings |
| `Example Project/` | Shipped sample ("The Memory Forge") | Sample data — update only deliberately |
| `crucible-project/` | James's personal trilogy (untracked) | NEVER modify during plugin work |
| `archive/` | The pre-plugin old system | Read-only, historical |

## Architecture

Command (`commands/X.md`) → invokes Skill (`skills/X/SKILL.md`) → skill drives the
workflow and shells out to Python scripts for anything deterministic (state,
backup, detection). Bi-chapter reviews launch the 5 `agents/` via the Task tool
with ABSOLUTE paths (agents never search). Scripts are called two ways:
`${CLAUDE_PLUGIN_ROOT}/scripts/...` from commands, relative `scripts/...` from
skills. `scripts/run_python.sh` resolves python3 cross-platform;
`scripts/cross_platform.py` is the shared library every plugin script imports.

### State machinery (exact names)

All state lives in the project (not this repo), under `.crucible/state/`:
`planning-state.json`, `outline-state.json`, `draft-state.json`, `edit-state.json`.
Content files at project root: `story-bible.json` (schema:
`STORY_BIBLE_SCHEMA` in `skills/crucible-writer/scripts/update_story_bible.py`),
`style-profile.json`, `voice-sample.md`. Backups: `.crucible/backups/incremental/`
with base64url-encoded filenames. All JSON writes go through
`cross_platform.safe_write_json` (atomic).

Detection (`cross_platform._check_directory_for_markers`) recognizes three
structure types — `dotcrucible` (`.crucible/` present), `rootlevel` (`state.json`),
`legacy` (`story-bible.json` or `planning/` at root) — but the planner only ever
creates `dotcrucible`. The `rootlevel`/`legacy` branches are vestigial; see
Landmine 4 before touching them.

## Canonical Rulings (when docs disagree)

1. **Forge Point naming**: FP0/FP1/FP2/FP3/Apex at beats 6/11/21/28/33.
   `The-Crucible-Structure/11-quick-reference.md` uses a divergent FP1–FP4 scheme —
   legacy, do not propagate it.
2. **Beat names**: `03-the-36-beats.md` is authoritative.
   `10-beat-to-chapter-mapping.md` still uses Hero's Journey names — legacy.
3. **Review trigger**: a bi-chapter review is due when
   `chapters_complete - last_review_at_chapter >= 2`. This exact rule, nowhere else's.
4. **Chapter file naming**: `chapter-NN.md` is canonical for new code. (Existing
   code globs both `ch*.md` and `chapter*.md`; don't narrow the globs.)
5. **Planning docs**: 9 question-and-answer document cycles compiling to ~10 files
   (thesis, 3 strand maps, 5 forge points, dark mirror, constellation bible,
   mercy ledger, world forge, summary).

## Named Landmines → Rules

Mistakes this repo has already produced, each with its preventing rule.

1. **Version drift** — the version currently lives in FOUR places and they have
   diverged before (plugin.json 2.0.0 vs VERSION 1.0.18 vs marketplace.json 1.0.17).
   RULE: every release updates ALL of: `VERSION`, `.claude-plugin/plugin.json`,
   `.claude-plugin/marketplace.json` (plugin entry), the `README.md` footer, and a
   `CHANGELOG.md` entry. `scripts/bump_version.py` does NOT touch marketplace.json —
   check it by hand.
2. **Hooks are disabled** — `hooks/hooks.json` is `{"hooks": {}}` (cache-mismatch
   workaround). RULE: never document backups, session context injection, or the
   Stop-hook review reminder as active. Re-enabling requires testing the plugin
   cache issue first. plugin.json deliberately has no `hooks` key (a duplicate-file
   error fix from 1.0.11) — do not add one.
3. **Bi-chapter logic is duplicated in 5 files** — `update_story_bible.py`
   (canonical `sync_draft_state()`), `check_stop_conditions.py`,
   `backup_on_change.py`, `load_project_context.py`, `update_draft_state.py`.
   RULE: change the review rule in all five together, or refactor to one import —
   never in just one.
4. **Dead state branches** — `state.json` (rootlevel) and `project-state.json`
   (referenced by the Stop hook, written by nothing) are vestigial. RULE: don't
   extend them; removing them is an architectural change — ask James first.
5. **Title parsing contract** — `load_project_context.py`, `detect_project.py`,
   and `status_reporter.py` all parse a line containing `Book Title:` from the
   project CLAUDE.md. RULE: `templates/CLAUDE.md` must always contain a
   `Book Title: [TITLE]` line; never remove it or change its spelling.
6. **ASCII only in tool output** — emoji broke Windows cmd (purged in 1.0.7).
   RULE: scripts and agent report formats emit ASCII (`[x]`, `[####----]`, `═`
   boxes are the established set).
7. **Python 3.8+ compatibility** — no walrus-heavy 3.10+ syntax, no external deps.
   RULE: standard library only; every script must run under `python3` on macOS
   and `py -3` on Windows.
8. **Invalid agent model IDs** — 1.0.16 fixed a dead dated model string. RULE:
   agent frontmatter uses only `haiku` or `inherit`; never pin dated model IDs.
9. **AskUserQuestion always** — every user choice goes through the
   AskUserQuestion tool, never plain-text A/B/C. Max 4 questions × 4 options,
   headers ≤ 12 chars.
10. **State writes are atomic** — RULE: all JSON writes go through
    `safe_write_json`; never `open(...).write(json.dumps(...))`.

## Quality Bars per Deliverable (checkable)

**A command (`commands/*.md`) is done when:** it has frontmatter
(`allowed-tools`, `argument-hint`, `description`); it dispatches to a skill or
script rather than embedding workflow logic; every user choice uses
AskUserQuestion; paths passed to agents are absolute; it is registered in
`marketplace.json`'s `commands` array.

**A skill is done when:** `skills/<name>/SKILL.md` has `name` + trigger-rich
`description` frontmatter; long reference material lives in `references/`, not
SKILL.md; deterministic work is a script in `scripts/`; state is saved after
every user answer (interview-pattern skills); it is registered in
`marketplace.json`'s `skills` array.

**An agent is done when:** `tools: Read, Grep, Glob` and `permissionMode: plan`
(read-only); model is `haiku` or `inherit`; its prompt contract requires absolute
paths; it emits the fixed ASCII report format with X/10 metrics and
Critical/Warning/Suggestion buckets.

**A script is done when:** it imports `cross_platform.py` for detection/IO; it
either handles all three structure types or is explicitly dotcrucible-only (say
so in the docstring); writes are atomic; output is ASCII; it runs on Python 3.8.

**A genre pack is done when:** it is exactly three files
(`genre-rules.md`, `question-overrides.md`, `world-building-guide.md`); it only
overrides questions/rules and never alters the 36-beat core; it is auto-detected
by directory presence (no registration needed).

**A release is done when:** all four version strings agree; CHANGELOG has the
entry; the commit subject is `vX.Y.Z: summary`.

## Workflow

Per James's global rules: never push to main. Branch (`feat/`, `fix/`, `docs/`,
`chore/`) → conventional commits → PR via `gh pr create` → CI/review → merge.
Test any script change by running it against `Example Project/` (never against
`crucible-project/`).

## Escalation — Ask James, Exactly When

1. Any schema change to a state file or `story-bible.json`.
2. Anything that reads from or writes to `crucible-project/`.
3. Removing legacy/vestigial code paths (dead state branches, `fantasy-writing.md`
   vs `genre-writing.md` duplication).
4. Version-scheme or release-process decisions.
5. Re-enabling hooks.
6. Changing the 36-beat core, beat names, or Forge Point placement anywhere.

Known cleanup items (flagged, deliberately not done — ask before doing):
`skills/crucible-writer/scripts/update_story_bible.py.bak` is committed;
`crucible-project/ebook/output/node_modules/` is untracked bulk;
`fantasy-writing.md` duplicates `genre-writing.md`; hooks re-enablement.
