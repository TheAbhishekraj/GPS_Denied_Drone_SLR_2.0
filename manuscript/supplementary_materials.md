# Supplementary Materials Description
## GPS-Denied Drone Navigation: A Systematic Literature Review
### Guidance for Organising, Uploading, and Citing Supplementary Materials

---

**Document Version:** 1.0  
**Date:** 2026-07-11  
**Manuscript:** GPS-Denied Drone Navigation: A Systematic Literature Review (N = 231)  
**Zenodo Repository:** https://doi.org/10.5281/zenodo.XXXXXXX *(update with real DOI once reserved)*

---

## 1. What Files to Include and Why

The following files should be included in the supplementary archive. Each file is justified by its contribution to transparency, reproducibility, and FAIR data principles.

| File | Format | Purpose | FAIR Principle Served |
|---|---|---|---|
| `database_final_231.csv` | CSV (UTF-8) | Full systematic review database (N=231 papers, all coded variables) | Findable, Accessible, Reusable |
| `data_dictionary.md` | Markdown | Defines every column in the CSV | Interoperable, Reusable |
| `README.md` | Markdown | Overview of archive contents, how to use the data | Findable, Accessible |
| `prisma_checklist_2020.pdf` | PDF | Completed PRISMA 2020 checklist | Reusable, Interoperable |
| `prisma_flowdiagram.svg` | SVG | PRISMA 2020 flow diagram (vector format) | Accessible, Reusable |
| `search_strings.md` | Markdown | Full Boolean search strings for IEEE Xplore, Scopus, Web of Science | Reusable |
| `analysis_scripts/01_descriptive_stats.py` | Python | Replicates Table I–III results | Reusable, Interoperable |
| `analysis_scripts/02_ate_analysis.py` | Python | Replicates Table VII ATE RMSE statistics | Reusable, Interoperable |
| `analysis_scripts/03_figures.py` | Python | Generates all manuscript figures | Reusable, Interoperable |
| `analysis_scripts/requirements.txt` | Text | Python package dependencies | Interoperable, Reusable |
| `figures_highres/` | Directory | High-resolution (300+ DPI or vector) versions of all manuscript figures | Accessible |
| `coding_guide.md` | Markdown | Instructions used for coding papers in the database | Reusable, Interoperable |
| `inter_rater_reliability.md` | Markdown | Report of screening reliability (if applicable) | Reusable |
| `LICENSE` | Text | CC BY 4.0 licence text | Accessible, Reusable |

**Why these files matter:**
- `database_final_231.csv` is the primary dataset — the entire manuscript is derived from it. Without it, readers cannot verify, extend, or challenge the findings.
- The analysis scripts allow full reproduction of all tables and figures from the raw data.
- The PRISMA checklist demonstrates methodological rigour and is required for SLR publication standards.
- The search strings allow other researchers to update the review by rerunning the search in future years.

---

## 2. How to Organise and Zip the Archive

### Recommended Directory Structure

```
GPS_Denied_SLR_Supplementary/
│
├── README.md                          ← Start here
├── LICENSE                            ← CC BY 4.0
├── data_dictionary.md                 ← Column definitions for the CSV
├── coding_guide.md                    ← How papers were coded
├── search_strings.md                  ← Full search strings (all databases)
├── prisma_checklist_2020.pdf          ← Completed PRISMA 2020 checklist
├── inter_rater_reliability.md         ← Screening reliability report
│
├── data/
│   └── database_final_231.csv         ← Main dataset
│
├── prisma/
│   ├── prisma_flowdiagram.svg         ← PRISMA flow (vector)
│   └── prisma_flowdiagram.png         ← PRISMA flow (300 DPI raster)
│
├── analysis_scripts/
│   ├── requirements.txt               ← pip dependencies
│   ├── 01_descriptive_stats.py        ← Table I–III
│   ├── 02_ate_analysis.py             ← Table VII, ATE statistics
│   └── 03_figures.py                  ← All manuscript figures
│
└── figures_highres/
    ├── fig1_prisma_flow.pdf
    ├── fig2_publication_trends.pdf
    ├── fig3_navigation_methods.pdf
    ├── fig4_sensor_distribution.pdf
    ├── fig5_ate_boxplot.pdf
    ├── fig6_dataset_usage.pdf
    └── fig7_venue_distribution.pdf
```

