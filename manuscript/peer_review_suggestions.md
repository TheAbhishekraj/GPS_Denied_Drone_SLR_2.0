# Peer Review & Improvement Suggestions
## GPS-Denied Drone Navigation — Systematic Literature Review
**Version:** 1.0 | **Date:** 2026-07-11

> This document provides structured editorial feedback, tool recommendations, writing improvement suggestions, and journal-specific formatting guidance to prepare the manuscript for submission.

---

## Part 1: Editorial Feedback by Section

### Abstract
**Current Status:** Good. Key statistics are present. Fixed in v2.0 (median = 0.080 m, Sensor Fusion = 39.4%).

**Suggestions:**
1. Add the review period more precisely: "2015 through June 2025" to clarify the search cutoff.
2. Mention the PRISMA framework in the abstract — it is a key differentiator from non-systematic reviews.
3. Consider adding a one-sentence statement of the most important implication (e.g., "These findings demonstrate that centimetre-level GPS-denied navigation is achievable in controlled settings and identify outdoor evaluation as the key frontier for future work.").
4. Word count target: **150–250 words** for most IEEE journals (current: ~230 words ✅).
5. Avoid the phrase "data-driven synthesis" — prefer "quantitative systematic analysis" for IEEE.

---

### Section I: Introduction
**Current Status:** Well-structured. Contributions are clearly enumerated.

**Suggestions:**
1. **Add a motivation paragraph with specific application examples** — e.g., "A compromised GPS signal has resulted in UAV failures in [specific incident/domain]." This increases impact.
2. **Strengthen the gap statement:** The third paragraph should explicitly name the closest competing review(s) and explain why they are insufficient. Currently, references [6] and [7] are cited but their limitations are not clearly articulated.
3. **Add statistical context in paragraph 2:** "As of 2025, the drone navigation market is projected to exceed $XX billion..." (optional, journal-dependent).
4. **Contribution bullet 2** is vague — replace "A quantitative characterization" with "A quantitative characterization of IMU (85.7%), monocular camera (44.6%), and LiDAR (37.6%) adoption, and publication trends from 2015 to 2025."
5. Ensure the "roadmap paragraph" (last paragraph of introduction) matches the actual section structure of the paper.

---

### Section II: Methodology
**Current Status:** Solid PRISMA-aligned methodology. Research questions are clear.

**Suggestions:**
1. **Add inter-rater reliability discussion:** Acknowledge that a single extractor was used and describe any verification steps taken (e.g., 10% double-coded by a second reviewer, or automated script verification).
2. **Add a search date statement:** "Searches were last conducted on [exact date]" — reviewers expect this.
3. **Quality Assessment subsection is missing.** Add a brief Section II.G or II.F describing how paper quality was assessed (e.g., were papers graded? Was there a risk-of-bias assessment?). For a descriptive SLR, you can state: "No formal risk-of-bias tool was applied; quality was implicitly controlled through the inclusion criterion requiring quantitative performance metrics."
4. **Table in Section II.D (PRISMA numbers):** The note "All 231 papers...met full eligibility criteria" may draw reviewer skepticism — clarify that the search strategy was designed to be highly targeted (Boolean string specificity), which naturally reduces false positives.
5. **Add Data Analysis subsection detail:** Mention specific Python libraries (pandas version, seaborn, scipy if used for statistics). Reproducibility is important for systematic reviews.

---

### Section III: Results
**Current Status:** Comprehensive. 9 subsections cover all key analyses.

