from pathlib import Path
import os
import pandas as pd

from kpi_automation.validate import validate_input
from kpi_automation.kpis.definitions import compute_kpis
from kpi_automation.ingest_snowflake import load_sales_data

RAW_PATH = Path("data/raw/sample_sales.csv")
OUT_PATH = Path("data/processed/kpis_daily.csv")
REPORT_PATH = Path("reports/kpi_report.html")


def run_pipeline() -> None:
    """
    Runs KPI automation pipeline.
    Supports CSV input (default) or Snowflake input if USE_SNOWFLAKE=true.
    """

    use_snowflake = os.getenv("USE_SNOWFLAKE", "false").lower() == "true"

    if use_snowflake:
        print("Loading input from Snowflake...")
        df = load_sales_data()
    else:
        print("Loading input from CSV...")
        df = pd.read_csv(RAW_PATH)

    validate_input(df)

    print("Computing KPIs...")
    kpis = compute_kpis(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    kpis.to_csv(OUT_PATH, index=False)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary = kpis.describe(include="all").to_html()

    REPORT_PATH.write_text(
        f"<h1>KPI Report</h1>"
        f"<p>Source: {'Snowflake' if use_snowflake else RAW_PATH}</p>"
        f"{summary}"
        f"<h2>Latest KPI Rows</h2>"
        f"{kpis.tail(10).to_html(index=False)}",
        encoding="utf-8",
    )

    print("Pipeline completed successfully.")
    print(f"Output saved to: {OUT_PATH}")
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    run_pipeline()

