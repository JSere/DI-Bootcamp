import pandas as pd
from sqlalchemy import create_engine

# 1. Cargar datos y crear base de datos SQLite
df = pd.read_csv('netflix_titles.csv')
engine = create_engine('sqlite:///netflix.db')
df.to_sql('netflix', engine, if_exists='replace', index=False)

def run_query(query, title=""):
    if title:
        print(f"=== {title} ===")
    result = pd.read_sql_query(query, engine)
    print(result)
    print("\n" + "="*40 + "\n")

# Query 1: Select *
run_query("SELECT * FROM netflix LIMIT 5;", "Query 1: Select *")

# Query 2: Select Distinct
run_query("SELECT DISTINCT show_id FROM netflix LIMIT 5;", "Query 2: Select Distinct")

# Query 3: Select Where
run_query("SELECT DISTINCT title FROM netflix WHERE release_year > 2020 LIMIT 5;", "Query 3: Select Where")

# Query 4: Select and, or, not
run_query("""
    SELECT DISTINCT title 
    FROM netflix 
    WHERE release_year > 2020 AND type = 'Movie' AND NOT rating = 'R'
    LIMIT 5;
""", "Query 4: Select and, or, not")

# Query 5: Order By
run_query("""
    SELECT title, release_year 
    FROM netflix 
    ORDER BY release_year DESC, title ASC 
    LIMIT 5;
""", "Query 5: Order By")

# Query 6: Limit Values
run_query("SELECT * FROM netflix LIMIT 5;", "Query 6: Limit Values")

# Query 7: Aggregations
run_query("""
    SELECT 
        MIN(release_year) AS min_year,
        MAX(release_year) AS max_year,
        COUNT(show_id) AS total_shows,
        AVG(release_year) AS avg_year,
        SUM(release_year) AS sum_year
    FROM netflix;
""", "Query 7: Min, Max, Count, Avg, Sum")

# Query 8: Like
run_query("SELECT DISTINCT country FROM netflix WHERE country LIKE '%United States%' LIMIT 5;", "Query 8: Like")

# Query 9: In
run_query("""
    SELECT title, country 
    FROM netflix 
    WHERE country IN ('United States', 'India', 'United Kingdom') 
    LIMIT 5;
""", "Query 9: In")

# Query 10: Between
run_query("SELECT title, release_year FROM netflix WHERE release_year BETWEEN 2020 AND 2021 LIMIT 5;", "Query 10: Between")

# Query 11: Self Join
run_query("""
    SELECT a.title AS title_1, b.title AS title_2, a.release_year 
    FROM netflix a 
    JOIN netflix b ON a.release_year = b.release_year AND a.show_id <> b.show_id 
    LIMIT 5;
""", "Query 11: Joins")

# Query 12: Union
run_query("""
    SELECT title, type FROM netflix WHERE release_year = 2021
    UNION
    SELECT title, type FROM netflix WHERE release_year = 2020
    LIMIT 5;
""", "Query 12: Unions")

# Query 13: Case Statement
run_query("""
    SELECT title, release_year,
        CASE 
            WHEN release_year >= 2020 THEN 'Recent'
            WHEN release_year >= 2015 THEN 'Modern'
            ELSE 'Classic'
        END AS era
    FROM netflix
    LIMIT 5;
""", "Query 13: Case Statements")

# Query 14: Subquery
run_query("""
    SELECT title, release_year 
    FROM netflix 
    WHERE release_year = (SELECT MAX(release_year) FROM netflix)
    LIMIT 5;
""", "Query 14: Sub Queries")

# Query 15: Coalesce
run_query("SELECT title, COALESCE(director, 'Unknown Director') AS director_name FROM netflix LIMIT 5;", "Query 15: Coalesce")

# Query 16: Cast
run_query("SELECT title, CAST(release_year AS TEXT) AS release_year_str FROM netflix LIMIT 5;", "Query 16: Convert")

# Query 17: Lag / Lead
run_query("""
    SELECT title, release_year,
        LAG(title, 1) OVER (ORDER BY release_year) AS prev_title,
        LEAD(title, 1) OVER (ORDER BY release_year) AS next_title
    FROM netflix
    LIMIT 5;
""", "Query 17: Lag/Lead")

# Query 18: Row Number
run_query("""
    SELECT title, type,
        ROW_NUMBER() OVER (PARTITION BY type ORDER BY release_year DESC) AS row_num
    FROM netflix
    LIMIT 5;
""", "Query 18: Row Number")

# Query 19: Dense Rank
run_query("""
    SELECT title, release_year,
        DENSE_RANK() OVER (ORDER BY release_year DESC) AS year_rank
    FROM netflix
    LIMIT 5;
""", "Query 19: Dense Rank")

# Query 20: CTE (With)
run_query("""
    WITH recent_shows AS (
        SELECT title, release_year, type
        FROM netflix
        WHERE release_year >= 2021
    )
    SELECT type, COUNT(*) AS total_count
    FROM recent_shows
    GROUP BY type;
""", "Query 20: With (CTE)")