### How to Create the Zip Archive

**Windows (PowerShell):**
```powershell
Compress-Archive -Path "GPS_Denied_SLR_Supplementary" -DestinationPath "GPS_Denied_SLR_Supplementary.zip"
```

**macOS / Linux (Terminal):**
```bash
zip -r GPS_Denied_SLR_Supplementary.zip GPS_Denied_SLR_Supplementary/
```

**File size check:** Ensure the final `.zip` is < 100 MB (MDPI limit) and < 25 MB per file (IEEE ScholarOne limit for individual files). If figures make the archive too large, upload figures to Zenodo and reference the DOI in the submission portal.

---

## 3. README Template for the Supplementary Archive

*Copy and paste the text below into `GPS_Denied_SLR_Supplementary/README.md`; fill in bracketed fields before publishing.*

---

```markdown
# GPS-Denied Drone Navigation: A Systematic Literature Review
## Supplementary Materials — README

**Authors:** [Author 1], [Author 2], [Author 3]  
**Manuscript Title:** GPS-Denied Drone Navigation: A Systematic Literature Review  
**Journal:** [Target Journal Name]  
**Submission Date:** [YYYY-MM-DD]  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.XXXXXXX  
**Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

### Overview

This archive contains the complete dataset, analysis scripts, and supporting materials
for the systematic literature review of GPS-denied drone navigation published in
[Journal Name]. The review synthesised N = 231 peer-reviewed papers published between
2013 and 2023, identifying trends in navigation methods, sensor usage, benchmark datasets,
and quantitative positioning accuracy (Absolute Trajectory Error RMSE).

---

### Contents

| File / Folder | Description |
|---|---|
| `data/database_final_231.csv` | Main dataset: 231 papers, [N] coded variables. See `data_dictionary.md` for column definitions. |
| `data_dictionary.md` | Defines every column in `database_final_231.csv` |
| `coding_guide.md` | Protocol used to screen and code each paper |
| `search_strings.md` | Full Boolean search strings for all databases |
| `prisma_checklist_2020.pdf` | Completed PRISMA 2020 reporting checklist |
| `prisma/prisma_flowdiagram.svg` | PRISMA 2020 flow diagram (vector) |
| `analysis_scripts/` | Python scripts to reproduce all manuscript tables and figures |
| `figures_highres/` | High-resolution versions of all manuscript figures |
| `LICENSE` | CC BY 4.0 licence |

---

### How to Reproduce the Analysis

**Requirements:** Python 3.9+, pip

1. Install dependencies:
   ```bash
   pip install -r analysis_scripts/requirements.txt
   ```
2. Run descriptive statistics (Tables I–III):
   ```bash
   python analysis_scripts/01_descriptive_stats.py
   ```
3. Run ATE RMSE analysis (Table VII):
   ```bash
   python analysis_scripts/02_ate_analysis.py
   ```
4. Generate all figures:
   ```bash
   python analysis_scripts/03_figures.py
   ```
   Output figures are saved to `figures_highres/`.

---

### Data Collection

- **Search date:** [YYYY-MM-DD]
- **Databases searched:** IEEE Xplore, Scopus, Web of Science
- **Inclusion criteria:** Peer-reviewed; English language; primary navigation contribution; UAV (multi-rotor); reports real-flight results; published 2013–2023
- **Exclusion criteria:** Simulation-only; fixed-wing aircraft; GPS-assisted navigation; duplicate publications

---

### Citation

If you use this dataset, please cite:

> [Author 1], [Author 2], [Author 3]. (2026). GPS-Denied Drone Navigation: A Systematic Literature Review Dataset (N=231) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

And the associated manuscript:

> [Author 1], [Author 2], [Author 3]. (2026). GPS-Denied Drone Navigation: A Systematic Literature Review. *[Journal Name]*. https://doi.org/[manuscript DOI]

---

### Contact

For questions about the dataset or analysis scripts, contact: [corresponding author email]
```

