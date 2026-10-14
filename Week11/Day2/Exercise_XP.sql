----------Exercise 1 complex subquery
--1
SELECT 
    m.medal_name,
    (
        SELECT AVG(gc.age)
        FROM games_competitor gc
        JOIN competitor_event ce ON gc.id = ce.competitor_id
        WHERE ce.medal_id = m.id AND gc.age IS NOT NULL
    ) AS average_age
FROM medal m
WHERE m.medal_name != 'NA'
  AND EXISTS (
      SELECT 1 
      FROM competitor_event ce2 
      WHERE ce2.medal_id = m.id
  ); 
  
 --2
 SELECT 
    nr.region_name,
    COUNT(DISTINCT gc.person_id) AS unique_competitors
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN games_competitor gc ON pr.person_id = gc.person_id
WHERE gc.id IN (
    SELECT competitor_id
    FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 3
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;  

--3
CREATE TEMP TABLE temp_competitor_medals AS
SELECT 
    competitor_id,
    COUNT(medal_id) AS total_medals
FROM competitor_event
GROUP BY competitor_id;

SELECT 
    competitor_id,
    total_medals
FROM temp_competitor_medals
WHERE total_medals > 2
ORDER BY total_medals DESC;

--4
DELETE FROM temp_competitor_medals
WHERE competitor_id NOT IN (
    SELECT DISTINCT competitor_id
    FROM competitor_event
    WHERE medal_id IS NOT NULL
);
-----exercise 2 advanced data manipulation----------
UPDATE person
SET height = (
    SELECT AVG(p_sub.height)
    FROM person p_sub
    JOIN person_region pr_sub ON p_sub.id = pr_sub.person_id
    WHERE pr_sub.region_id IN (
        SELECT pr_main.region_id 
        FROM person_region pr_main 
        WHERE pr_main.person_id = person.id
    )
    AND p_sub.height IS NOT NULL
)
WHERE height IS NULL;

--2
CREATE TEMP TABLE multi_event_participants (
    competitor_id INT,
    games_id INT,
    total_events INT
);

INSERT INTO multi_event_participants (competitor_id, games_id, total_events)
SELECT 
    gc.id, 
    gc.games_id, 
    COUNT(ce.event_id) AS total_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE gc.id IN (
    SELECT gc_sub.id
    FROM games_competitor gc_sub
    JOIN competitor_event ce_sub ON gc_sub.id = ce_sub.competitor_id
    GROUP BY gc_sub.id, gc_sub.games_id
    HAVING COUNT(ce_sub.event_id) > 1
)
GROUP BY gc.id, gc.games_id;

--3
SELECT 
    nr.region_name,
    AVG(medal_count.medals) AS avg_medals_per_competitor
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN games_competitor gc ON pr.person_id = gc.person_id
JOIN (
    SELECT competitor_id, COUNT(medal_id) AS medals
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id
) medal_count ON gc.id = medal_count.competitor_id
GROUP BY nr.region_name
HAVING AVG(medal_count.medals) > (
    SELECT AVG(total_medals)
    FROM (
        SELECT COUNT(medal_id) AS total_medals
        FROM competitor_event
        WHERE medal_id IS NOT NULL
        GROUP BY competitor_id
    ) overall_avg
);

--4
CREATE TEMP TABLE competitor_seasons AS
SELECT 
    gc.person_id,
    g.season
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
GROUP BY gc.person_id, g.season;

SELECT person_id
FROM competitor_seasons
WHERE season IN ('Summer', 'Winter')
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2;





