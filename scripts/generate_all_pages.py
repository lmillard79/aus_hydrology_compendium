"""
Generate all missing conference pages from raw data files.

For each conference year (FMA and HWRS), generates:
1. Updated mindmap overview page (with ASCII tree, themes, practitioner insights,
   research gaps, cross-cutting connections)
2. Individual theme detail pages in conference subdirectories

Usage:
    python scripts/generate_all_pages.py
    python scripts/generate_all_pages.py --dry-run   # preview without writing
    python scripts/generate_all_pages.py --conference fma_2023  # single conference
"""

import argparse
import json
import re
import sys
from pathlib import Path


DATA_DIR = Path("docs/data/conference-papers")
PAGES_DIR = Path("docs/conference-papers")
MKDOCS_YML = Path("mkdocs.yml")

CONFERENCE_META = {
    "fma_2019": {"label": "FMA 2019", "series": "FMA", "year": 2019, "sources": 137},
    "fma_2020": {"label": "FMA 2020", "series": "FMA", "year": 2020, "sources": 19},
    "fma_2022": {"label": "FMA 2022", "series": "FMA", "year": 2022, "sources": 72},
    "fma_2023": {"label": "FMA 2023", "series": "FMA", "year": 2023, "sources": 79},
    "fma_2024": {"label": "FMA 2024", "series": "FMA", "year": 2024, "sources": 118},
    "fma_2025": {"label": "FMA 2025", "series": "FMA", "year": 2025, "sources": 140},
    "hwrs_2005": {"label": "HWRS 2005", "series": "HWRS", "year": 2005, "sources": 66},
    "hwrs_2011": {"label": "HWRS 2011", "series": "HWRS", "year": 2011, "sources": 299},
    "hwrs_2012": {"label": "HWRS 2012", "series": "HWRS", "year": 2012, "sources": 145},
    "hwrs_2014": {"label": "HWRS 2014", "series": "HWRS", "year": 2014, "sources": 88},
    "hwrs_2015": {"label": "HWRS 2015", "series": "HWRS", "year": 2015, "sources": 138},
    "hwrs_2016": {"label": "HWRS 2016", "series": "HWRS", "year": 2016, "sources": 48},
    "hwrs_2018": {"label": "HWRS 2018", "series": "HWRS", "year": 2018, "sources": 61},
    "hwrs_2021": {"label": "HWRS 2021", "series": "HWRS", "year": 2021, "sources": 79},
    "hwrs_2022": {"label": "HWRS 2022", "series": "HWRS", "year": 2022, "sources": 124},
    "hwrs_2023": {"label": "HWRS 2023", "series": "HWRS", "year": 2023, "sources": 135},
    "hwrs_2024": {"label": "HWRS 2024", "series": "HWRS", "year": 2024, "sources": 161},
    "hwrs_2025": {"label": "HWRS 2025", "series": "HWRS", "year": 2025, "sources": 129},
}

# These already have hand-crafted theme detail pages — skip regenerating them
SKIP_THEME_PAGES = {"fma_2024", "fma_2025"}


def load_json(path: Path) -> dict | None:
    """Load a JSON file, returning None if missing."""
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_text(path: Path) -> str:
    """Load a text file, stripping the header block before the === separator."""
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8")
    sep = "=" * 60
    if sep in content:
        parts = content.split(sep, 2)
        return parts[-1].strip() if len(parts) >= 2 else content.strip()
    return content.strip()


def json_to_ascii_tree(node: dict, prefix: str = "", is_last: bool = True) -> list[str]:
    """Recursively convert a JSON mind map node to ASCII tree lines."""
    connector = "└── " if is_last else "├── "
    lines = [prefix + connector + node["name"]]
    children = node.get("children", [])
    extension = "    " if is_last else "│   "
    for i, child in enumerate(children):
        lines.extend(
            json_to_ascii_tree(child, prefix + extension, i == len(children) - 1)
        )
    return lines


def build_ascii_tree(mindmap_json: dict) -> str:
    """Build a full ASCII tree string from the raw mindmap JSON."""
    root_name = mindmap_json.get("name", "Mind Map")
    lines = [root_name]
    children = mindmap_json.get("children", [])
    for i, child in enumerate(children):
        lines.extend(json_to_ascii_tree(child, "", i == len(children) - 1))
    return "\n".join(lines)


def slugify(text: str) -> str:
    """Convert a theme name to a URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def get_theme_slug(theme_name: str, index: int) -> str:
    """Generate a consistent slug for a theme."""
    return slugify(theme_name)


def generate_theme_page(
    conf_key: str,
    meta: dict,
    theme: dict,
    index: int,
    mindmap_title: str,
) -> str:
    """Generate a theme detail page from a theme dict."""
    theme_name = theme["theme"]
    subtopics = theme.get("subtopics", [])
    content = theme.get("query_response", "").strip()
    label = meta["label"]
    series = meta["series"]
    year = meta["year"]
    conf_slug = conf_key.replace("_", "-")

    subtopic_list = "\n".join(f"- {s}" for s in subtopics) if subtopics else ""

    return f"""# {theme_name}

