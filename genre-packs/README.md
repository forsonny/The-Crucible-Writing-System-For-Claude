# Genre Packs — Multi-Genre Crucible Writing System

## Overview

The Crucible Writing System's 36-beat narrative framework is genre-agnostic at its core. The three strands (Quest, Fire, Constellation), five Forge Points, Mercy Engine, and Dark Mirror antagonist system work across all fiction genres. Genre packs provide the genre-specific layer on top of this universal foundation.

## How It Works

```
                    ┌─────────────────────┐
                    │   Genre Selection   │ ← Phase 1 of Planner
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   genre-rules.md    question-overrides.md   world-building-guide.md
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Base Crucible      │
                    │  36 Beats           │
                    │  3 Strands          │
                    │  5 Forge Points     │
                    │  Mercy Engine       │
                    │  Dark Mirror        │
                    └─────────────────────┘
```

## Available Genre Packs

### Fantasy (`fantasy/`)
Epic/high fantasy, sword & sorcery, dark fantasy, low fantasy. Magic systems, medieval-inspired worlds, ancient prophecies, quests.

**Strand Mapping:** Quest = destroy/protect artifact, save kingdom | Fire = magic that corrupts | Constellation = fellowship, sworn bonds

### Sci-Fi (`sci-fi/`)
Hard SF, soft SF, cyberpunk, biopunk, solarpunk, post-singularity, near/far-future, military SF, first contact.

**Strand Mapping:** Quest = solve anomaly, complete mission | Fire = tech/augmentation with cost | Constellation = crew, AI companions

### Dystopian/Utopian (`dystopian-utopian/`)
Totalitarian dystopia, corporate dystopia, ecological dystopia, social media dystopia, ambiguous utopia, fallen utopia, post-apocalyptic rebuilding.

**Strand Mapping:** Quest = expose/overthrow the system | Fire = ability to see through the regime | Constellation = resistance cell, defectors

### Space Opera (`space-opera/`)
Galactic-scale adventure, military SF, new space opera, planetary romance, galactic empire, space western, space fantasy.

**Strand Mapping:** Quest = galactic-scale mission | Fire = psionic/alien power | Constellation = ship crew, multi-species alliance

### Thriller (`thriller/`)
Psychological, political, techno-thriller, espionage, conspiracy, legal, medical thriller.

**Strand Mapping:** Quest = expose conspiracy, survive | Fire = obsession, moral compromise | Constellation = handler/asset, informants, allies

### Alternate History (`alternate-history/`)
Military alt-history, political alt-history, secret history, supernatural alt-history, steampunk/dieselpunk, counterfactual memoir.

**Strand Mapping:** Quest = navigate/correct the divergence | Fire = forbidden knowledge of the true timeline | Constellation = resistance, archivists, descendants

### Romantasy (`romantasy/`)
Fae romance, dark romantasy, cozy romantasy, court intrigue romance, warrior romance, academy romantasy, reverse harem.

**Strand Mapping:** Quest = break curse, save realm (intertwined with romance) | Fire = the bond/attraction that threatens to consume | Constellation = court politics, forbidden love, the couple as constellation center

## Each Genre Pack Contains

| File | Purpose |
|------|---------|
| `genre-rules.md` | Genre conventions, prose guidelines, dialogue rules, trope guidance, subgenre notes |
| `question-overrides.md` | Genre-flavored options for planning questions (replaces base options by question ID) |
| `world-building-guide.md` | Genre-specific world-building guidance with World Forge mapping |

## The Universal Core (What Doesn't Change)

These elements remain identical across all genres:

- The 36-beat structure and 5 movements
- The three strands (Quest, Fire, Constellation) — only their *manifestation* changes
- The 5 Forge Points and their convergence requirements
- The Mercy Engine (4 acts of mercy with payoffs)
- The Dark Mirror antagonist design
- Anti-hallucination protocols
- Style capture and matching
- All Python automation scripts
- All 5 review agents (voice, continuity, outline, timeline, prose)
- The editor skill (all 4 editing levels)
- State management and session recovery

## Creating a Custom Genre Pack

1. Create a new directory under `genre-packs/`
2. Add three files following the structure of existing packs:
   - `genre-rules.md` — Start from the genre closest to yours and adapt
   - `question-overrides.md` — Override only the questions that need genre-specific options
   - `world-building-guide.md` — Focus on what makes your genre's world-building unique
3. The planner will automatically detect and offer the new genre during selection

## Hybrid Genres

For stories that blend genres (e.g., sci-fi thriller, dystopian romantasy), pick the **primary** genre pack and note the secondary genre in the project state. The writer can reference both genre packs during drafting.
