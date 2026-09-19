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
    
# Step 2: Filtering & Derived Metrics
    print("[2/6] Applying Filters and Computing Derived Metrics...")
    filtered_df, excluded_df = apply_filters_and_derived(
        raw_df, 
        measure_col=measure_col
    )
    
    # Export filtered CSVs
    filtered_df.to_csv(output_dir / "filtered_data.csv", index=False)
    excluded_df.to_csv(output_dir / "excluded_data.csv", index=False)

    audit_records.append({
        "step": 2,
        "operation": "Filtering & Derived Metrics",
        "rule": "Exclude non-positive measures and out-of-scope rows",
        "rows_before": len(raw_df),
        "rows_after": len(filtered_df)
    })

# Step 3: Summarization
    print("[3/6] Generating Aggregation Summaries...")
    summarizer = DataSummarizer(filtered_df, measure_col=measure_col)
    
    # Single-category grouping
    grouped_df = summarizer.group_by_category(country_col)
    grouped_df.to_csv(output_dir / "summary_grouped.csv", index=False)

    # Top 10 categories
    top10_df = summarizer.get_top_n(country_col, top_n=10)
    top10_df.to_csv(output_dir / "summary_top10.csv", index=False)

    # Two-way Pivot Table with Margins
    pivot_df = summarizer.create_pivot_table(index_col=country_col, columns_col=tq_col)
    pivot_df.to_csv(output_dir / "summary_pivot.csv")

    audit_records.append({
        "step": 3,
        "operation": "Aggregation Summaries",
        "rule": "Compute grouped sum/mean/count, top 10 ranking, and 2-way pivot",
        "rows_before": len(filtered_df),
        "rows_after": len(grouped_df)
    })

# Step 4: NumPy vs Loop Performance Benchmark
    print("[4/6] Executing NumPy Benchmark...")
    benchmark_res = run_numpy_benchmark(
        series=raw_df[measure_col],
        sample_size=100_000,
        threshold=100_000.0
    )
    audit_records.append({
        "step": 4,
        "operation": "NumPy Benchmark",
        "rule": "Sample 100k non-null rows and benchmark Python loop vs vectorized NumPy",
        "rows_before": 100_000,
        "rows_after": 100_000
    })

# Step 5: Data Visualizations
    print("[5/6] Generating Charts and Heatmaps...")
    generate_bar_chart(
        top10_df, 
        cat_col=country_col, 
        output_path=output_dir / "bar.png"
    )
    generate_heatmap(
        pivot_df, 
        output_path=output_dir / "heatmap.png"
    )
    audit_records.append({
        "step": 5,
        "operation": "Data Visualizations",
        "rule": "Generate bar.png and heatmap.png",
        "rows_before": len(top10_df),
        "rows_after": len(top10_df)
    })
