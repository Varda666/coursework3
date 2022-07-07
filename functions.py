from json import JSONDecodeError
import logging
from flask import Flask, request, render_template, send_from_directory, jsonify
import json
from pprint import pp


def get_all_posts():
    try:
        with open(f"data/data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except JSONDecodeError:
        return 'Файл не открывается'
    except FileNotFoundError:
        return 'Файл не преобразуется'



def get_posts_by_post_id(post_id):
    data = get_all_posts()
    for post in data:
        if post_id in post["pk"]:
            if post['content'] is None or post['content'] == '':
                return ''
            else:
                return post


def get_posts_by_user(user_name):
    user_name = str(user_name).lower()
    data = get_all_posts()
    posts_found = []
    for post in data:
        if user_name == post['poster_name'].lower():
            posts_found.append(post)
        else:
            pass
    return posts_found
    raise KeyError('Нет такого пользователя')

def get_all_comments():
    try:
        with open("data/comments.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except JSONDecodeError:
        return 'Файл не открывается'
    except FileNotFoundError:
        return 'Файл не преобразуется'

def get_comments_by_post_pk(pk):
    data = get_all_comments()
    comment_found = []
    try:
        for comment in data:
            if pk == comment["post_id"]:
                comment_found.append(comment)
                return comment_found
    except KeyError:
        return 'Поста с таким номером нет'
    except ValueError:
        return 'Комментариев нет'


def search_posts(q):
    data = get_all_posts()
    posts_found = []
    for post in data:
        if q.lower() in post['content'].lower():
            posts_found.append(post)
    return posts_found

def get_post_by_pk(pk):
    data = get_all_posts()
    posts_found = []
    for post in data:
        if post["pk"] == pk:
            posts_found.append(post)
    return posts_found




