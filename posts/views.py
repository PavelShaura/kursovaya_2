from flask import Blueprint, render_template, request, jsonify
from posts.dao.class_posts import Posts
from comments.dao.class_comment import Comments

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")
posts_dao = Posts('./data/data.json')
comments_data = Comments('./data/comments.json')


@posts_blueprint.route('/')
def index():
    posts = posts_dao.get_posts_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route("/posts/<int:uid>")
def post_page(uid):
    comments = comments_data.get_comments_by_post_id(uid)
    post = posts_dao.get_post_by_pk(uid)
    return render_template('post.html', comments=comments, post=post)


@posts_blueprint.route("/search/")
def search_page():
    search_by = request.args['s']
    if search_by:
        posts = posts_dao.search_for_posts(search_by)[0:10]
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts)


@posts_blueprint.route("/users/<username>/")
def feed_page(username):
    post_user = posts_dao.get_posts_by_user(username)
    return render_template('user-feed.html', post=post_user)


@posts_blueprint.route("/api/posts")
def index_test():
    post = posts_dao.get_posts_all()
    return jsonify(post)


@posts_blueprint.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = posts_dao.get_post_by_pk(uid)
    return jsonify(post)
