# HWRS 2024 Mind Map

## HWRS 2024 Research Highlights

**Conference:** Hydrology & Water Resources Society 2024  
**Sources:** 161 papers  
**Generated:** April 2026

---

## Mind Map Structure

```
HWRS 2024 Research Highlights
├── Extreme Flood Events
│   ├── February 2022 Flood
│   │   ├── Intensity: NE NSW and SE QLD
│   │   ├── Record specific peak flow
│   │   ├── Impact: 1% AEP design levels
│   │   └── Conditions: High antecedent soil moisture
│   └── Flood Management Insights
│       ├── Importance of initial conditions
│       ├── Reduced propagation times
│       └── Multi-peak hydrograph complexity
├── Renewable Energy Infrastructure
│   ├── Modelling Challenges
│   │   ├── Data scarcity in remote areas
│   │   ├── Computational costs for large catchments
│   │   └── High-risk electrical asset protection
│   └── Technical Solutions
│       ├── TUFLOW Sub-Grid Sampling (SGS)
│       ├── High-resolution (HR) raster mapping
│       └── Integrated hydrological models (RORB)
├── Stormwater & Dam Analytics
│   ├── Target Flow Control Systems (TFCS)
│   │   ├── Calibration-free reactive control
│   │   ├── Applied to multiple storages
│   │   └── Uses real-time level sensors
│   └── Breach Hydro Framework
│       ├── Rapid dam break analytics
│       ├── Probabilistic water balance modelling
│       └── Validation against HEC-RAS
└── Climate Change & Hydrology
    ├── Murray-Darling Basin Study
    │   ├── 1895-2023 instrumental baseline
    │   ├── Projected runoff reduction
    │   └── Impact of Hadley cell expansion
    ├── Joint Probability Analysis
    │   ├── Bivariate normal distribution
    │   ├── Box-Cox data transformations
    │   └── Riverine and tidal interactions
    └── Design Temperature (TDF)
        ├── Temperature-Duration-Frequency curves
        ├── GEV distribution analysis
        └── Non-stationary climate covariates
```

---

## Main Themes

### 1. [Extreme Flood Events](hwrs-2024/extreme-flood-events.md)
- February 2022 Flood
- Flood Management Insights

### 2. [Renewable Energy Infrastructure](hwrs-2024/renewable-energy-infrastructure.md)
- Modelling Challenges
- Technical Solutions

### 3. [Stormwater & Dam Analytics](hwrs-2024/stormwater-dam-analytics.md)
- Target Flow Control Systems (TFCS)
- Breach Hydro Framework

### 4. [Climate Change & Hydrology](hwrs-2024/climate-change-hydrology.md)
- Murray-Darling Basin Study
- Joint Probability Analysis
- Design Temperature (TDF)

---

## Theme Detail Pages

- [Extreme Flood Events](hwrs-2024/extreme-flood-events.md)
- [Renewable Energy Infrastructure](hwrs-2024/renewable-energy-infrastructure.md)
- [Stormwater & Dam Analytics](hwrs-2024/stormwater-dam-analytics.md)
- [Climate Change & Hydrology](hwrs-2024/climate-change-hydrology.md)
---

## Practitioner Insights

*Key recommendations for floodplain managers, hydrologists, and water resources professionals.*

