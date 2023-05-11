from flask import Flask, redirect
from routes.products_routes import products_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
import os

SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask (__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(products_routes, url_prefix="/products")
app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(sessions_routes, url_prefix="/sessions")

@app.route('/')
def index():
    return redirect ('/products')
