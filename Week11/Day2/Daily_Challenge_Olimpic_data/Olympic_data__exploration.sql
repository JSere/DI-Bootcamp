-- Exercise 1
CREATE TEMP TABLE summer_winter_medals AS
SELECT 
    competitor_id,
    SUM(CASE WHEN season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM olympics_data
WHERE medal IS NOT NULL
GROUP BY competitor_id
HAVING SUM(CASE WHEN season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN season = 'Winter' THEN 1 ELSE 0 END) > 0;

SELECT * FROM summer_winter_medals;

CREATE TEMP TABLE two_sport_competitors AS
SELECT competitor_id
FROM (
    SELECT competitor_id, COUNT(DISTINCT sport) AS sport_count, COUNT(medal) AS total_medals
    FROM olympics_data
    WHERE medal IS NOT NULL
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT sport) = 2
) sub;

SELECT * 
FROM (
    SELECT o.competitor_id, COUNT(o.medal) AS total_medals
    FROM olympics_data o
    JOIN two_sport_competitors t ON o.competitor_id = t.competitor_id
    WHERE o.medal IS NOT NULL
    GROUP BY o.competitor_id
    ORDER BY total_medals DESC
    LIMIT 3
) top_three;


-- Exercise 2
SELECT region
FROM (
    SELECT r.region, 
           ROW_NUMBER() OVER (ORDER BY event_medals DESC) as rn
    FROM (
        SELECT competitor_id, event, COUNT(medal) AS event_medals
        FROM olympics_data
        WHERE medal IS NOT NULL
        GROUP BY competitor_id, event
    ) ce
    JOIN regions r ON ce.competitor_id = r.competitor_id
) sub
LIMIT 5;

CREATE TEMP TABLE no_medal_frequent_participants AS
SELECT competitor_id, full_name, COUNT(DISTINCT games) AS games_participated
FROM olympics_data
GROUP BY competitor_id, full_name
HAVING COUNT(DISTINCT games) > 3 
   AND SUM(CASE WHEN medal IS NOT NULL THEN 1 ELSE 0 END) = 0;

SELECT * FROM no_medal_frequent_participants;