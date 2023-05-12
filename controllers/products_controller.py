from flask import render_template, request, redirect, session
from models.product import all_products, get_product, create_product, update_product, delete_product, create_review, get_reviews
from services.session_info import current_user

def index():
    products = all_products()
    return render_template('products/index.html', products = products, current_user=current_user())

def new():
    return render_template('products/new.html', current_user=current_user())

def create():
    product_name = request.form.get('product_name')
    brand = request.form.get('brand')
    image_url = request.form.get('image_url')
    create_product(product_name, brand, image_url)
    return redirect('/')

def edit(id):
    product = get_product(id)
    return render_template('products/edit.html', product=product, current_user=current_user())

def update(id):
    product_name = request.form.get('product_name')
    brand = request.form.get('brand')
    image_url = request.form.get('image_url')
    update_product(product_name, brand, image_url)
    return redirect ('/')

def delete(id):
    delete_product(id)
    return redirect('/')

def reviews(id):
    product = get_product(id)
    reviews = get_reviews(id)
    return render_template('/products/reviews.html', product=product, current_user=current_user(), reviews=reviews)

def post_review():
    product_id = request.form.get('product_id')
    user_id = session['user_id']
    review = request.form.get('review')
    create_review(product_id, user_id, review)
    return render_template('/products/reviews.html')
    

def suggest():
    return render_template('/products/suggest.html', current_user=current_user())