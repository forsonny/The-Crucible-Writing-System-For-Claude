---
name: crucible-planner
# prettier-ignore
description: Interactive planning system for fiction novels using the Crucible Structure—a 36-beat narrative framework with three interwoven story strands (Quest, Fire, Constellation), five Forge Points, and a Mercy Engine. Supports multiple genres including fantasy, sci-fi, dystopian/utopian, space opera, thriller, alternate history, and romantasy. Use when user wants to plan a novel, provides a story premise/synopsis, asks to "plan my book," wants to create planning documents, or mentions the Crucible Structure. Guides users through multi-choice questions to generate 7 planning document categories (14 files total) from a simple premise.
---

# Crucible Planner

Interactive planning system for fiction novels using the Crucible Structure. Supports multiple genres through genre packs.

## Overview

Starting from a simple premise, guide users through multi-choice questions to build seven interconnected planning document categories (14 files total):

1. **Crucible Thesis** — philosophical core
2. **Strand Maps** — Quest, Fire, Constellation (3 separate maps)
3. **Forge Point Blueprints** — five convergence crises
4. **Dark Mirror Profile** — antagonist design
5. **Constellation Bible** — character relationships
6. **Mercy Ledger** — mercy/payoff tracking
7. **World Forge** — world-building

## Before Starting

**Always read these references:**
- `references/crucible-structure.md` (the 36-beat structure)
- `references/question-sequences.md` (complete question flows)

**After genre selection, also read:**
- `genre-packs/<selected-genre>/genre-rules.md` (genre conventions)
- `genre-packs/<selected-genre>/question-overrides.md` (genre-specific question options)
- `genre-packs/<selected-genre>/world-building-guide.md` (genre world-building guidance)

## Workflow

```
Phase 1: INTAKE → Accept premise, initialize state, confirm scope
Phase 2: QUESTIONING → 9 document cycles with multi-choice questions
Phase 3: COMPILATION → Generate documents, present package
```

## Phase 1: Intake

### Accept Premise

Extract from user input:
- Core concept (1-2 sentences)
- Protagonist sketch
- Central conflict hint

**If premise too vague, use AskUserQuestion:**
```json
{
  "questions": [
    {
      "header": "Protagonist",
      "question": "Who is your protagonist?",
      "options": [
        {"label": "Reluctant chosen one", "description": "A chosen one who doesn't want the role"},
        {"label": "Ordinary hero", "description": "An ordinary person thrust into extraordinary circumstances"},
        {"label": "Fallen power", "description": "A powerful figure who's lost everything"},
        {"label": "Seeking redemption", "description": "A morally gray character seeking redemption"}
      ],
      "multiSelect": false
    }
  ]
}
```

### Initialize State

```bash
python scripts/init_project.py "./crucible-project" "Title" "Premise"
```

### Select Genre

**CRITICAL: Genre must be selected before scope confirmation.** This loads the genre pack that provides genre-specific question options, rules, and world-building guidance.

Use AskUserQuestion for genre selection:
```json
{
  "questions": [
    {
      "header": "Genre",
      "question": "What genre is your story?",
      "options": [
        {"label": "Fantasy", "description": "Epic/high fantasy, sword & sorcery, dark fantasy, low fantasy"},
        {"label": "Sci-Fi", "description": "Hard SF, soft SF, cyberpunk, biopunk, near/far-future"},
        {"label": "Space Opera", "description": "Galactic-scale adventure, military SF, space fantasy"},
        {"label": "Romantasy", "description": "Romantic fantasy, fae romance, fantasy with romance as co-plot"}
      ],
      "multiSelect": false
    }
  ]
}
```

If user selects "Other" or needs more options, offer second set:
```json
{
  "questions": [
    {
      "header": "Genre",
      "question": "Which of these genres fits your story?",
      "options": [
        {"label": "Dystopian/Utopian", "description": "Totalitarian, corporate, ecological, or fallen utopia"},
        {"label": "Thriller", "description": "Psychological, political, espionage, conspiracy, techno-thriller"},
        {"label": "Alternate History", "description": "Historical divergence, counterfactual, secret history"}
      ],
      "multiSelect": false
    }
  ]
}
```

**After genre selection:**
1. Store the genre in project state: `python scripts/save_state.py "<project_path>" --answer "meta" "genre" "What genre is your story?" "<selected>" "<description>"`
2. Read the three genre pack files from `genre-packs/<selected-genre>/`
3. Use genre-specific question options from `question-overrides.md` during Phase 2

### Confirm Scope

