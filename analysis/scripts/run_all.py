import subprocess
import sys

scripts = [
    '01_clean_data.py',
    '02_generate_figures.py',
    '03_generate_references.py',
    '04_generate_report.py',
    '05_verify_all.py'
]

for script in scripts:
    print(f"\n🚀 Running {script}...")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

print("\n✅ All scripts completed!")

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
    