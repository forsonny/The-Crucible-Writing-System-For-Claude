# Changelog

All notable changes to the Crucible Suite plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-07-08

### Added

#### Operating Manuals (CLAUDE.md rewrite)
- New root `CLAUDE.md` - plugin development manual: repo map, architecture and
  state machinery reference, canonical rulings for doc inconsistencies, named
  landmines with preventing rules, per-deliverable quality bars, escalation rules
- Rewrote `templates/CLAUDE.md` as a project operating manual: source-of-truth
  table, session protocol, measure-don't-estimate rules, checkable quality bars,
  exact escalation triggers. Adds the `Book Title:` line that detection scripts
  (`load_project_context.py`, `detect_project.py`, `status_reporter.py`) parse -
  fixes title always reading as "Untitled"

#### Three New Skills
- **crucible-tic-audit** (`/crucible-suite:crucible-tic-audit`) - deterministic
  prose-tic scanner (`tic_scan.py`) with hard per-chapter caps (filter words,
  said-bookisms, em-dash-per-scene limits, signature-word overuse,
  declarative-opening percentage, sentence stats, metaphor-domain drift flags),
  LLM judgment pass for context-dependent tics, optional subtractive fix pass.
  Caps overridable via project-root `tic-caps.json`
- **crucible-expand** (`/crucible-suite:crucible-expand`) - safe word-count
  expansion pipeline: pre-edit backups, mandatory tic-clean baseline,
  author-approved expansion map, 100-200 word voice-matched additions,
  per-chapter re-scans, measured before/after reporting
- **crucible-handoff** (`/crucible-suite:crucible-handoff`) - session-close
  ritual: measured word counts (wc -w), story-bible reconciliation, CLAUDE.md
  status update, structured SESSION handoff document for cold-start resume

### Fixed
- Version drift: `VERSION`, `plugin.json`, `marketplace.json`, and the README
  footer now all agree (previously 1.0.18 / 2.0.0 / 1.0.17 / 1.0.18)
- `marketplace.json` plugin description updated to multi-genre (was still
  epic-fantasy-only from v1.x)

## [2.0.0] - 2026-03-21

### Added

#### Multi-Genre Support (7 Genre Packs)
- New `genre-packs/` directory with seven packs: `fantasy`, `sci-fi`,
  `dystopian-utopian`, `space-opera`, `thriller`, `alternate-history`,
  `romantasy`
- Each pack is three files: `genre-rules.md`, `question-overrides.md`,
  `world-building-guide.md`
- `genre-packs/genre-config.md` + `genre-packs/README.md` - selection and
  override mechanics
- New base `rules/genre-writing.md` (generalizes the Sanderson-style
  speculative-system laws across genres)
- Planner Phase 1 intake gains genre selection (saved via
  `save_state.py --answer "meta" "genre"`); outliner, writer, and editor are
  genre-aware
- `templates/CLAUDE.md` gains Genre / Genre Pack fields

### Unchanged
- The 36-beat core (three strands, five movements, Forge Points, Mercy Engine,
  Dark Mirror), all scripts, and all five review agents are identical across
  genres

*(Backfilled 2026-07-08 - this release shipped in commit `e3ad069` without a
changelog entry.)*

## [1.0.18] - 2025-12-20

### Added

#### Comprehensive Author Documentation
- New `The-Crucible-Structure/` folder with complete framework documentation
- Designed for both plugin users and authors writing by hand

**Core Documentation (16 files):**
- `00-introduction.md` - Overview and philosophy of the Crucible Structure
- `01-quick-start.md` - Five-minute overview for rapid onboarding
- `02-the-three-strands.md` - Quest, Fire, Constellation strands explained
- `03-the-36-beats.md` - Complete beat-by-beat breakdown
- `04-the-five-movements.md` - Movement structure with percentages
- `05-forge-points.md` - Four Forge Points + Apex mechanics
- `06-the-mercy-engine.md` - Four mercies and Beat 31 payoff
- `07-the-dark-mirror.md` - Antagonist as thematic shadow
- `08-the-three-currencies.md` - Power, Humanity, Time system
- `09-strand-weave-pattern.md` - How strands interleave
- `10-beat-to-chapter-mapping.md` - 18/25/35 chapter options
- `11-quick-reference.md` - Single-page printable cheatsheet
- `12-glossary.md` - 26 terms defined
- `13-tutorial-walkthrough.md` - Step-by-step planning guide (3-4 hours)
- `14-faq-and-troubleshooting.md` - 50+ common questions answered
- `15-visual-diagrams.md` - ASCII diagrams of complete structure

