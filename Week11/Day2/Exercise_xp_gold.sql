----exercise 1
--1
SELECT DISTINCT p.id, p.full_name
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
JOIN event e ON ce.event_id = e.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
  AND p.id IN (
      SELECT p_ind.id
      FROM person p_ind
      JOIN games_competitor gc_ind ON p_ind.id = gc_ind.person_id
      JOIN competitor_event ce_ind ON gc_ind.id = ce_ind.competitor_id
      JOIN medal m_ind ON ce_ind.medal_id = m_ind.id
      JOIN event e_ind ON ce_ind.event_id = e_ind.id
      WHERE m_ind.medal_name IN ('Gold', 'Silver', 'Bronze')
        AND e_ind.event_name NOT LIKE '%Team%'
        AND e_ind.event_name NOT LIKE '%Relay%'
        AND e_ind.event_name NOT LIKE '%Doubles%'
        AND e_ind.event_name NOT LIKE '%Fours%'
        AND e_ind.event_name NOT LIKE '%Eights%'
  )
  AND p.id IN (
      SELECT p_team.id
      FROM person p_team
      JOIN games_competitor gc_team ON p_team.id = gc_team.person_id
      JOIN competitor_event ce_team ON gc_team.id = ce_team.competitor_id
      JOIN medal m_team ON ce_team.medal_id = m_team.id
      JOIN event e_team ON ce_team.event_id = e_team.id
      WHERE m_team.medal_name IN ('Gold', 'Silver', 'Bronze')
        AND (e_team.event_name LIKE '%Team%' 
             OR e_team.event_name LIKE '%Relay%' 
             OR e_team.event_name LIKE '%Doubles%' 
             OR e_team.event_name LIKE '%Fours%' 
             OR e_team.event_name LIKE '%Eights%')
  );

--2
CREATE TEMP TABLE temp_region_medals AS
SELECT 
    nr.region_name,
    COUNT(ce.medal_id) AS total_medals
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN person p ON pr.person_id = p.id
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY nr.region_name;

SELECT region_name, total_medals
FROM temp_region_medals
ORDER BY total_medals DESC
LIMIT 3; 
--3
CREATE TEMP TABLE temp_gold_multi_games AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS unique_games_count
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name = 'Gold'
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 2;

--------------------exercise 2--------
--1
UPDATE person
SET weight = (
    SELECT AVG(p_avg.weight)
    FROM person p_avg
    JOIN games_competitor gc_avg ON p_avg.id = gc_avg.person_id
    JOIN competitor_event ce_avg ON gc_avg.id = ce_avg.competitor_id
    JOIN medal m_avg ON ce_avg.medal_id = m_avg.id
    WHERE m_avg.medal_name IN ('Gold', 'Silver', 'Bronze')
      AND p_avg.weight IS NOT NULL
)
WHERE id IN (
    SELECT p_multi.id
    FROM person p_multi
    JOIN games_competitor gc_multi ON p_multi.id = gc_multi.person_id
    JOIN competitor_event ce_multi ON gc_multi.id = ce_multi.competitor_id
    JOIN medal m_multi ON ce_multi.medal_id = m_multi.id
    WHERE m_multi.medal_name IN ('Gold', 'Silver', 'Bronze')
    GROUP BY p_multi.id
    HAVING COUNT(DISTINCT gc_multi.games_id) > 1
);
--2
-- 1. Crear tabla temporal con el número de eventos por competidor
CREATE TEMP TABLE temp_competitor_event_counts AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(ce.event_id) AS total_events_participated
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY p.id, p.full_name;

-- 2. Identificar competidores en múltiples estaciones
SELECT 
    tc.person_id,
    tc.full_name,
    tc.total_events_participated
FROM temp_competitor_event_counts tc
WHERE tc.person_id IN (
    SELECT gc_s.person_id
    FROM games_competitor gc_s
    JOIN games g_s ON gc_s.games_id = g_s.id
    GROUP BY gc_s.person_id
    HAVING COUNT(DISTINCT g_s.season) > 1
);


--3

CREATE TEMP TABLE temp_region_medal_heights AS
SELECT 
    nr.region_name,
    AVG(p.height) AS avg_region_height
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN person p ON pr.person_id = p.id
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
  AND p.height IS NOT NULL
GROUP BY nr.region_name;


SELECT 
    rmh.region_name,
    ROUND(rmh.avg_region_height, 2) AS avg_region_height,
    ROUND((SELECT AVG(p_all.height) FROM person p_all WHERE p_all.height IS NOT NULL), 2) AS overall_avg_height,
    ROUND(rmh.avg_region_height - (SELECT AVG(p_all.height) FROM person p_all WHERE p_all.height IS NOT NULL), 2) AS height_difference
FROM temp_region_medal_heights rmh;