RESPONSE:
**Extreme Flood Events**
*   **Update lifetime flood exposure calculations:** Stop using the traditional binomial distribution to calculate lifetime exposure risk. Because design rainfalls and flood probabilities increase over time due to climate change, the binomial theorem is no longer valid. **Practitioners should use the Poisson binomial formula** to account for changing probabilities year-on-year [1-3].
*   **Reconsider "zero afflux" criteria:** Strict zero afflux requirements can hinder sustainable development. **Move toward holistic, risk-based approval frameworks using Annual Average Damage (AAD)**. Approval authorities should tolerate minor residual afflux if the development provides a net community benefit and negative impacts on individuals are appropriately mitigated [4, 5]. 
*   **Report design exceedance probabilities:** Because of natural variability, there is a non-zero probability that design criteria will be exceeded even during events at design immunity levels. **Include measures of possible design exceedances (even simple exceedance counts) in engineering reports** rather than relying exclusively on mean or median peak flows, communicating this uncertainty clearly to decision-makers [6, 7].
*   **Refine coincident rainfall estimation for dam failures:** Avoid relying solely on simple bivariate log-normal methods to estimate coincident rainfall for dam failure consequence assessments. **Adopt storm space-time patterns and incorporate coincident rainfall variability**, as the relationship between coincident flows and potential loss of life (PLL) is highly non-linear, and median estimates alone are inadequate [8-10].
*   **Assess nonlinearity in extreme events:** Do not assume a fixed nonlinearity parameter (e.g., $m=0.8$) across all event frequencies. The hydraulic behavior of catchments changes from frequent to extreme events. **Use a full spectrum of calibration and couple hydrological models with 2D hydraulic routing tools (like TUFLOW)** for large catchments [11-13].

**Renewable Energy Infrastructure**
*   **Optimize models for large, data-poor catchments:** Renewable projects (solar and wind farms) are often located in remote areas with massive upstream catchments and scarce terrain data. **Leverage sub-grid sampling and high-resolution mapping in TUFLOW** to mitigate inaccurate spatial data and reduce the heavy computational costs of running multiple Annual Exceedance Probabilities (AEPs) over large domains [14-16]. 
*   **Address structural and electrical vulnerabilities:** Acknowledge that the dispersed nature of renewable assets requires evaluating different AEPs for erosion, trafficability, and freeboard [15]. **Pay critical attention to electrical assets (BESS, switchyards, inverters)** where flood inundation can cause catastrophic equipment failure, cooling system disruption, and prolonged operational downtime [17]. If data on upstream farm dams is unavailable, conservatively model them at maximum capacity [15].

**Stormwater & Dam Analytics**
*   **Implement Adaptive Target Hydrograph Control (ATHC):** To avoid expensive stormwater infrastructure pipe upgrades, **retrofit existing stormwater storages with smart, real-time orifice controls**. The ATHC method adjusts outflows in real-time based purely on storage volumes, successfully matching pre-development hydrographs and adapting dynamically to 40-95% increases in peak inflows driven by climate and land-use changes [18-20].
*   **Adopt rapid water-balance tools for dam breach analytics:** Traditional hydrodynamic models are often too slow and unstable for extensive dam break uncertainty analysis. **Use rapid probabilistic water-balance models (like Breach Hydro) to run tens of thousands of simulations quickly**, allowing you to thoroughly quantify parameter uncertainty (breach width, time, peak flow) and cross-validate against historical failure data [21-24].
*   **Transition to ensemble inflow forecasting:** Hydropower and reservoir operators should move from deterministic ("single truth") forecasts to ensemble forecasts (e.g., providing 200 possible traces). This provides vital insights into the likelihood of extremes for dam safety and trading. **Invest heavily in stakeholder training** so end-users understand how to interpret medians and percentiles [25-27].

**Climate Change & Hydrology**
*   **Shift climate change from a "sensitivity test" to a policy driver:** Industry practice must stop treating climate change as a mere sensitivity test that yields maps but no design changes. **Actively incorporate climate change into flood planning levels and design standards.** Use tools like the Climate Change Calculator to rapidly assess how flood probabilities and average annual damages will shift under various socio-economic pathways (SSPs) without requiring hundreds of new model runs [28-31].
*   **Use "Bottom-up" (Scenario-Neutral) stress testing:** To manage the deep uncertainty of climate projections, **stress-test systems using a bottom-up approach**. Evaluate how sensitive flood peaks are to combined changes in two key drivers: intensifying extreme rainfall and increasing rainfall losses (due to drier antecedent conditions) [32, 33].
*   **Apply the "Storylines Approach" for decision-makers:** Probabilistic climate models can cause decision paralysis due to overwhelming uncertainty. **Frame climate risks using the "storylines approach"**—creating physically self-consistent, localized, and plausible narratives (e.g., an "Optimistic" slightly drier future vs. a "Conservative" significantly warmer/drier future). This makes the data actionable for asset managers [34-36].
*   **Update hydroclimate baselines:** Recognize that statistical stationarity no longer holds. For major systems like the Murray-Darling Basin, **practitioners should treat the historical record up to 1990 as the baseline**, acknowledging that the baseline has shifted since then and must be modeled dynamically (e.g., via transient stochastic modeling) for medium- and long-term planning [37-39].
---

