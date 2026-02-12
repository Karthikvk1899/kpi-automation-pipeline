import pandas as pd
from kpi_automation.kpis.definitions import compute_kpis

def test_compute_kpis_columns():
    df = pd.DataFrame([{
        "date": "2026-02-12",
        "orders": 10,
        "revenue": 1000,
        "returns": 1,
        "marketing_spend": 100,
        "visits": 2000
    }])

    out = compute_kpis(df)

    assert "aov" in out.columns
    assert "roas" in out.columns
    assert out.loc[0, "aov"] == 100.0
    assert out.loc[0, "roas"] == 10.0
