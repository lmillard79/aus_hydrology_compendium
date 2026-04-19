# HWRS 2021 Mind Map

## HWRS 2022 Hydrology and Water Resources Research

**Conference:** Hydrology & Water Resources Society 2021  
**Sources:** 79 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
HWRS 2022 Hydrology and Water Resources Research
├── Flood Estimation & Modelling
│   ├── ARR2019 Design Rainfall
│   │   ├── Underestimation Bias in NSW & Victoria
│   │   ├── Queensland Bias Assessment (162 sites)
│   │   └── Regionalized Overestimation (Cairns & Brisbane)
│   ├── Hydrologic Toolsets
│   │   ├── WBNM (Watershed Bounded Network Model)
│   │   ├── TUFLOW 1D/2D ROG Models
│   │   ├── FLIKE Software (LP3 Distribution)
│   │   └── FLOW-3D for Fish Passage Design
│   └── Technological Innovations
│       ├── BoM GeoFabric 3 Catchment Aggregation
│       ├── CFD for Vertical Slot Fishways
│       └── HEH (Hydraulically Equivalent Hydrology)
├── Climate Change & Uncertainty
│   ├── Stationarity Issues
│   │   ├── Milly et al. (2008) 'Stationarity is dead'
│   │   ├── Anthropocene Pulse & Press Disturbances
│   │   └── Non-stationary Trend Estimation
│   ├── Future Projections
│   │   ├── RCP 4.5 & RCP 8.5 Scenarios
│   │   ├── CMIP5 Global Climate Models (GCMs)
│   │   └── Climate Tipping Points (CTPs)
│   └── Adaptation Strategies
│       ├── Adaptive Governance & Markets
│       ├── No-regret & Reversible Designs
│       └── Fail-safely vs Fail-safe Philosophies
├── Urban Water Security
│   ├── Queensland Framework
│   │   ├── Water Act 2000 Entitlements
│   │   ├── Supplemented vs Unsupplemented Water
│   │   └── Regional Level of Service (LOS)
│   ├── Yield Estimation
│   │   ├── System Yield vs Demand Gaps
│   │   ├── Operational Yield (Dynamic Simulation)
│   │   └── Victorian Desalination Project (VDP)
│   └── Drought Response
│       ├── Water Carting (Communities < 5000)
│       ├── Diversification (Desalination & Recycling)
│       └── Triggers for Restrictions
└── Data Science in Hydrology
    ├── Neurocomputing
    │   ├── Machine Learning (Predictive Patterns)
    │   ├── Deep Learning (Neural Networks)
    │   └── Bayesian Networks
    ├── Big Data Sources
    │   ├── Remote Sensing (Satellite Missions)
    │   ├── Atmospheric Reanalysis (ERA5, BARRA)
    │   └── AWAP (Australian Water Availability Project)
    └── AWAP Limitations
        ├── Smoothing via Surface Fitting
        ├── Underestimation of Extreme Events
        └── Climatology Biases
