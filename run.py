from flask import Flask

from posts.views import posts_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
