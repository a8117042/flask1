from flask import Flask

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

    return app
