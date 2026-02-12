import pandas as pd

def compute_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["orders", "revenue", "returns", "marketing_spend", "visits"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["aov"] = df["revenue"] / df["orders"]                 # Average Order Value
    df["return_rate"] = df["returns"] / df["orders"]
    df["conversion_rate"] = df["orders"] / df["visits"]
    df["roas"] = df["revenue"] / df["marketing_spend"]       # Return on Ad Spend

    out_cols = [
        "date", "orders", "revenue", "returns", "marketing_spend", "visits",
        "aov", "return_rate", "conversion_rate", "roas"
    ]
    return df[out_cols]
