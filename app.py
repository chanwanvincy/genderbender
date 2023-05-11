from flask import Flask, redirect

import os

SECRET_KEY = os.environ.get("SECRET_KEY", "")

app = Flask (__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint

@app.route('/')
def index():
    return ('/products')