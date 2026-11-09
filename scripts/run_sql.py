"""Run every .sql file in sql/ against the synthetic CSV using SQLite (no setup needed)."""
import glob
import sqlite3

import pandas as pd

conn = sqlite3.connect(":memory:")
pd.read_csv("data/synthetic_pairing_funnel.csv").to_sql("funnel", conn, index=False)
for path in sorted(glob.glob("sql/*.sql")):
    print(f"\n== {path} ==")
    print(pd.read_sql_query(open(path).read(), conn).to_string(index=False))
