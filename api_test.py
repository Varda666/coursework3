import pytest
from app import app

def test_all():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    assert type(response.json) == list, "Возвращается не список"
    keys = ["poster_avatar", "poster_name", "views_count", "content", 'likes_count', 'pic', 'pk', 'c']
    for item in response.json:
        for key in item:
            assert key in keys, 'Такого ключа в словаре нет'

def test_one():
    response = app.test_client().get('/api/posts/2')
    assert response.status_code == 200
    assert type(response.json) == dict, "Возвращается не словарь"
    keys = ["poster_avatar", "poster_name", "views_count", "content", 'likes_count', 'pic', 'pk', 'c']
    for item in response.json:
        for key in item:
            assert key in key, 'Такого ключа в словаре нет'


