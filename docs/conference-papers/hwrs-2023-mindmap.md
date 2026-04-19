# HWRS 2023 Mind Map

## HWRS 2023: Hydrological Modelling and Flood Management

**Conference:** Hydrology & Water Resources Society 2023  
**Sources:** 135 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
HWRS 2023: Hydrological Modelling and Flood Management
├── Flood Forecasting and Warning Systems
│   ├── FLASH System (RHDHV)
│   │   ├── Cloud-based Architecture
│   │   ├── Ultra-fast Hydrodynamic Modelling
│   │   ├── Lizard Data Platform
│   │   └── Real-time Dashboards
│   ├── Total Flood Warning System (TFWS)
│   │   ├── Monitoring and Prediction
│   │   ├── Interpretation
│   │   ├── Message Construction
│   │   ├── Communication
│   │   └── Community Response
│   └── Rainfields/STEPS (BoM)
├── Hydrological Modelling Techniques
│   ├── Calibration and Optimization
│   │   ├── AutoCal Surrogate Modelling
│   │   ├── Resampling (Over-sampling/KGE-OS)
│   │   └── Metaheuristic Algorithms (NSGA-II, PSO)
│   ├── Infiltration and Losses
│   │   ├── SCS Curve Number (SCS-CN)
│   │   ├── Green-Ampt Multi-layer Soil Model
│   │   └── Initial/Continuing Loss Model
│   └── Direct Rainfall (Rain-on-Grid)
│       ├── TUFLOW SGS & Quadtree
│       ├── 3Di Cloud Modelling
│       └── DEM Pre-treatment
├── Case Studies and Extreme Events
│   ├── Fitzroy River (WA) 2023
│   │   ├── Ex-Tropical Cyclone Ellie
│   │   ├── Bridge Failure at Fitzroy Crossing
│   │   └── Dynamic Bed Rating Curves
│   ├── Narracan Dam (VIC)
│   │   ├── Gated Spillway Operations
│   │   ├── Upstream Impact Assessment
│   │   └── Becks Bridge Road Inundation
│   ├── Dry Creek (SA)
│   │   ├── Channel Morphology Changes
│   │   ├── Urbanisation Impacts
│   │   └── Sinuosity and Deposition
│   ├── Warrah Creek (NSW)
│   └── Hunter Valley Flood Scheme
└── Climate and Future Trends
    ├── Rainfall Anomaly Prediction (WASP/HLC)
    ├── Cybernetic Water Systems
    ├── Serious Gaming for Education
    └── Immersive Environments (AR/VR)
