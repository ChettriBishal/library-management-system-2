import os
from bcrypt import checkpw, hashpw, gensalt
from src.config import sql_query
from src.models.database import get_item, insert_item
from src.utils.uuid_generator import generate_uuid
from src.utils.logs import Log


class Authentication:
    log_obj = Log(os.path.basename(__file__))

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def _check_password(self, hashed_password):
        if checkpw(self.password.encode('utf8'), hashed_password):
            return True
        return False

    def _hash_password(self):
        salt = gensalt()
        hashed_password = hashpw(self.password.encode('utf-8'), salt)
        return hashed_password

    def login(self):
        check_user = get_item(sql_query.GET_USER_BY_USERNAME,
                              (self.username, ))
        if check_user is None:
            print(f"User with username `{self.username}` does not exist!")
        else:
            stored_hashed_password = check_user[2]

            if self._check_password(stored_hashed_password):
                print(f"Logged in as `{self.role}` successfully!!")
                self.log_obj.logger.info(f"{self.username} logged in")
                return check_user
            else:
                self.log_obj.logger.info(
                    f"{self.username} entered wrong password")
                return None

    def signup(self):
        check_user = get_item(sql_query.GET_USER_BY_USERNAME,
                              (self.username, ))
        if check_user:
            print(f"Choose a different username!")
            return None
        else:
            hashed_password = self._hash_password()
            user_info = (
                generate_uuid(),
                self.username,
                hashed_password,
                self.role,
            )
            insert_item(sql_query.ADD_USER, user_info)
            self.log_obj.logger.info(f"{self.username} has signed up")
            return user_info[0] # return the uuid
