# Software and Systems

**Conference:** HWRS 2012 — Water Resources Management and Modelling  
**Theme 3 of HWRS 2012**

---

## Overview

- eWater Source
- Existing Tools

---

## Detailed Analysis

**Software and systems are increasingly central to Water Resources Management and Modelling, enabling practitioners to address complex, multi-sectoral "wicked" problems such as climate change, competing water demands, and environmental sustainability** [1], [2]. The sources highlight a widespread transition from isolated, domain-specific tools to integrated, highly flexible, and heavily scrutinized modelling platforms.

**The Shift to Integrated Modelling Platforms: eWater Source**
A major theme in the sources is the development and adoption of **eWater Source (formerly Source IMS), which serves as Australia's National Hydrological Modelling Platform** [3], [2]. Historically, water authorities relied on legacy models like IQQM, REALM, and MSM-BigMod, which operated at different spatial and temporal scales and were difficult to link together seamlessly [4], [5], [6]. 
*   **Unified Framework:** Source was designed to encompass and enhance the functionalities of these legacy systems [7]. It integrates the full land phase of the hydrological cycle, offering modes for catchments, river management, and river operations [3], [8]. 
*   **Water Sharing and Optimization:** Source can simulate complex management rules, such as continuous sharing Resource Assessment Systems (RAS), where individual users independently manage their share of water [8], [9], [10]. For water ordering and allocation, it allows users to choose between heuristic (rules-based) systems and optimization-based Network Linear Programming (NetLP) solvers like RELAX IV and PPRN [11], [12].
*   **Quality Assurance:** To ensure models are robust and fit for purpose, the development of Source is backed by a rigorous quality assurance (QA) framework. This includes a hierarchy of best-practice guidelines for model application, structured code testing, peer-reviewed scientific reference guides, and automated test cases [13], [14], [15], [16].

**Coupling and Interoperability of Diverse Models**
Because no single software can perfectly simulate every physical process, **modern systems emphasize dynamic coupling and interoperability.**
*   **OpenMI Technology:** The Open Modelling Interface (OpenMI) standard is used to facilitate run-time data exchange between different software tools operating at varying spatial and temporal resolutions [17], [18]. For instance, OpenMI has successfully coupled the 3D finite-element groundwater model **FEFLOW** with the physically based, distributed surface water model **MIKE SHE**, combining advanced subsurface capabilities (like saltwater intrusion) with comprehensive evapotranspiration and overland flow processes [17], [19], [18].
*   **Hydrodynamic Integration:** In the Hawkesbury-Nepean catchment, Source was used for catchment hydrology while the **TUFLOW/FABM** model managed in-stream hydrodynamics and water quality [20], [21]. Customized plug-ins rapidly export daily flow and constituent loads from Source to TUFLOW [22]. Similarly, the MIKE suite (MIKE 11, MIKE SHE) has been integrated into real-time decision support systems for river operations, utilizing data assimilation to continuously correct simulated water levels against real observations [23], [24].

**Advanced Hydraulic and Hydrodynamic Modelling**
Resolving intricate flow behaviours—such as floodplain inundation, tidal interactions, and dam breaks—requires specialized 2D and 3D software:
*   **ANUGA:** This free, open-source software solves the shallow water wave (SWW) equation using a finite-volume method on unstructured grids. It is capable of acting as both a highly detailed 2D hydraulic model and a catchment hydrologic model, routing rainfall directly over the domain to model overland flow and mainstream flooding simultaneously [25], [26], [27], [28].
*   **ELCOM / CAEDYM:** These 3D models are extensively applied to predict velocity, temperature, salinity, and aquatic ecosystem dynamics in lakes, reservoirs, and estuaries [29], [30], [31], [32]. They support real-time reservoir management to optimize water quality and mitigate issues like algae blooms or turbidity [33], [34], [35].
*   **MIKE FLOOD and MIKE 21:** Used to evaluate floodplain connectivity, quantify wetland inundation, and optimize environmental releases from dams [24], [36], [37]. 

**GIS, Spatial Data, and Topographic Tools**
Software used for spatial analysis and data manipulation is vital for parameterizing hydrologic models:
*   **GRIDDA:** A specialized Windows program developed to easily aggregate and average gridded climate data (like AWAP or SILO) across irregular, "crooked" catchment boundaries extracted from GIS shapefiles, bypassing the need for expensive proprietary software [38], [39].
*   **LiDAR-RIM (Rapid Inundation Model):** This tool leverages high-resolution LiDAR Digital Elevation Models (DEMs) and simple mass balance equations to rapidly estimate flood inundation extents, depths, and volumes, serving as a computationally cheap alternative to full hydrodynamic modelling [40], [41], [42]. 
*   **DamSite:** An automated series of Python algorithms that assesses DEMs to identify topographically and hydrologically suitable locations for new dam walls, generating preliminary cost-yield potentials across millions of simulated sites [43], [44].

**Optimization for Decision Support and Portfolio Management**
Software is increasingly used to optimize resource trade-offs rather than simply simulating them:
*   **Evolutionary Algorithms:** Genetic Algorithms like the Elitist Non-dominated Sorting Genetic Algorithm (NSGA-II) are paired with simulation engines (like REALM) to find optimal multi-reservoir operating rules that balance the competing demands of consumptive users and environmental flows [45], [46], [47].
*   **Environmental Portfolios:** Optimization decision models help environmental water managers navigate complex variables (e.g., carryover rules, water pricing, antecedent ecological conditions) to strategically deploy environmental water holdings across multiple assets and over multi-year scales [48], [49], [50].
*   **Water Distribution Systems:** Specialized software, such as **Optimizer** and **WDNetXL**, apply genetic algorithms and hydraulic solvers to find the minimum-cost designs for urban water distribution networks [51], [52].

**Educational Needs for Modelling Software**
Finally, the sources identify a gap in how software is taught. The proliferation of complex, "easy-to-use" simulation software creates a risk that students will treat models as "point-and-click" black boxes [53]. To counter this, educators advocate for open-source, modular, object-oriented frameworks like **CHIMERA** and **Hydromad** (built in R), which require students to construct conceptual models from basic elements, thereby teaching the fundamental mechanics and assumptions underlying hydrologic software [54], [55], [56], [57].

---

**See Also:**
- [← HWRS 2012 Mind Map Overview](../hwrs-2012-mindmap.md)
- [Conference Papers Home](../index.md)
