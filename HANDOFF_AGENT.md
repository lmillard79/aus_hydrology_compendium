# Handoff: Conference Papers to Website Conversion

## Project Overview
**Goal**: Build a searchable, indexed website of flood hydrology knowledge from Australian conference proceedings (FMA & HWRS).

**Concept**: "Mind Map of Mind Maps" - A global index that aggregates themes and sources across multiple conferences and years, allowing practitioners to search and discover relevant papers by topic rather than just by conference/year.

## What We Have Now

### 1. Data Structure

**Location**: `docs/data/conference-papers/`

**Files**:
- `fma_YYYY.json` - Extracted mind map data for each FMA conference
- `hwrs_YYYY.json` - Extracted mind map data for each HWRS conference  
- `fma_YYYY_theme_XX_theme-X.txt` - Detailed theme summaries (from NotebookLM queries)
- `fma_YYYY_all_themes_detailed.json` - Aggregated data with all theme responses
- `schema.json` - JSON schema defining the data structure

### 2. JSON Structure (fma_YYYY.json)

```json
{
  "notebook": "FMA_2024",
  "year": 2024,
  "conference": "FMA",
  "sources_count": 118,
  "mind_map_title": "Flood Management and Research 2024",
  "main_themes": [
    {
      "id": "theme-1",
      "theme": "Infragravity Waves in Coastal Creeks",
      "description": "",
      "subtopics": ["Background", "Low Cost Gauges", "Observed Data Analysis", "Conclusions"],
      "key_papers": []
    }
  ],
  "generated_date": "2026-04-18T11:57:41.251123Z",
  "notebooklm_url": "https://notebooklm.google.com/notebook/..."
}
```

### 3. Theme Summary Files (*.txt)

These contain **rich, AI-generated summaries** with:
- Full thematic analysis (2-5 paragraphs)
- Embedded citations like [1], [2], [3]
- Practical insights for practitioners
- Links to source papers (when available)

**Example content**: See `docs/data/conference-papers/fma_2024_theme_01_theme-1.txt`

## What Needs to Be Built

### 1. Website Structure (MkDocs)

**Framework**: MkDocs with Material theme (already configured in `mkdocs.yml`)

**Current nav structure**:
```yaml
nav:
  - Conference Papers:
    - Overview: conference-papers/index.md
    - FMA 2024: conference-papers/fma-2024-mindmap.md
    - FMA 2023: conference-papers/fma-2023-mindmap.md
    ...
```

### 2. Key Pages to Generate

#### A. Conference Year Pages (e.g., `fma-2024-mindmap.md`)
- Display mind map title and themes
- Link to individual theme detail pages
- Show source count
- Link back to NotebookLM notebook

#### B. Theme Detail Pages (NEW)
- **Full theme summary** from .txt files
- **Subtopics** with descriptions
- **Key papers** (when available)
- **Related themes** from other years (cross-linking)

#### C. Global Topic Index (NEW - The "Mind Map of Mind Maps")
**This is the killer feature!**

A page that aggregates themes ACROSS all conferences:
- **Topic**: "Infragravity Waves"
  - FMA 2024: "Infragravity Waves in Coastal Creeks" [link]
  - FMA 2023: "Coastal Dynamics" [link]
  - HWRS 2022: "Wave Modelling" [link]

- **Topic**: "Flood Damage Assessment"
  - FMA 2024: "2023 DT01 Flood Damage Tool" [link]
  - HWRS 2023: "Economic Analysis Methods" [link]

**How to build this**: 
1. Extract all `theme` values from all JSON files
2. Normalize/cluster similar themes (fuzzy matching)
3. Group by topic category
4. Generate cross-reference links

#### D. Source/Paper Index (NEW)

A searchable index of all papers mentioned:
- Paper title
- Authors (when available)
- Year
- Conference source
- Themes it appears in
- Link to conference notebook

### 3. Data Processing Pipeline

**Input**: `docs/data/conference-papers/*.json` + `*.txt`

**Processing Steps**:
1. **Load all JSON files**
   - Parse each conference year's data
   - Extract themes, subtopics, metadata

2. **Load theme summaries**
   - Match .txt files to their corresponding JSON themes
   - Extract citations using regex: `\[(\d+)\]` or author patterns

3. **Build global index**
   - Create topic clusters across years
   - Cross-reference similar themes
   - Build paper citation index