**Conference:** {label} — {mindmap_title}  
**Theme {index + 1} of {series} {year}**

---

## Overview

{subtopic_list}

---

## Detailed Analysis

{content}

---

**See Also:**
- [← {label} Mind Map Overview](../{conf_slug}-mindmap.md)
- [Conference Papers Home](../index.md)
"""


def generate_mindmap_page(
    conf_key: str,
    meta: dict,
    mindmap_json: dict,
    themes_json: dict | None,
    practitioner_text: str,
    connections_text: str,
    gaps_text: str,
    theme_slugs: list[tuple[str, str]],
    has_theme_pages: bool,
) -> str:
    """Generate the full mindmap overview page for a conference."""
    label = meta["label"]
    series = meta["series"]
    year = meta["year"]
    sources = meta["sources"]
    conf_slug = conf_key.replace("_", "-")
    mindmap_title = mindmap_json.get("name", f"{label} Research")

    ascii_tree = build_ascii_tree(mindmap_json)

    themes_section = ""
    if themes_json:
        theme_entries = []
        for i, theme in enumerate(themes_json.get("themes", [])):
            name = theme["theme"]
            subtopics = theme.get("subtopics", [])
            slug = slugify(name)
            if has_theme_pages:
                header = f"### {i + 1}. [{name}]({conf_slug}/{slug}.md)"
            else:
                header = f"### {i + 1}. {name}"
            bullet_list = "\n".join(f"- {s}" for s in subtopics[:4])
            theme_entries.append(f"{header}\n{bullet_list}")
        themes_section = "\n\n".join(theme_entries)

    theme_pages_section = ""
    if has_theme_pages and theme_slugs:
        links = "\n".join(
            f"- [{name}]({conf_slug}/{slug}.md)" for name, slug in theme_slugs
        )
        theme_pages_section = f"""---

## Theme Detail Pages

{links}
"""

    practitioner_section = ""
    if practitioner_text:
        practitioner_section = f"""---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

{practitioner_text}
"""

    connections_section = ""
    if connections_text:
        connections_section = f"""---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

{connections_text}
"""

    gaps_section = ""
    if gaps_text:
        gaps_section = f"""---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

{gaps_text}
"""

    series_full = (
        "Floodplain Management Australia"
        if series == "FMA"
        else "Hydrology & Water Resources Society"
    )

    return f"""# {label} Mind Map

## {mindmap_title}

**Conference:** {series_full} {year}  
**Sources:** {sources} papers  
**Generated:** April 2026

---

## Mind Map Structure

```
{ascii_tree}
```

---

## Main Themes

{themes_section}

{theme_pages_section}{practitioner_section}{connections_section}{gaps_section}---

