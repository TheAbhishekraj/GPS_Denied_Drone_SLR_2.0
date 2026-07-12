# Systematic Review: GPS‑Denied Drone Navigation

## Project Overview

This repository contains the complete workflow for a systematic literature review (SLR) on **GPS‑denied drone navigation**.  
The review covers **231 unique papers** (deduplicated from an initial set of 250), with analyses of publication trends, sensor configurations, navigation methods, evaluation environments, and localization accuracy (ATE RMSE).

## Repository Structure

├── README.md # This file
├── requirements.txt # Python dependencies
├── data/
│ ├── raw/ # Original dataset (database_original.xlsx)
│ └── processed/ # Cleaned dataset (database_final_231.csv, .xlsx)
├── analysis/
│ ├── scripts/ # All Python scripts
│ │ ├── 01_clean_data.py
│ │ ├── 02_generate_figures.py
│ │ ├── 03_generate_references.py
│ │ ├── 04_generate_report.py
│ │ ├── 05_verify_all.py
│ │ └── run_all.py
│ └── output/
│ ├── figures/ # 9 publication‑ready figures
│ ├── report.md # Full analysis report with remarks
│ └── tables.md # Clean tables for manuscript
├── references/
│ ├── bibliography.txt # Numbered reference list (1–231)
│ └── references.bib # BibTeX file for LaTeX
├── manuscript/
│ ├── paper_final.md # Complete final manuscript with integrated figures
│   ├── cover_letter.md
│   ├── author_contributions.md
│   ├── conflict_of_interest.md
│   └── data_availability.md
├── docs/
│ ├── do_and_dont.md
│ ├── manual_current_literature.md
│ ├── review_methodology_phase_by_phase.md
│ └── prompt_and_key_pointers.md
└── .vscode/
└── settings.json # VS Code project settings


## Software Used

| Tool | Purpose |
|------|---------|
| **Python 3.8+** | Data processing, analysis, and figure generation |
| **pandas** | Data manipulation |
| **matplotlib / seaborn** | Figure generation |
| **openpyxl** | Excel file reading/writing |
| **VS Code** | Code editing and Markdown preview |
| **Zotero (optional)** | Reference management |

## Researcher Workflow (How to Operate)

1. **Data Collection** – Gather papers (initial set of 250).
2. **Data Cleaning** – Run `01_clean_data.py` to deduplicate and produce `database_final_231.csv`.
3. **Data Analysis** – Run `02_generate_figures.py` to create all figures.
4. **Reference Generation** – Run `03_generate_references.py` to create `bibliography.txt` and `references.bib`.
5. **Report Generation** – Run `04_generate_report.py` to produce the analysis report and tables.
6. **Verification** – Run `05_verify_all.py` to confirm consistency across all files.
7. **Manuscript Writing** – Use the generated tables, figures, and report to write `paper_final.md`.

## Key Findings

- **231 unique papers** analysed (19 duplicates removed).
- **96.1%** of studies include real‑flight experiments.
- **Median ATE RMSE** = 0.080 m (centimetre‑level accuracy).
- **Sensor fusion** (LiDAR + camera + IMU) yields the best accuracy.
- **IMU** is used in >85% of studies.
- **Event cameras** are emerging in recent work.

## Project Status

**STATUS: MANUSCRIPT COMPLETE.** All analyses, data verification, and manuscript writing have been finalized. The project is ready for journal submission.

## How to Reproduce

1. Install Python 3.8+ and required packages: `pip install -r requirements.txt`
2. Place your raw Excel file in `data/raw/database_original.xlsx`.
3. Run the scripts in order from the project root:
   ```bash
   python analysis/scripts/run_all.py


#4 All outputs will be generated in analysis/output/ and references/.
# Contact For questions or collaboration, please contact [Abhishek Raj/rajabhi2602@gmail.com].