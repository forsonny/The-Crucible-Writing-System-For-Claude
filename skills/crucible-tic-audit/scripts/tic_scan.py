#!/usr/bin/env python3
"""Deterministic prose-tic scanner for Crucible manuscripts.

WHAT: Counts mechanical style tics per chapter file and compares them against
      hard per-chapter caps, emitting a PASS/FAIL report (text or JSON).
WHY:  Tic hunting by eye consumed whole editing sessions and expansion passes
      kept re-introducing the same tics (the "treadmill"). Regex counting is
      cheap, repeatable, and immune to reviewer fatigue. Judgment calls
      (over-explanation, metaphor drift in context) are NOT decided here --
      this script only counts and flags; the crucible-tic-audit skill's LLM
      pass rules on flagged items.

Usage:
    python3 tic_scan.py CHAPTER.md [CHAPTER2.md ...] [--caps CAPS.json] [--json]
    python3 tic_scan.py DRAFT_DIR [--caps CAPS.json] [--json]

Caps resolution order: --caps path, then tic-caps.json in the current working
directory (project root), then the bundled assets/tic-caps.json defaults.

Python 3.8+ compatible. Standard library only. ASCII output only.
"""

import argparse
import json
import os
import re
import sys

# WHAT: Filter-word constructions that put a perception verb between the
#       reader and the image. WHY: the style contract sets a hard cap of 0.
FILTER_PATTERNS = [
    r"\b(?:she|he|they|i)\s+(?:felt|saw|heard|noticed|realized|realised)\b",
    r"\bcould\s+(?:feel|see|hear)\b",
    r"\bseemed\s+to\b",
    r"\bas\s+if\b",
    r"\bas\s+though\b",
]

# WHAT: Dialogue-tag verbs other than "said"/"asked", counted only when they
#       sit adjacent to quoted dialogue (approximate tag detection).
# WHY:  The contract is "said only, action beats for variety"; these verbs used
#       outside dialogue tags are legitimate, so we anchor to quote marks.
BOOKISM_VERBS = (
    "exclaimed|retorted|breathed|confirmed|continued|spoke|muttered|whispered|"
    "hissed|growled|snapped|stated|declared|announced|replied|responded|"
    "interjected|queried|remarked|observed|offered|admitted|conceded"
)
BOOKISM_PATTERNS = [
    # "...," she exclaimed  /  "...?" Rumi whispered
    r"[\"”][,.]?\s+(?:\w+\s+)?(?:%s)\b" % BOOKISM_VERBS,
    # she exclaimed, "..."
    r"\b(?:%s)\s*[,:]?\s*[\"“]" % BOOKISM_VERBS,
]

# WHAT: "Not X. Y." rhetorical construction (a negation sentence of <=40 chars
#       followed immediately by a new sentence). Approximate by design.
NOT_X_Y_PATTERN = r"\bNot\s+[^.!?\n]{1,40}[.]\s+[A-Z*]"

# WHY: (?<!-)--(?!-) avoids counting markdown horizontal rules (---) as dashes.
EM_DASH_PATTERN = r"—|(?<!-)--(?!-)"
SCENE_SPLIT_PATTERN = r"(?m)^##\s+Scene\b"
SENTENCE_SPLIT_PATTERN = r"(?<=[.!?])\s+"


def load_caps(caps_arg):
    """Resolve the caps file: explicit flag > project root > bundled default."""
    candidates = []
    if caps_arg:
        candidates.append(caps_arg)
    candidates.append(os.path.join(os.getcwd(), "tic-caps.json"))
    bundled = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "assets", "tic-caps.json"
    )
    candidates.append(os.path.normpath(bundled))
    for path in candidates:
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                caps = json.load(f)
            caps["_source"] = path
            return caps
    print("[ERROR] No tic-caps.json found (looked for: %s)" % ", ".join(candidates))
    sys.exit(1)


