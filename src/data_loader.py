import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load the processed dataset and return a DataFrame."""
    df = pd.read_csv(filepath, encoding="utf-8")