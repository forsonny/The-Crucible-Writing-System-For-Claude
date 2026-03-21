# Crucible Project Memory

## Project Info
- **Title**: [TITLE]
- **Series**: [SERIES NAME] Book [#]
- **Genre**: [GENRE — fantasy/sci-fi/dystopian-utopian/space-opera/thriller/alternate-history/romantasy]
- **Genre Pack**: genre-packs/[GENRE]/
- **Target**: [TARGET] words
- **Current**: [CURRENT] words

## Current Status
- **Phase**: [planning|outlining|writing|editing]
- **Chapter**: [#]
- **Scene**: [#]
- **Last Activity**: [DATE]

## Project Rules
- Never invent characters not in the Constellation Bible
- Never create plot points not in the outline
- Always verify against story bible before writing
- Flag `[INVENTED: description]` for any invented details
- Save state after every scene

## Commands
- `/crucible-suite:crucible-status` - Check progress
- `/crucible-suite:crucible-continue` - Resume from any phase
- `/crucible-suite:crucible-plan` - Start or continue planning
- `/crucible-suite:crucible-outline` - Generate chapter outlines
- `/crucible-suite:crucible-write` - Draft prose
- `/crucible-suite:crucible-edit` - Revise manuscript
- `/crucible-suite:crucible-review` - Trigger manual review
- `/crucible-suite:crucible-restore` - Restore from backup

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
