-- task 1
WITH company_budgets AS (
    SELECT 
        company_name,
        budget,
        LAG(budget) OVER (PARTITION BY company_name ORDER BY release_date, movie_id) AS prev_budget
    FROM movies_database
),
growth_rates AS (
    SELECT 
        company_name,
        CASE 
            WHEN prev_budget > 0 THEN (budget - prev_budget)::NUMERIC / prev_budget 
            ELSE NULL 
        END AS growth_rate
    FROM company_budgets
)
SELECT 
    company_name,
    AVG(growth_rate) AS avg_budget_growth_rate
FROM growth_rates
GROUP BY company_name;

-- task 2
WITH global_avg AS (
    SELECT AVG(movie_rating) AS avg_rating FROM movies_database
),
high_rated_appearances AS (
    SELECT 
        am.actor_name,
        COUNT(m.movie_id) AS movie_count
    FROM movies_database m
    JOIN actor_movies am ON m.movie_id = am.movie_id
    CROSS JOIN global_avg g
    WHERE m.movie_rating > g.avg_rating
    GROUP BY am.actor_name
),
ranked_actors AS (
    SELECT 
        actor_name,
        movie_count,
        RANK() OVER (ORDER BY movie_count DESC) AS rk
    FROM high_rated_appearances
)
SELECT 
    actor_name,
    movie_count
FROM ranked_actors
WHERE rk = 1;

-- task 3
SELECT 
    genre_name,
    movie_title,
    revenue,
    AVG(revenue) OVER (
        PARTITION BY genre_name 
        ORDER BY release_date, movie_id 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM movies_database;

-- task 4
WITH series_revenue AS (
    SELECT 
        k.keyword AS movie_series,
        SUM(m.revenue) AS total_revenue
    FROM movies_database m
    JOIN movie_keywords k ON m.movie_id = k.movie_id
    GROUP BY k.keyword
),
ranked_series AS (
    SELECT 
        movie_series,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS rk
    FROM series_revenue
)
SELECT 
    movie_series,
    total_revenue
FROM ranked_series
WHERE rk = 1;