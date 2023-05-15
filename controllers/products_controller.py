from flask import render_template, request, redirect, session
from models.product import all_products, get_product, create_product, update_product, delete_product, create_review, number_of_entries, get_reviews, create_update, get_review, delete_review, create_suggest
from services.session_info import current_user

def index():
    products = all_products()
    return render_template('products/index.html', products=products, current_user=current_user())

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
    update_product(id, product_name, brand, image_url)
    return redirect ('/')

def delete(id):
    delete_product(id)
    return redirect('/')

def reviews(id):
    product = get_product(id)
    reviews = get_reviews(id)
    return render_template('/products/reviews.html', product=product, current_user=current_user(), reviews=reviews)

def post_review(id):
    product_id = id
    user_id = session['user_id']
    new_review = request.form.get('new_review')
    # if number_of_entries(product_id, user_id) == 0:
    create_review(product_id, user_id, new_review)
    # redirect on a POST request
    return redirect(f'/products/{product_id}/reviews')
    
def edit_review(id):
    product = get_product(id)
    product_id = id
    user_id = str(session['user_id'])
    review = get_review(product_id, user_id)
    return render_template('/products/edit_review.html', product=product, review=review)

def update_review(id):
    product_id = id
    user_id = str(session['user_id'])
    review = request.form.get('review')
    create_update(product_id, user_id, review)
    return redirect(f'/products/{product_id}/reviews')

def remove_review(id):
    product_id = id
    user_id = str(session['user_id'])
    delete_review(product_id, user_id)
    return redirect(f'/products/{product_id}/reviews')

def suggest():
    return render_template('/products/suggest.html', current_user=current_user())

def add_suggest():
    product_name = request.form.get('product_name')
    brand = request.form.get('brand')
    product_url = request.form.get('product_url')
    create_suggest(product_name, brand, product_url)
    return redirect('/')

