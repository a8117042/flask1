import pytest
from flask1 import create_app

@pytest.fixture
def app():
    app = create_app({'TESTING' : True})

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello(client):
    rv = client.get("/")
    assert "Hello Flask!" == rv.data.decode('utf8')
