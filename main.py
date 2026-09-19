from pathlib import Path
import pandas as pd

# Import modular components from src
from src.data_filtering import load_data, apply_filters_and_derived
from src.summary import DataSummarizer
from src.benchmark import run_numpy_benchmark
from src.visualizations import generate_bar_chart, generate_heatmap
from src.validation import build_and_check_validation, export_audit_log

def main():
    # 1. Define Paths and Settings
    project_root = Path(__file__).parent.resolve()
    data_path = project_root / "data" / "customs_2015.csv"
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    measure_col = "dutiablevaluephp"
    country_col = "countryoriginiso3"
    tq_col = "tqcategory"
    audit_records = []

    print("=== Starting Case Study Pipeline ===")

    # Step 1: Ingestion
    print("\n[1/6] Loading Dataset...")
    raw_df = load_data(data_path)
    audit_records.append({
        "step": 1,
        "operation": "Data Ingestion",
        "rule": "Load raw Customs 2015 dataset",
        "rows_before": len(raw_df),
        "rows_after": len(raw_df)
    })

