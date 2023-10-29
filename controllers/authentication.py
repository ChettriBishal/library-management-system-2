from bcrypt import checkpw

from utils import sql_query
from models.database import get_item


class Authentication:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def _check_password(self, hashed_password):
        if checkpw(self.password, hashed_password):
            return True
        return False

    def login(self):
        check_user = get_item(sql_query.GET_USER_BY_USERNAME, (self.username,))
        if check_user is None:
            print(f"User with username `{self.username}` does not exist!")
        else:
            stored_hashed_password = check_user[2]

            if self._check_password(stored_hashed_password):
                print(f"Logged in as `{self.role}` successfully!!")
                return check_user
            else:
                return None

    def signup(self):
        pass
