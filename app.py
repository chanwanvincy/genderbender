from flask import Flask, redirect
from routes.products_routes import products_routes
import os

# SECRET_KEY = os.environ.get("SECRET_KEY", "")

app = Flask (__name__)
# app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(products_routes, url_prefix="/products")

@app.route('/')
def index():
    return redirect ('/products')
