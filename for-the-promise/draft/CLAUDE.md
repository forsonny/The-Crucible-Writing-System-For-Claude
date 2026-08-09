# Writing Phase Context

This CLAUDE.md loads when you access the draft/ directory.

## Writing Resources

### Story Bible (DO NOT IMPORT WHOLE FILE)
The story bible at `../story-bible.json` tracks all written content.
Query specific sections:

```bash
# Get current character states
python -c "import json; d=json.load(open('story-bible.json')); print(json.dumps(d.get('character_states', {}), indent=2))"

# Get chapter summary
python -c "import json; d=json.load(open('story-bible.json')); print(d.get('chapters', {}).get('CHAPTER_NUM', {}).get('summary', 'Not found'))"

# Get unresolved foreshadowing
python -c "import json; d=json.load(open('story-bible.json')); print([p for p in d.get('foreshadowing', {}).get('planted', []) if not p.get('paid_off')])"
```

### Style Profile
- `../style-profile.json` - Author voice characteristics (load once per session)

### Current Chapter Outline
- `../outline/chapter-[N].md` - Load ONLY current chapter outline

## What to Load Per Scene

**Required (load every scene):**
1. Current scene outline section
2. Style profile (if not already loaded)
3. Previous chapter summary (from story bible, ~200 words)
4. Active character states (from story bible)

**Load on-demand only:**
- Specific world details (only if scene requires)
- Specific foreshadowing threads (only if planting/paying off)

## What NOT to Load

- Full text of previous chapters (use summaries)
- Full planning documents (already incorporated in outline)
- Multiple chapter outlines at once
- Entire story bible (query specific sections)

## Writing Rules

- Save after EVERY scene
- Update story bible character states after every scene
- Flag any invented details as `[INVENTED: description]`
- Never write content not in the scene outline without asking
