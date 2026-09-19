import pandas as pd


def new_audit_record(
    step: int,
    operation: str,
    rule: str,
    rows_before: int,
    rows_after: int,
) -> dict:
    """builds one row for the audit log"""
    return {
        "step": step,
        "operation": operation,
        "rule": rule,
        "rows_before": rows_before,
        "rows_after": rows_after,
    }


def missing_values_report(df: pd.DataFrame, columns: list[str] | None = None) -> dict:
    """counts nulls per column, checks all columns by default"""
    if columns is None:
        columns = list(df.columns)

    report = {}
    for col in columns:
        report[col] = int(df[col].isna().sum())

    return report