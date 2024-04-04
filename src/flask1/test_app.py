import pytest

from flask1 import create_app


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_helloエンドポイントにアクセスした場合文字列が返る(client):
    rv = client.get("/")
    assert "Hello Flask!" == rv.data.decode("utf8")


@pytest.mark.parametrize(
    [
        "name",
    ],
    [
        pytest.param("ogawa", id="name = ogawa"),
        pytest.param("higashi", id="name = higashi"),
    ],
)
def test_helloエンドポイントに名前をつけた場合その名前が入った文字列が返る(
    client, name
):
    rv = client.get(f"/hello/{name}")
    assert f"Hello {name}" == rv.data.decode("utf8")
