import json


class Comments:

    def __init__(self, path):
        """ Путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        comments = self.load_data()

        comments_by_id = []

        for comment in comments:
            if post_id == comment['post_id']:
                comments_by_id.append(comment)
        return comments_by_id
