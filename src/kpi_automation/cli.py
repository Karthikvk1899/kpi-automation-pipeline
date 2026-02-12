from pathlib import Path
import pandas as pd

from kpi_automation.validate import validate_input
from kpi_automation.kpis.definitions import compute_kpis

RAW_PATH = Path("data/raw/sample_sales.csv")
OUT_PATH = Path("data/processed/kpis_daily.csv")
REPORT_PATH = Path("reports/kpi_report.html")

def run_pipeline(raw_path: Path = RAW_PATH) -> None:
    df = pd.read_csv(raw_path)
    validate_input(df)

    kpis = compute_kpis(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    kpis.to_csv(OUT_PATH, index=False)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary = kpis.describe(include="all").to_html()
    REPORT_PATH.write_text(
        f"<h1>KPI Report</h1><p>Source: {raw_path}</p>"
        f"{summary}<h2>Latest Rows</h2>{kpis.tail(10).to_html(index=False)}",
        encoding="utf-8",
    )

if __name__ == "__main__":
    run_pipeline()
