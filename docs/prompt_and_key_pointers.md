# Prompts and Key Pointers for Researchers

## Useful Prompts for AI (e.g., ChatGPT, Claude) When Conducting a Review

| Use Case | Prompt |
|----------|--------|
| **Data extraction** | "Extract the following fields from this paper: title, authors, year, sensor type, navigation method, metric, accuracy value." |
| **Deduplication** | "Identify duplicate entries in this CSV based on the DOI column." |
| **Figure generation** | "Write Python code to create a boxplot of ATE RMSE grouped by sensor type." |
| **Interpretation** | "Based on the following table, what are the key takeaways regarding sensor fusion?" |
| **Writing** | "Draft a discussion section comparing our findings with previous systematic reviews." |
| **Verification** | "Cross-check all numbers in the manuscript against the source CSV and flag any discrepancies (e.g., ATE RMSE values or percentages)." |
| **Finalization** | "Insert all figures into the manuscript markdown replacing the placeholders and render the PRISMA diagram using Mermaid." |


## Key Pointers for a Successful Systematic Review

- **Define a clear scope** – avoid being too broad or too narrow.
- **Use multiple databases** – to minimise publication bias.
- **Record your search strategy** – date, databases, keywords, filters.
- **Use a PRISMA flow diagram** – to show the number of papers at each stage.
- **Automate repetitive tasks** – cleaning, deduplication, figure generation.
- **Keep your data open** – share your dataset and scripts for reproducibility.
- **Cite your sources** – use a consistent referencing style.
- **Get feedback early** – from supervisors or peers.

## Checklist Before Submission

- [ ] Have I answered all research questions?
- [ ] Are all figures and tables correctly referenced in the text?
- [ ] Is the reference list complete and consistent?
- [ ] Have I checked for plagiarism and typos?
- [ ] Does my methodology align with PRISMA guidelines?
- [ ] Are my datasets and scripts available for readers?

---

*These prompts and pointers are based on experience from this SLR and can be adapted for future projects.*



# 🧠 Complete AI Prompt Engineering Guide for Systematic Reviews

This guide provides a **structured thinking framework** for using AI (ChatGPT, Claude, etc.) effectively in a systematic review. It covers:

1. **How to think** – questions you must ask yourself before prompting.
2. **What to prompt** – ready‑to‑use prompts for each phase.
3. **How to check** – checkpoints to validate AI output.
4. **How to track** – progress tracking tables.

---

## 📌 Phase 0: Planning and Scoping

### Questions to Ask Yourself (Before Prompting)

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is the core research question? | Defines inclusion/exclusion criteria. |
| 2 | What are the key terms and synonyms? | Builds the search string. |
| 3 | Which databases should I search? | Ensures comprehensive coverage. |
| 4 | What is the time frame? | Sets boundaries (e.g., 2015–2025). |
| 5 | What is the publication type? | Peer‑reviewed journals, conferences, preprints? |
| 6 | What is the language? | Usually English. |

### Prompt Examples (Copy & Paste)

**To define scope:**
> *“I am conducting a systematic review on [topic]. Help me formulate a clear research question using the PICO (Population, Intervention, Comparison, Outcome) framework. Also suggest synonyms and alternative terms for the search string.”*

**To build a search string:**
> *“Generate a Boolean search string for [topic] that combines keywords for [concept 1] and [concept 2]. Include synonyms and database‑specific syntax for IEEE Xplore, Scopus, and Web of Science.”*

### Checkpoints
- [ ] Research question is clear and answerable.
- [ ] Search string is tested on at least one database.
- [ ] Inclusion/exclusion criteria are documented.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Define research question | ☐ | | |
| Build search string | ☐ | | |
| Select databases | ☐ | | |
| Document criteria | ☐ | | |

---

## 📌 Phase 1: Search and Screening

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | How many papers did each database return? | Understands coverage. |
| 2 | How many duplicates exist? | Prevents double‑counting. |
| 3 | What are my inclusion/exclusion criteria? | Screens systematically. |
| 4 | Am I using title/abstract screening or full‑text? | Balances thoroughness vs. time. |
| 5 | Do I need a PRISMA flow diagram? | Standard reporting requirement. |

