#!/usr/bin/env python3
"""
Generate theme detail pages from extracted conference data.
Processes all years for FMA and HWRS conferences.
"""
import json
import os
from pathlib import Path

def slugify(text):
    """Convert theme name to URL-friendly slug."""
    return text.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace(',', '').replace('.', '')[:50]

def create_theme_page(conference, year, theme, output_dir):
    """Create a markdown page for a single theme."""
    theme_id = theme['id']
    theme_name = theme['theme']
    subtopics = theme.get('subtopics', [])
    content = theme.get('query_response', '')
    
    # Create filename from theme name
    filename = f"{slugify(theme_name)}.md"
    filepath = output_dir / filename
    
    # Build subtopics list
    subtopics_text = '\n'.join([f"- {s}" for s in subtopics]) if subtopics else "- (No subtopics listed)"
    
    # Create page content
    page_content = f"""# {theme_name}

**Conference:** {conference} {year}  
**Theme ID:** {theme_id}  
**NotebookLM ID:** `{theme.get('notebook_id', 'N/A')}`  

---

!!! note "Citation Note"
    Citations [1], [2], etc. refer to sources in the NotebookLM notebook. These are conference paper references that can be explored in the interactive notebook.

---

## Subtopics

{subtopics_text}

---

{content}

---

## Navigation

- [← Back to {conference} {year} Mind Map](../{conference.lower()}-{year}-mindmap.md)
- [Conference Papers Home](../index.md)
"""
    
    # Write file
    filepath.write_text(page_content, encoding='utf-8')
    return filename

def process_conference_year(conference, year, data_dir, output_base_dir):
    """Process all themes for a single conference year."""
    json_file = data_dir / f"{conference.lower()}_{year}_all_themes_detailed.json"
    
    if not json_file.exists():
        print(f"  Skipping {conference} {year} - no data file found")
        return []
    
    # Load data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    notebook_id = data.get('metadata', {}).get('notebook_id', 'N/A')
    themes = data.get('themes', [])
    
    if not themes:
        print(f"  Skipping {conference} {year} - no themes found")
        return []
    
    # Create output directory
    output_dir = output_base_dir / f"{conference.lower()}-{year}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"  Processing {conference} {year} ({len(themes)} themes)...")
    
    created_files = []
    for theme in themes:
        theme['notebook_id'] = notebook_id  # Add notebook ID to theme
        filename = create_theme_page(conference, year, theme, output_dir)
        created_files.append((theme['theme'], filename))
    
    return created_files

def main():
    """Main entry point."""
    base_dir = Path("e:/GitHub/Aus_Hydrology_Compendium")
    data_dir = base_dir / "docs/data/conference-papers"
    output_base_dir = base_dir / "docs/conference-papers"
    
    # FMA years to process (excluding 2024-2025 which are already done)
    fma_years = [2019, 2020, 2022, 2023]
    
    # HWRS years to process
    hwrs_years = [2005, 2011, 2012, 2014, 2015, 2016, 2018, 2021, 2022, 2023, 2024, 2025]
    
    print("Generating theme detail pages...")
    print()
    
    total_pages = 0
    
    # Process FMA years
    print("FMA Conference Papers:")
    for year in fma_years:
        files = process_conference_year("FMA", year, data_dir, output_base_dir)
        if files:
            print(f"    Created {len(files)} pages:")
            for theme_name, filename in files:
                print(f"      - {filename} ({theme_name})")
            total_pages += len(files)
    
    print()
    
    # Process HWRS years
    print("HWRS Conference Papers:")
    for year in hwrs_years:
        files = process_conference_year("HWRS", year, data_dir, output_base_dir)
        if files:
            print(f"    Created {len(files)} pages:")
            for theme_name, filename in files:
                print(f"      - {filename} ({theme_name})")
            total_pages += len(files)
    
    print()
    print(f"Total pages created: {total_pages}")
    print("Done!")

if __name__ == "__main__":
    main()
