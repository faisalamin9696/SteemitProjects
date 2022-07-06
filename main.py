import requests
from flask import Flask, render_template
import os

app = Flask(__name__)


# main file
@app.route('/')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()


@app.route('/active_posts')
def active_posts_page():
    response = requests.get(
        url=f'https://sds0.steemworld.org/feeds_api/getActiveCommunityPostsByCreated/hive-144064/faisalamin/50/1000').json()
    cols_res = response['result']['cols']
    rows_res = response['result']['rows']
    return render_template('active_posts.html', items_cols=cols_res, items_rows=rows_res)
