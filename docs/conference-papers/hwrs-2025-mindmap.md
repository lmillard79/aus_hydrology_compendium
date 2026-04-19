# HWRS 2025 Mind Map

## HWRS 2025: Hydrology and Water Resources Research

**Conference:** Hydrology & Water Resources Society 2025  
**Sources:** 129 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
HWRS 2025: Hydrology and Water Resources Research
├── Flood Modelling and Forecasting
│   ├── Calibration Metrics
│   │   ├── Relative Peak Flow Error (RPFE)
│   │   ├── Nash-Sutcliffe Efficiency (NSE)
│   │   ├── Kling-Gupta Efficiency (KGE)
│   │   └── Relative Volume Error (RVE)
│   ├── AI and Machine Learning
│   │   ├── Long Short-Term Memory (LSTM)
│   │   ├── Artificial Neural Networks (ANN)
│   │   └── Monte Carlo Dropout for Uncertainty
│   ├── Regional Analysis
│   │   ├── Index Flood Method (IFM)
│   │   ├── Quantile Regression
│   │   └── Log-Pearson Type 3 (LP3)
│   └── Inundation Mapping
│       ├── Height Above Nearest Drainage (HAND)
│       ├── CaMa-Flood Hydrodynamic Model
│       └── Satellite-based Surface Water Extent
├── Climate Change and Variability
│   ├── Climate Projections
│   │   ├── CMIP6 Global Climate Models
│   │   ├── Pattern Scaling Framework
│   │   └── Internal Variability vs Model Uncertainty
│   ├── Climate Drivers
│   │   ├── El Niño-Southern Oscillation (ENSO)
│   │   ├── La Niña Rainfall Phases
│   │   └── Millennium Drought
│   └── Impacts
│       ├── Declining Cool Season Rainfall
│       ├── Increased Sea Level Rise
│       └── Coastal Floodplain Waterlogging
├── Water Resource Management
│   ├── Catchment Processes
│   │   ├── Budyko Framework (Water-Energy Balance)
│   │   ├── Initial Loss-Continuing Loss (IL-CL)
│   │   └── Groundwater Extraction by Plantations
│   ├── Infrastructure and Governance
│   │   ├── Runoff Dam Inventories
│   │   ├── Reservoir Sizing (Source vs WATHNET)
│   │   ├── Murray-Darling Basin Plan
│   │   └── Farm Modernisation (ISO 55000)
│   └── Innovative Solutions
│       ├── Blue Carbon Wetland Restoration
│       ├── Managed Aquifer Recharge (MAR)
│       └── Nature-based Solutions
└── Community and Social Factors
    ├── Citizen Science (The People's Catchment)
    ├── Flood Sentinel Networks
    ├── First Nations Water Governance
    ├── Public-Private Partnerships (PPP)
    └── UHF/CB Radio Communication
```

---

## Main Themes

### 1. [Flood Modelling and Forecasting](hwrs-2025/flood-modelling-and-forecasting.md)
- Calibration Metrics
- AI and Machine Learning
- Regional Analysis
- Inundation Mapping

### 2. [Climate Change and Variability](hwrs-2025/climate-change-and-variability.md)
- Climate Projections
- Climate Drivers
- Impacts

### 3. [Water Resource Management](hwrs-2025/water-resource-management.md)
- Catchment Processes
- Infrastructure and Governance
- Innovative Solutions

### 4. [Community and Social Factors](hwrs-2025/community-and-social-factors.md)
- Citizen Science (The People's Catchment)
- Flood Sentinel Networks
- First Nations Water Governance
- Public-Private Partnerships (PPP)

---

## Theme Detail Pages

- [Flood Modelling and Forecasting](hwrs-2025/flood-modelling-and-forecasting.md)
- [Climate Change and Variability](hwrs-2025/climate-change-and-variability.md)
- [Water Resource Management](hwrs-2025/water-resource-management.md)
- [Community and Social Factors](hwrs-2025/community-and-social-factors.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
**Flood Modelling and Forecasting**

*   **Address Rating Curve Extrapolation Risks:** Historic discharges in Australian hydrologic datasets (like the Hydrologic Reference Stations) often rely on extreme rating curve extrapolation, with over 60% of 1:100 AEP events involving significant extrapolation [1, 2]. Practitioners should calculate the extrapolation ratio before model calibration; if the 1:100 AEP ratio is greater than 3, apply mitigation procedures such as adopting upper and lower confidence band hydrographs during calibration [2, 3].
*   **Select Fit-for-Purpose Calibration Metrics:** When calibrating models for urban design flood estimation (e.g., using continuous simulation to inform Flood Frequency Analysis), prioritize calibration metrics that emphasize peak flow accuracy, such as the Relative Peak Flow Error (RPFE). Complex metrics like the Nash-Sutcliffe Efficiency (NSE) or Kling-Gupta Efficiency (KGE), which focus heavily on volume, can lead to poorer performance in capturing the critical peak flow data needed for design [4-6]. 
*   **Incorporate Pre-Burst Rainfall for Volume-Driven Systems:** In dam catchments or systems sensitive to flood volume, ignoring excess pre-burst rainfall can lead to underestimated design flood estimates. Practitioners should extract pre-burst temporal patterns from local pluviograph data and sample them dynamically in Monte Carlo simulations, avoiding "simple" pre-burst subtraction methods [7-9].
*   **Refine Dam Antecedent Storage Assumptions:** When assessing maximum lake levels for dam safety, do not rely on simplistic daily volume percentiles or full supply volumes to set antecedent conditions. Instead, extract storage volumes *prior* to historical flood-producing storms to generate realistic antecedent storage probability curves. This prevents the underestimation of extreme lake levels during rare design events [10-13]. 

**Climate Change and Variability**

*   **Fast-Track Climate Adjustments in Legacy Models:** To efficiently prioritize portfolio updates under the new ARR 2019 v4.2 climate guidance, avoid full hydrologic-hydraulic model rebuilds. Instead, re-run existing fast-processing hydrologic models (e.g., RORB) using a matrix of decoupled climate inputs (varying rainfall depths and loss rates) and translate the resulting peak flows to water levels using existing rating curves from the hydraulic models. This "bottom-up" approach rapidly identifies locations most sensitive to climate thresholds [14-16].
*   **Adopt Scenario and Sensitivity Testing Early:** The shift to Shared Socioeconomic Pathways (SSPs) in ARR v4.2 can drastically increase infrastructure sizing requirements (e.g., up to a 56% increase in detention basin volumes under SSP5-8.5). Practitioners must integrate these scenarios into early planning to avoid costly redesigns [17-19]. Consider testing against a defined temperature-rise trajectory rather than getting paralyzed by SSP scenario selection [20, 21].
*   **Use Localized Data Over Generalized Multipliers:** Generalized scaling rates for rainfall intensity increases may not apply reliably across varying local topography and weather patterns. Where possible, utilize localized analysis of temperature and rainfall intensity relationships to avoid overestimating or underestimating local climate change impacts [22, 23]. Similarly, for coastal flood planning, utilize local Bayesian trend analyses for sea-level rise rather than relying strictly on superseded, uncalibrated global models (e.g., older IPCC projections) to avoid undue pressure on housing and planning constraints [24-26].
*   **Adjust Hydroclimate Reference Periods:** Be aware of non-stationarity in recent decades. When assessing long-term water availability, explicitly distinguish the climate of recent decades (e.g., post-1997 or post-1975) from early-20th-century data. Incorporating recent wet years (2020-2023) can increase yield estimates, but drier systems or those with multi-year storages remain highly sensitive to baseline choices [27-29].

**Water Resource Management**

*   **Design Catchment-Wide Nature-Based Solutions (NbS):** Isolated urban interventions are insufficient for riverine flood mitigation. Adopt a "spongy catchment" approach by placing specific NbS where they are most geomorphologically effective: 
    *   *Upstream*: Use afforestation, grassland management, and soil conservation to maximize infiltration and detain water [30, 31].
    *   *Midstream*: Utilize wetlands, riparian revegetation, and leaky barriers to attenuate peak flows and increase flow resistance [30, 32].
    *   *Downstream*: Reconnect floodplains and reactivate palaeochannels to divert and convey floodwaters away from vulnerable areas [33, 34].
*   **Adjust Hydraulic Roughness for Revegetation:** When utilizing NbS or riparian restoration, hydrologic models must be updated to account for increased hydraulic roughness. Areas rezoned for development without accounting for the elevated flood planning levels associated with riparian revegetation will be vulnerable to flood impacts [35-37].
*   **Use High-Resolution Models for NbS Validation:** Do not rely exclusively on semi-distributed hydrological models to simulate the flood-attenuation effects of NbS, as they can underestimate peak reduction by up to 30%. Employ high-resolution hydrodynamic models (like Rain-on-Grid) for final design validation to accurately capture localized depth, velocity, and inundation extents [38-40].

**Community and Social Factors**

*   **Simplify and Standardize Risk Communication:** Current flood planning materials are overly complex and lack actionable guidance. Planners should clearly define specific flood types (e.g., flash, riverine, overland) in lay terms and provide explicit, instructional guidance on what property owners should do to manage these specific risks [41-43]. 
*   **Leverage Citizen Science for Flood Intelligence:** Establish and support community-led "Flood Sentinel" networks to monitor rainfall and streamflow, particularly in small-to-moderate rural catchments where rapid-onset floods (6–48 hours) outpace official BOM warning systems. Integrate this local, quality-controlled data into official forecasting workflows to drastically improve early warning lead times [44-46]. Furthermore, prioritize resilient communication infrastructure (like UHF/CB radios) that functions during power and network outages [47].
*   **Shift from Flood Avoidance to Flood Resilience Policies:** Eliminate the assumption that future flood hazards must be completely avoided through extreme, conservative planning overlays, which generate severe economic burdens and insurance costs for communities. Transition to resilience-based governance by applying Pareto Optimum and Kaldor-Hicks criteria, focusing on adaptive community capacity and infrastructure rather than attempting to enforce zero background risk [48-51]. 
*   **Engage Youth in Water Policy:** The Murray-Darling Basin and other regional areas face an aging demographic and youth out-migration. Water managers must move away from traditional engagement and actively involve young people via grassroots, peer-led research and community initiatives where they already gather, ensuring long-term capacity building for future water governance [52-54].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes presented at the HWRS 2025 symposium are deeply interconnected, reflecting a paradigm shift in hydrology from isolated technical disciplines to integrated, socio-ecological systems thinking. The overarching cross-cutting issue is the need to build resilience against a non-stationary climate by combining advanced modelling with inclusive community governance. 

Here is a comprehensive breakdown of how these themes connect, including specific papers that bridge these disciplines:

**1. The Intersection of Climate Change and Flood Modelling**
A major cross-cutting issue is the obsolescence of traditional, stationary flood models in the face of a changing climate. Researchers are bridging **Climate Change and Variability** with **Flood Modelling** by updating design guidelines and forecasting tools to account for shifting rainfall patterns and extreme weather.
*   **Integrating new climate guidelines into flood design:** Paper 20 assesses the real-world impacts of the newly updated Australian Rainfall and Runoff (ARR2019 v4.2) climate change guidelines, demonstrating how adopting Shared Socioeconomic Pathway (SSP) scenarios significantly increases detention basin volume requirements and design flows for urban infrastructure [1, 2]. Paper 148 similarly explores these ARR2019 v4.2 climate impacts on the stormwater management of large-scale solar farms [3, 4]. 
*   **Isolating climate drivers in flood models:** Paper 124 explores the causal influence of specific climate impacts on hydrology, using controlled experiments to isolate how changes in rainfall totals, seasonality, and extreme daily rainfall individually affect streamflow and flood modelling [5, 6]. 
*   **Long-range forecasting:** Paper 132 bridges seasonal climate prediction systems (ACCESS-S2) with hydrological models (AWRA-L) to develop a prototype for long-range, multi-month flood inundation forecasting in Australia [7, 8].

**2. Bridging Flood Forecasting with Community and Social Factors**
Technical flood data is only useful if it is understood and utilized by the people affected. A strong interdisciplinary connection is emerging between **Flood Modelling** and **Community/Social Factors**, emphasizing that effective disaster risk management requires citizen participation and clear risk communication.
*   **Citizen Science for Flood Intelligence:** Paper 92, "The People’s Catchment," establishes community-led flood intelligence networks where local residents (Flood Sentinels) collect and share rainfall and streamflow data, bridging the gap in rural areas where official monitoring infrastructure is lacking [9-11].
*   **Visualizing uncertainty for emergency responders:** Paper 140 bridges advanced machine learning (LSTM models for flood forecasting) with social utility by designing schematic visualisations to effectively communicate forecast uncertainty, peak heights, and timing to the NSW State Emergency Service [12, 13].
*   **Risk communication and equity:** Paper 5 investigates how local governments communicate flood risks in property planning, highlighting the need to translate technical hazard information into clear guidance for lay audiences [14, 15]. Furthermore, Paper 31 argues that relying purely on traditional hydrology models without assessing the socio-economic impacts on household welfare creates inequitable flood risk governance [16, 17].

**3. Water Resource Management under Climate Uncertainty**
The connection between **Water Resource Management** and **Climate Change** is driven by the urgent need to secure water supplies as droughts become more frequent and evaporation rates rise.
*   **Adapting baselines for water availability:** Paper 143 investigates how altering the historical climate reference period (e.g., post-1975 vs. post-1997) to account for recent climate non-stationarity impacts the assessment of water availability and yield in Victoria [18, 19].
*   **Regional climate projections:** Paper 32 synthesises CMIP6 climate projections to assess future regional water availability in the Murray Darling Basin, partitioning the uncertainty of runoff declines caused by higher potential evapotranspiration and reduced winter rainfall [20-22].
*   **Embracing "Deep Uncertainty":** Paper 156 argues that the traditional paradigm of water resource management is obsolete in a post-truth world facing climate change, advocating for a transition toward "scenario thinking" to navigate deep epistemic uncertainties [23, 24].

**4. Socio-Ecological Governance in Water Management**
The interplay between **Water Resource Management** and **Community/Social Factors** highlights that water allocation is a deeply human and political issue, requiring diverse stakeholder engagement and the integration of Indigenous knowledge.
*   **Human rights and First Law:** Paper 103 applies a human rights-based approach to Australia's new national water agreement, bridging hydrology with Indigenous First Law. It reframes human rights to recognize the deep connections between people, water, Country, and climate in the Kimberley region [25-27].
*   **Youth engagement in policy:** Paper 117 addresses demographic shifts in the Murray-Darling Basin, noting that traditional forms of participatory water management must evolve to include youth voices and grassroots movements to tackle future climate challenges [28, 29].
*   **Communicating environmental needs:** Paper 161 bridges complex eco-hydrological science with public engagement by developing targeted communication materials to explain the benefits of environmental water recovery in the competitive water market of the Yarra and Werribee rivers [30-32].

**5. The Ultimate Intersection: Nature-Based Solutions (NbS)**
**Nature-based Solutions (NbS) act as the nexus connecting all four themes.** NbS (such as restoring wetlands, reconnecting floodplains, and riparian revegetation) are used to manage water resources, adapt to climate change, mitigate floods, and require heavy social buy-in.
*   **Flood Modelling of NbS:** Paper 15 addresses the computational challenges and uncertainties of using Rain-on-Grid hydrodynamic models to capture the micro-scale flood attenuation effects of NbS interventions [33, 34]. 
*   **Water Quality and Flooding:** Paper 91 demonstrates that strategies designed to "slow the waters" for flood mitigation concurrently improve water quality by trapping nutrients and sediments [35, 36].
*   **Social Licence for NbS:** Paper 150 explicitly bridges the technical and social divide by examining the "social licence to operate" for NbS in Ipswich. It concludes that the adoption of nature-based flood mitigation is constrained not just by technical feasibility, but by competing development priorities, market forces, and the need for boundary-spanning community partnerships [37-39].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
**Flood Modelling and Forecasting**
*   **Advanced Hydraulic and Hydrologic Modelling:** There is a critical need for methodological advancements to adapt and refine automated calibration techniques for hydrodynamic models, especially when assessing Nature-based Solutions (NbS) [1]. Furthermore, simulating bridge flows remains a complex challenge, and significant work is required to improve the accuracy and confidence of representing bridges in 2D floodplain models [2].
*   **Data Quality and Parameter Uncertainty:** The evaluation of rating curves is severely hindered by a lack of streamflow gaugings. Addressing this requires the development of consistent data-sharing frameworks and transparent data custodianship protocols at the basin scale [3, 4]. In dam failure assessments, breach formation remains a massive source of uncertainty; future work should supplement empirical models with feasibility checks, sensitivity analysis, and probabilistic methods [5, 6]. Additionally, evaluating the lifecycle of Water Sensitive Urban Design (WSUD) assets requires field investigations and sensitivity analyses on variable inputs (e.g., cement compositions, retaining wall designs) and future rainfall variations [7].
*   **Forecasting Enhancements:** To improve AI-based seasonal streamflow forecasting, researchers recommend integrating multiple climate indices (such as the Pacific Decadal Oscillation), developing hybrid physics-informed models, and applying transfer learning for data-scarce regions [8, 9]. Long-range flood inundation outlooks need improved spatial accuracy, which could be achieved by integrating hydrodynamic outputs, machine learning corrections, and near-real-time remote sensing data (e.g., Sentinel satellites) [10]. Finally, global routing models like CaMa-Flood can be improved for regional simulations by implementing the Australian Hydrological Geospatial Fabric to better define river widths and bank heights [11].

**Climate Change and Variability**
*   **Climate Scenarios and Downscaling:** A deeper understanding of the temporal and climatic structures of datasets is essential to improve the reliability of machine learning applications in climate downscaling [12]. Furthermore, the non-linear relationship between global temperature trajectories and rainfall intensities introduces highly asymmetric risks; regulatory bodies need clearer, risk-based pathways or pre-defined temperature trajectories to help select appropriate Shared Socioeconomic Pathway (SSP) scenarios [13-15].
*   **Systemic Hydroclimatic Impacts:** The impacts of sea-level rise on estuarine salinity dynamics are subject to high uncertainty. Future studies should use probabilistic or Monte Carlo approaches, coupled with enhanced data collection both upstream and downstream of tidal limits, to assess shifting hydrological regimes [16-18]. When analyzing the influence of the El Niño-Southern Oscillation (ENSO) on flood flows, further analysis must incorporate the strength of the ENSO phase (using the new relative Niño index) and expand investigations across more catchments to verify regional trends [19].

**Water Resource Management**
*   **Demand and Supply Modeling:** Improving irrigation demand models requires integrating remote sensing to capture real-time crop area data and implementing conceptual improvements to differentiate the behavior of individual irrigators within a district [20, 21]. Assessing future water security vulnerabilities should incorporate the latest stochastic climate inputs, extend modelling periods, and apply sensitivity analysis to test the robustness of vulnerability indices [22].
*   **Catchment and Urban Water Balances:** Evaluating the net urban water balance in the Murray-Darling Basin faces significant data uncertainties; further analysis is required to obtain reliable data on land use changes, impervious surface growth, and wastewater production [23]. To reduce uncertainty in total runoff volume estimations, future field efforts should target direct measurements of the largest farm dams in catchments [24]. Additionally, future research must prioritize climate-specific water use models and long-term monitoring networks to manage groundwater extraction by plantation forestry under changing climates [25].
*   **Nature-Based Solutions (NbS) and Emerging Technology:** There is currently a lack of quantified information on incorporating NbS to increase flood resilience; future work will provide critical reviews of hydrodynamic tools, economic methods, and co-benefit quantification [26, 27]. On the technological front, realizing the potential of quantum innovations (like quantum sensing and post-quantum cryptography) for water systems demands a forward-looking agenda to develop, launch, and evaluate collaborative pilot projects [28].

**Community and Social Factors**
*   **Flood Risk Communication:** The quality and translation of flood planning information for lay audiences remain inadequate. Future studies must work with planners, hydrologists, and community members to evaluate how flood risk materials are perceived, understood, and applied in decision-making [29]. 
*   **Citizen Science and Community Resilience:** Pilot projects utilizing citizen science (e.g., The People's Catchment) highlight the need for further research to refine community-led flood intelligence models. Key future directions include establishing data-sharing protocols with official agencies (like the SES and BoM), developing co-produced flood information systems, and implementing training programs for local volunteers in data analysis and emergency response [30-32].
*   **Cross-Border Governance:** Transboundary water governance faces institutional lock-in and inertia. Future research is recommended to examine political willingness to craft adaptive institutions and transcend existing structures to create anticipatory systems [33]. Analytical typologies should be enhanced to track the dynamics of governance structures over time, with a specific focus on the role of crises and the impact of emerging technological surveillance platforms on cross-boundary water intelligence [34].
---

**See Also:**
- [Conference Papers Home](index.md)