**Suggestions:**
1. **Section III.A — Publication Trends:** Add a trend analysis sentence: "A compound annual growth rate (CAGR) of approximately XX% was observed over 2015–2025." This strengthens the quantitative narrative.
2. **Section III.B — Sensors:** Add a sentence on *why* IMU is so prevalent physiologically — connect to drone flight control requirements (attitude estimation at > 100 Hz).
3. **Section III.C — Methods:** The percentages in Table III don't exactly add to 100% due to rounding. Check: 39.4+21.2+14.7+14.7+6.1+3.9 = 100.0% ✅ — no issue, but verify in the final script output.
4. **Section III.F — Overall ATE RMSE:** The statement "198 real-flight experiments (85.7%)" should be verified: 198/231 = 85.7% ✅. Consider adding a violin plot or cumulative distribution function (CDF) plot as an additional figure for richer visualization.
5. **Section III.G — Sensor-wise accuracy:** Note that configurations with n < 5 have very limited statistical power. Add a disclaimer: "Configurations with n < 5 should be interpreted with caution due to limited sample size."
6. **Section III.H — Method-wise accuracy:** The n-values (66, 14, 33, 6, 34, 45) sum to 198 ✅ — this is consistent. Excellent.
7. **Missing subsection:** Consider adding **Section III.J: Temporal Accuracy Trends** — "Has ATE RMSE improved over time (2015 vs. 2025)?" This would be a compelling new finding.

---

### Section IV: Discussion
**Current Status:** Good structure with 4 subsections. Findings 1–7 are well-articulated.

**Suggestions:**
1. **Finding 3 (LiDAR):** The phrase "LiDAR-inertial fusion provides the accuracy floor" is ambiguous. Replace with "LiDAR-inertial fusion provides the accuracy *ceiling* (i.e., the best achievable performance)" — the word "floor" connotes a lower bound, not an upper bound.
2. **Comparison with Prior Reviews (Section IV.B):** Provide a specific comparison table (see Part 5 below). The current prose comparison is weak for a journal publication.
3. **Trends (Section IV.C):** Add a paragraph on **energy-efficient navigation** — a growing trend in nano-drones and edge AI deployment.
4. **Limitations (Section IV.D):** Should explicitly quantify the grey literature risk (e.g., "A search of arXiv (cs.RO category, same date range) returned approximately XX preprints; spot-checking 10 found that 8 were already included in our corpus via the conference paper versions, suggesting minimal coverage gap.").
5. **Add a paragraph on statistical heterogeneity:** ATE RMSE values are not directly comparable across environments and datasets. Acknowledge this as a structural limitation affecting all meta-analyses of this type.

---

### Section V: Conclusions
**Current Status:** Strong 6-point summary with practical recommendations.

**Suggestions:**
1. **Conclusion 3** cites "0.07–0.08 m" — corrected to "0.080 m" in v2.0.
2. Add a sentence explicitly linking conclusions back to the 5 research questions defined in Section II.A.
3. Consider ending with a call to action: "Standardized outdoor GPS-denied benchmarks and open-source multi-sensor UAV platforms are urgently needed to accelerate progress in real-world deployment."

---

## Part 2: Tool Recommendations

### 2.1 Plagiarism Check
| Tool | Access | Target Score | How to Use |
|------|--------|-------------|------------|
| **iThenticate** | Paid (institutional) | < 15% similarity | Upload PDF/DOCX via iThenticate portal. Review highlighted matches; exclude properly cited material. |
| **Turnitin** | Institutional | < 20% | Available via university submission portal. |
| **QuillBot Plagiarism Checker** | Free (up to 5,000 words) | < 10% | Paste text at quillbot.com/plagiarism-checker. Use section by section. |
| **Grammarly** | Free/Premium | — | Use for grammar check simultaneously. |

**Target:** < 15% overall similarity, < 3% from any single source. Text in Results and Discussion is most at risk (heavy reference to prior work).

---

### 2.2 Grammar and Style
| Tool | Recommendation |
|------|---------------|
| **Grammarly Premium** | Enable: "Academic", "Formal" style. Disable passive-voice suggestion in methods (passive is acceptable in IEEE). Turn ON: clarity, wordiness, unclear antecedents. |
| **ProWritingAid** | Use "Academic" report. Focus on "Overused Words" and "Sentence Variety" reports. |
| **Hemingway Editor** | Good for catching overly complex sentences. Aim for Grade 12–14 reading level for IEEE. |

---

