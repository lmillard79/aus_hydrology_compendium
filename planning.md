# Hydrology Knowledge Compendium — Agent Handoff Document

## Project Overview

Build a searchable, Wikipedia-style knowledge compendium for Australian flood hydrology and water resources engineering. The site is a **navigable index of abstracts and summaries** that points back to primary sources. It does not reproduce copyrighted content. It makes the knowledge landscape discoverable.

Target audience: hydrologists, water resources engineers, flood practitioners, dam safety engineers, planners, and students — in Australia and internationally.

---

## What This Is (and Is Not)

**It is:**
- A curated, annotated index of abstracts and key findings
- A navigable mind map of how topics and papers connect
- A plain-language orientation layer for practitioners entering a topic area
- An open, community-extendable knowledge graph

**It is not:**
- A repository of full papers (copyright issue)
- A replacement for primary sources
- A static document — it should grow over time

---

## Technical Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| Static site generator | MkDocs with Material theme | Python-native, clean search built in, easy to maintain |
| Hosting | GitHub Pages | Free, permanent, globally accessible, open to community contribution |
| Content format | Markdown files | Plain text, version controlled, human readable |
| Search | MkDocs built-in search | No backend required, works at static site level |
| Graph visualisation | Optional: D3.js or Quartz overlay | Visual mind map of topic connections |

---

## Repository Structure

```
hydrology-compendium/
│
├── docs/
│   ├── index.md                    # Home page — what this is, how to navigate
│   ├── about.md                    # Project rationale, contributing guidelines
│   │
│   ├── flood-frequency/
│   │   ├── index.md                # Topic overview
│   │   ├── lp3.md                  # Log Pearson III method
│   │   ├── tcev.md                 # Two Component Extreme Value
│   │   ├── gev.md                  # Generalised Extreme Value
│   │   ├── non-stationarity.md     # Non-stationarity in flood records
│   │   └── references.md           # Annotated reference list for this node
│   │
│   ├── design-rainfall/
│   │   ├── index.md
│   │   ├── ifd-curves.md
│   │   ├── areal-reduction.md
│   │   ├── temporal-patterns.md
│   │   └── references.md
│   │
│   ├── probable-maximum/
│   │   ├── index.md
│   │   ├── pmp-methods.md
│   │   ├── pmf-application.md
│   │   ├── pmf-misapplication.md   # Links to HWRS 2026 paper when published
│   │   └── references.md
│   │
│   ├── dam-safety/
│   │   ├── index.md
│   │   ├── ancold-guidance.md
│   │   ├── consequence-categories.md
│   │   └── references.md
│   │
│   ├── arr/                        # Australian Rainfall and Runoff
│   │   ├── index.md
│   │   ├── book3-flood-frequency.md
│   │   ├── arr-evolution.md
│   │   └── references.md
│   │
│   ├── open-data/
│   │   ├── index.md
│   │   ├── bom-data.md
│   │   ├── arr-datahub.md
│   │   └── references.md
│   │
│   └── glossary.md                 # Plain-language definitions
│
├── mkdocs.yml                      # Site configuration
├── README.md                       # GitHub-facing project description
└── CONTRIBUTING.md                 # How others can add to this
```

---

## Page Template (Every Node Follows This)

```markdown
# [Topic Name]

## What this is
One paragraph. Plain language. No jargon assumed. 
What is this method or concept, in terms a capable engineer 
from another discipline could understand.

## Why it matters in Australian practice
One paragraph. Connect to real decisions — dam design, 
flood planning, infrastructure investment. 
What goes wrong if this is misunderstood or misapplied.

## Key concepts
Brief entries, 2-4 sentences each. Link to deeper pages 
where they exist within the compendium.

## Landmark references

### [Author Year — Short title]
- **Source:** FMA / HWRS / ANCOLD / ARR / Journal
- **Access:** Open / Paywalled / Contact author
- **Abstract summary:** 2-3 sentences on what this paper 
  contributed and why it matters
- **Link:** [DOI or source URL if open]

### [Repeat for each key reference]

## Unresolved questions
Honest plain-language list of where the field has not 
settled. What practitioners disagree about. 
What the evidence does not yet resolve.

## Related topics
- [Link to adjacent node]
- [Link to adjacent node]
```

---

## MkDocs Configuration (mkdocs.yml)

