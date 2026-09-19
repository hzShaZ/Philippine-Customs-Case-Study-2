from pathlib import Path

DATA_PATH = Path("data/2015.csv")
OUTPUT_DIR = Path("output")

REFERENCE_ROW_COUNT = 2_236_612
REFERENCE_COLUMN_COUNT = 30
REFERENCE_DUTIABLE_SUM = 3_587_267_375_257  # PHP
REFERENCE_SHA256 = "b3b5a3a95340179a716a05611d51ad4906484d38363d1ac36494a404c04e4370"

REQUIRED_COLUMNS = {"countryorigin_iso3", "tq", "dutiablevaluephp"}

# Analysis columns
CATEGORY_COL_1 = "countryorigin_iso3"
CATEGORY_COL_2 = "tq"
MEASURE_COL = "dutiablevaluephp"


FILTER_CONFIG = {
    "min_dutiable_value": 0,
    "excluded_countries": set(),
}