import sqlite3
import pandas as pd
from pathlib import Path

# paths
CLEAN = Path("data/nba_cleaned.csv")
DB = Path("data/nba.sqlite")

# Load data
df = pd.read_csv(CLEAN)
print("Loading DataFrame:", df.shape)

# SQLite connection
con = sqlite3.connect(DB)

# SQLite
df.to_sql("draft_stats", con, if_exists="replace", index=False)

# check
rows = pd.read_sql("SELECT COUNT(*) AS total_rows FROM draft_stats;", con)
cols = pd.read_sql("PRAGMA table_info(draft_stats);", con)

print("\n Wrote table 'draft_stats' to", DB)
print(rows)
print("\nFirst 10 columns:")
print(cols.head(10))

con.close()
 