from json import JSONDecodeError
import logging
from flask import Flask, request, render_template, send_from_directory, jsonify
import json
from pprint import pp


def get_all_posts():
    with open(f"data/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_posts_by_post_id(post_id):
    data = get_all_posts()
    for post in data:
        if post_id in data["pk"]:
            if data['content'] is None or data['content'] == '':
                return ''
            else:
                return post


def get_posts_by_user(user_name):
    data = get_all_posts()
    for post in data:
        if user_name in data["poster_name"]:
            if data['content'] is None or data['content'] == '':
                return ''
            else:
                return post
        raise KeyError ('Нет такого пользователя')

def get_all_comments():
    with open("comments.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_comments_by_post_pk(pk):
    data = get_all_comments()
    posts_found = []
    for post in data:
        if pk == post["post_id"]:
            posts_found.append(post)
            return posts_found
        else:
            return ''


def search_posts(q):
    data = get_all_posts()
    posts_found = []
    for post in data:
        if query.lower() in post['content'].lower():
            posts_found.append(post)
    return posts_found

def get_post_by_pk(pk):
    data = get_all_posts()
    posts_found = []
    for post in data:
        if pk == post["pk"]:
            posts_found.append(post)
    return posts_found