---

## 4. Data Dictionary for `database_final_231.csv`

Every column in the main dataset is defined below. Columns are listed in the order they appear in the CSV file.

| # | Column Name | Data Type | Description | Allowed Values / Format | Example |
|---|---|---|---|---|---|
| 1 | `paper_id` | Integer | Unique sequential identifier for each paper | 1–231 | `42` |
| 2 | `doi` | String | Digital Object Identifier of the paper | `https://doi.org/10.XXXX/XXXXX` | `https://doi.org/10.1109/TRO.2022.12345` |
| 3 | `title` | String | Full title of the paper as published | Free text | `"Robust Visual-Inertial Odometry for UAVs"` |
| 4 | `authors` | String | Semicolon-separated author names (Last, First M.) | `Lastname, Firstname; ...` | `"Smith, John A.; Jones, Mary"` |
| 5 | `year` | Integer | Year of publication | 2013–2023 | `2022` |
| 6 | `venue` | String | Journal or conference name (full, unabbreviated) | Free text | `"IEEE Transactions on Robotics"` |
| 7 | `venue_type` | Categorical | Type of publication venue | `journal`, `conference`, `workshop` | `journal` |
| 8 | `venue_abbrev` | String | Standard abbreviation of venue | Free text | `IEEE TRO` |
| 9 | `nav_method_primary` | Categorical | Primary navigation method category | `sensor_fusion`, `visual_odometry_slam`, `lidar`, `inertial`, `rf_uwb`, `other` | `sensor_fusion` |
| 10 | `nav_method_detail` | String | More specific description of navigation approach | Free text | `"Visual-Inertial Odometry (VIO)"` |
| 11 | `primary_sensor` | Categorical | Primary sensor modality | `stereo_camera`, `mono_camera`, `depth_camera`, `lidar_3d`, `lidar_2d`, `imu`, `uwb`, `radar`, `sonar`, `optical_flow`, `event_camera`, `gps_other`, `barometer`, `magnetometer`, `wifi`, `other` | `stereo_camera` |
| 12 | `sensor_combination` | String | Semicolon-separated list of all sensors used | Sensor names from column 11 | `"stereo_camera; imu"` |
| 13 | `algorithm_name` | String | Name of algorithm/system if explicitly named | Free text or `NA` | `"ORB-SLAM3"`, `"VINS-Mono"`, `NA` |
| 14 | `uses_deep_learning` | Boolean | Whether deep learning (NN) is part of the pipeline | `TRUE`, `FALSE` | `TRUE` |
| 15 | `uses_map` | Boolean | Whether a pre-built map is used | `TRUE`, `FALSE` | `FALSE` |
| 16 | `environment_indoor` | Boolean | Tested in indoor environment | `TRUE`, `FALSE` | `TRUE` |
| 17 | `environment_outdoor` | Boolean | Tested in outdoor environment | `TRUE`, `FALSE` | `FALSE` |
| 18 | `real_flight` | Boolean | Real UAV flight experiment performed | `TRUE`, `FALSE` | `TRUE` |
| 19 | `simulation_only` | Boolean | Only simulation, no real flight | `TRUE`, `FALSE` | `FALSE` |
| 20 | `benchmark_dataset` | String | Semicolon-separated dataset names used | `EuRoC`, `TUM-VI`, `KITTI`, `ETH3D`, `UZH-FPV`, `Custom`, `NA`, etc. | `"EuRoC; Custom"` |
| 21 | `euroc_used` | Boolean | EuRoC MAV dataset used | `TRUE`, `FALSE` | `TRUE` |
| 22 | `reports_ate` | Boolean | ATE (Absolute Trajectory Error) is reported | `TRUE`, `FALSE` | `TRUE` |
| 23 | `ate_metric` | Categorical | Metric form of ATE reported | `rmse`, `mean`, `median`, `max`, `std`, `multiple`, `NA` | `rmse` |
| 24 | `ate_rmse_m` | Float | ATE RMSE value in metres (best result reported) | Positive real number, or `NA` | `0.052` |
| 25 | `ate_rmse_unit_original` | Categorical | Original unit as reported in paper | `m`, `cm`, `mm`, `deg`, `NA` | `m` |
| 26 | `ate_rmse_original_value` | Float | ATE RMSE in original units (before conversion) | Positive real number, or `NA` | `5.2` |
| 27 | `rpe_reported` | Boolean | Relative Pose Error (RPE) reported | `TRUE`, `FALSE` | `FALSE` |
| 28 | `rpe_value_m` | Float | RPE value in metres, if reported | Positive real number, or `NA` | `NA` |
| 29 | `drift_reported` | Boolean | Drift (e.g., % of path length) reported | `TRUE`, `FALSE` | `FALSE` |
| 30 | `drift_value` | Float | Drift value (check units in next column) | Positive real number, or `NA` | `NA` |
| 31 | `drift_unit` | Categorical | Unit of drift value | `m`, `percent`, `m_per_km`, `NA` | `NA` |
| 32 | `trajectory_length_m` | Float | Trajectory length in metres (if stated) | Positive real, or `NA` | `120.5` |
| 33 | `uav_type` | Categorical | UAV platform type | `quadrotor`, `hexarotor`, `octorotor`, `fixed_wing`, `hybrid`, `micro_uav`, `nano_uav`, `other` | `quadrotor` |
| 34 | `uav_model` | String | Specific UAV model if named | Free text or `NA` | `"DJI M100"`, `NA` |
| 35 | `payload_g` | Float | UAV payload capacity in grams, if stated | Positive real, or `NA` | `500.0` |
| 36 | `compute_platform` | String | Onboard compute platform, if named | Free text or `NA` | `"NVIDIA Jetson Xavier"`, `NA` |
| 37 | `hz_est` | Float | State estimation frequency in Hz, if stated | Positive real, or `NA` | `100.0` |
| 38 | `realtime` | Boolean | System runs in real-time (not post-processed) | `TRUE`, `FALSE`, `NA` | `TRUE` |
| 39 | `open_source` | Boolean | Code or dataset made openly available | `TRUE`, `FALSE` | `FALSE` |
| 40 | `open_source_url` | String | URL to open-source code or dataset | URL or `NA` | `"https://github.com/..."` |
| 41 | `comparison_methods` | String | Semicolon-separated names of compared baseline methods | Free text or `NA` | `"ORB-SLAM3; LIO-SAM"` |
| 42 | `screen_title_abstract` | Categorical | Screening decision at title/abstract stage | `include`, `exclude`, `uncertain` | `include` |
| 43 | `screen_fulltext` | Categorical | Screening decision at full-text stage | `include`, `exclude` | `include` |
| 44 | `exclusion_reason` | String | Reason for exclusion, if excluded | Free text or `NA` | `NA` |
| 45 | `coder_id` | String | ID of the person who coded this paper | `C1`, `C2`, `C3` | `C1` |
| 46 | `coding_date` | Date | Date the paper was coded | `YYYY-MM-DD` | `2024-08-15` |
| 47 | `notes` | String | Miscellaneous coder notes | Free text or `NA` | `"Reports ATE on EuRoC V1 sequence only"` |

