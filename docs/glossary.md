# Glossary

Plain-language definitions of terms used across this compendium. Where a term has a dedicated topic node, it is linked.

---

**AEP — Annual Exceedance Probability**
The probability that a flood of a given magnitude will be equalled or exceeded in any given year. A 1% AEP flood has a 1-in-100 chance of being equalled or exceeded in any year. Preferred in Australian practice over ARI for design flood specification. See ARR Book 1.

**ARI — Average Recurrence Interval**
The average time between flood events of a given magnitude. A 100-year ARI flood corresponds approximately to a 1% AEP flood. Now largely superseded by AEP in Australian practice but still encountered in older references and some regulatory contexts.

**ARR — Australian Rainfall and Runoff**
The national guideline for flood estimation in Australia, published by Engineers Australia and hosted at arr.ga.gov.au. The current edition (ARR 2019) replaced the 1987 edition and introduced substantial changes to design rainfall, frequency analysis, and temporal patterns. See [ARR node](arr/index.md).

**EY — Exceedances per Year**
A flood frequency descriptor used for more frequent events (e.g. 1 EY = the flood exceeded on average once per year). Used in ARR 2019 alongside AEP for the full frequency range.

**FLIKE**
A software package for at-site flood frequency analysis developed by the Cooperative Research Centre for Catchment Hydrology. Implements LP3 fitting using Bayesian inference, L-moments, and MLE, consistent with ARR Book 3. Now superseded by more recent implementations but widely referenced in the literature.

**GEV — Generalised Extreme Value distribution**
A three-parameter probability distribution encompassing the Gumbel, Fréchet, and Weibull distributions as special cases. Used in flood frequency analysis as an alternative to LP3. See [GEV](flood-frequency/gev.md).

**IFD — Intensity-Frequency-Duration**
Relationships between rainfall intensity, frequency (AEP), and duration used to construct design storms. Published for Australia by the Bureau of Meteorology. See [Design Rainfall](design-rainfall/index.md).

**LP3 — Log Pearson Type III distribution**
A three-parameter probability distribution applied to the logarithms of annual maximum flood data. The standard distribution recommended in ARR Book 3 for Australian at-site flood frequency analysis. See [LP3](flood-frequency/lp3.md).

**Non-stationarity**
The condition where the statistical properties of a flood record (mean, variance, distribution shape) change over time due to land use change, urbanisation, or climate variability and change. Challenges the assumption underlying standard frequency analysis. See [Non-stationarity](flood-frequency/non-stationarity.md).

**PILF — Potentially Influential Low Flows**
Annual maximum flood values that are anomalously low and may distort LP3 fitting if included without treatment. Identified using the Multiple Grubbs-Beck Test (MGBT) in ARR 2019 Book 3.

**PMF — Probable Maximum Flood**
The flood resulting from the PMP applied to a catchment. Used as the upper bound design event for high-consequence dams. See [Probable Maximum](probable-maximum/index.md).

**PMP — Probable Maximum Precipitation**
The theoretically greatest depth of precipitation for a given duration that is physically possible over a given storm area. Estimated using methods in the BoM Bulletin of the Australian Bureau of Meteorology. See [Probable Maximum](probable-maximum/index.md).

**TCEV — Two Component Extreme Value distribution**
A probability distribution that models flood series as a mixture of two populations — ordinary floods and extraordinary floods. Developed in Australia to handle the bimodal behaviour of flood records in some catchments. See [TCEV](flood-frequency/tcev.md).

---

*Add new terms via pull request. See [CONTRIBUTING.md](https://github.com/lmillard79/Aus_Hydrology_Compendium/blob/main/CONTRIBUTING.md).*
