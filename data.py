"""Data helpers and a sample dataset generator."""
import pandas as pd
import numpy as np

def sample_timeseries(n=50, seed=42):
    rng = np.random.RandomState(seed)
    dates = pd.date_range('2023-01-01', periods=n, freq='D')
    df = pd.DataFrame({
        'date': dates,
        'value': rng.randn(n).cumsum() + 50,
        'category': rng.choice(['A','B','C'], size=n)
    })
    return df

def load_csv(path):
    return pd.read_csv(path)