```yaml
site_name: Australian Hydrology Compendium
site_description: A searchable index of flood hydrology and water resources knowledge
site_url: https://[username].github.io/hydrology-compendium

theme:
  name: material
  palette:
    primary: blue grey
    accent: teal
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - search.suggest
    - search.highlight
    - toc.integrate

plugins:
  - search
  - tags

markdown_extensions:
  - toc:
      permalink: true
  - admonition
  - tables

nav:
  - Home: index.md
  - Flood Frequency Analysis:
    - Overview: flood-frequency/index.md
    - LP3: flood-frequency/lp3.md
    - TCEV: flood-frequency/tcev.md
    - GEV: flood-frequency/gev.md
    - Non-stationarity: flood-frequency/non-stationarity.md
    - References: flood-frequency/references.md
  - Design Rainfall:
    - Overview: design-rainfall/index.md
  - Probable Maximum:
    - Overview: probable-maximum/index.md
  - Dam Safety:
    - Overview: dam-safety/index.md
  - ARR:
    - Overview: arr/index.md
  - Open Data:
    - Overview: open-data/index.md
  - Glossary: glossary.md
  - About: about.md
```

---

## README.md Content (for GitHub)

```markdown
# Australian Hydrology Compendium

A searchable, open index of Australian flood hydrology and 
water resources knowledge.

This is not a paper repository. It is a navigation layer — 
annotated abstracts, plain-language summaries, and a map of 
how ideas connect — pointing back to primary sources in FMA, 
HWRS, ANCOLD, ARR, and the peer-reviewed literature.

## Why this exists

The cumulative knowledge base of Australian hydrology is 
scattered, siloed, and hard to navigate. Practitioners 
reinvent solutions because they cannot find prior work. 
This compendium aims to make the knowledge graph visible 
and searchable.

## Contributing

See CONTRIBUTING.md. Pull requests welcome.

## Scope

Current nodes: flood frequency analysis, design rainfall, 
PMF methods, dam safety, ARR, open data sources.

## Built with

MkDocs + Material theme, hosted on GitHub Pages.
```

---

## Build and Deploy Commands

```bash
# Install dependencies
pip install mkdocs mkdocs-material

# Serve locally for development
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

---

## Phase 1 Scope (First Node Only)

**Topic:** Flood Frequency Analysis in Australia

Complete the following pages before moving to any other topic:

1. `flood-frequency/index.md` — orientation and overview
2. `flood-frequency/lp3.md` — LP3 method, Australian context, FLIKE
3. `flood-frequency/tcev.md` — TCEV, when it applies, key papers
4. `flood-frequency/non-stationarity.md` — unresolved tensions, current research
5. `flood-frequency/references.md` — annotated reference list

Do not expand to other nodes until Phase 1 is published and working.

---

## Content Sourcing Workflow

1. Feed papers into NotebookLM by topic node
2. Use NotebookLM to identify main arguments, chronological development, unresolved questions
3. Use NotebookLM output as research scaffold only — do not publish directly
4. Write each page in plain language using the template above
5. Verify access status for each reference (open / paywalled)
6. Commit to GitHub, deploy via mkdocs gh-deploy

---

## Key Source Organisations

| Organisation | Description | Notes |
|-------------|-------------|-------|
| FMA | Floodplain Management Australia conference proceedings | Partially open |
| HWRS | Hydrology and Water Resources Symposium proceedings | Partially open |
| ANCOLD | Australian National Committee on Large Dams | Guidance documents, some open |
| ARR | Australian Rainfall and Runoff (Engineers Australia) | Book chapters open at arr.ga.gov.au |
| BoM | Bureau of Meteorology | Data and technical reports, mostly open |
| Geoscience Australia | ARR datahub, national datasets | Mostly open |

---

## What the Agent Should NOT Do

- Do not reproduce full paper text (copyright)
- Do not invent citations or DOIs
- Do not mark paywalled content as open
- Do not expand scope beyond Phase 1 until instructed
- Do not use a database or backend — static files only
- Do not add complexity before the basic pipeline works

---

## Definition of Done for Phase 1

- [ ] GitHub repository created and public
- [ ] MkDocs installed and serving locally
- [ ] GitHub Pages deployment working
- [ ] Five flood frequency pages complete using template
- [ ] Search working across all pages
- [ ] At least ten annotated references in flood-frequency/references.md
- [ ] README accurately describes the project