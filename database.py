from tinydb import TinyDB, Query
from os import path as os_path
from uuid import uuid4

CURRENT_DIR = os_path.dirname(os_path.abspath(__file__))
DEFAULT_DB_FILE = os_path.join(CURRENT_DIR, 'db.json')
USER_FIELD = 'username'
PASSWORD_FIELD = 'password'


class InvalidCredentialsException(RuntimeError):
    pass


class Database:
    def __init__(self, db_file=DEFAULT_DB_FILE):
        self.db = TinyDB(db_file)

    def add_user(self, username: str, password: str = None):
        if username not in [user[USER_FIELD] for user in self.get_users()]:
            self.db.insert({USER_FIELD: username, PASSWORD_FIELD: password or str(uuid4())})

    def update_user_password(self, username: str, old_password: str, new_password: str):
        try:
            user = Query()
            current_password = self.get_user(username)[0][PASSWORD_FIELD]
            if old_password != current_password:
                raise InvalidCredentialsException('The user is not found or the old password is incorrect')
            self.db.update({PASSWORD_FIELD: new_password}, (user[USER_FIELD] == username))
        except KeyError:
            raise InvalidCredentialsException('The user is not found or the old password is incorrect')

    def add_users(self, users: list):
        self.db.insert_multiple(users)

    def get_user(self, username):
        user = Query()
        return self.db.search(user['username'] == username)

    def get_users(self):
        return self.db.all()

    def clear(self):
        self.db.drop_tables()
