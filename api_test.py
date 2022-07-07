import pytest
from app import app

def test_all():
    response = app.test_client().get('/api/posts/')
    assert type(response) == list, "Возвращается не список"
    keys = ["poster_avatar", "poster_name", "views_count"]
    for item in response:
        for key in item:
            assert key in keys, 'Такого ключа в словаре нет'

def test_one():
    response = app.test_client().get('/api/posts/<int:pk>')
    assert type(response) == dict, "Возвращается не словарь"
    keys = ["poster_avatar", "poster_name", "views_count"]
    for item in response:
        for key in item:
            assert key in keys, 'Такого ключа в словаре нет'
