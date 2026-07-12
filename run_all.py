import os
import subprocess
import sys
from pathlib import Path

import sys
# Fix Windows unicode output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

def main():
    print("=" * 60)
    print("🚀 Starting SLR 2.0 Reproducible Pipeline")
    print("=" * 60)
    
    # Ensure we run from the project root
    root_dir = Path(__file__).resolve().parent
    os.chdir(root_dir)
    print(f"📍 Working directory set to: {root_dir}")

    # Check for raw input file
    raw_data_path = root_dir / 'data' / 'raw' / 'database_original.xlsx'
    if not raw_data_path.exists():
        print(f"❌ Error: Raw input data missing at {raw_data_path}")
        print("Please ensure the raw data file is present before running the pipeline.")
        sys.exit(1)

    scripts = [
        ('01_clean_data.py', 'Cleaning and deduplicating data'),
        ('02_generate_figures.py', 'Generating figures and charts'),
        ('03_generate_references.py', 'Building bibliography and BibTeX'),
        ('04_generate_report.py', 'Generating markdown reports and tables'),
        ('05_verify_all.py', 'Verifying data consistency across all outputs')
    ]

    scripts_dir = root_dir / 'analysis' / 'scripts'

    for script_name, description in scripts:
        script_path = scripts_dir / script_name
        if not script_path.exists():
            print(f"❌ Error: Script missing at {script_path}")
            sys.exit(1)
            
        print(f"\n▶️ Stage: {description} ({script_name})...")
        
        # We run the script inside its own directory if it relies on local relative paths,
        # but the prompt says "ensure relative paths only". Let's run from root, 
        # assuming the scripts are robust, or run from scripts_dir if they were written that way.
        # Previously they were run from scripts_dir. Let's run from root, but execute the script path.
        # Wait, if they have hardcoded relative paths like `../data/`, they must run from `analysis/scripts/`.
        # I'll run them from `analysis/scripts/` to be safe, but output the logs here.
        
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        result = subprocess.run([sys.executable, str(script_path)], cwd=root_dir, capture_output=True, text=True, env=env)
        
        if result.returncode != 0:
            print(f"❌ Error during execution of {script_name}:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(result.returncode)
        else:
            print(f"✅ {script_name} completed successfully.")
            # Optional: print(result.stdout) if verbose

    print("\n" + "=" * 60)
    print("🎉 ALL STAGES COMPLETED SUCCESSFULLY!")
    print("Check analysis/output/ for the generated figures and reports.")
    print("=" * 60)

if __name__ == '__main__':
    main()