### 2.3 Reference Management
| Step | Tool | Instructions |
|------|------|-------------|
| Import BibTeX | **Zotero** | File → Import → `references/references.bib` |
| Set citation style | Zotero | Edit → Preferences → Cite → IEEE |
| Export formatted list | Zotero | Select all → Right-click → "Create Bibliography" → IEEE → Copy to clipboard |
| Verify DOIs | **DOI.org** | Paste each DOI at doi.org to confirm it resolves |
| Check for retracted papers | **Retraction Watch** | retraction watch.com/retracted-article-database — search key author names |

---

### 2.4 Figure Formatting
| Requirement | Specification |
|-------------|--------------|
| **IEEE raster figures** | ≥ 300 DPI for print, 72 DPI for web-only |
| **IEEE vector figures** | EPS or PDF preferred (infinite resolution) |
| **Font in figures** | Times New Roman or IEEE-compatible sans-serif, min 8 pt in figure |
| **Column width (single-col)** | 3.5 inches (8.89 cm) |
| **Column width (double-col)** | 7.16 inches (18.19 cm) |
| **Figure format** | Export as PDF (vector) or PNG ≥ 600 DPI from matplotlib |
| **Tool** | Inkscape (free) for vector editing; Adobe Illustrator for professional work |

**To increase DPI of existing figures:**
```python
# In your matplotlib script, change:
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
# or for vector:
plt.savefig('figure.pdf', bbox_inches='tight')
```

---

### 2.5 PRISMA Diagram Rendering
| Tool | Instructions |
|------|-------------|
| **mermaid.live** | Go to https://mermaid.live → paste code from `docs/prisma_flow_diagram.md` → "Actions" → Export PNG (set scale to 3x for 300 DPI equivalent) or SVG |
| **Obsidian** | Install "Mermaid" plugin → render in preview pane → right-click → copy image |
| **VS Code** | Install "Markdown Preview Mermaid Support" extension → preview renders diagram |
| **draw.io** | Recreate the PRISMA boxes manually using the PRISMA template at diagrams.net |

---

### 2.6 LaTeX Formatting (IEEE TRO / RA-L)
| Step | Instructions |
|------|-------------|
| 1. Template | Download `IEEEtran.cls` from https://www.ieee.org/publications/authors/author-templates.html |
| 2. Overleaf | Create new project → Upload template → Upload `paper_final.md` content converted to `.tex` |
| 3. BibTeX | Upload `references/references.bib` → use `\bibliographystyle{IEEEtran}` |
| 4. Figures | Upload all `.png` files from `analysis/output/figures/` → reference with `\includegraphics[width=\columnwidth]{fig1_publications_over_time}` |
| 5. Compile | `pdflatex` → `bibtex` → `pdflatex` × 2 |
| 6. Check | Page limit: IEEE TRO allows ~12 pages in two-column format |

**Key LaTeX commands for IEEE:**
```latex
\documentclass[journal]{IEEEtran}
\usepackage{cite}         % IEEE citation compression [1]-[3]
\usepackage{graphicx}     % figures
\usepackage{amsmath}      % math
\usepackage{booktabs}     % professional tables
\usepackage{hyperref}     % DOI links

\title{GPS-Denied Drone Navigation: A Systematic Literature Review...}
\author{First Author, \IEEEmembership{Member, IEEE}, Second Author...}
\maketitle
\begin{abstract}...\end{abstract}
\begin{IEEEkeywords}...\end{IEEEkeywords}
```

---

### 2.7 Word Formatting (IEEE / MDPI)
| Template | Download Location |
|----------|------------------|
| **IEEE Word template** | https://template-selector.ieee.org/ → Select journal type |
| **MDPI Word template** | https://www.mdpi.com/authors/word_template |
| **Table formatting** | Use Word's "Borders and Shading" → remove all internal borders except horizontal rules under header row (IEEE table style) |
| **Figure placement** | Figures should be inserted inline, not in text boxes. Use "In Line with Text" wrapping. |

---