def count_all(pattern, text):
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def strip_headings(text):
    """Remove markdown headings so titles don't pollute sentence stats."""
    return re.sub(r"(?m)^#{1,6}\s.*$", "", text)


def sentence_list(text):
    prose = strip_headings(text)
    # WHY: italicized fragments and dialogue still count as sentences for
    # rhythm purposes; we only drop empty splits.
    raw = re.split(SENTENCE_SPLIT_PATTERN, prose)
    return [s.strip() for s in raw if s.strip()]


def scan_file(path, caps):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    result = {"file": path, "counts": {}, "flags": {}, "violations": []}
    counts = result["counts"]

    counts["filter_words"] = sum(count_all(p, text) for p in FILTER_PATTERNS)
    counts["said_bookisms"] = sum(count_all(p, text) for p in BOOKISM_PATTERNS)
    counts["not_x_y"] = len(re.findall(NOT_X_Y_PATTERN, text))
    # WHY: "way-station" is world vocabulary, not the tic.
    counts["the_way"] = count_all(r"\bthe way\b", text) - count_all(
        r"\bthe way-station\b", text
    )
    counts["something"] = count_all(r"\bsomething\b", text)
    counts["noun_of_a_person_who"] = count_all(
        r"\bthe \w+ of (?:a|an) (?:person|man|woman|girl|boy|soldier|child)\s+who\b",
        text,
    )
    counts["the_particular"] = count_all(r"\bthe (?:particular|specific)\b", text)

    for phrase, cap in caps.get("signature_phrases", {}).items():
        key = "phrase:%s" % phrase
        counts[key] = count_all(re.escape(phrase), text)
        if counts[key] > cap:
            result["violations"].append((key, counts[key], cap))

    for word, cap in caps.get("signature_words", {}).items():
        key = "word:%s" % word
        # WHY: stem a trailing 'e' so "architecture" also counts
        # "architectural"/"architecturally" -- the crutch is the word family.
        stem = word[:-1] if word.endswith("e") else word
        counts[key] = count_all(r"\b%s\w*\b" % re.escape(stem), text)
        if counts[key] > cap:
            result["violations"].append((key, counts[key], cap))

    # Em-dashes are capped per SCENE, so split on scene headings.
    # WHY: segment 0 is the pre-"## Scene 1" chunk (chapter title); it is
    # counted into the total but not held to the per-scene cap. If a file has
    # no scene headings, the whole file is treated as one scene.
    segments = re.split(SCENE_SPLIT_PATTERN, text)
    dash_counts = [len(re.findall(EM_DASH_PATTERN, s)) for s in segments]
    counts["em_dashes_total"] = sum(dash_counts)
    scene_dashes = dash_counts[1:] if len(dash_counts) > 1 else dash_counts
    counts["em_dashes_per_scene"] = scene_dashes
    dash_cap = caps.get("em_dashes_per_scene", 3)
    for i, n in enumerate(scene_dashes, start=1):
        if n > dash_cap:
            result["violations"].append(("em_dashes scene %d" % i, n, dash_cap))

    # Sentence rhythm stats.
    sentences = sentence_list(text)
    if sentences:
        lengths = [len(s.split()) for s in sentences]
        counts["sentences"] = len(sentences)
        counts["avg_sentence_length"] = round(sum(lengths) / len(lengths), 1)
        long_w = caps.get("long_sentence_words", 40)
        vlong_w = caps.get("very_long_sentence_words", 60)
        counts["sentences_over_%d" % long_w] = sum(1 for n in lengths if n > long_w)
        counts["sentences_over_%d" % vlong_w] = sum(1 for n in lengths if n > vlong_w)
        the_openings = sum(1 for s in sentences if re.match(r"^[*\"“]?The\b", s))
        counts["declarative_opening_pct"] = round(100.0 * the_openings / len(sentences), 1)
        pct_cap = caps.get("declarative_opening_pct_max", 45)
        if counts["declarative_opening_pct"] > pct_cap:
            result["violations"].append(
                ("declarative_opening_pct", counts["declarative_opening_pct"], pct_cap)
            )

    # Simple-cap checks (per-chapter integers).
    for key in (
        "filter_words",
        "said_bookisms",
        "not_x_y",
        "the_way",
        "something",
        "noun_of_a_person_who",
        "the_particular",
    ):
        cap = caps.get(key)
        if cap is not None and counts[key] > cap:
            result["violations"].append((key, counts[key], cap))

    # WHAT: Metaphor-drift words are FLAGS, not violations. WHY: only context
    # can tell "the tide of refugees" (drift) from a literal river. The skill's
    # LLM pass rules on each flag.
    for domain, words in caps.get("metaphor_drift_watchlist", {}).items():
        hits = {}
        for w in words:
            n = count_all(r"\b%s\b" % re.escape(w), text)
            if n:
                hits[w] = n
        if hits:
            result["flags"][domain] = hits

    counts["word_count"] = len(strip_headings(text).split())
    return result


