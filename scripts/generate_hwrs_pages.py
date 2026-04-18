"""Generate HWRS mind map markdown pages from JSON data."""

import json
from pathlib import Path


def generate_tree(themes, indent=0):
    """Generate ASCII tree structure from themes."""
    lines = []
    for i, theme in enumerate(themes):
        is_last = i == len(themes) - 1
        prefix = "└── " if is_last else "├── "
        lines.append("    " * indent + prefix + theme["theme"])
        
        subtopics = theme.get("subtopics", [])
        for j, sub in enumerate(subtopics):
            sub_is_last = j == len(subtopics) - 1
            sub_prefix = "└── " if sub_is_last else "├── "
            lines.append("    " * (indent + 1) + sub_prefix + sub)
    
    return "\n".join(lines)


def generate_hwrs_markdown(json_file):
    """Generate markdown content from HWRS JSON file."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    year = data["year"]
    title = data.get("mind_map_title", f"HWRS {year} Research Highlights")
    sources = data["sources_count"]
    themes = data.get("main_themes", [])
    notebook_url = data.get("notebooklm_url", "")
    
    md = f"""# HWRS {year} Mind Map

## {title}

**Conference:** Hydrology & Water Resources Society {year}  
**Sources:** {sources} papers  
**Generated:** April 18, 2026  
**Interactive Map:** [View in NotebookLM]({notebook_url})

---

## Mind Map Structure

```
HWRS {year}
{generate_tree(themes)}
```

---

## Main Themes

"""
    
    for theme in themes:
        theme_name = theme["theme"]
        description = theme.get("description", "")
        subtopics = theme.get("subtopics", [])
        
        md += f"""### {theme_name}
"""
        if description:
            md += f"{description}\n\n"
        
        for sub in subtopics:
            md += f"- **{sub}**\n"
        
        md += "\n"
    
    # Add data link and footer
    md += f"""---

## Data

Full JSON data: [hwrs_{year}.json](../../data/conference-papers/hwrs_{year}.json)

---

**See Also:**
- [HWRS Mind Map Index](hwrs-index.md)
- [Conference Papers Home](index.md)
"""
    
    return md


def main():
    """Generate all HWRS mind map pages."""
    data_dir = Path("docs/data/conference-papers")
    output_dir = Path("docs/conference-papers")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all hwrs JSON files
    hwrs_files = sorted(data_dir.glob("hwrs_*.json"))
    
    for json_file in hwrs_files:
        # Skip raw mindmap files
        if "raw_mindmap" in json_file.name:
            continue
        
        year = json_file.stem.replace("hwrs_", "")
        output_file = output_dir / f"hwrs-{year}-mindmap.md"
        
        print(f"Generating {output_file}...")
        
        try:
            markdown = generate_hwrs_markdown(json_file)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"  ✓ Created {output_file}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
