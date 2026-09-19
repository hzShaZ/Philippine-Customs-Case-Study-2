import time
import numpy as np
import pandas as pd

def run_numpy_benchmark(
    series: pd.Series, 
    sample_size: int = 100_000, 
    threshold: float = 100_000.0
) -> dict:
    """Compares Python loop vs vectorized NumPy execution times and results over 5 runs.
    
    Parameters:
        series: Pandas Series containing the numerical measure.
        sample_size: Number of non-null values to sample.
        threshold: Numeric threshold for filtering.
        
    Returns:
        dict: Dictionary containing loop sum, vector sum, median times, and match boolean.
    """
    np.random.seed(42)
    clean_array = series.dropna().to_numpy()
    actual_sample_size = min(sample_size, len(clean_array))
    sample = np.random.choice(clean_array, size=actual_sample_size, replace=False)