import sqlite3, pandas as pd, os

os.makedirs("data/sql_exports", exist_ok=True)
con = sqlite3.connect("data/nba.sqlite")
q = """
WITH tiers AS (
  SELECT *,
         CASE
           WHEN overall_pick BETWEEN 1 AND 10 THEN '01-10'
           WHEN overall_pick BETWEEN 11 AND 20 THEN '11-20'
           WHEN overall_pick BETWEEN 21 AND 30 THEN '21-30'
           WHEN overall_pick BETWEEN 31 AND 45 THEN '31-45'
           WHEN overall_pick BETWEEN 46 AND 60 THEN '46-60'
           ELSE 'Undrafted/NA'
         END AS pick_tier
  FROM draft_stats
)
SELECT pick_tier,
       ROUND(AVG(win_shares), 2) AS avg_ws,
       ROUND(AVG(value_over_replacement), 2) AS avg_vorp,
       ROUND(AVG(years_active), 2) AS avg_years,
       COUNT(*) AS players
FROM tiers
GROUP BY pick_tier
ORDER BY pick_tier;
"""
df = pd.read_sql(q, con)
con.close()
print(df)
df.to_csv("data/sql_exports/pick_tiers_value.csv", index=False)
print("\nSaved -> data/sql_exports/pick_tiers_value.csv")
  