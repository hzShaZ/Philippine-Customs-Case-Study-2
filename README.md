# 2015 Philippine Customs Data Summary — Group 5

A Python pipeline that loads, filters, summarizes, and visualizes the 2015 Philippine Customs dataset, with validation checks confirming the numbers add up.

## Project Structure
```
group5-case2/
├── config.py              # paths, reference totals, required columns, filter config
├── main.py                # runs the full pipeline
├── README.md
├── contributions.md
├── submission_manifest.txt
├── requirements.txt
├── analysis.ipynb          # notebook demonstrating the imported pipeline code
├── analysis.html           # HTML export of the above
├── data/
│   └── 2015.csv             # raw dataset, not committed
├── output/                  # generated summary csvs, plots, validation and audit logs
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # CustomsDataLoader, loads and validates the csv
│   ├── audit.py               # audit record builder, missing value checks
│   ├── data_filtering.py      # two-condition filter, derived columns
│   ├── benchmark.py            # numpy vs loop comparison
│   ├── summary.py               # DataSummarizer, grouped/pivot/top10 tables
│   ├── validation.py             # reconciliation checks, audit log export
│   └── visualizations.py          # bar chart and heatmap
```

## Features
- Loads the raw csv and checks required columns exist before doing anything else
- Handles the file's Latin-1 encoding and mixed-type columns automatically
- Filters on two conditions and adds two derived columns
- Compares a Python loop against a vectorized NumPy calculation over 5 runs, confirms they match
- Generates grouped, two-factor grouped, pivot, and top 10 summary tables
- Generates a bar chart and a heatmap from those tables
- Runs reconciliation checks against the official reference totals and internal consistency, writes validation.csv, exits with an error if anything fails
- Builds and exports an audit trail of every pipeline step

## Prerequisites & Installation
Python 3.10+, then:
```bash
pip install -r requirements.txt
```

## Dataset
- File: 2015.csv (Philippine Customs import records)
- Source: [PASTE ACTUAL URL HERE]
- Downloaded: [PASTE ACTUAL DATE HERE]
- File size: 493.5 MB
- SHA-256: b3b5a3a95340179a716a05611d51ad4906484d38363d1ac36494a404c04e4370 (verified match)
- Confirmed shape after load: 2,236,612 rows, 30 columns, matches the reference totals in the assignment brief

## Columns used
- Category 1: countryorigin_iso3
- Category 2: tq
- Measure: dutiablevaluephp

## Known data issues and how we handled them
- File is Latin-1 encoded, not UTF-8, likely due to accented text in some fields. Loaded with encoding="latin1"
- Columns entry, prefcode, subport, port have mixed types, loaded with low_memory=False to avoid the dtype warning
- Zero missing values found in countryorigin_iso3, tq, or dutiablevaluephp

## Filter and transformation rules
- Row kept if dutiablevaluephp >= min_dutiable_value (see FILTER_CONFIG in config.py) AND countryorigin_iso3 is not in excluded_countries
- Rows failing either condition go into the excluded set, not dropped silently
- Derived columns added after filtering: dutiablevalue_kphp (measure divided by 1,000) and is_high_value (flag, true if dutiablevaluephp >= 1,000,000)

**Note:** FILTER_CONFIG currently has min_dutiable_value set to 0 and an empty excluded_countries set, so the filter is currently a no-op (0 rows excluded on the full run). This needs a real threshold and/or excluded country list decided before final submission, otherwise the "filter with two conditions" requirement isn't meaningfully demonstrated.

## Assumptions
- Missing values in the filter columns are treated as excluded rows, not zero-filled
- Pivot table margins are excluded from all interior-sum validation checks and from the heatmap

## How to Run
1. Place 2015.csv in data/
2. pip install -r requirements.txt
3. python main.py
4. Check output/ for grouped.csv, grouped_two.csv, pivot.csv, top10.csv, bar.png, heatmap.png, validation.csv, audit_log.csv

## Notebook
analysis.ipynb imports and runs the same pipeline code as main.py, with outputs shown inline. Export to HTML after running all cells (VS Code: notebook toolbar "..." menu → Export → HTML, or `jupyter nbconvert --to html analysis.ipynb`).
