# Crucible Suite

A Claude Code plugin for writing epic fantasy novels using the Crucible Structure--a 36-beat narrative framework with three interwoven story strands.

## Overview

Crucible Suite guides authors through the complete novel-writing process:

1. **Planning** - Interactive questionnaire generates 9 comprehensive planning documents
2. **Outlining** - Transform planning documents into detailed chapter-by-chapter outlines
3. **Writing** - Scene-by-scene drafting with style matching and anti-hallucination protocols
4. **Editing** - Multi-level revision from developmental editing to final polish

## Features

- **36-Beat Narrative Framework** - Structured story beats ensure compelling pacing
- **Three Interwoven Strands** - Quest (external), Fire (internal), Constellation (relationships)
- **Four Forge Points + Apex** - Critical convergence moments where all strands collide
- **Mercy Engine** - Track acts of mercy that pay off in the climax
- **Bi-Chapter Reviews** - Automated quality checks every 2 chapters
- **Anti-Hallucination Protocols** - Strict verification against planning documents
- **Automatic Backups** - Never lose your work

## Installation

### From GitHub (Recommended)

```bash
# Add the marketplace
/plugin marketplace add https://github.com/forsonny/The-Crucible-Writing-System-For-Claude.git

# Install the plugin
/plugin install crucible-suite@crucible-writing-system

# Restart Claude Code to activate
```

### Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/forsonny/The-Crucible-Writing-System-For-Claude.git
   ```
2. Add as local marketplace:
   ```bash
   /plugin marketplace add ./The-Crucible-Writing-System-For-Claude
   ```
3. Install:
   ```bash
   /plugin install crucible-suite@crucible-writing-system
   ```
4. Restart Claude Code

## Quick Start

### Start a New Project

```
/crucible-suite:crucible-plan [your premise]
```

Example:
```
/crucible-suite:crucible-plan A young blacksmith discovers she can forge weapons that steal memories. When her village is destroyed by a memory-hunting cult, she must master her forbidden gift to save the last people who remember the old ways.
```

### Continue Where You Left Off

```
/crucible-suite:crucible-continue
```

### Check Project Status

```
/crucible-suite:crucible-status
```

## Commands

| Command | Description |
|---------|-------------|
| `/crucible-suite:crucible-plan [premise]` | Start planning with a premise |
| `/crucible-suite:crucible-outline [book#]` | Create chapter outlines |
| `/crucible-suite:crucible-write [chapter#]` | Draft prose scene-by-scene |
| `/crucible-suite:crucible-edit [chapter#\|all]` | Revision and editing |
| `/crucible-suite:crucible-status` | Show project progress |
| `/crucible-suite:crucible-continue` | Resume from any phase |
| `/crucible-suite:crucible-review [range]` | Trigger manual review |
| `/crucible-suite:crucible-tic-audit [scope]` | Prose-tic scan against hard style caps, optional fix pass |
| `/crucible-suite:crucible-expand [scope] [target]` | Safe word-count expansion (fix-first, small additions) |
| `/crucible-suite:crucible-handoff [name]` | Session-close ritual: measured counts, bible sync, handoff doc |
| `/crucible-suite:crucible-restore [timestamp]` | Restore from backup |

## The Crucible Structure

### Three Strands

- **Quest Strand** - The external mission, burden, or objective
- **Fire Strand** - Internal power, curse, or transformation
- **Constellation Strand** - Relationships, community, bonds that anchor or break

### Six Movements

| Movement | Name | % of Book | Function |
|----------|------|-----------|----------|
| I | Ignition | 10% | Light the forge |
| II | First Tempering | 20% | Shape through failure |
| III | Scattering | 25% | Expand, harden, fragment |
| IV | Brightest Burning | 25% | Master, gather, choose |
| V | Final Forging | 15% | Converge, fail, transcend |
| Coda | Tempered Blade | 5% | Reveal what was made |

### Forge Points

Critical moments where all three strands collide:

| Forge Point | Location | Function |
|-------------|----------|----------|
| Ignition Forge | ~10% (Beat 6) | Threshold destroyed; no return |
| First Crucible | ~25% (Beat 11) | All strands in crisis; one sacrificed |
| Second Crucible | ~50% (Beat 21) | Harder choice, higher stakes |
| Third Crucible | ~75% (Beat 28) | Deepest sacrifice before finale |
| Apex Willed Surrender | ~90% (Beat 33) | Essential thing given up by choice |

## Review Agents

Five specialized agents analyze your prose during bi-chapter reviews:

| Agent | Focus |
|-------|-------|
| **voice-checker** | Style and voice consistency |
| **continuity-checker** | Plot and character continuity |
| **outline-checker** | Adherence to chapter outlines |
| **timeline-checker** | Chronological consistency |
| **prose-checker** | Craft-level feedback |

## Planning Documents

The planning phase generates 9 documents:

| Document | Purpose |
|----------|---------|
| **Crucible Thesis** | Core forging question and strand summaries |
| **Quest Strand Map** | External mission beats and progression |
| **Fire Strand Map** | Internal transformation arc |
| **Constellation Strand Map** | Relationship dynamics and bonds |
| **Forge Points** | Detailed convergence scenes (5 files) |
| **Dark Mirror Profile** | Antagonist as shadow of protagonist |
| **Constellation Bible** | Character relationships and dynamics |
| **Mercy Ledger** | Acts of mercy that pay off in climax |
| **World Forge** | Worldbuilding tied to theme |

## Project Structure

When you start a Crucible project, it creates:

```
your-project/
+-- CLAUDE.md                    # Project memory
+-- .crucible/
|   +-- state/
|       +-- planning-state.json  # Session state
+-- planning/
    +-- CLAUDE.md                # Planning context
    +-- strand-maps/             # Generated strand documents
    +-- forge-points/            # Forge point details
```

As you progress through phases, additional directories are created:

```
+-- outline/                     # Added during outlining
|   +-- CLAUDE.md
|   +-- by-chapter/
+-- draft/                       # Added during writing
|   +-- CLAUDE.md
|   +-- chapters/
+-- story-bible.json             # Generated during writing
+-- style-profile.json           # Captured from samples
```

## Requirements

- Claude Code (latest version recommended)
- Python 3.8+ (for automation scripts)

---

## Documentation

### Learn the Crucible Structure

The **[The-Crucible-Structure/](The-Crucible-Structure/)** folder contains comprehensive documentation for learning the framework -- whether you use the plugin or write by hand:

| Document | Description |
|----------|-------------|
| [Introduction](The-Crucible-Structure/00-introduction.md) | Overview and philosophy |
| [Quick Start](The-Crucible-Structure/01-quick-start.md) | Five-minute overview |
| [Tutorial Walkthrough](The-Crucible-Structure/13-tutorial-walkthrough.md) | Step-by-step planning guide |
| [Visual Diagrams](The-Crucible-Structure/15-visual-diagrams.md) | ASCII diagrams of the structure |
| [FAQ & Troubleshooting](The-Crucible-Structure/14-faq-and-troubleshooting.md) | Common questions and solutions |

**Core Concepts:**
- [The Three Strands](The-Crucible-Structure/02-the-three-strands.md) - Quest, Fire, Constellation
- [The 36 Beats](The-Crucible-Structure/03-the-36-beats.md) - Complete beat breakdown
- [Forge Points](The-Crucible-Structure/05-forge-points.md) - The five crisis moments
- [The Mercy Engine](The-Crucible-Structure/06-the-mercy-engine.md) - Compassion that pays off
- [The Dark Mirror](The-Crucible-Structure/07-the-dark-mirror.md) - Antagonist design

**Worksheets:** Printable planning templates in [worksheets/](The-Crucible-Structure/worksheets/)

**Examples:** Completed worksheets based on a sample story in [worksheets/examples/](The-Crucible-Structure/worksheets/examples/)

### Plugin Reference

Technical reference documentation for plugin developers:

| Skill | Reference Files |
|-------|-----------------|
| **crucible-planner** | `crucible-structure.md`, `dark-mirror-guide.md`, `forge-point-rules.md`, `mercy-engine-guide.md`, `question-key-mapping.md`, `question-sequences.md` |
| **crucible-outliner** | `beat-to-chapter-mapping.md`, `narrative-craft.md`, `outline-templates.md` |
| **crucible-writer** | `anti-hallucination.md`, `bi-chapter-review.md`, `context-management.md`, `prose-craft.md`, `story-bible-commands.md`, `style-capture.md`, `writing-process.md` |
| **crucible-editor** | `copy-editing-standards.md`, `developmental-checklist.md`, `line-editing-guide.md`, `polish-techniques.md` |

Access these via the `skills/[skill-name]/references/` directories.

## FAQ

**Q: Can I use Crucible Suite for non-fantasy genres?**
A: The 36-beat structure works well for any genre with strong character arcs. The terminology is fantasy-flavored, but the underlying principles--external goal, internal transformation, relationship dynamics--are universal.

**Q: How long should my novel be?**
A: Crucible Suite is optimized for epic fantasy (120,000-180,000 words). The 36 beats map to approximately 40-50 chapters at 3,000-4,000 words each.

**Q: Can I modify the beat structure?**
A: The planning documents you generate are fully editable. Adjust beat placement, merge beats, or split them as needed for your story.

**Q: What if I already have a partial draft?**
A: Use `/crucible-suite:crucible-continue` to detect your project state. You can generate planning documents retroactively or start outlining from any point.

**Q: How do bi-chapter reviews work?**
A: Every two chapters, the system automatically runs five review agents (voice, continuity, outline, timeline, prose) to catch issues early. You can also trigger reviews manually with `/crucible-suite:crucible-review`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Commands not recognized** | Ensure plugin is installed: check `~/.claude/plugins/crucible-suite/` exists |
| **Python scripts fail** | Verify Python 3.8+ is installed and in PATH |
| **Session state lost** | Run `/crucible-suite:crucible-restore` to recover from automatic backups |
| **Review agents timeout** | Large chapters may need more time; break into smaller scenes |
| **Planning seems stuck** | Use `/crucible-suite:crucible-status` to check progress, `/crucible-suite:crucible-continue` to resume |

## Contributing

Contributions are welcome! Here's how to help:

1. **Report Issues** - Found a bug or have a feature request? [Open an issue](https://github.com/forsonny/The-Crucible-Writing-System-For-Claude/issues)
2. **Submit PRs** - Fork the repo, make changes, and submit a pull request
3. **Share Feedback** - Tell us about your writing experience with Crucible Suite
4. **Spread the Word** - Star the repo and share with other fantasy writers

### Development Setup

```bash
# Clone the repository
git clone https://github.com/forsonny/The-Crucible-Writing-System-For-Claude.git
cd The-Crucible-Writing-System-For-Claude

# Test scripts
python scripts/detect_project.py
```

## License

MIT License - See [LICENSE](LICENSE) for details.

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/forsonny/The-Crucible-Writing-System-For-Claude/issues)
- **Documentation**: Reference files in `skills/*/references/` directories
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md) for version history

---

*Version 2.1.0 -- [Changelog](CHANGELOG.md) -- [License](LICENSE)*
