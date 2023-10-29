from utils import prompts, sql_query
from controllers.authentication import Authentication
from helpers import input_helper
from models.database import get_item
from controllers.user import Admin, Visitor, Librarian

from utils.exceptions import UserDoesNotExist


def home():
    while True:
        choice = input(prompts.HOME)
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            exit(0)
        else:
            print("Enter a valid choice!")


def signup():
    print("---------------SIGN UP---------------")
    visitor_info = input_helper.get_visitor_details()
    visitor = Authentication(*visitor_info)
    visitor.signup()


def login():
    print("---------------SIGN IN---------------")
    username = input("Enter the username: ")
    password = input(f"Enter the password for `{username}: ")
    role = get_item(sql_query.GET_USER_ROLE, (username,))
    try:
        if role is None:
            raise UserDoesNotExist(username)
    except UserDoesNotExist as user_error:
        print(user_error)

    role = role[0]
    user = Authentication(username, password, role)
    if role == 'admin':
        admin = Admin(username, password, role)
        admin_menu(admin)
    elif role == 'visitor':
        visitor = Visitor(username, password, role)
    elif role == 'librarian':
        pass
    user.login()


def admin_menu(admin):
    pass


def user_menu(admin):
    pass


def librarian_menu(admin):
    pass
