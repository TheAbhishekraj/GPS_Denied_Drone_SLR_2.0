# Reproducibility Protocol

This document outlines the exact steps to reproduce the entire data processing, analysis, and output generation pipeline for the GPS-Denied Drone SLR 2.0.

## Environment Setup
Ensure you have Python 3.10 or 3.11 installed.

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/TheAbhishekraj/GPS_Denied_Drone_SLR_2.0.git
   cd GPS_Denied_Drone_SLR_2.0
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
3. Install the exact pinned dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Exact Commands to Run

The entire pipeline can be executed via a single entrypoint script from the repository root:
```bash
python run_all.py
```

### Estimated Runtime
The complete pipeline takes less than **30 seconds** on a modern laptop. It runs locally without requiring external database access (the raw dataset is bundled in `data/raw/`).

## Expected Generated Files

Upon successful execution, the following artifacts will be (re)generated:

- **Cleaned Data:** `data/processed/database_final_231.csv` and `.xlsx`
- **Figures:** 9 PNG files in `analysis/output/figures/` (e.g., publication trends, sensor accuracy distributions)
- **Reports:** `analysis/output/report.md`, `analysis/output/tables.md`, and `analysis/output/sensor_accuracy.csv`
- **Bibliography:** `references/bibliography.txt` and `references/references.bib`

## Troubleshooting

- **Missing Input Error:** Ensure `data/raw/database_original.xlsx` exists before running the script.
- **Python Version Issues:** If you encounter syntax errors, verify your Python version is $\ge$ 3.10.
- **Dependency Issues:** Ensure you ran `pip install -r requirements.txt` within the activated environment.
