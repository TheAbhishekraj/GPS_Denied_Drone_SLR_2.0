# Submission Checklist
## GPS-Denied Drone Navigation: A Systematic Literature Review
### Pre-Submission Quality Control Checklist — Manuscript v2.0

---

**Date Started:** __________  
**Target Journal:** __________  
**Manuscript Version:** v2.0  
**Instructions:** Mark each item ✅ when completed, ❌ if not applicable, or 🔄 if in progress.

---

## PART 1: Pre-Writing and Data Checks

### 1.1 Data Consistency

- [ ] All statistics in the manuscript have been cross-checked against `database_final_231.csv` (see `verification_report.md`)
- [ ] Abstract median ATE RMSE corrected from 0.07 m → **0.080 m**
- [ ] Abstract Sensor Fusion percentage corrected from 41.6% → **39.4%** (91/231)
- [ ] Q1 (0.048 m) and Q3 (0.120 m) ATE percentiles recomputed from raw data and confirmed
- [ ] All category totals sum to N = 231 (navigation methods: 91+49+34+34+14+9 = 231 ✅)
- [ ] Publication year totals sum to N = 231 (3+6+12+8+3+13+21+18+34+29+84 = 231 ✅)
- [ ] Sensor n-values footnote added clarifying N=152 is a subset of 198 ATE reporters
- [ ] Indoor (87.0%) and Outdoor (12.6%) percentages verified from database
- [ ] Real flight 96.1% (222/231) verified from database
- [ ] EuRoC 24.7% (57/231) verified from database
- [ ] Top-4 venue 66.7% (154/231) verified from database
- [ ] No statistics from v1.x drafts remain uncorrected

### 1.2 Figure Quality

- [ ] All figures are saved at ≥ 300 DPI (raster) or in vector format (EPS, SVG, PDF)
- [ ] All figures are readable in both colour and greyscale (colour-blind safe palette used, e.g., Okabe-Ito or ColorBrewer)
- [ ] Each figure has a unique, descriptive file name (e.g., `fig3_ate_boxplot_by_method.pdf`)
- [ ] Figure widths match journal requirements: single column = 3.5 in, double column = 7.16 in
- [ ] All text in figures is legible at the intended print size (minimum 8 pt font after scaling)
- [ ] No figures contain embedded hyperlinks that could break in PDF conversion
- [ ] All axes are labelled with units
- [ ] All legends are inside or adjacent to the figure (not floating)
- [ ] PRISMA flow diagram is complete and compliant with PRISMA 2020
- [ ] Box plots include n values for each group

### 1.3 Reference Completeness

- [ ] All cited papers have a corresponding entry in `references.bib`
- [ ] No uncited entries in `references.bib`
- [ ] All DOIs have been verified (use doi.org to check each one)
- [ ] All conference papers include: authors, title, conference name, year, pages, DOI
- [ ] All journal papers include: authors, title, journal (abbreviated per IEEE style), volume, issue, pages, year, DOI
- [ ] No "(n.d.)" (no date) entries — if a source has no date, verify or exclude
- [ ] No bare URLs used as references (archived with Wayback Machine if web source is necessary)
- [ ] Author names are consistent (no "Smith, J." mixing with "John Smith")

---

## PART 2: Manuscript Formatting Checks

### 2.1 Title and Author Information

- [ ] Title is ≤ 15 words and contains key terms: "GPS-denied", "drone" or "UAV", "systematic review"
- [ ] All authors are listed in the correct order
- [ ] All author affiliations are complete (institution, department, city, country)
- [ ] All author email addresses are correct and institutional
- [ ] Corresponding author is clearly marked
- [ ] All ORCID iDs are included for all authors (format: 0000-0000-0000-0000)

### 2.2 Abstract

