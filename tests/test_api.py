from run import app


def test_api_posts():
    """Проверяем что
    - возвращается список
    - у элементов есть нужные ключи"""
    response = app.test_client().get('/api/posts/')
    needed_keys = ['content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk']
    post = response.json
    assert isinstance(post, list), "Выгружается не список"
    for el in post:
        for key in needed_keys:
            assert (bool(key in el.keys()) == True), "Ошибка получения ключей"


def test_api_posts_by_id():
    """Проверяем что
    - возвращается словарь
    - у элемента есть нужные ключи"""

    response = app.test_client().get('/api/posts/')
    needed_keys = ['content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk']
    post = response.json
    assert isinstance(post, dict), "Выгружается не словарь"
    for el in post:
        for key in needed_keys:
            assert (bool(key in el.keys()) == True), "Ошибка получения ключей"
