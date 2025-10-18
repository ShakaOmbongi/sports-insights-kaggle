# clean_data.py (fixed)
import pandas as pd
from pathlib import Path

RAW = Path("data/raw/nbaplayersdraft.csv")
OUT = Path("data/nba_cleaned.csv")

df = pd.read_csv(RAW)
print("Before cleaning:", df.shape)

# Normalize column names
df.columns = [c.strip().lower() for c in df.columns]

# Drop rows missing key identifiers
df = df.dropna(subset=["player", "team", "year"])

# Clean text fields
for c in ["player", "team", "college"]:
    if c in df.columns:
        df[c] = df[c].astype(str).str.strip()

# Convert number-like columns to numeric
num_cols = [
    "year", "rank", "overall_pick", "years_active", "games", "minutes_played",
    "3_point_percentage", "free_throw_percentage", "average_minutes_played",
    "points_per_game", "average_total_rebounds", "average_assists",
    "win_shares", "win_shares_per_48_minutes", "box_plus_minus", "value_over_replacement"
]
for c in num_cols:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

# Sanity filter for PPG
if "points_per_game" in df.columns:
    df = df[(df["points_per_game"].isna()) | ((df["points_per_game"] >= 0) & (df["points_per_game"] <= 60))]

# Save cleaned version
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

print("After cleaning:", df.shape)
print(f"Saved -> {OUT}")
  