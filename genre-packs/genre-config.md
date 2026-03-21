# Genre Configuration System

The Crucible Writing System supports multiple fiction genres through **genre packs**. Each genre pack provides genre-specific rules, question options, and world-building guidance while keeping the core 36-beat Crucible Structure intact.

## How Genre Selection Works

1. During **Phase 1: Intake** of the Crucible Planner, the user selects their genre
2. The genre pack is loaded, providing:
   - **Genre Rules** (`genre-rules.md`) — Conventions, tropes, expectations
   - **Question Overrides** (`question-overrides.md`) — Genre-flavored options for planning questions
   - **World-Building Guide** (`world-building-guide.md`) — Genre-specific world-building considerations
3. The base Crucible Structure (36 beats, 3 strands, Forge Points, Mercy Engine) remains unchanged
4. Genre-specific rules are applied alongside the base rules during writing

## Available Genre Packs

| Genre | Directory | Best For |
|-------|-----------|----------|
| Fantasy | `genre-packs/fantasy/` | Epic/high fantasy, sword & sorcery, low fantasy |
| Sci-Fi | `genre-packs/sci-fi/` | Hard SF, soft SF, cyberpunk, biopunk, post-singularity |
| Dystopian/Utopian | `genre-packs/dystopian-utopian/` | Dystopia, utopia, post-apocalyptic, totalitarian |
| Space Opera | `genre-packs/space-opera/` | Galactic-scale SF, military SF, space adventure |
| Thriller | `genre-packs/thriller/` | Psychological, political, tech, espionage, conspiracy |
| Alternate History | `genre-packs/alternate-history/` | Historical divergence, counterfactual, secret history |
| Romantasy | `genre-packs/romantasy/` | Fantasy romance, romantic fantasy, fae romance |

## Strand Mapping Across Genres

The three Crucible strands adapt naturally to each genre:

| Strand | Fantasy | Sci-Fi | Thriller | Romantasy |
|--------|---------|--------|----------|-----------|
| **Quest** | Destroy artifact, save kingdom | Solve anomaly, complete mission | Expose conspiracy, survive | Break curse, save realm |
| **Fire** | Magic that corrupts | Tech/augmentation with cost | Obsession, moral compromise | Forbidden power/bond |
| **Constellation** | Fellowship, sworn bonds | Crew, AI companions | Handler/asset, allies | Court politics, forbidden love |

## Loading a Genre Pack

When the planner asks genre selection, it should:

1. Read `genre-packs/<selected-genre>/genre-rules.md`
2. Read `genre-packs/<selected-genre>/question-overrides.md`
3. Read `genre-packs/<selected-genre>/world-building-guide.md`
4. Apply genre-specific question options during the planning questionnaire
5. Store the selected genre in project state for use by outliner, writer, and editor

## Creating Custom Genre Packs

To create a new genre pack:

1. Create a directory under `genre-packs/`
2. Add three files: `genre-rules.md`, `question-overrides.md`, `world-building-guide.md`
3. Follow the structure of existing packs
4. The system will automatically detect and offer new packs during genre selection