**Worksheets (7 blank templates):**
- `worksheets/01-story-foundation-worksheet.md` - Premise, theme, targets
- `worksheets/02-three-strands-worksheet.md` - Strand mapping
- `worksheets/03-forge-points-worksheet.md` - Five crisis points
- `worksheets/04-mercy-ledger-worksheet.md` - Mercy tracking
- `worksheets/05-dark-mirror-worksheet.md` - Antagonist design
- `worksheets/06-beat-planning-worksheet.md` - 36 beats to chapters
- `worksheets/07-character-constellation-worksheet.md` - Character profiles

**Completed Examples (7 files):**
- Based on "The Memory Forge" sample story from Example Project
- Demonstrates proper detail level and cross-referencing
- Located in `worksheets/examples/`

### Changed

#### Main README Documentation Section
- Reorganized into "Learn the Crucible Structure" and "Plugin Reference" subsections
- Added links to tutorial, visual diagrams, FAQ, core concepts
- Added links to worksheets and completed examples

## [1.0.17] - 2025-12-20

### Changed

#### Repository Restructure
- Moved plugin from `plugin/crucible-suite/` to repository root
  - Plugin components now directly at root level for simpler installation
  - Removed nested plugin path from all documentation
- Merged `plugin-update` branch into `main`
  - All development work from v1.0.1 through v1.0.16 now on main branch
  - Installation URL simplified: no longer requires `#plugin-update` branch reference

#### README Accuracy Overhaul
- Changed "7 planning documents" to "9 planning documents" (accurate count)
- Added new "Planning Documents" section listing all 9 documents with purposes
- Fixed Forge Points section:
  - Changed "Five Forge Points" to "Four Forge Points + Apex"
  - Added beat numbers and locations for each forge point
- Added "Six Movements" table including Coda (was incorrectly showing 5)
- Fixed project structure documentation:
  - Split into "at creation" and "as you progress" sections
  - Accurately shows what directories exist at each phase
- Updated skill reference file lists to include all files:
  - crucible-planner: added `question-key-mapping.md`
  - crucible-writer: added `bi-chapter-review.md`, `story-bible-commands.md`
- Removed emoji characters (ASCII-only per project guidelines)
- Changed Unicode tree characters to ASCII (`+--` instead of special chars)

### Removed

#### Development Files
- Removed from repository root (archived locally):
  - `CC Plugins/` - Plugin documentation reference
  - `Claude Skills/` - Original skill files
  - `docs/` - Framework documentation
  - `Example Chapters/` - Sample content
  - `GAP-ANALYSIS.md`, `IMPLEMENTATION-PLAN.md`, `USER-FLOW-DIAGRAMS.md`
- These were development/reference files, not part of the plugin itself

## [1.0.16] - 2025-12-20

### Fixed

#### Review Agent Model Configuration
- Fixed invalid model ID in outline-checker and timeline-checker agents
  - Changed from non-existent `claude-haiku-4-20250514` to valid `haiku` shorthand
  - Agents were failing with "model configuration error" due to 404 API responses
  - Both agents now correctly use the haiku model for fast review checks

## [1.0.15] - 2025-12-20

### Fixed

#### Planning Completion in /crucible-continue Command
- Fixed command not verifying actual planning files exist before reporting "Planning COMPLETE"
  - Root cause: Command only read state JSON, didn't check if compile_documents.py had run
  - Added "CRITICAL: Planning Completion Check" section to command instructions
  - Claude now must verify `planning/crucible-thesis.md` exists before declaring planning complete
  - If Q&A done but files missing, offers to run compilation script
- This complements the v1.0.14 fix to detect_project.py with instructions for the command itself

## [1.0.14] - 2025-12-20

