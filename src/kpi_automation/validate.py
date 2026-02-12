import pandas as pd

REQUIRED_COLS = ["date", "orders", "revenue", "returns", "marketing_spend", "visits"]

def validate_input(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df.empty:
        raise ValueError("Input dataset is empty")

    if df[REQUIRED_COLS].isna().any().any():
        raise ValueError("Nulls detected in required columns")
