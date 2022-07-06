import json

import requests
from flask import Flask, render_template

app = Flask(__name__)

community_tag = 'hive-129948'


# main file
@app.route('/')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()


@app.route('/active_posts')
def active_posts_page():
    response = requests.get(
        url=f'https://sds0.steemworld.org/feeds_api/getActiveCommunityPostsByCreated/{community_tag}/faisalamin/50/1000').json()
    cols_res = response['result']['cols']
    rows_res = response['result']['rows']
    return render_template('active_posts.html', items_cols=cols_res, items_rows=rows_res)


# main file
@app.route('/author_report/<username>')
def author_report_page(username):
    return render_template('author_report.html', username=username)


# main file
@app.route('/community_report/<community>')
def community_report_page(community):
    response = requests.get(
        url=f'https://sds0.steemworld.org/feeds_api/getActiveCommunityReport/{community_tag}').json()
    cols_res = response['result']['cols']
    rows_res = response['result']['rows']
    return render_template('community_report.html', community=community, items_cols=cols_res, items_rows=rows_res)


@app.context_processor
def myfun1():
    def string_to_json(data):
        return json.loads(data)

    return dict(string_to_json=string_to_json)


@app.context_processor
def myfun2():
    def get_active_comments(author_name):
        response = requests.get(
            url=f'https://sds0.steemworld.org/feeds_api/getActiveCommunityAuthorReport/{community_tag}/{author_name}').json()
        result = response['result']
        total_comments = result["total_comment_count"]
        unique_comments = result["unique_comment_count"]
        mylist = [total_comments, unique_comments]
        return mylist

    return dict(get_comments=get_active_comments)
