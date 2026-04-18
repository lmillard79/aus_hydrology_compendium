# Modelling and Analysis

**Conference:** Floodplain Management Australia (FMA) 2025  
**Theme ID:** theme-2  
**Subtopics:** Continuous Simulation Modelling (CSM), Multi-Hazard Assessment, Climate Change Impacts  
**NotebookLM ID:** `d12b5b0a-4d09-405b-a6eb-7e1de55a02a8`  
**Interactive Notebook:** [View in NotebookLM](https://notebooklm.google.com/notebook/d12b5b0a-4d09-405b-a6eb-7e1de55a02a8)

---

!!! note "Citation Note"
    Citations [1], [2], etc. refer to sources in the NotebookLM notebook. These are conference paper references that can be explored in the interactive notebook.

---

## The Shift to Programmatic and Whole-of-Catchment Modelling

In the context of floodplain management, there is a strategic shift from ad-hoc, project-by-project modelling to comprehensive, lifecycle-based program design. For example, Melbourne Water has transitioned to a model lifecycle framework where flood models are reviewed every 5 years and fully remodelled every 10 years [1, 2]. This programmatic approach adopts **whole-of-catchment modelling**, which crosses administrative boundaries to reflect actual hydrological flow paths, thereby ensuring consistent data for emergency responders and local governments [3-5].

## Addressing Climate Change and Non-Stationary Risk

Modern modelling must grapple with non-stationary flood behavior driven by climate change and urban growth [6, 7]. Assessments are increasingly incorporating updated Australian Rainfall and Runoff (ARR) guidance and various Shared Socioeconomic Pathways (SSP) over long-term horizons (e.g., 2050 and 2090) [8-11]. Because flood risk is non-static, decision-making frameworks are evolving from purely hazard-based metrics (like peak depth or velocity) to **holistic risk-based assessments** that factor in economic values, social equity, and adaptive capacity [12-14].

## Advancements in Modelling Techniques

The sources highlight several emerging technologies and methodologies that improve the accuracy and utility of flood models:

- **Continuous Simulation (CS) vs. Event-Based Modelling:** Traditional event-based models take a static snapshot of peak flood results. In contrast, CS models long-term hydrological processes, capturing the complex interplay of rainfall, evaporation, and soil moisture over wet and dry phases [15, 16]. This approach provides nuanced insights into flood frequency, duration, and system memory, which is highly valuable for infrastructure resilience and environmental planning [15, 17, 18].
- **Surrogate Models and Machine Learning:** High-resolution hydraulic models are computationally expensive. To overcome this, **low-fidelity models and statistical surrogate models** are being used to rapidly emulate flood dynamics. By applying techniques like Empirical Orthogonal Function (EOF) analysis to filter and select the most informative training events, computational costs can be reduced by up to 97% while maintaining robust performance for fast flood forecasting [19-21].
- **1D-2D Coupled Hydrodynamic Modelling:** In complex urban-coastal environments, integrated 1D-2D modelling (using software like HEC-RAS) is highly effective for simulating compound scenarios, such as extreme dam releases combined with tidal flooding [22-24].
- **Computational Fluid Dynamics (CFD):** As computational power improves, 3D CFD simulations are becoming practical for analysing complex flow interactions, turbulence, and sediment transport at a high resolution beyond traditional boundaries [25, 26].

## Multi-Hazard and Cascading Risk Assessments

Disaster adaptation increasingly requires modelling the spatial and temporal coincidence of multiple hazards. A notable case study in Ōtautahi Christchurch (New Zealand) mapped the cascading impacts of pluvial and fluvial floods, coastal inundation, elevated groundwater, and earthquake-induced vertical land movement [27-30].

To interpret these complex multi-hazard models, planners use **Project Response Indicators (PRIs)**. PRIs establish thresholds where individual floodplain elements (like buildings or roads) become unacceptably vulnerable, acting as a trigger to signal exactly *when* and *where* a change in management strategy or infrastructure investment is required [27, 31-33]. In New South Wales, this multi-hazard philosophy is central to the development of regional **Disaster Adaptation Plans (DAPs)**, which map out long-term adaptation pathways to proactively manage compound disaster risks [34-37].

## Real-Time Intelligence and Evacuation Modelling

During the response phase of disaster management, modelling transitions from static planning to dynamic operational intelligence:

- **Real-Time Impact Analytics:** Cloud-based systems (like FloodMapp's DASH) process live hydrologic data to automatically generate real-time impact analytics via APIs. Rather than just mapping water, these tools instantly calculate how many properties need evacuation, which critical substations are inundated, and the exact kilometres of roads closed [38-41].
- **Dynamic Evacuation Modelling:** The Flood Evacuation Model (FEM) 3.0 utilises agent-based traffic simulation (MATSim v15) to model large-scale community evacuations. It features congestion-sensitive routing, live traffic data integration, and behavioural modeling, allowing emergency managers to test the impacts of infrastructure bottlenecks and optimize evacuation timing [42-44].

## Data Quality and Practical Planning Outputs

The reliability of any flood model hinges on its inputs and assumptions. For instance, high-quality bathymetric (underwater topography) data is critical; poor bathymetry heavily compromises calibration and can misrepresent the extent of property inundation [45, 46]. Similarly, decisions on whether to "block out" buildings in overland flow models can drastically alter identified flow paths and planning controls [47, 48].

Ultimately, these complex hydraulic outputs must be translated into actionable planning tools. Tools such as **Flood Flow Conveyance (FFC)** mapping delineate functional floodways, helping local councils implement appropriate land-use zoning and reducing the regulatory burden by clearly communicating where cut-and-fill development is acceptable versus where it will adversely impact flood storage [49-52].

---

## Related Topics

- [Disaster Adaptation Plans](disaster-adaptation-plans.md)
- [Infrastructure and Land Planning](infrastructure-land-planning.md)
- [Governance and Programs](governance-programs.md)
- [FMA 2025 Mind Map Overview](../fma-2025-mindmap.md)
