from flask import Flask, jsonify
from posts.views import posts_blueprint
from posts.dao.class_posts import Posts

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)

posts = Posts()


@app.route("/api/posts")
def index_test():
    post = posts.get_posts_all()
    return jsonify(post)


@app.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = posts.get_post_by_pk(uid)
    return jsonify(post)


if __name__ == "__main__":
    app.run(debug=True)