**See Also:**
- [Conference Papers Home](index.md)
"""


def process_conference(
    conf_key: str, dry_run: bool = False
) -> tuple[str, list[tuple[str, str]]]:
    """
    Process a single conference, generating/updating all its pages.

    Returns (mindmap_page_path, [(theme_name, slug), ...]) for nav building.
    """
    meta = CONFERENCE_META[conf_key]
    conf_slug = conf_key.replace("_", "-")
    label = meta["label"]

    mindmap_json = load_json(DATA_DIR / f"{conf_key}_raw_mindmap.json")
    if not mindmap_json:
        print(f"  SKIP {label}: no raw mindmap JSON found")
        return "", []

    themes_json = load_json(DATA_DIR / f"{conf_key}_all_themes_detailed.json")
    practitioner_text = load_text(DATA_DIR / f"{conf_key}_practitioner.txt")
    connections_text = load_text(DATA_DIR / f"{conf_key}_connections.txt")
    gaps_text = load_text(DATA_DIR / f"{conf_key}_gaps.txt")

    has_theme_pages = conf_key not in SKIP_THEME_PAGES
    theme_slugs: list[tuple[str, str]] = []

    if themes_json and has_theme_pages:
        mindmap_title = themes_json.get("metadata", {}).get(
            "mind_map_title", mindmap_json.get("name", "")
        )
        theme_dir = PAGES_DIR / conf_slug
        if not dry_run:
            theme_dir.mkdir(parents=True, exist_ok=True)

        for i, theme in enumerate(themes_json.get("themes", [])):
            slug = slugify(theme["theme"])
            theme_slugs.append((theme["theme"], slug))
            page_content = generate_theme_page(
                conf_key, meta, theme, i, mindmap_title
            )
            theme_path = theme_dir / f"{slug}.md"
            if dry_run:
                print(f"  [DRY RUN] Would write: {theme_path}")
            else:
                theme_path.write_text(page_content, encoding="utf-8")
                print(f"  Wrote theme page: {theme_path}")
    else:
        mindmap_title = mindmap_json.get("name", "")

    mindmap_content = generate_mindmap_page(
        conf_key,
        meta,
        mindmap_json,
        themes_json,
        practitioner_text,
        connections_text,
        gaps_text,
        theme_slugs,
        has_theme_pages,
    )

    mindmap_path = PAGES_DIR / f"{conf_slug}-mindmap.md"
    if dry_run:
        print(f"  [DRY RUN] Would write: {mindmap_path}")
    else:
        mindmap_path.write_text(mindmap_content, encoding="utf-8")
        print(f"  Wrote mindmap page: {mindmap_path}")

    return f"conference-papers/{conf_slug}-mindmap.md", theme_slugs


def build_nav_block(
    results: dict[str, tuple[str, list[tuple[str, str]]]]
) -> str:
    """Build the nav YAML block for Conference Papers section."""
    fma_years = sorted(
        [k for k in CONFERENCE_META if k.startswith("fma_")],
        key=lambda x: -CONFERENCE_META[x]["year"],
    )
    hwrs_years = sorted(
        [k for k in CONFERENCE_META if k.startswith("hwrs_")],
        key=lambda x: -CONFERENCE_META[x]["year"],
    )

    lines = ["  - Conference Papers:"]
    lines.append("    - Overview: conference-papers/index.md")
    lines.append("    - FMA Conferences:")

    for conf_key in fma_years:
        meta = CONFERENCE_META[conf_key]
        label = meta["label"]
        conf_slug = conf_key.replace("_", "-")
        _, theme_slugs = results.get(conf_key, ("", []))

        if theme_slugs:
            lines.append(f"      - {label}:")
            lines.append(
                f"        - Overview: conference-papers/{conf_slug}-mindmap.md"
            )
            for theme_name, slug in theme_slugs:
                lines.append(
                    f"        - {theme_name}: conference-papers/{conf_slug}/{slug}.md"
                )
        else:
            lines.append(
                f"      - {label}: conference-papers/{conf_slug}-mindmap.md"
            )

    lines.append("    - HWRS Conferences:")
    lines.append("      - HWRS Mind Map Index: conference-papers/hwrs-index.md")

    for conf_key in hwrs_years:
        meta = CONFERENCE_META[conf_key]
        label = meta["label"]
        conf_slug = conf_key.replace("_", "-")
        _, theme_slugs = results.get(conf_key, ("", []))

        if theme_slugs:
            lines.append(f"      - {label}:")
            lines.append(
                f"        - Overview: conference-papers/{conf_slug}-mindmap.md"
            )
            for theme_name, slug in theme_slugs:
                lines.append(
                    f"        - {theme_name}: conference-papers/{conf_slug}/{slug}.md"
                )
        else:
            lines.append(
                f"      - {label}: conference-papers/{conf_slug}-mindmap.md"
            )

    return "\n".join(lines)


def update_mkdocs_nav(nav_block: str, dry_run: bool = False) -> None:
    """Replace the Conference Papers section in mkdocs.yml."""
    content = MKDOCS_YML.read_text(encoding="utf-8")

    start_marker = "  - Conference Papers:"
    end_markers = [
        "\n  - Glossary:",
        "\n  - About:",
        "\n  - Cross-Cutting",
    ]

    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("WARNING: Could not find '- Conference Papers:' in mkdocs.yml")
        return

    end_idx = len(content)
    for marker in end_markers:
        idx = content.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx

    new_content = content[:start_idx] + nav_block + "\n" + content[end_idx:]

    if dry_run:
        print("\n[DRY RUN] mkdocs.yml Conference Papers nav block would become:")
        print(nav_block[:500] + "...")
    else:
        MKDOCS_YML.write_text(new_content, encoding="utf-8")
        print(f"\nUpdated mkdocs.yml nav ({len(nav_block)} chars)")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing files",
    )
    parser.add_argument(
        "--conference",
        help="Process a single conference key (e.g. fma_2023)",
    )
    args = parser.parse_args()

    conferences = (
        [args.conference]
        if args.conference
        else list(CONFERENCE_META.keys())
    )

    if args.conference and args.conference not in CONFERENCE_META:
        print(f"Unknown conference key: {args.conference}")
        print(f"Valid keys: {', '.join(CONFERENCE_META.keys())}")
        sys.exit(1)

    results: dict[str, tuple[str, list[tuple[str, str]]]] = {}

    for conf_key in conferences:
        meta = CONFERENCE_META[conf_key]
        print(f"\nProcessing {meta['label']}...")
        mindmap_path, theme_slugs = process_conference(conf_key, args.dry_run)
        results[conf_key] = (mindmap_path, theme_slugs)

    if not args.conference:
        print("\nUpdating mkdocs.yml nav...")
        nav_block = build_nav_block(results)
        update_mkdocs_nav(nav_block, args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
