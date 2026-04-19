# HWRS 2012 Mind Map

## Water Resources Management and Modelling

**Conference:** Hydrology & Water Resources Society 2012  
**Sources:** 145 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
Water Resources Management and Modelling
├── Hydraulic Models and Parameters
│   ├── Manning Roughness Coefficient (n)
│   │   ├── Estimation via Nikuradse Equivalent Sand-Roughness (ks)
│   │   ├── Keulegan relationship with Hydraulic Radius (R)
│   │   └── Chen Generalized Power-Law Model
│   └── Velocity Measurement Technologies
│       ├── Acoustic Doppler Current Profiler (ADCP)
│       ├── Stationary Method (ADCP-SM)
│       └── SonTek M9 Multi-band Acoustics
├── Design Flood Estimation Techniques
│   ├── Design Event Approach (DEA)
│   │   ├── Assumes AEP neutrality
│   │   └── Fixed inputs lead to probability bias
│   ├── Joint Probability Approach (JPA)
│   │   ├── Monte Carlo Simulation Technique (MCST)
│   │   ├── Accounts for rainfall duration, intensity, and losses
│   │   └── Regionalisation of rainfall temporal patterns
│   └── South African JPV Methodology
│       ├── Joint Peak-Volume relationship
│       ├── Peak-over-threshold (POT) analysis
│       └── Standardised observed flood hydrographs
├── Software and Systems
│   ├── eWater Source
│   │   ├── NetLP (Network Linear Programming) ordering
│   │   ├── Rules-based ordering
│   │   └── Catchment runoff modelling framework
│   └── Existing Tools
│       ├── REALM (Victoria, Australia)
│       ├── IQQM (NSW and Queensland, Australia)
│       ├── RORB runoff routing program
│       └── EPANet (Hydraulic simulation)
├── Water Supply and Demand Management
│   ├── Demand-Side Strategies
│   │   ├── Leakage detection and pressure reduction
│   │   ├── Effluent reuse and water recycling
│   │   └── Public awareness and billing improvement
│   └── System Optimization
│       ├── Minimization of pumping costs
│       └── Explicit vs. Implicit pump scheduling
└── Environmental and Specific Studies
    ├── Estuarine Wetlands (Hunter Estuary)
    │   ├── Mangrove vs. Saltmarsh dynamics
    │   ├── Tidal reinstatement effects
    │   └── Carbon sequestration rates
    └── Orographic Precipitation (Coffs Harbour)
        ├── Rainfall gradients and mountainous terrain
        ├── Wind direction correlation (Easterly winds)
        └── Hierarchical IFD modeling
