---Exercise 1: Detailed Medal Analysis
--1 
CREATE TEMP TABLE temp_dual_season_medals AS
SELECT 
    gc.id AS competitor_id,
    g.season,
    COUNT(ce.medal_id) AS medal_count
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id IS NOT NULL AND gc.id IN (
    SELECT c.id 
    FROM games_competitor c
    JOIN competitor_event e ON c.id = e.competitor_id
    JOIN games gm ON c.games_id = gm.id
    WHERE e.medal_id IS NOT NULL
    GROUP BY c.id
    HAVING COUNT(DISTINCT gm.season) = 2
)
GROUP BY gc.id, g.season;

SELECT * FROM temp_dual_season_medals;
-- 2
CREATE TEMP TABLE temp_two_sports_competitors AS
SELECT 
    gc.id AS competitor_id,
    p.full_name,
    COUNT(DISTINCT e.sport_id) AS sport_count,
    COUNT(ce.medal_id) AS total_medals
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT * 
FROM temp_two_sports_competitors 
WHERE total_medals IN (
    SELECT total_medals 
    FROM temp_two_sports_competitors 
    ORDER BY total_medals DESC 
    LIMIT 3
)
ORDER BY total_medals DESC 
LIMIT 3;

--------Exercise 2: Region and Competitor Performance------------
--1 
SELECT 
    nr.region_name,
    COUNT(ce.medal_id) AS total_medals
FROM games_competitor gc
JOIN person_region pr ON gc.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NOT NULL 
  AND ce.event_id IN (
      SELECT event_id 
      FROM competitor_event 
      WHERE competitor_id = gc.id AND medal_id IS NOT NULL
      GROUP BY event_id
      ORDER BY COUNT(medal_id) DESC
      LIMIT 1
  )
GROUP BY nr.id, nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

--2
CREATE TEMP TABLE temp_no_medal_frequent_competitors AS
SELECT 
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_count
FROM games_competitor gc
JOIN person p ON gc.person_id = p.id
WHERE gc.id NOT IN (
    SELECT DISTINCT competitor_id 
    FROM competitor_event 
    WHERE medal_id IS NOT NULL
)
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3;

SELECT * FROM temp_no_medal_frequent_competitors;






