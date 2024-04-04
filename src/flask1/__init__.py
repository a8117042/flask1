from flask import Flask, render_template, url_for, current_app, g

def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'test-secret'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    @app.route("/")
    def index():
        return "Hello Flask!"

    @app.get("/hello/<name>", endpoint="hello-endpoint")
    @app.post("/hello", endpoint="hello-endpoint")
    def hello(name):
        return f"Hello {name}"

    @app.get("/name/<name>")
    def show_name(name):

        users = [{"url":"ogawa", "username":"ogawa"}, {"url":"garaike", "username":"garaike"}]

        return render_template("index.html", name=name, users=users)

    ctx = app.app_context()
    ctx.push()

    print(current_app.name)

    g.connection = "connection"
    print(g.connection)

    with app.test_request_context():
        print(url_for("index"))
        print(url_for("hello-endpoint", name="world"))
        print(url_for("show_name", name="ichiro", page="1"))

    return app
