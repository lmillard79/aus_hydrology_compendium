# NotebookLM Manager

Automated extraction of mind maps from Google NotebookLM for the Australian Hydrology Compendium.

**Estimated Time:** 20-25 minutes for full extraction and integration

## Features

- **Batch Extract Mind Maps**: Extract mind maps from all your NotebookLM notebooks
- **Create Notebooks from PDFs**: Upload folders of conference papers as new notebooks
- **Transform to JSON Schema**: Automatically format mind map data for the compendium
- **Configuration Management**: Track which notebooks have been extracted

## Prerequisites

```powershell
# Install all dependencies
cd scripts
pip install -r requirements.txt
playwright install chromium
```

**Requirements:**
- Python 3.10-3.14
- Google account with NotebookLM access
- 200MB disk space for browser

## Quick Start

### 1. Create Configuration File

```powershell
cd scripts
python notebooklm_manager.py create-config
```

This creates `notebooks_config.json` with all your conference years.

### 2. Authenticate with NotebookLM

```powershell
notebooklm login
```

This opens a browser to authenticate with your Google account.

### 3. Get Your Notebook IDs

```powershell
python notebooklm_manager.py list
```

Copy the notebook IDs from the output and paste them into `notebooks_config.json`, replacing the `PLACEHOLDER` values.

### 4. Extract Mind Maps

Extract all pending (not yet extracted) notebooks:

```powershell
python notebooklm_manager.py extract-pending
```

Or extract all notebooks (including already extracted):

```powershell
python notebooklm_manager.py extract --force
```

## Creating New Notebooks from PDFs

If you have a folder of PDFs for a conference year:

```powershell
python notebooklm_manager.py create `
  --name "FMA 2025" `
  --pdf-folder "E:\\ConferencePapers\\FMA_2025" `
  --description "Floodplain Management Australia 2025 Conference Papers"
```

Then add the new notebook ID to `notebooks_config.json` and extract the mind map.

## Configuration File Format

```json
{
  "notebooks": [
    {
      "id": "58b99d93-4101-4e11-93d6-a377158f5a18",
      "year": 2024,
      "conference": "FMA",
      "sources_count": 118,
      "extracted": true,
      "mind_map_title": "Flood Risk Management: Coastal Dynamics..."
    }
  ],
  "hwrs_notebooks": [...],
  "metadata": {
    "total_fma_papers": 565,
    "total_hwrs_papers": 1473
  }
}
```

## Output Files

Extracted mind maps are saved to:
- `docs/data/conference-papers/fma_YYYY.json`
- `docs/data/conference-papers/hwrs_YYYY.json`

These JSON files follow the schema defined in `docs/data/conference-papers/schema.json`.

## Commands

| Command | Description |
|---------|-------------|
| `create-config` | Create sample configuration file |
| `list` | List all accessible notebooks |
| `create` | Create new notebook from PDF folder |
| `extract` | Extract mind maps from config |
| `extract-pending` | Extract only non-extracted notebooks |

## Complete Workflow

### Phase 1: First Time Setup (10 minutes)

```powershell
# 1. Create config file
python notebooklm_manager.py create-config

# 2. Login to NotebookLM (opens browser)
notebooklm login

# 3. List your notebooks to get IDs
python notebooklm_manager.py list

# 4. Edit scripts/notebooks_config.json
#    - Replace PLACEHOLDER values with actual notebook IDs
#    - Copy IDs from the list command output
```

### Phase 2: Batch Extraction (5 minutes)

```powershell
# Extract all pending notebooks
python notebooklm_manager.py extract-pending

# This creates:
#   - docs/data/conference-papers/fma_YYYY.json
#   - docs/data/conference-papers/hwrs_YYYY.json
```

### Phase 3: Generate Markdown (2 minutes)

```powershell
# Generate/update all conference papers markdown pages
python generate_markdown.py

# This updates:
#   - docs/conference-papers/index.md (overview table)
#   - docs/conference-papers/fma-YYYY-mindmap.md (individual pages)
```

### Phase 4: Build & Deploy (5 minutes)

```powershell
cd ..

# Test locally
venv\Scripts\mkdocs serve

# Build site
venv\Scripts\mkdocs build

# Push to trigger deployment
git add -A
git commit -m "Add extracted mind maps from NotebookLM"
git push origin main
```

## Alternative: Create New Notebook from PDFs

If you have conference papers as PDFs:

```powershell
# 1. Create notebook from PDF folder
python notebooklm_manager.py create `
  --name "FMA 2025" `
  --pdf-folder "E:\\ConferencePapers\\FMA_2025" `
  --description "Floodplain Management Australia 2025 Conference Papers"

# 2. Wait for upload to complete in NotebookLM web UI
# 3. Generate mind map in web UI
# 4. Get the new notebook ID
python notebooklm_manager.py list

# 5. Add to config and extract
python notebooklm_manager.py extract-pending
```

## Troubleshooting

### Authentication Issues

If you get auth errors:
```powershell
notebooklm login
# Or for Edge browser users:
notebooklm login --browser msedge
```

### Check Auth Status

```powershell
notebooklm auth check --test
```

### PDF Upload Fails

Ensure PDFs are:
- Not password protected
- Under 200MB per file
- Standard academic paper format

## Integration with Compendium

After extracting mind maps, rebuild the site:

```powershell
mkdocs build
mkdocs serve
```

The extracted JSON will automatically be used by the conference papers pages.

## Troubleshooting

### "Authentication fails"
```powershell
# Clear and re-authenticate
notebooklm login
# Or force re-auth: notebooklm login --force
```

### "NotebookLM API not responding"
The notebooklm-py library uses undocumented Google APIs. Check:
- [GitHub issues](https://github.com/teng-lin/notebooklm-py/issues) for latest status
- Your Google account has NotebookLM access at notebooklm.google.com

### "Rate limiting / Too many requests"
The script has built-in rate limiting. If you hit limits:
- Wait 60 seconds between runs
- Use `extract-pending` instead of `extract --force`

## Notes

- Mind map generation takes 3-5 seconds per notebook
- Each notebook must have mind map generated in NotebookLM web UI first
- The script transforms NotebookLM's raw mind map JSON into the compendium schema
- All timestamps are in UTC
- Config file tracks extraction state to avoid duplicate work
- Progress is logged to console; check for ✓ (success) or ✗ (error) markers
