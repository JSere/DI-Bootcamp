
SELECT *
FROM customer;

SELECT CONCAT(first_name,' ',last_name) AS full_name
FROM customer;

SELECT  DISTINCT create_date
FROM customer;

SELECT *
FROM customer
ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, phone
FROM address
WHERE LOWER(district) = 'texas';

SELECT *
FROM film 
WHERE film_id BETWEEN 15 AND 150;

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE '%star wars%'; 

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'st%'; 

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC, film_id
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;






































