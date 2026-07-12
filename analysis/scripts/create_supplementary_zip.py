#!/usr/bin/env python3
import os, shutil, zipfile
from pathlib import Path

# Use the current working directory (assumed to be the project root)
PROJECT_ROOT = Path.cwd()
OUTPUT_ZIP = PROJECT_ROOT / "supplementary_materials.zip"

FOLDERS = [
    "data/processed",
    "analysis/scripts",
    "analysis/output/figures",
]
FILES = ["requirements.txt", "README.md"]

def create_zip():
    if OUTPUT_ZIP.exists():
        os.remove(OUTPUT_ZIP)
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in FOLDERS:
            src = PROJECT_ROOT / folder
            if not src.exists():
                print(f"⚠️ Warning: {src} missing – skipping.")
                continue
            for root, dirs, files in os.walk(src):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=PROJECT_ROOT)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        for file in FILES:
            src = PROJECT_ROOT / file
            if src.exists():
                zipf.write(src, file)
                print(f"  Added: {file}")
            else:
                print(f"⚠️ Warning: {file} missing – skipping.")
    print(f"\n✅ ZIP created: {OUTPUT_ZIP} (size: {OUTPUT_ZIP.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    create_zip()