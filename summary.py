from pathlib import Path
import pandas as pd

class datasummarizer:
  def __init__(self, df: pd.Dataframe, cat1: str, cat2:str, measure: str):
    self.df = df
    self.cat1 = cat1
    self.cat2 = cat2
    self.measure = measure