**Total columns:** 47  
**Total rows (data):** 231 + 1 header row = 232 rows in the CSV file  
**Encoding:** UTF-8  
**Delimiter:** Comma (`,`)  
**Missing values:** `NA` (not empty cell, not `NaN`) — consistent throughout  
**Boolean encoding:** `TRUE` / `FALSE` (not 1/0, not yes/no)

---

## 5. Instructions for Uploading to Zenodo / Figshare

### 5.1 Zenodo (Recommended)

**Why Zenodo:** Free, run by CERN, integrates with GitHub, issues DOIs, CC BY 4.0 compatible, widely accepted by IEEE and MDPI.

**Step-by-step:**

1. **Create account:** Go to zenodo.org → Log in with ORCID (recommended — links deposit to your ORCID profile automatically) or create a Zenodo account.

2. **New upload:** Click the green "New Upload" button.

3. **Upload files:**
   - Drag and drop `GPS_Denied_SLR_Supplementary.zip` into the file upload area.
   - Also upload `database_final_231.csv` as a **separate** file (not only inside the zip) so Zenodo can preview it.
   - Upload `README.md` separately as well.

4. **Set record type:** Select "Dataset."

5. **Reserve DOI (important — do this before manuscript submission):** Click "Reserve DOI." This gives you a DOI to cite in the manuscript before the deposit is published.

