-- Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre
SELECT 
    genre_name,
    movie_title,
    RANK() OVER (PARTITION BY genre_name ORDER BY popularity DESC) AS popularity_rank
FROM movies_database;

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
WITH company_quartiles AS (
    SELECT 
        company_name,
        movie_title,
        revenue,
        NTILE(4) OVER (PARTITION BY company_name ORDER BY revenue DESC) AS revenue_quartile
    FROM movies_database
)
SELECT 
    company_name,
    movie_title,
    revenue,
    revenue_quartile
FROM company_quartiles
WHERE revenue_quartile = 1;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
SELECT 
    genre_name,
    movie_title,
    budget,
    SUM(budget) OVER (
        PARTITION BY genre_name 
        ORDER BY release_date, movie_id 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_budget
FROM movies_database;

-- Task 4: Identify the Most Recent Movie for Each Genre
SELECT DISTINCT
    genre_name,
    FIRST_VALUE(movie_title) OVER (
        PARTITION BY genre_name 
        ORDER BY release_date DESC
    ) AS most_recent_movie,
    FIRST_VALUE(release_date) OVER (
        PARTITION BY genre_name 
        ORDER BY release_date DESC
    ) AS release_date
FROM movies_database;


-- Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies
SELECT 
    actor_name,
    DENSE_RANK() OVER (ORDER BY COUNT(movie_id) DESC) AS appearance_rank
FROM movie_cast
GROUP BY actor_name;

-- Task 2: Identify the Top Director by Average Movie Rating
WITH director_ratings AS (
    SELECT 
        director_name,
        AVG(movie_rating) AS avg_rating,
        RANK() OVER (ORDER BY AVG(movie_rating) DESC) as rk
    FROM movie_directors
    GROUP BY director_name
)
SELECT 
    director_name,
    avg_rating
FROM director_ratings
WHERE rk = 1;

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
SELECT 
    actor_name,
    movie_title,
    movie_revenue,
    SUM(movie_revenue) OVER (
        PARTITION BY actor_name 
        ORDER BY release_date, movie_id
    ) AS cumulative_revenue
FROM actor_movies;

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
WITH director_budgets AS (
    SELECT 
        director_name,
        SUM(budget) AS total_budget,
        RANK() OVER (ORDER BY SUM(budget) DESC) as rk
    FROM movie_directors
    GROUP BY director_name
)
SELECT 
    director_name,
    total_budget
FROM director_budgets
WHERE rk = 1;