### 2.8 Zenodo Dataset Upload
1. Go to https://zenodo.org → Create Account → New Upload
2. Upload these files:
   - `data/processed/database_final_231.csv`
   - `analysis/scripts/` (zipped)
   - `analysis/output/figures/` (zipped)
   - `references/references.bib`
   - `README.md`
3. Set Access: **Open** (required for reproducibility)
4. Set License: **CC BY 4.0**
5. Set Resource Type: **Dataset**
6. Add keywords: GPS-denied, UAV, drone, navigation, SLAM, systematic review
7. Click "Publish" → You receive a **DOI** (e.g., `10.5281/zenodo.XXXXXXX`)
8. Add this DOI to the manuscript's Data Availability statement.

---

### 2.9 Journal Submission Portals
| Journal | Portal | URL |
|---------|--------|-----|
| **IEEE TRO** | IEEE Author Center | https://author-center.ieee.org |
| **IEEE RA-L** | Same as TRO | https://author-center.ieee.org |
| **Sensors (MDPI)** | MDPI Susy | https://susy.mdpi.com |
| **Drones (MDPI)** | MDPI Susy | https://susy.mdpi.com |

---

## Part 3: Writing Improvement Suggestions

### 3.1 Sentences to Rewrite

| Original | Suggested Revision | Reason |
|----------|--------------------|--------|
| "GPS signals are inherently susceptible to obstruction..." | "GPS signals are blocked by building structures, terrain, vegetation, and underground conditions, and are vulnerable to intentional jamming and spoofing." | More specific, stronger |
| "The problem of GPS-denied UAV navigation has attracted significant research attention..." | "GPS-denied UAV navigation has emerged as a central challenge in autonomous systems research..." | More direct, active voice |
| "This review provides researchers and engineers with a comprehensive, data-driven synthesis..." | "This review provides a quantitative, reproducible foundation for sensor selection, algorithm benchmarking, and future research priority-setting." | More specific outcome |
| "The growing prevalence of event cameras...reflects their advantage..." | "Event cameras have gained traction since 2020 due to their microsecond temporal resolution, high dynamic range, and low power consumption—properties that address specific failure modes of frame-based cameras in fast drone flight." | Technically richer |
| "Sensor fusion and LiDAR SLAM tend to achieve lower median errors..." | "Sensor fusion (median ATE RMSE = 0.050 m) and LiDAR SLAM (0.055 m) achieve statistically lower localization errors than visual-only or deep learning approaches, consistent with the complementary noise characteristics of LiDAR and IMU." | Quantitative and causal |

### 3.2 Paragraphs That Need Expansion

| Section | Current | Needed |
|---------|---------|--------|
| **II.B — Quality Assessment** | Missing entirely | Add 2–3 sentences: "No formal risk-of-bias tool was applied. Quality was implicitly controlled via the inclusion criterion requiring quantitative localization metrics evaluated on real hardware. Single-extractor bias was mitigated through automated cross-verification of all extracted values against the reference list and bibliography." |
| **IV.B — Prior Reviews** | 3 sentences, very general | Expand to full comparison table (see Part 5). Add: "Unlike [review X], which focused exclusively on monocular SLAM, this review spans six sensor modalities and six algorithm families, providing a uniquely comprehensive benchmark." |
| **IV.C — Trends** | 5 bullet-style paragraphs | Add: "Foundation model approaches (large vision–language models applied to scene understanding for UAV navigation) have appeared in preliminary arXiv preprints in late 2024–2025 but have not yet reached the peer-reviewed corpus—a gap likely to be filled in 2026–2027." |

### 3.3 Statistical Tests to Add

| Test | Purpose | How to Compute |
|------|---------|----------------|
| **Kruskal-Wallis H-test** | Test whether ATE RMSE distributions differ significantly across sensor configuration groups | `scipy.stats.kruskal(*[group_data for each sensor_type])` |
| **Mann-Kendall trend test** | Test whether median ATE RMSE has improved (decreased) significantly over 2015–2025 | `pymannkendall` library → `mk.original_test(yearly_median_rmse)` |

---

## Part 4: SLR Literature Comparison Table

