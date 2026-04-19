# Flood Frequency Analysis (FFA)

**Conference:** HWRS 2018 — HWRS 2018: Hydrology and Water Resources Symposium  
**Theme 2 of HWRS 2018**

---

## Overview

- Brisbane River Catchment
- Methodology

---

## Detailed Analysis

Flood Frequency Analysis (FFA) is an established statistical technique used to estimate the magnitude and frequency of flood events by fitting a probability distribution to recorded streamflow data [1-3]. Accurate FFA is essential for designing flood infrastructure and minimizing direct and indirect flood damages [4, 5]. At the HWRS 2018 (Hydrology and Water Resources Symposium), several papers explored methods to refine FFA, address its limitations, and apply it to both gauged and ungauged catchments across Australia.

**Optimizing Probability Distributions and Data Sampling**
A critical challenge in FFA is selecting the most appropriate probability distribution, as an incorrect choice can lead to significant biases in design flood estimates [6]. A study focusing on the Brisbane River Catchment evaluated five parametric distributions and found that the **Log Pearson Type III (LP3) distribution provided the best fit for the annual maximum (AM) flood series** at most stream gauging stations [7-9]. Another study in New South Wales compared the traditional Annual Maximum Series (AMS) sampling method against the Peaks-over-Threshold (POT) method. The research demonstrated that the **Peaks-over-Threshold (POT) model offers more accurate design flood estimates for frequent floods (smaller average recurrence intervals)**, whereas the AMS method (particularly using a logistics distribution) fitted better for larger, less frequent floods [10-13].

**Addressing Short Instrumental Records with Paleofloods and Hydraulic Modeling**
A major limitation of FFA is the short length of systematic gauge records (averaging only 42 years in eastern Australia), which introduces massive uncertainty when extrapolating estimates for rare and extreme events [14-16]. To combat this, **supplementing historical records with paleoflood data can extend the flood timeline by thousands of years and substantially narrow the confidence limits for extreme flood estimates** [17-19]. For example, incorporating just four paleoflood events into the FFA for the Callide Dam resulted in a 42% reduction in the 1% Annual Exceedance Probability (AEP) peak inflow estimate and significantly reduced the 90% confidence limits [20, 21]. Furthermore, improving the accuracy of extreme flow measurements through 2D hydrodynamic modeling for high-stage rating curves provides a more reliable foundation for updating FFA and verifying design flood peak flows [22-24].

**Regional Flood Frequency Analysis (RFFA) for Ungauged Catchments**
For catchments with little or no gauge data, RFFA is utilized to transfer flow statistics from gauged to ungauged sites [25, 26]. One HWRS 2018 paper proposed the use of **Ordinary Kriging, a geostatistical interpolation method, to provide unbiased estimations for RFFA** in Victoria [27, 28]. The kriging approach was shown to yield satisfactory relative error ranges (36% to 39%) and performed competitively against the benchmark RFFE Model 2016 recommended by Australian Rainfall and Runoff (ARR) [29-31].

**Urban Flood Frequency Estimation**
Because rural RFFE procedures do not seamlessly translate to urban catchments, researchers formulated a **preliminary Regional Urban Flood Frequency Estimation (RUFFE) method** [32-34]. This rapid assessment technique relies on specific urban parameters, including catchment area, total and effective imperviousness, and rainfall Intensity-Frequency-Duration (IFD) data [35]. Initial testing of the RUFFE method showed strong agreement with peak flows derived from traditional FFA in gauged urban catchments, providing a promising tool for future urban flood planning [34, 36].

---

**See Also:**
- [← HWRS 2018 Mind Map Overview](../hwrs-2018-mindmap.md)
- [Conference Papers Home](../index.md)
