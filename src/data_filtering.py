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