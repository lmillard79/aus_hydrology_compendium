# HWRS 2022 Mind Map

## HWRS 2022 Hydrology and Water Resources Research

**Conference:** Hydrology & Water Resources Society 2022  
**Sources:** 124 papers  
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

### 1. [Flood Estimation & Modelling](hwrs-2022/flood-estimation-modelling.md)
- ARR2019 Design Rainfall
- Hydrologic Toolsets
- Technological Innovations

### 2. [Climate Change & Uncertainty](hwrs-2022/climate-change-uncertainty.md)
- Stationarity Issues
- Future Projections
- Adaptation Strategies

### 3. [Urban Water Security](hwrs-2022/urban-water-security.md)
- Queensland Framework
- Yield Estimation
- Drought Response

### 4. [Data Science in Hydrology](hwrs-2022/data-science-in-hydrology.md)
- Neurocomputing
- Big Data Sources
- AWAP Limitations

---

## Theme Detail Pages

- [Flood Estimation & Modelling](hwrs-2022/flood-estimation-modelling.md)
- [Climate Change & Uncertainty](hwrs-2022/climate-change-uncertainty.md)
- [Urban Water Security](hwrs-2022/urban-water-security.md)
- [Data Science in Hydrology](hwrs-2022/data-science-in-hydrology.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
Here are the key practical recommendations and actionable insights for floodplain managers, hydrologists, and water resources professionals based on the HWRS 2022 research themes:

### 1. Flood Estimation & Modelling
*   **Implement Sub-Grid Sampling (SGS) in 2D Models:** When utilizing 2D shallow water equation solvers (such as TUFLOW), use sub-grid sampling (SGS) to extract terrain data. SGS improves the definition of cell storage and wetted perimeters, drastically improving cell size convergence and reducing simulation times [1, 2]. This allows practitioners to confidently replace 1D open channels with 2D cells, seamlessly preserving momentum transfer and energy loss interactions [3, 4].
*   **Improve High-Flow Rating Curves with Velocity Measurements:** Generating rating curves at high flows using 2D modelling is highly sensitive to the assumed surface roughness, leading to significant uncertainties in discharge outputs [5, 6]. To correct this, capture floodwater velocity measurements near the gauge during events (e.g., utilizing drones) and calibrate the model's roughness parameters to match the velocity, not just the water level [6].
*   **Avoid Oversimplifying Joint Probabilities:** In coastal/riverine flood studies, do not assume that a maximum peak river flow will coincide perfectly with a maximum tide (e.g., pairing a 1% AEP flow with a 1% AEP tide). This miscalculates the joint probability, resulting in an extreme event profile (e.g., 0.0001% AEP) that overestimates flood depths and distorts climate change multiplier applications [7, 8]. 
*   **Optimize Pier Loss Calculations:** When modeling bridge pier blockages in 2D models, apply the "at-pier" method rather than a span-averaged approach. Using velocities specifically at the piers rather than across the full bridge span provides a more accurate replication of analytical energy losses [9].
*   **Accelerate Long-Term Continuous Simulation (LTCS):** When executing LTCS for infrastructure like road networks, utilize a Hydraulically Equivalent Hydrology (HEH) approach. This method models reach storage to rapidly identify candidate periods of "backwater flooding," reducing the required 2D LTCS input size by over 90% and massively cutting computational bottlenecks [10, 11].

### 2. Climate Change & Uncertainty
*   **Adopt an "Operational Yield" Approach:** Move away from assessing system yield using static, time-sliced storage data. Instead, model "operational yield" using dynamic system simulations that start from current storage conditions and continuously adjust for changing climate and demand. This better characterizes exactly *when* a system will fail, helping managers optimize the timing of future supply augmentations [12, 13].
*   **Apply Sensible Peak Flow Estimations for Smaller Projects:** If you lack a flood event model to assess climate change impacts on peak flows, recognize that the percentage increase in peak flow will generally be *larger* than the percentage increase in rainfall intensity [14, 15]. This gap widens with higher initial/continuing losses. Practitioners can use regression equations based on these predictors (obtainable from the ARR Data Hub) for initial screening assessments [14, 16].
*   **Standardise Climate Data Selection:** For continuous simulation (like water balance modeling), use downscaled daily rainfall and evaporation projections that maintain annual and seasonal variabilities [17, 18]. For event-based designs (like flood levees), factor up current design rainfall intensities based on mean temperature projections associated with specific Representative Concentration Pathways (RCPs) [19, 20].
*   **Embrace "No-Regret" Adaptation Strategies:** The assumption of hydrologic stationarity (that the future will mimic the past) is dead [21, 22]. Engineers must design infrastructure robust against a range of plausible futures by prioritizing "no-regret" strategies (accruing benefits regardless of climate change), "safety-margin" designs (over-designing at little cost), and easily retrofitted structures [22, 23].

### 3. Urban Water Security
*   **Embed Actionable Drought Triggers in Operational Plans:** Do not wait for a crisis to make supply decisions. Identify specific dead or minimum operating (D/MO) storage levels that indicate a known duration of remaining supply. Embed these triggers directly into operational manuals so that demand restrictions or contingency supply connections are deployed proactively with sufficient lead time [24, 25].
*   **Perform Scenario-Neutral Climate Stress-Tests:** Instead of relying solely on top-down climate projections, use a "scenario-neutral" approach (such as the foreSIGHT framework). Test your water supply system against a wide grid of plausible changes in rainfall and potential evapotranspiration (PET) to identify its exact sensitivities [26, 27]. This exposes hidden failure modes—like multi-year reservoir depletion—that are not evident in historical records [28].
*   **Plan for Droughts Worse Than the Historical Record:** Historical modeling is no longer sufficient, especially for communities exceeding 5,000 people. Practitioners must run stochastic models (e.g., 10,000-year generated datasets) to stress-test systems against drought events far more severe than historically observed [29-31].

### 4. Data Science in Hydrology
*   **Deploy Machine Learning for Real-Time Flood Forecasting:** Train machine learning (ML) surrogate models using the outputs of highly detailed 1D-2D hydrodynamic models and historic rainfall data. Once trained, these ML models can process real-time radar "nowcasts" in a matter of seconds (compared to hours for traditional hydraulic models), providing highly accurate and immediate spatial flood warning maps [32-34].
*   **Implement "Mesh Modularization" for ML Models:** The biggest drawback to ML surrogate models is the computational cost of updating them every time an urban landscape changes (e.g., a new detention pond). Practitioners can use "mesh modularization" to isolate the changed area, extract its localized boundary conditions, and update the model without re-computing the entire catchment [35, 36].
*   **Enhance Flood Loss Estimation with Tree-Based Algorithms:** Traditional stage-damage curves that rely solely on water depth are subject to high uncertainty. Transition to tree-based data models that incorporate flow velocity, building floor area, construction quality, building value, and precautionary measures to drastically improve the reliability of disaster loss estimates for cost-benefit analyses [37-39].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
**The research themes in the sources represent a paradigm shift in modern hydrology: traditional, isolated, and deterministic approaches are being replaced by integrated, probabilistic, and computationally advanced methodologies.** 

Rather than existing in silos, the themes of Flood Estimation & Modelling, Climate Change & Uncertainty, Urban Water Security, and Data Science in Hydrology are deeply interwoven. **Data Science provides the computational power required to run complex Flood and Water Security models under the deep Uncertainty introduced by Climate Change.**

Here is how these cross-cutting issues connect, alongside specific examples of papers that bridge multiple themes:

### 1. Climate Change & Flood Estimation: The "Death of Stationarity"
A major cross-cutting issue in the sources is that historic climate records are no longer sufficient to predict future flood risks. **The assumption of "stationarity"—that the future will replicate the hydrologic past—is now widely considered obsolete due to climate change** [1], [2]. To estimate floods accurately, hydrologists must now embed climate uncertainty directly into their models.

*   **Bridging Paper (Ladson & Pedruco):** This paper explicitly bridges Climate Change and Flood Modelling by developing a method to estimate climate change-induced increases in peak flood flows [3]. Because global warming increases rainfall intensity, the authors use Australian Rainfall and Runoff (ARR) procedures to factor up design rainfall, utilizing hydrologic models (like RORB) to demonstrate how higher losses and varying Annual Exceedance Probabilities (AEPs) impact infrastructure design under future climates [4], [5].
*   **Bridging Paper (Ettema):** This research bridges atmospheric climate science with civil engineering flood design. It highlights how the convergence of dynamic weather patterns (like "bomb cyclones") and water’s material behavior can create multi-hazard extreme events that overwhelm civil infrastructure [6], [7]. The author argues that climate science and civil engineering must formally merge to prevent future disasters [6], [8].

### 2. Climate Change & Urban Water Security: Planning for Deep Uncertainty
Urban water security can no longer rely on single deterministic forecasts. **Because climate change brings "deep uncertainty" regarding future rainfall, evaporation, and droughts, water managers must shift toward stochastic (probabilistic) modelling to stress-test their supply networks** [9], [10], [11]. 

*   **Bridging Paper (Newman et al. - Kangaroo Island):** This paper uses a "scenario-neutral" approach to bridge climate uncertainty and water security. Because Kangaroo Island only has a single year's water supply capacity, traditional supply-and-demand overlays were failing [12]. Using the *foreSIGHT* software tool, the authors stress-tested the system against a massive ensemble of generated, perturbed climate futures, identifying the exact climatic thresholds where the water supply would fail [13], [14], [15].
*   **Bridging Paper (Lane et al. - QLD Urban Water Security):** Bridging water security with climate change projections, this paper applies downscaled Regional Climate Models (RCMs) from 11 General Circulation Models (GCMs) to simulate future water security [10], [16]. By focusing not just on the median projection, but on the full 80% confidence interval of extreme scenarios, the authors demonstrate how planners can make precautionary decisions despite massive climate modelling uncertainties [17], [18].
*   **Bridging Paper (Lockart & Berghout - Lower Hunter Water Security Plan):** This paper bridges all three themes by using R scripts (Data Science) to combine historic data with NARCliM1.5 climate change projections (Climate Uncertainty) to generate thousands of synthetic climate replicates. These were then fed into headworks models to assess system yield and trigger drought management plans (Water Security) [19], [20], [21].

### 3. Data Science & Flood Modelling: Next-Generation Forecasting
Traditional 2D hydrodynamic flood models (like TUFLOW or HEC-RAS) provide highly accurate mapping but are too computationally heavy to be useful during a live emergency. **Data science bridges this gap by using Machine Learning (ML) algorithms as "surrogate models" that emulate the physics of hydraulic models in a fraction of the time.**

*   **Bridging Paper (Ho et al. - Bangkok Digital Twin):** This paper bridges flood modelling and machine learning. A 1D-2D hydrodynamic flood model was built for Bangkok, but it took 30 hours to run [22], [23], [24]. By training a Temporal Convolutional Network (TCN) machine learning model on the hydraulic model's outputs and historical rainfall, the ML surrogate was able to predict flood depths and extents for real-time rain events in just 30 seconds, maintaining an accuracy of ~2cm [24], [25], [26]. 
*   **Bridging Paper (Garcia & Juan - Mesh Modularization):** The authors bridge big data and flood estimation by solving a major limitation of ML in dynamic urban environments: if the physical environment changes (e.g., a new reservoir is built), the ML model must usually be entirely retrained [27], [28]. They propose "mesh modularization" to isolate boundary conditions, drastically minimizing the computational cost of updating the ML surrogate and allowing for real-time flood alerts [29], [30]. 

### 4. Data Science & Urban Water Security: Predictive Resource Management
Ensuring urban and agricultural water security requires anticipating how much water will be lost to evaporation and how much will be demanded by users. **Artificial Intelligence and advanced statistics are being deployed to predict complex, non-linear hydrological variables that traditional empirical models fail to capture** [31], [32].

*   **Bridging Paper (Ng et al. - Forecasting Irrigation Demands):** To prevent over-releasing water from dams (which causes flooding) or under-releasing (which threatens water security), this study uses Bayesian Joint Probability (BJP) modelling [33]. This statistical data science approach generates probabilistic ensemble forecasts of future irrigation demands on the Murray River, outperforming traditional estimations [33], [34].
*   **Bridging Paper (Abed et al. - Predicting Pan Evaporation):** Evaporation heavily dictates water supply security. Because traditional linear models struggle with the non-linear behavior of evaporation, the authors bridged water security and data science by applying a Decision Tree Algorithm (an AI method) to handle large volumes of meteorological data and accurately predict monthly pan evaporation rates [31], [35].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
The research papers presented at HWRS 2022 highlight numerous gaps and chart detailed future directions across the hydrology and water resources disciplines. 

Here are the key unanswered questions and areas needing more investigation, categorized by the main research themes:

### Flood Estimation & Modelling
*   **Need for High-Quality Calibration Data:** A critical gap across multiple studies is the lack of high-quality, real-world data sets for model calibration and solver benchmarking [1-3]. For instance, traditional methods struggle to estimate high-flow rating curves because floods are difficult to measure accurately; researchers propose testing new technologies like drones to capture floodwater velocity data to improve hydraulic model estimations [4-6]. Similarly, there is a major knowledge gap stemming from an absence of quantitative field observations of high-Reynolds-number hydrodynamics in large dam spillways [7]. 
*   **Refining Design Rainfall and Frequency Analyses:** Investigations into the ARR2019 design rainfall method revealed sporadic underestimations and clustered overestimations (particularly in catchments smaller than 200 km²), which require further study to determine the systemic causes [8, 9]. Additionally, while Peaks-Over-Threshold (POT) methods show promise for regional flood frequency analysis (RFFA), they require broader validation on ungauged catchments and further investigation into how regional heterogeneity actually impacts the precision of quantile estimations [10-13].
*   **Updating Flood Damage Models:** Australian flood damage models, such as ANUFLOOD, are currently crude and subject to very high uncertainty [14, 15]. There is an **urgent need to develop new commercial flood damage functions** that incorporate critical parameters like floor area, precautionary measures, and building quality, rather than relying on water depth alone [16, 17].
*   **Advancing 2D and Direct Rainfall Modelling:** While 2D direct rainfall modelling is becoming more viable, calibrating these applications when sub-surface flows and stores are represented remains an emerging area requiring ongoing benchmarking [18, 19]. Researchers also note a need to investigate whether standard structures (e.g., box culverts) can be effectively modelled using purely 2D solutions with sub-grid sampling (SGS) and quadtree meshes [20, 21]. 

### Climate Change & Uncertainty
*   **Merging Civil Engineering and Atmospheric Science:** A significant gap exists in understanding how rapid shifts in weather patterns (e.g., bomb cyclones, blizzards) interact with water's phase changes (ice/liquid) to overwhelm civil infrastructure [22, 23]. Researchers emphasize that **civil engineering and atmospheric science must proactively merge** to design infrastructure capable of withstanding the dynamic, multi-hazard extreme events amplified by climate change [24, 25].
*   **Moving Beyond the "Stationarity" Assumption:** As human activity heavily impacts the climate (the Anthropocene), the assumption that the "future will replicate the past" is obsolete [26, 27]. Future research must focus on "disturbance hydrology"—understanding how overlapping human activities, land-use changes, and climate tipping points cascade into irreversible new hydrologic states [28-31].
*   **Lake and Reservoir Stratification:** To understand how climate change will alter the mixing regimes of oligomictic lakes, researchers cite a critical lack of long-term, high-frequency observational data [32]. Future studies should deploy continuous water quality monitoring stations and simulate mixing scenarios using updated meteorological forcing data (like CMIP6) [33, 34].

### Urban Water Security & Water Quality
*   **Proactive Drainage Design and Policy:** Existing urban drainage networks are severely stressed, and current design standards lack guidance on assessing specific environmental flows under climate change, such as the 1.5-year ARI event [35-37]. The industry must move away from reactive upgrades toward proactive city-scale scenario planning, update pollutant generation rates, and expand stormwater harvesting skills [38-41].
*   **Cascade Water Supply Systems (CWSS):** Despite their historical importance, there is a profound lack of spatial and temporal water quality data regarding these interconnected tank systems [42-44]. Future research should investigate the causal factors of severe downstream nutrient accumulation, explore the risks of nitrification and denitrification at the sediment-water interface, and pilot low-cost biofiltration vegetation to improve water quality [45-48].
*   **Fish Passage Hydraulics:** There is currently limited scientific understanding of the specific hydraulic criteria required for acceptable fish passage through road culverts, and a lack of approved guidance on the necessary hydraulic assessment methodologies to support these ecosystem needs [49].
*   **Quantifying Pollutant Uncertainty:** Models predicting annual nutrient and sediment loads are subject to high uncertainty (± 30-55%). Further investigations are required into instream decay parameters, rainfall-runoff model structures, and high-flow event monitoring to improve the predictive confidence required for risk-based decision making [50-52]. 

### Data Science in Hydrology
*   **The "Black-Box" Limitation of AI:** While artificial intelligence and machine learning (ML) show great promise in handling large datasets for prediction, they currently lack inherent physics-based understanding [53, 54]. A key future challenge is **incorporating known physical mechanisms into ML architectures** so researchers can understand *why* a system behaves a certain way, rather than just predicting the output [53, 54].
*   **Data Scarcity and Dynamic Environments:** Data-driven ML requires vast amounts of observational data, making it impractical in areas with poor monitoring networks [55]. Furthermore, surrogate ML models map a static input-to-output relationship. If the underlying landscape changes due to urban development, the computationally heavy process of training the surrogate must start over, identifying a need for new methods to seamlessly update ML models in dynamic environments [56, 57].
*   **Operationalizing Early Warning Systems:** Emerging real-time flood forecasting systems (like the FliFS Proof of Concept) need further pilot studies focused on accuracy, robustness for handling gridded datasets, and the integration of these models into online GIS environments before they can be fully operationalized for emergency responders [58-60]. Additionally, flow peak tracking tools should be expanded to predict downstream river responses based on specific, categorized antecedent conditions [61].
---

**See Also:**
- [Conference Papers Home](index.md)