### Fixed

#### Planning Completion Detection
- Fixed `/crucible-continue` incorrectly reporting planning as complete when document files were never generated
  - Root cause: `detect_project.py` only checked if 9 Q&A sessions were marked complete in state JSON
  - Did not verify that `compile_documents.py` had actually run to generate the planning files
  - Now requires BOTH conditions: Q&A complete (9/9 docs) AND `planning/crucible-thesis.md` exists
- Added `planning_files_exist()` helper function to verify compiled documents exist
- Added diagnostic fields to progress output: `qa_complete` and `files_generated`
- Updated `get_resume_point()` to detect and report the "compile needed" state
  - New message: "Q&A complete (9/9 docs). Run compile_documents.py to generate planning files."

## [1.0.13] - 2025-12-20

### Fixed

#### Planning Phase Completion
- Fixed planning phase not generating documents after completing all 9 questioning cycles
  - Root cause: No explicit transition instruction between Phase 2 (Document Generation) and Phase 3 (Compilation)
  - Added "Phase 2 Complete" section (lines 317-325) with explicit instruction to proceed to Phase 3 and run `compile_documents.py`
  - Claude now receives clear directive to compile documents after Document 9 verification

#### Documentation Accuracy
- Fixed "four Forge Points" to "five Forge Points" in skill description (line 4)
- Clarified document count: "7 planning document categories (14 files total)" in both description (line 4) and overview (line 13)
  - 7 categories: Crucible Thesis, Strand Maps, Forge Points, Dark Mirror, Constellation Bible, Mercy Ledger, World Forge
  - 14 files: includes 3 strand maps, 5 forge point files, and summary card

## [1.0.12] - 2025-12-19

### Fixed

#### Project Detection
- Fixed status command failing to find projects in subdirectories
  - Root cause: `find_crucible_project_with_type()` only searched upward (current dir and parents)
  - When user is in parent directory (e.g., `C:\books\test3`) with project in subdirectory (e.g., `crucible-project/`), detection failed
  - Added fallback search that checks immediate subdirectories (one level deep)
  - Skips hidden directories (starting with `.`) and handles permission errors gracefully

### Added

#### Shared Utilities
- `_check_directory_for_markers()` helper function in `cross_platform.py`
  - Extracts marker detection logic for reuse
  - Maintains priority order: `.crucible/`, `state.json`, `story-bible.json`, `planning/`

### Changed
- Updated `find_crucible_project_with_type()` docstring to document two-phase search order

## [1.0.11] - 2025-12-19

### Fixed

#### Plugin Loading
- Removed explicit `hooks` reference from plugin.json manifest
  - `hooks/hooks.json` is auto-loaded by Claude Code from the standard location
  - Explicit reference caused "Duplicate hooks file detected" error
  - Plugin now loads without errors

## [1.0.0] - 2024-12-11

### Added

#### Skills
- **crucible-planner** - Interactive planning system with 7 document generation
- **crucible-outliner** - Chapter-by-chapter outline generator
- **crucible-writer** - Scene-by-scene prose drafting with style matching
- **crucible-editor** - Multi-level revision and editing workflow

#### Commands
- `/crucible-suite:crucible-plan` - Start or continue planning with premise
- `/crucible-suite:crucible-outline` - Generate chapter outlines from planning
- `/crucible-suite:crucible-write` - Draft prose from outlines
- `/crucible-suite:crucible-edit` - Revision and editing workflows
- `/crucible-suite:crucible-status` - Show comprehensive project status
- `/crucible-suite:crucible-continue` - Auto-detect and resume from any phase
- `/crucible-suite:crucible-review` - Manual bi-chapter review trigger
- `/crucible-suite:crucible-restore` - Restore from backups

#### Agents
- **voice-checker** - Voice and style consistency analysis
- **continuity-checker** - Plot and character continuity tracking
- **outline-checker** - Outline fidelity verification
- **timeline-checker** - Chronological consistency analysis
- **prose-checker** - Craft-level feedback

#### Hooks
- **SessionStart** - Automatic project context loading
- **PostToolUse** - Incremental backup on Write/Edit
- **Stop** - Quality gate for bi-chapter reviews
- **SubagentStop** - Review agent completion verification