6. **Fill metadata:**
   | Field | Value |
   |---|---|
   | Upload type | Dataset |
   | Basic information – Title | GPS-Denied Drone Navigation SLR: Systematic Review Database (N=231) |
   | Publication date | Use acceptance date; or submission date for preprint |
   | Authors | All manuscript authors with ORCID iDs |
   | Description | Copy from README.md overview section |
   | Keywords | gps-denied, uav, drone, slam, systematic review, ate rmse, sensor fusion |
   | Licence | Creative Commons Attribution 4.0 International |
   | Access | Open Access |
   | Related publications | Add manuscript DOI once published (Related/alternate identifier) |

7. **Save draft:** Do NOT publish yet if manuscript is under review (keeps DOI reserved but record private).

8. **Publish:** Once the manuscript is accepted, return to the draft and click "Publish." The DOI becomes live.

9. **Link to ORCID:** After publishing, Zenodo will prompt you to add the deposit to your ORCID profile — do this for all authors.

### 5.2 Figshare (Alternative)

**Why Figshare:** Also free, widely used, good for figure sharing, integrates with Altmetric.

1. Go to figshare.com → Create account.
2. Click "+ Create new item."
3. Select item type: "Dataset."
4. Upload files (same as Zenodo).
5. Fill title, description, keywords, licence (CC BY 4.0).
6. Click "Reserve DOI" or "Generate DOI."
7. Click "Publish" when ready.

---

## 6. Caption / Legend Text for Manuscript

Use the following standardised text when referring to supplementary materials in the manuscript body. These are IEEE- and MDPI-style caption references.

### In-text references to supplementary materials:

```
The complete systematic review database, including all coded variables 
for each of the 231 included papers, is provided as Supplementary Table S1 
(database_final_231.csv) and is openly available at Zenodo 
(https://doi.org/10.5281/zenodo.XXXXXXX).
```

```
Full Boolean search strings for all three databases (IEEE Xplore, Scopus, 
Web of Science) are provided in Supplementary Materials (search_strings.md).
```

```
Python analysis scripts used to generate all figures and tables are 
available in the supplementary archive (analysis_scripts/) and at 
Zenodo (https://doi.org/10.5281/zenodo.XXXXXXX).
```

```
The completed PRISMA 2020 checklist is provided as a supplementary file 
(prisma_checklist_2020.pdf).
```

### Supplementary table/figure captions:

```
Table S1. database_final_231.csv — Complete systematic review database. 
N = 231 papers (2013–2023) coded across 47 variables including navigation 
method, primary sensor, benchmark dataset, ATE RMSE (where reported), 
UAV platform, and testing environment. Column definitions are provided 
in data_dictionary.md. Missing values are denoted 'NA'.
```

```
Figure S1. High-resolution PRISMA 2020 flow diagram illustrating the 
systematic search and screening process. Records identified: [N_ident]; 
records screened (title/abstract): [N_screen]; full-text assessed: [N_full]; 
included in synthesis: 231. Exclusion reasons are detailed in the 
diagram nodes.
```