Use AskUserQuestion to confirm scope:
```json
{
  "questions": [
    {
      "header": "Novel Length",
      "question": "What is your target novel length?",
      "options": [
        {"label": "Standard", "description": "100-150K words, ~20-25 chapters"},
        {"label": "Epic", "description": "150-250K words, ~25-35 chapters"},
        {"label": "Extended/Series", "description": "250K+ words or multi-book series, 35+ chapters"}
      ],
      "multiSelect": false
    },
    {
      "header": "Complexity",
      "question": "What is your narrative complexity?",
      "options": [
        {"label": "Single POV", "description": "Single protagonist focus"},
        {"label": "Dual POV", "description": "Two protagonists sharing the story"},
        {"label": "Ensemble", "description": "Multiple POVs (3-5 characters)"}
      ],
      "multiSelect": false
    }
  ]
}
```

## Phase 2: Document Generation

### Questioning Rules

1. **ALWAYS use AskUserQuestion tool** for all questions (provides interactive UI)
2. **Max 4 options per question** (tool limit) + "Other" is automatic
3. **Max 4 questions per AskUserQuestion call**
4. **Reference previous answers** to build coherence
5. **Save state IMMEDIATELY after EACH answer** (see Answer Persistence below)
6. **Verify before moving to next document**

### Answer Persistence Workflow

**CRITICAL: Save every answer immediately after receiving it with FULL CONTEXT.** This ensures progress is preserved if the session fails and answers can be understood later.

#### Save Command Format

Each answer is saved with the question text, selected answer, and description:

```bash
python scripts/save_state.py "<project_path>" --answer "<document>" "<state_key>" "<question_text>" "<answer>" "<description>"
```

**Parameters:**
1. `document` - The document key (e.g., "doc1_crucible_thesis")
2. `state_key` - The field name (e.g., "burden_type")
3. `question_text` - The full question that was asked
4. `answer` - The selected option label
5. `description` - The description of the selected option

#### Step-by-Step Workflow

1. **Ask the question using AskUserQuestion:**
   ```json
   {
     "questions": [{
       "header": "Burden",
       "question": "What form does the external burden take in your story?",
       "options": [
         {"label": "Physical object", "description": "An artifact that must be destroyed or protected"},
         {"label": "Person to save", "description": "Someone who must be rescued or kept alive"}
       ],
       "multiSelect": false
     }]
   }
   ```

2. **User selects:** "Physical object"

3. **IMMEDIATELY save with full context:**
   ```bash
   python scripts/save_state.py "./crucible-project" --answer "doc1_crucible_thesis" "burden_type" "What form does the external burden take in your story?" "Physical object" "An artifact that must be destroyed or protected"
   ```

4. **Verify save succeeded** (output shows question and answer)

5. **Ask next question**

#### What Gets Saved

Each answer is stored as:
```json
{
  "question": "What form does the external burden take in your story?",
  "answer": "Physical object",
  "description": "An artifact that must be destroyed or protected"
}
```

This provides full context when resuming or reviewing progress.

#### Example Save Commands

**Document 1 (Crucible Thesis):**
```bash
python scripts/save_state.py "./project" --answer "doc1_crucible_thesis" "burden_type" "What form does the burden take?" "Physical object" "An artifact to destroy or protect"
python scripts/save_state.py "./project" --answer "doc1_crucible_thesis" "fire_type" "What is the Fire's nature?" "Magical ability" "A power that corrupts with use"
```

**Nested Documents (Forge Points, Mercies):**
```bash
python scripts/save_state.py "./project" --answer "doc5_forge_points.fp0_ignition" "quest_crisis" "What Quest crisis emerges?" "Artifact stolen" "Enemy takes the burden"
python scripts/save_state.py "./project" --answer "doc8_mercy_ledger.mercy_1" "recipient" "Who receives mercy?" "Enemy soldier" "A combatant who surrendered"
```

#### On Document Completion

After the verification question is confirmed:
```bash
python scripts/save_state.py "./crucible-project" --complete <doc_num>
```

This marks the document complete and advances progress to the next document.

#### Error Handling

If a save fails:
1. Retry once
2. If still failing, inform the user but continue (answer is in context)
3. User can manually recover using `/crucible-continue`

### Question Format

**CRITICAL: Use the AskUserQuestion tool, NOT plain text options.**

Example AskUserQuestion call:
```json
{
  "questions": [
    {
      "header": "Burden",
      "question": "What form does the external burden take in your story?",
      "options": [
        {"label": "Physical object", "description": "An artifact that must be destroyed or protected"},
        {"label": "Person to save", "description": "Someone who must be rescued or kept alive"},
        {"label": "Knowledge/truth", "description": "Information that must be revealed or protected"},
        {"label": "Mission/quest", "description": "A task that must be completed"}
      ],
      "multiSelect": false
    }
  ]
}
```

**Header examples** (max 12 chars): "Burden", "Fire Type", "Bond", "Antagonist", "Theme", "Sacrifice"

**For verification questions**, use multiSelect: true to allow checking multiple items.

### Document Sequence

See `references/question-sequences.md` for base question banks.

**IMPORTANT:** For each question, check `genre-packs/<genre>/question-overrides.md` for genre-specific options. If an override exists for a question ID, use the genre-specific options instead of (or alongside) the base options. This ensures questions feel natural for the selected genre.

