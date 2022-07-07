import pytest
import functions

def test_get_all_posts():
    data = functions.get_all_posts()
    assert type(data) == list, 'Неверный тип данных в полученном результате'

    post = functions.get_all_posts()[0]
    assert type(post) == dict, 'Неверный тип данных в полученном результате'

def check_fields():
    data = functions.get_all_posts()
    post = functions.get_all_posts()[0]
    fields = ["poster_name", "poster_avatar", 'poster_content']
    for field in fields:
        assert hasattr(post, 'field'), 'Нет такого поля'


def check_users():
    data = functions.get_all_posts()
    users = ["leo", "johnny", "hank"]
    for user in users:
        assert hasattr(data, 'user'), 'Нет такого поля'

@pytest.fixture()
def get_correct_pk():
    data = functions.get_all_posts()
    correct_pk = []
    for post in data:
        correct_pk.append(post["pk"])
    return correct_pk

@pytest.mark.parametrize("pk", [1, 2, 3])
def test_get_post_by_pk(pk):
    data = functions.get_post_by_pk(pk)
    for post in data:
        assert post['pk'] == pk, 'Нет такого pk'


@pytest.mark.parametrize("q", ['елки', 'я'])
def test_search_posts(q):
    data = functions.get_all_posts()
    posts_found = []
    for post in data:
        assert q.lower() in post['content'].lower(), 'Нет такого слова в постах'


