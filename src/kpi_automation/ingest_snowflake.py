import os
import pandas as pd
import snowflake.connector


def load_sales_data() -> pd.DataFrame:
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    try:
        query = """
        SELECT
            date,
            orders,
            revenue,
            returns,
            marketing_spend,
            visits
        FROM KPI_DB.KPI_SCHEMA.SALES_DAILY
        ORDER BY date
        """

        df = pd.read_sql(query, conn)

        # Normalize Snowflake uppercase column names
        df.columns = [c.lower() for c in df.columns]

        return df

    finally:
        conn.close()

