#!/usr/bin/env python3
"""
Script 5: Final Verification – Check Consistency Across All Files
"""

import pandas as pd
import re
import os

# ============================================================
# CONFIG
# ============================================================
CSV_FILE = 'data/processed/database_final_231.csv'
BIB_FILE = 'references/bibliography.txt'
BIBTEX_FILE = 'references/references.bib'

print("=" * 60)
print("📊 FINAL VERIFICATION")
print("=" * 60)

# ============================================================
# 1. CHECK CSV
# ============================================================
df = pd.read_csv(CSV_FILE)
csv_rows = len(df)
csv_keys = set(df['Citation Key'].dropna())
print(f"✅ CSV rows: {csv_rows}")
print(f"✅ Unique CSV keys: {len(csv_keys)}")

# ============================================================
# 2. CHECK BIBLIOGRAPHY.TXT
# ============================================================
with open(BIB_FILE, 'r', encoding='utf-8') as f:
    bib_lines = [line for line in f if line.strip() and line.strip()[0].isdigit()]
bib_count = len(bib_lines)
print(f"✅ Bibliography entries: {bib_count}")

# ============================================================
# 3. CHECK REFERENCES.BIB
# ============================================================
with open(BIBTEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()
bibtex_count = len(re.findall(r'@\w+{', content))
bibtex_keys = set(re.findall(r'@\w+{([^,]+)', content))
print(f"✅ BibTeX entries: {bibtex_count}")
print(f"✅ Unique BibTeX keys: {len(bibtex_keys)}")

# ============================================================
# 4. COMPARE KEYS
# ============================================================
keys_match = (csv_keys == bibtex_keys)
print(f"\n✅ CSV keys match BibTeX keys: {keys_match}")

if not keys_match:
    in_csv_not_bib = csv_keys - bibtex_keys
    in_bib_not_csv = bibtex_keys - csv_keys
    if in_csv_not_bib:
        print(f"⚠️ In CSV but not BibTeX: {in_csv_not_bib}")
    if in_bib_not_csv:
        print(f"⚠️ In BibTeX but not CSV: {in_bib_not_csv}")

# ============================================================
# 5. FINAL SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("📊 VERIFICATION SUMMARY")
print("=" * 60)
print(f"CSV rows:                {csv_rows}")
print(f"Bibliography entries:    {bib_count}")
print(f"BibTeX entries:          {bibtex_count}")
print(f"Unique Citation Keys:    {len(csv_keys)}")

all_match = (csv_rows == bib_count == bibtex_count == len(csv_keys))
print(f"All files match:         {'✅ YES' if all_match else '❌ NO'}")

if all_match and keys_match:
    print("\n🎉 ALL FILES ARE CONSISTENT! Your dataset is ready.")
else:
    print("\n⚠️ Some files don't match. Please re-run the generation scripts.")
    