#### Rules
- `fantasy-writing.md` - Genre conventions and prose guidelines
- `crucible-structure.md` - 36-beat framework rules
- `anti-hallucination.md` - Verification protocols

#### Templates
- `CLAUDE.md` - Project memory template
- Project structure scaffolding

#### Scripts
- `backup_project.py` - Full project backup
- `backup_on_change.py` - Incremental backup
- `detect_project.py` - Project state detection
- `status_reporter.py` - Status report generation
- `load_project_context.py` - Session context injection
- `cross_platform.py` - Shared utilities

### Technical Details
- All SKILL.md files under 500 lines with progressive disclosure
- Cross-platform Python 3.8+ scripts
- JSON-based state management
- Automatic backup with 20-backup retention

## [1.0.1] - 2025-12-11

### Fixed

#### Hook Configuration
- Fixed hook timeouts from milliseconds to seconds (hooks use seconds, not ms)
- Removed invalid `matcher` field from SessionStart hook (matchers only valid for PreToolUse/PermissionRequest/PostToolUse)
- Updated prompt hooks with correct JSON response format requirement
- Added missing `hooks` reference to plugin.json

#### Python 3.8 Compatibility
- Fixed `is_relative_to()` usage in backup_on_change.py (method only exists in Python 3.9+)
- Changed to try/except pattern with `relative_to()` for broader compatibility

#### Code Quality
- Removed duplicate `load_draft()` function from init_draft.py
- Fixed unreachable code in update_draft_state.py (`const=-1` → `const=0`)
- Removed unused imports across multiple scripts
- Added error handling for file operations in save_draft.py and diff_report.py

#### Skill/Agent Configuration
- Removed invalid `allowed-tools` field from all SKILL.md files (not valid for skills per docs)
- Added `skills` field to all 5 review agent frontmatter

#### Command Integration
- Added explicit "Execution Instructions" sections to all 8 commands
- Commands now properly invoke their corresponding skills via Task tool

### Added

#### Scripts
- `load_draft.py` - Resume writing sessions from saved state (was missing)
- `update_draft_state.py` - Chapter tracking and bi-chapter review trigger

#### Features
- Bi-chapter review system in crucible-writer skill
- Chapter tracking for automatic review triggers every 2 chapters

#### Utilities
- `find_crucible_project()` function in cross_platform.py
- `extract_title_from_claude_md()` utility in cross_platform.py

### Changed
- Updated README.md with correct GitHub repository URL
- Enhanced backup_on_change.py path detection for Crucible files

## [1.0.2] - 2025-12-14

### Added

#### Answer Persistence System
- Full context storage for planning answers (question + answer + description)
- CLI interface for `save_state.py` with 5 parameters:
  - `--answer <document> <key> <question> <answer> <description>`
  - `--progress <doc_num> <question_num>`
  - `--complete <doc_num>`
  - `--scope <length> <complexity>`
- New `question-key-mapping.md` reference file with all 75 question-to-state-key mappings
- Answer Persistence Workflow section in crucible-planner SKILL.md
- Resuming Planning section in crucible-continue.md with saved answer display

#### Backward Compatibility
- `get_answer()` helper function in `compile_documents.py` handles both old (string) and new (dict) answer formats

### Changed
- Planning answers now stored as objects with full context instead of plain strings
- `/crucible-continue` now displays previously saved answers when resuming planning sessions

### Fixed
- Session recovery now preserves full question context, not just answer values
- Planning progress can be properly resumed after session failures

## [1.0.3] - 2025-12-14

### Added

#### Version Tracking
- Added `VERSION` file for simple version tracking
- Added `bump_version.py` script for version management:
  - `python bump_version.py patch` - 1.0.3 -> 1.0.4
  - `python bump_version.py minor` - 1.0.3 -> 1.1.0
  - `python bump_version.py major` - 1.0.3 -> 2.0.0
- Script updates both VERSION file and plugin.json

### Improved

