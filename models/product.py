from db.db import sql

def all_products():
    return sql('SELECT * FROM products')
    # returns all results with most recent changes made

def get_product(id):
    products = sql('SELECT * FROM products WHERE id=%s', [id])
    return products[0]

def create_product(product_name, brand, image_url):
    sql('INSERT INTO products (product_name, brand, image_url) VALUES(%s, %s, %s) RETURNING *', [product_name, brand, image_url])

def update_product(id, product_name, brand, image_url):
    sql('UPDATE products SET product_name=%s, brand=%s, image_url=%s WHERE id=%s RETURNING *', [product_name, brand, image_url, id])

def delete_product(id):
    sql('DELETE FROM products WHERE id=%s RETURNING *', [id])

def create_review(product_id, user_id, review):
    sql('INSERT INTO reviews (product_id, user_id, review) VALUES (%s, %s, %s) RETURNING *', [product_id, user_id, review])

def get_reviews(product_id):
    reviews = sql('SELECT * FROM reviews WHERE product_id=%s', [product_id])
    return reviews