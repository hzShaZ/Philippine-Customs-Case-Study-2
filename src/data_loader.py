"""Loads and validates the Philippine Customs dataset."""

from pathlib import Path
import pandas as pd


class CustomsDataLoader:
    """Loads a Customs CSV file and validates it against expected structure.

    Attributes:
        file_path: Path to the raw CSV file.
        required_columns: Set of column names that must be present.
        data: The loaded DataFrame, set after calling load().
        raw_row_count: Row count before any filtering, set after load().
    """

    def __init__(self, file_path: Path, required_columns: set[str]) -> None:
        self.file_path = file_path
        self.required_columns = required_columns
        self.data: pd.DataFrame | None = None
        self.raw_row_count: int = 0

    def load(self) -> pd.DataFrame:
        """Loads the CSV file into a DataFrame.

        Raises:
            FileNotFoundError: If the file does not exist at file_path.

        Returns:
            The loaded DataFrame.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Data file not found at {self.file_path}. "
                f"Download it and place it there before running."
            )
        self.data = pd.read_csv(self.file_path, encoding="latin1", low_memory=False)
        self.raw_row_count = len(self.data)
        return self.data

    def validate_columns(self) -> bool:
        """Checks that all required columns exist in the loaded data.

        Raises:
            ValueError: If any required column is missing.

        Returns:
            True if all required columns are present.
        """
        if self.data is None:
            raise RuntimeError("Call load() before validate_columns().")
        missing = self.required_columns - set(self.data.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        return True

    def summary_info(self) -> dict[str, int]:
        """Returns basic shape info about the loaded data.

        Returns:
            A dict with row count and column count.
        """
        if self.data is None:
            raise RuntimeError("Call load() before summary_info().")
        return {
            "row_count": len(self.data),
            "column_count": len(self.data.columns),
        }