#### Status Report Formatting
- Redesigned `format_report_text()` with clean ASCII box layout
- Added visual progress bars `[####----]` for each phase
- Added status icons: `[x]` complete, `[>]` in progress, `[ ]` pending
- Organized sections with clear headers (PLANNING, OUTLINE, WRITING, EDITING, BACKUP)
- Cross-platform ASCII characters (works on Windows cmd/PowerShell)

### Fixed

#### Project Detection Bug
- Fixed `status_reporter.py` and `detect_project.py` failing to find planner-created projects
- Root cause: Scripts looked for `.crucible/` directory but `init_project.py` creates `state.json` at project root
- Updated `find_crucible_project()` to detect both structures:
  - `dotcrucible`: Legacy `.crucible/` directory structure
  - `rootlevel`: `state.json` at project root (planner-created)

#### Status Reporter
- Fixed document completion detection to match state.json format (string keys like `"doc1_crucible_thesis"`)
- Fixed phase detection to recognize in-progress planning (checks `current_document` field)
- Updated path resolution for planning, outline, draft, and backup directories based on structure type

#### Detect Project
- Same structure detection improvements as status_reporter.py
- Planning progress now correctly reads from `state.json` for rootlevel projects
- File-based fallback detection for outline and draft directories

### Changed
- Both detection scripts now return structure type alongside project root
- Status report includes `structure_type` field in output

## [1.0.4] - 2025-12-14

### Fixed

#### Hook System Overhaul
- **Stop hook**: Changed from prompt-based to command-based
  - Prompt hooks cannot access file system, making review checks impossible
  - New `check_stop_conditions.py` script reads `draft-state.json` directly
  - Properly blocks session end when bi-chapter review is due
  - Prevents infinite loops via `stop_hook_active` check

- **SubagentStop hook**: Removed entirely
  - Prompt hooks cannot access agent output or file system
  - Was non-functional for validating review agent completeness

#### Hook Behavior
- Stop hook now correctly enforces bi-chapter reviews
- Exit code 2 with descriptive stderr message tells Claude exactly what to do
- Session cannot end until required reviews are completed

### Added

#### Scripts
- `check_stop_conditions.py` - Stop hook enforcement script
  - Reads project state from `.crucible/state/draft-state.json`
  - Checks `chapters_complete` vs `last_review_at_chapter`
  - Returns exit code 2 with action instructions when blocked
  - Returns exit code 0 when session can safely end

#### Enhanced Backup Script
- `backup_on_change.py` now includes chapter detection and review reminders:
  - `is_chapter_file()` - Detects chapter files by name patterns
  - `check_review_status()` - Checks if bi-chapter review is due
  - Outputs `hookSpecificOutput.additionalContext` as soft reminder
  - Claude receives context about pending reviews after chapter edits

### Changed

#### Hook Configuration
- SessionStart timeout increased from 10s to 15s for larger projects
- Stop hook now uses command type instead of prompt type
- Removed SubagentStop hook from configuration
- Updated description to reflect "review enforcement" purpose

### Technical Details
- All hooks now use command-based approach for file system access
- PostToolUse provides soft reminders via `additionalContext`
- Stop hook provides hard enforcement via exit code 2
- Hybrid approach: gentle nudges + strict gates

## [1.0.5] - 2025-12-18

### Fixed

#### Hook Output Compliance
- **backup_on_change.py**: Now outputs only `hookSpecificOutput` per official Claude Code hooks specification
  - Removed non-spec fields (`success`, `action`, `backup_result`)
  - Empty `{}` output when no context needed
  - `hookSpecificOutput.additionalContext` only when review reminder is required

#### Model Specification
- Updated model shorthand `haiku` to full model ID `claude-haiku-4-20250514` in 4 files:
  - `commands/crucible-restore.md`
  - `commands/crucible-status.md`
  - `agents/timeline-checker.md`
  - `agents/outline-checker.md`

#### Windows Compatibility
- **safe_write_json()**: Fixed atomicity issue on Windows
  - Added fallback delete-then-move pattern when `Path.replace()` fails
  - Temp file cleanup on error

#### Error Handling
- **backup_on_change.py**: Added comprehensive OSError handling
  - Handles stdin read errors alongside JSON decode errors
  - Graceful handling of filesystem errors during project detection
  - Cleanup block now handles permission errors and file-in-use scenarios

