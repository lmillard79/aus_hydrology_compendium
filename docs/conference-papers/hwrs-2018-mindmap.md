# HWRS 2018 Mind Map

## HWRS 2018: Hydrology and Water Resources Symposium

**Conference:** Hydrology & Water Resources Society 2018  
**Sources:** 61 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
HWRS 2018: Hydrology and Water Resources Symposium
├── TUFLOW Solver Comparison
│   ├── TUFLOW Classic
│   │   ├── CPU-based
│   │   ├── Implicit finite difference
│   │   └── Fixed timestep
│   ├── TUFLOW HPC
│   │   ├── GPU-based (Heavily Parallelised Compute)
│   │   ├── Explicit finite volume
│   │   ├── Adaptive timestep
│   │   └── Significant run time reduction
│   └── Gowrie Creek Case Study
│       ├── Toowoomba, QLD
│       ├── January 2011 Flood Event
│       └── Roughness reduction in CBD
├── Flood Frequency Analysis (FFA)
│   ├── Brisbane River Catchment
│   │   ├── 26 stream gauging stations
│   │   ├── Probability distribution selection
│   │   ├── Log Pearson Type III (LP3) best fit
│   │   └── Generalised Pareto (GP) second fit
│   └── Methodology
│       ├── EasyFit software
│       ├── FLIKE software
│       └── Goodness-of-fit tests (K-S, A-D, C-S)
├── Urban On-Site Detention (OSD)
│   ├── ARR2016 Impact
│   │   ├── Revised IFD estimates
│   │   └── Ensemble temporal patterns
│   └── System Performance
│       ├── Reduced peak flow magnitudes
│       ├── Shorter critical durations
│       └── Original sizing remains adequate
├── Climate Change and WSUD
│   ├── Performance Trends
│   │   ├── Efficiency generally reduced
│   │   ├── Wetlands may improve with PET increase
│   │   └── Bioretention/Infiltration basins sensitive
│   └── Modelling
│       ├── MUSIC software
│       ├── 6-minute rainfall time series
│       └── Flow duration curve scaling
├── Hydrologic Reconstructions
│   ├── Dendrochronology
│   │   ├── Tree ring growth analysis
│   │   ├── Pre-instrumental data extension
│   │   └── Lake Burbury (Tasmania) 1000-year study
│   └── Alternate wood properties
│       ├── Latewood density
│       ├── Blue light intensity
│       ├── Stable isotopes
│       └── Cell wall thickness
├── Water Data and Management
│   ├── Real Time Data Delivery
│   │   ├── DELWP Victoria WMIS
│   │   ├── Cloud hosting (AWS)
│   │   └── Telemetry expansion
│   └── Multi-variable Simulation
│       ├── SWAT model
│       ├── Soil moisture + Streamflow calibration
│       └── Improved water budget partitioning
├── Flood Impact Assessments
│   ├── Acceptable Impact Criteria
│   │   ├── Peak level increase (Afflux)
│   │   ├── Duration of flooding
│   │   └── Hydraulic hazard and velocity
│   └── Land Use Sensitivity
│       ├── Residential: 10-50mm
│       ├── Industrial/Commercial: 50-150mm
│       └── Agriculture: 150-400mm
└── Farm Dam Trends
    └── Victoria 2000-2015
        ├── Stable growth since 2010 (0.3%/year)
        ├── Higher growth 2000-2006 (1.4%/year)
        └── Manual digitisation from aerial imagery
