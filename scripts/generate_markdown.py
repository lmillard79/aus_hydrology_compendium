#!/usr/bin/env python3
"""
Generate Markdown pages from extracted NotebookLM JSON data.

This script creates the conference papers markdown pages from the JSON files
extracted by notebooklm_manager.py.

Usage:
    python generate_markdown.py
    
Output:
    - Updates docs/conference-papers/*.md files with latest data
"""

import json
import re
from datetime import datetime
from pathlib import Path


def generate_tree(themes: list, indent: int = 0) -> str:
    """Generate ASCII tree structure from themes."""
    lines = []
    for i, theme in enumerate(themes):
        is_last = (i == len(themes) - 1)
        prefix = "└── " if is_last else "├── "
        lines.append("  " * indent + prefix + theme.get('theme', theme.get('name', 'Unknown')))
        
        # Add subtopics
        subtopics = theme.get('subtopics', [])
        for j, sub in enumerate(subtopics):
            sub_is_last = (j == len(subtopics) - 1)
            sub_prefix = "└── " if sub_is_last else "├── "
            if isinstance(sub, dict):
                sub_name = sub.get('name', sub.get('topic', str(sub)))
            else:
                sub_name = str(sub).split(' - ')[0] if ' - ' in str(sub) else str(sub)
            lines.append("  " * (indent + 1) + sub_prefix + sub_name)
    
    return "\n".join(lines)


def generate_mindmap_markdown(data: dict) -> str:
    """Generate a mind map markdown page from notebook data."""
    
    name = data.get('notebook', 'Unknown')
    year = data.get('year', 'Unknown')
    conference = data.get('conference', 'Unknown')
    sources = data.get('sources_count', 0)
    title = data.get('mind_map_title', f'{conference} {year}')
    themes = data.get('main_themes', [])
    notebooklm_url = data.get('notebooklm_url', '')
    generated_date = data.get('generated_date', datetime.utcnow().isoformat())
    
    # Format filename base
    filename_base = f"{conference.lower()}-{year}-mindmap"
    
    md = f"""# {name} Mind Map

## {title}

**Conference:** {conference} {year}  
**Sources:** {sources} papers  
**Generated:** {generated_date[:10] if isinstance(generated_date, str) else generated_date}  
**Interactive Map:** [View in NotebookLM]({notebooklm_url})

---

## Mind Map Structure

```
{name}
{generate_tree(themes)}
```

---

## Main Themes

"""
    
    # Add each theme as a section
    for theme in themes:
        theme_name = theme.get('theme', theme.get('name', 'Unknown Theme'))
        description = theme.get('description', '')
        subtopics = theme.get('subtopics', [])
        
        md += f"""### {theme_name}
{description}

"""
        
        for sub in subtopics:
            if isinstance(sub, dict):
                sub_name = sub.get('name', sub.get('topic', str(sub)))
                sub_desc = sub.get('description', '')
                if sub_desc:
                    md += f"- **{sub_name}** - {sub_desc}\n"
                else:
                    md += f"- **{sub_name}**\n"
            else:
                # Handle string subtopics (format: "Name - Description")
                if ' - ' in str(sub):
                    parts = str(sub).split(' - ', 1)
                    md += f"- **{parts[0]}** - {parts[1]}\n"
                else:
                    md += f"- {sub}\n"
        
        md += "\n"
    
    # Add footer
    md += f"""---

## Data

Full JSON data: [{conference.lower()}_{year}.json](../data/conference-papers/{conference.lower()}_{year}.json)

---

**See Also:**
- [Conference Papers Home](index.md)
- [FMA 2024 Mind Map](fma-2024-mindmap.md)
- [FMA 2023 Mind Map](fma-2023-mindmap.md)
- [FMA 2019 Mind Map](fma-2019-mindmap.md)

---

*Last updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}*
"""
    
    return md