## Cross-Cutting Connections

*How the research themes in this conference connect and interact.*

RESPONSE:
The research themes at the HWRS 2024 conference are deeply interconnected, reflecting the reality that modern water resource management can no longer treat hydrology, infrastructure, and climate as isolated disciplines. The overarching cross-cutting issue across these themes is **non-stationarity**—the recognition that historical hydrological patterns are no longer reliable predictors of the future due to climate change and human interventions. 

Here is a comprehensive breakdown of how these themes connect, along with specific examples of papers that bridge multiple areas:

### 1. Climate-Induced Non-Stationarity in Extreme Flood Estimation
The most prominent interdisciplinary connection in the notebook is between **Climate Change & Hydrology** and **Extreme Flood Events**. Historically, flood frequency analysis assumed that the climate was stationary. However, warming temperatures are intensifying short-duration rainfall extremes while simultaneously altering soil moisture and antecedent catchment wetness.

*   **Updating Design Standards:** A major cross-cutting issue is how to adapt engineering design standards to a changing climate. Retallick et al. bridge this by evaluating the updated Australian Rainfall and Runoff (ARR) guidelines, demonstrating how factoring in temperature increases significantly alters existing flood level predictions under various Shared Socioeconomic Pathways (SSPs) [1, 2].
*   **Lifetime Exposure Risk:** Babister et al. intersect climate change and flood risk by presenting a novel method to estimate *lifetime flood exposure risk* [3]. Because the probability of design rainfall and flood levels changes every year due to climate change, traditional stationary binomial theorems are no longer valid, requiring new computational approaches [4, 5]. 
*   **Bottom-Up Flood Assessments:** O'Shea et al. connect these themes by proposing a "bottom-up" (or scenario-neutral) approach to event-based design flood estimation [6]. Their research looks at the joint impact of changing climate drivers—specifically how drier antecedent catchment conditions (which dampen floods) compete against intensifying rainfall extremes (which increase floods) [7].

### 2. The Hydrological Footprint of the Renewable Energy Transition
The push for net-zero emissions has spurred massive growth in **Renewable Energy Infrastructure**, creating a critical intersection with **Stormwater & Dam Analytics** and **Extreme Flood Events**. Renewable energy projects are often massive in scale, located in remote catchments, and introduce new impervious surfaces or terrain modifications that alter local hydrological cycles.

*   **Solar Farms and Stormwater Runoff:** Santhosh highlights the nexus of renewable energy and stormwater management, noting that utility-scale solar panels create impervious surfaces that alter soil moisture distribution, reduce water holding capacity, and increase runoff volume and kinetic energy [8-10]. This necessitates new, effective stormwater management practices specifically tailored for solar farms to prevent severe soil erosion [11].
*   **Flood Modelling for Energy Assets:** Azarnivand et al. bridge renewable energy and extreme floods by exploring the challenges of flood modelling for wind farms, solar farms, and Battery Energy Storage Systems (BESS) [12]. Because these assets are highly susceptible to flood damage and are often situated in remote areas with massive upstream catchments and scarce data, practitioners must utilize advanced hydraulic modelling features (like TUFLOW sub-grid sampling) to assess trafficability, immunity, and freeboard requirements [13, 14].
*   **Pumped Hydro and Groundwater:** Muller et al. bridge renewable infrastructure and baseflow analytics by assessing how tunnel excavations for the Snowy 2.0 pumped hydro-electric storage scheme affect groundwater and alpine stream perennialism during construction and operation [15].

