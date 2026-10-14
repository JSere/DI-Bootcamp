-- 1
CREATE TEMP TABLE temp_competitor_medal_breakdown AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(CASE WHEN e.event_name NOT LIKE '%Team%' 
                AND e.event_name NOT LIKE '%Relay%' 
                AND e.event_name NOT LIKE '%Doubles%' 
                AND e.event_name NOT LIKE '%Fours%' 
                AND e.event_name NOT LIKE '%Eights%' THEN 1 END) AS individual_medals,
    COUNT(CASE WHEN e.event_name LIKE '%Team%' 
                OR e.event_name LIKE '%Relay%' 
                OR e.event_name LIKE '%Doubles%' 
                OR e.event_name LIKE '%Fours%' 
                OR e.event_name LIKE '%Eights%' THEN 1 END) AS team_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
JOIN event e ON ce.event_id = e.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY p.id, p.full_name
HAVING COUNT(CASE WHEN e.event_name NOT LIKE '%Team%' 
                   AND e.event_name NOT LIKE '%Relay%' 
                   AND e.event_name NOT LIKE '%Doubles%' 
                   AND e.event_name NOT LIKE '%Fours%' 
                   AND e.event_name NOT LIKE '%Eights%' THEN 1 END) > 0
   AND COUNT(CASE WHEN e.event_name LIKE '%Team%' 
                   OR e.event_name LIKE '%Relay%' 
                   OR e.event_name LIKE '%Doubles%' 
                   OR e.event_name LIKE '%Fours%' 
                   OR e.event_name LIKE '%Eights%' THEN 1 END) > 0;
                   
--2
CREATE TEMP TABLE temp_competitors_three_sports AS
SELECT 
    p.id AS person_id,
    p.full_name
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN event e ON ce.event_id = e.id
JOIN sport s ON e.sport_id = s.id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT s.id) = 3;

SELECT 
    t.person_id,
    t.full_name,
    COUNT(ce.medal_id) AS total_medals
FROM temp_competitors_three_sports t
JOIN games_competitor gc ON t.person_id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY t.person_id, t.full_name
ORDER BY total_medals DESC
LIMIT 3;

--3
CREATE TEMP TABLE temp_regions_both_seasons AS
SELECT 
    nr.region_name,
    AVG(p.birth_year) AS avg_birth_year
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN person p ON pr.person_id = p.id
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
JOIN games g ON gc.games_id = g.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
  AND p.birth_year IS NOT NULL
GROUP BY nr.region_name
HAVING SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;

SELECT region_name, ROUND(avg_birth_year, 2) AS avg_birth_year
FROM temp_regions_both_seasons;

                   
                   
                   