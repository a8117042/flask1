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

@pytest.mark.parametrize(
    [
        "name",
    ],
    [
        pytest.param("ogawa"),
        pytest.param("higashi")
    ],
)
def test_name(client, name):
    rv = client.get(f"/hello/{name}")
    assert f"Hello {name}" == rv.data.decode('utf8')
    