### Prompt Examples

**To deduplicate:**
> *“I have a CSV file with columns: Title, Authors, Year, DOI. Write a Python script to identify and remove duplicate entries based on DOI and Title, keeping the first occurrence. Output a cleaned CSV and a report of removed duplicates.”*

**To create a PRISMA flow diagram:**
> *“Based on these numbers: [initial hits], [duplicates removed], [title/abstract screened], [full‑text assessed], [included studies], generate a PRISMA flow diagram in Mermaid format that I can embed in my paper.”*

**To screen abstracts:**
> *“Here is the abstract of a paper: [paste abstract]. Based on my inclusion criteria ([list criteria]), should this paper be included? Provide a reason.”*

### Checkpoints
- [ ] Duplicates removed (check count).
- [ ] Title/abstract screening completed.
- [ ] Full‑text screening completed.
- [ ] PRISMA flow diagram drafted.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Database search executed | ☐ | | |
| Duplicates removed | ☐ | | |
| Title/abstract screened | ☐ | | |
| Full‑text retrieved | ☐ | | |
| Full‑text screened | ☐ | | |
| PRISMA diagram created | ☐ | | |

---

## 📌 Phase 2: Data Extraction

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What fields do I need to extract? | Defines the database schema. |
| 2 | How do I handle missing data? | Avoids bias. |
| 3 | Are there ambiguous categories (e.g., sensor types)? | Standardises classification. |
| 4 | Who will extract data (manual or AI)? | Determines reliability. |
| 5 | How do I resolve disagreements? | Ensures consistency. |

### Prompt Examples

**To design the extraction form:**
> *“I am conducting a systematic review on [topic]. Suggest a comprehensive list of fields to extract from each paper, organised into categories: (a) bibliographic, (b) methodological, (c) sensor/technology, (d) performance metrics, (e) environment, (f) limitations.”*

**To extract structured data from a paper:**
> *“Extract the following fields from this paper: Title, Authors, Year, Journal, DOI, Sensor Type, Navigation Method, Localization Metric, Reported Accuracy, Environment (Indoor/Outdoor), Dataset, Real Flight (Yes/No). If a field is not mentioned, write ‘Not specified’. Return as a CSV row.”*

**To standardise sensor types:**
> *“I have a list of sensor types from papers: [list]. Group them into standard categories: e.g., ‘Monocular camera; IMU’, ‘LiDAR; IMU’, etc. Also suggest a master list of categories.”*

### Checkpoints
- [ ] Data extraction form is defined.
- [ ] At least 5 papers extracted manually to test form.
- [ ] All papers extracted (or extracted by AI with manual verification).
- [ ] Missing data is documented.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Define extraction fields | ☐ | | |
| Test extraction on 5 papers | ☐ | | |
| Extract all papers | ☐ | | |
| Verify extracted data | ☐ | | |

---

## 📌 Phase 3: Data Cleaning and Preparation

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | Are there duplicate entries? | Inflates results. |
| 2 | Are there missing values? | Affects analysis. |
| 3 | Are categorical variables standardised? | Enables grouping. |
| 4 | Are numeric values correctly typed? | Prevents calculation errors. |
| 5 | Are there outliers? | May skew results. |

### Prompt Examples

**To clean data:**
> *“I have a CSV with columns: [list]. Write a Python script that: (1) removes duplicate rows based on ‘Citation Key’, (2) replaces missing values in ‘Sensor Type’ with ‘Not specified’, (3) standardises ‘Indoor/Outdoor’ to ‘Indoor’, ‘Outdoor’, or ‘Mixed’, (4) converts ‘Reported numeric value’ to float, (5) drops rows where ‘ATE RMSE (m)’ is missing but keeps others. Save the cleaned data.”*

**To detect outliers:**
> *“Given this data of ATE RMSE values: [list or column], identify outliers using the IQR method (1.5 × IQR). List the outliers and suggest whether they should be excluded.”*

