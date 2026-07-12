# References Directory

This directory contains the final generated bibliography and BibTeX files for the SLR 2.0.

## Source of Truth
The canonical source of truth for all references is the **`data/processed/database_final_231.csv`** file. 

## Update Workflow
**Do not manually edit the files in this directory.**
If you need to update citations, fix typos in paper titles, or add missing references:
1. Update the original Excel file (`data/raw/database_original.xlsx`).
2. Run the reproducibility pipeline from the project root:
   ```bash
   python run_all.py
   ```
3. The script `analysis/scripts/03_generate_references.py` will automatically regenerate `bibliography.txt` and `references.bib` ensuring perfect consistency with the dataset.

## Consistency Guarantee
The pipeline includes a verification script (`05_verify_all.py`) that strictly asserts the number of entries in `bibliography.txt` and `references.bib` matches the number of rows in the final dataset (231), preventing citation drift.
