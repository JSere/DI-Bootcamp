CREATE TABLE public.items (
     items_id SERIAL PRIMARY KEY,
	 item_name VARCHAR(100) NOT NULL,
	 price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE public.customers (
   customer_id SERIAL PRIMARY KEY,
   first_name VARCHAR(50) NOT NULL,
   last_name VARCHAR(50) NOT NULL	
);

INSERT INTO public.items (item_name, price)
VALUES 
     ('Small Desk', 100),
     ('desk', 300),
     ('Fan', 80);

INSERT INTO public.customers (first_name, last_name)
VALUES 
     ('Greg', 'Jones' ),
     ('Sandra', 'Jones'),
     ('Scot', 'Scot'),
	 ('Trevor', 'Green'),
	 ('Melanie', 'Johnson');

SELECT * FROM public.items;

SELECT * FROM public.items
WHERE price > 80;

SELECT * FROM public.items
WHERE price <= 300;

SELECT * FROM public.customers
WHERE last_name = 'Smith'; -- empty no register of 'Smith'

SELECT * FROM public.customers
WHERE last_name = 'Jones';

SELECT * FROM public.customers
WHERE first_name != 'Scott';




