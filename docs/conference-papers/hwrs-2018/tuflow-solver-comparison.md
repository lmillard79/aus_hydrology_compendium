# TUFLOW Solver Comparison

**Conference:** HWRS 2018 — HWRS 2018: Hydrology and Water Resources Symposium  
**Theme 1 of HWRS 2018**

---

## Overview

- TUFLOW Classic
- TUFLOW HPC
- Gowrie Creek Case Study

---

## Detailed Analysis

At the HWRS 2018 symposium, the comparison between TUFLOW solvers is prominently featured in a study that benchmarks the traditional **TUFLOW Classic** solver against the newer **TUFLOW Heavily Parallelised Compute (HPC)** solver [1, 2]. This comparison is highly relevant to the broader context of the symposium, which frequently addressed the massive computational burdens introduced by the updated Australian Rainfall and Runoff 2016 (ARR2016) guidelines [3-5].

**The TUFLOW Solver Comparison**
Prior to September 2017, a major limitation of TUFLOW's Graphics Processing Unit (GPU) solver was its inability to couple with 1D networks. The release of the HPC solver removed this limitation, enabling full 1D/2D coupling for pits, pipes, culverts, and open channels [6, 7]. Using a calibrated model of the Gowrie Creek catchment in Toowoomba, researchers compared the two solvers using the exact same data inputs, grid resolution, and initial parameters [8, 9].

*   **Computational Speed:** The HPC solver, running on GPUs, proved to be vastly superior in speed compared to the CPU-based TUFLOW Classic. For the January 2011 flood event, **model run times were reduced by over 85%**, dropping from 744 minutes in Classic to just 77 minutes on a single GPU, and 60 minutes on two GPUs [10-12]. Similar reductions were seen for a smaller 20% AEP event, where run times dropped from 248 minutes to 21.5 minutes on two GPUs [11].
*   **Accuracy and Differences:** Overall, the HPC solver produced peak flood extents and depths that closely mirrored TUFLOW Classic [13, 14]. However, noticeable differences emerged in **areas with shallow water depths** (where small depth variations correspond to high percentage differences) and in **areas with complex flow patterns**, such as the Central Business District (CBD) and around hydraulic structures [15-18]. To achieve the best calibration match with the Classic model, the HPC model required a **20% reduction in hydraulic roughness (Manning's n)** specifically within the commercial areas of the CBD (from 0.05 to 0.04) [18-20].
*   **Solver Mechanics and Risks:** TUFLOW Classic uses an implicit scheme with a fixed, user-specified time step, meaning the model will crash and produce an error if it becomes unstable [12, 21]. In contrast, TUFLOW HPC uses an explicit solution with an adaptive time step, constantly reducing its time step to maintain mathematical stability [12, 21, 22]. Because HPC is unconditionally stable, it can effectively "mask" poor modelling techniques or parameterization errors by simply reducing the time step rather than failing [22, 23]. To mitigate this, **modellers are advised to run initial setups using TUFLOW Classic as a precautionary check** to identify and fix instabilities before relying on the speed of the HPC solver [23, 24].

**The Larger Context of HWRS 2018**
This solver comparison directly addresses a recurring theme at HWRS 2018: **the tension between advanced hydrological methodologies and computational limitations.** 

The transition from ARR1987 to ARR2016 replaced the single "Design Event" approach with ensemble and Monte Carlo frameworks to better represent natural flood variability [4, 25, 26]. This shift requires running 10 times to thousands of times more simulations per project [5, 27-29]. As noted in other HWRS 2018 papers, while hydrologic models can handle this increase, 2D hydraulic models face severe computational constraints, often forcing practitioners to compromise by selecting a single "representative flood" to model instead of a full ensemble [29-31]. 

By providing cost-effective run-time reductions of up to 100 times [2], GPU-accelerated solvers like **TUFLOW HPC are presented as the technological bridge that allows the industry to actually implement the rigorous, data-heavy ARR2016 standards** without being bottlenecked by the sheer processing time of 2D hydraulic modelling [6, 7, 24].

---

**See Also:**
- [← HWRS 2018 Mind Map Overview](../hwrs-2018-mindmap.md)
- [Conference Papers Home](../index.md)
