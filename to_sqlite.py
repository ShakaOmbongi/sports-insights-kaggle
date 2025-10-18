import sqlite3
import pandas as pd
from pathlib import Path

# File paths
CLEAN = Path("data/nba_cleaned.csv")
DB = Path("data/nba.sqlite")

# Load cleaned data
df = pd.read_csv(CLEAN)
print("Loading DataFrame:", df.shape)

# Create SQLite connection
con = sqlite3.connect(DB)

# Write DataFrame into SQLite
df.to_sql("draft_stats", con, if_exists="replace", index=False)

# Basic checks
rows = pd.read_sql("SELECT COUNT(*) AS total_rows FROM draft_stats;", con)
cols = pd.read_sql("PRAGMA table_info(draft_stats);", con)

print("\n Wrote table 'draft_stats' to", DB)
print(rows)
print("\nFirst 10 columns:")
print(cols.head(10))

con.close()
