import config
from src.data_loader import CustomsDataLoader
from src.audit import new_audit_record, missing_values_report
from src.data_filtering import filter_and_transform_data
from src.summary import DataSummarizer
from src.benchmark import run_numpy_benchmark
from src.visualizations import generate_bar_chart, generate_heatmap
from src.validation import build_and_check_validation, export_audit_log


def main() -> None:
    audit_records: list[dict] = []
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: load and validate
    loader = CustomsDataLoader(config.DATA_PATH, config.REQUIRED_COLUMNS)
    try:
        loader.load()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    try:
        loader.validate_columns()
    except ValueError as e:
        print(f"Error: {e}")
        return

    raw_df = loader.data
    audit_records.append(
        new_audit_record(1, "load_csv", "loaded raw file, no filtering yet", 0, loader.raw_row_count)
    )

    info = loader.summary_info()
    print(f"Loaded {info['row_count']} rows, {info['column_count']} columns.")

    nulls = missing_values_report(raw_df, columns=list(config.REQUIRED_COLUMNS))
    print(f"Missing values in required columns: {nulls}")

    # Step 2: filter
    filtered_df, excluded_df = filter_and_transform_data(
        raw_df,
        config.CATEGORY_COL_1,
        config.MEASURE_COL,
        min_value=config.FILTER_CONFIG["min_dutiable_value"],
        excluded_countries=config.FILTER_CONFIG["excluded_countries"],
    )
    audit_records.append(
        new_audit_record(
            2, "filter", "measure >= min_dutiable_value, country not excluded",
            len(raw_df), len(filtered_df),
        )
    )
    print(f"Filtered to {len(filtered_df)} rows, excluded {len(excluded_df)}.")

    # Step 3: numpy benchmark
    benchmark_res = run_numpy_benchmark(filtered_df[config.MEASURE_COL])
    print(f"Loop vs vectorized match: {benchmark_res['match']}")

    # Step 4: summary tables
    summarizer = DataSummarizer(
        filtered_df, config.CATEGORY_COL_1, config.CATEGORY_COL_2, config.MEASURE_COL
    )
    grouped_df, top10_df = summarizer.generate_single_grouped(config.OUTPUT_DIR)
    summarizer.generate_two_grouped(config.OUTPUT_DIR)
    pivot_df = summarizer.generate_pivot(config.OUTPUT_DIR)
    audit_records.append(
        new_audit_record(3, "summarize", "grouped, two-factor grouped, pivot generated",
                          len(filtered_df), len(grouped_df))
    )

    # Step 5: plots
    generate_bar_chart(top10_df, config.CATEGORY_COL_1, config.OUTPUT_DIR / "bar.png")
    generate_heatmap(pivot_df, config.OUTPUT_DIR / "heatmap.png")
    print("Plots saved.")

    # Step 6: validation + audit log export
    build_and_check_validation(
        raw_df, filtered_df, excluded_df, grouped_df, pivot_df, benchmark_res,
        config.MEASURE_COL, config.OUTPUT_DIR,
        ref_rows=config.REFERENCE_ROW_COUNT, ref_sum=config.REFERENCE_DUTIABLE_SUM,
    )
    export_audit_log(audit_records, config.OUTPUT_DIR)

    print("Pipeline complete. Check output/ folder.")


if __name__ == "__main__":
    main()