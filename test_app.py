import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add(client):
    response = client.get("/add/5/5")
    assert response.json["result"] == 10