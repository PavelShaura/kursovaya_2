import pytest
from posts.dao.class_posts import Posts
from comments.dao.class_comment import Comments


@pytest.fixture()
def posts_dao():
    posts_instance = Posts("./data/data.json")
    return posts_instance

@pytest.fixture()
def comment_dao():
    comments_data = Comments('./data/comments.json')
    return comments_data



@pytest.fixture()
def posts_dao():
    posts_dao_instance = Posts("./data/data.json")
    return posts_dao_instance