```

---

## Main Themes

### 1. [TUFLOW Solver Comparison](hwrs-2018/tuflow-solver-comparison.md)
- TUFLOW Classic
- TUFLOW HPC
- Gowrie Creek Case Study

### 2. [Flood Frequency Analysis (FFA)](hwrs-2018/flood-frequency-analysis-ffa.md)
- Brisbane River Catchment
- Methodology

### 3. [Urban On-Site Detention (OSD)](hwrs-2018/urban-on-site-detention-osd.md)
- ARR2016 Impact
- System Performance

### 4. [Climate Change and WSUD](hwrs-2018/climate-change-and-wsud.md)
- Performance Trends
- Modelling

### 5. [Hydrologic Reconstructions](hwrs-2018/hydrologic-reconstructions.md)
- Dendrochronology
- Alternate wood properties

### 6. [Water Data and Management](hwrs-2018/water-data-and-management.md)
- Real Time Data Delivery
- Multi-variable Simulation

### 7. [Flood Impact Assessments](hwrs-2018/flood-impact-assessments.md)
- Acceptable Impact Criteria
- Land Use Sensitivity

### 8. [Farm Dam Trends](hwrs-2018/farm-dam-trends.md)
- Victoria 2000-2015

---

## Theme Detail Pages

- [TUFLOW Solver Comparison](hwrs-2018/tuflow-solver-comparison.md)
- [Flood Frequency Analysis (FFA)](hwrs-2018/flood-frequency-analysis-ffa.md)
- [Urban On-Site Detention (OSD)](hwrs-2018/urban-on-site-detention-osd.md)
- [Climate Change and WSUD](hwrs-2018/climate-change-and-wsud.md)
- [Hydrologic Reconstructions](hwrs-2018/hydrologic-reconstructions.md)
- [Water Data and Management](hwrs-2018/water-data-and-management.md)
- [Flood Impact Assessments](hwrs-2018/flood-impact-assessments.md)
- [Farm Dam Trends](hwrs-2018/farm-dam-trends.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
Here are the key practical recommendations and actionable insights for floodplain managers, hydrologists, and water resources professionals, drawn from the HWRS 2018 symposium themes:

### 1. Flood Modelling and Hydraulic Analysis
*   **Verify TUFLOW HPC models against TUFLOW Classic:** While the Heavily Parallelised Compute (HPC) solver can reduce run times by up to 85%, its adaptive timestepping can mask modelling instabilities by continually reducing the timestep until stable. Practitioners should **run a few initial setups in Classic as a precautionary check** to identify and fix parameterization issues before relying fully on HPC [1-3]. 
*   **Adjust hydraulic roughness for complex areas in HPC:** When shifting from Classic to HPC, consider **reducing the Manning's *n* roughness values by 20% in complex urban areas (e.g., CBD commercial zones)** to achieve a more accurate match with established Classic model calibrations [4, 5].
*   **Select representative hydrographs carefully for 2D models:** When transitioning from a hydrologic Monte Carlo simulation to a computationally heavy 2D hydraulic model, hydrographs that are probability-neutral for upstream peaks may severely skew downstream volumes. To avoid biased water levels, **select representative hydrographs based on peak flow, but constrain the choice to the most dominant temporal pattern** found in the nearest probability-neutral hydrologic runs [6-8].
*   **Use 2D modelling for high-flow rating curves:** Traditional extrapolation of stream gauge rating curves becomes highly uncertain during large floods due to complex floodplain breakouts. **Develop synthetic rating curves using 2D hydrodynamic models**, and specifically **extract the stage-discharge relationship from the rising limb of the flood** as it provides a better representation of flood volumes for emergency management and warnings [9-11].

### 2. Flood Frequency Analysis (FFA)
*   **Supplement short gauge records with paleoflood data:** Traditional gauge records are often too short to capture extreme climatic variability. Incorporating paleoflood data (such as slackwater deposits) can **reduce 90% confidence limits for extreme events by up to 90%** (e.g., the 1% AEP event) [12-14]. Ensure, however, that paleoflood data is only applied if historical climatic and land conditions reflect modern regimes [14, 15].
*   **Adopt the Log Pearson Type III (LP3) distribution for at-site FFA:** When evaluating distributions for Australian catchments, **the LP3 distribution is highly recommended** as it frequently provides the best fit and most accurate design flood estimates [16-18].
*   **Use ordinary kriging for ungauged catchments:** For Regional Flood Frequency Analysis (RFFA), **ordinary kriging is a highly effective spatial interpolation technique** that considers spatial correlation, often outperforming the standard ARR2016 RFFE Model for estimating design floods at ungauged sites [19-21].

### 3. Urban Drainage, OSD, and WSUD
*   **Use the mean ensemble result for OSD compliance, but check the worst-case for safety:** When assessing On-Site Detention (OSD) performance under ARR2016 temporal pattern ensembles, **adopt the mean ensemble result to assess peak flow mitigation** [22-24]. However, you should **apply the worst-case ensemble result as a sensitivity check for critical safety elements**, such as storage freeboard and overflow behavior [24, 25]. Notably, OSD systems originally sized under ARR1987 generally still perform adequately under ARR2016 [26, 27].
*   **Incorporate safety margins into WSUD device sizing:** Future climate change (reduced rainfall, higher potential evapotranspiration) is expected to marginally reduce the pollutant removal efficiencies (TSS, TN, TP) of Water Sensitive Urban Design (WSUD) devices, particularly infiltration and bioretention basins. Designers must **incorporate small efficiency margins during the design phase** to ensure devices meet environmental compliance targets under future climate conditions [28-31].

### 4. Flood Impact Assessments and Floodplain Management
*   **Apply standardised, land-use-specific acceptable impact criteria:** Rather than arbitrarily enforcing a "no impact" rule, authorities should adopt tiered thresholds. For example: **10mm or less for residential properties** [32, 33]; **15-50mm for transport and public infrastructure** [33]; and **up to 50-70mm for agricultural and open space land**, provided escape routes are not compromised [34, 35].
*   **Assess impacts beyond the 1% AEP peak level:** Do not fixate solely on the 1% AEP peak level. **Evaluate impacts across a probability range** (e.g., 50% to 20% AEP for agricultural areas), and assess secondary impacts such as the duration of inundation, loss of warning time, and temporary construction-phase risks [36-38].
*   **Define floodways based on flow conveyance (~80% of flow):** Identifying floodways using purely 1D encroachment tools or arbitrary velocity-depth (VxD) thresholds is flawed. Instead, **use an iterative 2D approach that identifies the extent of the floodplain required to carry approximately 80% of the total flow** during a 1% AEP event. This correlates well with acceptable encroachment rules (<100mm upstream afflux) [39-41].
*   **Impose a finite design life on mine closure hydraulic structures:** Do not assume that permanent diversions or levees protecting post-closure mine pit voids will be maintenance-free indefinitely. Regulators and designers must **adopt a finite design life and assess landforms against a long-term sequence of successive smaller flood events**, which are more likely to cause scouring, piping, and eventual creek capture than a single extreme design event [42-44].

### 5. Managing Farm Dams and Low Flows
*   **Install bypass/release devices on farm dams:** The proliferation of farm dams significantly intercepts critical low flows required for downstream ecological health. Practitioners must **retro-fit low-flow bypass or release devices based on topography** (e.g., gravity bypasses where gradient allows) to return natural flows to ephemeral catchments. Ensure these devices are simple and require minimal ongoing maintenance [45-48].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes in the HWRS 2018 notebook are deeply interconnected, united by the overarching goal of managing hydrologic risk and uncertainty in a changing environment. The cross-cutting issues primarily revolve around dealing with the non-stationarity of climate, addressing the limitations of short historical data records, and navigating the computational challenges brought on by the new Australian Rainfall and Runoff 2016 (ARR2016) guidelines. 

Here is how these themes connect and the specific papers that bridge them:

**1. Managing Uncertainty: Hydrologic Reconstructions, Climate Change, and Flood Frequency Analysis (FFA)**
A major interdisciplinary connection is the need to understand extreme events and long-term water availability when historical gauge records are too short to accurately represent natural climate variability or the return periods of extreme events [1, 2]. To bridge this gap, researchers use **Hydrologic Reconstructions** to inform **FFA** and **Water Management**.
*   **Specific Example:** A paper on paleoflood hydrology demonstrates how analyzing slackwater deposits can extend the timeline of extreme flood events by over 1,000 years beyond the current gauge record [3-5]. This directly connects Hydrologic Reconstructions to FFA, helping to reduce uncertainty bounds for extreme flood estimates and understand if recent floods are statistical outliers [5, 6].
*   **Specific Example:** Another study uses dendrochronology (tree rings) to reconstruct a 1,000-year summer inflow record for Lake Burbury in Tasmania [1, 7]. This reconstructs pre-instrumental data to test the performance of hydro-electric water supply systems, bridging Hydrologic Reconstructions with Climate Change resilience and Water Management [7-9].

**2. Integrating ARR2016: FFA, TUFLOW Modelling, and Urban OSD**
The release of ARR2016 introduced significant methodological shifts, moving away from single "Design Events" to "Ensemble" and "Monte Carlo" frameworks that use multiple temporal patterns [10-12]. This creates a cross-cutting challenge: simulating these massive new data requirements without exceeding computational limits.
*   **Specific Example (FFA to TUFLOW):** A paper bridges FFA and TUFLOW by testing how to select computationally frugal "representative floods" from a vast Monte Carlo hydrologic set for use in 2D TUFLOW hydraulic models [10, 12, 13]. The study finds that hydrographs which appear "probability neutral" for upstream peak flows can yield widely biased, non-neutral downstream water levels in a 2D model [13, 14]. 
*   **Specific Example (FFA to Urban OSD):** Another paper explores the transition to ARR2016 temporal pattern ensembles to assess the mitigation performance of existing **Urban On-Site Detention (OSD)** systems [15, 16]. By running models with both ARR1987 and ARR2016 inputs, the authors found that OSD systems designed under older FFA methods generally still mitigate peak flow increases adequately under the new ensemble approach [17-19].

**3. Catchment Modification: Farm Dam Trends, Water Management, and Environmental Flows**
The proliferation of farm dams significantly alters natural flow regimes, cutting across the themes of Farm Dam Trends, Water Data, and environmental health. 
*   **Specific Example:** One study maps the growth in **Farm Dam Trends** across Victoria using spatial datasets from 2000 to 2015 [20]. The findings highlight that the total storage capacity of farm dams increased rapidly (driven by property subdivision and climate variability) and severely impacts streamflows [20, 21]. 
*   **Specific Example:** Connecting Farm Dams directly to **Water Data and Management**, another paper details a trial project in the Mount Lofty Ranges that installed low-flow bypass devices on existing farm dams [22-24]. This project utilizes telemetered monitoring to see if restoring these regular, small flow events can improve the health of water-dependent ecosystems without comprising the landholders' water security [25-27].

**4. Climate Change and Water Sensitive Urban Design (WSUD)**
As cities adapt to higher temperatures and altered rainfall patterns, the intersection of **Climate Change** and **WSUD** focuses on whether current green infrastructure can handle future extremes.
*   **Specific Example:** A study specifically bridges these two themes by applying future Global Climate Model (GCM) predictions to assess the long-term performance of WSUD treatment devices (like wetlands, swales, and bioretention basins) [28, 29]. By scaling historical rainfall records to reflect climate change scenarios for the years 2040 and 2065, the researchers found that WSUD pollutant removal performance is generally reduced under future conditions [30-32]. 

**5. Advanced Computational Tools: TUFLOW Solver Comparison and Flood Impact Assessments**
The ability to properly conduct **Flood Impact Assessments** relies heavily on the computational efficiency and accuracy of 2D hydraulic software like TUFLOW. 
*   **Specific Example:** A paper compares the traditional TUFLOW Classic solver against the new Heavily Parallelised Compute (HPC) solver using a 1D/2D model of Toowoomba [33, 34]. The study found that using the HPC solver with GPU technology reduced model run times by up to 85% while maintaining comparable accuracy in flood extents and depths [35-37]. This advancement directly enhances the industry's capacity to conduct widespread Flood Impact Assessments efficiently [35]. Another paper evaluates what constitutes an "acceptable impact" (e.g., changes in peak levels or duration of flooding) when using 2D models for Flood Impact Assessments across various land uses [38-40].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
**Flood Frequency Analysis (FFA) and Hydrologic Modelling**
*   **Peaks-over-Threshold (POT) methods are under-researched in Australia** for FFA, and future studies must extend POT analysis to more probability distributions and catchments to generalize findings [1-3]. 
*   Further research is needed to determine **why the Log Pearson III (LP3) distribution provides better fits** for annual maximum flood series in specific areas like the Brisbane River catchment [4, 5].
*   There is ongoing research into **applying kriging for Regional Flood Frequency Analysis (RFFA)** using comprehensive databases to present further developments [6].
*   Under the ARR2016 guidelines, **there is a lack of clear direction on how to treat ensemble results for Urban On-Site Detention (OSD) designs** [7, 8], and there is an identified gap in guidance on **how to select "probability neutral" representative hydrographs** for computationally heavy 2D hydraulic models [9, 10].
*   The ARR2016 Monte Carlo approach performed poorly in the Mount Lofty Ranges, indicating a need for **much more investigation before Monte Carlo can be reliably used in this region**, or determining if more complex models are necessary [11-13]. A standardized approach for baseflow separation is also required [14].
*   To estimate extreme rainfalls using Australian Water Availability Project (AWAP) data, ongoing research must address the **heterogeneity of coastal zones and inconsistencies in bias correction** [15-18].
*   Further investigation into temporal patterns is required, including testing the **variability of Huff curves with respect to gauge location** and their applicability in design event modelling [19, 20].

**Climate Change, WSUD, and Environmental Flows**
*   Further research is recommended to **evaluate climate change effects on catchment pollutant export rates, runoff parameters, and pollutant removal parameters** for Water Sensitive Urban Design (WSUD) devices [21].
*   Predicting climate change impacts on streamflows involves significant uncertainty, requiring **refined methodologies to accurately assess long-term environmental flow compliance** [22, 23]. 
*   Future research must also **quantify the effects of increasing potential evapotranspiration** as temperatures continue to rise [24].
*   There is scope to expand urban OSD research by examining ARR2016 climate change guidance, assessing pit-and-pipe networks, and analyzing overland flow paths and major hydraulic structures [25, 26].

**Hydrologic Reconstructions (Paleofloods and Tree Rings)**
*   For tree-ring hydrologic reconstructions, future methodological improvements include **using stochastic approaches to sample daily rainfall events outside the instrumental record** and developing winter/spring reconstructions to constrain resampling techniques [27].
*   Paleoflood analysis faces limitations regarding the **accuracy of Optically Stimulated Luminescence (OSL) dating** [28] and the scaling of discharges from slackwater deposit reaches to dams, requiring additional analysis for integration into current design hydrology [29].

**Catchment Modelling, Irrigation, and Water Quality**
*   For spatio-temporal water quality modelling, future improvements should explore **non-linear statistical structures, threshold-type models for low concentrations, and the incorporation of temporal land management data** (e.g., tillage, fertilizer application) [30-32].
*   **Quantifying microbial source pathways**, particularly from diffuse sources at a catchment-scale, remains a key modelling challenge [33, 34].
*   Vineyard irrigation is currently not accurately simulated; future work will test more sites, utilize new gridded evapotranspiration products, and use **pre-determined crop coefficient (Kc) relationships** to improve remote sensing monitoring [35, 36].
*   To improve multi-variable hydrological simulations (like SWAT), future studies should incorporate **remote sensing soil moisture datasets (e.g., SMOS, SMAP) and remotely sensed evapotranspiration data** [37].

**Infrastructure, Farm Dams, and Water Management**
*   The **long-term performance of unmaintained watercourses adjacent to permanent mine pit voids is largely untested** [38]. Regulators need to adopt consistent design lives and account for long-term risks like soil piping, differential settlement, and sedimentation/erosion [39, 40].
*   Ongoing monitoring is highly recommended to track the **changing number and storage capacity of farm dams** across Victoria, the Murray-Darling Basin, and other catchments [41, 42].
*   **Water accounting methodologies for complex, multi-user systems are still not universally available** and require further development [43], along with economic and hydrological modelling capabilities to support water sharing arrangements [44].
*   Robustness testing of optimal water operating plans requires future **sensitivity analysis to identify uncertain factors causing performance failures**, alongside exploring new objective functions for operational efficiency [45, 46].
*   There is an identified need to further **investigate the impacts of water tariffs on low-income households** and refine systems analyses for altered governance structures [47, 48].
---

**See Also:**
- [Conference Papers Home](index.md)
