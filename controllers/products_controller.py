from flask import render_template, request, redirect
from models.product import all_products, get_product, create_product, update_product, delete_product

def index():
    products = all_products()
    return render_template('products/index.html', products = products)

def new():
    return render_template('products/new.html')

def create():
    product_name = request.form.get('product_name')
    brand = request.form.get('brand')
    image_url = request.form.get('image_url')
    create_product(product_name, brand, image_url)
    return redirect('/')

def edit(id):
    product = get_product(id)
    return render_template('products/edit.html', product=product)

def update(id):
    product_name = request.form.get('product_name')
    brand = request.form.get('brand')
    image_url = request.form.get('image_url')
    update_product(product_name, brand, image_url)
    return redirect ('/')

def delete(id):
    delete_product(id)
    return redirect('/')