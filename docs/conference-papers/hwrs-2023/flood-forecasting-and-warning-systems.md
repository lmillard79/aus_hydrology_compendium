# Flood Forecasting and Warning Systems

**Conference:** HWRS 2023 — HWRS 2023: Hydrological Modelling and Flood Management  
**Theme 1 of HWRS 2023**

---

## Overview

- FLASH System (RHDHV)
- Total Flood Warning System (TFWS)
- Rainfields/STEPS (BoM)

---

## Detailed Analysis

At HWRS 2023, the discourse around flood forecasting and warning systems emphasizes the urgent need for agile, advanced models to combat the increasing severity and variability of flooding driven by rapid urbanization and climate change [1]. The sources highlight a multi-tiered approach to flood warning, ranging from continental-scale enterprise systems to hyper-local, ultra-fast hydrodynamic models and the integration of artificial intelligence.

**National-Scale Forecasting and the Bureau of Meteorology (BoM)**
A central pillar in Australia's response is the **Bureau of Meteorology’s Hydrological Forecasting System (HyFS), one of the world's largest operational systems spanning an entire continent** [2]. Built on the highly configurable Delft-FEWS framework, HyFS processes real-time intelligence from over 8,000 rainfall and river gauges, alongside radar and storm surge data [2, 3]. HyFS integrates deterministic rainfall forecasts from multiple international models (including ACCESS, ECMWF, USGFS, and JMA) to produce multi-model ensembles that offer insight into the range of possible flooding from incoming weather systems [4]. The BoM is continually evolving this system to incorporate continuous hydrological modelling and probabilistic flood forecasting using the Short-Term Ensemble Prediction System (STEPS) [5]. 

For longer-term preparedness, the **BoM is integrating its Australian Water Outlook (AWO) and Seasonal Streamflow Forecasting (SSF) services**. By applying Bayesian Joint Probability (BJP) statistical models to AWO seasonal forecasts, the Bureau can generate automated, consistent streamflow forecasts up to three months in advance, reducing reliance on real-time observations while maintaining high forecast skill [6-8].

**Addressing the Flash Flood Gap with Ultra-Fast Modelling**
Because the BoM typically does not provide forecast services for rapid-response watersheds with a time of concentration under 6 hours, specialized Flood Information Systems (FIS) have emerged to fill the gap [9]. A prominent example is **FLASH, a cloud-based real-time forecasting system that combines state-of-the-art radar rainfall data with ultra-fast hydrodynamic modelling** (utilizing TUFLOW or 3Di) [10, 11]. By leveraging mathematical advancements like Quadtree meshing and Sub-Grid Sampling (SGS), FLASH substantially reduces traditional computational lag times, allowing for real-time prediction of inundation extents at a high resolution [12-14]. During the July 2022 Hunter Valley floods, FLASH successfully provided critical operational advice to government agencies regarding impending levee overtopping and highway closures [15, 16].

**Radar, Satellite Integration, and Nowcasting**
Traditional reliance on point-location rain gauges for hydrologic model calibration introduces significant spatial and temporal uncertainty [17, 18]. To address this, the industry is increasingly leveraging **radar-based rainfall products like the BoM's Rainfields3 to enhance flood warnings** [19]. Radar-based ensemble nowcasting provides updated rainfall forecasts every few minutes, offering a critical advantage over traditional Numerical Weather Prediction (NWP) models that only update every few hours [20, 21]. Furthermore, innovative blending methodologies are actively being developed to merge radar, Himawari satellite, and gauge data to overcome the inherent limitations and error variances of individual instruments [22-24].

**Pre-Calculated Map Libraries for Immediate Urban Response**
An alternative approach to computationally heavy live-modelling is demonstrated by **"City on Alert," a real-time monitoring system developed for Montpellier, France** [25]. Rather than running complex hydraulic models during an event, this system relies on a **risk matrix that links real-time sensor data (rainfall accumulation and water levels) to a pre-compiled library of flood hazard maps** [26, 27]. This allows forecasters to rapidly identify the most representative flooding scenario and coordinate immediate emergency responses, such as evacuations and road diversions, without waiting for active model computations [27, 28].

**Global Forecasts and Artificial Intelligence**
At a broader scale, global streamflow forecasts like the **Copernicus Emergency Management Services' GloFAS** (which provides 46-day lead times) are being evaluated for Australian catchments [29]. Because these NWP-forced models can suffer from spatial resolution limitations and precipitation biases, researchers are applying **wavelet-based post-processing and quantile mapping to substantially improve forecast skill and correct distributional biases** [30-32]. 

Furthermore, HWRS 2023 highlights a significant shift toward the use of **Artificial Neural Networks (ANN) and machine learning (such as Long Short-Term Memory - LSTM networks) for streamflow forecasting** [33-35]. These AI techniques excel at handling the highly non-linear nature of streamflow data by mapping complex relationships between weather parameters (rainfall, temperature, wind, snow depth) and antecedent streamflow [34, 36-38]. Studies show that multi-variate LSTM models incorporating both historical streamflow and weather data yield highly accurate predictions, equipping stakeholders with better tools for mitigating the disastrous impacts of future floods [38, 39].

---

**See Also:**
- [← HWRS 2023 Mind Map Overview](../hwrs-2023-mindmap.md)
- [Conference Papers Home](../index.md)
