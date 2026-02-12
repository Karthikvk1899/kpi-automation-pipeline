# KPI Automation Pipeline (Python + GitHub Actions)

Automates KPI computation from raw CSV input with validation, unit tests, and scheduled execution via GitHub Actions.

## Features
- Ingest raw CSV (`data/raw/sample_sales.csv`)
- Validate schema + null checks
- Compute KPIs:
  - AOV
  - Return Rate
  - Conversion Rate
  - ROAS
- Generate outputs:
  - `data/processed/kpis_daily.csv`
  - `reports/kpi_report.html`
- CI: lint + tests on every push/PR
- Scheduled run: daily workflow + artifacts upload

## Run locally
```bash
pip install -e ".[dev]"
python -m kpi_automation.cli
pytest -q
