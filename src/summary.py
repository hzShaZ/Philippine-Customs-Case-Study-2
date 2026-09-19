from pathlib import Path
import pandas as pd

class DataSummarizer:
    def __init__(self, df: pd.DataFrame, cat1: str, cat2: str, measure: str):
        self.df = df
        self.cat1 = cat1
        self.cat2 = cat2
        self.measure = measure

    def generate_single_grouped(self, output_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
        grouped = self.df.groupby(self.cat1, dropna=False)[self.measure].agg(
            row_count='size', valid_measure_count='count', sum='sum', mean='mean'
        ).reset_index()
        grouped.to_csv(output_dir / "grouped.csv", index=False)

        top10 = grouped.sort_values(by="sum", ascending=False).head(10)
        top10.to_csv(output_dir / "top10.csv", index=False)
        return grouped, top10

    def generate_two_grouped(self, output_dir: Path) -> pd.DataFrame:
        grouped_two = self.df.groupby([self.cat1, self.cat2], dropna=False).agg(
            row_count=(self.measure, 'size'), measure_sum=(self.measure, 'sum')
        ).reset_index()
        grouped_two.to_csv(output_dir / "grouped_two.csv", index=False)
        return grouped_two

    def generate_pivot(self, output_dir: Path) -> pd.DataFrame:
        pivot = pd.pivot_table(
            self.df, values=self.measure, index=self.cat1, columns=self.cat2,
            aggfunc='sum', margins=True, margins_name='Total', dropna=False
        )
        pivot.to_csv(output_dir / "pivot.csv")
        return pivot