### Data Availability Statement (for manuscript):

> The systematic review database (N = 231, `database_final_231.csv`), analysis scripts, PRISMA 2020 checklist, and high-resolution figures are openly available at Zenodo under a Creative Commons Attribution 4.0 International licence: https://doi.org/10.5281/zenodo.XXXXXXX. All data required to reproduce the manuscript's analyses are contained within the supplementary archive.

---

## 7. FAIR Data Principles Compliance Checklist

FAIR stands for **F**indable, **A**ccessible, **I**nteroperable, **R**eusable. This checklist confirms compliance with the FAIR principles as defined by Wilkinson et al. (2016), *Scientific Data*.

### F — Findable

| # | Requirement | Status | Evidence |
|---|---|---|---|
| F1 | Data is assigned a globally unique, persistent identifier (PID) | ☐ | Zenodo DOI: https://doi.org/10.5281/zenodo.XXXXXXX |
| F2 | Data is described with rich metadata | ☐ | README.md and Zenodo metadata form completed |
| F3 | Metadata clearly and explicitly includes the identifier of the data | ☐ | DOI included in README.md and manuscript Data Availability Statement |
| F4 | Data is registered or indexed in a searchable resource | ☐ | Zenodo is indexed by DataCite, OpenAIRE, and Google Dataset Search |

### A — Accessible

| # | Requirement | Status | Evidence |
|---|---|---|---|
| A1 | Data is retrievable using a standardised communications protocol | ☐ | HTTPS (Zenodo download link) |
| A1.1 | Protocol is open, free, and universally implementable | ☐ | HTTPS is open |
| A1.2 | Protocol allows for authentication/authorisation where necessary | ☐ | No authentication required (Open Access) |
| A2 | Metadata remains accessible even if data is no longer available | ☐ | Zenodo preserves metadata for all records, even deleted ones |

### I — Interoperable

| # | Requirement | Status | Evidence |
|---|---|---|---|
| I1 | Data uses a formal, accessible, shared, and broadly applicable language | ☐ | CSV (UTF-8, comma-delimited) — universally readable |
| I2 | Data uses vocabularies that follow FAIR principles | ☐ | Column names follow consistent snake_case convention; units stated; Boolean values standardised |
| I3 | Data includes qualified references to other data | ☐ | `doi` column links each paper; `benchmark_dataset` column references external datasets by standard name |

### R — Reusable

| # | Requirement | Status | Evidence |
|---|---|---|---|
| R1 | Data has a plurality of accurate and relevant attributes | ☐ | 47 columns covering all relevant metadata dimensions |
| R1.1 | Data is released with a clear and accessible data usage licence | ☐ | CC BY 4.0 (LICENSE file in archive; stated in Zenodo metadata) |
| R1.2 | Data is associated with detailed provenance | ☐ | README.md states search date, databases, inclusion/exclusion criteria; coding_guide.md describes the coding protocol |
| R1.3 | Data meets domain-relevant community standards | ☐ | PRISMA 2020 standard followed; IEEE taxonomy used for venue abbreviations |

**FAIR Compliance Score:** ☐ / 15 (complete all checks before publication)

### To achieve full FAIR compliance:

1. ☐ Reserve and embed the Zenodo DOI in the manuscript before submission (F1, F3).
2. ☐ Complete the Zenodo metadata form fully, including keywords and related publications (F2, F4).
3. ☐ Ensure the CSV is UTF-8 encoded with no BOM, comma-delimited, and that `NA` is used consistently for all missing values (I1, I2).
4. ☐ Add the CC BY 4.0 `LICENSE` text file to the archive root (R1.1).
5. ☐ Complete the `README.md` with full provenance information (R1.2).
6. ☐ Complete the PRISMA 2020 checklist PDF and include in the archive (R1.3).
7. ☐ Link the Zenodo deposit to each author's ORCID profile after publishing (R1.2, F4).

---

*End of Supplementary Materials Description — v1.0 — 2026-07-11*
