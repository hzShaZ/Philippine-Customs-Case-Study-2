# Contributions

**Dataset Used:** Philippine Customs 2015 (`2015.csv`)

## Philip Shan Gallego — Project Setup, Pipeline Integration & Documentation

**Assigned Features:** Config setup, data loading class, column validation, audit record structure, control structures, data structures (dict, set, list), two standalone functions, loop. Also integrated the full pipeline (filtering, summary, benchmark, validation, visualization) into main.py, fixed a bug in summary.py, and built the analysis notebook and its HTML export.

**Core Functions & Modules:**
- `config.py` — paths, reference totals from the assignment brief, required columns, filter placeholders
- `src/data_loader.py` -> `CustomsDataLoader`: class with `load()`, `validate_columns()`, `summary_info()`
- `src/audit.py` -> `new_audit_record()`: builds one audit log entry
- `src/audit.py` -> `missing_values_report()`: loops through columns, counts nulls, default parameter on `columns`
- `main.py`: wires together data loading, filtering, summary generation, numpy benchmark, plotting, and validation into one end-to-end pipeline run
- `src/summary.py`: fixed an indentation bug and a `pd.Dataframe` typo that would have crashed on import
- `analysis.ipynb` / `analysis.html`: notebook demonstrating the imported pipeline code, with HTML export

### Commits
- `29cfec5` - Add config.py with paths, reference totals, and filter placeholders
- `8dd56fa` - Add CustomsDataLoader class with load, validate_columns, summary_info
- `2d63fcd` - add data loader and src package init
- `f5eb2ff` - main.py loads csv and hook up loader in main
- `0668ea6` - fix encoding and dtype warning on csv load
- `f9b1c38` - add audit module with record builder and null check
- `c2fba57` - use audit module in main, print missing value counts
- `6f673b2` - Solid, clean setup ready for merge into main
- `bd3ce40` - Moved summary.py from main into src
- `329face` - fix summary.py indentation bug, hook up filtering, summary, benchmark, validation, and plots in main
- `3984e6f` - add generated output files from full pipeline run
- `64bcbbb` - IPYNB notebook
- `f1003a1` - Analysis HTML

---

## [Irabagon Marc Ira] — [Summariazation]

**Assigned Features:** [Data Summarizer]

**Core Functions & Modules:**
- [summary.py]


### Commits
- '640ce4ff'- feat: imported modules to start the file
- 'ac88f8f' - feat: created new class for datasummarizing
- 'bc5405c'- feat: add generate_single_grouped and data summarizer
- '26684843'- feat: added top 10 rankinks
- '296f8cb'- feat: added categories and pivot table
- '9e62a08'- fix: formatting issues
---

## [Teammate 3 Name] — [Assigned Part]

**Assigned Features:** [fill in]

**Core Functions & Modules:**
- [fill in]

**Deliverables:** [fill in]

### Commits
- [fill in as they commit]

---

## [Teammate 4 Name] — [Assigned Part]

**Assigned Features:** [fill in]

**Core Functions & Modules:**
- [fill in]

**Deliverables:** [fill in]

### Commits
- [fill in as they commit]

---

## [Gabriel Agmata] — [Data Filtering]

**Assigned Features:** [data filtering]

**Core Functions & Modules:**
- [data_filtering.py]

### Commits
- 3a324c5 - feat(filter): define filter_and_transform_data with type hints and docstring
- 2cd05b6 - feat(filtering): implement 2-condition filter and zero-row error handling
- 09be285 - feat(filtering): create numerical and categorical derived columns
