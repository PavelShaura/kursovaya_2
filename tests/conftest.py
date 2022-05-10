import pytest
import run
from posts.dao.class_posts import Posts
from comments.dao.class_comment import Comments

@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()



@pytest.fixture()
def posts_dao():
    posts_instance = Posts("./data/data.json")
    return posts_instance


@pytest.fixture()
def comment_dao():
    comments_data = Comments('./data/comments.json')
    return comments_data