4. **Generate Markdown**
   - One page per conference year
   - One page per theme (optional)
   - Global topic index page
   - Paper bibliography page

5. **Update mkdocs.yml nav**
   - Auto-generate navigation structure

## Technical Implementation

### Existing Scripts

**`scripts/generate_markdown.py`**
- Currently generates basic conference pages
- **Extend this** or create `generate_enhanced_site.py`

### New Script Requirements

**`generate_global_index.py`**:
```python
# 1. Load all conference data
conferences = load_all_json('docs/data/conference-papers/*.json')

# 2. Build topic clusters
topics = cluster_themes_by_similarity(conferences)

# 3. Generate global index page
generate_topic_index_page(topics, 'docs/conference-papers/topic-index.md')

# 4. Generate enhanced conference pages
for conf in conferences:
    generate_enhanced_conference_page(conf)

# 5. Update mkdocs nav
update_mkdocs_yaml(nav_structure)
```

## Key Challenges & Solutions

### 1. Theme Normalization
**Problem**: Same topic appears with different names:
- "Infragravity Waves in Coastal Creeks" (FMA 2024)
- "Coastal Wave Dynamics" (HWRS 2023)
- "Surf Beat Phenomena" (FMA 2022)

**Solution**: Use fuzzy string matching (difflib.SequenceMatcher or rapidfuzz) to cluster similar themes.

### 2. Citation Extraction
**Problem**: Citations in summaries are `[1]`, `[2]` format - need to map to actual paper titles.

**Solution**: 
- Extract citation numbers from summaries
- Cross-reference with NotebookLM source lists (if available)
- Build paper metadata from citations

### 3. Search Functionality
**Problem**: Users need to find papers by topic across years.

**Solution**: 
- MkDocs Material has built-in search
- Ensure all theme names and summaries are in searchable markdown
- Add tags/categories to frontmatter

## Expected Output

### File Structure
```
docs/
├── conference-papers/
│   ├── index.md                    # Overview with links to all years
│   ├── topic-index.md              # NEW: Global topic cross-reference
│   ├── paper-bibliography.md       # NEW: All papers indexed
│   ├── fma-2024-mindmap.md         # Enhanced with theme links
│   ├── fma-2024/
│   │   ├── theme-01-infragravity-waves.md    # NEW: Full summary
│   │   ├── theme-02-damage-tool.md
│   │   └── theme-03-emergency-resources.md
│   ├── fma-2023/
│   │   └── ...
│   └── hwrs-2024/
│       └── ...
```

### MkDocs Nav Structure
```yaml
nav:
  - Home: index.md
  - Conference Papers:
    - Overview: conference-papers/index.md
    - Topic Index: conference-papers/topic-index.md
    - Paper Bibliography: conference-papers/paper-bibliography.md
    - FMA 2024: conference-papers/fma-2024-mindmap.md
    - FMA 2023: conference-papers/fma-2023-mindmap.md
    ...
```

## Success Criteria

1. ✅ All conference years have dedicated pages
2. ✅ Each theme has a detail page with full summary
3. ✅ Topic index shows related themes across years
4. ✅ Search works across all content
5. ✅ Paper bibliography lists all sources with links
6. ✅ Site deploys to GitHub Pages successfully

## Data Files to Reference

| File | Purpose |
|------|---------|
| `fma_2024.json` | Theme structure for FMA 2024 |
| `fma_2024_theme_01_theme-1.txt` | Detailed summary for Theme 1 |
| `fma_2024_all_themes_detailed.json` | Aggregated data with responses |
| `notebooks_config.json` | Notebook IDs and metadata |
| `schema.json` | JSON schema definition |

## Next Steps

1. Create `generate_global_index.py` script
2. Implement theme clustering/normalization
3. Generate enhanced markdown pages
4. Build topic index page
5. Build paper bibliography page
6. Update mkdocs.yml navigation
7. Test locally with `mkdocs serve`
8. Deploy to GitHub Pages

## Questions?

- Check existing `scripts/generate_markdown.py` for reference
- See `docs/data/conference-papers/` for sample data
- MkDocs Material docs: https://squidfunk.github.io/mkdocs-material/

---
**Context**: This project is being built for the FMA 2026 conference on the Gold Coast (this week!). The goal is to have a searchable compendium of flood hydrology knowledge that practitioners can use to discover relevant papers across all Australian conference proceedings.