### 3. Adaptive Infrastructure and Smart Stormwater Management
The intersection of **Stormwater & Dam Analytics** and **Climate Change & Hydrology** highlights a shift toward "smart" and adaptive infrastructure to cope with changing weather extremes and urbanization.

*   **Real-Time Control (RTC) of Stormwater:** Thyer et al. explore how climate change and urban density will increase future flood peaks, making traditional infrastructure upgrades (like larger pipes) prohibitively expensive [16]. They bridge these themes by proposing an "Adaptive Target Hydrograph Control" (ATHC) method, which uses real-time, smart orifice control at stormwater storage outlets to adapt to increased peak inflows (up to 95% higher) without needing physical infrastructure upgrades [16, 17].
*   **Climate Impacts on Water Quality:** Newton et al. bridge climate change and urban stormwater analytics by investigating how the longer dry spells expected under climate change will impact water quality [18, 19]. Extended dry periods allow for a greater buildup of pollutants on urban surfaces, which are then washed into waterways during subsequent storms [20].
*   **Dam Safety and Coincident Flooding:** Scorah et al. connect dam analytics to extreme flood events by examining the complex relationship between dam failure and coincident rainfall in downstream tributaries [21]. Accurately assessing the Potential Loss of Life (PLL) requires understanding the variability of extreme storms, making the accurate simulation of coincident flood flows vital for modern dam safety decisions [22, 23].

### Summary of Interdisciplinary Synergies
The research in this notebook clearly indicates that **water resource engineers can no longer rely on single-discipline approaches**. To build a solar farm, engineers must now understand extreme flood dynamics and sub-grid hydraulic modelling [12]. To design a stormwater network, practitioners must incorporate deep learning, real-time sensor controls, and non-stationary climate projections [16, 24]. Ultimately, the overarching message is that the compounding impacts of climate change, socio-economic development, and the energy transition require dynamic, multi-objective frameworks to ensure future water security and flood resilience [25, 26].
---

## Research Gaps

*Unanswered questions and future directions identified in the literature.*

RESPONSE:
Here are the key research gaps, future directions, and unanswered questions identified in the HWRS 2024 papers, categorized by your requested themes:

### **Extreme Flood Events**
*   **Limitations of Short Historical Records:** Our understanding of rare, extreme floods is highly constrained by the short length of systematic historical data. Authors strongly recommend exploring multiple lines of evidence—such as **indigenous knowledge, palaeofloods, and cosmogenic events**—to extend flood records and turn "myth" into history, which would reduce the deep uncertainty in flood frequency analyses [1-4].
*   **Coincident Flooding:** There is limited guidance in ARR2019 regarding the estimation of coincident rainfall for dam failure consequence assessments. Current methods often rely on approximations that underestimate the frequency of these events. Future research must direct attention to how coincident flows are represented and correlated to improve Potential Loss of Life (PLL) estimations [5-7]. 
*   **Storm Dynamics and Design Inputs:** There are unanswered questions about how climate change will impact storm dynamics, particularly East Coast Lows (ECLs) and convective thunderstorms. Researchers note a bias in current design inputs and recommend rerunning reconciled loss calibrations, as past loss models underrepresented ECLs [8-10].
*   **Need for "Bottom-Up" Assessments:** Because traditional "top-down" climate models carry deep uncertainty, researchers emphasize a need to adopt **scenario-neutral (bottom-up) frameworks** in practical, event-based flood modelling to better stress-test how changes in rainfall intensity and antecedent losses jointly impact flood risk [11-13].

