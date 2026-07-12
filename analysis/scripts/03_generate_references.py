#!/usr/bin/env python3
"""
Script 3: Generate bibliography.txt and references.bib from clean CSV
Input:  data/processed/database_final_231.csv
Output: references/bibliography.txt and references/references.bib
"""

import pandas as pd
import re
import os

# ============================================================
# CONFIG
# ============================================================
INPUT_FILE = 'data/processed/database_final_231.csv'
OUTPUT_BIBTXT = 'references/bibliography.txt'
OUTPUT_BIBTEX = 'references/references.bib'

# ============================================================
# LOAD DATA
# ============================================================
df = pd.read_csv(INPUT_FILE)
print(f"✅ Loaded {len(df)} papers")

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_BIBTXT), exist_ok=True)

# ============================================================
# GENERATE BIBLIOGRAPHY.TXT
# ============================================================
with open(OUTPUT_BIBTXT, 'w', encoding='utf-8') as f:
    for idx, row in df.iterrows():
        authors = row.get('Authors', 'Unknown Authors')
        title = row.get('Title', '')
        journal = row.get('Journal/Conference', '')
        year = int(row.get('Year', 0)) if pd.notna(row.get('Year')) else ''
        doi = row.get('DOI', '')
        
        ref = f"{authors}. {title}. {journal}"
        if year:
            ref += f". {year}"
        if doi:
            ref += f". doi:{doi}"
        f.write(f"{idx+1}. {ref}\n")

print(f"✅ bibliography.txt generated with {len(df)} entries")

# ============================================================
# GENERATE REFERENCES.BIB
# ============================================================
def escape_bibtex(text):
    if pd.isna(text):
        return ''
    text = str(text)
    for ch in ['\\', '{', '}', '_', '%', '&', '#']:
        text = text.replace(ch, '\\' + ch)
    return text

bib_lines = []
for idx, row in df.iterrows():
    key = row.get('Citation Key', f'paper{idx+1}')
    if pd.isna(key) or not str(key).strip():
        key = f'paper{idx+1}'
    
    journal = row.get('Journal/Conference', '')
    is_proceedings = any(x in str(journal) for x in ['Proceedings', 'IROS', 'ICRA', 'ISMAR', 'ICCV', 'NeurIPS', 'ECMR', 'AIHCIR'])
    entry_type = 'inproceedings' if is_proceedings else 'article'
    
    lines = [f"@{entry_type}{{{key},"]
    lines.append(f"  author = {{{escape_bibtex(row.get('Authors', ''))}}},")
    lines.append(f"  title = {{{escape_bibtex(row.get('Title', ''))}}},")
    if entry_type == 'article':
        lines.append(f"  journal = {{{escape_bibtex(journal)}}},")
    else:
        lines.append(f"  booktitle = {{{escape_bibtex(journal)}}},")
    lines.append(f"  year = {{{int(row.get('Year', 0))}}},")
    pub = row.get('Publisher', '')
    if pd.notna(pub) and str(pub).strip():
        lines.append(f"  publisher = {{{escape_bibtex(pub)}}},")
    doi = row.get('DOI', '')
    if pd.notna(doi) and str(doi).strip():
        lines.append(f"  doi = {{{doi}}},")
    # Remove trailing comma
    lines[-1] = lines[-1].rstrip(',')
    lines.append("}")
    bib_lines.append('\n'.join(lines))

with open(OUTPUT_BIBTEX, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(bib_lines))

print(f"✅ references.bib generated with {len(bib_lines)} entries")
print(f"\n✅ All files saved to references/ folder")
