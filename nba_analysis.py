import sqlite3, pandas as pd, os

# Paths
DB_PATH = os.path.join('data', 'nba.sqlite')
EXPORT_PATH = os.path.join('data', 'sql_exports')

os.makedirs(EXPORT_PATH, exist_ok=True)

# Connect to the database
conn = sqlite3.connect(DB_PATH)

# STUDY 2
team_query = """
SELECT 
    team,
    ROUND(AVG(win_shares), 2) AS avg_win_shares,
    ROUND(AVG(value_over_replacement), 2) AS avg_vorp,
    ROUND(AVG(years_active), 2) AS avg_years_active,
    COUNT(*) AS players_drafted
FROM draft_stats
WHERE team IS NOT NULL
GROUP BY team
HAVING COUNT(*) > 10
ORDER BY avg_win_shares DESC;
"""

team_df = pd.read_sql_query(team_query, conn)
print("\n=== Team Draft Efficiency ===")
print(team_df.head(10))
team_df.to_csv(os.path.join(EXPORT_PATH, 'team_draft_efficiency.csv'), index=False)


# STUDY 3
player_query = """
SELECT 
    player,
    team,
    points_per_game,
    average_total_rebounds,
    average_assists,
    win_shares_per_48_minutes,
    box_plus_minus,
    ROUND(
        (points_per_game * 0.4 +
         average_total_rebounds * 0.2 +
         average_assists * 0.2 +
         win_shares_per_48_minutes * 100 * 0.1 +
         box_plus_minus * 0.1), 2
    ) AS efficiency_index
FROM draft_stats
WHERE games > 100
ORDER BY efficiency_index DESC
LIMIT 25;
"""

player_df = pd.read_sql_query(player_query, conn)
print("\n=== Top 25 Most Efficient Players ===")
print(player_df)
player_df.to_csv(os.path.join(EXPORT_PATH, 'top_player_efficiency.csv'), index=False)

# Close connection
conn.close()

print("\n Saved both studies to:", EXPORT_PATH)
  