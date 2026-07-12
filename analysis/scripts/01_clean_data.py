#!/usr/bin/env python3
"""
Script 1: Clean and Deduplicate the Dataset
Input:  data/raw/database_original.xlsx
Output: data/processed/database_final_231.csv and .xlsx
"""

import pandas as pd
import os
import sys

# ============================================================
# CONFIG – Use raw strings (r'...') to avoid escape issues
# ============================================================
# Absolute path – works regardless of where you run the script
RAW_FILE = r'I:\My Drive\Literature review UAVGPS\GPS_Denied_Drone_SLR 2.0\data\raw\database_original.xlsx'
OUTPUT_CSV = r'I:\My Drive\Literature review UAVGPS\GPS_Denied_Drone_SLR 2.0\data\processed\database_final_231.csv'
OUTPUT_EXCEL = r'I:\My Drive\Literature review UAVGPS\GPS_Denied_Drone_SLR 2.0\data\processed\database_final_231.xlsx'

# ============================================================
# CHECK IF FILE EXISTS
# ============================================================
if not os.path.exists(RAW_FILE):
    print(f"❌ File not found: {RAW_FILE}")
    print("Please place your Excel file in data/raw/database_original.xlsx")
    sys.exit(1)

# ============================================================
# LOAD DATA
# ============================================================
df = pd.read_excel(RAW_FILE, sheet_name='database')
print(f"✅ Loaded {len(df)} rows from {RAW_FILE}")

# ============================================================
# REMOVE DUPLICATES (based on Citation Key)
# ============================================================
df_clean = df.drop_duplicates(subset=['Citation Key'], keep='first').copy()
print(f"✅ Kept {len(df_clean)} unique papers (removed {len(df) - len(df_clean)} duplicates)")

# ============================================================
# SAVE
# ============================================================
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

df_clean.to_csv(OUTPUT_CSV, index=False)
df_clean.to_excel(OUTPUT_EXCEL, index=False, sheet_name='database')
print(f"✅ Saved to:\n   - {OUTPUT_CSV}\n   - {OUTPUT_EXCEL}")

# ============================================================
# VERIFY UNIQUE KEYS
# ============================================================
unique_keys = df_clean['Citation Key'].nunique()
print(f"✅ Unique Citation Keys: {unique_keys}")