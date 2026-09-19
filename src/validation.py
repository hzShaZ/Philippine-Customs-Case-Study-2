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
    """Builds validation.csv checks, exports it, and exits with status 1 on failure.

    Parameters:
        raw_df: Loaded raw DataFrame.
        filtered_df: DataFrame after filtering.
        excluded_df: DataFrame containing excluded rows.
        grouped_df: Single category grouped summary DataFrame.
        pivot_df: Pivot table DataFrame with margins.
        benchmark_res: Output dictionary from run_numpy_benchmark.
        measure_col: Name of measure column (dutiablevaluephp).
        output_dir: Path to directory for output CSVs.
        ref_rows: Expected reference raw row count (Customs 2015).
        ref_sum: Expected reference measure sum (Customs 2015).

    Returns:
        pd.DataFrame: DataFrame containing all validation results.
    """
    raw_rows = len(raw_df)
    raw_sum = float(raw_df[measure_col].sum(skipna=True))
    sel_rows = len(filtered_df)
    sel_sum = float(filtered_df[measure_col].sum(skipna=True))
    excl_rows = len(excluded_df)