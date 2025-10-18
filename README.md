#  NBA Draft Value Analysis Dashboard

This project analyzes how NBA Draft Pick Tiers correlate with player success and career longevity.  
Using Python and Tableau, this analysis measures player performance across metrics like Win Shares, Value Over Replacement Player (VORP), and Years Active, providing insights into how draft position impacts long-term value.

---
##  Project Overview

The goal of this project is to explore whether players selected earlier in the NBA Draft deliver better on-court performance compared to later picks.  

---
## DashBoard on Tableau
 View Interactive Dashboard on Tableau Public (https://public.tableau.com/app/profile/shaka.ombongi/viz/NBA_Draft_Value_Analysis/Dashboard1?publish=yes)

---
### Key Questions:
- Do top draft picks perform significantly better than later-round selections?
- How does draft position affect career longevity?
- What trends can teams learn from historical draft data?

---
##  Metrics Analyzed
 Metrics  

 Win Shares (WS)  An estimate of the number of wins contributed by a player. 
 Value Over Replacement Player (VORP) | Measures a player’s overall impact compared to a replacement-level player. 
 Years Active  Represents the player’s career length and sustainability in the league. 

These metrics were aggregated and averaged by Draft Pick Tier:
- Picks 01–10 
- Picks 11–20  
- Picks 21–30
- Picks 31–45 
- Picks 46–60
---
## Data Source

- Dataset: NBA Player Statistics (Public Data)  
- Source: Aggregated from open public player statistics databases and draft records (2024 snapshot).  
- Kaggle link: https://www.kaggle.com/code/mattop/nba-draft-player-data-analysis-1989-2021/input  
- Processing: Cleaned and transformed using Python (pandas, qlite3), then visualized in Tableau.
---
## How to Run the Project

Clone the repository:
- git clone https://github.com/YourUsername/NBA-Draft-Value-Analysis.git
- cd sports-performance-analytics
---
## Tools Used

- Python (pandas, sqlite3)
- Tableau
- GitHub
---
## Insights Summary

- Top 10 draft picks show the highest average Win Shares and VORP.
- Mid and late round players occasionally outperform expectations.
- Career longevity declines gradually by pick tier, indicating early picks generally sustain longer careers.