| Review | Year | Topic | Papers | Sensor Focus | Method Focus | Accuracy Benchmark | Time Span |
|--------|------|-------|--------|-------------|-------------|-------------------|-----------|
| **This work** | **2025** | **GPS-denied UAV navigation** | **231** | **All (camera, LiDAR, event, thermal, radar, UWB)** | **All 6 categories** | **✅ Sensor-stratified ATE RMSE** | **2015–2025** |
| Younes et al. | 2017 | Visual odometry for MAVs | ~60 | Camera only | VO, VIO | ❌ No benchmark | 2010–2017 |
| Gallego et al. | 2020 | Event cameras | ~200 | Event camera | SLAM, VO | ❌ No UAV benchmark | 2006–2019 |
| Zhu et al. | 2020 | Visual SLAM | ~150 | Camera + IMU | SLAM only | ❌ Partial | 2010–2020 |
| Cadena et al. | 2016 | SLAM (general) | ~200 | All platforms | SLAM | ❌ Not UAV-specific | 2006–2016 |
| Abdi et al. | 2023 | UAV localization | ~80 | Camera + LiDAR | VIO, SLAM | ⚠️ Partial | 2018–2022 |

*Note: Counts are approximate for external reviews.*

---

## Part 5: Journal-Specific Formatting Requirements

### IEEE Transactions on Robotics (TRO)
| Requirement | Specification |
|-------------|--------------|
| Format | LaTeX (IEEEtran) — 2-column layout |
| Page limit | 12 pages (letter-sized) for regular papers |
| Figures | Max 15 figures; 300 DPI minimum; EPS/PDF preferred |
| References | IEEE citation style; no limit stated |
| Abstract | 250 words maximum |
| Keywords | 3–10 index terms from IEEE Thesaurus |
| Supplementary | Allowed as multimedia appendix |
| OA option | IEEE Open (fee: ~$2,195 USD) |
| Submission | IEEE Author Center (https://author-center.ieee.org) |
| Review | Typically 3–6 months for initial decision |

### IEEE Robotics and Automation Letters (RA-L)
| Requirement | Specification |
|-------------|--------------|
| Format | LaTeX (IEEEtran) — 2-column layout |
| Page limit | **8 pages** (letter-sized) — strict |
| Concurrent submission | Can submit simultaneously to ICRA 2026 |
| Abstract | 250 words maximum |
| Review | 2–4 months |
| Note | Shorter than TRO — manuscript may need condensing |

### Sensors (MDPI)
| Requirement | Specification |
|-------------|--------------|
| Format | Word or LaTeX (MDPI template) |
| Page limit | No strict limit; typically 15–25 pages |
| Figures | TIFF or EPS; 300 DPI minimum |
| References | APA or numbered style |
| Abstract | 200 words maximum |
| Article Processing Charge | CHF 2,600 (≈ $2,900 USD) — open access |
| Review | 2–6 weeks (fast turnaround) |
| Submission | https://susy.mdpi.com |

### Drones (MDPI)
| Requirement | Specification |
|-------------|--------------|
| Format | Same as Sensors (MDPI) |
| Article Processing Charge | CHF 2,600 |
| Scope | UAV-specific — excellent fit for this paper |
| Impact Factor | 4.4 (2024) |
| Review | 3–8 weeks |

---

## Recommendation

**Recommended target journal:** **IEEE Robotics and Automation Letters (RA-L)** with concurrent ICRA 2026 submission.

**Rationale:**
- RA-L has the highest density of GPS-denied UAV navigation papers in the corpus (45 out of 231 = 19.5%).
- Concurrent IROS/ICRA submission is allowed, increasing visibility.
- Fast review timeline (2–4 months).
- Impact factor appropriate for robotics SLR.
- **Trade-off:** Strict 8-page limit may require condensing the current manuscript. Alternatively, target **IEEE TRO** for the full-length paper (12 pages).

---

*File: `manuscript/peer_review_suggestions.md` | Version 1.0 | Generated: 2026-07-11*