```

---

## Main Themes

### 1. [Flood Forecasting and Warning Systems](hwrs-2023/flood-forecasting-and-warning-systems.md)
- FLASH System (RHDHV)
- Total Flood Warning System (TFWS)
- Rainfields/STEPS (BoM)

### 2. [Hydrological Modelling Techniques](hwrs-2023/hydrological-modelling-techniques.md)
- Calibration and Optimization
- Infiltration and Losses
- Direct Rainfall (Rain-on-Grid)

### 3. [Case Studies and Extreme Events](hwrs-2023/case-studies-and-extreme-events.md)
- Fitzroy River (WA) 2023
- Narracan Dam (VIC)
- Dry Creek (SA)
- Warrah Creek (NSW)

### 4. [Climate and Future Trends](hwrs-2023/climate-and-future-trends.md)
- Rainfall Anomaly Prediction (WASP/HLC)
- Cybernetic Water Systems
- Serious Gaming for Education
- Immersive Environments (AR/VR)

---

## Theme Detail Pages

- [Flood Forecasting and Warning Systems](hwrs-2023/flood-forecasting-and-warning-systems.md)
- [Hydrological Modelling Techniques](hwrs-2023/hydrological-modelling-techniques.md)
- [Case Studies and Extreme Events](hwrs-2023/case-studies-and-extreme-events.md)
- [Climate and Future Trends](hwrs-2023/climate-and-future-trends.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
**Flood Forecasting and Warning Systems**

*   **Integrate radar-based nowcasts with traditional forecasting:** For rapid-response catchments, practitioners should supplement Numerical Weather Prediction (NWP) models with radar-based ensemble nowcasts [1, 2]. These provide high-resolution updates every few minutes, enabling much more accurate tracking of spatial and temporal rainfall evolution during flash flood events [3-5]. Blending radar, satellite, and rain gauge data overcomes the spatial limitations of relying on point-source gauges alone [6-8].
*   **Adopt ultra-fast, cloud-based hydrodynamic modelling:** Implement real-time, cloud-based flood information systems (like the FLASH system utilizing TUFLOW or 3Di) that ingest forecast rainfall grids directly into 2D hydraulic models [9-11]. These systems can automate alerts based on specific trigger levels and provide hours of lead time to authorities for road closures and evacuations [12-14].
*   **Transition to comprehensive risk mitigation:** Do not rely solely on structural hazard management or generic "zero afflux" targets, which can foster a false sense of security [15-17]. Implement non-structural measures such as targeted community education, early warning systems, and land-use planning to address the vulnerability and exposure sides of the risk equation [18-20]. 

**Hydrological Modelling Techniques**

*   **Filter embedded bursts in PMP estimates:** When using the Generalised Short Duration Method (GSDM) for Probable Maximum Precipitation (PMP), be aware that up to 47% of temporal patterns may contain inconsistent embedded bursts [21, 22]. These can artificially inflate rainfall depths by up to 28%, leading to significant over-design of infrastructure like flood walls [23]. Practitioners should filter or smooth these embedded bursts out of the temporal patterns [21, 24]. 
*   **Apply joint probability for coastal and urban boundaries:** Avoid using conservative "cumulative extreme" assumptions (e.g., assuming a 1% AEP peak streamflow perfectly coincides with a 1% AEP storm tide) [25]. Using joint probability methods based on observed data provides a more realistic understanding of urban flood risks and prevents unnecessary economic and administrative burdens from overly conservative flood overlays [26-28].
*   **Use robustness metrics for extreme event calibration:** When calibrating conceptual rainfall-runoff models for extreme events outside the historical record, use a robustness metric. Subsample parameter sets that produce the lowest standard deviation across peak flows to reduce variability and increase confidence in the simulated extreme event responses [29-31].
*   **Couple surface and groundwater in direct rainfall models:** For continuous, long-term catchment-wide direct rainfall (rain-on-grid) simulations, couple the 2D surface model with a groundwater infiltration method (like Green-Ampt) [32, 33]. This prevents the need to constantly reset loss parameters between rainfall events and significantly improves the accuracy of peak levels and hydrograph receding patterns [33, 34].

**Case Studies and Extreme Events**

*   **Deploy real-time scour and image-based monitoring:** Extreme events, such as the 2023 Fitzroy River floods which destroyed the Great Northern Highway bridge, drastically alter riverbed conditions, rendering fixed-bed rating curves inaccurate [35-38]. Implement real-time scour monitoring (e.g., ground-penetrating radar) and place AI-assisted, image-based streamflow cameras on high ground to ensure data continuity when floodplain gauges fail [39-41].
*   **Re-evaluate temporary construction drainage standards:** Extreme rainfall events during construction can cause massive sediment runoff, scour, and costly delays [42, 43]. The standard 1-in-2 to 1-in-10 AEP design storms for temporary drainage are often insufficient [44, 45]. Monitor global climate drivers—such as a negative Indian Ocean Dipole (IOD), La Niña coupled with a positive Southern Oscillation Index (SOI), and a positive Southern Annular Mode (SAM)—and increase the capacity of temporary drainage controls when these indicators signal a high risk of extreme rainfall [46, 47].
*   **Leverage post-event modelling for rapid restoration:** Following extreme, un-gauged rainfall events, rapid direct-rainfall hydraulic modelling combined with site inspections can successfully identify newly altered flow paths [48, 49]. This allows asset owners to immediately prioritize temporary drainage restoration and bund installations around critical infrastructure [50, 51].

**Climate and Future Trends**

*   **Account for predictive hydrological errors in yield assessments:** Traditional water supply yield assessments often ignore predictive hydrological errors, which can overestimate system yield by up to 55% and underestimate design risks by a factor of 30 [52-54]. Furthermore, climate change is a present reality, not just a future problem; practitioners should use temperature covariates in stochastic models to detect and account for historical drying trends (e.g., a ~30% yield reduction observed in South-East Queensland since 1990) [55, 56].
*   **Adopt "climate-ready" environmental flow objectives:** Because climate change is altering baseline hydrology, historical reference states are becoming obsolete [57, 58]. Shift environmental flow objectives away from targeting specific individual species and instead focus on maintaining broad ecological functional groups that can adapt to changing water availability [59-61]. 
*   **Factor in rising rainfall losses and sub-hourly intensification:** Climate change is projected to increase both initial and continuing rainfall losses due to drier antecedent soil moisture [62-64]. While this may decrease the severity of frequent floods, rare and extreme floods will still increase in line with rainfall maxima [64-67]. Furthermore, sub-hourly extreme rainfall is intensifying at alarming rates (e.g., at least 20% per decade near Sydney), requiring immediate attention for urban flash-flood planning even in regions where daily rainfall totals appear stationary [68, 69].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes within the HWRS 2023 notebook—Flood Forecasting and Warning Systems, Hydrological Modelling Techniques, Case Studies and Extreme Events, and Climate and Future Trends—are highly interconnected. Rather than operating in silos, these themes collectively address the overarching challenge of managing increasingly volatile water resources in a non-stationary environment. 

The cross-cutting issues and interdisciplinary connections primarily manifest in three ways: the necessity of adapting models to climate-driven non-stationarity, the integration of data science and machine learning across all hydrologic disciplines, and the evolution of static models into real-time operational forecasting tools during extreme events.

### Cross-Cutting Issues and Interdisciplinary Connections

**1. The Non-Stationarity Challenge (Bridging Climate Trends, Modelling, and Extreme Events)**
A major cross-cutting issue is that historical data can no longer reliably predict future extreme events due to climate change [1]. This non-stationarity breaks traditional modelling assumptions. Researchers are finding that climate change creates a "dichotomy" in urban flood responses: intensifying storms cause more destructive, rare floods, while longer dry periods decrease the severity of frequent, nuisance floods [2-4]. Consequently, hydrological modelling techniques must be adapted to account for changing antecedent moisture conditions and rainfall losses in future climate scenarios [5, 6]. 

**2. Data Science and Machine Learning (Bridging Modelling, Forecasting, and Climate)**
Artificial Intelligence (AI) and Machine Learning (ML) act as the interdisciplinary glue connecting predictive climate modelling, streamflow forecasting, and operational design. Machine learning algorithms are being used to process vast amounts of disparate data—such as satellite imagery, radar rainfall, and climate indices—to improve both the accuracy and speed of hydrological models and flood forecasting systems [7-9].

**3. Operationalizing Models for Disaster Response (Bridging Modelling, Forecasting, and Extreme Events)**
Hydraulic and hydrologic models are no longer just used for long-term planning; advances in computational power have allowed them to be coupled with real-time forecasting systems to manage extreme events as they happen. Cloud-based platforms and ultra-fast hydrodynamic models are being used to simulate real-time flood extents, integrating atmospheric forecasts to warn communities and manage infrastructure dynamically [10-12].

### Specific Examples of Papers Bridging Multiple Themes

**Projecting rainfall and flood frequency curves under climate change by Wasko et al. [1, 13]**
* *Themes Bridged:* Climate and Future Trends, Hydrological Modelling Techniques, Extreme Events.
* *Connection:* This paper bridges climate change and modelling by forcing calibrated rainfall-runoff models with bias-corrected climate model projections to estimate future extreme flood quantiles. It highlights that while rare extreme rainfalls will increase, more frequent floods may actually decrease due to drier antecedent soil conditions [13]. 

**Flood Forecasting to Prepare Communities for Flood Events by Terry et al. [10, 11, 14]**
* *Themes Bridged:* Flood Forecasting and Warning Systems, Hydrological Modelling Techniques, Case Studies and Extreme Events.
* *Connection:* The authors detail the development of the "FLASH" Flood Information System, which utilizes ultra-fast hydrodynamic modelling (TUFLOW/3Di) combined with real-time radar and forecast rainfall grids [12, 15]. This technical modelling framework is directly applied to disaster response forecasting, as demonstrated during the extreme La Niña flood events in the Hunter Valley in 2022 [10, 14].

**Quantifying the Benefits of using Machine Learning for the Smart Design and Control of Stormwater Storages by Thyer et al. [7]**
* *Themes Bridged:* Hydrological Modelling Techniques, Flood Forecasting and Warning Systems, Climate and Future Trends.
* *Connection:* This paper uses machine learning multi-objective optimization to design and control distributed stormwater storages. By operating these storages dynamically in real-time during storm events, peak flows can be reduced, helping urban catchments adapt to the increased peak flows expected from climate change and densification [7]. 

**Robust Hydrological Model Calibration for Extreme Events by Dykman et al. [16, 17]**
* *Themes Bridged:* Hydrological Modelling Techniques, Case Studies and Extreme Events.
* *Connection:* Hydrologists frequently have to model extreme events that exceed any historically recorded data. This paper bridges modelling techniques and extreme events by proposing a "robustness metric" to help select conceptual rainfall-runoff model parameters that are specifically suited to simulating unseen extreme events reliably [16, 17].

**Towards Resilient Water Supply Management: Innovative Forecasting Techniques for Medium to Long-Term Rainfall Anomalies by Jiang et al. [8, 18]**
* *Themes Bridged:* Climate and Future Trends, Flood Forecasting and Warning Systems.
* *Connection:* This research connects long-term climate modeling with actionable forecasting by using the Wavelet System Prediction (WASP) methodology and Hierarchical Linear Combination (HLC) of climate indices (like ENSO and IOD). It aims to predict rainfall anomalies years in advance, giving water managers the foresight needed to handle climate uncertainty [8, 18]. 

**How useful are global streamflow forecasts for Australian catchments? by Johnson et al. [9, 19, 20]**
* *Themes Bridged:* Flood Forecasting and Warning Systems, Hydrological Modelling Techniques.
* *Connection:* This paper evaluates the Copernicus Emergency Management Services (CEMS) global streamflow forecasts (GloFAS) for Australian catchments. It integrates machine learning (Long Short-Term Memory models) and wavelet-based post-processing methods to correct biases in the forecasts, demonstrating an interdisciplinary approach to improving flood warning accuracy [9, 20].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
The papers from HWRS 2023 identify numerous research gaps, unanswered questions, and areas for future investigation across several critical themes in hydrological modelling and flood management. Here is a comprehensive breakdown of the future research directions highlighted by the authors:

### **Hydrological Modelling Techniques**
*   **Rainfall Loss Estimation:** Authors identify a **"critical knowledge gap" in the lack of robust procedures to estimate rainfall losses based on physical catchment characteristics** rather than historical calibration [1]. Future work aims to expand datasets (especially incorporating more clay soil observations) and apply advanced statistical and machine learning methods to develop accurate, rasterized loss maps and separate initial and continuing losses [1, 2].
*   **Direct Rainfall (Rain-on-Grid) Modelling:** While direct rainfall modelling is improving, further investigation is needed to understand its disadvantages and scalability. Future research should apply this approach to more case studies to explore the impact of varying grid cell resolutions, testing across different catchment sizes and soil types, and better representing vegetative rainfall losses [3, 4].
*   **Design Flood Estimation (ARR2019) Guidance:** There is an urgent need for the ARR2019 guidelines to address several unanswered questions. Authors call for clear guidance on how to assemble design flood surfaces (either locally or catchment-wide) [5, 6], how candidate hydrographs should be constructed in hydraulic models [7], and explanations for why historically calibrated losses differ from design losses [8]. Authors also stress the need for a funded expert panel to oversee ongoing maintenance and updates to ARR2019 [9]. 
*   **Embedded Bursts in Temporal Patterns:** Current temporal patterns often contain "inconsistent" embedded bursts. Future research is required to develop and evaluate suitable, consistent, and practical filtering techniques [10, 11]. When the Probable Maximum Precipitation (PMP) methodology is updated for climate change, authors recommend simultaneously updating temporal patterns to minimize these embedded bursts [11, 12].
*   **Catchment Non-linearity:** The standard industry assumption of non-linearity in extreme flood ranges (e.g., doubling rainfall results in more than double the runoff peak) is challenged. Authors argue there is **little strong evidence supporting the non-linear assumption for extreme floods** and recommend investigating the validity of linear parameterisations for extreme flood ranges [13, 14]. 
*   **Routing Models:** There is a need to investigate why predominately advective models and diffusive models (like RORB) perform similarly well [15]. Furthermore, authors point out that simple one-parameter depth-area-duration (DAD) functions cannot capture all drainage shapes, indicating a need for new functions that are both differentiable and integratable [16, 17].

### **Flood Forecasting and Warning Systems**
*   **Deep Learning and Machine Learning Forecasts:** For multi-variate deep neural network streamflow forecasting, future work needs to focus on **extending the forecast lead time while maintaining accuracy**. Researchers plan to experiment with different input combinations and vary input sequence sizes to determine the optimal number of lagged input data points that contribute to future streamflow [18, 19]. Machine learning algorithms are also recommended to improve models that use satellite data to map complex floodplain connectivity [20].
*   **Fast-Response Flash Flood Models:** Systems like the FLASH hydrodynamic model require continuous improvement. Identified areas for future development include refining flood modelling techniques for fast-response catchments and incorporating additional real-time validation of model outputs against streamflow and gauge height records [21].
*   **Calibration Metrics for Low Flows:** Current model evaluation metrics (like NSE) are typically biased toward peak floods. There is a gap in standard approaches to evaluate water quality and quantity models during low-flow periods. Researchers are investigating if using RMSE against half the standard deviation or RSR against coefficients of variation can better describe model fit for low flows [22, 23].

### **Case Studies and Extreme Events**
*   **Extreme Scour and Bank Migration:** Following the catastrophic failure of the Fitzroy River Bridge, authors recommend comprehensive hydraulic modelling that accounts for extreme changes in bed and bank conditions [24]. Future directions include leveraging **real-time scour monitoring technologies and AI-assisted, image-based backup systems** to predict flow conditions when physical gauges fail [24, 25].
*   **Dam Flood Attenuation:** There is a dearth of literature on how to quickly construct empirical relationships relating flood attenuation to spatial and catchment characteristics without using full hydrologic models [26]. Because of the complexity of catchment responses, current studies struggled to find generalizable rules; future research needs a larger sample of catchments of varying sizes [27].
*   **Drainage Infrastructure Enhancements:** Following rare flooding in the Poatina catchment, future investigations are needed to identify enhancements to drainage systems and formalize performance standards for remote assets [28, 29].

### **Climate and Future Trends**
*   **Sub-hourly Rainfall Intensification:** An observed upward trend of at least 20% per decade in sub-hourly extreme rainfall has been detected near Sydney. Since this trend is not linked to known natural climate variations, **future research is needed to unravel the underlying mechanisms of this intensification**. Authors urge the use of radar object-based techniques in other regions to assess if this trend is a widespread phenomenon [30].
*   **Water Supply Yield and Stationarity:** The traditional "yield" concept relies on a steady-state assumption that fails under non-stationary demand and changing climates. Authors question whether the yield concept can still be used with confidence and suggest that **future water resource planning must transition to dynamic simulation**. More work is required to explore different system configurations to assess how systems with large inertia respond to non-stationarity [31-33].
*   **Translating Runoff to Yields:** In Tasmania, while future change ratios have been calculated for runoff, the assumption that these runoff ratios can be directly applied to supply yields must be rigorously assessed for each individual system [34]. Future work includes developing a 2050 yield scenario and implementing supply models to estimate specific shortages [35].
*   **Compound Events:** To better assist water sector stakeholders, future research must investigate multi-annual cumulative wet/dry periods occurring alongside intense, short-duration extreme events, while also integrating projections of extreme heat [36, 37]. 
*   **Ecohydrology under Sea-Level Rise:** There are major unanswered questions regarding how to set "climate-ready" ecological objectives. For estuaries facing sea-level rise and changing entrance dynamics, researchers ask: **Do we need to plan for completely new ecological states?** What will be the ecological implications for upstream riverine reaches when entrances remain closed? Furthermore, how do we define "natural" compliance flows if the baseline flow regime fundamentally changes [38]?
---

**See Also:**
- [Conference Papers Home](index.md)
