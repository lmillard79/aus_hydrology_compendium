# Australian Hydrology Compendium

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deployed-blue)](https://lmillard79.github.io/aus-hydrology-compendium)
[![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/Lamilla79/aus_hydrology_compendium)

A searchable, open index of Australian flood hydrology and water resources knowledge.

This is **not** a paper repository. It is a navigation layer — annotated abstracts, plain-language summaries, and a map of how ideas connect — pointing back to primary sources in FMA, HWRS, ANCOLD, ARR, and the peer-reviewed literature.

## Why this exists

The cumulative knowledge base of Australian hydrology is scattered, siloed, and hard to navigate. Practitioners reinvent solutions because they cannot find prior work. This compendium aims to make the knowledge graph visible and searchable.

## Scope

Current Phase 1 node: **Flood Frequency Analysis** (LP3, TCEV, GEV, non-stationarity, references).

Planned Phase 2 nodes: design rainfall, PMF methods, dam safety, ARR, open data sources.

## Built with

[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), hosted on Hugging Face Spaces.

## Running locally

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Building

```bash
mkdocs build
```

Output goes to `site/`. This is what gets deployed to Hugging Face Spaces.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests welcome.

## Author

Lindsay Millard — Principal Hydrologist & Chartered Engineer (RPEQ, CEng MICE, CPEng, FIEAust).  
[LinkedIn](https://www.linkedin.com/in/lindsaymillard) · [GitHub](https://github.com/lmillard79)