- [ ] Abstract is ≤ 250 words (required for IEEE TRO and RA-L)
- [ ] Abstract does not contain citations
- [ ] Abstract does not contain undefined acronyms (SLAM, ATE, RMSE, VIO, EuRoC are defined)
- [ ] Abstract contains: problem statement, method (PRISMA SLR), N (231 papers), key findings, conclusions
- [ ] Corrected statistics are used (ATE RMSE = 0.080 m, Sensor Fusion = 39.4%)

### 2.3 Keywords

- [ ] 5–8 keywords provided (IEEE) or 5–10 (MDPI)
- [ ] Keywords include: GPS-denied navigation, UAV, SLAM, ATE, systematic literature review, sensor fusion
- [ ] Keywords are drawn from IEEE taxonomy or journal-specific keyword list
- [ ] No keyword repeats the title verbatim

### 2.4 Section Structure

- [ ] Manuscript has all required sections: Abstract, Introduction, Methods, Results, Discussion, Conclusions, References
- [ ] All section headings use correct capitalisation and numbering style for target journal
- [ ] No orphan headings (a heading is never the last item on a page with no following text)
- [ ] Introduction ends with a clear statement of research questions (numbered list)
- [ ] Introduction ends with a "Paper Organisation" paragraph
- [ ] Methods includes: search strategy, databases, search string (verbatim), date of search, inclusion/exclusion criteria, PRISMA flow
- [ ] Discussion has a dedicated "Limitations" subsection
- [ ] Conclusions do not simply repeat the Abstract

### 2.5 Figure Captions

- [ ] Every figure has a caption that begins with "Fig. X." (IEEE) or "Figure X." (MDPI)
- [ ] Every figure caption is self-contained (reader can understand the figure without reading the body text)
- [ ] Every figure caption includes the n value for data-based figures
- [ ] No figure caption exceeds 3 sentences without justification

### 2.6 Table Formatting

- [ ] Every table has a caption above the table (IEEE standard)
- [ ] Every table caption is self-contained
- [ ] All tables use horizontal rules only (no vertical lines) — IEEE style
- [ ] All table headings are in bold
- [ ] Units are stated in the column header, not in every cell
- [ ] No table is wider than the column/page width
- [ ] All abbreviations in tables are defined in a table footnote
- [ ] Table VII (ATE statistics) includes: n, min, Q1, median, Q3, max, IQR for each group

### 2.7 Equations and Notation

- [ ] All equations are numbered sequentially: (1), (2), etc.
- [ ] All variables are italicised on first use and defined
- [ ] Vectors are bold, scalars are italic (consistent throughout)
- [ ] All equation punctuation follows the sentence (period or comma after inline equations)

---

## PART 3: IEEE-Specific Checks

- [ ] Document class: `\documentclass[journal]{IEEEtran}` (for TRO/RA-L) or `\documentclass[conference]{IEEEtran}` (for IROS/ICRA)
- [ ] Two-column layout active and no manual column breaks inserted
- [ ] `\IEEEPARstart` used for the opening paragraph of the Introduction
- [ ] `\IEEEauthorblockN` and `\IEEEauthorblockA` used for author blocks
- [ ] `\begin{IEEEkeywords}` used for keywords section
- [ ] All figures use `\begin{figure}` (single column) or `\begin{figure*}` (double column)
- [ ] All tables use `\begin{table}` (single column) or `\begin{table*}` (double column)
- [ ] Citations use `\cite{}` with numeric keys; ranges use `\cite{ref1,ref2}` (IEEEtran formats automatically)
- [ ] `\bibliographystyle{IEEEtran}` used
- [ ] Manuscript compiled without LaTeX errors or warnings
- [ ] Final PDF checked for: correct font embedding, no missing glyphs, hyperlinks functional
- [ ] Page count is within journal limits (TRO: ~12–14 pp; RA-L: ≤8 pp excluding refs)
- [ ] No headers, footers, or page numbers in submitted manuscript (IEEEtran removes these)
- [ ] All figures are placed at top or bottom of columns, not inline mid-paragraph
- [ ] IEEE copyright notice added if submitting to a conference proceedings