### Changed

#### Path Encoding for Incremental Backups
- **backup_on_change.py**: Now uses base64url encoding for backup filenames
  - Replaces ambiguous underscore-based path flattening
  - Reversible encoding allows exact path reconstruction
  - Example: `draft/chapter-1.md` → `ZHJhZnQvY2hhcHRlci0xLm1k`

- **restore_project.py**: Backward-compatible path decoding
  - Tries base64url decode first (new format)
  - Falls back to underscore heuristics (legacy format)
  - Existing backups remain fully restorable

### Added

#### Shared Utilities
- **cross_platform.py**: New path encoding functions
  - `encode_path_b64(path)` - URL-safe base64 encoding
  - `decode_path_b64(encoded)` - Decode with padding restoration
  - `is_base64_encoded_path(s)` - Format detection for backward compatibility

### Technical Details
- All hook outputs now comply with official `hooks.md` specification
- Base64url encoding uses Python's `base64.urlsafe_b64encode/decode`
- Backward compatibility maintained for all existing incremental backups
- Cross-platform tested on Windows and Unix-like systems

## [1.0.10] - 2025-12-19

### Fixed

#### Model Specification
- Fixed invalid model ID in `crucible-status.md` and `crucible-restore.md`
  - Changed from non-existent `claude-haiku-4-20250514` to valid `claude-haiku-4-5-20251001`
  - Commands were failing with 404 API errors due to invalid model reference

#### Hook Configuration
- Temporarily disabled hooks to resolve plugin cache version mismatch
  - Hooks were referencing stale cached paths after version updates
  - Requires Claude Code restart to properly reload plugin configuration
  - Re-enable hooks after restart by restoring hooks.json content

### Changed

#### Plugin Installation Path
- Updated installed_plugins.json to point to source directory for local development
  - Allows immediate testing of plugin changes without cache rebuild

## [1.0.9] - 2025-12-19

### Added

#### Project Metadata Updates
- Added `--set` argument to `save_state.py` for updating project metadata
  - `--set title "Title"` - Update project title
  - `--set premise "Premise"` - Update project premise
  - Supports multiple `--set` flags in a single call
  - Also works for scope fields: target_length, complexity, chapters
- Example: `python save_state.py ./project --set title "New Title" --set premise "New premise"`

## [1.0.8] - 2025-12-19

### Fixed

#### Scope Answer Handling
- `save_state.py` now handles "scope" as a special document key
  - Previously failed with `KeyError: 'scope'` when skill saved scope answers via `--answer`
  - Scope answers now correctly stored in `state["scope"]` instead of `state["answers"]["scope"]`
  - Added key mapping for variations: `novel_length` -> `target_length`, `narrative_complexity` -> `complexity`
  - Automatically calculates chapter count when target_length is set

## [1.0.7] - 2025-12-19

### Fixed

#### Windows Console Encoding
- Replaced all emoji characters with ASCII equivalents in Python scripts
  - `✅` → `[OK]`
  - `❌` → `[ERROR]`
  - `✓` → `[x]` or `+`
- Windows cmd/PowerShell cannot encode Unicode emoji (charmap codec error)
- Affected 15+ scripts across planner, outliner, writer, and migration tools
- All console output now uses safe ASCII characters

### Changed
- All print statements now Windows-compatible without encoding workarounds

## [1.0.6] - 2025-12-18

### Added

#### New Scripts
- `draft_utils.py` - Shared draft utilities
- `extract_invented_markers.py` - Extract invention markers from prose
- `validate_before_write.py` - Pre-write validation
- `restore_backup.py` / `restore_project.py` - Backup restoration utilities

#### Story Bible Commands
- `story-bible-commands.md` reference for Writer skill

#### Bi-Chapter Review Reference
- `bi-chapter-review.md` documentation for review process

### Changed
- Enhanced cross_platform.py with additional project detection methods
- Updated hook configurations for better reliability
- Improved backup directory handling for different project structures

## [Unreleased]

### Planned
- Enhanced series support for multi-book projects
- Export to common writing software formats
- Integration with external writing tools
- Custom beat structure modifications
