# Log Pearson Type III (LP3)

## What this is

The Log Pearson Type III (LP3) distribution is a three-parameter probability distribution applied to the logarithms of annual maximum flood data. It is defined by a mean, standard deviation, and skewness coefficient. The skewness parameter is critical — it controls the shape of the upper tail, which determines the magnitude of rare design floods (1% AEP, 0.1% AEP).

In Australia, LP3 is the standard distribution for at-site flood frequency analysis, consistent with ARR 2019 Book 3. It is the same distribution recommended in the US Bulletin 17C (formerly 17B) guidelines, which heavily influenced Australian practice.

## Why it matters in Australian practice

The LP3 distribution is the starting point for almost every design flood estimate derived from gauged streamflow data in Australia. Dam spillway sizing, floodplain mapping studies, bridge hydraulics, and development assessments all typically begin here. The choice of fitting method — and particularly how outliers, zero flows, and [PILFs](../glossary.md#pilf--potentially-influential-low-flows) are handled — can shift the 1% AEP estimate by 30–50% at sites with short or variable records.

Australia's short, skewed, and often outlier-contaminated flood records make LP3 fitting more sensitive to method choice than in catchments with long, well-behaved records.

## Key concepts

**Fitting methods**
ARR 2019 Book 3 recommends Bayesian fitting as the primary method, with L-moments and MLE as alternatives. Bayesian fitting (as implemented in FLIKE and pyextremes ARR2019_Book3 fork) incorporates prior information on the skewness parameter, which stabilises estimates at short-record sites.

**PILF identification**
The Multiple Grubbs-Beck Test (MGBT) identifies annual maximum values that are anomalously low and likely drawn from a different population (e.g. dry-year flows rather than true flood events). PILFs are censored (treated as below a threshold) rather than deleted. Incorrect PILF treatment can significantly bias the fitted distribution.

**Record length sensitivity**
At-site LP3 estimates are unreliable for AEPs much rarer than approximately 5× the record length. A 30-year record should be treated with caution for estimates rarer than 1% AEP. Regional frequency analysis, historical data, and continuous simulation are tools to address this limitation.

**Generalised skewness**
Where at-site skewness is poorly estimated (short records), ARR recommends weighting the at-site skew with a regional (generalised) skew estimate. Regionalisation of skewness is a significant source of uncertainty.

## Landmark references

<!-- TEMPLATE — populate from NotebookLM research -->

### [Kuczera 1999 — Comprehensive at-site flood frequency analysis using Monte Carlo Bayesian inference]
- **Source:** Water Resources Research
- **Access:** Paywalled (Wiley)
- **Abstract summary:** *[To be completed]*
- **Link:** [DOI to be added]

### [Ball et al. 2019 — ARR Book 3: Peak flow estimation]
- **Source:** Australian Rainfall and Runoff, Engineers Australia
- **Access:** Open — arr.ga.gov.au
- **Abstract summary:** *[To be completed]*
- **Link:** https://arr.ga.gov.au/

### [England et al. 2019 — Bulletin 17C: Guidelines for determining flood flow frequency]
- **Source:** USGS Techniques and Methods
- **Access:** Open
- **Abstract summary:** *[To be completed]*
- **Link:** https://doi.org/10.3133/tm4B5

### [Haddad & Rahman 2011 — Regional flood frequency analysis in eastern Australia]
- **Source:** *[Journal to be confirmed]*
- **Access:** *[To be confirmed]*
- **Abstract summary:** *[To be completed]*
- **Link:** *[To be added]*

## Unresolved questions

- Whether the generalised skewness map in ARR 2019 is adequately regionalised for Australian conditions
- The appropriate prior distribution for Bayesian LP3 fitting in highly skewed catchments
- How to handle mixed populations (e.g. tropical vs. frontal events) that may not conform to a single LP3
- The extent to which short Australian records can reliably resolve the upper tail of the LP3

## Related topics

- [TCEV](tcev.md) — alternative to LP3 for bimodal flood populations
- [GEV](gev.md) — international alternative distribution
- [Non-stationarity](non-stationarity.md) — challenges to stationary LP3 assumption
- [Flood Frequency Overview](index.md)
- [Glossary](../glossary.md)
