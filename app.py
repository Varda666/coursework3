from flask import Flask, request, render_template, send_from_directory, jsonify
import functions
import logging
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def page_all_posts():
    data = functions.get_all_posts()
    return render_template('index.html', data=data)

@app.route("/post/<int:pk>/")
def page_post_by_pk(pk):
    posts = functions.get_post_by_pk(pk)
    comments = functions.get_comments_by_post_pk(pk)
    return render_template('post.html', posts=posts, comments=comments)

@app.route("/user/<user_name>", methods=["GET"])
def page_posts_by_name(user_name):
    posts = functions.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts)

@app.route("/search/")
def page_found_posts():
    q = request.args.get("q")
    posts = functions.search_posts(q)
    return render_template('search.html', posts=posts)


app.run()