def generate_index_markdown(all_data: list) -> str:
    """Generate the main index page for conference papers."""
    
    total_papers = sum(d.get('sources_count', 0) for d in all_data)
    total_notebooks = len(all_data)
    
    # Separate FMA and HWRS
    fma_data = [d for d in all_data if d.get('conference') == 'FMA']
    hwrs_data = [d for d in all_data if d.get('conference') == 'HWRS']
    
    md = f"""# Conference Papers & Mind Maps

This section contains AI-generated mind map summaries of papers from major Australian hydrology and floodplain management conferences, extracted using Google NotebookLM.

## Overview

- **Total Conferences:** {total_notebooks}
- **Total Papers Analysed:** {total_papers:,}
- **Last Updated:** {datetime.utcnow().strftime("%Y-%m-%d")}

## What are Mind Maps?

Each mind map is an AI-generated hierarchical visualization showing the main themes and subtopics covered in a conference year. They provide:

- **Main Themes** - The 3-5 primary topic areas discussed
- **Subtopics** - Specific issues, methods, and case studies
- **Cross-year Analysis** - Track how priorities evolve over time

## FMA (Floodplain Management Australia)

Annual conferences on flood risk reduction, emergency management, and floodplain policy.

| Year | Title | Papers | Status |
|------|-------|--------|--------|
"""
    
    for data in sorted(fma_data, key=lambda x: x.get('year', 0), reverse=True):
        year = data.get('year', '')
        title = data.get('mind_map_title', '')
        sources = data.get('sources_count', 0)
        extracted = data.get('extracted', False)
        status = "✅ Available" if extracted else "⏳ Pending"
        link = f"[View](fma-{year}-mindmap.md)" if extracted else "Pending"
        
        md += f"| {year} | {title[:50]}{'...' if len(title) > 50 else ''} | {sources} | {link} |\n"
    
    md += f"""
## HWRS (Hydrology & Water Resources Society)

Biennial conferences on hydrological research and water resources management.

| Year | Papers | Status |
|------|--------|--------|
"""
    
    for data in sorted(hwrs_data, key=lambda x: x.get('year', 0), reverse=True):
        year = data.get('year', '')
        sources = data.get('sources_count', 0)
        extracted = data.get('extracted', False)
        status = "✅ Available" if extracted else "⏳ Pending"
        
        md += f"| {year} | {sources} | {status} |\n"
    
    md += f"""
---

## Raw Data

Access the underlying data in JSON format:
- [JSON Schema](https://github.com/lmillard79/aus_hydrology_compendium/blob/main/docs/data/conference-papers/schema.json)

---

## Data Source

All mind maps are generated from conference papers uploaded to [Google NotebookLM](https://notebooklm.google.com/). 

**Process:**
1. Upload PDF papers to NotebookLM
2. Generate mind map using AI analysis
3. Extract structured JSON data programmatically
4. Transform to compendium format
5. Build MkDocs pages

---

*Generated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}*
"""
    
    return md


def main():
    """Main entry point."""
    
    data_dir = Path("../docs/data/conference-papers")
    output_dir = Path("../docs/conference-papers")
    
    # Ensure directories exist
    data_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load all JSON files
    all_data = []
    json_files = sorted(data_dir.glob("*.json"))
    
    print(f"Found {len(json_files)} JSON files")
    
    for json_file in json_files:
        if json_file.name == "schema.json":
            continue
            
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data['extracted'] = True  # Mark as extracted since file exists
                all_data.append(data)
                
                # Generate individual mind map page
                md_content = generate_mindmap_markdown(data)
                
                conference = data.get('conference', 'unknown').lower()
                year = data.get('year', 'unknown')
                output_file = output_dir / f"{conference}-{year}-mindmap.md"
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                print(f"  Generated: {output_file.name}")
                
        except Exception as e:
            print(f"  Error processing {json_file}: {e}")
    
    # Generate index page
    if all_data:
        index_md = generate_index_markdown(all_data)
        index_file = output_dir / "index.md"
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_md)
        
        print(f"\nGenerated: {index_file.name}")
        print(f"Total notebooks processed: {len(all_data)}")
        print(f"Total papers: {sum(d.get('sources_count', 0) for d in all_data):,}")
    else:
        print("\nNo data files found to process")


if __name__ == '__main__':
    main()
