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
    
    
    # 1. Standard Python for loop (5 runs)
    loop_times = []
    loop_sum = 0.0
    for _ in range(5):
        t0 = time.perf_counter()
        loop_sum = sum(val for val in sample if val > threshold)
        t1 = time.perf_counter()
        loop_times.append(t1 - t0)

    # 2. Vectorized NumPy boolean mask aggregation (5 runs)
    vector_times = []
    vector_sum = 0.0
    for _ in range(5):
        t0 = time.perf_counter()
        mask = sample > threshold
        vector_sum = float(np.sum(sample[mask]))
        t1 = time.perf_counter()
        vector_times.append(t1 - t0)
        
    # 3. Verify equal results within tolerance
    is_match = bool(np.isclose(loop_sum, vector_sum, atol=1e-2))

    return {
        "loop_sum": float(loop_sum),
        "vector_sum": float(vector_sum),
        "loop_median_sec": float(np.median(loop_times)),
        "vector_median_sec": float(np.median(vector_times)),
        "match": is_match
    }