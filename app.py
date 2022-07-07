from flask import Flask, request, render_template, send_from_directory, jsonify, make_response
import functions
import logging
import json

from logger import logger_one

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/", methods=["GET"])
def page_all_posts():
    data = functions.get_all_posts()
    return render_template('index.html', data=data)


@app.route("/post/<int:pk>/")
def page_post_by_pk(pk):
    post = functions.get_post_by_pk(pk)
    comments = functions.get_comments_by_post_pk(pk)
    return render_template('post.html', pk=pk, post=post, comments=comments)

@app.errorhandler(404)
def not_found(e):
   return 'Страница не найдена'

@app.errorhandler(500)
def not_found(e):
   return 'Ощибка на стороне сервера'


@app.route("/user/<user_name>", methods=["GET"])
def page_posts_by_name(user_name):
    posts = functions.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts)

@app.route("/search/")
def page_found_posts(q):
    q = request.args.get("q")
    posts = functions.search_posts(q)
    return render_template('search.html', posts=posts)


@app.route("/api/posts/")
def page_posts_in_json():
    data = functions.get_all_posts()
    logger_one.info("Запрос api/posts")
    return jsonify(data)

@app.route("/api/posts/<int:pk>")
def page_posts_by_pk_in_json(pk):
    data = functions.get_post_by_pk(pk)
    logger_one.info(f"Запрос api/posts{pk}")
    return jsonify(data)


app.run()

