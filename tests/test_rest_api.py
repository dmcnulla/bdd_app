import pytest
from fastapi.testclient import TestClient
from rest_api import app, db


USER1 = ['user1', 'password1']


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


def test_add_user(client, database):
    user_name = USER1[0]
    user_password = USER1[1]
    response = client.post('/users', json={'username': user_name, 'password': user_password})
    assert response.status_code == 200
    assert response.json() == {'message': f'User {user_name} added'}
