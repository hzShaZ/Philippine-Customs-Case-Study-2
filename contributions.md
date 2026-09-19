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

**Deliverables:** Working end-to-end pipeline, config.py, data_loader.py, audit.py, analysis.ipynb, analysis.html

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

## Marc Ira Irabagon — Summary Tables

**Assigned Features:** Grouped, two-factor grouped, pivot, and top 10 summary generation.

**Core Functions & Modules:**
- `src/summary.py` -> `DataSummarizer`: class handling all summary table generation
- `generate_single_grouped()`, `generate_two_grouped()`, `generate_pivot()`

**Deliverables:** `output/grouped.csv`, `output/grouped_two.csv`, `output/pivot.csv`, `output/top10.csv`

### Commits
- `640ce4f` - feat: imported modules to start the file
- `ac88f8f` - feat: created new class for datasummarizing
- `bc5405c` - feat: add generate_single_grouped and data summarizer
- `2668484` - feat: added top 10 rankings
- `296f8cb` - feat: added categories and pivot table
- `9e62a08` - fix: formatting issues

---

## Arwin A. Abad — Main Pipeline Integration, Visualizations & Validation

**Assigned Features:** Main pipeline integration (`main.py`), data visualizations, automated reconciliation checks, and audit trail logging.

**Core Functions & Modules:**
- `main.py`: `main()`
- `src/visualizations.py`: `generate_bar_chart()`, `generate_heatmap()`
- `src/validation.py`: `build_and_check_validation()`, `export_audit_log()`

**Deliverables:** `main.py`, `output/bar.png`, `output/heatmap.png`, `output/validation.csv`, `output/audit_log.csv`

### Commits
- `39c9f6f` - feat (main): integrate validation checks, step 6 audit record, and audit_log exporter
- `6f870c0` - feat (main): integrate chart generation and step 5 audit record
- `7b22df4` - feat (main): integrate numpy benchmark execution and step 4 audit record
- `ce81772` - feat (main): add grouped, top10, and pivot summary outputs with step 3 audit record
- `14aa9b0` - feat (main): add filtering, csv exports, and step 2 audit record
- `4c431b8` - feat (main): add data loading and step 1 audit record
- `e7915fc` - feat: updating main.py
- `bca47f0` - Merge branch 'feature/validation-and-audit' into feature/validation-and-audit
- `c793af8` - feat (validation): add non-zero exit handling and export_audit_log exporter function
- `7b65201` - feat (validation): implement reconciliation checks and validation.csv export
- `21cd1bb` - feat (validation): add function signature, type hints, and metric definitions
- `a07999e` - feat: add generate_heatmap function for origin country and TQ categories
- `56df25b` - feat: add generate_bar_chart function for top 10 dutiable values
- `50399cf` - chore: add visualization dependencies and imports
- `b5365f8` - Merge pull request #1 from hzShaZ/feature/config-and-loader

---

## Abdulaziz F. Macalalad — Performance Benchmarking

**Assigned Features:** Python loop vs vectorized NumPy comparison.

**Core Functions & Modules:**
- `src/benchmark.py` -> `run_numpy_benchmark()`

**Deliverables:** Performance execution metrics and speedup factor verification, feeds into `output/validation.csv`

### Commits
- `dc2e4b5` - feat (benchmark): add tolerance verification check and median performance metrics
- `79657be` - feat (benchmark): implement 5-run timing loop for python loop vs vectorized numpy
- `76274a3` - feat (benchmark): add function signature, docstring, and fixed-seed sampling

---

## Gabriel Agmata — Data Filtering

**Assigned Features:** Two-condition filter and derived column generation.

**Core Functions & Modules:**
- `src/data_filtering.py` -> `filter_and_transform_data()`

**Deliverables:** Filtered dataset with `dutiablevalue_kphp` and `is_high_value` derived columns, feeds into summary and validation steps

### Commits
- `3a324c5` - feat (filter): define filter_and_transform_data with type hints and docstring
- `2cd05b6` - feat (filtering): implement 2-condition filter and zero-row error handling
- `09be285` - feat (filtering): create numerical and categorical derived columns