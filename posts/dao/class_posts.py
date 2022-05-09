import json


class Posts:

    def __init__(self, path):
        """ Путь к файлу с данными"""
        self.path = path


    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """Возвращает посты"""

        posts_all = self.load_data()
        return posts_all

    def get_posts_by_user(self, name):
        """Возвращает посты определенного пользователя"""
        posts = self.load_data()
        for post in posts:
            if name in post['poster_name'].lower():
                return post

    def search_for_posts(self, search_by_tag):
        """Возвращает список постов по ключевому слову"""

        post_list = self.load_data()
        posts_list = []
        for post in post_list:
            if search_by_tag.lower() in post['content'].lower():
                posts_list.append(post)
        return posts_list

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        posts = self.load_data()
        for post in posts:
            if post["pk"] == pk:
                return post
