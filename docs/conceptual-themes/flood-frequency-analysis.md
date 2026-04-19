# Flood Frequency Analysis

**Type:** Methodology Collection  
**Notebook ID:** `YOUR_FFA_NOTEBOOK_ID_HERE`  
**Status:** Pending extraction

---

## Overview

This conceptual notebook aggregates flood frequency analysis (FFA) papers from across FMA and HWRS conferences. Unlike conference-specific collections, this notebook is **topic-centric** - bringing together all papers that discuss FFA methods regardless of when or where they were presented.

---

## Why a Conceptual Notebook?

Traditional conference organization separates related research:
- FFA papers from FMA 2024 appear in "Coastal Dynamics"
- FFA papers from HWRS 2023 appear in "Hydraulic Modelling"
- FFA papers from FMA 2019 appear in "Emergency Management"

This conceptual collection reunites them to show:
- **Method evolution** across time
- **Cross-conference consensus** on best practices
- **Technique comparison** (Gumbel vs. GEV vs. Bayesian)
- **Regional approaches** across Australia

---

## Expected Content

Once extracted from NotebookLM, this page will include:

### Mind Map Themes
- [ ] Design Flood Estimation Methods (DFE, DFA, DFF, DIF, AEP)
- [ ] Statistical Distributions (Gumbel, GEV, Log-Pearson III)
- [ ] Regional Flood Frequency Analysis
- [ ] Climate Change Non-Stationarity
- [ ] Uncertainty Quantification
- [ ] At-Site vs. Regional Analysis

### Cross-Conference Timeline
| Year | Conference | Key FFA Papers | Themes |
|------|------------|----------------|--------|
| 2025 | FMA | TBD | Climate adaptation |
| 2024 | FMA | TBD | Coastal flood risk |
| 2023 | HWRS | TBD | Design flood methods |
| ... | ... | ... | ... |

---

## Links to Conference Papers

This conceptual theme connects to:
- [FMA 2024 - Coastal Dynamics](../conference-papers/fma-2024-mindmap.md)
- [HWRS 2023 - Design Flood Methods](../conference-papers/hwrs-2023-mindmap.md)
- [FMA 2019 - Emergency Management](../conference-papers/fma-2019-mindmap.md)

---

## Source Mapping

Once extracted, this section will map papers from this conceptual notebook back to their conference origins:

```json
{
  "cross_references": [
    {
      "paper_title": "Example FFA Paper",
      "appears_in_conferences": ["FMA 2024", "HWRS 2023"],
      "conceptual_themes": ["Flood Frequency Analysis"],
      "method": "GEV Distribution"
    }
  ]
}
```

---

## Setup Required

To activate this notebook:

1. **Update Config**: Add your FFA notebook ID to `scripts/notebooks_config.json`:
   ```json
   {
     "id": "your-actual-notebook-id",
     "name": "Flood Frequency Analysis",
     "type": "methodology",
     "extracted": false
   }
   ```

2. **Extract Mind Map**:
   ```bash
   python scripts/notebooklm_manager.py extract-pending
   ```

3. **Query Themes**:
   ```bash
   python scripts/notebooklm_manager.py query-all-themes \
     --json-file docs/data/conference-papers/conceptual_ffa.json \
     --notebook-id your-actual-notebook-id
   ```

---

## Data Structure

Extracted data will be saved as:
- `docs/data/conference-papers/conceptual_ffa.json` (mind map structure)
- `docs/data/conference-papers/conceptual_ffa_theme_*.txt` (theme details)
- `docs/data/conference-papers/conceptual_ffa_bibliography.txt` (paper listing)

---

← [Back to Cross-Cutting Themes Overview](index.md)