**To generate descriptive statistics:**
> *“Calculate the mean, median, min, max, standard deviation, and count for the ‘Reported numeric value’ column, grouped by ‘Sensor Type’. Output as a table.”*

### Checkpoints
- [ ] No duplicate rows (check count).
- [ ] Missing values documented.
- [ ] Categorical variables standardised.
- [ ] Numeric columns are numeric.
- [ ] Outliers identified (decision made on handling).

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Deduplicate | ☐ | | |
| Handle missing values | ☐ | | |
| Standardise categories | ☐ | | |
| Fix data types | ☐ | | |
| Outlier analysis | ☐ | | |

---

## 📌 Phase 4: Analysis and Visualization

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What are the key trends I want to show? | Guides figure selection. |
| 2 | Which statistics are most informative? | Mean, median, distributions. |
| 3 | Are there subgroup differences? | Reveals patterns. |
| 4 | How do I handle small sample sizes? | Avoid over‑interpretation. |
| 5 | What is the best way to visualise each type of data? | Ensures clarity. |

### Prompt Examples

**To generate a publication trend figure:**
> *“Write Python code to create a bar chart of publications per year (2015–2025) from a CSV column ‘Year’. Add value labels on top of each bar. Save as PNG.”*

**To generate a sensor‑wise accuracy boxplot:**
> *“Create a boxplot of ATE RMSE grouped by Sensor Type, ordered by median. Show individual data points with a swarm overlay. Include sample size (n) below each group. Use a colour‑blind‑friendly palette.”*

**To generate a comparison table:**
> *“Create a table comparing median ATE RMSE, IQR, and count for each sensor type. Sort by median (lowest first). Export as CSV and Markdown.”*

**To interpret findings:**
> *“Based on this table of sensor‑wise median ATE RMSE, what are the key takeaways? Which sensor types perform best and why? Write a 200‑word summary suitable for a Discussion section.”*

### Checkpoints
- [ ] All planned figures generated.
- [ ] Figures are publication‑ready (font sizes, colours, labels).
- [ ] Statistical tests (if needed) are appropriate.
- [ ] Findings are interpreted with researcher remarks.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Generate trend figure | ☐ | | |
| Generate sensor figure | ☐ | | |
| Generate method figure | ☐ | | |
| Generate accuracy distribution | ☐ | | |
| Generate sensor‑wise comparison | ☐ | | |
| Interpret findings | ☐ | | |

---

## 📌 Phase 5: Interpretation and Writing

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What are the main findings in the context of existing literature? | Shows contribution. |
| 2 | Are there contradictions or surprises? | Highlight interesting results. |
| 3 | What are the limitations of this review? | Shows transparency. |
| 4 | What are the implications for practice and future research? | Adds value. |
| 5 | How do my findings compare with previous reviews? | Positions the work. |

### Prompt Examples

**To draft the Discussion:**
> *“Based on the following findings: [list key results]. Write a Discussion section for a systematic review on [topic]. Structure it into: (1) Summary of findings, (2) Comparison with previous reviews, (3) Implications, (4) Limitations, (5) Future research directions. Use a formal academic tone.”*

**To draft the Limitations:**
> *“Given that our review includes only English‑language, peer‑reviewed papers from 2015–2025, and we used a single‑extractor approach. What are the other limitations we should mention? Also suggest how these limitations affect the interpretation of results.”*

**To draft the Conclusions:**
> *“Write a Conclusions section that succinctly answers the research question, highlights the main contributions, and suggests actionable next steps for practitioners and researchers.”*

### Checkpoints
- [ ] Introduction, Methods, Results, Discussion, Conclusions drafted.
- [ ] All figures and tables are referenced in the text.
- [ ] Limitations are explicit.
- [ ] Future work is proposed.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Draft Introduction | ☐ | | |
| Draft Methods | ☐ | | |
| Draft Results | ☐ | | |
| Draft Discussion | ☐ | | |
| Draft Conclusions | ☐ | | |
| Cross‑reference figures/tables | ☐ | | |

