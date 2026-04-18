# Non-stationarity in Flood Records

## What this is

Standard flood frequency analysis assumes that the statistical properties of a flood record — the mean, variance, and distribution shape — are constant over time (stationarity). Non-stationarity is the condition where this assumption fails: where flood magnitudes or frequencies are changing systematically due to land use change, urbanisation, reservoir regulation, or shifts in climate driven by natural variability (ENSO, IPO) or anthropogenic climate change.

Non-stationarity is not new — hydrologists have long recognised that catchments change. What has intensified the debate is the question of whether anthropogenic climate change has already introduced trends into flood records significant enough to invalidate standard frequency analysis for design purposes.

## Why it matters in Australian practice

If flood records are non-stationary, then fitting a stationary distribution to them conflates different underlying populations. A 1% AEP estimate derived from a stationary LP3 fit to a record with an upward trend in flood peaks will underestimate current and future flood risk. Conversely, a dataset influenced by high ENSO variability may exhibit apparent trends that are not persistent.

This matters acutely for long-lived infrastructure — dams, bridges, major culverts — where the design is intended to perform across a 50–100 year asset life under potentially non-stationary conditions. It also matters for regulatory frameworks that define design floods using fixed AEP language, which implicitly assumes stationarity.

## Key concepts

**Sources of non-stationarity**

- *Land use change* — urbanisation increases runoff volumes and peak flows; deforestation changes catchment response time
- *Reservoir regulation* — dams alter the downstream flood frequency distribution; upstream regulation changes contributing area hydrology
- *ENSO and IPO variability* — Australian flood records are strongly modulated by El Niño–Southern Oscillation and the Interdecadal Pacific Oscillation, producing multi-decadal wet and dry periods that can appear as trends in short records
- *Anthropogenic climate change* — projected changes in rainfall intensity, seasonality, and antecedent moisture conditions may alter flood frequency distributions over the asset life of infrastructure

**Testing for non-stationarity**
Standard tests include the Mann-Kendall trend test, Pettitt change-point test, and Spearman's rank correlation. However, these tests have low power for short Australian records and high natural variability. A statistically significant trend does not necessarily indicate a physically meaningful permanent shift.

**Non-stationary frequency analysis methods**
Several approaches have been proposed:

- *Covariate-based models* — fitting LP3 or GEV parameters as functions of time or a physical covariate (e.g. ENSO index, catchment imperviousness)
- *Continuous simulation* — using rainfall-runoff models driven by projected climate data to generate synthetic flood records under future conditions
- *Scenario-based design* — presenting a range of flood estimates corresponding to different climate scenarios rather than a single design value

**The stationarity debate**
Milly et al. (2008) argued in *Science* that "stationarity is dead" — that anthropogenic climate change has rendered the stationarity assumption invalid for water resources design. This generated substantial debate. Australian researchers have been active in characterising the limits of non-stationary methods for practical application.

## Landmark references

<!-- TEMPLATE — populate from NotebookLM research -->

### [Milly et al. 2008 — Stationarity is dead: whither water management?]
- **Source:** Science, Vol. 319
- **Access:** Paywalled (AAAS)
- **Abstract summary:** *[To be completed]*
- **Link:** https://doi.org/10.1126/science.1151915

### [Serinaldi & Kilsby 2015 — Stationarity is undead: uncertainty dominates the distribution of extremes]
- **Source:** Advances in Water Resources
- **Access:** Paywalled (Elsevier)
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

### [Ishak et al. 2013 — Evaluating the non-stationarity of Australian annual maximum flood]
- **Source:** Journal of Hydrology
- **Access:** Paywalled (Elsevier)
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

### [Franks & Kuczera 2002 — Flood frequency analysis: Evidence and implications of secular climate variability, New South Wales]
- **Source:** Water Resources Research
- **Access:** Paywalled (AGU)
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

## Unresolved questions

- Whether anthropogenic climate change has already produced detectable non-stationarity in Australian flood records beyond natural ENSO/IPO variability
- How to distinguish persistent trends from multi-decadal natural variability in records shorter than 100 years
- Whether non-stationary frequency analysis methods produce more reliable design estimates or simply propagate larger uncertainty
- How regulatory frameworks should incorporate non-stationarity — what AEP means for a non-stationary system
- The appropriate design horizon for infrastructure under uncertain non-stationarity

## Related topics

- [LP3](lp3.md) — stationary frequency analysis
- [Design Rainfall](../design-rainfall/index.md) — climate change in IFD context
- [ARR](../arr/index.md)
- [Flood Frequency Overview](index.md)
- [Glossary](../glossary.md)