---

## PART 4: MDPI-Specific Checks (Sensors / Drones)

- [ ] MDPI LaTeX template downloaded from mdpi.com/authors/latex
- [ ] `\documentclass{Definitions/mdpi}` used
- [ ] Journal name specified: `\Journal{Sensors}` or `\Journal{Drones}`
- [ ] Author contributions statement written in CRediT format (see Section 6 of this checklist)
- [ ] MDPI-formatted abstract (max 200 words; one paragraph)
- [ ] "Highlights" section included (3–5 bullet points summarising key results) — MDPI optional but recommended
- [ ] References in numbered Vancouver style with DOI
- [ ] "Data Availability Statement" includes the Zenodo DOI
- [ ] "Conflicts of Interest" statement included
- [ ] APC invoice details confirmed (institution billing or personal)
- [ ] If submitting to a Special Issue: special issue name and editor confirmed with journal office

---

## PART 5: Reference Checks

- [ ] Reference list is in alphabetical order (MDPI) or order of citation (IEEE) — consistent with journal style
- [ ] Every reference cited in text appears in the reference list
- [ ] Every reference in the list is cited in the text
- [ ] All DOIs formatted as: `https://doi.org/10.XXXX/XXXXX` (full URL form for MDPI)
- [ ] For IEEE: DOIs formatted as plain numbers per IEEEtran style: `doi: 10.XXXX/XXXXX`
- [ ] Journal name abbreviations are IEEE-standard (use IEEEabrv.bib file)
- [ ] No broken DOIs (all checked via doi.org)
- [ ] All web references include access date: "[Online]. Available: URL. [Accessed: Day-Mon-Year]"
- [ ] Author names: first name abbreviated (J. Smith, not John Smith) — IEEE style
- [ ] Volume and issue numbers present for all journal articles
- [ ] Page numbers present for all journal and conference articles (if paginated)
- [ ] No duplicate references
- [ ] Dissertation/thesis references include: university, city, degree type, year
- [ ] arXiv preprints include: arXiv identifier and year (note: may not be accepted as primary references by IEEE TRO)

---

## PART 6: Ethical and Compliance Checks

### 6.1 Data Availability Statement

- [ ] Data Availability Statement is included in the manuscript
- [ ] Statement references the Zenodo DOI for `database_final_231.csv`
- [ ] Statement specifies which data are openly available and which (if any) are restricted
- [ ] Example: *"The systematic review database (N = 231) and analysis scripts are openly available at Zenodo: https://doi.org/10.5281/zenodo.XXXXXXX (CC BY 4.0)."*

### 6.2 Conflict of Interest

- [ ] Conflict of Interest statement included
- [ ] If no conflicts: *"The authors declare no conflict of interest."*
- [ ] If funding received: funding body named and grant number provided
- [ ] Funders had no role in: study design, data collection, analysis, interpretation, or publication decision

### 6.3 Funding Statement

- [ ] Funding statement included (or "This research received no external funding")
- [ ] Grant numbers included for all funding sources
- [ ] Acknowledgements section thanks colleagues who assisted but did not qualify for authorship

### 6.4 Author Contributions (CRediT Taxonomy)

- [ ] Author contributions listed using CRediT roles (required for MDPI; recommended for IEEE):
  - Conceptualization
  - Methodology
  - Software
  - Validation
  - Formal Analysis
  - Investigation
  - Resources
  - Data Curation
  - Writing – Original Draft
  - Writing – Review & Editing
  - Visualization
  - Supervision
  - Project Administration
  - Funding Acquisition
- [ ] Every author has at least one CRediT role
- [ ] Contributions are accurate and agreed upon by all authors
- [ ] All authors have read and approved the final manuscript

### 6.5 ORCID

