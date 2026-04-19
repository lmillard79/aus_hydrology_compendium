# Rainfall Disaggregation Vietnam

**Conference:** HWRS 2014 — Hydrology and Water Resources Symposium 2014  
**Theme 4 of HWRS 2014**

---

## Overview

- Method of Fragments

---

## Detailed Analysis

At the Hydrology and Water Resources Symposium 2014, research presented by Phuong Cu Thi and James E. Ball addressed the critical challenge of acquiring high-resolution rainfall data for flood simulation in the **Ba River basin** in central Vietnam [1-3]. 

Accurate rainfall-runoff and flood modeling requires sub-daily (hourly) continuous rainfall data to properly capture the temporal distribution of storms [4, 5]. However, in many Asian countries like Vietnam, continuously recording rain gauges are scarce, and hydrologists must rely predominantly on daily-read gauges [2, 5]. Within the Ba River basin, for instance, there are over 26 long-term rainfall stations, but only 12 provide the hourly data necessary for reliable simulation [6]. 

To overcome this limitation, the researchers utilized the **Method of Fragments (MoF)** to disaggregate daily rainfall records into hourly intervals [2, 5]. MoF is a non-parametric technique that relies on conditionally resampling historical hourly rainfall patterns (the "fragments") from continuous gauges to proportionally distribute the daily rainfall totals at non-recording gauges [7]. While MoF has been successfully utilized in Australia, this study was particularly significant as it evaluated the method's effectiveness in a **tropical monsoon climate**, which is characterized by extreme wet and dry seasons and heavy rainfall influenced by tropical cyclones [6, 8, 9].

To implement the MoF effectively and accurately reflect the basin's hydrology, the researchers took the following approaches:
*   **Evaluating Station Similarity:** Nearby continuous stations were selected to act as donor sites based on their statistical similarity to the target daily-read stations. This similarity was rigorously evaluated using daily metrics (like maximum wet/dry spells and seasonal rainfall) and sub-daily metrics (like maximum intensity timing and fraction of zero-rainfall periods) [10, 11].
*   **Overcoming Pattern Repetition:** A primary limitation of the MoF is that relying on a small dataset can lead to artificial repetition, producing cyclic patterns in the simulated rainfall [12]. The researchers mitigated this by pooling fragment datasets from multiple nearby stations, granting the model more diverse options for disaggregating the large rainfall events that drive floods [12].
*   **Addressing Seasonal Variations:** To account for the extreme intra-annual shifts of a monsoon climate, fragment selection utilized a 15-day moving window centered on the target calendar day [13, 14]. Furthermore, historical daily data was segregated into four specific continuity classes based on whether the preceding and subsequent days were wet or dry [13]. 

The disaggregation model was validated by comparing the statistical characteristics of the simulated 1-hour, 3-hour, and 5-hour annual rainfall maxima against observed data at the An Khe and Son Hoa stations [15, 16]. The study found that the simulated data fell within the 5% and 95% confidence limits of the historical frequency curves, indicating that errors remained within an acceptable range [15, 17]. 

Ultimately, the symposium presentation concluded that the Method of Fragments is a simple yet robust tool for generating sub-daily extreme rainfall sequences in monsoonal environments [16]. By combining abundant daily records with the limited available pluviograph data, hydrologists can significantly improve the temporal resolution of rainfall data required for reliable catchment and flood modeling [16].

---

**See Also:**
- [← HWRS 2014 Mind Map Overview](../hwrs-2014-mindmap.md)
- [Conference Papers Home](../index.md)
