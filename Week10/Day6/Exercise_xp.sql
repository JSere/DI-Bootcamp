-- exercise 1
SELECT * 
FROM language;

SELECT 
    f.title, 
    f.description, 
    l.name AS language
FROM film f
INNER JOIN language l 
    ON f.language_id = l.language_id;

SELECT 
    f.title, 
    f.description, 
    l.name AS language
FROM language l
LEFT JOIN film f 
    ON l.language_id = f.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) 
VALUES 
    ('Inception'),
    ('Interstellar'),
    ('The Dark Knight');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    language_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
    CONSTRAINT fk_language FOREIGN KEY (language_id) REFERENCES language(language_id)
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
    (1, 1, 'Increíble película', 9, 'Una obra maestra de la ciencia ficción.'),
    (2, 1, 'Excelente historia', 10, 'Efectos visuales impresionantes y gran guión.');

DELETE FROM new_film 
WHERE id = 1;

SELECT * FROM customer_review;


-- exercise 2
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

SELECT
    tc.constraint_name, 
    kcu.column_name, 
    ccs.table_name AS foreign_table_name,
    ccs.column_name AS foreign_column_name 
FROM information_schema.table_constraints AS tc 
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccs
    ON ccs.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY' 
  AND tc.table_name = 'customer';

DROP TABLE customer_review;

SELECT COUNT(*) AS total_outstanding
FROM rental
WHERE return_date IS NULL;

SELECT 
    f.title, 
    f.replacement_cost, 
    r.rental_date
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

SELECT DISTINCT f.title, f.description
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE' 
  AND a.last_name = 'MONROE'
  AND f.description ILIKE '%sumo%';

SELECT f.title, f.length, f.rating, c.name AS category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R';

SELECT DISTINCT f.title, p.amount, r.return_date
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'MATTHEW' 
  AND c.last_name = 'MAHAN'
  AND p.amount > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01 23:59:59';

SELECT DISTINCT f.title, f.description, f.replacement_cost
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'MATTHEW' 
  AND c.last_name = 'MAHAN'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;