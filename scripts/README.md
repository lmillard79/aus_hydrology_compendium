# NotebookLM Manager

Automated extraction of mind maps from Google NotebookLM for the Australian Hydrology Compendium.

## Features

- **Batch Extract Mind Maps**: Extract mind maps from all your NotebookLM notebooks
- **Create Notebooks from PDFs**: Upload folders of conference papers as new notebooks
- **Transform to JSON Schema**: Automatically format mind map data for the compendium
- **Configuration Management**: Track which notebooks have been extracted

## Prerequisites

```powershell
# Install notebooklm-py with browser support
pip install "notebooklm-py[browser]"

# Install Playwright browser for authentication
playwright install chromium
```

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

## Workflow

1. **First time setup**: `create-config` → `login` → edit config with IDs
2. **Daily extraction**: `extract-pending`
3. **New conference year**: `create` → edit config → `extract-pending`
4. **Regenerate all**: `extract --force`

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

## Notes

- Mind map generation takes 3-5 seconds per notebook
- Each notebook must have mind map generated in NotebookLM web UI first
- The script transforms NotebookLM's raw mind map JSON into the compendium schema
- All timestamps are in UTC
