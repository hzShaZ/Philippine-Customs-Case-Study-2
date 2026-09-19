import config
from src.data_loader import CustomsDataLoader
from src.audit import new_audit_record, missing_values_report


def main() -> None:
    audit_records: list[dict] = []

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

    audit_records.append(
        new_audit_record(
            step=1,
            operation="load_csv",
            rule="loaded raw file, no filtering yet",
            rows_before=0,
            rows_after=loader.raw_row_count,
        )
    )

    info = loader.summary_info()
    print(f"Loaded {info['row_count']} rows, {info['column_count']} columns.")

    nulls = missing_values_report(loader.data, columns=list(config.REQUIRED_COLUMNS))
    print(f"Missing values in required columns: {nulls}")

    print(f"Audit records so far: {audit_records}")


if __name__ == "__main__":
    main()