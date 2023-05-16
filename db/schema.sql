CREATE DATABASE genderbender_db;
\c genderbender_db

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name TEXT,
    brand TEXT,
    image_url TEXT
);

INSERT INTO products(product_name, brand, image_url) VALUES
    ('Orginals Half Binder', 'gc2b', 'https://cdn.shopify.com/s/files/1/0739/5475/products/Front_Shot_-_Black_0d6c937f-c5ba-4ab9-8df4-b81ea36499b6_1024x.jpg?v=1604678143');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INT,
    user_id INT,
    review TEXT
);

CREATE TABLE suggests (
    id SERIAL PRIMARY KEY,
    user_id INT,
    product_name TEXT,
    product_url TEXT
);

INSERT INTO reviews(product_id, user_id, review) VALUES
    ('1', '1', 'My first review');




-- is combination of product_id and user_id connected to an existing review id? (users can only submit 1 review per product)

SELECT COUNT(*) FROM reviews WHERE product_id=1 AND user_id=1 ;