# Flood Frequency Analysis in Australia

## What this is

Flood frequency analysis is the process of estimating the probability that a flood of a given magnitude will occur. It answers the foundational question in flood engineering: how big is the 1% AEP flood at this location? The analysis fits a probability distribution to observed annual maximum flood data (or uses regional methods where records are short or absent) and reads off design flood estimates at nominated AEP levels.

In Australia, the standard at-site method is the Log Pearson Type III (LP3) distribution fitted to the annual maximum series, consistent with ARR 2019 Book 3. Regional methods, record extension techniques, continuous simulation, and historical/palaeoflood data are used to supplement or replace at-site analysis where records are inadequate.

## Why it matters in Australian practice

Design flood estimates underpin infrastructure sizing, floodplain mapping, development approvals, dam safety assessments, and insurance premium setting. Errors in frequency analysis propagate directly into decisions about bridge deck levels, levee heights, spillway capacity, and evacuation triggers. In dam safety, an incorrect frequency estimate can mean a spillway is undersized — with catastrophic consequences.

Australia's flood records are short (typically 20–80 years), highly variable, and drawn from a climate that produces extreme outlier events. This makes frequency analysis more uncertain here than in many other countries, and makes the choice of method, distribution, and record treatment more consequential.

## Key concepts

- **[LP3 distribution](lp3.md)** — The standard Australian method. Fitted using Bayesian inference via FLIKE or equivalent. Sensitive to outliers and record length.
- **[TCEV distribution](tcev.md)** — Two-population mixture model developed in Australia to handle catchments with distinct flood-generating mechanisms.
- **[GEV distribution](gev.md)** — Generalised Extreme Value; internationally common, used in ARR as a cross-check and in some regional analyses.
- **[Non-stationarity](non-stationarity.md)** — The challenge of applying stationary frequency models to records that may reflect a changing climate or land use.
- **Regional frequency analysis** — Pooling data from nearby catchments to estimate flood quantiles at ungauged or short-record sites. Covered in ARR Book 3.
- **[PILF treatment](../glossary.md#pilf--potentially-influential-low-flows)** — Identification and censoring of anomalously low annual maxima using the Multiple Grubbs-Beck Test.

## Landmark references

*See [References](references.md) for the full annotated list.*

Key works shaping Australian practice include Bulletin 17B/C methodology translations, the LP3 adoption in ARR 1987 and 2019, Kuczera's FLIKE development, and the TCEV literature from Rossi, Fiorentino, and Versace.

## Unresolved questions

- How much weight to give historical and palaeoflood information in extending short records
- Whether LP3 adequately captures the upper tail of Australian flood distributions
- How to account for non-stationarity in a regulatory framework designed around stationary return periods
- The appropriate treatment of zero flows and PILFs in arid and semi-arid catchments
- Regional versus at-site analysis — when is a short at-site record better than a regional estimate?

## Related topics

- [Design Rainfall](../design-rainfall/index.md)
- [ARR](../arr/index.md)
- [Dam Safety](../dam-safety/index.md)
- [Glossary](../glossary.md)