```

---

## Main Themes

### 1. [Flood Estimation & Modelling](hwrs-2021/flood-estimation-modelling.md)
- ARR2019 Design Rainfall
- Hydrologic Toolsets
- Technological Innovations

### 2. [Climate Change & Uncertainty](hwrs-2021/climate-change-uncertainty.md)
- Stationarity Issues
- Future Projections
- Adaptation Strategies

### 3. [Urban Water Security](hwrs-2021/urban-water-security.md)
- Queensland Framework
- Yield Estimation
- Drought Response

### 4. [Data Science in Hydrology](hwrs-2021/data-science-in-hydrology.md)
- Neurocomputing
- Big Data Sources
- AWAP Limitations

---

## Theme Detail Pages

- [Flood Estimation & Modelling](hwrs-2021/flood-estimation-modelling.md)
- [Climate Change & Uncertainty](hwrs-2021/climate-change-uncertainty.md)
- [Urban Water Security](hwrs-2021/urban-water-security.md)
- [Data Science in Hydrology](hwrs-2021/data-science-in-hydrology.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
**Flood Estimation & Modelling**
*   **Utilise Hydrologic Pre-Processing:** To drastically reduce computational time and cost in catchment-wide 2D hydrodynamic modelling, use hydrologic models as pre-processors. By extracting a small number of critical events that represent the Design Flood Estimate (DFE), practitioners can reduce the number of events hydraulically modelled from over 1,000 down to less than 5 [1, 2].
*   **Adopt Sub-Grid Sampling (SGS) for Direct Rainfall:** When using 2D direct rainfall (rain-on-grid) models, implementing SGS is highly recommended. SGS improves the definition of cell storage and conveyance, allowing for much larger 2D cell sizes (and thereby faster run times) while maintaining model accuracy [3-5]. Avoid using 1st-order traditional solvers in complex urban or open-channel scenarios, as they perform poorly and become numerically diffusive [6].
*   **Implement Depth-Varying Roughness:** For forested floodplains, avoid using static Manning’s *n* values. Adopting depth-varying roughness relationships (which account for the transition from trunk to canopy as water levels rise) yields a far more reliable reproduction of actual flood stage hydrographs [7, 8]. 
*   **Rethink the "Zero Afflux" Paradigm:** While regulatory authorities increasingly request "zero afflux" (0 mm change) for development approvals, practitioners should recognize this is often theoretically and practically impossible to guarantee due to cumulative measurement, topographic, and modelling errors [9-11]. Management should transition toward strategies based on net community benefit and sustainable development rather than absolute zero impact mandates [12, 13].
*   **Upgrade Floodway Scour Assessments:** Current 1D modelling and standard weir equations are often inadequate for assessing extreme flow conditions over floodways [14]. Practitioners should apply 2D or 3D Computational Fluid Dynamics (CFD) modelling to capture the complex interaction between orifice flow (through culverts) and weir flow (over embankments) to properly design scour countermeasures and prevent roadway washouts [15, 16].

**Climate Change & Uncertainty**
*   **Account for Non-Linear Peak Flow Increases:** When factoring climate change into infrastructure design, hydrologists must recognize that the percentage increase in peak flood flow is generally much larger than the percentage increase in rainfall intensity [17, 18]. 
*   **Adopt Scenario-Neutral Stress Testing:** Rather than relying purely on a limited set of top-down General Circulation Model (GCM) projections, employ scenario-neutral climate stress-testing (such as the foreSIGHT framework). This helps identify system-specific "failure modes" (e.g., multi-year drawdown failures) across a wide range of plausible temperature and precipitation combinations, thereby reducing decision paralysis [19-22].
*   **Transition to "Operational Yield" Assessments:** Stationarity is no longer a safe assumption [23, 24]. Water resource planners should transition to "operational yield" modelling, which evaluates system performance starting from current storage conditions and steps forward progressively under changing demand and climate scenarios. This allows managers to identify exact future time-points when the system will fail to meet security criteria, enabling optimized timing for infrastructure expansion [25, 26]. 

**Urban Water Security**
*   **Prepare Contingency Plans for Rapid Depletion:** Surface water supplies in many regional communities can deplete to critical levels within a short 2-to-5-year timeframe during severe droughts [27, 28]. Relying solely on demand restrictions is inadequate [29]. Planners must pre-identify and prepare contingency supply options (e.g., accessing dead storage, emergency desalination, water carting) well in advance of crises to avoid suboptimal, expensive emergency construction [28, 30, 31].
*   **Implement Integrated Model Management:** For large-scale greenfield developments, water utilities should move away from siloed models. Implement collaborative "Integrated Water Management" frameworks that dynamically link lot, precinct, and catchment models (e.g., MUSIC, Source, and TUFLOW) to holistically evaluate the benefits of purified recycled water and stormwater harvesting [32-34].
*   **Link Stormwater and Transport Models:** To accurately estimate Expected Annual Damages (EAD) and improve emergency evacuation planning, dynamically link stormwater models (like SWMM) with agent-based transport models. This ensures that the time-dependent hydrologic failure of a drainage network is directly translated into realistic traffic delays and road closures [35, 36].

**Data Science in Hydrology**
*   **Deploy Machine Learning (ML) Surrogates for Real-Time Forecasting:** Replace computationally heavy hydrodynamic models with ML surrogate models (such as Temporal Convolutional Networks) for real-time operations. By training ML models on the inputs/outputs of calibrated 2D hydraulic models, practitioners can generate highly accurate (e.g., ~2cm error) flood inundation maps in seconds rather than hours, giving emergency services critical advance warning [37-39].
*   **Use Mesh Modularization for Dynamic Environments:** One major hurdle for ML surrogate models is that they must be entirely retrained if the physical landscape (like urban development) changes. Overcome this by using "mesh modularization"—isolating localized edits to specific sub-domains so that only the modified portions of the model need to be recomputed, making ML practical for ever-changing urban environments [40-42].
*   **Utilize Hybrid Spatial Rainfall Methods:** To combat data sparsity and real-time gauge failures in operational flow forecasting, use hybrid calculation methods. By blending gridded daily rain data, Thiessen polygon weightings, and real-time single-gauge patterns, hydrologists can drastically reduce bias and create robust hourly spatial rainfall inputs that resist operational data interferences [43-45].
*   **Upgrade Flood Damage Estimation:** Move away from simplistic stage-damage curves that only rely on water depth. Calibrate loss models with local empirical data and apply tree-based ML algorithms to factor in highly influential variables such as floor area, building value, flow velocity, and precautionary measures, which significantly enhances the reliability of cost-benefit analyses for mitigation works [46-48].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes in the HWRS 2022 notebook are deeply interconnected, reflecting the evolution of hydrology into a transdisciplinary science [1]. Rather than treating flood risk, climate change, water security, and data science in isolation, modern hydrological practice relies on integrating these domains to solve complex real-world challenges. 

Here is a comprehensive breakdown of the cross-cutting issues, interdisciplinary connections, and specific papers that bridge these main research themes:

### 1. The Intersection of Flood Estimation & Climate Change
A recurring cross-cutting issue is the "death of stationarity"—the recognition that historical climate data is no longer a reliable predictor of future hydrological behaviour [2]. Consequently, researchers are actively bridging climate change projections with flood estimation models to ensure infrastructure can withstand future extremes.
*   **Adapting Flood Peaks for Infrastructure:** Ladson & Pedruco bridge these themes by developing an approximate method to predict climate-change-induced increases in flood peaks for infrastructure design, specifically factoring up design rainfall estimates using future climate projections without needing a full hydrologic model [3, 4].
*   **Mine Water Planning:** Zhan et al. use high-resolution climate change projections to undertake both event-based flood risk assessments (like flood levee design) and continuous water balance modelling [5, 6]. By integrating downscaled General Circulation Models (GCMs) into their flood and catchment simulations, they provide a quantitative framework for adapting mining infrastructure to future wet and dry extremes [7, 8].

### 2. Data Science as an Enabler for Advanced Flood Modelling
While two-dimensional (2D) hydrodynamic models have become the gold standard for flood estimation, they are computationally heavy and slow. Data science and machine learning (ML) are bridging this gap, creating fast, scalable solutions for real-time flood warning and probabilistic analysis.
*   **Surrogate Modelling:** Garcia & Juan address the computational limits of 2D solvers (like HEC-RAS 2D) by developing "mesh modularization." This enables the creation of supervised Machine Learning surrogate models that can accurately estimate flood inundation at near-instantaneous speeds, bridging high-resolution flood modelling with machine learning to make real-time flood alert systems feasible [9-11].
*   **Digital Twins for Urban Flooding:** Ho et al. demonstrate this intersection through a pilot project in Bangkok. They trained a machine learning model on the outputs of a calibrated hydraulic model and historical rain events [12, 13]. This ML surrogate processes real-time rainfall "nowcasts" to generate urban flood prediction maps in seconds rather than hours, feeding directly into an operational Digital Twin to aid emergency responses [14, 15].

### 3. Urban Water Security under Climate Change & Uncertainty
Urban water security requires reliable yield estimates, but climate change introduces "deep uncertainty" regarding future rainfall, evaporation, and population demands [16]. Researchers are bridging these themes by using stochastic data generation to stress-test urban water supplies against varied future climates.
*   **Scenario-Neutral Stress Testing:** Newman et al. bridge climate uncertainty and urban water security by applying a "scenario-neutral" climate stress-test to the Middle River Reservoir on Kangaroo Island [17, 18]. Instead of relying on a single climate forecast, they generate diverse hydroclimatic time series to identify specific failure modes (e.g., multi-year droughts) as the climate warms [19, 20].
*   **Synthetic Climate Sequences for Water Planning:** Lockart & Berghout detail the hydrologic modelling behind the Lower Hunter Water Security Plan [21]. They combine historical streamflow with NARCliM climate change projections, generating 100,000 replicates of 120-year synthetic climate sequences [22, 23]. This allows them to quantify the exact probabilities of triggering drought management responses under uncertain future conditions [24]. 
*   **Operational Yield Approaches:** Rhodes et al. discuss how climate change and variability create profound uncertainties in long-term yield estimates for Melbourne Water. They advocate for dynamic "operational yield" simulation approaches that assess changing system performance under climate shifts rather than relying on static historic yields [25-27]. 

### 4. Leveraging Data Science for Urban Water Security
Data science is increasingly being utilized to predict the complex, non-linear variables that dictate both the availability of urban water and the damages caused when water systems fail.
*   **Predicting Evaporation with AI:** Abed et al. use Decision Tree (DT) algorithms to predict monthly pan evaporation rates [28]. Because evaporation is a highly complex, nonlinear process heavily influenced by climate change, these data-driven AI models provide water managers with precise tools to forecast reservoir losses, directly supporting urban water security [29, 30].
*   **Multivariate Flood Damage Assessment:** Nafari & Sheers bridge data science, flood estimation, and urban water security by challenging traditional, simplistic depth-damage curves used in Australia. They developed a tree-based model to evaluate the complex interactions between water depth, flow velocity, building value, and socioeconomic status to better estimate disaster losses in urban areas [31-33]. 

**Summary**
The cross-cutting narrative in the HWRS 2022 notebook is the **transition from deterministic to probabilistic and adaptive approaches**. Flood modellers and urban water planners can no longer rely on static historical data due to **Climate Change & Uncertainty**. To manage this, they are increasingly relying on **Data Science**—ranging from stochastic climate generators to machine learning surrogates—to rapidly process vast amounts of data, simulate thousands of plausible futures, and ensure **Urban Water Security** and resilient infrastructure.
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
The HWRS 2022 papers identify several critical research gaps and propose future directions across the fields of hydrology, flood modelling, climate change, water security, and data science. 

### 1. Flood Estimation & Modelling
*   **High-Quality Calibration Data:** A major gap in 2D hydraulic modelling is the lack of high-quality, real-world benchmarking datasets to validate models and reduce input uncertainty [1-3]. Furthermore, there is a distinct need to calibrate hydraulic models at high flows, which requires new technologies (like drones) to measure floodwater velocities where traditional discharge measurements are unavailable [4, 5].
*   **Very Frequent Floods:** The application of the Peaks-Over-Threshold (POT) approach for estimating very frequent floods is currently limited in Australia [6]. **Future research should focus on using larger datasets across multiple states, defining regions based on the Region of Influence (ROI) approach, assessing the impact of sample sizes, and incorporating climate change and non-stationarity into the POT paradigm** [7, 8].
*   **Design Guidelines for Floodways:** Current Australian guidance relies heavily on one-dimensional (1D) equations, which are inadequate for complex weir and orifice flows at floodways [9, 10]. **There is a need to update guidelines (such as Austroads 2013) to include 2D and 3D CFD modelling guidance, which should be confirmed through physical and numerical modelling** [11, 12]. 
*   **Flood Damage Assessment:** Existing models, such as ANUFLOOD, are no longer sufficiently accurate for assessing commercial building damage [13, 14]. There is an urgent need to develop new commercial flood damage estimation functions that move beyond just water depth to incorporate building quality, precautionary measures, and floor area [15, 16]. 
*   **ARR2019 Improvements:** Researchers identified a need to revise Australian Rainfall and Runoff (ARR) 2019 guidelines to better address dynamic variations in catchment response times according to rainfall intensity [17, 18]. Additionally, further investigation is needed into the geographical clustering of overestimation and underestimation biases in the ARR2019 design rainfall methods [19, 20].

### 2. Climate Change & Uncertainty
*   **Standardised Climate Change Guidelines:** A significant gap exists in standardising how climate change signals are applied to water security assessments and generated rainfall datasets [21, 22]. **Future priorities include developing a "go-to" platform for climate models/emission scenarios, creating guidelines for decision-making frameworks, and proposing methods to overcome the assumption of hydrologic stationarity** [23-25].
*   **Rainfall Uncertainty vs. Temperature:** While climate models consistently predict higher temperatures, predicting future rainfall is highly uncertain [26-28]. Because climate models have low skill in predicting rainfall, future research might lean toward stochastic generation of future hydroclimates using temperature as a covariate rather than relying directly on GCM rainfall outputs [25, 29, 30].
*   **Deep Uncertainty in Yield Estimation:** Current approaches to determining water supply yield struggle with the "deep uncertainty" of climate change and future water demands [31, 32]. "Operational yield" approaches show promise but require more work to model the full range of long-term adaptation pathways and capacity-expansion requirements [33, 34]. 
*   **Multi-Hazard Infrastructure Failures:** There are significant gaps in understanding how dynamic weather patterns and water phase changes interact to create multi-hazard disasters that overwhelm civil infrastructure like dams and bridges [35-37]. 

### 3. Urban Water Security & Water Quality
*   **Water Quality in Cascade Water Supply Systems (CWSS):** Despite their historical importance, there is a severe lack of systematic water quality, demand, and consumption data for rural CWSS [38, 39]. The causes of eutrophication in these systems are not well understood [40]. **Future investigations should focus on nitrification and denitrification at the sediment-water interface, and explore low-cost, passive intervention strategies like biofiltration** [40, 41].
*   **Pollutant and Catchment Modelling:** There are high levels of uncertainty in models estimating nutrient and sediment loads (e.g., the Port Phillip Bay model) [42, 43]. Future work needs to reduce parameter uncertainty in rainfall-runoff models, account for extreme climatic events, and improve the simplistic representation of river regulation [42, 43].
*   **Infrastructure Sustainability (IS) Ratings:** Meeting IS rating requirements for water quality poses major challenges because baseline freshwater environment datasets often do not exist and are onerous to establish [44, 45]. There is also a lack of approved methodologies and guidance for assessing the required 1.5-year ARI stream-forming flows [46, 47].

### 4. Data Science in Hydrology
*   **Machine Learning (ML) Limitations:** ML models for flood forecasting treat underlying hydraulic models as the "ground truth," meaning they inherit all the assumptions and errors (such as mass imbalances) of the physical models [48, 49]. Additionally, ML models struggle to predict extreme events if such events were absent from their training data [48]. 
*   **Dynamic Urban Landscapes:** A major limitation of ML surrogate models is that they assume a static environment. In rapidly developing urban landscapes, models must be continually retrained. **Future research is directing attention toward "modularization" to minimize the computational burden of updating these models** [50, 51].
*   **Stochastic Rainfall Models (SRM):** Statistical evaluation metrics for SRMs often fail to capture discrepancies in simulated rainfall (like antecedent moisture), meaning that statistically "good" modelled rainfall can still translate into "poor" modelled streamflow [52, 53]. **Further research is needed to identify and rectify the hidden sources of discrepancy in simulated rainfall** [53].
*   **Regionalisation of Forecasts:** While regionalising parameters from synthetic data or neighbouring catchments shows promise, current studies are limited to gauges that are geographically close and share hydrologic patterns [54]. Future studies require testing across a larger number of gauges and more diverse scenarios [55].
---

**See Also:**
- [Conference Papers Home](index.md)
