from pathlib import Path
import pandas as pd

class datasummarizer:
  def __init__(self, df: pd.Dataframe, cat1: str, cat2:str, measure: str):
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


