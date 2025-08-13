import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Loads the processed dataset and returns a DataFrame."""
    df = pd.read_csv(filepath, encoding="utf-8")
    # Ensure date columns are in the correct format
    if "Order.Date" in df.columns:
        df["Order.Date"] = pd.to_datetime(df["Order.Date"], errors="coerce")
    return df
