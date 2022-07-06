import requests
from flask import Flask, render_template
import os

app = Flask(__name__)


# main file
@app.route('/')
def home_page():
    return "Hello World"


if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)


@app.route('/active_posts')
def active_posts_page():
    return "hello, World"
