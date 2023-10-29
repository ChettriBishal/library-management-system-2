from utils import prompts, sql_query
from controllers.authentication import Authentication
from helpers import input_helper
from models.database import get_item
from controllers.user import Admin, Visitor, Librarian
from controllers.book import Book

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
    if user.login() is None:
        print("Wrong password! Please try again")
        return

    if role == 'admin':
        admin = Admin(username, password, role)
        admin_menu(admin)
    elif role == 'visitor':
        visitor = Visitor(username, password, role)
        visitor_menu(visitor)
    elif role == 'librarian':
        librarian = Librarian(username,password,role)
        librarian_menu(librarian)


def admin_menu(admin):
    while True:
        choice = input(prompts.ADMIN_MENU)
        if choice == '1':
            admin.register_librarian()
        elif choice == '2':
            admin.list_users()
        elif choice == '3':
            admin.remove_user()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


def visitor_menu(visitor):
    while True:
        choice = input(prompts.VISITOR_MENU)

        if choice == '1':
            bookname = input("\nEnter the name of the book to query: ")
            response = visitor.query_book(bookname)
            if response is None:
                print(f"No book with name {bookname} found!")
            else:
                book_cnt = get_item(sql_query.NO_OF_BOOKS_OF_SAME_NAME,(bookname,))
                print(f"Number of copies of `{bookname}`: {book_cnt}")
        elif choice == '2':
            visitor.sort_books_by_rating()
        elif choice == '3':
            visitor.sort_books_by_price()
        elif choice == '4':
            genre = input("\nEnter the genre whose books you want to see: ")
            visitor.group_books_by_genre(genre)
        elif choice == '5':
            bookname = input("\nEnter the name of the book to issue: ")
            visitor.issue_book(bookname)

        elif choice == '6':

        elif choice == '7':

        elif choice == '8':


        elif choice == '9':
            break
        else:
            print("Invalid choice!")


def librarian_menu(admin):
    pass
