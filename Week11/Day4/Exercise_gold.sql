-- exercise 1 task 1
WITH budget_leads_lags AS (
    SELECT 
        movie_title,
        release_date,
        budget,
        LAG(budget) OVER (ORDER BY release_date, movie_id) AS prev_budget,
        LEAD(budget) OVER (ORDER BY release_date, movie_id) AS next_budget
    FROM movies_database
)
SELECT 
    movie_title,
    release_date,
    budget,
    prev_budget,
    next_budget
FROM budget_leads_lags
WHERE budget > prev_budget 
  AND budget < next_budget;

-- exercise 1 task 2
WITH yearly_genre_ratings AS (
    SELECT 
        genre_name,
        movie_title,
        release_year,
        movie_rating
    FROM movies_database
)
SELECT 
    genre_name,
    movie_title,
    release_year,
    AVG(movie_rating) OVER (
        PARTITION BY genre_name 
        ORDER BY release_year 
        RANGE BETWEEN 2 PRECEDING AND 2 FOLLOWING
    ) AS moving_avg_rating
FROM yearly_genre_ratings;

-- exercise 1 task 3
SELECT 
    genre_name,
    movie_title,
    revenue,
    ROW_NUMBER() OVER (PARTITION BY genre_name ORDER BY revenue DESC) AS revenue_row_number,
    RANK() OVER (PARTITION BY genre_name ORDER BY revenue DESC) AS revenue_rank,
    DENSE_RANK() OVER (PARTITION BY genre_name ORDER BY revenue DESC) AS revenue_dense_rank
FROM movies_database;

-- exercise 2 task 1
SELECT DISTINCT
    actor_name,
    FIRST_VALUE(movie_title) OVER (
        PARTITION BY actor_name 
        ORDER BY release_date ASC, movie_id ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_movie_title,
    FIRST_VALUE(release_date) OVER (
        PARTITION BY actor_name 
        ORDER BY release_date ASC, movie_id ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_movie_release_date,
    FIRST_VALUE(movie_title) OVER (
        PARTITION BY actor_name 
        ORDER BY release_date DESC, movie_id DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_movie_title,
    FIRST_VALUE(release_date) OVER (
        PARTITION BY actor_name 
        ORDER BY release_date DESC, movie_id DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_movie_release_date
FROM actor_movies;

-- exercise 2 task 2
WITH genre_avg_revenue AS (
    SELECT 
        genre_name,
        AVG(revenue) AS avg_genre_revenue
    FROM movies_database
    GROUP BY genre_name
),
overall_avg_revenue AS (
    SELECT AVG(revenue) AS avg_overall_revenue FROM movies_database
),
filtered_genres AS (
    SELECT g.genre_name
    FROM genre_avg_revenue g
    CROSS JOIN overall_avg_revenue o
    WHERE g.avg_genre_revenue > o.avg_overall_revenue
)
SELECT 
    m.genre_name,
    m.movie_title,
    m.revenue,
    RANK() OVER (PARTITION BY m.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM movies_database m
JOIN filtered_genres f ON m.genre_name = f.genre_name;

-- exercise 2 task 3
WITH actor_total_revenues AS (
    SELECT 
        actor_name,
        SUM(movie_revenue) AS total_actor_revenue
    FROM actor_movies
    GROUP BY actor_name
),
ranked_actor_revenues AS (
    SELECT 
        actor_name,
        total_actor_revenue,
        PERCENT_RANK() OVER (ORDER BY total_actor_revenue DESC) AS rev_percent_rank
    FROM actor_total_revenues
)
SELECT 
    actor_name,
    total_actor_revenue
FROM ranked_actor_revenues
WHERE rev_percent_rank <= 0.10;