import pytest
from fastapi.testclient import TestClient
from rest_api import app, db


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def database():
    db.clear()
    yield db


def test_greet(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world'}


def test_get_users(client, database):
    database.add_users([{'username': 'user1', 'password': 'password1'}])
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json() == [{'password': 'password1', 'username': 'user1'}]