```

---

## Main Themes

### 1. [Hydraulic Models and Parameters](hwrs-2012/hydraulic-models-and-parameters.md)
- Manning Roughness Coefficient (n)
- Velocity Measurement Technologies

### 2. [Design Flood Estimation Techniques](hwrs-2012/design-flood-estimation-techniques.md)
- Design Event Approach (DEA)
- Joint Probability Approach (JPA)
- South African JPV Methodology

### 3. [Software and Systems](hwrs-2012/software-and-systems.md)
- eWater Source
- Existing Tools

### 4. [Water Supply and Demand Management](hwrs-2012/water-supply-and-demand-management.md)
- Demand-Side Strategies
- System Optimization

### 5. [Environmental and Specific Studies](hwrs-2012/environmental-and-specific-studies.md)
- Estuarine Wetlands (Hunter Estuary)
- Orographic Precipitation (Coffs Harbour)

---

## Theme Detail Pages

- [Hydraulic Models and Parameters](hwrs-2012/hydraulic-models-and-parameters.md)
- [Design Flood Estimation Techniques](hwrs-2012/design-flood-estimation-techniques.md)
- [Software and Systems](hwrs-2012/software-and-systems.md)
- [Water Supply and Demand Management](hwrs-2012/water-supply-and-demand-management.md)
- [Environmental and Specific Studies](hwrs-2012/environmental-and-specific-studies.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
**Actionable Insights for Hydraulic Models and Parameters**
*   **Use caution with 2D depth-averaged numerical models in urban areas:** When modelling urban floodplains, do not assume 2D models will perfectly capture velocity distribution and cross-channel flow around buildings. Models should replicate the prototype building construction (e.g., slab-on-ground vs. piers) as closely as possible, because the specific construction type significantly alters local flood hazard, hydraulic jumps, and flow distribution [1], [2], [3]. 
*   **Estimate overland flow quickly without full drainage data:** If you lack the time or data to survey underground drainage assets for LGA-wide "rain-on-grid" modelling, you can simulate drainage capacity by subtracting the rainfall intensity of the drainage system's design ARI (e.g., 5-year ARI) from the major flood design ARI (e.g., 100-year ARI). Apply the standard temporal pattern to this net rainfall intensity to rapidly approximate overland flow extents [4], [5].
*   **Derive Manning’s *n* using ADCPs in natural channels:** In natural channels where hydrologic data is poor, you can estimate Manning's roughness coefficient (*n*) by using an Acoustic Doppler Current Profiler (ADCP) to measure vertical velocity profiles. You can then apply the universal logarithmic law and power-resistance formulas to estimate boundary shear velocity and Nikuradse's equivalent sand-roughness to back-calculate a more accurate *n* [6], [7].

**Actionable Insights for Design Flood Estimation Techniques**
*   **Transition from the Design Event Approach (DEA) to Monte Carlo Simulations:** The traditional DEA assumes "ARI neutrality" (that inputs like losses and temporal patterns represent a central tendency), which introduces significant bias. Instead, use the Monte Carlo Simulation Technique (MCST) or Joint Probability Approach to sample the probabilistic nature of inputs like initial/continuing losses and spatial/temporal rainfall patterns. This yields much more realistic design flood estimates [8], [9], [10], [11].
*   **Test multiple boundary scenarios for coastal flood models:** In coastal areas subject to simultaneous extreme rainfall and storm surge, do not rely on a static tailwater boundary. Instead, evaluate multiple alternatives (e.g., peak rainfall coinciding with peak ocean level, peak rainfall coinciding with peak normal tide, and combined probabilities) and adopt the worst-case scenario. When there is a high risk to life or property, apply a time-dependent rise and fall rather than a constant water level [12], [13], [14].
*   **Account for residual risks beyond the 1 in 100 AEP:** Do not base floodplain planning and infrastructure solely on a 1 in 100 AEP standard. Consider the hazards and forces associated with much rarer events (e.g., 1 in 2000 AEP) and apply tolerable risk limits commonly used in dam safety guidelines to better manage residual life-safety risks on floodplains [15], [16], [17]. 

**Actionable Insights for Software and Systems**
*   **Address Non-Hydrological Behaviours (NHB) using flexible conceptual models:** For real-time, event-based flood forecasting facing missing flow data, unknown transmission losses, or backwater/tidal impacts, complex 1D/2D hydraulic models are often too slow or data-intensive. Instead, use flexible conceptual models (like URBS) coupled with simple, physically realistic approaches such as tide-dependent rating curves and manual flow diversion/bypassing algorithms to quickly and effectively account for these anomalies [18], [19], [20].
*   **Calibrate hourly models using aggregated daily data:** It is inappropriate to transfer parameters from a model run at a daily time step to one run at a sub-daily (hourly) time step, as this will underestimate peak flows. If you lack historical sub-daily data for calibration, use hourly averaged daily rainfall to calibrate parameters suitable for running your hydrological model in hourly time steps [21], [22], [23].
*   **Select objective functions based on forecasting goals:** Be aware that a single objective function cannot provide good estimates for all streamflow characteristics. If you need accurate total streamflow simulations, use an objective function that gives more weight to high and medium flows. Calibrating specifically against low flows will improve low flow predictions, but at the direct expense of high flow simulation accuracy [24], [25].
*   **Correct mass balance errors in whole-of-river models:** When calibrating multi-gauged river systems, over-fitting to fix mass balance errors can degrade your model's hydrological integrity. The most effective ways to correct unaccounted differences between observed and simulated flows are to apply an unconstrained loss/gain function based on flow, or to apply a scaling factor to the rainfall-runoff model contributions and then apply a flow-based loss/gain function [26], [27], [28], [29]. 

**Actionable Insights for Water Supply and Demand Management**
*   **Adopt a risk management approach for flood storage pre-releases:** Do not rely on a "No Further Rainfall" assumption, which maximizes the danger of underestimating actual rainfall and overtopping. Base release decisions on the "most probable rainfall forecast" utilizing runoff routing models, and actively adjust operational releases by continuously monitoring actual vs. forecast rainfall [30], [31], [32], [33].
*   **Maintain long-term baselines for climate change planning:** When planning water resources, do not use short-term records (e.g., the past 15–20 years) as a new baseline, because it is difficult to isolate the climate change signal from high natural variability. Instead, use long records (100+ years) and interpret future GCM projections as a trend in the long-term mean rainfall or runoff, utilizing stochastic replicates for alternative time series [34], [35].

**Actionable Insights for Environmental and Specific Studies**
*   **Dynamically link groundwater data to rainfall-runoff parameters:** In catchments where baseflow is a significant component of streamflow and a decline in groundwater levels is observed, stationary conceptual models often fail. You can improve model performance by dynamically linking the maximum capacity of the routing store parameter (e.g., x3 in the GR4J model) to observed changes in the groundwater standing water level [36], [37], [38]. 
*   **Use simple GIS models for preliminary nutrient load tracking:** If your local council needs to assess the impact of land-use changes on stormwater nutrient loads (TN, TP), you can start with a simple GIS and Excel-based export rate model. This provides a sufficiently accurate initial magnitude assessment to identify priority areas for mitigation before investing in expensive, detailed continuous simulation models like eWater Source [39], [40].
*   **Standardise and monitor WSUD to reduce council liability:** Local councils acquiring millions of dollars of Water Sensitive Urban Design (WSUD) assets face substantial future liabilities if systems fail. Immediately standardise WSUD terminology, set up performance monitoring, safeguard devices during construction, and establish an incentive scheme to reward developers for proactive stormwater management [41], [42], [43].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes in this notebook are deeply interconnected, reflecting the shift in modern water resources management from isolated, single-discipline studies to integrated, whole-of-system approaches. The cross-cutting issues primarily revolve around the need to balance human consumptive demands with ecological health, manage the uncertainties introduced by climate change, and utilize advanced computational software to seamlessly link hydrology, hydraulics, and environmental science. 

Here are the primary cross-cutting issues and specific examples of interdisciplinary connections bridging these themes:

### 1. Bridging Software Systems with Complex Hydrology and Hydraulics
A major cross-cutting theme is the development and integration of software frameworks capable of simulating the full water cycle by coupling disparate **Hydraulic Models** and **Software and Systems**. Historically, groundwater, surface water, and hydraulic routing were modeled separately. 
*   **Coupling Surface and Groundwater:** Papers demonstrate how OpenMI technology successfully couples the powerful 3D subsurface capabilities of FEFLOW (groundwater) with the distributed surface and unsaturated zone models of MIKE SHE (surface water) [1, 2]. This allows researchers to study complex interactions like seawater intrusion in coastal aquifers under climate change scenarios [2, 3]. 
*   **Catchment-to-Estuary Integration:** Another prime example of bridging themes is the Hawkesbury-Nepean Water Quality Model, which connects eWater Source (a hydrological catchment model) with TUFLOW/FABM (an in-stream 1D/2D hydrodynamic and water quality model) to test wastewater servicing and land-use scenarios [4-6]. 
*   **Hydraulics for Hydrology:** Advanced 2D hydraulic engines are increasingly being used to solve hydrologic catchment responses. For example, the ANUGA software uses the Shallow Water Wave (SWW) equation on an unstructured finite-volume grid to simultaneously model rainfall-runoff (hydrology) and complex urban overland flow paths (hydraulics) [7-9]. 

### 2. Enhancing Design Flood Estimation with Hydrodynamic Inputs
**Design Flood Estimation Techniques** are heavily intertwined with **Hydraulic Models and Parameters** to account for the joint probability of concurrent flood-producing factors (such as rainfall, antecedent moisture, and storm surge). 
*   **Joint Probability in Coastal Floodplains:** In coastal areas, hydrologic models alone cannot resolve the complex interactions of tides and floodplain routing. To solve this, researchers applied a Monte Carlo hydrologic framework (RORB) to generate thousands of flood scenarios, and bridged this with a 2D hydraulic model by developing "look-up tables." These tables relate peak flows and tide levels to actual floodplain water levels, effectively embedding complex hydraulic behaviors into stochastic flood estimation [10-12]. 
*   **Model Parameterization Challenges:** When modeling urban floodplains using 2D hydraulics, the physical representation of parameters—such as modeling buildings as solid obstructions versus structures on piers—significantly alters the localized velocity, depth, and flood hazard [13, 14]. 

### 3. Trade-offs Between Water Supply, Demand, and Environmental Health
**Water Supply and Demand Management** intersects heavily with **Environmental Studies** through the concept of the "working river" and environmental portfolio management. With increasing volumes of water entitlements being purchased for the environment, managers use advanced **Software and Systems** to optimize these competing needs.
*   **Optimizing Environmental Water Portfolios:** Decision-support optimization models are used to determine when to carry over, trade, or release environmental water [15-17]. For instance, a conceptual framework explicitly links River System Models with Ecological Response Models (ERMs) to evaluate how Environmental Water Requirements (EWRs) can be met under varying climatic conditions without compromising human users [18-20]. 
*   **Configuring Consumptive Flows for Ecology:** The MacKenzie River case study investigates how transfers of water intended for human consumption can be specifically timed and configured as "pulses" or "freshes" to maximize the health of aquatic ecosystems (monitored via algal/diatom responses), successfully bridging supply management with ecological outcomes [21-23].
*   **Multi-Objective Optimisation:** Using the Elitist Non-dominated Sorting Algorithm (NSGA-II) combined with the REALM simulation engine, researchers demonstrated that the reliability of environmental flows in the Wimmera-Mallee system could be vastly improved simply by optimizing the operating rules, without reducing the reliability of supply for consumptive users [24-26].

### 4. Climate Change, Non-Stationarity, and Adaptive Management
Addressing climate change creates a massive interdisciplinary bridge across **Environmental Studies**, **Flood Estimation**, and **Water Supply Management**. Models calibrated on historical data may no longer be valid if catchment dynamics shift outside the envelope of natural variability.
*   **Non-Stationary Hydrology:** Studies show that long-term droughts (like the Millennium Drought) fundamentally alter groundwater levels and rainfall-runoff relationships. Researchers are exploring how incorporating groundwater data into conceptual rainfall-runoff models can help capture this "non-stationarity" over time [27-29].
*   **Predicting Future Water Quality:** Climate change directly impacts reservoir hydrodynamics and ecology. Using 3D hydrodynamic models on Lake Mead, researchers assessed how decreased inflows and increased air temperatures might alter salinity, algae blooms, and nutrient distribution, combining environmental limnology with hydraulic modeling to secure future urban water supplies [30-32]. 
*   **Dynamic Dam Management:** Recent models investigate the trade-off between keeping reservoirs full for water security versus lowering temporary full supply levels (FSL) during the wet season for flood mitigation. Using eWater Source, studies on the Wivenhoe Dam highlight the delicate balance between preventing downstream flood damage and ensuring long-term urban supply security under changing seasonal forecasts [33-35].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
**Hydraulic Models and Parameters**
*   Flood emergency response tools need to integrate **catchment variability** (including spatial and temporal rainfall patterns, rainfall intensity, and antecedent conditions) and interactive predictions, which are currently noted as being beyond the scope of existing 2D models [1].
*   In the regional modeling of coal seam gas extraction, there is a gap regarding **how near-source hydraulic properties should be upscaled** to reflect complex coal and interburden relationships, and whether establishing a head versus saturation relationship in a single-phase model can adequately replace explicit two-phase flow simulation [2, 3].
*   Two-dimensional (2D) depth-averaged numerical models often fail to replicate complex 3D surface behaviors (like hydraulic jumps); thus, **further study is required on how floodplain obstacles, such as fences and cars, impact local flood hazard conditions** [4, 5].
*   Using the universal logarithmic law to estimate shear velocity and Manning's roughness introduces substantial uncertainties, highlighting a need for methodologies to **better approximate the uncertainty in roughness estimates** derived from vertical velocity profiles [6, 7].
*   In evaluating river reach loss and gain accounting, future investigations need to **target specific environments (e.g., highly regulated rivers, or areas with high groundwater and floodplain interaction)** to understand why certain reaches perform poorly during validation and to develop robust combinations of accounting methods [8, 9].
*   When using groundwater data to inform time-varying conceptual rainfall-runoff models, **further investigation is needed to determine which parameters are best informed by groundwater levels** and whether time-varying parameters are even necessary if a system reaches a new stable baseline state [10, 11].

**Design Flood Estimation Techniques**
*   The Monte Carlo Simulation Technique (MCST) for flood estimation needs to be tested on **larger, ungauged catchment datasets** to evaluate the applicability of various derived regional input variables [12].
*   Current joint probability frameworks for coastal tailwater conditions require testing with **hydraulic models using lower flows and varying tide levels** to properly verify lookup tables. Furthermore, research needs to be extended to investigate **storm surge-dominated events** and the independence of spatial and temporal rainfall patterns [13-16].
*   When assessing rare flood hazards, overcoming the **challenges associated with estimating flood probabilities from short periods of record** remains a significant hurdle [17]. 
*   The assumption of Average Recurrence Interval (ARI) neutrality in the design event approach introduces significant uncertainties. This necessitates **further research on input variability (such as temporal patterns and losses) across a greater number of catchments** [18, 19].
*   The **impact of non-stationarity** on the selection of probability distributions for flood frequency analysis requires further investigation, as historical assumptions of stationarity may no longer hold true [20].

**Software and Systems**
*   A significant amount of research is needed before the **new science of decadal prediction** can accurately forecast rainfall and runoff several years or decades ahead to meaningfully guide water resources planning [21].
*   For the eWater Source platform, researchers noted the need for **flexible user-defined objective functions to improve high and low flow calibration** [22]. Furthermore, integration with tools like the BoM Geofabric and AWAP products is needed, along with capabilities to **incorporate the impacts of bushfire vegetation regrowth and surface-groundwater interactions** [23]. Current software versions also suffer from limited portability and difficulties in conducting dynamic "What-if" scenario analyses [24].
*   In complex coupled models (like MIKE SHE/FEFLOW or MIKE URBAN), gaps include a need for **improved functionality for troubleshooting coupling issues**, separate flow regulations for incoming and outgoing flows, and expanded applications to address **saltwater intrusion** and climate change in coastal aquifers [25, 26].
*   When modeling environmental water portfolios via optimization, the objective functions need refinement to properly **represent sub-optimal wet and detrimental wet conditions**, and models must be tested in real catchments to ensure computational run times are not prohibitive [27].

**Water Supply and Demand Management**
*   A fundamental barrier to climate adaptation is the **disconnect between climate science capability and the needs of water resource decision-makers**. This is exacerbated by uncertainty in precipitation projections, a lack of effective communication, and an absence of decision-making tools to translate scientific uncertainty into manageable risk [28-30].
*   In assessing farm dam impacts, high uncertainty in current regionalization equations requires future work to **digitize farm dams from aerial imagery, increase the sample size for surface-area-to-volume relationships, and conduct larger surveys and metering to improve demand factor estimates** [31-33].
*   Current modeling of non-residential urban water use is limited; future work should **extend modeling to other non-residential user groups** (beyond schools and industry), assess predictions over longer periods, and test the inclusion of climatic variables (temperature, rainfall) to improve model accuracy [34].
*   For Water Sensitive Urban Design (WSUD), significant knowledge gaps exist between research and practical application, primarily driven by a **lack of performance monitoring and limited maintenance budgets** [35, 36].

**Environmental and Specific Studies**
*   In 2D hydrologic response modeling, there is a **lack of valid physical descriptions for extremely high Manning's N values (e.g., 10 or 20)**, raising questions about the appropriateness of using such values to manipulate and calibrate overland flow models [37].
*   To better project sub-daily rainfall patterns in a future climate, algorithms need to **incorporate additional atmospheric covariates (beyond just atmospheric temperature)** and couple disaggregation algorithms with daily downscaling models [38, 39].
*   When conducting qualitative model predictive error analysis for groundwater, the methodology needs to be tested on **more complex, "real-world" models**, as current simplifications (like rigid zones of parameter uniformity) may be ineffective for fate and transport modeling that is highly sensitive to small-scale heterogeneities [40].
*   For reservoir water quality modeling (e.g., Lake Mead) under climate change scenarios, future studies need to evaluate **other meteorological changes (wind speed, relative humidity, cloud cover) and hydrological shifts (storm runoff, inflow turbidity)**, as well as model the dynamics of multiple algae groups [41, 42].
*   Following events like the Christchurch earthquakes, comprehensive flood hazard planning is delayed by **uncertainties surrounding the future of "red-zoned" land and required levels of service** across varying climate change and sea-level rise scenarios [43].
---

**See Also:**
- [Conference Papers Home](index.md)