### **Renewable Energy Infrastructure**
*   **Solar Farm Hydrology and Erosion:** Research on the landscape hydrology of utility-scale solar farms is surprisingly limited. Existing runoff generation models lack validation with field-specific data, and there is a critical need for field research on less ideal sites with steeper slopes (>5-8%) where erosion is a major concern [14-17]. 
*   **Solar-Specific Stormwater Management:** There is a major gap in the regulatory realm regarding runoff volume and quality at solar facilities. General construction permits are inadequate for the unique design of solar farms, and there is a pressing need to develop and validate **solar-specific infiltration and stormwater management practices** [18, 19].
*   **Data Scarcity in Remote Catchments:** Renewable energy projects (like wind and solar farms) are often located in remote, arid regions where vital hydrological data (like initial and continuing loss values) is absent. Flood modelling in these areas faces challenges integrating low-resolution and high-resolution terrain data, highlighting the need for advanced 2D modelling techniques (like TUFLOW's sub-grid sampling) [20-22].

### **Stormwater & Dam Analytics**
*   **Dam Breach Parameter Uncertainty:** Relying on a single regression equation to predict a dam breach is deemed inadequate due to massive uncertainties in breach formation time and peak flow. Future analysis must investigate additional regression equations (e.g., USBR, Zhong) and alternative 1D/2D analytical processes (e.g., HEC-RAS, TUFLOW) across a wider variety of dam locations to provide defendable outcomes [23-26].
*   **Corrugated Steel Pipe (CSP) Defects:** The knowledge base regarding defective CSPs is insufficient from a hydraulic engineering perspective. Unanswered questions remain about optimizing flow patterns to minimize water splashes (which cause pitting corrosion in the crown/middle of pipes) and developing eco-friendly debris control devices to prevent blockages [27-29].
*   **Vegetated Roofs and WSUD:** In stormwater management, there are gaps in understanding the complex interactions between vegetation, roof layers, and microclimates. Furthermore, the detailed mechanisms of **how changes in rainfall and potential evapotranspiration (PET) affect Water Sensitive Urban Design (WSUD) devices** require further research to inform climate-proofed WSUD designs [30-32].
*   **Air-Water Flow Instrumentation:** Current instrumentation cannot continuously measure internal air-water flow properties (like air concentration and bubble sizes) in 3D spaces like stilling basins. Advancing phase-detection intrusive probes and utilizing remote sensing (LIDAR/drones) to gather **quantitative validation data at prototype-scale hydraulic structures** is a critical future direction [33-35].

### **Climate Change & Hydrology**
*   **Rainfall-Partitioning Unknowns:** The impact of climate change on rainfall-partitioning (how rainfall translates into runoff) remains highly uncertain and statistically difficult to detect. Catchments are shifting to lower runoff states post-drought, but models cannot easily replicate this by just reducing rainfall inputs. Researchers recommend moving away from streamflow-only tests to system-wide "big laboratories" to understand these ecological and hydrological shifts [36-39].
*   **CO2 Fertilization and Evapotranspiration:** A major epistemic uncertainty is how plant physiological responses to increased atmospheric CO2 (carbon fertilization) will affect vegetation dynamics and catchment evapotranspiration. Upscaling leaf-level efficiency knowledge to regional runoff assessments requires significant future investigation [40-42].
*   **Groundwater Representation in Models:** Many conceptual rainfall-runoff models fail to simulate long-term groundwater dynamics effectively, leading them to mischaracterize multi-year climatic shifts. Future research must improve calibration techniques by integrating groundwater processes to prevent the overestimation of future water availability [43-45].
*   **Translating Science into Policy:** A significant gap exists between climate change guidelines and actual engineering practice. Currently, climate change is often relegated to a "sensitivity test" resulting in maps that do not impact final design levels. There is an urgent call for **formal policy changes** to incorporate climate change directly into flood planning levels and lifetime exposure risks [46, 47].
---

**See Also:**
- [Conference Papers Home](index.md)
