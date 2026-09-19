from pathlib import Path
import config
from src.data_loader import CustomsDataLoader


def main() -> None:
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

    info = loader.summary_info()
    print(f"Loaded {info['row_count']} rows, {info['column_count']} columns.")


if __name__ == "__main__":
    main()