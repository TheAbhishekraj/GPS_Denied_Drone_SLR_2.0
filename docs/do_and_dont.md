
---

## 📄 File 2: `docs/do_and_dont.md`

*Place this file in the `docs/` folder.*

```markdown
# Do's and Don'ts for Systematic Reviews (with Lessons from This Project)

## DO's

| Do | Why |
|----|-----|
| **Always deduplicate using Citation Key** / DOI | Prevents double‑counting and ensures accurate statistics. |
| **Use DOIs as permanent links** | DOIs never change; avoid fragile URLs. |
| **Generate figures programmatically** | Ensures reproducibility and consistency. |
| **Keep raw data separate from processed data** | Preserves original data for verification. |
| **Document all scripts and steps** | Enables transparency and future updates. |
| **Verify consistency across all output files** | Catch mismatches early (e.g., CSV vs BibTeX). |
| **Use colour‑blind‑friendly palettes** | Makes figures accessible to all readers. |
| **Include sample sizes (n) in plots** | Shows the reliability of each comparison. |
| **Write researcher remarks** | Interprets tables and figures – adds value beyond raw numbers. |
| **Use version control (Git)** | Tracks changes and facilitates collaboration. |

## DON'Ts

| Don't | Why |
|-------|-----|
| **Don't rely on manual copy‑paste** | Risk of errors; automate where possible. |
| **Don't use hard‑coded absolute paths** | Makes scripts non‑portable; use relative paths or raw strings (`r"path"`) especially for Windows paths to avoid escape character issues. |
| **Don't ignore duplicates** | They inflate counts and skew results. |
| **Don't use overly generic URLs** | Use DOI‑based links (https://doi.org/...) for reliability. |
| **Don't skip verification** | Mismatches between CSV and BibTeX can cause citation errors. |
| **Don't use default font sizes** | Journal requirements vary; choose fonts and sizes that are publication‑ready. |
| **Don't overcomplicate figures** | Clarity > complexity; avoid excessive data ink. |
| **Don't assume all papers have the same format** | Handle missing data gracefully in scripts. |
| **Don't forget to update the paper when the dataset changes** | Keep manuscript and data in sync. |

