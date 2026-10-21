-- Create product_orders table
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL
);


CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE
);


CREATE OR REPLACE FUNCTION get_order_total(p_order_id INT)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC;
BEGIN
    SELECT COALESCE(SUM(price), 0)
    INTO total_price
    FROM items
    WHERE order_id = p_order_id;
    
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;


CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

ALTER TABLE product_orders 
ADD COLUMN user_id INT REFERENCES users(user_id) ON DELETE CASCADE;


CREATE OR REPLACE FUNCTION get_user_order_total(p_user_id INT, p_order_id INT)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC;
BEGIN
    SELECT COALESCE(SUM(i.price), 0)
    INTO total_price
    FROM items i
    JOIN product_orders o ON i.order_id = o.order_id
    WHERE o.order_id = p_order_id AND o.user_id = p_user_id;
    
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;