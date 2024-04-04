from flask import Flask, render_template

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
        return render_template("index.html", name=name)

    return app
