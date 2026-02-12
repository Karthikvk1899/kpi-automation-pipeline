import argparse
import os

from kpi_automation.cli import run_pipeline


def main():
    parser = argparse.ArgumentParser(description="Run KPI Automation Pipeline")
    parser.add_argument(
        "--source",
        choices=["csv", "snowflake"],
        default="csv",
        help="Choose input source: csv or snowflake",
    )

    args = parser.parse_args()

    # Set environment variable based on choice
    if args.source == "snowflake":
        os.environ["USE_SNOWFLAKE"] = "true"
    else:
        os.environ["USE_SNOWFLAKE"] = "false"

    run_pipeline()


if __name__ == "__main__":
    main()
