import pytest

keys_should_be = {'content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk'}


class TestMyApp:

    def test_get_all(self, posts_dao):
        """ Проверяем получение всех постов"""
        posts = posts_dao.get_posts_all()
        assert type(posts) == list
        assert len(posts) > 0
        assert set(posts[0].keys()) == keys_should_be

    def test_get_by_pk(self, posts_dao):
        """ Проверяем получение одного поста"""
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict
        assert post["pk"] == 1
        assert set(post.keys()) == keys_should_be


class TestApi:

    def test_api_posts_1(self, test_client):

        response = test_client.get('/api/posts/', follow_redirects=True)
        post = response.json
        assert response.status_code == 200, "Статус-код запроса не ок"
        assert isinstance(post, list), "Выгружается не словарь"

        for q in post:
            for key in keys_should_be:
                assert (bool(key in q.keys()) == True), "Ошибка получения ключей"

    def test_api_posts_2(self, test_client):

        response = test_client.get('/api/posts/1', follow_redirects=True)
        post = response.json
        assert response.status_code == 200, "Статус код запроса не ок"
        assert isinstance(post, dict), "Выгружается не словарь"

        for q in post:
            for key in keys_should_be:
                assert not (bool(key in q.keys())) == True, "Ошибка получения ключей"