**Document 1: Crucible Thesis (10 questions)**
- The Burden (external mission)
- The Fire (internal power/curse)
- Core Constellation Bond
- Dark Mirror Connection
- Forging Question
- Antagonist's Truth
- The Surrender
- Theme
- Blade's Purpose
- Verification

**Document 2: Quest Strand Map (7 questions)**
- Burden's Origin
- Why This Protagonist
- Antagonist's Stake
- Quest Escalation
- Impossible Requirement
- Resolution Method
- Verification

**Document 3: Fire Strand Map (7 questions)**
- Fire Manifestation
- The Danger
- Cost of Use
- Mastery Path
- Hardening Phase
- Mastery Moment
- Verification

**Document 4: Constellation Strand Map (7 questions)**
- Faithful Companion
- The Sacrifice
- Betrayal Source
- Expansion
- Bond That Saves
- Constellation Fate
- Verification

**Document 5: Forge Point Blueprints (5 × 4 questions)**
For each Forge Point (Ignition, First, Second, Third, Apex):
- Quest Crisis
- Fire Crisis  
- Constellation Crisis
- What is Sacrificed

**Document 6: Dark Mirror Profile (9 questions)**
- Origin Parallel
- The Divergence
- Antagonist's Want
- Compelling Offer
- Why Tempting
- Hidden Cost
- Defeat Method
- Antagonist's End
- Verification

**Document 7: Constellation Bible (12 questions)**
- Protagonist Profile
- Faithful Companion details
- Core Bond Character details
- Mentor/Catalyst
- Sacrifice Character
- Additional cast
- Verification

**Document 8: Mercy Ledger (4 × 4 questions)**
For each of 4 mercies:
- Recipient
- Merciful Act
- Immediate Cost
- Later Payoff

**Document 9: World Forge (9 questions)**
- World's Wound
- Power System Source
- Power Limitations
- Previous Wielders
- Key Locations
- World-Protagonist Mirror
- Magic Rules
- Timeline Framework
- Verification

---

### Phase 2 Complete

After completing Document 9 verification, Phase 2 is complete. All foundational planning documents have been created.

**Proceed to Phase 3** to compile the documents into the final planning structure by running compile_documents.py.

---

## Phase 3: Compilation

### Generate Documents

```bash
python scripts/compile_documents.py "./crucible-project"
```

Creates:
```
planning/
├── crucible-thesis.md
├── strand-maps/
│   ├── quest-strand.md
│   ├── fire-strand.md
│   └── constellation-strand.md
├── forge-points/
│   ├── fp0-ignition.md
│   ├── fp1-first-crucible.md
│   ├── fp2-second-crucible.md
│   ├── fp3-third-crucible.md
│   └── apex-willed-surrender.md
├── dark-mirror-profile.md
├── constellation-bible.md
├── mercy-ledger.md
├── world-forge.md
└── crucible-summary.md
```

### Present to User

```
✅ **Crucible Planning Complete!**

📄 [View Crucible Thesis](computer:///path/planning/crucible-thesis.md)
📄 [View Strand Maps](computer:///path/planning/strand-maps/)
📄 [View Forge Points](computer:///path/planning/forge-points/)
📄 [View Dark Mirror Profile](computer:///path/planning/dark-mirror-profile.md)
📄 [View Constellation Bible](computer:///path/planning/constellation-bible.md)
📄 [View Mercy Ledger](computer:///path/planning/mercy-ledger.md)
📄 [View World Forge](computer:///path/planning/world-forge.md)
📋 [View Quick Reference](computer:///path/planning/crucible-summary.md)

After presenting the document links, use AskUserQuestion for next steps:
```json
{
  "questions": [
    {
      "header": "Next Steps",
      "question": "What would you like to do next?",
      "options": [
        {"label": "Review documents", "description": "Review and adjust any planning document"},
        {"label": "Begin outline", "description": "Start creating chapter outlines from your plan"},
        {"label": "Start drafting", "description": "Jump straight into writing prose"}
      ],
      "multiSelect": false
    }
  ]
}
```

## State Management

Save after every question cluster:
```bash
python scripts/save_state.py "./crucible-project"
```

Resume interrupted session:
```bash
python scripts/load_state.py "./crucible-project"
```

## Bundled Resources

### references/
- `crucible-structure.md` — Complete 36-beat structure
- `question-sequences.md` — Full question bank by document
- `forge-point-rules.md` — Strand convergence mechanics
- `dark-mirror-guide.md` — Antagonist design
- `mercy-engine-guide.md` — Mercy/payoff mechanics

### assets/templates/
- Document templates for generation

### scripts/
- `init_project.py` — Initialize project
- `save_state.py` — Save progress
- `load_state.py` — Load progress
- `compile_documents.py` — Generate all documents
