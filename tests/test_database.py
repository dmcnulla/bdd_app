import pytest
from database import Database, InvalidCredentialsException
import uuid


DB_FILE = 'temp.json'
USER1 = 'user1'
USER2 = 'user2'
PASSWORD1 = 'password1'
PASSWORD2 = 'password2'
USERS = [
    {"username": USER1, "password": PASSWORD1},
    {"username": USER2, "password": PASSWORD2}
]


@pytest.fixture(scope="session")
def db_file(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / DB_FILE
    return fn


@pytest.fixture()
def db(db_file):
    yield Database(db_file=db_file)


def assert_valid_uuid(uuid_to_test, version=4):
    uuid_obj = uuid.UUID(uuid_to_test, version=version)
    assert str(uuid_obj) == uuid_to_test


def test_add_user(db):
    db.add_user('my_username')
    user = db.get_user('my_username')
    assert 'my_username' == user[0]['username']
    assert_valid_uuid(user[0]['password'])


def test_add_users(db):
    db.add_users(USERS)
    user1 = db.get_user(USER1)
    assert USER1 == user1[0]['username']
    assert PASSWORD1 == user1[0]['password']
    user2 = db.get_user(USER2)
    assert USER2 == user2[0]['username']
    assert PASSWORD2 == user2[0]['password']


def test_update_user_succeeds(db):
    db.add_user(USER1, PASSWORD1)
    db.update_user_password(USER1, PASSWORD1, PASSWORD2)
    user = db.get_user(USER1)
    assert USER1 == user[0]['username']
    assert PASSWORD2 == user[0]['password']


def test_update_user_fails(db):
    db.add_user(USER2, PASSWORD2)
    # ToDo: This was only fails when run with
    #  test_update_user_succeeds, so I changed the user, but that is not good.
    with pytest.raises(InvalidCredentialsException) as e:
        db.update_user_password(USER2, PASSWORD1, PASSWORD2)
    assert 'The user is not found or the old password is incorrect' == str(e.value)
