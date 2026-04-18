# Generalised Extreme Value (GEV) Distribution

## What this is

The Generalised Extreme Value (GEV) distribution is a three-parameter family that unifies the three classical extreme value distributions — the Gumbel (Type I), Fréchet (Type II), and Weibull (Type III) — under a single parameterisation. The shape parameter ξ (xi) determines which type applies: ξ = 0 gives Gumbel, ξ > 0 gives Fréchet (heavy tail), ξ < 0 gives Weibull (bounded upper tail).

GEV is the internationally standard distribution for flood frequency analysis in many countries, particularly through the UK Flood Estimation Handbook (FEH) and the INDEX-FLOOD method. In Australia it is used as a cross-check and in regional analyses rather than as the primary at-site method.

## Why it matters in Australian practice

The GEV provides a useful alternative to LP3, particularly for regional frequency analysis and as a diagnostic tool. Where LP3 gives unexpected results (e.g. a physically implausible upper bound from a negative skew with a Weibull-type LP3), GEV provides an independent check.

L-moments — the preferred fitting method for GEV — are more robust to outliers than conventional moments, making GEV with L-moments an attractive option for short or skewed Australian records. ARR 2019 Book 3 notes GEV as an alternative distribution.

## Key concepts

**Shape parameter (ξ)**
The shape parameter controls tail behaviour. For Australian flood data, ξ is typically positive (heavy-tailed Fréchet type), meaning very large floods are possible with non-negligible probability. Estimating ξ reliably requires large samples; it is the primary source of uncertainty in GEV fitting.

**L-moments**
L-moments (probability-weighted moments) are the standard fitting method for GEV. They are more efficient than conventional moments for heavy-tailed distributions and are less sensitive to outliers. The L-moment ratio diagram is a useful diagnostic for distribution selection.

**GEV in regional analysis**
The INDEX-FLOOD method pairs GEV with L-moments for regional frequency analysis — pooling data from homogeneous regions to estimate the growth curve (shape and scale parameters), then scaling by the index flood (usually the median annual maximum). Used in the UK FEH and explored in Australian contexts.

**Gumbel as a special case**
The Gumbel distribution (ξ = 0, two parameters) was historically used in Australia before LP3 adoption. It is lighter-tailed than the GEV Fréchet case and tends to underestimate rare floods in many Australian catchments.

## Landmark references

<!-- TEMPLATE — populate from NotebookLM research -->

### [Hosking & Wallis 1997 — Regional Frequency Analysis: An Approach Based on L-moments]
- **Source:** Cambridge University Press
- **Access:** Paywalled (book)
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

### [Cunnane 1989 — Statistical distributions for flood frequency analysis]
- **Source:** WMO Operational Hydrology Report No. 33
- **Access:** Open (WMO)
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

### [Wallis, Matalas & Slack 1974 — Just a moment!]
- **Source:** Water Resources Research
- **Access:** Paywalled
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

## Unresolved questions

- Whether GEV or LP3 provides a better fit to Australian flood data across diverse climate regions
- How to estimate the GEV shape parameter reliably from short records (the fundamental challenge)
- Whether regional GEV analysis is feasible for Australian conditions given climate heterogeneity
- The appropriate use of GEV as a cross-check versus a primary method in practice

## Related topics

- [LP3](lp3.md) — the standard Australian at-site method
- [TCEV](tcev.md) — mixture distribution for bimodal populations
- [Non-stationarity](non-stationarity.md)
- [Flood Frequency Overview](index.md)
- [Glossary](../glossary.md)