- [ ] All authors have ORCID iDs (register free at orcid.org if not already registered)
- [ ] ORCID iDs verified and added to the manuscript author block
- [ ] ORCID iDs linked in the submission portal (IEEE Author Center / MDPI Susy)

### 6.6 Ethical Statement

- [ ] If human subjects data collected: IRB approval stated
- [ ] If no human subjects: *"Not applicable"* in the Ethics section (required by MDPI)
- [ ] This is an SLR of published literature — no primary data collection — state this clearly

---

## PART 7: Supplementary Materials Checks

- [ ] Supplementary materials described in the main manuscript with explicit reference: "(see Supplementary Materials, Table S1)"
- [ ] Each supplementary file is numbered sequentially: Table S1, Table S2, Figure S1, etc.
- [ ] Supplementary zip archive created: `GPS_Denied_SLR_Supplementary.zip`
- [ ] Archive contains: `database_final_231.csv`, `README.md`, analysis scripts, high-res figures
- [ ] `README.md` template completed (see `supplementary_materials.md`)
- [ ] Data dictionary completed for all columns of `database_final_231.csv`
- [ ] Supplementary archive uploaded to Zenodo and DOI obtained
- [ ] Supplementary archive uploaded to journal submission portal (ScholarOne or Susy)
- [ ] File sizes within journal limits (IEEE ScholarOne: 25 MB per file; MDPI: 100 MB total)
- [ ] Supplementary files open correctly in standard software (Excel, Python, text editor)

---

## PART 8: Cover Letter Guidance

### 8.1 Structure of Cover Letter

A strong cover letter should include the following elements in order:

1. **Opening paragraph:** State the title, the manuscript type (systematic literature review), and the requested journal.
2. **Scope statement:** Explain why this manuscript fits the journal's scope. Be specific — reference the journal's aims and the paper's contribution to that scope.
3. **Novelty statement:** State clearly what is new about this work in 3–5 bullet points.
4. **Key findings:** List the 3 most important quantitative findings from the manuscript.
5. **Data availability:** Note that the full dataset is openly available at Zenodo.
6. **Suggested reviewers:** Provide 3–5 suggested reviewers with name, institution, and email, chosen for expertise in GPS-denied navigation and SLR methodology.
7. **Exclusion list (optional):** List any reviewers who should be excluded due to conflict of interest.
8. **Closing:** Confirm all authors have approved the submission, there is no dual submission, and the work is original.

### 8.2 Journal-Specific Scope Statements

**IEEE TRO:**
> *"This manuscript presents a PRISMA-compliant systematic literature review of GPS-denied UAV navigation, synthesising 231 papers (2013–2023) through quantitative meta-analysis of Absolute Trajectory Error RMSE. This work aligns with IEEE Transactions on Robotics' mission to publish research advancing autonomous systems and robot motion, providing the field with an evidence-based synthesis that is directly actionable for robotics researchers."*

**IEEE RA-L:**
> *"This letter presents a systematic, data-driven characterisation of GPS-denied UAV navigation performance across 231 papers, providing the field's first open, PRISMA-compliant benchmark database. This aligns with IEEE Robotics and Automation Letters' focus on timely, high-impact contributions to autonomous systems research."*

**Sensors (MDPI):**
> *"This systematic review synthesises multi-modal sensing approaches for GPS-denied drone navigation across 231 primary studies, providing a sensor-stratified analysis of positioning accuracy. This aligns directly with Sensors' scope in measurement science, sensor integration, and UAV sensing applications."*

**Drones (MDPI):**
> *"This systematic literature review on GPS-denied drone navigation synthesises 231 papers (2013–2023) and provides the field's first open benchmark database of navigation performance metrics. This work aligns directly with Drones' mission to advance knowledge of unmanned aerial systems across indoor, outdoor, and complex environments."*

### 8.3 Novelty Statement (Use in Cover Letter)

