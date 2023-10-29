from utils import sql_query
from controllers.authentication import Authentication
from models.database import get_many_items, get_item, remove_item


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def user_details(self):
        return f"Username: {self.username} | Role: {self.role}"


class Admin(User):
    def register_librarian(self, username, password, user_role="librarian"):
        new_librarian = Authentication(username, password, user_role)
        new_librarian.signup()
        print("-----------------------------")
        print(f"Librarian with username `{username}` registered successfully!")

    def list_users(self):
        response = get_many_items(sql_query.GET_ALL_USERS, None)
        users = [User(*user) for user in response]
        for user in users:
            print(user.user_details())

    def remove_user(self, username):
        check_user = get_item(sql_query.GET_USER_BY_USERNAME, (username,))
        print(check_user)
        if check_user is None:
            print(f"User with username `{username} does not exist!")
        else:
            remove_item(sql_query.REMOVE_USER, (username,))
            print(f"{username} successfully removed!!!")


class Librarian(User):
    pass


class Visitor(User):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)
    