def format_report(results, caps):
    lines = []
    lines.append("=" * 60)
    lines.append("TIC SCAN REPORT   (caps: %s)" % caps.get("_source", "?"))
    lines.append("=" * 60)
    total_violations = 0
    for r in results:
        status = "PASS" if not r["violations"] else "FAIL (%d)" % len(r["violations"])
        total_violations += len(r["violations"])
        lines.append("")
        lines.append("%s  [%s]  %s words" % (
            r["file"], status, r["counts"].get("word_count", "?")))
        lines.append("-" * 60)
        for v in r["violations"]:
            lines.append("  [FAIL] %-28s %s (cap %s)" % v)
        show = (
            "filter_words", "said_bookisms", "not_x_y", "the_way", "something",
            "noun_of_a_person_who", "the_particular", "em_dashes_total",
            "avg_sentence_length", "declarative_opening_pct",
        )
        for key in show:
            if key in r["counts"]:
                lines.append("  %-35s %s" % (key, r["counts"][key]))
        for key, val in r["counts"].items():
            if key.startswith(("word:", "phrase:")):
                lines.append("  %-35s %s" % (key, val))
        if r["flags"]:
            lines.append("  metaphor-drift flags (verify in context, not auto-fail):")
            for domain, hits in r["flags"].items():
                pretty = ", ".join("%s x%d" % (w, n) for w, n in sorted(hits.items()))
                lines.append("    %-12s %s" % (domain, pretty))
    lines.append("")
    lines.append("=" * 60)
    lines.append("TOTAL: %d file(s), %d violation(s)" % (len(results), total_violations))
    lines.append("=" * 60)
    return "\n".join(lines)


def collect_targets(paths):
    """Expand directories to chapter files; exclude .pre-edit.md backups."""
    targets = []
    for p in paths:
        if os.path.isdir(p):
            for name in sorted(os.listdir(p)):
                if name.endswith(".md") and ".pre-edit" not in name and \
                        re.match(r"(?:ch|chapter)", name, re.IGNORECASE):
                    targets.append(os.path.join(p, name))
        elif os.path.isfile(p):
            targets.append(p)
        else:
            print("[ERROR] Not found: %s" % p)
            sys.exit(1)
    return targets


def main():
    parser = argparse.ArgumentParser(description="Crucible prose-tic scanner")
    parser.add_argument("paths", nargs="+", help="chapter files or draft directories")
    parser.add_argument("--caps", help="path to a tic-caps.json override")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args()

    caps = load_caps(args.caps)
    targets = collect_targets(args.paths)
    if not targets:
        print("[ERROR] No chapter files found in given paths")
        sys.exit(1)

    results = [scan_file(t, caps) for t in targets]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_report(results, caps))

    # Exit code signals violations so callers can gate on it.
    sys.exit(1 if any(r["violations"] for r in results) else 0)


if __name__ == "__main__":
    main()