---

## 📌 Phase 6: Verification and Submission

### Questions to Ask Yourself

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | Are all citations correctly formatted? | Prevents rejection. |
| 2 | Are the figures and tables numbered consistently? | Professional presentation. |
| 3 | Is the reference list complete? | Checks completeness. |
| 4 | Have I checked for spelling and grammar? | Professionalism. |
| 5 | Have I shared the dataset and scripts? | Reproducibility. |

### Prompt Examples

**To verify reference consistency:**
> *“I have a CSV file with 231 Citation Keys and a bibliography.txt file with numbered entries. Write a Python script to check that every Citation Key in the CSV appears in the bibliography, and vice versa. Report any mismatches.”*

**To generate a submission checklist:**
> *“Create a final submission checklist for a systematic review paper, covering: (a) manuscript structure, (b) figures and tables, (c) references, (d) supplementary materials, (e) ethical considerations, (f) journal‑specific requirements.”*

### Checkpoints
- [ ] All files are consistent (CSV ↔ BibTeX ↔ bibliography).
- [ ] Manuscript is proofread.
- [ ] Supplementary materials (data, scripts) are organised.
- [ ] Journal formatting guidelines are followed.

### Progress Tracker
| Task | Status | Date | Notes |
|------|--------|------|-------|
| Verify file consistency | ☐ | | |
| Proofread manuscript | ☐ | | |
| Prepare supplementary materials | ☐ | | |
| Format for target journal | ☐ | | |
| Submit | ☐ | | |

---

## 📋 Master Progress Tracker (Copy This Table)

| Phase | Task | Status | Due Date | Notes |
|-------|------|--------|----------|-------|
| 0 | Define research question | ☐ | | |
| 0 | Build search string | ☐ | | |
| 1 | Execute database search | ☐ | | |
| 1 | Remove duplicates | ☐ | | |
| 1 | Title/abstract screening | ☐ | | |
| 1 | Full‑text screening | ☐ | | |
| 1 | PRISMA flow diagram | ☐ | | |
| 2 | Define extraction fields | ☐ | | |
| 2 | Extract data | ☐ | | |
| 3 | Clean data | ☐ | | |
| 3 | Standardise categories | ☐ | | |
| 4 | Generate figures | ☐ | | |
| 4 | Generate tables | ☐ | | |
| 4 | Interpret findings | ☐ | | |
| 5 | Draft manuscript | ☐ | | |
| 5 | Add references | ☐ | | |
| 6 | Verify consistency | ☐ | | |
| 6 | Final proofread | ☐ | | |
| 6 | Submit | ☐ | | |

---

## 🔁 The “Plan‑Do‑Check‑Act” Cycle for Each Phase

| Step | Action | Example |
|------|--------|---------|
| **Plan** | Define what you need and what question to ask. | *“I need to generate a boxplot of ATE RMSE by sensor type.”* |
| **Do** | Use the prompt to generate output (code, text, analysis). | Paste the prompt into ChatGPT/Claude. |
| **Check** | Verify the output against your requirements. | Does the boxplot have correct labels? Is it sorted? |
| **Act** | Refine the output if needed, or proceed to the next task. | Adjust colours, font sizes, or ask for improvements. |

## 🧠 Key Insight: How to Ask Clear Questions

1. **Be specific** – mention columns, data types, expected output.
2. **Provide context** – share a sample row or a snippet of your data.
3. **Define constraints** – “only keep sensors with at least 3 papers”, “use colour‑blind‑friendly palette”.
4. **Request both code and explanation** – so you understand and can modify later.
5. **Ask for validation steps** – “also include a verification step to count unique keys.”

---

## 📁 Save This File

Save this as:
```
docs/prompt_and_key_pointers.md
```

You now have a complete, reusable guide for using AI throughout any systematic review.  

**Next step:** Let me know if you want help creating the actual `paper_final.md` using the report and tables you generated, or if you need a PRISMA flow diagram template.