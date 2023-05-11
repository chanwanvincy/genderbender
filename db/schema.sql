CREATE DATABASE genderbender_db;
\c genderbender_db

CREATE TABLE products {
    id SERIAL PRIMARY KEY,
    product_name TEXT,
    brand TEXT,
    image_url TEXT
}