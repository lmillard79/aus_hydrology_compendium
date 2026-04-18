# Contributing to the Australian Hydrology Compendium

Thank you for considering a contribution. This compendium grows through the collective knowledge of practitioners. Pull requests are welcome.

---

## What can be contributed

- Abstract summaries for references marked *[To be completed]*
- New landmark references following the template below
- Corrections to factual errors
- New topic nodes (discuss via Issue before starting)
- Glossary entries

## What cannot be contributed

- Full paper text (copyright)
- Invented citations or DOIs
- Paywalled content marked as open access
- AI-generated text published directly without practitioner review

---

## Page template

Every topic page follows this structure:

```markdown
# [Topic Name]

## What this is
One paragraph. Plain language. No jargon assumed.

## Why it matters in Australian practice
One paragraph. Real decisions, failure modes, consequences.

## Key concepts
Brief entries, 2–4 sentences each. Link to deeper pages where they exist.

## Landmark references

### [Author Year — Short title]
- **Source:** FMA / HWRS / ANCOLD / ARR / Journal name
- **Access:** Open / Paywalled / Contact author
- **Abstract summary:** 2–3 sentences on what this paper contributed and why it matters
- **Link:** [DOI or source URL if open]

## Unresolved questions
Honest plain-language list of where the field has not settled.

## Related topics
- [Link to adjacent node]
```

---

## Reference entry template

```markdown
### [Author(s) Year — Title]
- **Source:** [Journal / Conference / Publisher]
- **Access:** Open / Paywalled / [URL if open]
- **Abstract summary:** [2–3 sentences. Your own words. Do not reproduce abstract verbatim.]
- **Link:** [DOI or direct URL]
```

---

## Process

1. Fork the repository
2. Create a branch: `git checkout -b add-reference-kuczera1999`
3. Make changes following the templates above
4. Commit: `git commit -m "Add Kuczera 1999 LP3 reference"`
5. Push and open a Pull Request

For new topic nodes, open an Issue first to discuss scope and confirm it fits the compendium structure before writing content.

---

## Style guide

- Plain language — write as if for a capable engineer from another discipline
- British English spelling (Oxford Dictionary)
- No jargon without a [glossary](docs/glossary.md) entry or inline explanation
- Be specific about access status — do not guess
- Do not mark speculative or uncertain information as fact
