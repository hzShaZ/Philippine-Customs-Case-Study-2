import pandas as pd


def filter_and_transform_data(
    df: pd.DataFrame,
    cat1_col: str,
    measure_col: str,
    min_value: float = 1.0,
    excluded_countries: set | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Filters dataset using two conditions and creates two derived columns."""
    if excluded_countries is None:
        excluded_countries = set()
        
        # 2-condition filter
    cond1 = df[measure_col] >= min_value
    cond2 = ~df[cat1_col].isin(excluded_countries)

    keep_mask = cond1 & cond2
    filtered_df = df.loc[keep_mask].copy()
    excluded_df = df.loc[~keep_mask].copy()

    if filtered_df.empty:
        raise ValueError("Filter criteria returned zero rows.")