> The key novel contributions of this manuscript are:
> 1. **First PRISMA-compliant SLR** of GPS-denied UAV navigation covering all modalities (visual, LiDAR, inertial, RF) and both indoor and outdoor environments.
> 2. **Quantitative meta-analysis** of ATE RMSE across 198 papers (median: 0.080 m, IQR: 0.048–0.120 m), enabling for the first time a data-driven comparison of navigation method performance.
> 3. **Openly available, reproducible database** (N = 231, Zenodo DOI: [insert DOI]) with data dictionary, analysis scripts, and PRISMA checklist.
> 4. **Benchmark diversity analysis** revealing that EuRoC dominates 24.7% of studies, raising questions about over-fitting to a single dataset.
> 5. **Outdoor deployment gap** quantified: only 12.6% of papers test in outdoor environments, identifying the field's most critical open challenge.

### 8.4 Suggested Reviewers

Include 3–5 experts in the cover letter. Choose researchers who:
- Have published SLRs or surveys in robotics/UAV navigation (methodological expertise)
- Have published primary research in GPS-denied navigation (domain expertise)
- Are NOT co-authors, recent collaborators, or from the same institution as any author
- Have publicly available email addresses (from their lab website or recent paper)

---

## PART 9: Post-Submission Checks

- [ ] Submission confirmation email received and saved
- [ ] Manuscript number recorded: __________
- [ ] Submission date recorded: __________
- [ ] Target decision date calculated (typical review: 6–12 weeks for IEEE, 4–8 weeks for MDPI)
- [ ] Reminder set to follow up if no decision in 12 weeks (IEEE) or 8 weeks (MDPI)
- [ ] Preprint posted to arXiv (cs.RO) if permitted by target journal (check Sherpa/Romeo at sherpa.ac.uk/romeo)
- [ ] Zenodo deposit published (or set to publish on acceptance)
- [ ] All authors informed of submission and manuscript number

### 9.1 Responding to Reviewers

When reviews are received:

- [ ] Read all reviews before responding to any
- [ ] Identify: major revisions, minor revisions, and outright rejections
- [ ] Prepare a point-by-point response letter (one response per reviewer comment)
- [ ] For each comment: quote the original comment, state your response, and quote the revised text
- [ ] Accept all reasonable suggestions, even if minor; explain (politely) why any suggestion was not adopted
- [ ] Highlight all changes in the revised manuscript (using track changes or coloured text)
- [ ] Complete revision within the journal's deadline (typically 30–90 days)
- [ ] Re-check statistics and figures after revision
- [ ] Re-run plagiarism check after revision

---

## PART 10: Final Sign-Off Table

Complete this table before clicking "Submit" in the journal portal.

| Check Category | Completed? | Date | Initials |
|---|---|---|---|
| Data consistency (verification report reviewed) | ☐ | __________ | ______ |
| All discrepancies corrected | ☐ | __________ | ______ |
| Figures at correct DPI / vector format | ☐ | __________ | ______ |
| References verified (DOIs, formatting) | ☐ | __________ | ______ |
| Abstract within word limit | ☐ | __________ | ______ |
| Ethical statements complete | ☐ | __________ | ______ |
| Author contributions (CRediT) complete | ☐ | __________ | ______ |
| ORCID iDs confirmed for all authors | ☐ | __________ | ______ |
| Supplementary archive ready and uploaded | ☐ | __________ | ______ |
| Zenodo DOI obtained and cited in manuscript | ☐ | __________ | ______ |
| Plagiarism check passed (< 15%) | ☐ | __________ | ______ |
| Grammar/style check passed | ☐ | __________ | ______ |
| Cover letter written and proofread | ☐ | __________ | ______ |
| All authors have approved the final manuscript | ☐ | __________ | ______ |
| Submission portal metadata completed | ☐ | __________ | ______ |
| **FINAL SUBMISSION APPROVED** | ☐ | __________ | ______ |

---

*End of Submission Checklist — v1.0 — 2026-07-11*
