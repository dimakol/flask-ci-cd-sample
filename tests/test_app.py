import pytest
from app import app  # your Flask app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_health(client):
    response = client.get("/health")
    assert response.status_code == 200
