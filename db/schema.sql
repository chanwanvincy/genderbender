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
    -- from hidden post
    product_id TEXT,
    -- from hidden post
    user_id TEXT,
    review TEXT
);

CREATE TABLE suggests (
    id SERIAL PRIMARY KEY,
    user_id TEXT,
    product_name TEXT,
    product_url TEXT
)

-- is combination of product_id and user_id connected to an existing review id? (users can only submit 1 review per product)