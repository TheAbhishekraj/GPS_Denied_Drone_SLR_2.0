# Manual: How to Reproduce This Specific Literature Review

This document explains how to reproduce the entire workflow for the **GPS‑denied drone navigation** systematic review, from raw data to final outputs.

## Prerequisites

- Python 3.8+ installed.
- Required packages: `pandas`, `matplotlib`, `seaborn`, `openpyxl`, `requests`, `tqdm`.
- Your raw Excel file with all columns (including `Citation Key`, `DOI`, etc.) placed in `data/raw/database_original.xlsx`.

## Step‑by‑Step Instructions

### 1. Set Up the Project Environment

```bash
# Install dependencies
pip install -r requirements.txt

2. Clean and Deduplicate
bash
cd analysis/scripts
python 01_clean_data.py
This script:

Loads data/raw/database_original.xlsx.

Removes duplicate rows based on Citation Key.

Saves database_final_231.csv and .xlsx in data/processed/.

3. Generate Figures
bash
python 02_generate_figures.py
Creates 9 figures in analysis/output/figures/:

Publication trend, sensor types, navigation methods, indoor/outdoor, real vs sim, ATE RMSE distribution, sensor‑wise boxplot, mean bar plot, median bar plot.

4. Generate References
bash
python 03_generate_references.py
Produces:

references/bibliography.txt (numbered list 1–231).

references/references.bib (BibTeX file).

5. Generate Analysis Report
bash
python 04_generate_report.py
Outputs:

analysis/output/report.md – full report with tables, figures, and researcher remarks.

analysis/output/tables.md – clean tables for direct copy‑paste.

analysis/output/sensor_accuracy.csv – sensor‑wise accuracy data.

6. Verify Everything
bash
python 05_verify_all.py
Checks that CSV rows, bibliography entries, and BibTeX entries all match (231).

7. (Optional) Run All Steps at Once
bash
python run_all.py

Outputs for Your Manuscript
Tables: Copy from tables.md.

Figures: All PNG files in analysis/output/figures/.

Report: Use report.md as a foundation for your Results and Discussion sections.

References: bibliography.txt for the reference list; references.bib for LaTeX.

Troubleshooting
FileNotFoundError: Ensure your raw file is correctly named and placed.

Missing packages: Install using pip install -r requirements.txt.

Path errors: Use forward slashes (/) or raw strings (r'...') in Python scripts

