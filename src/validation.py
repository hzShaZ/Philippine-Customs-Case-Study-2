from pathlib import Path
import sys
import pandas as pd

def build_and_check_validation(
    raw_df: pd.DataFrame,
    filtered_df: pd.DataFrame,
    excluded_df: pd.DataFrame,
    grouped_df: pd.DataFrame,
    pivot_df: pd.DataFrame,
    benchmark_res: dict,
    measure_col: str,
    output_dir: Path,
    ref_rows: int = 2_236_612,
    ref_sum: float = 3_587_267_375_257.0
) -> pd.DataFrame:
    """Builds validation.csv checks, exports it, and exits with status 1 on failure."""
    raw_rows = len(raw_df)
    raw_sum = float(raw_df[measure_col].sum(skipna=True))
    sel_rows = len(filtered_df)
    sel_sum = float(filtered_df[measure_col].sum(skipna=True))
    excl_rows = len(excluded_df)

    grouped_rows = int(grouped_df["row_count"].sum())
    grouped_sum = float(grouped_df["sum"].sum())

    # Extract interior sum of pivot table excluding margins
    pivot_interior = pivot_df.drop(index="Total", columns="Total", errors="ignore")
    pivot_interior_sum = float(pivot_interior.sum().sum())

    checks = [
        {"check": "Reference Row Count", "expected": ref_rows, "actual": raw_rows, "tolerance": 0, "pass": raw_rows == ref_rows},
        {"check": "Reference Sum Check", "expected": ref_sum, "actual": raw_sum, "tolerance": 1.0, "pass": abs(raw_sum - ref_sum) <= 1.0},
        {"check": "Rows Partition Equality", "expected": raw_rows, "actual": sel_rows + excl_rows, "tolerance": 0, "pass": raw_rows == (sel_rows + excl_rows)},
        {"check": "Grouped Row Count Match", "expected": sel_rows, "actual": grouped_rows, "tolerance": 0, "pass": sel_rows == grouped_rows},
        {"check": "Grouped Sum Match", "expected": sel_sum, "actual": grouped_sum, "tolerance": 1.0, "pass": abs(sel_sum - grouped_sum) <= 1.0},
        {"check": "Pivot Interior Sum Match", "expected": sel_sum, "actual": pivot_interior_sum, "tolerance": 1.0, "pass": abs(sel_sum - pivot_interior_sum) <= 1.0},
        {"check": "NumPy vs Loop Benchmark", "expected": benchmark_res["loop_sum"], "actual": benchmark_res["vector_sum"], "tolerance": 1e-2, "pass": benchmark_res["match"]}
    ]

    val_df = pd.DataFrame(checks)
    val_df.to_csv(output_dir / "validation.csv", index=False)